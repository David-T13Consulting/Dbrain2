---
classification: internal
status: draft
updated: 2026-10-01
tags: [safe, metrics, flow, assessments, measure-and-grow, lens/pgm, lens/tc]
---

# Metrics and assessments

What to measure at team, ART, portfolio and transformation level, plus how to run Measure and Grow.
Built from the PI Execution and Iteration Execution metric templates, the predictability workbook,
the Assessments/Measure and Grow toolkit and the DevOps deck, then updated to the 6.0 measurement model.

## [6.0] The measurement model: three domains

| Domain | Question | Examples |
|---|---|---|
| **Outcomes** | Are we delivering business results? | OKR key results, value stream KPIs, NPS, revenue, cost, employee engagement |
| **Flow** | How efficient is delivery? | The six flow metrics below |
| **Competency** | How proficient are we? | Measure and Grow assessments (core competencies, now organised by discipline [2024+]) |

The 5.1 toolkits mix velocity, predictability, quality counts and early flow metrics in one template.
6.0 replaced that with these three domains and made **flow** the lead operational signal.

## The six flow metrics [6.0]

| Metric | Definition | Use it to see | Watch-out |
|---|---|---|---|
| **Flow distribution** | Share of work items by type (features, enablers, defects, risks/debt) | Whether capacity allocation is respected | Defects crowding out features |
| **Flow velocity** | Number of items completed per period | Throughput trend | Not comparable across teams |
| **Flow time** | Elapsed time from start (or request) to done | Speed / lead time | Long tails hide in averages; use percentiles |
| **Flow load** | Items in progress (WIP) | Overload, which predicts long flow time (Little's law) | High load + low velocity = multitasking |
| **Flow efficiency** | Active time ÷ flow time | Waiting and handoffs | Often 10–20% in traditional orgs |
| **Flow predictability** | Planned vs actual business value (the predictability measure) | Reliability, i.e. trust | Gaming by sandbagging objectives |

## Predictability (toolkit workbook)

- Each team's **committed** objectives carry planned BV (1–10, set by BOs at PI Planning).
- At the end of the PI, BOs score **actual** BV for *all* objectives, including uncommitted ones.
- Team achievement % = Σ actual (committed + uncommitted) ÷ Σ planned (committed only).
- ART predictability = average, or roll-up, of team achievement. **Target band: 80–100%.**
- Read the **trend across PIs**, per team and per ART. A first PI at 50–60% is normal; the goal is to
  get into the band and stay there.
- Coaching point from the toolkit: ask "how do we raise this number without taking our foot off the
  gas?" The answer is better planning, smaller batches and fewer dependencies, not padding.

## Iteration and ART metric templates [5.1]

| Iteration metrics (team) | ART performance metrics (per PI) |
|---|---|
| Stories loaded / accepted / % accepted / not accepted (pushed, deferred, deleted) / added mid-iteration (target 0) | ART velocity; predictability %; business and enabler features planned vs accepted; stories planned vs accepted |
| % stories with automated test; defects at start and end; new tests (automated vs manual); % automated; unit test coverage | Unit test coverage %; open defects; total tests; % automated; NFR tests |
| Flow distribution (stories / enablers / defects) | Flow distribution; flow time (features); flow efficiency |

Use them as a starting kit. In 6.0, report flow metrics plus predictability, and keep quality metrics
as team-level diagnostics.

## Continuous Delivery Pipeline metrics

From the DevOps deck:

- **Lead time vs process time per CDP step**, and **%C&A** (percent complete and accurate) per step.
  The value stream mapping core.
- **Deploys and releases per PI**, for trend.
- **Cumulative flow diagrams**, to spot bottlenecks.
- **Pipeline efficiency**, i.e. flow efficiency end to end.
- **Innovation accounting**: leading indicators per feature or epic hypothesis.
- **Full-stack telemetry and BVIRs** (big visible information radiators): time since last outage,
  response times, usage, utilisation.
- **[AI-Native] CALMR governance metrics** cited for AI-augmented delivery: deployment risk, lead
  time for fixes, defect severity, MTTR *(to verify)*.

## Portfolio and transformation metrics

- **LPM measures:** employee engagement, NPS, partner health, Business Agility assessment, OKRs +
  LPM self-assessment, value stream KPIs. See [[lean-portfolio-management]].
- **LACE KPIs:**
  - **Adoption:** % trained, ARTs launched, value streams on SAFe.
  - **Assessment:** Business Agility, DevOps health radar.
  - **Outcome:** % improvement in predictability, time to market, productivity, engagement and
    customer satisfaction.

  Balance adoption metrics (easy to game) with outcome metrics (what executives pay for). See
  [[transformation-playbook]].

## Measure and Grow

**Definition:** how a portfolio evaluates its progress toward business agility and chooses its next
improvement steps. **Measure** means running the assessments. **Grow** means turning the results into
improvement backlog items.

### The assessments

| Assessment | Scope | Structure |
|---|---|---|
| **Business Agility assessment** | All competencies, high level | ~6 statements per competency (the "new" v2 version is terminology-agnostic and simpler than the original v10) |
| **Core competency assessments** (×7) | One competency in depth | Statements grouped into the competency's dimensions |
| **DevOps Health Radar** | CDP maturity | CE / CI / CD / RoD sub-dimensions |

**[2024+]** The assessments were renamed to follow the five SAFe Disciplines. **[AI-Native]**
Online assessments sit in Comparative Agility, with an AI "SAFe CoPilot" suggesting next steps
*(to verify)*.

**Scale:** 5 points plus N/A (True / More true than false / Neither / More false than true / False).
It is easy to answer and doesn't force either/or. Caveats from the toolkit: people **score themselves
higher**, and the same score can hide **different reasoning**. So always discuss results; don't just
average them.

**Example statements** (paraphrased from the Business Agility assessment, useful as interview probes):

- *TTA:* people trained; cross-functional teams; teams of teams organised around solutions with
  end-to-end skills.
- *APD:* customer-centric definition; customer validation throughout; plan together on cadence;
  regular integrated demos; release as needed; ongoing investment in delivery infrastructure.
- *ESD:* multi-horizon roadmaps; emergent requirements; intentional + evolutionary architecture;
  **incremental compliance**; suppliers in the agile process; update deployed solutions on demand.
- *LPM:* vision communicated; work aligned to vision; **economic framework for prioritisation**;
  moving away from project funding; funding reviewed on cadence; outcome metrics; execution patterns
  shared.
- *LAL:* compelling change vision; authenticity; openness; personal advocacy; decisions moved to the
  information; obstacles removed.
- *OA:* fast strategy change; MVP-first for large investments; end-to-end flow visualised; delays
  addressed; business teams agile; continuous feedback instead of annual reviews.
- *CLC:* relentless improvement; data over opinion; time for innovation; safe experimentation;
  investment in growth; purposeful learning sharing.

**Agile Product Delivery assessment dimensions** (example of the depth available):

- **Customer centricity and design thinking:** segments, market research, Gemba, vision → roadmaps,
  value proposition, 1–3 year solution roadmap, PI roadmap, whole-product model, personas, empathy
  maps, journey maps, story maps, capacity allocation.
- **Develop on cadence, release on demand:** PI Planning quality and participation, ART Kanban WIP,
  WSJF, feature benefits, BO value scoring, I&A follow-through, IP iteration use, iteration ≤2 weeks,
  System Demo every iteration, ART board, **80–100% predictability**, release any time, release on
  market rhythms.
- **DevOps and the CDP:** defined CDP, shared dev/deploy/ops responsibility, per-step timing metrics,
  recovery, CI on every commit, test automation, trunk-based development, security in the pipeline,
  code/dependency scanning, production-like staging, continuous promotion, deploy ≠ release, targeted
  releases, build automation, everything in version control.

### Running Measure and Grow

| Phase | Guidance |
|---|---|
| **When** | Scenario 1: business agility **baseline** at the start. Scenario 2: **ART effectiveness** (APD + TTA) after 2–3 PIs. Scenario 3: **accelerate** (deep dive on the weakest competencies) |
| **Prepare** | Who participates (cross-role, cross-level); facilitated or self-assessment; anonymity; spreadsheet or online tool; preparation checklist in the toolkit |
| **Facilitate** | Explain the scale and the why; make sure each statement is understood in context ("What does this mean for us? Why is it desirable? Whose responsibility is it?") |
| **Analyse** | Radar charts by competency or dimension; look at **spread between roles** (for example leaders vs teams), not just means; compare with the previous baseline |
| **Grow** | Pick a few improvement opportunities → items in the LACE or ART backlog → re-assess next cycle. Celebrate gains |

## Use it as…

- **PgM:** run a PI dashboard of predictability (trend) + the six flow metrics + 2–3 quality signals.
  At I&A, explain *why* each metric matters before showing numbers.
- **PL:** outcomes are your domain. Tie every epic to leading indicators and every PI to key results.
  Flow time for features is your customer-responsiveness metric.
- **TC:** Measure and Grow gives an engagement both its diagnostic and its proof of value. The
  Business Agility baseline is a natural paid discovery deliverable, and re-assessment after 2–3 PIs
  shows the delta.

## Related

[[pi-planning-and-execution]] · [[lean-portfolio-management]] · [[transformation-playbook]] · [[devops-and-architecture]]
