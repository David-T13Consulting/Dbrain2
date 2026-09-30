#!/usr/bin/env python3
"""Deterministic numbers for the weekly-assessment skill. The model never does this arithmetic.

Usage: python3 compute_week.py <input.json> [--vault <path to Dbrain2>]
Input: {"week_start": "YYYY-MM-DD" (a Monday),
        "activities": [ {id, start_local, sport_type, moving_time_s, distance_m, elevation_gain_m,
                         avg_hr?, terrain?, intent?, hr_stream?: {"time": [...s], "heartrate": [...bpm]}} ]}
        covering the target week plus the lookback weeks before it.
Output: one JSON object on stdout. Exits non-zero if the reference notes can't be parsed.
"""
import json, re, sys, os
from datetime import date, datetime, timedelta

RUNS = {"Run", "TrailRun"}

def vault_root(argv):
    if "--vault" in argv:
        return argv[argv.index("--vault") + 1]
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

def read_zones(vault, on_date):
    """Zone upper bounds (Z1..Z4) in effect on on_date, from the dated table in athlete-baseline.md.
    Returns (uppers, effective_from, assumed) where assumed=True if on_date predates every row."""
    p = os.path.join(vault, "20 Areas/Running/athlete-baseline.md")
    txt = open(p, encoding="utf-8").read()
    rows = []
    for m in re.finditer(r"^\|\s*(\d{4}-\d{2}-\d{2})\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|", txt, re.M):
        eff = date.fromisoformat(m.group(1))
        uppers = [int(m.group(i)) for i in (3, 4, 5, 6)]
        if uppers != sorted(uppers):
            sys.exit(f"ERROR: zone bounds not increasing in row {eff}")
        rows.append((eff, uppers))
    if not rows:
        sys.exit("ERROR: cannot parse the dated zone table in athlete-baseline.md")
    rows.sort()
    valid = [r for r in rows if r[0] <= on_date]
    eff, uppers = valid[-1] if valid else rows[0]
    return uppers, str(eff), not valid

def read_flags(vault):
    p = os.path.join(vault, "30 Resources/Running/weekly-flags.md")
    fm = open(p, encoding="utf-8").read().split("---")[1]
    cfg = {}
    for key in ("load_change_pct", "min_easy_share_pct", "lookback_weeks"):
        m = re.search(rf"^{key}:\s*(\d+)\s*$", fm, re.M)
        if not m:
            sys.exit(f"ERROR: missing {key} in weekly-flags.md frontmatter")
        cfg[key] = int(m.group(1))
    return cfg

def zone_of(hr, uppers):
    for i, u in enumerate(uppers):
        if hr <= u:
            return i + 1
    return 5

def local_date(a):
    return datetime.fromisoformat(a["start_local"]).date()

def zone_seconds(a, uppers):
    """Returns (seconds per zone dict, covered_seconds, method)."""
    s = a.get("hr_stream")
    secs = {z: 0.0 for z in range(1, 6)}
    if s and s.get("time") and s.get("heartrate") and len(s["time"]) == len(s["heartrate"]):
        t, hr = s["time"], s["heartrate"]
        for i in range(1, len(t)):
            dt = t[i] - t[i - 1]
            if 0 < dt <= 30:  # ignore pauses/gaps
                secs[zone_of(hr[i], uppers)] += dt
        return secs, sum(secs.values()), "stream"
    if a.get("avg_hr"):
        secs[zone_of(a["avg_hr"], uppers)] = a["moving_time_s"]
        return secs, a["moving_time_s"], "avg_hr_estimate"
    return secs, 0, "no_hr"

def main():
    argv = sys.argv[1:]
    data = json.load(open(argv[0], encoding="utf-8"))
    vault = vault_root(argv)
    cfg = read_flags(vault)
    ws = date.fromisoformat(data["week_start"])
    uppers, zones_from, zones_assumed = read_zones(vault, ws)
    if ws.weekday() != 0:
        sys.exit("ERROR: week_start must be a Monday")
    we = ws + timedelta(days=6)
    acts = data["activities"]
    week = [a for a in acts if ws <= local_date(a) <= we]
    runs = [a for a in week if a["sport_type"] in RUNS]
    other = [a for a in week if a["sport_type"] not in RUNS]

    def mins(xs): return round(sum(a["moving_time_s"] for a in xs) / 60, 1)

    # lookback load
    prior = []
    for k in range(1, cfg["lookback_weeks"] + 1):
        s0 = ws - timedelta(days=7 * k); s1 = s0 + timedelta(days=6)
        prior.append(sum(a["moving_time_s"] for a in acts if s0 <= local_date(a) <= s1) / 60)
    import statistics
    prior_avg = round(statistics.median(prior), 1)  # median: one big race week cannot distort the baseline (D23)
    total = mins(week)
    delta_pct = round((total - prior_avg) / prior_avg * 100, 1) if prior_avg else None

    # zones
    zsum = {z: 0.0 for z in range(1, 6)}; covered = 0.0; methods = {}
    for a in runs:
        s, c, m = zone_seconds(a, uppers)
        for z in zsum: zsum[z] += s[z]
        covered += c; methods[a["id"]] = m
    run_secs = sum(a["moving_time_s"] for a in runs)
    pct = lambda x: round(x / covered * 100, 1) if covered else None
    easy_share = pct(zsum[1] + zsum[2])

    # week type
    intents = [a.get("intent") for a in runs]
    race_week = "race" in intents
    post_race = any(a.get("intent") == "race" and ws - timedelta(days=7) <= local_date(a) < ws for a in acts)
    week_type = "race" if race_week else "post-race" if post_race else "normal"
    exempt = week_type in ("race", "post-race")

    flags = []
    f1 = delta_pct is not None and abs(delta_pct) > cfg["load_change_pct"]
    if f1 and week_type == "post-race" and delta_pct < 0: f1 = False
    flags.append({"id": "F1", "name": "load-change", "fired": f1, "value": delta_pct, "threshold": cfg["load_change_pct"]})
    f2 = easy_share is not None and easy_share < cfg["min_easy_share_pct"]
    flags.append({"id": "F2", "name": "intensity", "fired": f2, "value": easy_share, "threshold": cfg["min_easy_share_pct"],
                  "evaluable": easy_share is not None})
    flags.append({"id": "F3", "name": "no-quality", "fired": (not exempt) and not any(i in ("intervals", "hills", "tempo") for i in intents)})
    flags.append({"id": "F4", "name": "no-long", "fired": (not exempt) and "long" not in intents})

    out = {
        "week": f"{ws}..{we}", "week_type": week_type,
        "load": {"total_moving_min": total, "run_moving_min": mins(runs), "other_moving_min": mins(other),
                 "run_distance_km": round(sum(a["distance_m"] for a in runs) / 1000, 1),
                 "run_elevation_m": round(sum(a["elevation_gain_m"] for a in runs)),
                 "runs": len(runs), "other_sessions": len(other)},
        "trend": {"prior_weeks_moving_min": [round(x, 1) for x in prior], "prior_median_min": prior_avg, "delta_pct": delta_pct},
        "intensity": {"z1_z2_pct": easy_share, "z3_pct": pct(zsum[3]), "z4_z5_pct": pct(zsum[4] + zsum[5]),
                      "hr_coverage_pct": round(covered / run_secs * 100, 1) if run_secs else None, "method_per_run": methods},
        "sessions": [{"id": a["id"], "date": str(local_date(a)), "terrain": a.get("terrain"), "intent": a.get("intent")} for a in runs],
        "unclassified_or_unsure": [a["id"] for a in runs if a.get("intent") in (None, "unsure")],
        "flags": flags,
        "zone_upper_bounds_used": uppers, "zones_effective_from": zones_from, "zones_assumed": zones_assumed, "flag_config_used": cfg,
    }
    print(json.dumps(out, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
