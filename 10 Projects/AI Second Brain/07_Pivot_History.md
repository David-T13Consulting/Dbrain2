---
classification: internal
note_type: synthesis
source: DECISIONS.md D1–D142, 02_Critical_Assessment.md, sovereignty-router-proposal-2026-10-19, agent-topology-proposal-2026-10-21 (Cowork synthesis, 21 Oct 2026)
review_status: unreviewed
created: 2026-10-21
updated: 2026-10-21
---
# Pivot history: the big decisions and why

**Purpose:** let David explain, in a client conversation, why the plan changed several times since 7 Sep 2026, and why that is evidence of method rather than drift. Synthesis of the decision log; the log stays the source of truth. **Unreviewed:** David to check the "why" wording before it is used client-facing.

## The 30-second version

> "The thesis never moved: the personal system is the substrate, the evaluation and governance layer is the product, and no client data goes in. What moved was *where the compute runs and how much process wraps it*. Each change was triggered by a measurement or by a cost I could see, and each decision was logged with the condition that would reverse it. When the condition fired, I reversed it. That is the governance I sell, applied to myself."

## What never changed (7 Sep → today)

| Constant | First set | Why it held |
|---|---|---|
| No client-confidential data in the system; demos on synthetic material | Standing rule, 7 Sep; contract-disclosure rule D16 | It is the gating constraint for a regulated-industry consultant |
| Governance = GTM: demo trustworthiness, not speed | Thesis, 7 Sep | It is the differentiator; everything else is substrate |
| Live system David drives, screen-shared | D1 | Highest credibility; forces a real vertical slice |
| Plain markdown + git, classification in frontmatter | D9 | Portable, auditable, makes multi-user a filter later |
| Agentic file search, no vector RAG | D5 | Right for a personal corpus; validated in 02_Critical_Assessment §2.1 |
| Running/Strava as the showcase domain, golden dataset as "receipts" | D14, D15, D7 | Real, frequent, checkable, and free of client data |
| David populates, Claude structures (fact-check gate) | D13 | Keeps the knowledge base trustworthy |

## The pivots

| # | Date | From → to | Trigger | Why (as recorded) | Decisions |
|---|---|---|---|---|---|
| 0 | 7 Sep | Webinar roadmap → own plan | Critical assessment of the Prisme One plan | Built for a solo creator, not a consultant with confidentiality duties; it missed security, evaluation, regulation and recovery. Instrumentation moved from phase 4 to a week 3 gate; servers out of scope; model choice deferred to evidence | D1–D8 |
| 1 | 8 Sep | Consulting-domain showcase → running | Evidence-led review of what David actually used notes and AI for | A real, frequent use case with checkable ground truth and no client data | D14, D15 |
| 2 | 1 Oct | 3-month read-only showcase → full personal platform (S1–S6): local models, phone, voice, always-on | David's goals made explicit after review; capacity raised to 20+ h/week | Local inference, cross-device access and voice were central goals; a travelling laptop cannot be always-on, so a dedicated host was planned | D45, D52–D56 |
| 3 | 1–12 Oct | Three agents writing freely → one lead, one queue, tiered reviews | Two stale branches and tangled uncommitted work in one day; then review loops eating runs | Ownership first (D63); then the process was lightened four times as reviews became the bottleneck | D63, D65, D70, D72, D77, D111, D112, D127, D128 |
| 4 | 1–8 Oct | Mac mini 24–32 GB, €800–1.5k → 64 GB, €3.7k, purchase approved | Sizing: 24 GB leaves no headroom for model, retrieval, speech and agents together | Bigger local models wanted; purchase gated on the T9 benchmark | D53, D92, D95, D107 |
| 5 | 9 Oct | Platform plan → same plan plus explicit end goal, audit gates G1–G4, calendars and mail, usable security | David restated the end goal ("usable for me", personal and work calendars and mail) | Gates give pass/fail release criteria; integrations come one connector at a time after security | D126 |
| 6 | 19 Oct | Buy hardware, run local → rent EU compute behind a sovereignty router (L0–L3); reuse Open WebUI; 1 review per step | T9 benchmark: a rented 27B+ model outclasses the local 4B; ~130 decisions and review loops had consumed most of the time since 12 Oct | Renting removes purchase, hardware ceiling and home ops; building blocks exist for most layers; **the router is the demonstrable governance product.** No hardware was bought | D134–D140 |
| 7 | 21 Oct | One big hosted cutover → three small, usable stages (Mac, Claude Code, hosted EU) | Need for usable wins sooner; stage 1 was mostly built | The three stages become the router's three levels (L0, L3, L1) on one vault, one query service, one eval set | D141 |
| 8 | 21 Oct | Idea of an organiser plus confidentiality agents and role agents → router + one runtime agent + skills; critical tier = local only | Research check (Anthropic 2026; Google/MIT scaling study; CaMeL) | Confidentiality enforced in code and logged, not in prompts; multi-agent costs 3–10x tokens and degrades sequential work | D142 |

## The pattern: three causes, not random change

| Cause | Pivots | What it shows |
|---|---|---|
| **Measurement overturned an assumption** | 6 (local 4B too weak), 8 (multi-agent evidence) | Decisions were set up to be overturned by data: D8 deferred the model choice to a benchmark on purpose |
| **Scope grew as goals became explicit** | 2, 5 | Early plan was a read-only showcase; David's real goal is a system he uses daily, by phone and voice |
| **Process cost became visible** | 3, 6 (review depth), 7 | Governance has a cost too; it was measured and cut each time it exceeded its value |

Every decision row carries a **"revisit when"** column. Pivot 6 is the cleanest example: D53 said "revisit if availability relaxes or memory use changes"; the benchmark changed the premise, so the purchase was reversed before money was spent.

## Hard questions to be ready for

| Question | Honest answer |
|---|---|
| "You approved a €3.7k host on 8 Oct and cancelled it on 19 Oct. Isn't that churn?" | The order was gated on a benchmark (D92). The benchmark showed rented models beat any model the box could run, so the gate did its job and no money was spent. Lesson (Cowork's reading, not in the log): compare renting with buying earlier |
| "L0 meant the Mac, then a rented GPU, then the Mac again." | True; D141 fixed it as "own machine". The level model itself (L0–L3) stayed stable; only its hardware example moved |
| "142 decisions in six weeks is a lot." | Yes. Most are small operational rules; the process was deliberately lightened in D77, D127 and D137. The big decisions fit on this page |
| "Why not just use Claude for everything?" | Retention terms changed in Aug 2026 (30-day default for business tiers); EU clients ask where data went. The router answers that per request, with a log line |

## Related
- [[10 Projects/AI Second Brain/DECISIONS|DECISIONS]] — full log, source of truth
- [[10 Projects/AI Second Brain/02_Critical_Assessment|02_Critical_Assessment]] — pivot 0
- [[10 Projects/AI Second Brain/02_Architecture/sovereignty-router-proposal-2026-10-19|Sovereignty router proposal]] — pivot 6
- [[10 Projects/AI Second Brain/02_Architecture/agent-topology-proposal-2026-10-21|Agent topology proposal]] — pivot 8
