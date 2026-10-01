---
classification: internal
status: draft
updated: 2026-10-01
tags: [safe, hub]
---

# SAFe: knowledge base

Working reference on the Scaled Agile Framework for three jobs: **Product Leader (PL)**, **Program
Manager (PgM)** and **Transformation Consultant (TC)**. It is meant to replace re-reading the
certification material: what each construct is for, how to run it, what goes wrong, and what to say
to a client.

**Classification `internal`.** The pages are synthesised in my own words, mainly from David's
licensed SAFe 5.1 toolkits (KPMG US archive, see [[30 Resources/SAFe/sources|sources]]), and updated to current SAFe
terminology. They contain no client material. They are for personal reference: don't publish them,
and don't hand them to clients as SAFe content.

## Version stance: read this first

The toolkits are **SAFe 5.1 (2020–21)**. SAFe has moved three times since then. These pages use
**6.0 vocabulary as the baseline** and tag deltas inline.

| Tag | Meaning |
|---|---|
| **[5.1]** | Term or practice as it appears in the toolkits; renamed or retired since |
| **[6.0]** | Introduced or changed in SAFe 6.0 (March 2023) |
| **[2024+]** | From the October 2024 "reimagining": five **SAFe Disciplines** with **competencies** under them, replacing the seven core competencies as the top-level structure. Four Big Picture configurations removed from the main picture |
| **[AI-Native]** | From **AI-Native SAFe** (released June 2026). Extends Core SAFe, does not replace it. Full page: [[ai-native-safe]] |

Core SAFe 6.0 is still the reference model most clients, certifications and job descriptions use.
Speak 6.0 by default, know the 5.1 words because client organisations still use them, and treat
2024+ and AI-Native material as the current direction.

## Reading order

| # | Page | What it answers | Lens |
|---|---|---|---|
| 1 | [[principles-and-mindset]] | Why SAFe works the way it does: values, 10 principles, House of Lean | TC |
| 2 | [[configurations-and-competencies]] | The building blocks, configurations, competencies → disciplines | TC |
| 3 | [[roles]] | Who does what, with a RACI and staffing heuristics | All |
| 4 | [[events-and-cadence]] | Every event: purpose, timebox, owner, inputs and outputs | PgM |
| 5 | [[artifacts-and-backlogs]] | Backlog hierarchy, Kanbans, PI objectives, WSJF, roadmaps | PL · PgM |
| 6 | [[product-management-and-po]] | The PM/PO system: vision to accepted story | PL |
| 7 | [[pi-planning-and-execution]] | PI Planning end to end, ART Sync, I&A, predictability | PgM |
| 8 | [[lean-portfolio-management]] | Strategy, lean budgets, guardrails, portfolio Kanban, LPM events | PL · TC |
| 9 | [[lean-agile-leadership]] | What leaders must do, and the symptoms when they don't | TC |
| 10 | [[transformation-playbook]] | Implementation Roadmap, LACE, VS/ART identification, VSM, launch | TC |
| 11 | [[metrics-and-assessments]] | Outcomes, flow, competency; predictability; Measure and Grow | PgM · TC |
| 12 | [[devops-and-architecture]] | CALMR, the Continuous Delivery Pipeline, runway, enablers | PgM |
| 13 | [[regulated-environments]] | SAFe under banking and medtech compliance | TC |
| 14 | [[facilitation-checklists]] | One-page run sheets per event | PgM |
| 15 | [[ai-native-safe]] | The AI-Native operating model (June 2026): shifts, outcomes, roles, events, governance, roadmap, critique | All |
| — | [[30 Resources/SAFe/glossary\|glossary]] | Acronyms and the 5.1 → 6.0 rename table | All |
| — | [[30 Resources/SAFe/sources\|sources]] | Pointer note to the toolkit archive, licence status, external refs | — |

## The twelve things that matter most

1. **SAFe is an operating model for organising around value, not a meeting schedule.** Value streams
   and ARTs come first. Everything else is plumbing. A transformation that skips the value stream and
   ART identification workshop just relabels the org chart. See [[transformation-playbook]].
2. **The ART is the unit of delivery.** It has 50–125 people and 5–12 teams on one cadence, one
   backlog and one PI Planning. Teams don't deliver alone, the train does. See [[roles]].
3. **PI Planning is the non-negotiable event.** It aligns demand to capacity in two days, surfaces
   dependencies, and turns the plan into committed objectives. If an ART runs only one SAFe event
   properly, it should be this one. See [[pi-planning-and-execution]].
4. **Content authority is split deliberately.** PM owns *what* at ART level (features, WSJF). PO owns
   *what* at team level (stories). The architect owns *how* at system level. The RTE owns *the
   process*, not the content. Blurred authority is the most common failure. See [[product-management-and-po]].
5. **Predictability is the trust currency.** Business value planned vs achieved, 80–100%. It
   rebuilds business–IT trust faster than any velocity chart. See [[metrics-and-assessments]].
6. **Fund value streams, not projects.** Lean budgets plus four guardrails replace project cost
   accounting. This is where transformations stall, because Finance and the PMO have to change.
   See [[lean-portfolio-management]].
7. **Epics are hypotheses, not projects.** An epic has a hypothesis statement, a lean business case and
   an MVP, then a pivot-or-persevere decision. This is the bridge from portfolio to product thinking.
8. **Leaders go first.** Train executives before practitioners. Managers become developers of people
   and Business Owners rather than task directors. See [[lean-agile-leadership]].
9. **Quality and compliance are built in, in small batches.** In regulated industries, the argument
   that "we can't do agile, we're regulated" usually comes from the QMS's waterfall habits, not from the
   regulation. See [[regulated-environments]].
10. **The IP iteration is capacity buffer, not a hardening sprint.** Removing it is the most reliable
    way to destroy predictability and innovation.
11. **Flow replaced velocity as the lead metric in 6.0.** Use flow distribution, velocity, time,
    load, efficiency and predictability. See [[metrics-and-assessments]].
12. **Set the date.** PI Planning works as a forcing function: scheduling it is what makes ART launch
    preparation actually happen. See [[transformation-playbook]].

## How to use this for the three lenses

| You are acting as… | Start with | Then |
|---|---|---|
| **Product Leader** (CPO, Head of Product, Solution/Product Manager) | [[product-management-and-po]] | [[artifacts-and-backlogs]] → [[lean-portfolio-management]] → [[metrics-and-assessments]] |
| **Program Manager** (RTE, STE, delivery lead, APMO) | [[pi-planning-and-execution]] | [[events-and-cadence]] → [[facilitation-checklists]] → [[devops-and-architecture]] |
| **Transformation Consultant** (SPC-style, LACE lead, exec advisor) | [[transformation-playbook]] | [[lean-agile-leadership]] → [[lean-portfolio-management]] → [[regulated-environments]] |

## Scope and exclusions

**In scope:** Core SAFe 6.0 concepts, the practical mechanics captured in the 5.1 toolkits
(agendas, checklists, templates, anti-patterns), and the post-6.0 direction at headline level.

**Out of scope:** verbatim copies of the toolkit slides or templates (the originals stay in the
archive, see [[30 Resources/SAFe/sources|sources]]); the Japanese and French toolkit editions; the SAFe for Marketing and
Meetup Organizer kits, which are low value for these lenses. AI-Native SAFe has its own
page, with every claim tagged by source tier.

## Gaps and figures to verify

- **AI-Native SAFe (June 2026):** see [[ai-native-safe#Gaps and things to verify]]. Session blogs are
  primary, but the 12 critical success factors and the Sense and Respond activities aren't public yet.
- **SAFe Disciplines (2024+):** the five discipline names are confirmed from a Scaled Agile blog post.
  The full competency list under each is still evolving and is not reproduced here.
- **Kanban state names and the core values list** follow 6.0 as best known. Check against the current
  Big Picture before teaching from them.
