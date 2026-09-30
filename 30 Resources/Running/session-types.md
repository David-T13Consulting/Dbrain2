---
classification: internal
status: v1.3 drafted 30 Sep 2026 from David's decisions D27–D32 (tuned on dev batches 01 + 02). Tested only on held-out batches, from batch 03
updated: 2026-09-30
---
# Session types: classification rubric

The rubric the golden dataset (T3.1) is labelled against. Zones and target paces: [[athlete-baseline]].
Each run gets **two axes and two flags**, scored separately:
- **Terrain** (the surface): road | trail | mountain
- **Intent** (the main label): race | hills | intervals | long | tempo | recovery | easy | unsure
- **`tempo_block`** flag: the run contains race-pace work, whatever its main label (D28)
- **`vertical`** flag: the run contains steep climbing work, whatever its terrain (D31)

## Axis 0 · Is it a run? (D30)
Only runs are classified. Hikes, walks and rides count toward weekly load and get `load-only`.
- `sport_type` isn't Run or TrailRun → load-only
- Name says it's a hike or walk ("Hike", "Walk", "Randonnée", "Marche") → load-only, whatever the sport_type (e.g. 21 Jul 2026 "Morning Hike" logged as TrailRun)
- Pace slower than 10:00/km **and** average HR ≤140 **and** climbing <50 m/km → load-only (the climbing condition keeps slow mountain runs in, e.g. Tignes 17 Jul 2026 at 10:15/km)

## Axis 1 · Terrain = the surface (applied in order; first match wins)
1. **[T1]** ≥50 m climbing per km → **mountain**, whatever the shoes
2. **[T2]** Road shoes → **road**
3. **[T3]** Trail shoes → **trail**
4. **[T4]** No gear, or gear not in the shoe list (D30): 15–50 m/km → trail · <15 → road
Strava's sport_type is **not** used for terrain; it's unreliable.
Namur Tiennes and Citadelle repeats are **not** mountain terrain: they're road or trail with the `vertical` flag (D31).

## Axis 2 · Intent (applied in order; first match wins)
| Intent | Rule |
|---|---|
| **[I1]** race | Named event (race name in title or description). DNFs count. Unnamed hard efforts are **not** race |
| **[I2]** hills | **Structured climb repeats:** ≥3 climb/descend cycles on the same or similar climb, HR reaching Z4+ on the climbs and dropping on the descents. Checked before intervals |
| **[I3]** intervals | Work/rest alternation, ≥3 reps, detected from pace/HR in the data (don't rely on manual laps), or reps in a Runna description |
| **[I4]** long | Road ≥75 min · trail/mountain ≥2 h. **Duration wins over tempo** (D28): a long run with race-pace work is `long` + `tempo_block`. Runna's "Long Run" label is ignored |
| **[I5]** tempo | Not long, and a **tempo block** exists (definition below) |
| **[I6]** recovery | Average HR ≤156 (Z1–Z3) **and** within the post-race window: 7 days after a race up to 21 km, 14 days after a marathon, ultra or mountain race (D27). Needs recent race dates as context. Never used outside that window |
| **[I7]** easy | Average HR ≤156 (Z1–Z3), no rule above matched |
| **[I8]** unsure | Nothing above matched, or no HR on trail/mountain where it's needed. Goes to David and counts toward the 10% exception budget |

## Flag · `tempo_block` (D28, D29, D32)
**≥15 min continuous at race effort, not in reps** (reps with rest are intervals). Race effort means:
- **Flat road:** pace ≤5:10/km (David's target marathon pace or faster; half ~4:40, 5–10 km a little faster). Strict: David's easy runs sit at 5:15–5:20
- **Trail, mountain, or a sustained climb** (where pace means nothing): HR ≥157 (Z4+)
- **Or** a Runna description that prescribes race-pace blocks (e.g. 8 Nov 2025: 6 km @4:50, 2 km @4:25, 4 km @4:50)
Set on any run. On a non-long run it makes the main intent `tempo`.

## Flag · `vertical` (D31)
Steep climbing work, the "mountain simulation" David does on Namur Tiennes and the Citadelle:
- the steepest 200 m of climbing averages **≥15%**, **or**
- **≥2 separate climbs** of ≥30 m gain each at **≥8%** average
Needs the altitude stream; without it the flag is `null`, not `false`. Thresholds are Claude's proposal from 7 runs, untested; GPS altitude noise is about ±2 points near 8%.

## Worked context
- **Hills vs a hilly run:** a continuous run over hilly ground is not `hills`. It gets its intent from effort and may carry `vertical`.
- **Tuesday-evening trail runs** (David, 29 Sep): usually intervals, sometimes endurance.

## Known edge cases (seed rows for T3.1)
- Tuesday trail intervals without manual laps: structure has to be detected from the pace/HR streams.
- 25 Sep 2026 "9km Long Run": Runna calls it long; David calls it recovery (6 days after the Dents du Midi). I4 ignores the label; I6 post-race window.
- 11 Aug 2026 "Evening Run": road shoes, 478 m in 6.8 km of 17–27% reps. David: mountain × hills (T1, I2).
- 8 Nov 2025 Runna long run with tempo blocks: trail, 1:44 <2 h → tempo via the Runna description.
- 23 Aug 2026 18 km, 3 × 6 km progression (HR 137 → 158): David labelled tempo; v1.3 says long + tempo_block. The one known dev miss under D28.
- 21 Aug 2026 Ostend: HR flat at 88 for the first 2.2 km. A flatlined HR is a sensor fault, not an effort.
- 18 Aug 2026 pyramid: HR artifact of 179 during the warm-up.
- 15 Nov 2025 Yvoir half trail, DNF. Still counts as race.
- A race run at training effort (e.g. a controlled Gelbressoise 20 km before Haversin): the rule says race, but the effort says long. Decide at labelling.

## Version history
- **v1.3** (30 Sep 2026): recovery post-race only (D27); two labels, duration-first + `tempo_block` (D28); tempo = target race pace on flat, HR Z4 off-road (D29, D32); hikes excluded, unknown gear = no gear (D30); terrain = surface + `vertical` flag (D31); easy ceiling raised from 148 to 156. From batch 02, where v1.2 scored 85% / 50% held-out.
- **v1.2** (29 Sep 2026): tuned on batch 01 (D25).
