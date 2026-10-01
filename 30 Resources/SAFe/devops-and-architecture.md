---
classification: internal
status: draft
updated: 2026-10-01
tags: [safe, devops, architecture, built-in-quality, large-solution, lens/pgm]
---

# DevOps, architecture and large solutions

The technical delivery system behind the ART: the DevOps approach (CALMR), the Continuous Delivery
Pipeline, Lean-Agile architecture, built-in quality, and how SAFe handles very large systems. Built from
the Scalable DevOps, Lean-Agile Architecture and Building Really Big Systems toolkits.

## DevOps: the problem and the CALMR approach

The underlying conflict: the business wants features *now*, Dev wants to go faster, Ops wants
stability. **DevOps** is a mindset, culture, set of principles and technical practices that deliver
value faster, routinely and reliably, across Dev, Ops, Security, Compliance, Architecture and the
business.

The deck cites *The DevOps Handbook*: high performers deploy **30× more often** with **200× shorter
lead times**, **60× fewer failures** and **168× faster recovery** (dated figures, good as an order of
magnitude).

| CALMR | Practice | Signals of maturity |
|---|---|---|
| **C**ulture | Shared responsibility for dev, deploy and operate; tolerate failure, recover fast; share learning across silos | Devs on call; blameless postmortems |
| **A**utomation | Automate the CDP with an integrated toolchain. **Fix a broken process before automating it** | One-click deploys; IaC |
| **L**ean flow | Small batches, limited WIP, short queues, extreme visibility | Trunk-based development; WIP limits on ART Kanban |
| **M**easurement | Flow through the pipeline; full-stack telemetry (business, app, infra, client) per stakeholder | BVIRs, federated monitoring |
| **R**ecovery | Low-risk releases; stop-the-line; plan and rehearse failure; roll back and fix forward | Feature toggles, canaries, MTTR tracked |

## Continuous Delivery Pipeline (CDP)

| Aspect | Sub-activities (6.0 wording) | Who leads | Key practices |
|---|---|---|---|
| **Continuous Exploration (CE)** | Hypothesise → collaborate and research → architect → synthesise | PM + SA | Lean startup, design thinking, MVPs, roadmap, ART backlog |
| **Continuous Integration (CI)** | Develop → build → test end-to-end → stage | Teams + system team | Version control, automated builds, test automation, staging ≈ production |
| **Continuous Deployment (CD)** | Deploy → verify → monitor → respond | Teams + Ops | Deploy to prod behind toggles, smoke tests, telemetry, incident response |
| **Release on Demand (RoD)** | Release → stabilise → measure → learn | PM + BOs | Decouple deploy from release; release by segment; innovation accounting |

Key ideas:

- **Develop on cadence, release on demand.**
- **Decouple release elements.** Different "value streamlets" release at different rhythms, for example
  end-user functionality every two weeks, security updates as needed, major capabilities per market event.
- **Separate deployment from release** with feature toggles and dark launches.

## Lean-Agile architecture

**Architect roles span domains** (business, information, application, technical):

| SAFe role | Scope |
|---|---|
| **Enterprise Architect** | Across value streams: technology strategy, enabler epics, portfolio runway |
| **Solution Architect** | Across systems in a Solution Train: solution intent, cross-ART design |
| **System Architect** | A single system / ART: runway, enablers, NFRs, PI Planning architecture briefing |

**Organising around value: the architecture angle:**

- **Conway's law:** systems mirror the communication structures of the organisation that builds them.
- **Inverse Conway manoeuvre:** design the team and ART structure to produce the architecture you want.
- **Team topologies [6.0]:** stream-aligned, complicated-subsystem, platform and enabling teams. The
  same patterns apply at ART level (stream-aligned, complicated-subsystem and platform ARTs).
- **Fracture planes** (natural seams for splitting systems and teams): business-domain bounded context
  (DDD), regulatory compliance, change cadence, team location (weakest), risk/performance isolation,
  technology, user personas.
- Architects belong in the **VSAIW**. Without them, ART designs ignore system coupling.

**Architectural runway:** existing code, components and infrastructure that let near-term features be
built without excessive redesign. Built through **architecture enablers** and consumed by features.
With too little runway, velocity peaks and then falls; with too much, it is waste.

**Solution intent:** the single source of truth for current and intended solution behaviour.

- **Fixed vs variable:** what is decided and what is still being explored.
- **Minimum sufficient documentation:** prefer models over documents; keep it collaborative; defer
  decisions to the latest responsible moment; document each item once; stay high level.
- **MBSE** (model-based systems engineering) for complex and cyber-physical systems.
- It supports compliance, contracts and traceability (see [[regulated-environments]]).

**Set-based design:** explore several design options in parallel and converge on the optimum. This
avoids "false predictability" from fixing a point design early. Toolkit example: exploring lidar,
optical and radar for an obstacle-detection decision.

**Architect Sync:** weekly, 30–60 min, facilitated by the STE or chief architect. Covers enabler
progress, design reviews, significant design issues, runway backlog, and risks to the long-term
vision. Feeds the ART Sync. See [[events-and-cadence]].

## Built-in quality

- **5.1:** a core value plus five dimensions: flow, architecture and design quality, code quality,
  system quality, release quality.
- **6.0:** no longer a core value, but still an essential Team and Technical Agility practice.
- **Practices:** XP (TDD, BDD, pair work, collective ownership, refactoring, CI), shift-left testing,
  definition of done at every level, and **automated compliance tests in the same iteration as the
  functionality**.
- **"Give teams automated scripts instead of checklists."** Include safety, security and performance
  tests in the DoD.

## Building really big systems (Large Solution / ESD)

The **Enterprise Solution Delivery** competency (**[2024+] Large Solution Integration and Delivery**
discipline) has three dimensions:

1. **Lean systems and solution engineering**
2. **Coordinating trains and suppliers**
3. **Continually evolving live systems**

**Nine practices** (Building Really Big Systems toolkit):

| Practice | What it means |
|---|---|
| Continually refine the **fixed/variable solution intent** | Know the goal (regulatory and existing systems are fixed), and let the rest emerge through backlogs and workshops |
| Apply **multiple planning horizons** | Multi-year vision/epics → 3–4 PI roadmap → committed PI. Solution roadmap drives ART roadmaps, with feedback upward |
| **Architect for scale, modularity, releasability, serviceability** | Decouple components through well-defined interfaces so ARTs can build, test and release independently |
| **Continually address compliance** | Lean QMS; automated V&V and traceability; see [[regulated-environments]] |
| Build and integrate with **ARTs and Solution Trains** | Solution Train roles (STE, Solution Mgmt/Arch), Pre/Post-PI Planning, Solution Demo |
| Apply **"continuish" integration** | When true CI is impossible (hardware, suppliers), integrate on a fixed frequent cadence and use simulation, emulation and mocks |
| **Manage the supply chain** with systems-of-systems thinking | Suppliers on cadence, in PI Planning, with agile contracts |
| Build a **CDP for large solutions** | Pipeline spanning ARTs and suppliers |
| **Evolve deployed systems** | Design for upgrade in service, telemetry and recovery |

Planning tip: keep **teams and ARTs stable** and align work to their expertise (rows by ART on the
roadmap). T- and E-shaped skills make stable-team planning easier.

## Use it as…

- **PgM:** the CDP and CALMR are your improvement backlog. Measure lead time per CDP step and attack
  the biggest delay each PI. Protect enabler capacity through capacity allocation.
- **PL:** release on demand is a product lever: feature toggles and segment releases let you run real
  experiments. The architectural runway is a product investment; negotiate it, don't fight it.
- **TC:** use the inverse Conway manoeuvre and fracture planes in the VSAIW. In regulated or large
  cyber-physical clients (med tech, core banking), the nine big-system practices are the credible story.

## Related

[[events-and-cadence]] · [[regulated-environments]] · [[metrics-and-assessments]] · [[artifacts-and-backlogs]] · [[transformation-playbook]]
