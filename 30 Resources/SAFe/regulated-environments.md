---
classification: internal
status: draft
updated: 2026-10-01
tags: [safe, compliance, regulated, banking, medtech, lens/tc]
---

# SAFe in regulated environments

How SAFe handles compliance, and how to argue it with risk, quality and compliance functions in
banking, asset management, healthcare and medtech. SAFe mechanics come from the Regulatory and
Compliance toolkit and the 2017 compliance white paper. The industry mapping at the end is general
knowledge, marked *(to verify)*. This is David's niche: regulated-industry delivery.

## The core argument

1. **Two communities, two value systems.** Compliance values specifications, V&V, objective evidence,
   audits and sign-offs, and treats *change as risk*. Agile values working systems, collaboration and
   responding to change, and treats *change as opportunity*. The business needs both.
2. **Regulations say *what*; the organisation decides *how*.** Most "we must do waterfall" constraints
   live in the **QMS's interpretation** of the regulation, which is "more lore than fact". Leffingwell's
   line is that a single-pass waterfall mandate is "an industry myth".
3. **Waterfall creates compliance debt.** It produces late V&V, a large bow wave of testing and compliance
   work at the end, missed windows, and no chance to learn from compliance findings. Like technical
   debt, it compounds.
4. **SAFe's answer is to make compliance part of flow:** build and comply incrementally, organise for
   value *and* compliance, build quality and compliance in, verify and validate continuously.

## Two types of compliance requirement

| Type | Governs | Examples (from the toolkit) | Where it lands in SAFe |
|---|---|---|---|
| **Product** (solution) | Function and performance of the product | PCI DSS: encrypt sensitive data in transit; vehicle braking distance at a given speed | NFRs, features, acceptance criteria, solution intent |
| **Process** (QMS) | Development rigour: analysis, steps, documentation, reviews | FDA 21 CFR 820: documented SRS as the V&V baseline; ISO 15504 / ASPICE: independent QA assurance | Definition of Done, compliance enablers, Lean QMS policies |

## The four SAFe practices for compliance

### 1. Build the solution and compliance incrementally

- Compliance standards require specifications to *exist*, not to be written *up front*.
- Specifications evolve with the system in small batches, with continuous review.
- Each PI is a PDCA cycle and produces **objective evidence**: solution progress, compliance progress
  (quality, compliance, manufacturability), customer and regulatory feedback, and improvement stories.

### 2. Organise for value and compliance

- Value streams and ARTs include **QA, security, testing, V&V and even IV&V** as members, or as shared
  services where independence rules require it (independence is achieved through reporting lines and
  incentives, not by sitting outside the ART).
- Compliance people **attend ART events**. PM makes sure the ART backlog reflects compliance priorities.
  Teams plan compliance work at PI Planning. I&A looks for better ways to build compliance into flow.

### 3. Build quality and compliance in

- **Lean QMS:** compliance experts and teams co-design how evidence is produced, and the QMS itself
  improves at each PI.
- **Automate compliance** inside the design-build-test pipeline: traceability, static analysis,
  security scans, automated approvals, test evidence capture.
- Manual reviews and audits that remain become **backlog work in small batches** (stories and
  enablers), so that **final sign-off becomes "a quick, boring non-event"**.
- Track **code coverage, requirements coverage and traceability completeness every iteration**,
  focusing on *trends*.

### 4. Continuously verify and validate

- **Verification:** "we built the solution right", meaning it matches the specifications in the backlog
  and solution intent.
- **Validation:** "we built the right solution", meaning fitness for use, confirmed by POs, customers,
  UAT and end users at demos.
- **Compliance:** "and we have objective evidence".
- **Solution intent** holds requirements, models and **traceability**, which evolve with the system.
- **Requirements meta-model:** every requirement type has tests. Compliance work appears in two places:
  - in the **Definition of Done** (e.g. "every story peer-reviewed", "impacted requirements revisited
    for each feature");
  - as **compliance enablers** in the backlog (e.g. a "design review" enabler whose DoD requires actions
    to be recorded and resolved).
- **System Demo** every iteration gives objective evidence of integration. The **PI System Demo**
  includes compliance results (reviews, audits, milestone events such as a clinical trial or flight
  test). The **IP iteration** gives time for integrated assessment and metrics.
- **I&A** asks: are we on track for certification milestones? Are compliance procedures blocking flow?

## Releasing in high-assurance environments

Final release may still need extra steps: final documentation and evidence package, baseline and
archive the configuration, final testing in the operational environment (possibly witnessed by
assessors), and internal or external approvals. Because quality and compliance were built in, these
become routine rather than months-long events.

## Industry mapping *(general knowledge, to verify per client)*

| Domain | Typical regimes | SAFe hooks |
|---|---|---|
| **EU/US banking** | DORA (EU ICT risk and resilience, incl. testing and third-party risk); EBA ICT/outsourcing guidelines; SR 11-7 (US model risk); SOX ITGC (change management, segregation of duties); PCI DSS; GDPR; BCBS 239 (risk data) | Compliance and resilience enablers; automated change evidence in the CDP instead of manual CAB; SoD enforced by pipeline permissions; model validation as enablers and DoD for model features; third-party/supplier ARTs on cadence |
| **US asset management** | SEC/FINRA rules; SOX; SOC 1/2 controls; vendor risk | Control evidence generated by the pipeline; audit trail via ALM traceability; LPM lean governance with audit participation |
| **Medtech / SaMD** | EU MDR 2017/745 / IVDR; IEC 62304 (software lifecycle); ISO 13485 (QMS); ISO 14971 (risk); IEC 62366 (usability); FDA QMSR (21 CFR 820 aligned with ISO 13485); AAMI TIR45 (agile for medical device software); EU AI Act for AI-enabled devices | Solution intent as the design history file backbone; risk management as continuous enablers; V&V per increment; IV&V as shared service; release package as an explicit final step |
| **Belgian healthcare IT** | GDPR + national health data rules; eHealth platform and homologation obligations | See [[30 Resources/Belgian Healthcare & eHealth/README\|Belgian Healthcare & eHealth]]; homologation tests as compliance enablers and release criteria |

## Objections you will hear, and answers

| Objection | Answer grounded in SAFe |
|---|---|
| "The regulator requires a full spec up front." | It requires a spec to exist and be the V&V baseline, not that it's written first. Show solution intent with traceability that evolves per PI |
| "Auditors need sign-offs." | Sign-offs still happen, in small batches and in the DoD. Final sign-off becomes routine |
| "QA must be independent." | Independence is achieved through reporting and incentives. Participation in the ART is what makes it effective |
| "Our CAB needs to approve every change." | Move to risk-based, automated change evidence in the CDP. Keep human approval for high-risk changes |
| "Agile means no documentation." | SAFe means *minimum sufficient* documentation: models over documents, a single source of truth |

## Use it as…

- **TC (primary):** lead with "regulations define *what*, your QMS defines *how*" and offer a **Lean
  QMS review** as an early engagement deliverable. It is a differentiated, regulated-industry offer
  that generic agile coaches can't make credibly.
- **PgM:** put compliance enablers and DoD items into PI Planning explicitly, and report compliance
  metric *trends* at every I&A.
- **PL:** treat compliance as product NFRs and solution-intent content. In medtech and SaMD the design
  history is part of the product.

## Related

[[devops-and-architecture]] · [[artifacts-and-backlogs]] · [[pi-planning-and-execution]] · [[lean-portfolio-management]] · [[transformation-playbook]]
