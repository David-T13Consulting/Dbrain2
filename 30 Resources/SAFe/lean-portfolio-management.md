---
classification: internal
status: draft
updated: 2026-10-01
tags: [safe, lpm, portfolio, funding, governance, lens/pl, lens/tc]
---

# Lean Portfolio Management (LPM)

How strategy, funding and governance work once you stop funding projects. Built mainly from the LPM
Execution toolkit: readiness workbook, guardrails, participatory budgeting guide, Strategic Portfolio
Review and Portfolio Sync decks, CapEx/OpEx, compliance and TBM white papers. This is usually where a
SAFe transformation succeeds or stalls, because Finance, the PMO and executives have to change their
own operating model.

## What a SAFe portfolio is

A **collection of development value streams**, each building and maintaining one or more solutions,
under one governance and funding model. Small and medium enterprises usually have one portfolio. Large
enterprises have several, typically one per business unit. Each portfolio has a **portfolio canvas**,
**strategic themes**, **value stream budgets** and a **portfolio Kanban**.

## The three LPM collaborations

| Collaboration | Responsibilities | Typical people |
|---|---|---|
| **Strategy and investment funding** | Connect the portfolio to enterprise strategy; maintain the portfolio vision; establish value stream budgets and guardrails; run the portfolio Kanban flow of epics | Enterprise execs, LPM members, Business Owners, solution portfolio manager, Finance, Enterprise Architect, Epic Owners |
| **Agile portfolio operations** | Coordinate value streams; support ART/solution train execution; foster operational excellence (APMO + LACE, CoPs, execution patterns, agile contracts) | APMO, LACE, RTE/STE community |
| **Lean governance** | Forecast and adjust budgets dynamically; measure portfolio performance; coordinate continuous compliance; audit | APMO, BOs, Enterprise Architect, Finance, Compliance |

## Strategy: themes, canvas, vision

- **Strategic themes** are differentiating business objectives, expressed as **OKRs [6.0]** with an
  objective and 2–5 measurable key results. The toolkit contrasts good themes (specific, e.g. "appeal
  to 18–29 demographic", "reduce warehousing cost 35%") with bad ones (generic, e.g. "maximise
  shareholder value").
- **Portfolio canvas:** a business-model-canvas adaptation covering value streams, solutions, customers,
  channels, customer relationships, value propositions, budget, KPIs/revenue, key partners, activities
  and resources, cost structure and revenue streams. Done as current state → future state(s), with the
  gap driving epics.
- **SWOT / TOWS** templates are used to generate future-state hypotheses.

## Lean budgets

Fund **value streams**, not projects. Each value stream budget has two parts:

| Part | Covers |
|---|---|
| **Run the business** (solution costs) | Features, capabilities and epics *below* the portfolio epic threshold, plus operations and maintenance |
| **Grow the business** (epic investments) | Epics *above* the threshold, approved through the portfolio Kanban |

**Benefits** (Executive Workshop): full control of spend, no costly project variance analyses, no
resource reshuffling, no blame game over project overruns.

**Cadence:** value stream budgets are typically adjusted **about twice a year** through participatory
budgeting. More often makes planning hard. Less often locks spending in for too long.

## The four lean budget guardrails

| # | Guardrail | Mechanism | Practical note |
|---|---|---|---|
| 1 | **Guide investments by horizon** | Allocate % across **H3 Evaluating** (new potential solutions), **H2 Emerging** (graduated from H3), **H1** (*Investing* in solutions needing significant ongoing investment; *Extracting* value from stable solutions with minimal new investment), **H0 Retiring** (decommissioning) | The toolkit cites recommended ratios from an HBR article. Agree the ratio with the CFO explicitly |
| 2 | **Apply capacity allocation** | Per value stream, the % of capacity for new features, enablers, tech debt and maintenance in each PI | Stops enablers and tech debt being starved by WSJF |
| 3 | **Approve significant initiatives** | **Portfolio epic threshold** (cost, number of PIs, strategic importance, or a mix). Below → decomposed into ART/solution Kanbans. Above → portfolio Kanban and LPM approval. **All epics need a lean business case** | The threshold is the single most important LPM policy: too low drowns LPM, too high loses control |
| 4 | **Continuous Business Owner engagement** | BOs attend PI Planning, I&A and prep; communicate the portfolio vision; verify spend goes to the right things | Name the BOs per value stream (template in the toolkit) |

## Participatory Budgeting (PB)

A structured forum where stakeholders collaboratively allocate value stream budgets across solutions
and epics. Its roots are in civic participatory budgeting.

**How to run it (from the PB guide):**

1. **Prepare content.** The highest-priority epics from the portfolio Kanban (business + enabler,
   including in-flight ones) with cost estimates, plus the baseline run-the-business costs per value
   stream.
2. **Brief the business context.** BOs set the theme, for example retaining a top B2B customer, a 20%
   budget cut, or expanding exploration into adjacent markets.
3. **Gather participants.** LPM fiduciaries, BOs, Epic Owners, PM/Solution Mgmt, enterprise and system
   architects, other key stakeholders.
4. **Form groups of 5–8.** Mix value streams and roles, with at least one person per group who
   understands most of the epics. *Example:* 40 leaders in five groups of eight.
5. **Split the money.** Each group gets the total portfolio budget, divided equally among its members.
6. **Fund.** Groups collaboratively fund solutions and epics. Partially funded items become candidates
   for termination or renegotiation, and their money is reallocated. Groups may fund *more* than
   forecast (if they think the estimate is low) or *less* (if the investment looks too high for the
   benefit hypothesis).
7. **Check guardrails.** Groups check their choices against the horizon guardrails.
8. **Decide.** **LPM fiduciaries make the final decision.** The groups' results are input, not a
   vote.

**Why it's worth the effort:** multi-perspective insight, buy-in on hard choices, more realistic
budgets, more ownership, and less overhead than top-down budgeting.

## Epics: hypothesis, business case, MVP

**Epic hypothesis statement:**

| Field | Content |
|---|---|
| Funnel entry date | For ageing in the Kanban |
| Epic name / owner | — |
| Description | Elevator-pitch value statement: *For* <customers> *who* <do something> *the* <solution> *is a* <how> *that* <value> *unlike* <alternative> *our solution* <does better> |
| **Business outcome hypothesis** | Measurable benefit if the hypothesis holds (e.g. "+50% shoppers under 25", "availability 95% → 99.7%") |
| **Leading indicators** | Early measures that predict the outcome (innovation accounting) |
| NFRs | Constraints that apply |

**Lean business case** (sections in the toolkit template): owner and stakeholders, description,
outcome hypothesis, leading indicators, in scope / out of scope, NFRs, **MVP features**, additional
potential features, analysis summary, **go / no-go**, then solution analysis (customers affected;
impact on solutions, programs and services; sales, distribution, deployment and support), cost
estimates (MVP and full), development type (build, buy, partner) and incremental implementation
strategy.

**Forecasting an epic** (toolkit what-if tool): per ART, take the ART's share of the epic's story
points and divide by (historical PI velocity × % of capacity allocated to the epic) to get the number
of PIs. Use low and high estimates to produce a range.

**After the MVP:** pivot, persevere or stop, decided at the Strategic Portfolio Review against the
leading indicators.

## LPM events

| | **Strategic Portfolio Review (SPR)** | **Portfolio Sync** | **Participatory Budgeting** |
|---|---|---|---|
| Purpose | Define and optimise the portfolio: balance short/long term, risk, cost | Operational visibility and decentralised execution support | Allocate value stream budgets |
| Cadence | **Quarterly** (per PI, often mid-PI) | **Monthly** (the SPR replaces it in SPR months) | ~**Twice a year** |
| Facilitation | APMO | APMO | LPM |
| Required | Senior leaders, BOs, Enterprise Architect, solution portfolio manager | Senior leaders, BOs, APMO, LACE | LPM fiduciaries, BOs, Epic Owners, PM, architects |
| Optional | Epic Owners, PM/Solution Mgmt, RTEs | RTEs, SM/TCs, Epic Owners | — |
| Typical agenda | Portfolio context; vision and canvas; strategic themes/OKRs; horizon and other guardrails; portfolio metrics and KPIs; portfolio roadmap; **MVP pivot/persevere/stop**; **approve and prioritise epics** | Lean metrics; in-flight epics and MVPs; advancing epics through the Kanban; impediments; cross-value-stream dependencies and releases; roadmap update; improvement backlog; decisions | See above |

**Best practices (both events):** fixed cadence; Kanban updated *before* the meeting; pre-read data
summary (MVP results, value stream KPIs); value stream reps (BOs, PM, RTE) present; rotate the agenda
focus rather than running the same agenda every time.

**Anti-patterns (both):** ad hoc scheduling; inconsistent attendance; status updates instead of
decisions; no facilitator, so it overruns; no usable metrics; tech or business not represented;
decisions not communicated; vision and canvas never updated.

**Calendar pattern (LPM events calendar template):** iterations follow a three-step rhythm: Portfolio Sync, Portfolio Sync, then SPR + participatory budgeting. *(This is the toolkit template. In practice PB runs about twice a year, not every SPR.)*

## Lean governance: CapEx / OpEx

Software capitalisation is a common LPM blocker, because Finance fears losing CapEx under Agile.

- **Disclaimer.** Rules vary by country, industry and company policy. Involve the financial authority
  early. US references: FASB 86 for software for sale; SOP 98-1 / ASC 350-40 for internal-use software.
  IFRS (IAS 38) applies in Europe *(to verify per client)*.
- **Typically expensed:** feasibility research, prototyping, alternatives analysis, high-level
  architecture for decision-making, training, production maintenance and support.
- **Potentially capitalisable:** committed new functionality and upgrades that increase functionality,
  including salaries, materials, contract labour and directly attributable burden. G&A and overhead are
  excluded.
- **Under waterfall,** capitalisation started after requirements and design established feasibility
  and management committed funding.
- **Under SAFe:**
  - Exploration and spikes (epics in analysis, enabler exploration) are OpEx.
  - New feature work is potential CapEx. Tag features for CapEx treatment.
  - Maintenance and defects are OpEx.
  - Allocate by **story hours** (hours on stories under CapEx-typed features ÷ total hours) or by
    **story points** (same ratio using points).
- **TBM (Technology Business Management) white paper:** pairs SAFe with TBM's cost taxonomy to give a
  "bill of IT" in business terms. PMs then own both run-the-business and change-the-business spend.
  Useful framing with CIOs and CFOs.

## LPM performance measures (Executive Workshop example)

| Goal | Measure |
|---|---|
| Employee engagement | Engagement surveys, Agile people-ops data |
| Customer satisfaction | NPS |
| Partner health | Partner and vendor surveys |
| Business agility | Business Agility self-assessment |
| Portfolio performance | OKRs; LPM self-assessment |
| Value stream performance | Value stream KPIs |
| *(6.0)* Flow | Portfolio-level flow metrics, see [[metrics-and-assessments]] |

## LPM implementation readiness (15-point checklist, restated)

1. LPM people trained (Leading SAFe + LPM).
2. Value streams and ARTs identified; portfolio organised around value.
3. Strategic themes with key results.
4. Portfolio Kanban with exit criteria, WIP limits and **epic threshold**.
5. Portfolio vision and canvas (current/future).
6. People named for each LPM collaboration.
7. Value stream budgets established.
8. Guardrails set: horizon %, capacity allocation, epic threshold, BO engagement.
9. Portfolio Sync and SPR cadence, attendees, agenda and outcomes defined.
10. PB parameters set: cadence, dates, participants, inputs.
11. **Projects-to-products transition plan:** PMO, Finance and Accounting engaged; impacted systems
    and reports identified; HR and people managers engaged.
12. Epic hypothesis template adapted.
13. Lean business case template adapted.
14. LPM tooling chosen.
15. LPM metrics agreed.

## Use it as…

- **PL:** LPM is where a CPO gets real authority. Push for value-stream funding plus guardrails, and
  use epic hypotheses and MVPs to make bets explicit. Your portfolio language is OKRs, horizons and
  leading indicators.
- **PgM:** the APMO is the evolution path for a classic PMO. Own the Portfolio Sync, epic forecasting
  and continuous compliance coordination.
- **TC:** item 11 (projects to products) is the real change. Engage Finance on CapEx and budget
  cadence *early*, and use the TBM framing with CFO and CIO. For banks and asset managers, capitalisation
  and audit trail are the first objections you will hear.

## Related

[[artifacts-and-backlogs]] · [[events-and-cadence]] · [[metrics-and-assessments]] · [[regulated-environments]] · [[transformation-playbook]]
