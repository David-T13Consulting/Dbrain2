---
name: classify-session
description: Classify one Strava activity by terrain (road/trail/mountain) and intent (race/intervals/hills/long/tempo/recovery/easy). Use when a single activity needs a session type, for the weekly assessment or golden-dataset scoring.
classification: internal
version: 0.2
---
# classify-session

Takes **one activity**, already fetched, and returns **one JSON line**. Reads nothing except the two
reference notes below. Calls no API and writes no file.

## Sources of truth (read these first; never restate their thresholds from memory)
- Rubric and rule IDs: `30 Resources/Running/session-types.md`
- Zones and shoe list: `20 Areas/Running/athlete-baseline.md`
If either is missing or unreadable, stop and say so. Don't fall back to generic running knowledge.

## Input
One activity object with: `id, name, description, sport_type, start_local, gear_id, distance_m,
moving_time_s, elevation_gain_m, avg_hr, max_hr, laps[]`, and optionally `streams`
(`time, heartrate, velocity, altitude`). Streams are needed to detect intervals and hills without manual laps.

## Procedure
1. **Scope.** If `sport_type` isn't Run or TrailRun → output `terrain: null, intent: "load-only"`. Stop.
2. **Terrain.** Apply T1→T4 in order; first match wins. Never use `sport_type` for terrain.
3. **Intent.** Apply I1→I8 in order; first match wins. I8 (unsure) is the fallback when nothing else matches. Use HR zones from the baseline.
   On trail or mountain terrain, judge effort by HR only, never by pace.
4. **Confidence** (0–1) reflects how cleanly the rule fired:
   - Clean match on complete data → ≥0.9
   - A rule matched but a close competitor exists (listed edge case, borderline threshold) → 0.5–0.9
   - Missing HR on trail or mountain, conflicting signals, or HR artifacts affecting the decision → <0.5
   - I8 fired → always <0.5
5. **Below 0.5, or when I8 fires, don't guess.** Set `intent: "unsure"` and put your best candidate in `candidate`.
   This goes to David. It's the designed path, not a failure.

## Output: exactly one JSON line, nothing else
{"activity_id": "...", "terrain": "road|trail|mountain|null", "intent": "race|intervals|hills|long|tempo|recovery|easy|unsure|load-only", "candidate": "<intent or null>", "confidence": 0.0, "rules": ["T1", "I1"], "evidence": "<≤25 words: the facts that made the rule fire>"}

## Rules of conduct
- Every figure in `evidence` must come from the input. Never estimate a number you weren't given.
- An HR spike in the first 5 minutes that contradicts the rest of the data is a sensor artifact (see baseline). Ignore it and say so in `evidence`.
- Don't use the activity name as proof of intent except in I1 (race: a named event) and I4 (a "Long Run" label from Runna).

## Worked examples (from real activities)
- 13 Sep 2026 "Morning Run", description "Jogging de Namur", road shoes, 9.9 km, avg HR 167:
  `{"terrain":"road","intent":"race","confidence":0.95,"rules":["T1","I1"],"evidence":"Named event (Jogging de Namur) in description; road shoes; avg HR 167, Z5."}`
- 19 Sep 2026 "Dents du Midi 2026", trail shoes, 60.6 km, 3,866 m climbing (64 m/km):
  `{"terrain":"mountain","intent":"race","confidence":0.95,"rules":["T2","I1"],"evidence":"Named event; trail shoes; 64 m climbing/km ≥50."}`
- 18 Aug 2026 "Pyramid Set", road shoes, Runna description with 9 reps, max HR 179 in warm-up:
  `{"terrain":"road","intent":"intervals","confidence":0.9,"rules":["T1","I2"],"evidence":"Runna description lists 9 reps with walking rest; laps alternate. Warm-up HR 179 is an artifact, ignored."}`
