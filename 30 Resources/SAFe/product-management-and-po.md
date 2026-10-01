---
classification: internal
status: draft
updated: 2026-10-01
tags: [safe, product-management, product-owner, lens/pl]
---

# Product Management and Product Owner

The product system inside SAFe: how a market need becomes an accepted story, and who holds content
authority at each step. This is the Product Leader's home page.

## The PM ↔ PO system

| | **Product Management (ART)** | **Product Owner (team)** |
|---|---|---|
| Faces | Market, customers, Business Owners, Solution Mgmt | The team, plus PM |
| Owns | Vision, ART roadmap, **ART backlog**, features, WSJF, release decisions | **Team backlog**, stories, acceptance |
| Time horizon | Next 1–3 PIs, plus a longer roadmap | This PI, next iteration |
| Accepts | Features | Stories |
| Key events | PI Planning (vision briefing), PO Sync, System Demo, SPR inputs | Iteration planning, refinement, review, PO Sync, PI Planning breakouts |
| Ratio | ~1 PM per 3–5 POs is a common rule of thumb *(to verify for 6.0)* | 1 PO per 1–2 teams |
| Main failure | Throws requirements over the wall; acts as super-PO | Proxy PO with no authority; absent; domain expert overriding the team |

**Mental model:** PM decides *which outcomes and features, in which order*. PO decides *which slices,
in which order, and when they're done*. If the PO is re-prioritising features, or the PM is writing
stories, the system has failed.

## From market need to accepted story

1. **Continuous Exploration** (first stage of the CDP). Hypothesise → collaborate and research →
   architect → synthesise. Product Management leads, with the architect and customers.
2. **Customer centricity and design thinking toolset.** Market segmentation, personas, empathy maps,
   journey maps (across the operational value stream), story maps, Gemba visits, whole-product model.
3. **Epic** (if large) → hypothesis + lean business case + MVP. See [[lean-portfolio-management]].
4. **Feature.** Short name + **benefit hypothesis** + acceptance criteria. Sized to fit one PI.
5. **WSJF ranking** in the ART backlog, done collaboratively at PO Sync. See [[artifacts-and-backlogs]].
6. **PI Planning.** PM briefs the vision and the **top ~10 features**. Teams break features into stories.
7. **Iterations.** PO refines, splits, and accepts stories. The team demos at Iteration Review.
8. **System Demo.** PM sees integrated features and accepts them.
9. **Release on demand.** PM decides when to expose value to users (deploy ≠ release).
10. **Measure.** Innovation accounting: did the leading indicators move? Pivot or persevere.

## Writing features

**Feature template** (adapted from the Day-1 briefing "Top 10 features" template):

| Field | Guidance |
|---|---|
| Name | 1–3 words, a business phrase rather than a component name |
| Benefit hypothesis | "We believe <this feature> will result in <measurable outcome>, which we will know when <leading indicator>" |
| Acceptance criteria | 3–6 testable statements, including NFR impacts |
| Type | Business or enabler |
| WSJF inputs | Value, time criticality, RR|OE, size |

**Vision formats** for PI Planning briefings: rolling-wave briefing, vision document, preliminary
data sheet, or **draft press release** (Amazon-style). The press release forces outcome language.

## Writing stories: INVEST

| Letter | Meaning | Practical test |
|---|---|---|
| **I**ndependent | Can be built and accepted on its own; slice vertically | No "story B needs story A in the same iteration" |
| **N**egotiable | A statement of intent, not a contract | Detail lives in the conversation and the acceptance criteria |
| **V**aluable | Valuable to a user, in the user's voice | "Refactor the logging system" → "As a consumer I get a consistent, clear error message so I know what to do" |
| **E**stimable | The team can size it | If not, run a spike (domain or technical) |
| **S**mall | Fits in an iteration, ideally a few days | If over ~8 points, split |
| **T**estable | Has acceptance criteria | "Results return quickly" → "first page in ≤3 s" |

## Ten ways to split a feature or story

| # | Pattern | Example shape |
|---|---|---|
| 1 | **Workflow steps** | Publish pricing to the in-home display → to the web portal → to the smart thermostat |
| 2 | **Business-rule variations** | Sort customers by zip → by demographics → by consumption |
| 3 | **Major effort** | First variant carries the infrastructure. Later variants are cheap |
| 4 | **Simple / complex** | "Simplest version that could possibly work" first |
| 5 | **Variations in data** | Messages in Spanish → Arabic → … |
| 6 | **Data entry methods** | Simple form first, rich UI later |
| 7 | **Defer system qualities** | Correct first, then fast / scalable |
| 8 | **Operations** (CRUD) | Create → read → update → delete |
| 9 | **Use-case scenarios** | Happy path first, then alternates |
| 10 | **Break out a spike** | Learn first, then build |

## Normalised estimating (first PI only)

When an ART starts, there is no shared velocity. Normalise estimates with this toolkit rule:

1. Give each team **8 points per iteration per full-time developer or tester** (minus PTO and other
   time off).
2. A story that takes about a day is 1 point. Size the rest relative to it.
3. Split anything above 8 points.

This gives right-sized stories and comparable points across teams, which you need for feature and
epic forecasting. Drop it once real velocities exist.

## PO Sync: the product team's weekly room

From the PO Sync guide and FAQ:

- **Purpose:** progress toward PI objectives, scope changes, and feature development problems or
  opportunities.
- **Cadence and timebox:** weekly, 30–60 min, facilitated by the RTE or PM.
- **Rotate themes:** feature check-ins, mid-PI scope adjustment, PI objective risk review, WSJF
  scoring for the next PI.
- **Diagnostic questions:** Is any feature or objective at risk? Is any team short of capacity? Where
  can work be shifted or re-scoped?
- **Failure signs:** nobody brings enabler detail (invite the SA); updates run long (meet more often,
  facilitate tighter); attendance drops (state the purpose, add variety, run a retro on the sync itself).

## Release on demand: product levers

- **Separate deploy from release.** Feature toggles, dark launches, canary releases, and releasing to
  specific user segments.
- **Decouple release elements.** Different parts of the solution release at different rhythms, for
  example UI every two weeks, security patches as needed, major capabilities per PI or market event.
- **Exploit market rhythms.** Time releases to trade shows, fiscal events and regulatory windows.

## [6.0] and later shifts relevant to product leaders

- **OKRs** run through strategy, portfolio and ART levels. PI objectives can be framed as OKRs.
- **Flow metrics** for product: flow time and flow predictability for features (see [[metrics-and-assessments]]).
- **[2024+] Product Development Flow** is now a named discipline. Product is a first-class concern in
  the framework, not a sub-topic of Agile Product Delivery.
- **[AI-Native]** *Intent declarations* ("reduce decision latency on X", not "add AI") and *outcome
  trees* that connect portfolio OKRs to team outcomes. Directionally aligned with outcome-based product
  management. *(to verify)*

## Use it as…

- **PL (primary):** run the PM role as a *portfolio of bets*. Every feature carries a benefit
  hypothesis and every epic an MVP plus leading indicators. Your credibility comes from predictability
  plus outcomes, not output.
- **PgM:** the PM/PO split is where most escalations come from. Use the table above to settle disputes.
- **TC:** PO capability is usually the binding constraint in a transformation. Budget PO training and
  coaching *per team*, and source POs from BAs before reaching for SMEs.

## Related

[[artifacts-and-backlogs]] · [[pi-planning-and-execution]] · [[lean-portfolio-management]] · [[roles]] · [[metrics-and-assessments]]
