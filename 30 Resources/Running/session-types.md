---
classification: internal
status: confirmed by David 29 Sep 2026, v1.2 (tuned on dev batch 01, D25). Tested only on held-out batches
updated: 2026-09-29
---
# Session types: classification rubric

The rubric the golden dataset (T3.1) is labelled against. Zones: [[athlete-baseline]].
Two independent axes, scored separately. Only runs (Run, TrailRun) are classified.
Hikes, walks and rides count toward weekly load and get no type.

## Axis 1 · Terrain (applied in order; first match wins)
1. **[T1]** ≥50 m climbing per km → **mountain**, whatever the shoes (e.g. 11 Aug 2026: road shoes, 71 m/km of 17–27% hill reps = mountain for David)
2. **[T2]** Road shoes (28636543, 21087212) → **road**
3. **[T3]** Trail shoes (25832441) → **trail**
4. **[T4]** No gear recorded: 15–50 m/km → trail · <15 → road
Strava's sport_type is **not** used; it's unreliable.

## Axis 2 · Intent (applied in order; first match wins)
| Intent | Rule |
|---|---|
| **[I1]** race | Named event (race name in title or description). DNFs count. Unnamed hard efforts are **not** race |
| **[I2]** hills | **Structured climb repeats:** ≥3 climb/descend cycles on the same or similar climb, HR reaching Z4+ on the climbs and dropping on the descents. Checked before intervals: it's the more specific pattern |
| **[I3]** intervals | Work/rest alternation, ≥3 reps, detected from pace/HR in the data (don't rely on manual laps), or reps in a Runna description |
| **[I4]** tempo | ≥15 min continuous in Z3–Z4 (149–165), not in reps. **Wins over duration:** a long run with a sustained hard block or a progression finish is tempo |
| **[I5]** long | Road ≥75 min · trail/mountain ≥2 h. **Runna's "Long Run" label is ignored** (Runna applies it to 47-min runs) |
| **[I6]** recovery | (a) ≤45 min and average HR ≤140 (Z1), **or** (b) average HR ≤148 (Z1–Z2) within 14 days after a race. Needs recent race dates as context |
| **[I7]** easy | Average HR ≤148 (Z1–Z2), no rule above matched |
| **[I8]** unsure | Nothing above matched, or no HR on trail/mountain. Goes to David and counts toward the 10% exception budget |

**Hills vs a hilly run** (delegated to Claude, 29 Sep): a continuous run over rolling or hilly ground is **not** "hills".
It's classified by its effort; the hilliness shows up in the terrain axis. "Hills" means deliberate repeats only.

**Tuesday-evening trail runs** (David, 29 Sep): usually intervals, sometimes endurance.

## Known edge cases (seed rows for T3.1)
- Tuesday trail intervals without manual laps: structure has to be detected from the pace/HR streams.
- 25 Sep 2026 "9km Long Run": Runna calls it long; David calls it recovery (6 days after the Dents du Midi). Resolved by v1.2 (I5 ignores the label, I6b post-race window).
- 11 Aug 2026 "Evening Run": road shoes, 478 m in 6.8 km. David: mountain × hills. Resolved by v1.2 (T1 climbing first, I2 hills before intervals).
- 8 Nov 2025 Runna long run with tempo blocks. David: trail × tempo. v1.1's long-before-tempo (D21) was wrong; reverted in v1.2.
- 18 Aug 2026 pyramid: HR artifact of 179 during the warm-up.
- 15 Nov 2025 Yvoir half trail, DNF. Still counts as race.
- A race run at training effort (e.g. a controlled Gelbressoise 20 km before Haversin): the rule says race, but the effort says long. Decide at T3.1 labelling.
