---
name: weekly-assessment
description: Turn one week (Mon–Sun) of classified Strava sessions into a coaching assessment covering load trend, intensity balance, flags and a verdict. Use when David asks how his training week went, or for golden-dataset scoring.
classification: internal
version: 0.1
---
# weekly-assessment

**Split of work:** `compute_week.py` computes every number. You write the verdict. **You never do arithmetic**,
round differently, or state a figure that isn't in the script output. This split is how the skill meets its
threshold of 100% of numbers matching a deterministic recalculation.

## Sources of truth
- Flag rules and thresholds: `30 Resources/Running/weekly-flags.md` (the script reads the frontmatter)
- Zones: `20 Areas/Running/athlete-baseline.md` (the script reads the table)
- Session intents: output of the `classify-session` skill

## Input
The target week plus the 4 weeks before it, as activities. Each run should already carry `terrain` and
`intent` from classify-session, and `hr_stream` where available. Non-run activities (hikes, rides, walks)
are included as load only.

## Procedure
1. **Check classification.** If any run in the target week lacks an intent, classify it first (classify-session). Don't guess.
2. **Run** `python3 compute_week.py <input.json>`. If it exits with an error, stop and report the error verbatim.
3. **Write the assessment** using only the script's output:

```
Week <week> · <week_type>
Load: <total_moving_min> min (<delta_pct>% vs 4-wk avg <prior_avg_min>) · <runs> runs, <run_distance_km> km, <run_elevation_m> m D+ · <other_sessions> other
Intensity: Z1–Z2 <z1_z2_pct>% · Z3 <z3_pct>% · Z4–Z5 <z4_z5_pct>% (HR coverage <hr_coverage_pct>%)
Sessions: <one line per run: date · terrain × intent>
Flags: <each fired flag with its value and threshold, or "none">
Verdict: <max 2 sentences: what the week was, and the one thing to change or keep next week>
```

## Rules of conduct
- **Coverage caveat:** if `hr_coverage_pct` < 80, or any run's method is `avg_hr_estimate` or `no_hr`, the verdict says the intensity read is partial. If F2 isn't evaluable, write "intensity: not assessable".
- **Unsure sessions:** if `unclassified_or_unsure` isn't empty, name those runs and say the F3/F4 flags may be wrong until David labels them.
- **Week type drives tone:** in a post-race week, low load and no quality session are the plan, not a problem. Don't advise more.
- **No medical advice.** Pain, illness or HRV interpretation is out of scope. If a description mentions injury, say so and defer to David.
- The verdict judges the week against the flag rules. It doesn't invent new rules.
