---
classification: internal
status: approved by David 29 Sep 2026 (defaults; tested against labelled weeks at T3)
load_change_pct: 30
min_easy_share_pct: 75
lookback_weeks: 4
---
# Weekly assessment: flag rules

The thresholds live in the frontmatter above; `compute_week.py` reads them from there. This table is the human-readable version.

| Flag | Fires when | Suppressed in |
|---|---|---|
| **F1 load-change** | This week's run + non-run moving time differs from the average of the previous `lookback_weeks` by more than ±`load_change_pct`% | Post-race week (drop only) |
| **F2 intensity** | Less than `min_easy_share_pct`% of HR-covered run time is in Z1–Z2 | — |
| **F3 no-quality** | No run with intent intervals, hills or tempo | Race week, post-race week |
| **F4 no-long** | No run with intent long | Race week, post-race week |

**Week types:** a *race week* contains a run with intent race. A *post-race week* is one where a race happened in the 7 days before the week started.
Weeks run Monday to Sunday in local time.
