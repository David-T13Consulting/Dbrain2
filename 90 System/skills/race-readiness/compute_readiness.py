#!/usr/bin/env python3
"""Deterministic readiness features + predicted time. The model never does this arithmetic.

Usage: python3 compute_readiness.py <input.json> [--vault <path to Dbrain2>]
Input: {"as_of": "YYYY-MM-DD",
        "race": {"name", "date", "terrain": "road|trail|mountain", "distance_km", "elevation_m"},
        "activities": [ {id, name, description?, start_local, sport_type, moving_time_s, elapsed_time_s,
                         distance_m, elevation_gain_m, terrain?, intent?} ]}   # ~12 months of history
Output: one JSON object on stdout.
"""
import json, os, re, sys, statistics
from datetime import date, datetime, timedelta

RUNS = {"Run", "TrailRun"}

def vault_root(argv):
    if "--vault" in argv: return argv[argv.index("--vault") + 1]
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

def read_cfg(vault):
    fm = open(os.path.join(vault, "30 Resources/Running/readiness-rules.md"), encoding="utf-8").read().split("---")[1]
    cfg = {k: int(v) for k, v in re.findall(r"^(\w+):\s*(\d+)\s*$", fm, re.M)}
    need = ["lookahead_weeks","endurance_lookback_weeks","terrain_lookback_weeks","endurance_ok_ratio_x100",
            "endurance_borderline_ratio_x100","climb_ok_ratio_x100","climb_borderline_ratio_x100",
            "recovery_km_effort_per_day_x10","reference_max_age_days","reference_min_ratio_x100",
            "reference_max_ratio_x100","riegel_exponent_x100","range_road_pct","range_trail_pct"]
    miss = [k for k in need if k not in cfg]
    if miss: sys.exit(f"ERROR: readiness-rules.md frontmatter missing {miss}")
    return cfg

d_ = lambda a: datetime.fromisoformat(a["start_local"]).date()
km_effort = lambda km, elev: km + elev / 100
family = lambda t: "road" if t == "road" else "offroad"
def band(x, ok, bl):
    return None if x is None else "ok" if x >= ok else "borderline" if x >= bl else "not"
def hms(sec):
    sec = int(round(sec)); return f"{sec//3600}:{sec%3600//60:02d}:{sec%60:02d}"

def main():
    argv = sys.argv[1:]; data = json.load(open(argv[0], encoding="utf-8")); cfg = read_cfg(vault_root(argv))
    as_of = date.fromisoformat(data["as_of"]); race = data["race"]; rd = date.fromisoformat(race["date"])
    days_to = (rd - as_of).days
    if days_to < 0 or days_to > cfg["lookahead_weeks"] * 7:
        print(json.dumps({"race": race["name"], "in_window": False, "days_to_race": days_to})); return
    acts = [a for a in data["activities"] if d_(a) <= as_of]
    runs = [a for a in acts if a["sport_type"] in RUNS]
    offroad = race["terrain"] != "road"
    race_dist = km_effort(race["distance_km"], race["elevation_m"]) if offroad else race["distance_km"]

    # C4 reference race + Riegel
    ref = None
    for a in sorted(runs, key=d_, reverse=True):
        if a.get("intent") != "race" or "dnf" in (a.get("description", "") + " " + a.get("name", "")).lower(): continue
        if (as_of - d_(a)).days > cfg["reference_max_age_days"]: continue
        if family(a.get("terrain")) != family(race["terrain"]): continue
        a_dist = km_effort(a["distance_m"]/1000, a["elevation_gain_m"]) if offroad else a["distance_m"]/1000
        r = race_dist / a_dist
        if cfg["reference_min_ratio_x100"]/100 <= r <= cfg["reference_max_ratio_x100"]/100:
            ref = (a, a_dist); break
    pred = None
    if ref:
        a, a_dist = ref
        t = a["elapsed_time_s"] * (race_dist / a_dist) ** (cfg["riegel_exponent_x100"]/100)
        pct = (cfg["range_trail_pct"] if offroad else cfg["range_road_pct"]) / 100
        pred = {"mid": hms(t), "low": hms(t*(1-pct)), "high": hms(t*(1+pct)), "mid_s": round(t), "range_pct": pct*100,
                "reference": {"id": a["id"], "name": a["name"], "date": str(d_(a)), "elapsed": hms(a["elapsed_time_s"]),
                              "distance_basis": round(a_dist, 1)}}

    # C1 endurance
    since = as_of - timedelta(weeks=cfg["endurance_lookback_weeks"])
    recent = [a for a in runs if d_(a) > since]
    longest = max(recent, key=lambda a: a["moving_time_s"], default=None)
    target_s = pred["mid_s"] if pred else race_dist * 6 * 60
    c1_ratio = round(longest["moving_time_s"] / target_s, 2) if longest else 0.0
    c1 = {"longest_run": {"id": longest["id"], "date": str(d_(longest)), "moving": hms(longest["moving_time_s"])} if longest else None,
          "target_duration": hms(target_s), "target_basis": "predicted time" if pred else "km-effort x 6 min",
          "ratio": c1_ratio, "band": band(c1_ratio, cfg["endurance_ok_ratio_x100"]/100, cfg["endurance_borderline_ratio_x100"]/100)}

    # C2 terrain specificity
    if offroad:
        weeks = []
        for k in range(cfg["terrain_lookback_weeks"]):
            e1 = as_of - timedelta(days=7*k); e0 = e1 - timedelta(days=6)
            weeks.append(sum(a["elevation_gain_m"] for a in runs if e0 <= d_(a) <= e1))
        med = statistics.median(weeks); r2 = round(med / race["elevation_m"], 2) if race["elevation_m"] else None
        c2 = {"weekly_climb_m_last_weeks": [round(w) for w in weeks], "median_weekly_climb_m": round(med), "race_climb_m": race["elevation_m"],
              "ratio": r2, "band": band(r2, cfg["climb_ok_ratio_x100"]/100, cfg["climb_borderline_ratio_x100"]/100)}
    else:
        c2 = {"band": "n/a", "reason": "road race"}

    # C3 recovery
    worst = None
    for a in runs:
        if (as_of - d_(a)).days > 90: continue
        if a.get("intent") != "race" and a["moving_time_s"] < 3*3600: continue
        ke = km_effort(a["distance_m"]/1000, a["elevation_gain_m"])
        need = ke / (cfg["recovery_km_effort_per_day_x10"]/10)
        r3 = round((rd - d_(a)).days / need, 2)
        if worst is None or r3 < worst["ratio"]:
            worst = {"effort": {"id": a["id"], "name": a["name"], "date": str(d_(a)), "km_effort": round(ke, 1)},
                     "days_between": (rd - d_(a)).days, "days_needed_heuristic": round(need), "ratio": r3}
    c3 = dict(worst or {"ratio": None}, band=band(worst["ratio"], 1.0, 0.5) if worst else "ok")

    c4 = {"band": "found" if ref else "none"}
    out = {"race": race["name"], "race_date": race["date"], "in_window": True, "days_to_race": days_to,
           "race_distance_basis": round(race_dist, 1), "distance_unit": "km-effort" if offroad else "km",
           "C1_endurance": c1, "C2_terrain": c2, "C3_recovery": c3, "C4_reference": c4,
           "predicted_time": pred if pred else {"withheld": True, "reason": "no comparable finished race"},
           "config_used": cfg}
    print(json.dumps(out, ensure_ascii=False, indent=1))

if __name__ == "__main__":
    main()
