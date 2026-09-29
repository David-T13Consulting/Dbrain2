---
classification: internal
status: approved by David 29 Sep 2026 (T2.1)
---
# Success thresholds: showcase skills

Set **before** the skills are written. Format: *handles ≥X% of cases with <Y% exceptions.*
Measured against the golden dataset (T3.1). Rubric: `30 Resources/Running/session-types.md`.

| Skill | Input → output | Threshold | Exceptions (routed to David) |
|---|---|---|---|
| **1 · classify-session** | One run → terrain + intent | Terrain correct in ≥95% of cases · intent correct in ≥85% | <10% flagged "unsure" |
| **2 · weekly-assessment** | A week of classified sessions → load trend, effort balance, one-line verdict | Every number 100% matches a deterministic recalculation · verdict passes the LLM-judge rubric in ≥90% of cases · zero made-up numbers | <5% |
| **3 · race-readiness** | Next race within 6 weeks → ready / borderline / not ready + confidence **+ predicted time range** | Agrees with David's **blind** call in ≥80% of cases · 100% of low-confidence (<50%) cases held back and escalated · "no race in window" when true · **approved 29 Sep:** actual chip time falls inside the predicted range in ≥70% of races, with the range no wider than ±3% road / ±8% trail, and time withheld (never guessed) when no reference exists | As many as the low-confidence band produces |

## Why
- Intent is set below terrain: terrain is mostly determined by shoes, while intent has real ambiguity.
- Skill 2 separates numbers (checked by code) from judgment (checked by an LLM judge). Only judgment needs a model to score it.
- Skill 3 is measured on whether it holds back when it should, not on how often it's right. The low-confidence path gets demoed on purpose.
- The 6-week window is a Claude assumption that David approved.
- Time prediction was added at T2.4 by David. Its threshold is proposed. The sample is small (a handful of races a year), so it will be backtested on past races using only data up to each race day.
