---
classification: internal
status: live log (ground truth for race-readiness, D24)
---
# Readiness calls: blind log

David logs his call **before** seeing the skill's output. Agreement = same verdict band.
Actual result is added after the race and scores the predicted time range.

| Race | Date | David's call (logged on) | David's time guess | Skill verdict (conf.) | Skill range | Agree? | Actual (chip) | In range? |
|---|---|---|---|---|---|---|---|---|
| Semi-marathon de Dinant | 2026-10-04 | borderline (29 Sep) | 1:35 | borderline (0.60) | 1:38:54–1:45:01 (mid 1:41:57) | ✅ yes | 1:39:06 | ✅ yes, 12 s inside the fast edge |

## Notes
- **Dinant:** the skill's verdict was driven by C3 recovery (15 of ~62 heuristic days after the Dents du Midi); C1 ok; C4 ref = 20km de Bruxelles 1:37:07. Known limitation logged **before** the race: road Riegel ignores course climbing, and the reference (182 m climbing) is hillier than the Meuse route, so the range may be conservative. Not adjusted after seeing David's guess, to keep the eval clean.
- **Dinant result (chip 1:39:06, given by David 5 Oct via Cowork):** in range, 2:51 faster than the skill's mid (1:41:57) and 12 s inside the fast edge; David's guess (1:35) was 4:06 too fast. Consistent with the pre-race note that the range may be conservative on a flatter course. One race is not evidence for recalibrating.
