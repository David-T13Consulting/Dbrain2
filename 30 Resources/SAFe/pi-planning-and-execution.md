---
classification: internal
status: draft
updated: 2026-10-01
tags: [safe, pi-planning, inspect-and-adapt, execution, lens/pgm]
---

# PI Planning and execution

The Program Manager's core page: prepare, run and close a PI. Built mainly from the PI Planning
toolkit (facilitator's guide, readiness workbook, Day-1 briefings), the PI Execution toolkit and the
I&A guide.

## 1. Readiness: three areas

The toolkit says any of these three can derail the event:

| Area | Key questions |
|---|---|
| **Organisational readiness** (strategic alignment) | Is the planning scope clear (value stream, ART)? Is there an RTE who understands the role? Are the PI dates, iteration and PI cadence set? Does every team have an SM/TC and PO, and dedicated members? Do business owners and PM agree on priorities? |
| **Content readiness** | Is it known who sets the business context and who presents the vision? Is there a clear vision for the next few PIs and a top ~10 feature list? Is there an architecture briefing (new enabler epics, NFRs)? A development-practices briefing (tools, CI, DoD)? Is the system team formed and are shared services identified? Are tooling, environments and the test strategy known? |
| **Facility readiness** | Is the room big enough for the whole ART, with team tables (avoid breakout rooms, which dilute the face-to-face benefit)? Are remote connections, supplies, food and timezone handling sorted? |

**Size rules from the readiness workbook:** limit around **125 people / 12 teams**, typically
**50–100 people in 7–10 teams**.

**Content preparation owners** (adapted from the workbook):

| Item | Owner |
|---|---|
| Final agenda with timeboxes and speakers | RTE |
| Facilitator prep. A first-time RTE who isn't an SPC pairs with an SPC | RTE |
| Executive briefing (business context) | Senior executive, as high as you can get |
| Product vision briefings + handouts / backlog | PM + BOs |
| ART backlog: top ~10 features | PM + POs |
| Architecture vision briefing | CTO / architects / security |
| Development practices briefing | Senior dev management |
| Event calendar for the PI (iterations, syncs, demos, I&A, next PI Planning) | RTE |

## 2. The two-day agenda

**Day 1**

| Time | Session | What happens |
|---|---|---|
| 8:00–9:00 | **Business context** | Senior exec: state of the business, strategic themes, SWOT or other format |
| 9:00–10:30 | **Product/solution vision** | PM(s): vision, top features, benefit hypotheses. Strictly timeboxed if there are several PMs |
| 10:30–11:30 | **Architecture vision and development practices** | SA: enablers, NFRs, runway. Tech lead: DoD, tooling, CI/test automation, I&A improvement items |
| 11:30–13:00 | **Planning context and lunch** | RTE explains the mechanics: capacity, objectives, board, risks |
| 13:00–16:00 | **Team breakouts #1** | Teams draft plans. PM and architects circulate |
| 16:00–17:00 | **Draft plan review** | Each team presents its draft objectives, capacity/load, risks and dependencies |
| 17:00–18:00 | **Management review and problem solving** | Leaders adjust scope, resources, priorities and constraints. Output: planning adjustments |

**Day 2**

| Time | Session | What happens |
|---|---|---|
| 8:00–9:00 | **Planning adjustments** | Management presents its decisions as a united front |
| 9:00–11:00 | **Team breakouts #2** | Final plans. **BOs circulate and assign business value (1–10)** to each team objective |
| 11:00–13:00 | **Final plan review and lunch** | Teams present final plans, risks and impediments |
| 13:00–14:00 | **ART risks** | Remaining ART-level risks **ROAMed** in front of everyone |
| 14:00–14:15 | **Confidence vote** | Fist of five, team by team and then for the ART |
| 14:15–? | **Plan rework** (if needed) | Continue until commitment is reached |
| After | **Planning retrospective and moving forward** | What worked; final instructions; next steps |

## 3. Team breakout: the steps

1. Clarify features and priorities with PM.
2. Calculate **capacity per iteration**, accounting for holidays, PTO and **capacity allocation** for
   maintenance and support.
3. Brainstorm stories (user + enabler) at backlog level of detail. Too much detail creates false
   precision and WIP.
4. Add improvement items from the last I&A and team retros.
5. Identify dependencies on other teams and add them to the ART planning board.
6. Load iterations in sequence until capacity is reached. **The IP iteration gets no stories.**
7. Park what doesn't fit in a "not this PI" list.
8. Write **PI objectives** (SMART; committed vs **uncommitted**).
9. List risks and impediments.

Physical deliverables per team are one sheet per iteration, one for objectives and one for risks.
Colour-code story cards by type (user story, enabler, maintenance, dependency) so the ART can see the
mix of work.

## 4. PI objectives, business value, uncommitted objectives

- **Committed objectives:** the team is confident it can deliver them.
- **Uncommitted objectives:** planned and counted against capacity, but carrying low-confidence
  assumptions. They give a predictability buffer *without* sandbagging. Leaving them out of the
  "planned" total is what protects predictability.
- **Business value:** BOs score each objective 1–10 during Day-2 breakouts. This is the conversation
  that builds business–IT trust.
- **ART PI objectives** (6.0 emphasis): the ART-level roll-up, often summarised by the RTE/PM after
  planning.

## 5. ROAM and the confidence vote

| ROAM | Meaning | Typical follow-up |
|---|---|---|
| **R**esolved | No longer a concern | Note it and close it |
| **O**wned | Someone takes ownership; can't be resolved in the room | Owner + date, reviewed at ART Sync |
| **A**ccepted | Can't be resolved; accept it | Make it explicit to the BOs |
| **M**itigated | Plan in place to reduce it | Mitigation in the backlog |

**Confidence vote:** fist of five (1–5). If the average is ≥3 the plan is committed. Anyone voting
1–2 gets heard. If confidence is low, rework the plan. Don't override the vote, because it is the
ART's commitment, not management's.

## 6. Executing the PI

| Mechanism | What the RTE watches |
|---|---|
| **ART Sync** (Coach Sync + PO Sync) weekly | Objectives at risk, dependency slips, ROAM status, scope adjustments |
| **System Demo** every iteration | Integrated, tested features, not team-by-team slides |
| **ART planning board** | Dependency strings still valid? New ones surfacing? |
| **Metrics** | Iteration and ART performance metrics, flow metrics (see [[metrics-and-assessments]]) |
| **Release** | Release on demand, decoupled from the PI boundary |
| **IP iteration** | Protected: innovation, hackathons, training, infrastructure, PI Planning and I&A |

## 7. Inspect and Adapt (end of PI)

| Part | Timebox | Content |
|---|---|---|
| **PI System Demo** | ≤60 min | Everything the ART built this PI, more formal than iteration demos. Have PM, PO or SA frame each part with the business problem and the strategy link |
| **Quantitative and qualitative measurement** | 20–45 min | RTE presents the metrics and explains *why* each matters. Key metric: **ART predictability measure** |
| **Retrospective + problem-solving workshop** | 20–30 min retro, then ≥60 min workshop | ART-level systemic problems, solved in groups |

**Predictability measure:**

```
Team achievement % = Actual business value (committed + uncommitted achieved) / Planned business value (committed only)
ART predictability = average across teams (or the ART-level roll-up)
Target band: 80–100%   (>100% is possible via uncommitted objectives)
```

BOs score *actual* business value with each team **before** the I&A. Schedule those sessions in
advance.

**Problem-solving workshop (structured root-cause):**

1. **Agree the problem.** What, where, when, impact. "A problem well stated is half solved."
2. **Root-cause analysis.** Fishbone diagram (people, process, tools, program, environment), then
   **5 Whys** on each cause.
3. **Find the biggest root cause.** Dot-vote (5 votes per person), then a **Pareto chart**.
4. **Restate the problem** for the top root cause.
5. **Brainstorm solutions.**
6. **Create improvement backlog items.** They enter the ART backlog and are planned in the next PI
   Planning.

Distributed I&A checkpoints from the toolkit: **0:30** problem understood and causes on the fishbone →
**1:00** 5 Whys done, Pareto drawn, problem restated → **1:30** solutions voted, improvement items
identified, read-out ready.

## 8. Distributed PI Planning: what changes

Adapted from the distributed guide and Remote ART toolkit:

- Mindset matters more than tooling: "share the pain" of timezones across locations.
- A facilitator per location; a tested tooling cheat sheet; dedicated channels per team plus an RTE
  "front of room" line.
- Digital ART board and team boards in a shared tool, with storage and access prepared in advance.
- Book stakeholder time slots (BOs, PM, SA) for team consultations.
- Timezone-friendly agenda: the two days may stretch to 3–4 shorter days.
- An extra **Coach Sync** at the start of Day 2, plus facilitator debriefs after Day 1.

## 9. Large Solution: Pre- and Post-PI Planning

- **Pre-PI Planning:** Solution Mgmt, STE and Solution Architect, with ART representatives, set solution
  context, capabilities and milestones for the ARTs' planning.
- **Post-PI Planning:** integrate ART plans into solution PI objectives and a solution board, and
  resolve cross-ART risks.

## Use it as…

- **PgM (primary):** set the date first (forcing function), then work through the readiness workbook
  backwards. Your success metrics are predictability in the 80–100% band, the confidence vote and the
  I&A improvement items actually delivered.
- **PL:** your two moments are the vision briefing and the Day-2 business-value conversation with the
  BOs. Prepare the top 10 features with benefit hypotheses before the event, not during it.
- **TC:** the first PI Planning is the transformation's "show". Pair a first-time RTE with an SPC, and
  invite skeptical executives to watch the management review.

## Related

[[events-and-cadence]] · [[facilitation-checklists]] · [[metrics-and-assessments]] · [[artifacts-and-backlogs]] · [[roles]]
