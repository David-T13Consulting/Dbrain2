---
name: race-readiness
description: Assess readiness for David's next race within 6 weeks (ready / borderline / not ready + confidence) and give a predicted finish-time range. Use when David asks if he's ready for a race, or for golden-dataset scoring.
classification: internal
version: 0.1
---
# race-readiness

**Split of work:** `compute_readiness.py` computes every number (criteria C1–C4, predicted time). You weigh
the criteria and write the verdict. **You never do arithmetic** and never state a figure the script didn't produce.

## Sources of truth
- Criteria, thresholds, time model: `30 Resources/Running/readiness-rules.md` (the script reads the frontmatter)
- Races: `20 Areas/Running/race-goals.md`
- Session intents: `classify-session` output. Races must be classified as `race` to count as references

## ⚠️ Blind-call protocol (the ground truth for the ≥80% agreement threshold)
Before running for a race, check `20 Areas/Running/readiness-calls.md`. **If David's call for that race isn't
logged yet, ask for it first**: ready / borderline / not ready, plus a time guess if he has one.
Don't show or hint at your output until his call is logged. Otherwise the agreement score is contaminated.

## Procedure
1. Pick the next race in `race-goals.md` within the look-ahead window. None → reply "No race in window" and stop.
2. Check the blind call (above).
3. Build the input (race + ~12 months of classified activities) and run `python3 compute_readiness.py <input.json>`. On error, report it verbatim and stop.
4. Weigh the criteria:
   - Any C1 or C3 `not` → at best **borderline**. Two or more `not` → **not ready**.
   - All applicable criteria `ok` → **ready**.
   - Mixed → **borderline**, and name the deciding criterion.
5. **Confidence** (0–1): high when criteria agree and data is complete; lower when a heuristic decides the verdict alone (C3 is a heuristic), when a criterion is missing, or when the only reference is old.
   **Below 0.5 → withhold the verdict**, state the evidence for each side, and escalate to David.
6. Log the output next to David's call in `readiness-calls.md` (write access: only when David approves the write in session).

## Output
```
<race> · <date> · in <days_to_race> days
Verdict: <ready|borderline|not ready|withheld> (confidence <0.00>)
C1 Endurance: <band> (<longest_run.moving> vs target <target_duration>)
C2 Terrain: <band> (<median_weekly_climb_m> m/wk vs <race_climb_m> m) | n/a
C3 Recovery: <band> (<days_between> of ~<days_needed_heuristic> days after <effort.name>, heuristic)
C4 Reference: <reference.name> <reference.elapsed> | none
Predicted: <low>–<high> (mid <mid>) | withheld: <reason>
Why: <max 2 sentences: the deciding criterion and what would change the call>
```

## Rules of conduct
- C3 is the "1 day per mile" heuristic applied to km-effort. Always label it a heuristic. It's conservative for trained ultra runners, so calibrate it against David's calls.
- A predicted time is never produced without a C4 reference. Withholding is the designed path.
- No medical advice. Injury or illness mentioned → note it, defer to David, confidence <0.5.
