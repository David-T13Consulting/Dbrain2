---
captured: 2026-09-30
source: Cowork session 5 (working session, not phone)
classification: internal
status: unprocessed
tags: []
---
# Assistant scope ideas (beyond the running coach)

**David's words:** "at what point can I add scope to my assistant (not only a running coach, but a calendar genie, an home energy tracker, a vacation planner, a knowledge digest system and repository, etc...)"
Clarified: "by calendar genie, I had something more personal in mind. School lunch menus, trash pick up calendar, kids activities, etc"

## Claude's proposal (not a decision; for triage)
- **When:** after the H1 gate (realistically mid-October at current pace). Each new domain reuses the pattern: rules in the vault, skills, a ~50-row test set, blind scoring, dated baselines. Cost ~1–2 weeks each, mostly David's labelling time.
- **Why a second domain matters:** a method working in two domains proves it's a method, not a one-off, which is a stronger client demo.
- **Proposed order:**
  1. Family logistics (school menus, trash pickup, kids' activities): right/wrong checkable against source documents; natural second user for the week-10 multi-user step; used weekly. Constraint: children's data, minimised (first names/initials, no health or school details); demo with a synthetic family.
  2. Knowledge digest + repository: highest demo value for Tower13, highest data risk (client material). After the eval dashboard and a proven data-policy filter.
  3. Home energy tracker: checkable, low risk, but proves the same point as running. Optional.
  4. Vacation planner: not in the system; ad hoc use of Claude.
- **Caution:** domains don't need a second agent; the week-11 second agent stays tied to a real limit.

## Open (parked in OPEN_QUESTIONS.md as OQ-11)
Where each family source lives · who else would use it · David's rule on children's data.
