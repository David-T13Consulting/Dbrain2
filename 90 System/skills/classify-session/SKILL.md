---
name: classify-session
description: Classify one Strava activity by terrain (road/trail/mountain), intent (race/hills/intervals/long/tempo/recovery/easy) and two flags (tempo_block, vertical). Use when a single activity needs a session type, for the weekly assessment or golden-dataset scoring.
classification: internal
version: 0.4
---
# classify-session

Takes **one activity**, already fetched, and returns **one JSON line**. Reads nothing except the two
reference notes below. Calls no API and writes no file.

## Sources of truth (read these first; never restate their thresholds from memory)
- Rubric and rule IDs: `30 Resources/Running/session-types.md`
- Zones, target race paces and shoe list: `20 Areas/Running/athlete-baseline.md`
If either is missing or unreadable, stop and say so. Don't fall back to generic running knowledge.
Use the zone row and target-pace row **in effect on the activity's date** (`effective_from` ≤ date; if the date predates every row, use the earliest row and lower confidence to ≤0.9). Never use a bpm or pace value from memory or from this file.

## Input
One activity object with: `id, name, description, sport_type, start_local, gear_id, distance_m,
moving_time_s, elevation_gain_m, avg_hr, max_hr, laps[]`, and optionally `streams`
(`time, heartrate, velocity, altitude, distance`). Streams are needed to detect intervals, hills, tempo blocks and the `vertical` flag.
Plus `recent_races`: date and distance of races in the 14 days before the activity (needed for I6 recovery).

## Procedure
1. **Is it a run?** Apply Axis 0. If not → `terrain: null, intent: "load-only"`, flags null. Stop.
2. **Terrain.** Apply T1→T4 in order; first match wins. Climbing (T1) beats shoes. Unknown gear = no gear. Never use `sport_type` for terrain.
3. **Flags.** Compute `tempo_block` and `vertical` per the rubric. `vertical` is `null` without an altitude stream.
   Tempo block effort: pace on flat road, HR (Z4+) on trail, mountain or sustained climbs, or a Runna race-pace description.
4. **Intent.** Apply I1→I8 in order; first match wins. Long (I4) comes before tempo (I5). Recovery (I6) only inside the post-race window.
5. **Confidence** (0–1) reflects how cleanly the rule fired:
   - Clean match on complete data → ≥0.9
   - A rule matched but a close competitor exists (listed edge case, borderline threshold) → 0.5–0.9
   - Missing HR on trail or mountain, conflicting signals, or HR artifacts affecting the decision → <0.5
   - I8 fired → always <0.5
6. **Below 0.5, or when I8 fires, don't guess.** Set `intent: "unsure"` and put your best candidate in `candidate`.
   This goes to David. It's the designed path, not a failure.

## Output: exactly one JSON line, nothing else
{"activity_id": "...", "terrain": "road|trail|mountain|null", "intent": "race|hills|intervals|long|tempo|recovery|easy|unsure|load-only", "candidate": "<intent or null>", "tempo_block": true|false|null, "vertical": true|false|null, "confidence": 0.0, "rules": ["T1", "I1"], "evidence": "<≤25 words: the facts that made the rules and flags fire>"}

## Rules of conduct
- Every figure in `evidence` must come from the input. Never estimate a number you weren't given.
- An HR spike in the first 5 minutes that contradicts the rest of the data is a sensor artifact (see baseline). Ignore it and say so in `evidence`.
- A flatlined HR (the same value for more than 2 minutes) is a sensor fault. Exclude those samples before averaging.
- Don't use the activity name as proof of intent except in I1 (race: a named event). Runna's "Long Run" label is **not** evidence.

## Worked examples (from real activities)
Flags are `null` where the example had no streams.
- 13 Sep 2026 "Morning Run", description "Jogging de Namur", road shoes, 9.9 km, avg HR 167:
  `{"terrain":"road","intent":"race","tempo_block":null,"vertical":null,"confidence":0.95,"rules":["T2","I1"],"evidence":"Named event (Jogging de Namur) in description; road shoes; avg HR 167, Z5."}`
- 19 Sep 2026 "Dents du Midi 2026", trail shoes, 60.6 km, 3,866 m climbing (64 m/km):
  `{"terrain":"mountain","intent":"race","tempo_block":null,"vertical":true,"confidence":0.95,"rules":["T1","I1"],"evidence":"Named event; trail shoes; 64 m climbing/km ≥50."}`
- 18 Aug 2026 "Pyramid Set", road shoes, Runna description with 9 reps, max HR 179 in warm-up:
  `{"terrain":"road","intent":"intervals","tempo_block":false,"vertical":false,"confidence":0.9,"rules":["T2","I3"],"evidence":"Runna description lists 9 reps with walking rest; laps alternate. Warm-up HR 179 is an artifact, ignored."}`
