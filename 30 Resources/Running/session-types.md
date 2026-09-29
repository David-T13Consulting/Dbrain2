---
classification: internal
status: confirmed by David 29 Sep 2026 (v1; thresholds get tested against the golden dataset at T3.1)
updated: 2026-09-29
---
# Session types: classification rubric

The rubric the golden dataset (T3.1) is labelled against. Zones: [[athlete-baseline]].
Two independent axes, scored separately. Only runs (Run, TrailRun) are classified.
Hikes, walks and rides count toward weekly load and get no type.

## Axis 1 · Terrain (applied in order; first match wins)
1. **[T1]** Road shoes (28636543, 21087212) → **road**, whatever the climbing (e.g. 11 Aug 2026: 71 m/km of hill work on road)
2. **[T2]** Trail shoes (25832441) and ≥50 m climbing per km → **mountain**
3. **[T3]** Trail shoes → **trail**
4. **[T4]** No gear recorded: ≥50 m/km → mountain · 15–50 → trail · <15 → road
Strava's sport_type is **not** used; it's unreliable (e.g. 8 Nov 2025 Runna long run tagged TrailRun).

## Axis 2 · Intent (applied in order; first match wins)
| Intent (first match wins) | Rule |
|---|---|
| **[I1]** race | Named event (race name in title or description), or a race-effort HR profile. DNFs count |
| **[I2]** intervals | Work/rest alternation, ≥3 reps, detected from pace/HR in the data (don't rely on manual laps), or reps in a Runna description |
| **[I3]** hills | **Structured climb repeats:** ≥3 climb/descend cycles on the same or similar climb, HR reaching Z4+ on the climbs and dropping on the descents |
| **[I4]** tempo | ≥15 min continuous in Z3–Z4 (149–165), not in reps |
| **[I5]** long | Road ≥75 min · trail/mountain ≥2 h · or labelled "Long Run" by Runna |
| **[I6]** recovery | ≤45 min and average HR ≤140 (Z1) |
| **[I7]** easy | Everything else with average HR ≤148 (Z1–Z2) |

**Hills vs a hilly run** (delegated to Claude, 29 Sep): a continuous run over rolling or hilly ground is **not** "hills".
It's classified by its effort (easy, long, tempo), and the hilliness is captured by the terrain axis. "Hills" means
deliberate repeats only. That keeps the two axes independent.

**Tuesday-evening trail runs** (David, 29 Sep): usually intervals, sometimes endurance. Expect trail × intervals
most weeks and trail × easy/long otherwise. Trail intervals on a slope can look like hills; the difference is
whether the reps are timed or distance-based efforts (intervals) or climbs (hills).

## Known edge cases (seed rows for T3.1)
- Tuesday trail intervals without manual laps: structure has to be detected from the pace/HR streams.
- 25 Sep 2026 "9km Long Run": Runna calls it long, but it's 47 min. Plan label vs metrics.
- 11 Aug 2026 "Evening Run": road shoes, 478 m climbing in 6.8 km. Road × hills?
- 8 Nov 2025 Runna long run with tempo blocks, trail shoes, 28 m/km. Long or tempo? Trail or road?
- 18 Aug 2026 pyramid: HR artifact of 179 during the warm-up.
- 15 Nov 2025 Yvoir half trail, DNF. Still counts as race.
- A race run at training effort (e.g. a controlled Gelbressoise 20 km before Haversin): the rule says race, but the effort says long. Decide at T3.1 labelling.
