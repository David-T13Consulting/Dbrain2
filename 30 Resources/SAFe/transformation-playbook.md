---
classification: internal
status: draft
updated: 2026-10-01
tags: [safe, transformation, implementation-roadmap, lace, value-streams, lens/tc]
---

# Transformation playbook

How to take an organisation from "we've decided to do SAFe" to running ARTs and a funded portfolio.
Built from the Implementation Roadmap, LACE, Value Stream and ART Identification (VSAIW), Value Stream
Mapping (VSMW), Team Formation and PI Planning toolkits. This is the Transformation Consultant's main
page.

## The Implementation Roadmap: 12 steps

| # | Step | Purpose | Key outputs / accelerators | Typical pitfalls |
|---|---|---|---|---|
| 1 | **Reaching the tipping point** | Create urgency: burning platform or proactive leadership | 3-minute pitch; problem statement with cost of delay | Starting without a real "why" |
| 2 | **Train Lean-Agile change agents** | Build a critical mass of SPCs (internal + partner) | SPC cohort | Relying only on external coaches |
| 3 | **Train executives, managers and leaders** | Leaders learn *what they must do* (Deming) | Executive Workshop, Leading SAFe | Executives "too busy". Deming: "if you can't come, send no one" |
| 4 | **Create a LACE** | Guiding coalition running the transformation as an Agile team | LACE canvas, mission, backlog | LACE = rebranded PMO with no authority |
| 5 | **Identify value streams and ARTs** | Organise around value; design ARTs | **VSAIW**, development value stream canvas | Mirroring the org chart; ARTs with many dependencies |
| 6 | **Create the implementation plan** | Choose the first ART; three-PI rolling roadmap | Launch sequence; transformation backlog | Over-detailed plans (Reinertsen: more detail → longer cycle times) |
| 7 | **Prepare for ART launch** | Train ART leaders; set the date; readiness | **Set the PI Planning date as a forcing function**; ART readiness workbook; role mapping | Waiting for perfect readiness |
| 8 | **Train teams and launch the ART** | **Quickstart**: train everyone and run the first PI Planning in about a week | SAFe for Teams + PI Planning | Training teams months before launch |
| 9 | **Coach ART execution** | Short-term wins: plan, execute, demo and retro the first PIs | System Demos, I&A, coaching SMs and POs, DevOps maturity | Coaches leave after PI Planning |
| 10 | **Launch more ARTs and value streams** | "Rinse and repeat" | Next VSAIW outputs | Scaling before the first ART is stable |
| 11 | **Extend to the portfolio** | LPM: themes, lean budgets, guardrails, portfolio Kanban | LPM toolkit (see [[lean-portfolio-management]]) | LPM left until year 3; projects keep being funded |
| 12 | **Accelerate** | Relentless improvement; Measure and Grow; competencies; agility beyond IT | Business Agility assessment; APMO, LACE, CoPs | Declaring victory after the ART launches |

**Training sequence by role** (Implementation Roadmap):

| Audience | Course | When |
|---|---|---|
| Change agents | Implementing SAFe (SPC) | Step 2 |
| Executives, managers, leaders | Leading SAFe; Executive Workshop | Step 3 |
| LPM, portfolio leaders | Lean Portfolio Management | Step 11 (earlier if possible) |
| PO / PM / BO / Solution Mgmt | SAFe POPM | Step 7 |
| SM / Team Coach, RTE | SAFe Scrum Master; RTE | Step 7 |
| Architects | SAFe for Architects | Step 7 |
| All ART members | SAFe for Teams | Step 8 (launch week) |

Training managers in the team-level classes as well pays off, because it makes them able to support
self-organisation.

## LACE: the Lean-Agile Center of Excellence

**What it is.** A small, cross-functional Agile team of **3–9 people** that owns the transformation
backlog. A C-level sponsor acts as its **Product Manager**. It has its own PO and SM. It runs on
iterations and a **PI cadence**, synchronised with the ARTs, and **demos** its work like any other team.

**Typical responsibilities:**

- Implementation plan and transformation backlog
- Transformation metrics and progress communication
- Training and coaching, done directly or sourced
- Facilitating VSAIWs and supporting ART launches
- Communities of practice
- Lean-Agile events, and links to the external community
- Extending Lean-Agile practices to HR, finance and contracts
- Relentless improvement

**LACE creation workshop** (half a day, small working group of SPCs and sponsors). It fills the
**LACE canvas** in eight steps:

| Step | Canvas box | Content |
|---|---|---|
| 1 | Mission statement | For / who / the LACE / is a / that / unlike / we… |
| 2 | Responsibilities | In scope, plus an explicit **out of scope** list |
| 3 | Key stakeholders | Leadership questions (urgency, budget, priorities, people impact, extending to HR/finance/contracts) and implementation questions (training, existing Lean-Agile experience, LPM, DevOps/architecture). Map on **influence × interest**: Engage / Satisfy / Inform / Monitor |
| 4 | Principal roles + team and locations | PM (sponsor), PO, SM; members who give influence across the stakeholder map |
| 5 | KPIs / success criteria | **Adoption** (% trained, ARTs launched, value streams on SAFe), **Assessment** (Business Agility, DevOps health radar), **Outcome** (% better predictability, time to market, productivity, engagement, customer satisfaction) |
| 6 | Key activities and cadence | Iteration and PI length; how it demos |
| 7 | Budget | Training, events, tooling, staffing |
| 8 | Communication strategy | Advertising, recognition, events, PR, knowledge sharing, interactive events, word of mouth, 1:1 coaching |

**Capacity allocation for the LACE** splits its time across three kinds of work:

- **Requests for help:** troubleshooting, queries, escalations.
- **Operational work:** communications, CoPs, wider organisational change in HR, finance, marketing
  and tooling.
- **SAFe implementation:** backlog workshops, training, ART launches, coaching, I&A facilitation,
  extending to the portfolio.

**Where the LACE finds improvement items:** VSAIWs, PI Planning (dependencies, ROAM, confidence vote),
I&As, VSMWs, CoPs, Gemba, office hours.

**Scaling the LACE:** start with one central LACE. As the transformation grows, move to a hub-and-spoke
model with portfolio or business-unit LACEs.

## Value Stream and ART Identification Workshop (VSAIW)

**Purpose.** Design the organisation's **network** side, meaning value streams and ARTs. It doesn't
reorganise the hierarchy. Saying so explicitly lowers resistance.

**Preparation** (from the prep guide):

1. **Scope.** One SAFe portfolio per workshop.
2. **Participants (≤20):** LACE/SPCs; executives with the authority to cut across silos; BOs and
   stakeholders who know the operational flow; technical authorities and development managers who
   know the systems and people.
3. **Alignment beforehand:**
   - Run it the day after Leading SAFe if possible.
   - Hold an "Organising Around Value" briefing (30–60 min).
   - Run **empathy interviews** with attendees (template in the toolkit).
   - Write 1–2 **problem statements** in the form WHAT / WHEN / WHERE / IMPACT, with cost-of-delay data
     if you have it.
4. **Facilitation:** 1–2 SPC leads plus one facilitator per operational value stream group; a dry run;
   1-day version (few or known value streams, or a re-evaluation) vs 2-day version (first time, several
   value streams); tables of 4–8 with colour-coded stickies; printed workbooks.

**Workshop flow:**

| Module | Step / activity | Facilitation notes |
|---|---|---|
| 1. Why value streams | **Identify silos** and their impact on flow | Keep the output, you will test the ART designs against it later |
| 2. Identify and validate | **2.1 Operational value streams (OVS)** by type: *fulfilment*, *manufacturing*, *software product*, *supporting* | "What can customers get if they visit our website?" Don't model manufacturing as a development value stream |
| | 2.2 Write an OVS definition; elaborate **8–12 steps** | Not a process map. Show handoffs between functions |
| | **2.3 Solutions** the OVS uses or sells | Only solutions you actively develop (not email or ALM tools). Group tightly coupled systems; flag shared ones |
| | **2.4 People** who build and support each solution | FTEs, locations, contractors, suppliers, scarce skills (single points of failure) |
| | **2.5 Development value streams (DVS)** | Triggered by feature requests. "Don't think about ARTs yet." If most features touch every system, it's one DVS. If systems are decoupled, there are several |
| | **2.6 Realise DVSs into ARTs** | Three cases: several DVSs in one ART; one DVS = one ART; one DVS → several ARTs (**Solution Train**). ART topologies: **stream-aligned**, **complicated-subsystem**, **platform**. Geography, language and cost centre are weaker splitting criteria. Not everything needs an ART |
| | **2.7 Validation-test the ART options** | Score H/M/L (L = best) on **coordination and dependencies**, **epic distribution and WIP**, **organisational change impact** (plus custom tests: compliance, architecture, suppliers). Don't just add up the scores, some tests weigh more. An intermediate design plus a target state is fine |
| | 2.8 **Development value stream canvas** | Complete one live; finish the rest after the workshop |
| 3. Next steps | **Pick the most opportunistic first ART**, scored on *leadership support*, *collaborating teams*, *clear product/solution*, *significant challenge or opportunity* | Score relative to the lowest. Use 1–5 if many ARTs |
| | **Launch sequencing**: all at once or staggered? | Depends on existing Agile teams, SPC capacity, and whether the org has launched an ART before |
| | Next steps; **agree launch dates** | A date is a forcing function. Schedule implementation planning separately |

**Banking example used in the toolkit:** loan origination OVS → systems (channels, loan origination,
credit scoring, core banking) → two DVSs (front-end origination plus scoring; core banking) with few
dependencies between them → ARTs split by location and skill. This maps directly to retail and
commercial banking clients.

## Value Stream Mapping Workshop (VSMW)

Run it **after** the VSAIW, on **one** known value stream at a time. It is value stream mapping
(cross-functional, strategic, leadership level), **not process mapping** (inside one function,
tactical).

| Prep item | Guidance |
|---|---|
| Scope | One value stream with **8–12 steps**, known *before* the workshop. Pre-fill the business-context and step/team rows of the current-state canvas |
| Participants | **8–11 functional leaders**, one per step, empowered to change their area. SMEs can drop in |
| Inputs | Business context (from the DVS canvas or empathy interviews), steps, and per-step metrics: process time, lead time, %C&A (percent complete and accurate) |
| Output | Current-state map → bottlenecks → **future-state canvas** and improvement plan |

**After the workshop: eight actions** (actions guide):

1. Complete the future-state canvas.
2. Turn participants into a **CoP or leadership coalition** that owns the plan.
3. **Socialise** the plan through ART and team events.
4. Turn the plan into an **epic + lean business case** and get it approved.
5. Split it into **features**, plan them at PI Planning.
6. **Implement**.
7. **Measure** (Gemba plus metrics vs the current state).
8. **Adjust** the plan; re-run the VSMW once the top bottlenecks are cleared. This is how a value stream
   management practice becomes routine.

## Team formation: the Agile team charter

A half-day workshop that builds the charter in ten steps. Use it for new teams, and re-run periodically.

1. **Purpose**: a WHY statement, "TO <contribution> SO THAT <impact>" (Sinek's Golden Circle). Pairs draft, then the team consolidates.
2. **Team name, type and responsibilities**: stream-aligned, complicated-subsystem, platform or enabling; what the team owns on the ART. Name the team after its value, not a component.
3. **Working agreements**: brainstorm, group, then check each one with a quick support vote.
4. **Success measures**: objective → quantified definition of success → mixed measures including leading indicators → a date.
5. **Definition of Done**: brainstorm, then sort by frequency (every story / iteration / integration / release) and by *doing now* vs *start doing*.
6. **Key interactions**: other teams, their area, **interaction mode** (e.g. "as a service", collaboration, facilitation, from Team Topologies) and frequency.
7. **Key stakeholders**: mapped by interest and influence, with how the team will keep each one informed.
8. **Team member responsibilities**: primary and secondary, for each person.
9. **Distinctive competencies**: 1–2 per person, plus 1–2 skills each person wants to learn (to match with other teams).
10. **Team events and flow**: when, where and how long team events run; Scrum or Kanban.

## Quickstart ART launch (one week)

Days 1–2 are SAFe for Teams training for the whole ART, days 3–4 are the first PI Planning, and day 5
is spare or used for tooling and team set-up. The prerequisites are the VSAIW done, readiness work done,
the backlog's top ~10 features ready, and roles cast and trained. Going "all in, all at once" per ART
works better than piecemeal team-by-team adoption.

## Common transformation failure patterns (consultant's list)

| Pattern | Early signal | Counter |
|---|---|---|
| **IT-only SAFe** | No BOs at PI Planning; Finance absent | Executive Workshop; BO role defined per ART; LPM on the roadmap from day 1 |
| **Org-chart ARTs** | ARTs named after departments; many cross-ART dependencies | Re-run the VSAIW with validation tests |
| **Renamed PMO** | The LACE produces status reports, not change | LACE canvas with outcome KPIs; C-level PM |
| **Proxy POs** | POs can't accept stories without approval | PO casting by attributes; decision rights in the RACI |
| **Waterfalled PIs** | Integration in iteration 5; hardening in the IP iteration | System Demo every iteration; DevOps investment |
| **No portfolio change** | Projects still funded annually; epics = projects | LPM readiness checklist; participatory budgeting pilot |
| **Coach exit after launch** | Predictability drops in PIs 2–3 | Coaching through ≥3 PIs (step 9) |
| **Metrics theatre** | Velocity compared between teams; 100% predictability "every time" | Flow metrics; predictability band 80–100% |

## Use it as…

- **TC (primary):** the roadmap is also an engagement model. A credible offer is phased:
  1. Diagnostic: Executive Workshop, "without" symptoms, Business Agility baseline.
  2. Design: LACE canvas, VSAIW, VSMW.
  3. First ART launch with ≥3 PIs of coaching.
  4. LPM extension.
  5. Measure and Grow.

  Each phase has its own artifacts and success criteria. This fits fractional, embedded and
  referral-sourced engagements.
- **PgM:** steps 7–9 are the RTE's job. The readiness workbook and the "set the date" principle are
  the tools.
- **PL:** steps 5 and 11 decide your product boundaries (DVS and ART) and your funding. Be in those
  rooms.

## Related

[[lean-agile-leadership]] · [[roles]] · [[pi-planning-and-execution]] · [[lean-portfolio-management]] · [[metrics-and-assessments]] · [[regulated-environments]]
