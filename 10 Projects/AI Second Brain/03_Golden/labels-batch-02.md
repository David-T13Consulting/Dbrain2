---
classification: internal
status: HELD-OUT batch (test set, D25). Prepared by Claude 30 Sep 2026, blind: facts only, no skill predictions. Labelled by David 30 Sep 2026 via multiple choice. Scores rubric v1.2 / classify-session v0.3.
---
# Golden dataset: labelling batch 02 (held-out, 20 runs)

**Sampling:** eligible pool = every Run/TrailRun on Strava, Jan 2025 – 29 Sep 2026 (133 activities), minus batch 01 (dev set), minus the 3 classify-session worked examples, minus 2 kid runs under 1.2 km. Shuffled once with seed `20260930`; batch 02 = the first 20 of that order. Batches 03–06 take the next 20 each (order in `heldout-order.md`). Nothing hand-picked.
**Shoes:** road = 28636543 / 21087212 · trail = 25832441 · "unlisted" = a gear id the rubric doesn't know (21432884).
**Context** = a named race within 14 days before or 7 days after the run.

| # | Strava id | Date | Name / description | Shoes | km | Moving | Climb m (m/km) | Avg HR | Structure seen in data | Context | Terrain | Intent | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 19832868668 | Fri 21 Aug 2026 | Morning Run (Ostend) | road | 8.1 | 42:45 | 28 (3) | 136* | Steady ~5:15/km; last 1.5 km ~4:50/km. HR 134 → 166 over the last 6 km. *HR flat at 88 for the first 2.2 km (sensor) | – | road | easy | |
| 2 | 19455704946 | Sat 25 Jul 2026 | Morning Trail Run (Grospierres, FR) | trail | 10.1 | 1:01:56 | 283 (28) | 153 | One 4 km climb (125 → 360 m, HR 155–163), 2.5 km rolling on top, 3.5 km descent. HR 140–165 | – | trail | easy | |
| 3 | 19427741252 | Thu 23 Jul 2026 | Morning Run (Saintes-Maries-de-la-Mer) | road | 5.7 | 42:39 | 3 (1) | 109 | Single lap, 7:28/km, max HR 127. Segment "Dans le sable" | – | road | easy | |
| 4 | 19398418968 | Tue 21 Jul 2026 | "Morning Hike", logged as TrailRun (Grospierres, FR) | trail | 5.4 | 1:01:05 | 229 (43) | 99 | 11:20/km, max HR 130 | – | trail | not a run (hike) | |
| 5 | 18727313292 | Sat 30 May 2026 | Lunch Run | road | 5.1 | 31:06 | 35 (7) | 136* | Steady ~6:03/km, HR 125–139. *First 700 m read 168–170 (likely artifact) | Day before 20 km de Bruxelles | road | easy | |
| 6 | 18390649319 | Tue 5 May 2026 | Evening Run | road | 12.3 | 1:04:42 | 43 (4) | 155 | 3.1 km @5:48 (HR 138) · 0.9 km @4:24 (162) · 1.7 km @5:25 (155) · 2.0 km @4:34 (172) · 1.5 km @5:20 (156) · 1.0 km @4:39 (166) · 2.1 km @5:28 (159) | – | road | intervals | |
| 7 | 18315285916 | Thu 30 Apr 2026 | Morning Run (Ostend) | road | 7.5 | 40:45 | 21 (3) | 151 | 2.0 km @5:39 (HR 143) · 5.6 km @5:21 (HR 155, max 162) | – | road | easy | |
| 8 | 17645958217 | Sun 8 Mar 2026 | Morning Run | road | 30.1 | 2:42:50 | 86 (3) | 154 | 7.0 km @5:40 (HR 150) · 17.0 km @5:10 (HR 155) · 6.1 km @5:46 (HR 153) | – | road | long | |
| 9 | 17511072187 | Tue 24 Feb 2026 | Evening Run | road | 11.1 | 1:06:08 | 199 (18) | 144 | 4.6 km @5:26 (HR 130) · 4 × ~665 m park loop @3:56 / 3:58 / 4:41 / 5:30 (HR 175 / 169 / 156 / 149), ~180 m easy between · 3.0 km @7:35 with 150 m climbing | – | road | intervals | |
| 10 | 17158229967 | Sat 24 Jan 2026 | Morning Run / "Belle sortie avec la team ☀️" | road | 27.0 | 2:25:09 | 87 (3) | 148 | 15.0 km @5:29 (HR 143) · 11.0 km @4:59 (HR 154) · 1.0 km @7:47 climbing 39 m | – | road | long | |
| 11 | 17039186757 | Tue 13 Jan 2026 | Evening Run (Jambes track) | road | 12.0 | 1:08:57 | 139 (12) | 137 | 2.4 km @5:55 · 1.4 km climbing 89 m · 6 × ~810 m @3:47–4:04 (HR 145–159), ~200 m @6:00–7:00 between · 2.3 km @7:34 | – | road | intervals | |
| 12 | 16421768454 | Tue 11 Nov 2025 | Race Pace Practice K's / Runna: 3 km warm-up + strides · 4 × 1 km @4:35, 90 s walk · 1 km cool-down | road | 8.7 | 46:27 | 44 (5) | 144 | 3.0 km @5:11 (HR 136) · 4 × 1 km @4:11 / 4:41 / 4:36 / 4:36 (HR 155 / 149 / 156 / 152) with ~90 s walks · 1.0 km @5:45 (HR 154, 27 m climb) | 4 days before Yvoir demi trail | road | intervals | |
| 13 | 16067331907 | Tue 7 Oct 2025 | Tuesday Evening Run (Jambes track) | road | 9.7 | 54:13 (elapsed 1:22) | 4 (0) | 144 | 4.2 km @6:18 (HR 135) · 1.6 km @3:45 (HR 161) · 6 × ~210 m @2:46–3:53 (HR 153–167), ~100 m jogs · 1.9 km @7:20 | – | road | intervals | |
| 14 | 15674846559 | Tue 2 Sep 2025 | Evening Run | unlisted | 5.7 | 32:41 | 31 (5) | 141 | 2.5 km @5:38 (HR 137) · 0.5 km @5:07 (151) · 0.1 km walk · 0.6 km @4:42 (153) · 1.9 km @6:04 (143) | 4 days before Swisspeaks Marathon | road | easy | |
| 15 | 15188697248 | Mon 21 Jul 2025 | Afternoon Run (Les Mathes, FR) | unlisted | 7.0 | 41:56 (elapsed 52:15) | 42 (6) | 145 | ~5:59/km. Out along the dyke 1.5 km @HR 137, back 1.5 km @HR 153 | – | road | easy | |
| 16 | 15100094470 | Sun 13 Jul 2025 | Lunch Run | unlisted | 16.1 | 1:57:18 | 537 (33) | 159 | 3.5 km flat @HR 155, then 12.6 km with 4 climbs of ~100–130 m around the Citadelle (Tienne des Biches and Panorama each climbed twice). HR 163–173 on climbs, 142–156 between | – | mountain | hills | |
| 17 | 15049527580 | Tue 8 Jul 2025 | 10km Easy Run | unlisted | 10.2 | 1:03:33 | 46 (5) | 145 | Steady ~6:15/km, HR 140–150; final 700 m climb HR 165–170 | – | road | easy | |
| 18 | 14949433778 | Sun 29 Jun 2025 | Morning Run | unlisted | 13.0 | 1:22:00 | 308 (24) | 162 | 5.3 km @6:03 (HR 158) · 2.3 km @7:20 climbing 111 m (HR 164) · 5.4 km @6:07 (HR 164). Same Citadelle loop done twice; HR 163–170 from km 4 | – | mountain | tempo | |
| 19 | 13508624497 | Sat 1 Feb 2025 | Morning Run | road | 20.0 | 1:44:37 | 245 (12) | 154 | No laps. km 0–6.5 ~4:50/km (HR 145–166) · Citadelle climb km 6.5–8 · km 8–13 easier (HR 140–150) · km 13.5–17.5 fastest, ~4:35/km (HR 159–167) · climb home | – | mountain | long | |
| 20 | 13261477312 | Sat 4 Jan 2025 | Morning Run | road | 15.0 | 1:18:09 | 185 (12) | 162 | No laps. HR 158–174 from km 1.5 to the end, ~4:45/km on the flat, one 90 m climb km 5.5–7.5 | – | road | long | |

Labels: terrain = road | trail | mountain · intent = race | intervals | hills | long | tempo | recovery | easy | can't tell | not a run

Extra answer from David after labels were locked (didn't change any label): what makes a run **mountain** is *the steepness of the climbs*, not the average climbing per km.

## Blind scoring: rubric v1.2 (classify-session v0.3) vs David. **First held-out score.**

Rubric applied by Claude as written, after all 20 labels were locked. Unlisted gear (…884) isn't covered by T1–T4, so T4 (no gear) was applied as the nearest rule; that's a gap either way.

| # | David | Rubric v1.2 | Terrain | Intent | Why the rubric missed |
|---|---|---|---|---|---|
| 1 | road · easy | road · recovery | ✅ | ❌ | I6a: 42:45 ≤45 min and avg HR 136 ≤140, but the average is dragged down by 2.2 km of flat-88 sensor data. The artifact rule only covers the first 5 min |
| 2 | trail · easy | trail · tempo | ✅ | ❌ | I4: ~25 min at HR 155–163 on the 4 km climb counts as "continuous Z3–Z4" |
| 3 | road · easy | road · recovery | ✅ | ❌ | I6a: 42:39, HR 109. David calls it easy |
| 4 | trail · not a run | trail · easy | ✅ | ❌ | A hike logged as TrailRun. Nothing in the rubric checks activity type beyond sport_type |
| 5 | road · easy | road · recovery | ✅ | ❌ | I6a: 31 min, HR 136. Pre-race shakeout; David calls it easy |
| 6 | road · intervals | road · intervals | ✅ | ✅ | I3: 3 hard blocks with easy running between |
| 7 | road · easy | road · tempo | ✅ | ❌ | I4: 5.6 km lap @HR 155 (30 min in Z3) |
| 8 | road · long | road · tempo | ✅ | ❌ | I4 beats I5: 17 km @HR 155 |
| 9 | road · intervals | road · intervals | ✅ | ✅ | |
| 10 | road · long | road · tempo | ✅ | ❌ | I4 beats I5: 11 km @4:59, HR 154 (a progression finish, which v1.2 calls tempo) |
| 11 | road · intervals | road · intervals | ✅ | ✅ | |
| 12 | road · intervals | road · intervals | ✅ | ✅ | |
| 13 | road · intervals | road · intervals | ✅ | ✅ | |
| 14 | road · easy | road · easy | ✅ (T4 fallback) | ✅ | |
| 15 | road · easy | road · easy | ✅ (T4 fallback) | ✅ | |
| 16 | mountain · hills | trail · hills | ❌ | ✅ | T1 needs ≥50 m/km; this is 33 m/km of short steep Citadelle climbs. T4 fallback → trail |
| 17 | road · easy | road · easy | ✅ (T4 fallback) | ✅ | |
| 18 | mountain · tempo | trail · tempo | ❌ | ✅ | T1 again (24 m/km). Intent borderline: part of the HR sits above 165 |
| 19 | mountain · long | road · tempo | ❌ | ❌ | T1 (12 m/km, one steep Citadelle climb) and T2 (road shoes). I4 fires on ~18 min at HR 159–167 |
| 20 | road · long | road · tempo | ✅ | ❌ | I4 beats I5: 78 min at HR 158–174, unnamed |

**Terrain 17/20 = 85%** (threshold ≥95%) · **Intent 10/20 = 50%** (threshold ≥85%) · Unsure 0/20.
Both below threshold. This is the "held-out batches show v1.2 overfit to batch 01" condition in D25: dev re-score was 100% / 100%, held-out is 85% / 50%.

### Failure causes (hypotheses, for David to confirm before any rubric change)
| Cause | Rows | What the data suggests | Open question |
|---|---|---|---|
| **A · Recovery is too eager** | 1, 3, 5 | David labelled 0 of 8 easy/recovery runs "recovery" in this batch. Batch 01's two recovery labels were both within 6 days after a big race. I6a (≤45 min + HR ≤140) may not match how David uses the word | Is "recovery" only a post-race thing for you? |
| **B · Tempo fires on ordinary long and easy runs** | 2, 7, 8, 10, 19, 20 | David's long/easy runs sit at HR 150–155, which is already Z3 with LTHR 166. His 20 km de Bruxelles averaged 163 for 96 min, which hints LTHR is set too low (OQ-6). Separately, batch 01 tempo rows (#5, #9) had prescribed or deliberate pace blocks; #10 here (progression finish) is long | Is tempo about intent (a planned block) rather than HR? And a re-test of LTHR |
| **C · Mountain = steep climbs, not average gradient** | 16, 18, 19 | David stated it. Average m/km can't see a 100 m climb at ~20% inside a flat 20 km | What's the threshold: max grade over a climb, or a named steep climb? |
| **D · Unlisted gear** | 14–18 | Gear 21432884 (and 21432902 elsewhere in the pool) isn't in the rubric | Which shoes were these? |
| **E · Hikes logged as runs** | 4 | Name says Hike, sport_type says TrailRun, pace 11:20/km | OK to treat "Hike" in the name, or pace slower than ~10:00/km on low HR, as not a run? |

### Protocol note
If rubric v1.3 is tuned on these 20 rows, batch 02 becomes **dev** too. v1.2's headline stays 85% / 50% on batch 02; v1.3 gets scored only on batch 03 onwards.
