---
classification: internal
status: draft
updated: 2026-10-01
tags: [safe, configurations, competencies, lens/tc]
---

# Configurations and competencies

The structural map: which building blocks exist, how much of SAFe a client needs, and how
Scaled Agile now organises the framework.

## The four configurations (6.0 Big Picture)

| Configuration | Adds | Use when | Typical client signal |
|---|---|---|---|
| **Essential SAFe** | Agile teams + ART + PI cadence + ART roles | One or a few ARTs; the starting point for every implementation | "We have 6–10 scrum teams on one product and they trip over each other" |
| **Large Solution SAFe** | Solution Train, Solution Mgmt/Arch/STE, Solution Intent, suppliers | Multiple ARTs build one large, complex solution (cyber-physical systems, core banking platforms) | "Three ARTs, one release, integration hell" |
| **Portfolio SAFe** | LPM, strategic themes, lean budgets, portfolio Kanban, Epic Owners, Enterprise Architect | Several value streams need strategy/funding alignment | "Annual project funding is killing us" |
| **Full SAFe** | All of the above | Enterprises with multiple large solutions and portfolios | Large banks, defence, automotive |

**[2024+]** The October 2024 refresh removed the four configuration views from the main Big Picture in
favour of a disciplines/competencies navigation. The configurations are still the most useful way to
size an engagement. Expect clients and certified practitioners to keep talking in these terms.

## Essential SAFe: the ten critical success factors

From the Essential SAFe diagnostic, restated. If an ART is struggling, check these first. Each factor
comes with the symptom you see when it is missing.

| # | Success factor | Symptom when missing |
|---|---|---|
| 1 | **Lean-Agile principles** understood | Practices adopted cargo-cult style; no way to adapt them to context; disputes about process can't be resolved |
| 2 | **Real Agile teams and trains** (cross-functional, with PM/Arch/RTE authority) | Unclear decision rights, over-specialisation, bottlenecks, local optimisation |
| 3 | **Cadence and synchronisation** | No rhythm, gradual drift into disorder, events hard to schedule, teams overloaded |
| 4 | **PI Planning** | Misalignment, demand > capacity, late dependency discovery, low commitment |
| 5 | **Customer centricity, DevOps, release on demand** | Low customer satisfaction, risky big-batch releases, Dev vs Ops friction |
| 6 | **System Demo** | Teams "sprinting" but the system isn't; false progress; waterfalled PIs |
| 7 | **Inspect and Adapt** | Problems persist; improvements treat symptoms; no predictability measure |
| 8 | **IP iteration** | No estimating buffer; tyranny of the urgent; tech debt grows; burnout |
| 9 | **Architectural runway** | Velocity peaks then falls; architecture decays; irregular releases |
| 10 | **Lean-Agile leadership** | Teams can't learn from leaders; leaders say one thing and do another |

Use this as a **one-page ART health check** in a client diagnostic. Score each factor as red, amber
or green, then attach the matching symptom as evidence.

## The seven core competencies (5.0 → 6.0)

Business agility is described as mastery of seven competencies.

| Competency | Dimensions (short) | Key page |
|---|---|---|
| **Lean-Agile Leadership** | Mindset/values/principles; leading by example; leading change | [[lean-agile-leadership]] |
| **Team and Technical Agility** | Agile teams; teams of Agile teams; built-in quality | [[devops-and-architecture]] |
| **Agile Product Delivery** | Customer centricity and design thinking; develop on cadence and release on demand; DevOps and the CDP | [[product-management-and-po]] |
| **Enterprise Solution Delivery** | Lean systems engineering; coordinating trains and suppliers; continually evolving live systems | [[devops-and-architecture]] |
| **Lean Portfolio Management** | Strategy and investment funding; agile portfolio operations; lean governance | [[lean-portfolio-management]] |
| **Organisational Agility** | Lean-thinking people and Agile teams; lean business operations; strategy agility | [[lean-agile-leadership]] |
| **Continuous Learning Culture** | Learning organisation; innovation culture; relentless improvement | [[lean-agile-leadership]] |

"Without X" symptom lists for each competency (from the Executive Workshop) are in
[[lean-agile-leadership#Diagnostic: "without" symptoms per competency]].

## [2024+] SAFe Disciplines

In October 2024 Scaled Agile reorganised the framework around **five Disciplines**, each holding a
set of **competencies** framed as business problems to solve. Around 21 competencies were cited at
the time, and the list is growing.

| Discipline | Business problem it targets | Closest 5.x/6.0 competency |
|---|---|---|
| **Lean Portfolio Management** | Strategy agility: funding and governing the right work | LPM (+ parts of Organisational Agility) |
| **Team and Technical Agility** | Accelerating value delivery | Team and Technical Agility |
| **Product Development Flow** | Building innovative, customer-centric products | Agile Product Delivery |
| **Large Solution Integration and Delivery** | Building large-scale systems | Enterprise Solution Delivery |
| **Leadership and Culture** | Establishing a new way of working | Lean-Agile Leadership + Continuous Learning Culture + Organisational Agility |

The Measure and Grow assessments were renamed to follow the disciplines (see [[metrics-and-assessments]]).
*(To verify: the exact competency list per discipline before using it with a client.)*

## The Big Picture, layer by layer (6.0 vocabulary)

| Layer | Core constructs |
|---|---|
| **Team** | Agile Teams (Scrum, Kanban, XP), PO, SM/Team Coach, team backlog, iterations |
| **ART** (5.1 "Program") | ART, RTE, Product Management, System Architect, Business Owners, System Team, ART backlog, ART Kanban, PI Planning, System Demo, I&A, IP iteration |
| **Large Solution** | Solution Train, STE, Solution Management, Solution Architect, Solution Intent, Solution Context, suppliers, Pre/Post-PI Planning, Solution Demo |
| **Portfolio** | LPM, strategic themes, portfolio canvas, value stream budgets, guardrails, portfolio Kanban, Epic Owners, Enterprise Architect, APMO |
| **Spanning palette** | Vision, roadmap, milestones, shared services, CoPs, system team, OKRs **[6.0]**, metrics |
| **Foundation** | Lean-Agile leadership, core values, mindset, principles, Implementation Roadmap, SPC |

## Use it as…

- **TC:** start every scoping conversation with the configuration question ("how many ARTs, how many
  value streams, one solution or many?"). It sizes the engagement and the LACE.
- **PgM:** the Essential SAFe ten are your ART operating checklist.
- **PL:** Portfolio SAFe is where product leadership gets funding authority. Push for it once the first
  ARTs are stable.

## Related

[[principles-and-mindset]] · [[roles]] · [[transformation-playbook]] · [[metrics-and-assessments]]
