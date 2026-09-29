---
classification: internal
status: DRAFT (axes confirmed by David 29 Sep 2026; thresholds proposed by Claude, pending David's confirmation)
updated: 2026-09-29
---
# Session types: classification rubric

The rubric the golden dataset (T3.1) is labelled against. Zones: [[athlete-baseline]].
Two independent axes, scored separately. Only runs (Run, TrailRun) are classified.
Hikes, walks and rides count toward weekly load and get no type.

## Axis 1 · Terrain (applied in order; first match wins)
1. Road shoes (28636543, 21087212) → **road**, whatever the climbing (e.g. 11 Aug 2026: 71 m/km of hill work on road)
2. Trail shoes (25832441) and ≥50 m climbing per km → **mountain**
3. Trail shoes → **trail**
4. No gear recorded: ≥50 m/km → mountain · 15–50 → trail · <15 → road
Strava's sport_type is **not** used; it's unreliable (e.g. 8 Nov 2025 Runna long run tagged TrailRun).

## Axis 2 · Intent (applied in order; first match wins)
| Intent | Proposed rule | ⚠️ To confirm |
|---|---|---|
| race | Named event (race name in title or description), or a race-effort HR profile | Are Tuesday group runs ever "race"? |
| intervals | Laps alternate work and rest (≥3 reps), or a Runna description with reps | — |
| hills | Repeated climbs: ≥3 climb/descend cycles, with HR peaking in Z4+ on the climbs | Road hill repeats vs a hilly trail run: where's the line? |
| tempo | ≥15 min continuous in Z3–Z4 (149–165), not in reps | — |
| long | Road ≥75 min · trail/mountain ≥2 h · or labelled "Long Run" by Runna | Duration-based, or "longest run of the week"? |
| recovery | ≤45 min and average HR ≤140 (Z1) | — |
| easy | Everything else with average HR ≤148 (Z1–Z2) | — |

## Known edge cases (seed rows for T3.1)
- 25 Sep 2026 "9km Long Run": Runna calls it long, but it's 47 min. Plan label vs metrics.
- 11 Aug 2026 "Evening Run": road shoes, 478 m climbing in 6.8 km. Road × hills?
- 8 Nov 2025 Runna long run with tempo blocks, trail shoes, 28 m/km. Long or tempo? Trail or road?
- 18 Aug 2026 pyramid: HR artifact of 179 during the warm-up.
- 15 Nov 2025 Yvoir half trail, DNF. Still counts as race.
