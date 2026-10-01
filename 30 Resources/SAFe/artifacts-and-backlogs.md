---
classification: internal
status: draft
updated: 2026-10-01
tags: [safe, artifacts, backlogs, wsjf, lens/pl, lens/pgm]
---

# Artifacts and backlogs

The work-item hierarchy, the Kanban systems that move it, and the planning artifacts that carry
alignment from strategy to story.

## Backlog hierarchy

| Level | Work item | Size / horizon | Owner | Backlog / Kanban | Format |
|---|---|---|---|---|---|
| Portfolio | **Epic** (business or enabler) | Multi-PI, above the portfolio epic threshold | Epic Owner | Portfolio backlog / **Portfolio Kanban** | Epic hypothesis statement + lean business case |
| Large solution | **Capability** | Fits in one PI, spans ARTs | Solution Mgmt | Solution backlog / Solution Kanban | Like a feature, with a benefit hypothesis |
| ART | **Feature** (business or enabler) | Fits in one PI, one ART | Product Management | **ART backlog** [6.0] (5.1: Program Backlog) / **ART Kanban** | Name + benefit hypothesis + acceptance criteria |
| Team | **Story** (user or enabler) | Fits in one iteration | PO | Team backlog / team Kanban | "As a <role> I can <activity> so that <value>" + acceptance criteria |
| Team | Task | Hours | Team | — | — |

**Enablers** exist at every level and have four types:

| Enabler type | Purpose | Example |
|---|---|---|
| **Exploration** | Research, prototypes, spikes to understand customer needs or options | Evaluate three OCR vendors |
| **Architecture** | Build architectural runway | Event bus for case updates |
| **Infrastructure** | Build/improve dev, test, deploy environments | Ephemeral test environments |
| **Compliance** | Activities required for V&V, audits, regulatory evidence | Design review with recorded actions |

**NFRs** (non-functional requirements) are *constraints* on backlogs, not backlog items. They live
in the Definition of Done and the solution intent and are tested continuously.

## Kanban systems

**Portfolio Kanban:**

| 5.1 states (toolkits) | 6.0 states | Exit / pull policy (toolkit example, adapted) |
|---|---|---|
| Funnel | **Funnel** | Pull when an Epic Owner has capacity |
| Reviewing | **Reviewing** | Hypothesis statement written; pull into analysis when an Epic Owner is available (WIP-limited) |
| Analysing | **Analysing** | Lean business case + MVP defined; **LPM approves** (go/no-go) |
| Portfolio Backlog | **Ready** | Pull when ART capacity and budget are available |
| Implementing: MVP | **Implementing** | Build the MVP; evaluate the hypothesis |
| Implementing: Persevere | ↳ (persevere) | Continue only if the MVP hypothesis is proven; decentralise into ART backlogs |
| Done | **Done** | No longer a portfolio concern |

Design questions from the toolkit when setting one up: which states to add or remove, WIP limits for
Reviewing and Analysing, and **swim lanes** (business vs enabler, mandatory/regulatory, expedite).
Exit criteria act as an agreement between stakeholders and keep epics consistent. Update them as you
learn.

**ART Kanban** (typical): Funnel → Analysing → Ready → Implementing → Validating on staging →
Deploying to production → Releasing → Done. Each state should have explicit exit policies and WIP limits.

## Planning artifacts

| Artifact | What it is | Owner | When it changes |
|---|---|---|---|
| **Strategic themes** | Differentiating business objectives linking the enterprise strategy to the portfolio. **As OKRs [6.0]**: objective plus 2–5 measurable key results | LPM with enterprise execs | Annually / at the SPR |
| **Portfolio canvas** | Business-model-canvas adaptation: value streams, solutions, customers, channels, value propositions, KPIs/revenue, budget, partners, activities, resources, costs | LPM | Current and future state; reviewed at the SPR |
| **Vision** | Future state of the solution: problem, users, features/benefits, NFRs | PM / Solution Mgmt | Rolling. Briefed at every PI Planning |
| **Roadmap** | PI roadmap (next ~3 PIs, committed + forecast) and solution roadmap (1–3 years) | PM / Solution Mgmt | Each PI |
| **Milestones** | PI, fixed-date (regulatory, trade show) and learning milestones | PM / RTE | As needed |
| **PI objectives** | Business and technical goals per team and per ART for the PI. Committed vs **uncommitted**. BOs assign business value (1–10) | Teams (draft) + BOs (value) | PI Planning |
| **ART planning board** [6.0] (5.1: Program Board) | Features by iteration per team, dependencies (strings), milestones | RTE | PI Planning, updated in ART Sync |
| **ROAM risk board** | Risks sorted as Resolved / Owned / Accepted / Mitigated | RTE | PI Planning, ART Sync |
| **Solution intent** | Single source of truth for current and intended solution behaviour, fixed vs variable | Solution Mgmt + Solution Arch | Continuously |
| **Definition of Done** | Team, ART, solution and release DoDs; includes compliance items | Teams / RTE | Revisited at I&A |

## WSJF: Weighted Shortest Job First

```
WSJF = Cost of Delay / Job Size (duration proxy)
Cost of Delay = User/Business Value + Time Criticality + Risk Reduction & Opportunity Enablement (RR|OE)
```

**How to run it:**

1. Score with a **modified Fibonacci scale** (1, 2, 3, 5, 8, 13, 20).
2. Go **column by column, not item by item**. Put a 1 on the smallest item in each column and score
   the rest relative to it.
3. Do it collaboratively (PM + POs + BO + SA) at PO Sync before PI Planning.
4. Re-score each PI. WSJF is relative and perishable.

**Pitfalls:**

- Treating the output as precise.
- Job size inflated by one gating ART.
- Enablers losing every time. Use capacity allocation as the guardrail so enablers aren't left to WSJF alone.
- Business stakeholders gaming the "value" column. Insist on evidence from the benefit hypothesis.

## Capacity allocation

The percentage of each PI's capacity reserved by work type: new features, enablers, tech debt,
maintenance and defects. Set as policy per value stream, adjusted at PI boundaries by PM + SA (and
LPM at portfolio level). It is one of the four lean budget guardrails. See [[lean-portfolio-management]].

## Templates in the toolkit archive

These are not reproduced here. Locations are in [[30 Resources/SAFe/sources|sources]].

- Epic hypothesis statement; lean business case (LPM toolkit)
- Strategic themes (OKR) template; portfolio canvas; development value stream canvas
- ART readiness workbook, program backlog workbook, capacity allocation, ART canvas (PI Planning toolkit)
- Writing and splitting stories guide; estimating poker cards; iteration burn-up (Iteration Execution toolkit)

## Use it as…

- **PL:** you own features and their benefit hypotheses. Write the hypothesis *before* you write
  acceptance criteria. See [[product-management-and-po]].
- **PgM:** the ART planning board plus ROAM is your PI control tower. Keep it live after PI Planning.
- **TC:** a portfolio Kanban with real exit criteria and an epic threshold is the clearest sign that LPM
  has been implemented rather than just announced.

## Related

[[product-management-and-po]] · [[pi-planning-and-execution]] · [[lean-portfolio-management]] · [[30 Resources/SAFe/glossary|glossary]]
