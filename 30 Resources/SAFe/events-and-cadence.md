---
classification: internal
status: draft
updated: 2026-10-01
tags: [safe, events, cadence, governance, lens/pgm]
---

# Events and cadence

Every SAFe event on one page: purpose, cadence, timebox, owner, attendees, inputs and outputs.
Facilitation detail is in [[facilitation-checklists]], and PI Planning and I&A are covered in depth in
[[pi-planning-and-execution]].

## The cadence model

- **Iteration:** 2 weeks (the norm; ≤2 weeks is an assessment criterion).
- **PI (Planning Interval [6.0], formerly Program Increment [5.1]):** typically 8–12 weeks, i.e. 4–5
  development iterations plus one **IP iteration**. Toolkit examples assume 5 iterations (4 dev + IP),
  roughly 10 weeks.
- **Develop on cadence, release on demand.** Cadence governs planning and integration. Releases are
  decoupled and happen whenever the business needs them.
- **Synchronisation:** all teams on an ART share iteration boundaries. Solution Trains align ART PIs.
- **LPM cadence:** Portfolio Sync monthly, Strategic Portfolio Review quarterly (per PI), Participatory
  Budgeting roughly twice a year.

```
PI  = | It1 | It2 | It3 | It4 | IP |
        └ System Demo after every iteration
                                └ IP: PI System Demo + I&A + PI Planning + innovation/learning
```

## Team events

| Event | Purpose | Cadence / timebox | Owner / facilitator | Key inputs → outputs |
|---|---|---|---|---|
| **Iteration Planning** | Commit to iteration goals and the stories that deliver them | Start of iteration · ≤4h | SM/TC facilitates; PO owns content | Refined team backlog, capacity, PI objectives → **iteration goals**, committed stories |
| **Daily Stand-up (DSU)** | Sync on progress toward the iteration goal; surface impediments | Daily · 15 min | Team (SM/TC supports) | Team board → updated plan, "meet-after" list |
| **Backlog Refinement** | Prepare upcoming stories: split, estimate, add acceptance criteria | Weekly or more · ~1h | PO | Features in flight → ready stories |
| **Iteration Review** | Demo working increment to PO and stakeholders; get feedback | End of iteration · ~1h | PO / team | Done stories → feedback, backlog adjustments |
| **Iteration Retrospective** | Inspect how the team worked; pick improvements | End of iteration · ~1h | SM/TC | Iteration data → 1–2 improvement items in the backlog |

## ART events

| Event | Purpose | Cadence / timebox | Owner | Attendees | Inputs → outputs |
|---|---|---|---|---|---|
| **PI Planning** | Align the ART on mission; plan the next PI; commit | Every PI · 2 days | RTE | Everyone on the ART + BOs + PM + SA + stakeholders | Vision, top ~10 features, capacity → **team and ART PI objectives**, **ART planning board**, ROAMed risks, confidence vote |
| **ART Sync** | Progress toward PI objectives; dependencies, risks, scope adjustments | Weekly (or as needed) · 30–60 min + meet-afters | RTE (or co-facilitated) | RTE, PM, POs, SM/TCs, SA, as needed | ART board, PI objectives → decisions, escalations, scope tweaks |
| ↳ **Coach Sync** **[6.0]** (5.1: **Scrum of Scrums**) | Coordinate dependencies and impediments between teams | Weekly (1–2×) · 30–60 min | RTE | RTE + SM/TCs | Team updates → impediment actions, meet-afters |
| ↳ **PO Sync** | Feature progress, scope adjustment, backlog refinement, WSJF prep | Weekly · 30–60 min | RTE or PM | PM + POs | ART backlog → scope changes, refined features |
| **System Demo** | Demo the *integrated* increment of the whole ART | End of every iteration · ~60 min | PM / RTE | ART, BOs, stakeholders | Integrated system → feedback, objective progress evidence |
| **Architect Sync** | Align technical approach and runway across ARTs or the solution | Weekly · 30–60 min | STE or chief architect | Architects, PM/SM, tech leads | Enabler status, designs → technical decisions, runway adjustments |
| **Prepare for PI Planning** | Ready the vision, features, capacity, logistics | Throughout the PI | RTE + PM + SA | ART leadership | → readiness (see ART Readiness checklist) |
| **Inspect and Adapt (I&A)** | PI System Demo + quantitative review + problem-solving workshop | End of every PI · ~half day | RTE | Whole ART + BOs | PI results → predictability measure, **improvement backlog items** |
| **IP iteration** | Estimating buffer, innovation, learning, PI Planning and I&A time | Last iteration of each PI | RTE | ART | → innovation spikes, training, infra work |

**[5.1] → [6.0]:** the toolkits treat SoS and PO Sync as the standard events and ART Sync as an
optional merger of the two. In 6.0, **ART Sync is the standard name**, made up of a Coach Sync and a
PO Sync that may run together or separately.

## Large Solution events

| Event | Purpose | Cadence | Owner |
|---|---|---|---|
| **Pre-PI Planning** | Set solution context and objectives for the ARTs' PI Planning | Before ART PI Planning | STE |
| **Post-PI Planning** | Integrate ART plans into a solution plan; solution PI objectives | After ART PI Planning | STE |
| **Solution Demo** | Demo the integrated solution | Each PI (more often if possible) | Solution Mgmt / STE |
| **Solution Train Sync** | Cross-ART coordination | Weekly or as needed | STE |
| **Solution I&A** | Solution-level retrospective and problem solving | Each PI | STE |

## Portfolio (LPM) events

| Event | Purpose | Cadence | Facilitation | Required |
|---|---|---|---|---|
| **Strategic Portfolio Review** | Strategy and investment decisions: MVP pivot/persevere, approve epics, vision/canvas, themes and OKRs, guardrails | **Quarterly** (per PI, often mid-PI) | APMO | Senior leaders, BOs, Enterprise Architect, solution portfolio manager |
| **Portfolio Sync** | Operational visibility: lean metrics, epic/ART execution issues, cross-value-stream dependencies, improvement backlog | **Monthly** (replaced by the SPR in an SPR month) | APMO | Senior leaders, BOs, APMO, LACE |
| **Participatory Budgeting** | Stakeholders allocate value stream budgets across solutions and epics | **~Twice a year** | LPM | LPM fiduciaries, BOs, Epic Owners, PM/SM, architects |

Detail: [[lean-portfolio-management#LPM events]].

## [AI-Native] event changes

AI-Native SAFe (June 2026) replaces three ART events for AI-Native ARTs. Core SAFe events remain valid
for Core SAFe ARTs. Detail and sources: [[ai-native-safe#10. Events (Session 4)]].

| Core SAFe | AI-Native SAFe |
|---|---|
| PI Planning (2 days) | **PI Outcome Planning** (1 day, outcome breakouts then team breakouts, PI Outcome Planning Board) |
| Inspect and Adapt (end of PI) | **ART Sense and Respond** (2h every iteration, RTE-facilitated: sense outcome progress, customer feedback and workflow, then respond) |
| System Demo | **Customer Demos** (by purpose and reach) |

## Common anti-patterns across events

| Anti-pattern | Fix |
|---|---|
| Syncs turn into status reports for stakeholders | Re-state the purpose; facilitate tightly; send stakeholders to the System Demo for status |
| Events run too long | Prefer more frequent short syncs to long ones; timebox and use meet-afters |
| Teams don't send representatives | Require a proxy, or written updates read out by the RTE |
| System Demo shows slides, not the system | "No slides, all demo" rule; insist on integrated, tested features; demo problems too |
| I&A skipped "because we're busy" | It is the only systemic improvement loop. Protect it the same way as PI Planning |
| Portfolio events are ad hoc, status-only, with no facilitator | Fixed cadence, APMO facilitation, decisions logged and communicated |

## Use it as…

- **PgM:** this page is your operating calendar. Put the entire PI's events in the calendar at the
  start of the PI, including the next PI Planning and I&A.
- **PL:** your events are PO Sync, System Demo, PI Planning (vision briefing) and the SPR.
- **TC:** check event health with the anti-pattern table. It quickly shows how mature an ART is.

## Related

[[pi-planning-and-execution]] · [[facilitation-checklists]] · [[roles]] · [[lean-portfolio-management]]
