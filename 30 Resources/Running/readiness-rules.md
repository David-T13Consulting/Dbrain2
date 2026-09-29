---
classification: internal
status: approved by David 29 Sep 2026 (criteria); numeric defaults proposed by Claude, calibrate at T3
lookahead_weeks: 6
endurance_lookback_weeks: 6
terrain_lookback_weeks: 4
endurance_ok_ratio_x100: 75
endurance_borderline_ratio_x100: 50
climb_ok_ratio_x100: 50
climb_borderline_ratio_x100: 25
recovery_km_effort_per_day_x10: 16
reference_max_age_days: 365
reference_min_ratio_x100: 50
reference_max_ratio_x100: 200
riegel_exponent_x100: 106
range_road_pct: 3
range_trail_pct: 8
---
# Race readiness: rules

Thresholds are in the frontmatter (stored ×100 or ×10 to stay integers). `compute_readiness.py` reads them from there.

**Km-effort** = km + climbing(m)/100. Used for trail/mountain distance and for recovery.

| Criterion | Computed as | ok / borderline / not |
|---|---|---|
| **C1 Endurance coverage** | Longest run (moving time) in the last 6 weeks ÷ predicted race duration (or, with no prediction, race km-effort × 6 min) | ≥0.75 / ≥0.50 / below |
| **C2 Terrain specificity** (trail & mountain races only) | Median weekly climbing over the last 4 weeks ÷ race climbing | ≥0.50 / ≥0.25 / below. n/a for road |
| **C3 Recovery** | For every race or run ≥3 h in the last 90 days: days until race day ÷ (km-effort ÷ 1.6). This is the "1 day per mile" heuristic, applied to km-effort. Worst case counts | ≥1.0 / ≥0.5 / below |
| **C4 Recent comparable result** | Most recent finished race (DNFs excluded) in the same terrain family (road, or trail+mountain), ≤365 days old, with distance ratio 0.5–2.0 | found / — / none (then no time prediction) |

**Predicted time** = Riegel: T₂ = T₁ × (D₂/D₁)^1.06, using elapsed (chip) time of the C4 reference race. Distances are km for road, km-effort for trail and mountain.
Range: ±3% road, ±8% trail/mountain. No reference → time **withheld**, never guessed.
