---
classification: internal
status: HELD-OUT batch (test set, D25). Prepared by Claude 30 Sep 2026, blind: facts only, no skill predictions. Labelled by David 30 Sep 2026 (one run per screen). Scores rubric v1.3 / classify-session v0.4.
---
# Golden dataset: labelling batch 03 (held-out, 20 runs)

**Sampling:** rows 21–40 of `heldout-order.md` (seed 20260930). Nothing hand-picked.
**Shoes:** road = 28636543 / 21087212 · trail = 25832441 · unlisted = gear not in the baseline.
**Context** = a named event within 14 days before or after the run.
**New in this batch:** two flags labelled for every run. `tempo_block` = the run contains ≥15 min at race effort. `vertical` = the run contains steep climbing work (Tiennes / Citadelle type). Terrain is the surface; mountain only for real mountains (D31).
Climb figures: gain / horizontal distance of named Strava segments (approximate).

| # | Strava id | Date | Name | Shoes | km | Moving | Climb m (m/km) | Avg HR | Structure seen in data | Context | Terrain | Intent | tempo_block | vertical | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 16853059708 | Sat 27 Dec 2025 | Morning Run | road | 21.1 | 1:50:23 | 74 (4) | 152 | Laps 5.0 km @5:10 · 3.0 @5:13 · 3.0 @5:02 · 5.0 @5:17 · 3.0 @5:16 · 2.1 @5:25; HR 149–154 throughout. One 32 m climb at 9% | – | road | long | yes | no | Relabelled 30 Sep: was intervals, David "most likely misclick" (D38) |
| 2 | 15278687605 | Tue 29 Jul 2025 | Evening Run (Profondeville) | trail | 7.5 | 1:35:37 | 908 (121) | 157 | Repeated climbs: Montée Rivière ×3 (84 m, 26%), Rivage Sart ×4 (92 m, 24%), TSY1 ×4 (124 m, 23%), Couleuvrine ×3 (143 m, 27%), Piwi's Up ×4 (129 m, 21%). HR 156–167 up, 140–150 down | – | trail | hills | no | yes | |
| 3 | 13563521926 | Tue 4 Feb 2025 | Evening Run (Jambes track) | road | 13.1 | 1:09:38 | 75 (6) | 148 | 4.6 km @5:42 (HR 135) · 0.83 @4:33 · 0.41 @4:01 · 1.03 @4:10 · 0.62 @4:08 · 0.41 @4:03 · 1.01 @4:14 (HR 158–165), ~200 m easy between · 3.1 km @5:57 | – | road | intervals | no | no | |
| 4 | 17592917374 | Tue 3 Mar 2026 | Evening Run | road | 13.0 | 1:07:16 | 6 (0) | 152 | 2.5 km @5:29 (HR 138) · then 3.8 km continuous @4:42–4:59 (~18 min, HR 156–162) · 6.7 km @5:16 (HR 153) | – | road | tempo | yes | no | |
| 5 | 18573247540 | Tue 19 May 2026 | Evening Run | road | 10.4 | 58:10 | 281 (27) | 151 | 2.6 km downhill (HR 138) · 20 × (30 s @~4:20 / 30 s @~6:15) up the Citadelle (Av. Jean Ier, 126 m over 1.9 km, ~7%), HR 157→177 · 1.2 km down · same 20 × 30/30 again, HR 157→181 · 2.8 km home. Steepest bit ~11% over 240 m | – | road | hills | yes | yes | |
| 6 | 17362588733 | Tue 10 Feb 2026 | Evening Run (TrailRun) | trail | 7.0 | 51:49 | 247 (35) | 140 | Single lap, 7:24/km. Climbs: ND du Vivier 78 m at 13% (HR 139), Mur du Vivier 45 m at 17% (144), Wartet 53 m at 11% (161), Bayet–Wartet 35 m at 6% (160) | – | trail | easy | no | yes | |
| 7 | 16116057985 | Sun 12 Oct 2025 | "Long Run" (TrailRun) | trail | 20.0 | 2:04:04 | 564 (28) | 152 | Citadelle tour: Tienne Maquet 118 m at 20%, Tienne des Biches 103 m at 20%, Escaliers 48 m at 18%, Panorama 75 m at 14%, zigzag 110 m at 9%. HR 155–166 on climbs, 143–155 elsewhere | – | trail | long | yes | yes | |
| 8 | 13478263501 | Tue 28 Jan 2025 | Evening Run (TrailRun) | unlisted | 10.0 | 1:04:55 | 352 (35) | 143 | The same ~1 km Citadelle loop (climbs ~5%) done 4 times; loops 2–3 faster (HR 155–165), loops 1 and 4 easier (HR 117–148) | – | trail | tempo | yes | no | |
| 9 | 15639611296 | Tue 26 Aug 2025 | Evening Run | trail | 11.0 | 1:08:56 | 260 (24) | 148 | Single lap. Climbs: Rue St-Hubert 94 m at 15% (HR 159), Mur Feman Nuñez 40 m at 15% (168), Rue de Naninne 40 m at 6% (163), Bois Brûlé 37 m at 10% (158) | 4 days before Epicutrail | trail | tempo | yes | no | |
| 10 | 15873479996 | Sat 20 Sep 2025 | Morning Run | road | 10.6 | 1:08:38 | 170 (16) | 142 | 5.7 km @6:29 (HR 141) · 4.8 km @6:34 (HR 143). Citadelle via Sentier Jacques André, 102 m at 6% (HR 149) | 14 days after Swisspeaks Marathon | road | recovery | no | no | |
| 11 | 15024530818 | Sun 6 Jul 2025 | "15km Hilly Progressive Long Run" | unlisted | 17.5 | 1:50:26 | 476 (27) | 156 | 3.5 km flat (HR 139) · Citadelle loop ×3 (Terra-Nova 43 m at 10%, Jacques André 102 m at 6%), HR on climbs 155 → 166 → 169 loop by loop · 3.5 km home (HR 155–157) | – | trail | long | yes | yes | |
| 12 | 17147026003 | Fri 23 Jan 2026 | Morning Run | road | 8.0 | 48:03 | 61 (8) | 138 | Single lap, steady 6:00/km, max HR 150 | – | road | easy | no | no | |
| 13 | 15454932945 | Thu 14 Aug 2025 | Lunch Run (Louvain-la-Neuve) | unlisted | 8.0 | 50:28 | 143 (18) | 145 | Single lap, 6:18/km. Mur du Ruchaux 34 m at 11% (HR 161), Rue des Bruyères 30 m at 6% (156) | – | road | easy | no | no | |
| 14 | 17013941043 | Sun 11 Jan 2026 | "Ice run" | road | 23.0 | 2:05:38 | 82 (4) | 148 | Laps 11.0 km @5:28 (HR 145) · 4.0 @5:31 (147) · 4.0 @5:16 (153) · 4.0 @5:33 with 61 m climb (155) | – | road | long | yes | no | |
| 15 | 15779175836 | Tue 9 Sep 2025 | Evening Run (TrailRun) | trail | 11.5 | 1:12:54 | 232 (20) | 132 | Single lap, 6:20/km, HR 127–145 on segments; one 35 m climb at 14% | 3 days after Swisspeaks Marathon | trail | recovery | no | yes | |
| 16 | 18417683147 | Thu 7 May 2026 | Afternoon Run | road | 16.0 | 1:27:17 | 204 (13) | 157 | 3.0 km @5:50 climbing 72 m (HR 145) · 3.0 @5:11 downhill (153) · 7.5 km @5:01 (HR 163) · 2.5 km @6:45 climbing 99 m (161) | – | road | tempo | yes | no | |
| 17 | 18022049085 | Sun 5 Apr 2026 | Afternoon Run | road | 7.2 | 35:03 | 20 (3) | 165 | Single lap, 4:52/km on the flat, HR 164–167 throughout | 7 days before Marathon Namur | road | tempo | yes | no | |
| 18 | 18761411819 | Tue 2 Jun 2026 | Evening Run (TrailRun) | trail | 6.4 | 38:40 | 169 (26) | 160 | ~22 × (20 s fast / 40 s easy), about a third of the easy parts climbing at 9–15%; HR 160–184 (flat 170 for the first 2 min: sensor) · 1.7 km cool-down (134) | 5 days before Namuraid | trail | hills | yes | yes | |
| 19 | 15964615850 | Sat 27 Sep 2025 | "12km Long Run" (Wissant, FR) | road | 12.0 | 1:05:14 | 127 (11) | 153 | Laps 5.0 km @5:22 (HR 154) · 4.0 @5:29 (149) · 3.0 @5:24 (156) | – | road | easy | yes | no | |
| 20 | 15539168358 | Thu 21 Aug 2025 | Evening Run | unlisted | 8.5 | 52:19 | 79 (9) | 137 | Single lap, steady 6:10/km, max HR 155 | 9 days before Epicutrail | road | easy | no | no | |

Labels: terrain = road | trail | mountain · intent = race | intervals | hills | long | tempo | recovery | easy | can't tell | not a run · flags = yes | no


## Blind scoring: rubric v1.3 (classify-session v0.4) vs David. **Held-out.**
Applied by Claude as written, after all labels were locked. Values from the baseline rows in effect on each run's date (marathon pace 5:10; Z4 ≥157).

| # | David | v1.3 | Terrain | Intent | tempo_block (D / v1.3) | vertical (D / v1.3) | Why v1.3 missed |
|---|---|---|---|---|---|---|---|
| 1 | road · ~~intervals~~ long (D38) | road · long | ✅ | ❌ → ✅ after relabel | yes / yes ✅ | no / no ✅ | No work/rest alternation in the laps (5:02–5:25); 110 min road → long |
| 2 | trail · hills | **mountain** · hills | ❌ | ✅ | no / no ✅ | yes / yes ✅ | T1: 121 m/km ≥50 → mountain. David: trail (Profondeville is not a real mountain) |
| 3 | road · intervals | road · intervals | ✅ | ✅ | no / no ✅ | no / no ✅ | |
| 4 | road · tempo | road · tempo | ✅ | ✅ | yes / yes ✅ | no / no ✅ | |
| 5 | road · hills | road · intervals | ✅ | ❌ | yes / no ❌ | yes / no ❌ | I2 needs ≥3 climb/descend cycles; this is 2 × 20 × 30/30 *on* a ~7% climb. Tempo block excludes reps. ~7% is under the 8% vertical threshold |
| 6 | trail · easy | trail · easy | ✅ | ✅ | no / no ✅ | yes / yes ✅ | |
| 7 | trail · long | trail · long | ✅ | ✅ | yes / no ❌ | yes / yes ✅ | Climbs at HR 155–166 aren't 15 min continuous at Z4 |
| 8 | trail · tempo | trail · tempo | ✅ (T4) | ✅ | yes / yes ✅ | no / no ✅ | (borderline: loops 2–3 at HR 155–165) |
| 9 | trail · tempo | trail · easy | ✅ | ❌ | yes / no ❌ | no / yes ❌ | Avg HR 148, climbs at 158–168 but no 15 min continuous at Z4. 94 m at 15% fires vertical |
| 10 | road · recovery | road · recovery | ✅ | ✅ | no / no ✅ | no / no ✅ | 14-day window after Swisspeaks |
| 11 | trail · long | trail · hills | ✅ (T4) | ❌ | yes / yes ✅ | yes / yes ✅ | 110 min < 2 h trail long threshold; Citadelle loop ×3 fires I2 |
| 12 | road · easy | road · easy | ✅ | ✅ | no / no ✅ | no / no ✅ | |
| 13 | road · easy | **trail** · easy | ❌ | ✅ | no / no ✅ | no / no ✅ | T4: unknown gear, 18 m/km ≥15 → trail. David: road |
| 14 | road · long | road · long | ✅ | ✅ | yes / no ❌ | no / no ✅ | Laps 5:16–5:33, never ≤5:10 |
| 15 | trail · recovery | trail · recovery | ✅ | ✅ | no / no ✅ | yes / no ❌ | One 35 m climb at 14% (<15%, only one climb) |
| 16 | road · tempo | road · long | ✅ | ❌ | yes / yes ✅ | no / no ✅ | D28 duration-first: 87 min road ≥75 → long, although 7.5 km @5:01 is 44% of the run |
| 17 | road · tempo | road · tempo | ✅ | ✅ | yes / yes ✅ | no / no ✅ | |
| 18 | trail · hills | trail · intervals | ✅ | ❌ | yes / no ❌ | yes / no ❌ | 20/40 reps, HR never drops → I2 no, I3 yes. Reps excluded from tempo block. Climbs only 10–17 m each |
| 19 | road · easy | road · easy | ✅ | ✅ | yes / no ❌ | no / no ✅ | Laps 5:22–5:29. Note: D28 says a non-long run with a tempo block is `tempo`, so easy + tempo_block is inconsistent with the schema |
| 20 | road · easy | road · easy | ✅ | ✅ | no / no ✅ | no / no ✅ | |

**Terrain 18/20 = 90%** (≥95%) · **Intent 14/20 = 70%** (≥85%) · **tempo_block 14/20 = 70%** · **vertical 16/20 = 80%** · Unsure 0.
Intent up from 50% (v1.2 on batch 02) to 70% on fresh data. Still below threshold.
**After the #1 ground-truth correction (D38): intent 15/20 = 75%.** Both figures are kept; the corrected one is the headline, with the correction disclosed.

### Failure causes (hypotheses, for David)
| Cause | Rows | What the data suggests |
|---|---|---|
| **G1 · T1 contradicts D31** | 2 | D31 made mountain "real mountains", but T1 (≥50 m/km) was kept and fires on a Belgian hill-repeat session. Altitude (e.g. terrain above ~1,000 m) would separate the Alps from Profondeville |
| **G2 · T4 cut-off** | 13 | Unknown gear at 18 m/km → trail; David road. Unknown-gear rows so far: 27–35 m/km = trail, 5–18 = road |
| **G3 · David's tempo block is broader than race pace** | 5, 7, 9, 14, 18, 19 | All 6 flag misses are false negatives: sustained Z3 running (5:16–5:33 at HR 150–156), hard reps, and hilly runs with Z4 climbs all count as "tempo block" for David |
| **G4 · Reps on a climb = hills** | 5, 18 | David calls reps done on a climb "hills", even with 2 sets or time-based reps. I2 requires ≥3 climb/descend cycles |
| **G5 · Duration-first vs a big tempo block** | 16 | 38 min @5:01 in an 87-min run = tempo for David. But batch 02 #8 (88 min @5:10 in 163 min) = long. One row; don't tune on it |
| **G6 · #1 has no visible reps** | 1 | Labelled intervals, but laps don't alternate. Worth a check: structure outside the laps, or a misclick |
