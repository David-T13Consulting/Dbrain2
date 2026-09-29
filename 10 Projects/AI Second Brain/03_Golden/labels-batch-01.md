---
classification: internal
status: pilot batch, labelled by David 29 Sep 2026 via multiple choice (issued 2026-09-29 09:46)
---
# Golden dataset: labelling batch 01 (pilot, 10 runs)

Blind: facts only, no skill predictions. David labels what the session **actually was**, not what the rubric would say.
Labels: terrain = road | trail | mountain · intent = race | intervals | hills | long | tempo | recovery | easy | can't tell

| # | Strava id | Date | Name / description | Shoes | km | Moving | Climb (m/km) | Avg HR | Structure seen in data | Terrain | Intent | Note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 20325096316 | Fri 25 Sep 2026 | 9km Long Run / "9km at a conversational pace" | road | 9.0 | 47:29 | 0 (0) | 142 | single lap | road | recovery | |
| 2 | 20293691486 | Wed 23 Sep 2026 | Lunch Run | road | 5.0 | 28:43 | 52 (10) | 138 | single lap | road | recovery | |
| 3 | 20092795744 | Tue 8 Sep 2026 | Evening Run | trail | 14.0 | 1:15:01 | 205 (15) | 145 | 4.3 km warm-up · ~10 × (2 min / 1 min) · 2.9 km cool-down | trail | intervals | |
| 4 | 20043286347 | Sat 5 Sep 2026 | Morning Run | road | 13.0 | 1:05:28 | 265 (20) | 155 | 2.5 km @ HR 132 · 2+2 km climbing @ 160–162 · 2.5 km @ 155 · 2+2 km @ 162–165 | road | tempo | |
| 5 | 19862725793 | Sun 23 Aug 2026 | Lunch Run | road | 18.0 | 1:33:00 | 188 (10) | 148 | 3 × 6 km, HR 137 → 148 → 158 | road | tempo | |
| 6 | 19700546128 | Tue 11 Aug 2026 | Evening Run | road | 6.8 | 59:07 | 478 (71) | 142 | ~17 × 1 min climbs at 17–27% grade, 30 s + walk down | mountain | hills | |
| 7 | 19601685642 | Tue 4 Aug 2026 | Evening Run | trail | 11.0 | 1:14:20 | 458 (42) | 148 | single lap, max HR 175 | trail | easy | |
| 8 | 19354602065 | Fri 17 Jul 2026 | Morning Trail Run / "Club med powa" (Tignes) | trail | 12.1 | 2:03:57 | 926 (77) | 141 | 3.3 km climb (553 m) then 8.8 km | mountain | long | |
| 9 | 16393052403 | Sat 8 Nov 2025 | 16km Long Run with Runna / 4 km comfortable · 6 km @4:50 · 2 km @4:25 · 4 km @4:50 | trail | 17.5 | 1:43:49 | 483 (28) | 153 | 4 laps matching the description | trail | tempo | |
| 10 | 18992119312 | Sat 20 Jun 2026 | Morning Run | trail | 14.9 | 1:21:16 | 326 (22) | 64 (flat: sensor fault) | single lap | trail | can't tell | |

Excluded on purpose: the 3 activities used as worked examples in classify-session (Jogging de Namur, Dents du Midi, Pyramid Set), so the skill isn't tested on examples it has already seen.

## Blind scoring: rubric v1.1 (classify-session v0.2) vs David

| # | David | Rubric v1.1 | Terrain | Intent | Why the rubric missed |
|---|---|---|---|---|---|
| 1 | road · recovery | road · long | ✅ | ❌ | I4 fired on Runna's "Long Run" label (47 min run). Recovery (I6) also fails: 47 min, HR 142 > 140 limits |
| 2 | road · recovery | road · recovery | ✅ | ✅ | |
| 3 | trail · intervals | trail · intervals | ✅ | ✅ | |
| 4 | road · tempo | road · tempo | ✅ | ✅ | |
| 5 | road · tempo | road · long | ✅ | ❌ | 93 min ≥ 75 → I4 long fires before I5 tempo (progression run) |
| 6 | mountain · hills | road · intervals | ❌ | ❌ | T1 road shoes override 71 m/km; I2 intervals checked before I3 hills |
| 7 | trail · easy | trail · easy | ✅ | ✅ | (low confidence: no streams to rule out tempo) |
| 8 | mountain · long | mountain · long | ✅ | ✅ | |
| 9 | trail · tempo | trail · long | ✅ | ❌ | Runna "Long Run" label + long-before-tempo ordering (D21) |
| 10 | trail · can't tell | trail · unsure | ✅ | abstain ✅ | No HR → I8. Correct abstention, excluded from accuracy |

**Terrain 9/10 = 90%** (threshold ≥95%) · **Intent 5/9 = 56%** (threshold ≥85%) · Unsure 1/10 = 10% (budget <10%).
