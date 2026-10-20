---
classification: internal
archived: 2026-10-19
archive_reason: superseded by the 19 Oct pivot (D134-D140); kept verbatim below this banner
---
> **Archived 19 Oct 2026, verbatim.** This is the roadmap as it stood before the rent-not-buy pivot (D134–D140). The current version is [[10 Projects/AI Second Brain/04_Roadmap]].

# The Roadmap — Local Personal AI System, Operated and Demonstrated

**Amended 1 October 2026 at David's request.** The original rationale, H1/H2/H3 work packages and completed work are retained below. The delivery order in §0 replaces the original week-by-week schedule.

**Requirements closed later the same day (session 12, D52–D59):** devices, host availability, weekly capacity, numeric service targets and the source/metadata schema are now decided and recorded in §0. December 2026 is a schedulable target at 20+ h/week. Planning changes only — the always-on host is specified but not purchased.

**Supersedes** §5 of `02_Critical_Assessment.md`.
**Built from three sources:** the Prisme One webinar (personal architecture), Product School (rigour and commercial framing), and current published practice (mechanics, security, regulation).

**Your parameters, as confirmed:**

| | |
|---|---|
| **Showcase format** | A live system you drive — screen-shared, real tasks, in front of a client |
| **Access and collaboration** | David across devices first; measurable multi-agent execution next; additional human users deferred until the personal service is reliable |
| **Devices** (D52) | Committed: iPhone, iPad, MacBook Air. S4 stretch: Apple Watch, Tesla in-car browser — same private endpoint, no architectural change |
| **Availability** (D53) | Answers any time, any place. A dedicated always-on host (Mac mini class, 24–32 GB, €800–1,500) replaces the Air as inference host; the Air becomes a client |
| **Offline** (D54) | Capture only: durable queue, idempotent retries, visible pending state. No on-device inference in the initial target |
| **Capacity** (D55) | 20+ hours per week, sustained |
| **Security anchor** | Generic but strict — design to the tightest common denominator |
| **Horizon** | December 2026 — schedulable at the D55 capacity, still subject to delivery gates |
| **Service targets** (D56) | Cited text answer p95 **< 8 s** · voice push-to-talk to first spoken word **< 5 s** · recovery time **< 8 h** · recovery point **zero confirmed captures** |

## 0. Current delivery order — amendment of 1 October 2026

**Outcome:** an Obsidian second brain for personal and permitted professional use, running a local model, reachable across devices through text and voice, with evidence that David can build, operate and maintain it. Keep the running workflow as the established domain; supervised wiki maintenance is the shared platform. A small synthetic professional example later demonstrates transfer without importing client information.

**Working architecture:** one inference host David controls, with authenticated clients on phone, tablet and laptop. **D53 settled the host question:** an always-on requirement rules out a travelling laptop, so the host is dedicated hardware and the Air becomes a client. Benchmark on the Air to choose the model and size memory, then confirm on the host — T9 is now "which spec and which model meet the D56 targets", not "Air or host". Models, runtime, networking and speech tools remain choices to evaluate; nothing is purchased, installed or selected by this amendment. Offline capture is required; full offline inference on every device is not part of the initial target.

### Proposed amendment of 19 October 2026 — no hardware, rented compute, sovereignty router

**Status: proposed, not approved.** David decided on 19 Oct not to buy hardware and to rent compute online (Q121). Everything else below waits for Q127–Q131. Full proposal: [[10 Projects/AI Second Brain/02_Architecture/sovereignty-router-proposal-2026-10-19|sovereignty router proposal]]; demo: [[10 Projects/AI Second Brain/05_App_Prototype/sovereignty-router-demo.html|sovereignty-router-demo.html]].

- Rent models and speech from EU providers (L1 default), with Claude allowed per question where the data permits; switchable levels L0–L3 through one gateway (LiteLLM) with ceiling rules, no looser fallback and a level badge on every answer.
- Orchestrator: rules set the ceiling, a floor-level classifier sets the task type, an eval-derived routing table picks the model; replaces S5's coordinator and checker.
- Reuse Open WebUI + Open Relay for phone and voice, an LLM-wiki skill for ingest (with git approval).
- Would cut: the host purchase (D53, D107), T9b, M6b, the custom Shortcut path, the S4 local voice build. Would keep: golden dataset, G1-inj, verdict logic, workstream W, no client data. D46 changes only with David's approval (data policy §8).

### Amendment of 9 October 2026 — end goal restated, independent audit applied

**Status: approved in direction by David (9 Oct, "update the plan"; "squeeze it in and move faster"); items marked ⚑ go to the lead for evaluation before they become tasks; the data-policy change (W2) needs David's own approval under data policy §8.** Source: [[10 Projects/AI Second Brain/02_Architecture/audit-codex-2026-10-09|audit summary]] and [[10 Projects/AI Second Brain/02_Architecture/audit-codex-2026-10-09-report|verbatim report]].

**End goal (David, 9 Oct, verbatim):** *"I need a second-brain AI-powered system available through text and voice on my phone, watch, macbook (and tesla) to be my source of knowledge (vault(s): personal and professional), have access to my context (MCPs to emails, calendar, documents, etc) and must be able to improve itself, learn and built itself from bits of information I throw at it."*

**Goal coverage before this amendment:**

| Goal element | Plan before 9 Oct | Gap |
|---|---|---|
| Text and voice on phone, Mac | S2 (P2.4 text, done) · S4 (voice) | None in design; voice unproven |
| Watch, Tesla | S4 stretch | Tesla: private-service link unverified (audit); stays stretch |
| Personal and professional vaults | Dbrain2 personal; client vault decided 7 Oct, separate | Professional use blocked by the red line; no plan to make it usable |
| Context: email, calendar, documents | **Nothing scheduled before 18 Dec**; §6 and project rules: no MCP before month 4 | **The largest gap** |
| Improves itself, learns from bits thrown at it | S3 writer, P3.0, P2.7 failure loop | Never stated as one end-to-end proof |

**Audit verdict, Cowork's read:** agree with findings 1–9 and with the four release gates. The audit is right that this is an implementation-and-proof gap, not a design gap. It under-weights two things the end goal makes central: context connectors (it ranks them last) and professional use (it treats it as a gate to pass later, not a workstream). Both are added below.

**"Learning" defined (adopted from the audit):** the system learns by (1) approved memory writes from captures, (2) corrections that replace facts without the old version resurfacing, (3) every confirmed failure becoming a regression case, (4) skills and prompts improved against those cases. No model retraining is planned.

**Release gates (adopted), mapped to stages:**

| Gate | Passes when | Stage |
|---|---|---|
| G1 · Reliable read-only assistant | Reviewed representative evals (per question type, held-out subset); honest abstention; **source-injection suite on the read path**; measured host performance | S2 exit |
| G2 · Safe memory writes | Independent restore first; exact-patch approval; stale-edit, replay, rejection, concurrent-edit, interrupted-save tests; **remember → recall → correct from the phone** | S3 exit |
| G3 · Sensitive or professional use | Enforced tier separation proven with synthetic markers across files, search, logs, backups and agent tools; tested retention incl. backups and audit logs; approved data flow per provider; data policy v1.0 approved | New workstream W, before any work account is connected |
| G4 · Integrations and autonomy | One scoped connector at a time: read-only, least scope, revocable, audited; benefit over the baseline measured | New stage C, then S5 |

**Plan changes:**

1. **S2 exit adds** the read-path injection suite (instructions in notes, fabricated authority, exfiltration requests, cross-domain retrieval) and reports retrieval coverage, answer correctness and citation support as three separate numbers. T9's 5/8 is a model-selection result, not a reliability claim.
2. **S3 exit is re-anchored** on the audit's milestone: from the phone, an approved benign fact survives restart, is recalled with its source in a fresh session, and is corrected without the old version resurfacing; rejection, a concurrent Obsidian edit and an interrupted save are included. Voice approval names the exact pending proposal (D125 ask-with-options applies).
3. **New workstream W · Usable security (data policy v1.0), W2–W3:** David wants the system usable daily for personal and professional life, including work email and calendar. That reverses the "no client-confidential data in any system" red line, so it is redesigned, not relaxed. Cowork drafts, David approves (§8). Starting principles:
   - **Tier by source, not by guessing content.** Each account and connector is bound to one vault and tier (personal → Dbrain2; work and client → the client vault, R1). An instance never reads another tier.
   - **Contract gate (D16) stays:** client material enters only for engagements whose contract states AI use.
   - **Query live, persist little.** Connectors are read at question time; only facts David approves are written to a vault (G2 flow). No bulk mail import.
   - **Read-only, least scope, revocable:** calendar read; mail read limited to chosen accounts or folders; tokens in the Keychain, never in a file an agent can read; one switch revokes each connector.
   - **Client tier is processed locally by default**; any cloud processing needs verified provider terms (no training, retention, subprocessors, transfers) and an approved data-flow entry.
   - **Development agents never reach client-tier data or connector tokens** (dedicated macOS service user on the host, D108; ends the D110 Air exception).
   - **Content is evidence, never instruction**; every connector passes the injection suite first.
   - **Text-free audit of every connector call**; retention set per store, including backups and audit logs.
   - **Incident procedure:** stop exposure, revoke, preserve permitted evidence, assess, repair, verify.
   - **Legal:** controller/processor roles and GDPR transfers for professional processing are `unverified` until the T0.7 lawyer review.
4. **New stage C · Context connectors (squeezed in, no cut):** C1 personal calendar, read-only, W7 (16–20 Nov), alongside S4 on the host; C2 personal mail, read-only, W8; C3 work calendar and mail into the client-tier instance, W9–W10, **only after G3 passes**; documents (Drive and local folders) after the demo unless C1–C3 finish early. Each connector has its own brief, scopes, injection cases and revoke test. This amends the "no MCP before month 4" rule and §6 for read-only connectors only.
5. **Operations additions (S6, some earlier):** retention-sweep test after long downtime (P2.7); retention for backups and audit logs; question hashes and filenames in traces treated as personal data, not anonymous; release decision bound to exact code, model, prompt and corpus versions; incident procedure (T8); runtime README reconciled.
6. **Pace:** David chose to add C and W without cutting. The plan already had no slack and is about a week behind (S1 exit evidence incomplete; S2 has P2.1, P2.3, P2.5, P2.6, P2.7 open with exit due 23 Oct). The cut order (Q31) remains the safety valve; Cowork proposes adding as **cut 0**: C3 (work accounts) moves after the demo if G3 has not passed by Fri 13 Nov. Never cut: G3 before any work account, the injection suite before any connector.

**⚑ For the lead to evaluate (not yet tasks):**
- Is the read-path injection suite small enough to fit S2 without moving the 23 Oct exit, or does it go to S3?
- P2.5 F0 scorer: the audit says the six "row" failures include five correct times. Check the scorer's accept rule before F0 is committed.
- Retention sweep only while the service runs: confirm in code and add the restart-after-downtime test to P2.7.
- Do traces' deterministic question hashes allow re-identification by dictionary? If yes, salt per install or drop them.
- Secret scanner covers the runtime repo only: extend to the vault and handoff files, or record why not.
- Client-tier requirement R5 (French, English and **Dutch**) conflicts with D121 (English and French only). D121's trigger ("a client demo needs one") may apply; ask David.
- Whole-vault phone profile (`mvp-whole-vault`) vs R1: make vault root and allowlist configuration before C1.
- Connector technology: MCP servers vs direct read-only APIs (Google Calendar/Gmail, Apple Calendar via EventKit). The audit's point stands: MCP itself gives no safety guarantee. Brief with options before W7.

*Evaluated by the lead, 12 Oct (session 46): six became tasks (G1-inj, retention after downtime, trace hashes, secret-scanner scope, R1 before C1, C0); the F0 scorer check needed no change (it fails a row answer that does not say the word is not the note's own, by design); R5 against D121 is David's call, Q98. Detail in D126.*

### Six delivery stages

| Stage | Work, in dependency order | Exit evidence | Existing work retained |
|---|---|---|---|
| **S1 · Align architecture** | Confirm device/access expectations, weekly time and budget; inventory hardware; define source, knowledge, proposal and runtime boundaries; reconcile project instructions | One authoritative plan, bounded initial corpus, data-flow and permission design, measurable acceptance criteria | T0/T1 completed foundations; T8 governance design starts here |
| **S2 · Local read-only slice** | Benchmark local model candidates on the current Mac; implement scoped search and cited answers; record quality, latency and memory; enforce local inference without silent cloud fallback | Reproducible local question-answering run, source citations and abstention cases, measured resource use; evidence for retaining the Air or considering a dedicated host | T9 moves forward; T4.1/T5/T6 start with platform evaluations |
| **S3 · Supervised wiki maintenance** | Preserve source evidence; propose synthesis, links and contradictions; validate an exact patch; bind approval to that patch and base revision; apply through one writer; commit and update index/log | One source safely updates connected notes; rejection produces no knowledge changes; stale approval is rejected; rollback and independent restore demonstrated before runtime writes | T4.2 before T4.3; D41–D44; running fixes continue alongside |
| **S4 · Remote text and voice** | Add private authenticated access, mobile UI, durable capture queue, local speech recognition and local speech output; define vault sync separately | Text/voice works away from home on agreed devices; captures survive host/network loss; retry does not duplicate; pending/error states are visible | CAPTURE remains interim until this passes |
| **S5 · Measured multi-agent execution** | Add coordinator, curator and evidence checker with scoped tools; compare with the S2/S3 single-agent baseline; persist state and bound retries/time/tool use | Checker benefit and latency cost measured; unauthorized tool actions denied; interrupted work resumes without double writes; David can inspect an execution trace | T11 moves ahead of T10; no requirement for multiple models in memory |
| **S6 · Operate and demonstrate** | Finish monitoring, reliability contract, threat tests, backup/restore and upgrade runbooks; pin versions; rehearse normal and failure paths; package synthetic demo/code/evals | Rebuild and restore drills pass; upgrade regression results recorded; two repeatable demos include a controlled failure and recovery | T5/T6/T8/T12/T13 completed; T10 deferred |

Security, evaluation and observability begin in S1/S2 and continue through all stages. S6 verifies them; it does not introduce them for the first time. No service is treated as available merely because a process starts.

**Two work tracks:** the platform follows S1–S6; running validation continues through T2.6/T3/T4.1 and new correction tasks. The full 150-row running dataset is not a prerequisite for local inference, read-only retrieval or remote-capture experiments. Running features still need their own thresholds before reliability claims. Platform gates require their own evaluation evidence.

### Storage, evidence and permissions

| Layer | Plan |
|---|---|
| Inbox | Raw, unprocessed capture; triage remains a separate action |
| Durable sources | Preserve approved original text or source records after triage; binary/audio content stays outside the vault at `~/Documents/Source_Material/<project-or-topic>/` (D51). Stable IDs are `src-<YYYYMMDDTHHmm>-<short content hash>` (D57). Voice audio is deleted on successful transcription, making the transcript the retained original evidence (D58) |
| Approved knowledge | Keep PARA and wikilinks in 10–40. Minimum frontmatter (D59): `classification`, `source`, `review_status`, `note_type`, `created`/`updated` — new notes now, retrofit as P1.4 once OQ-20 settles whether `classification` splits into separate domain/sensitivity/processing/sharing axes. Retain facts, interpretations and unresolved contradictions distinctly |
| System instructions | 90 System holds policy, schema, templates and readable procedures; AGENTS.md stays the vault authority |
| Application code | Plan a separate repository for runtime, tools, tests, deployment and synthetic fixtures; current scripts remain in place until a separately authorized migration establishes one source of truth |
| Runtime state | Queues, pending patches, caches, temporary audio and redacted traces outside the vault; retention and recovery rules defined before collection |

Source content is evidence, never authority to execute instructions. Follow claims back to originals; AI summaries must not become circular evidence. Retention exceptions and deletion procedures must account for backups and version history.

Classification informs access control but is not an access-control mechanism. Enforce allowed roots, paths and tools before retrieval and execution, with a deterministic writer restricted to approved patches. A file outside the vault can still be reachable to an agent; verify actual access boundaries. Keep the existing data-policy exclusions and per-change approval requirements. Local inference grants no permission to ingest client material.

**Roles:** coordinator dispatches bounded workflows; curator reads scoped evidence and proposes changes; checker reviews support and contradictions; a deterministic commit service writes only approved changes. Roles may share one local model sequentially. Multiple skills alone do not establish multi-agent execution.

**Access:** distinguish Obsidian note synchronization, remote service access and offline capture. Choose a canonical agent-write location and conflict policy; reject stale patches after human or sync edits. Restrict remote access to authenticated devices/users and keep the model endpoint private. Do not interpret host unavailability as successful capture or inference.

### Evaluation and operational acceptance

- Version corpus, model/quantization, prompts, rules, runtime and test inputs together for reproducibility. Maintain development sets and an untouched final acceptance set; tuning on a batch moves it to development.
- Keep running thresholds in [[10 Projects/AI Second Brain/02_Architecture/success-thresholds|success-thresholds]]. Add separate suites for retrieval/citations/abstention, source-to-wiki updates, malicious source instructions, permissions, voice, interrupted jobs and concurrent edits.
- Numeric targets are set (D56): text p95 < 8 s, voice to first word < 5 s, RTO < 8 h, RPO zero confirmed captures. Report p50/p95 latency, **peak memory** (it drives the 24 vs 32 GB host call), sample counts and test conditions — never an average alone. The < 5 s voice target is expected to be the first to come under pressure, since ASR, retrieval, generation and speech share one always-on box; S4 reports the real p95 and renegotiates rather than treating a miss as failure.
- Score deterministic calculations against independent expected results. Use a model judge only where judgment is needed, with a documented rubric and human spot checks.
- Use evidence states (supported, incomplete, conflicting, withheld) in the new UI. Existing skill confidence values are heuristic scores, not calibrated probabilities; preserve existing escalation behavior until any skill change is separately approved.
- Report mandatory knowledge approvals separately from avoidable exception handling. Reducing approval volume is not a success target. Unsupported-claim and retrieval rates need explicit denominators and uncertainty; 150 cases do not establish a <1% failure rate with strong confidence.
- Introduce redacted traces, access enforcement and secret scanning at the first service/writer boundary. Record job outcomes, queue age, errors, latency, model version and tool decisions without dumping private prompts into logs.
- Treat Git history, device synchronization and independent backups as separate controls. Test both a bad-commit rollback and restore after loss of the working copy; include source storage and runtime state in the recovery design.

### Findings to turn into correction tasks

The 1 October review reproduced `load-only` hikes counted as runs, 200% HR coverage on an inconsistent synthetic stream, and “no quality” firing for `long` + `tempo_block`. Inspection also found weekly rather than per-activity zone selection, absent history treated as zero load, and stale classifier instructions/examples. These are **open corrections**, not fixes completed by this amendment. Decide the F3 quality-work definition with David before changing it; the broad tempo flag alone is not necessarily enough.

### Task mapping and history

[[10 Projects/AI Second Brain/TASKS|TASKS]] is the execution checklist; [[10 Projects/AI Second Brain/PROGRESS|PROGRESS]] records evidence and decisions. Existing T IDs and completed checkboxes stay intact. New P tasks fill platform gaps. D45–D48 amend D2/D6/D8 and clarify the wiki/evaluation scope without rewriting prior decisions. §2–§3 below retain the original planning history; their week numbers are reference labels, not current dependencies or deadlines.

---

## 1. The strategic reframe — original rationale retained

The webinar's endpoint is *"a personal AI system that makes me productive."* **That is not showcaseable to a consulting client.** Every creator on LinkedIn claims it, the demo is unfalsifiable, and productivity claims from a director are assumed rather than impressive.

Here is what is actually scarce, and what your Product School material hands you on a plate:

> **You are not demonstrating that AI makes you faster. You are demonstrating that you know how to make AI trustworthy enough to deploy inside a regulated business — and you have built the instrumentation to prove it on yourself first.**

The personal system is the *substrate*. The eval and governance layer is the *product*. Your own course says it twice:

- *"Golden datasets are your receipts. When a buyer asks 'how do you test this?', your golden dataset is the answer. **This is the demo.**"*
- *"Can't screen-share this in a sales call? Not product-grade."*

And the commercial thesis, straight from the Responsible AI Maturity slide: **Governance = GTM.** Level 1 is compliance, where most organisations plateau. Level 3 is a governance story that closes deals. You are building a Level 3 artifact at personal scale.

**What this changes concretely:** instrumentation moves from "phase 4, if time allows" to the H1 gate. You build the measurement layer *while* you build the first skill, not after. It is the differentiator, not the polish.

### Why this fits you specifically

The Advanced Agents whiteboard is, functionally, your job description:

```
        PM  ─────────►  Agent Era  ◄─────────  Engineer
 (pure strategy,     Taste + Judgment          (pure code,
   no building)    + Problem Shaping            no taste)
                  + Agent Orchestration
```

You are approaching that centre from the PM side, and you have the one thing engineers building the same demo usually lack: you can define what "good" means and defend it to a board. Per the *"evals are a team sport"* slide, deciding success criteria is explicitly the PM's job. Lead with that.

---

## 2. September planning history — superseded ordering

| Earlier plan | September choice (historical) | Why |
|---|---|---|
| Evals in phase 2, loosely defined | **Golden dataset in week 3, eval dashboard in week 5** | It's the showcase artifact, not a hygiene step |
| Model/hosting decision in phase 4 | **Week 9, decided against your own golden set** | You'll have data instead of opinions — and that's a demo moment |
| Server "conditional, possibly never" | **Explicitly out of scope** | Adds operational risk to a live demo, proves nothing to a client |
| Multi-user "not addressed" | **H3, with architecture prepared from week 1** | You confirmed humans-sharing matters |
| Security as a warning | **Designed in from week 0, demonstrated in the demo** | It's the thing you're selling |

---

## 3. Original 13-week work packages — retained reference

Originally structured on Product School's Three Horizons. The following week labels preserve the September plan; execute the work in §0 order and use TASKS for completion status. The original gates describe domain/demo maturity, not prerequisites blocking every platform experiment.

### Week 0 — Foundations (~4 hours, this week)

| # | Task | Output |
|---|---|---|
| 0.1 | Revoke the Telegram token; sweep all source material for other secrets | Clean corpus |
| 0.2 | Write `data-policy.md` — three tiers (public / internal / client-confidential), red lines, what may never enter the system | 1 page |
| 0.3 | Run the *"last 30 days of conversations → where am I spending time → what should be automated"* prompt | Evidence-led candidate list |
| 0.4 | **Choose the showcase workflow** — the one thing the system will do excellently | 1 sentence |

**On 0.4 — the single most consequential decision in this plan.** Criteria: it must be something you do genuinely repeatedly; it must have a *checkable* right answer (or you can't build a golden dataset); it must be legible to a client in under 30 seconds; and it must not require client-confidential data to demonstrate. A good shape is something like *"turn a messy discovery-call transcript into a structured findings memo in my house format."* A bad shape is *"help me think"* — unmeasurable, undemoable.

**Gate:** you can state the workflow and your red lines in one sentence each.

---

### H1 · Weeks 1–4 — Ship (earn credibility)

**Goal:** a working, instrumented vertical slice. Narrow and deep, not broad.

| Week | Build | Notes |
|---|---|---|
| **1** | Vault skeleton (`00 Inbox / 10 Projects / 20 Areas / 30 Resources / 40 Archive / 90 System`), hand-written `AGENTS.md`, `git init`. Agent gets **read-only**. **No MCP servers.** | Migrate a *bounded* subset of knowledge — enough to serve the showcase workflow, nothing more. Resist the urge to import everything; that's the collector's fallacy and it costs you weeks. Write `AGENTS.md` yourself — auto-generated ones measurably underperform. |
| **2** | Three `SKILL.md` files for the showcase workflow. **Write the success threshold before the skill.** | Per the evals-team slide, defining success criteria is your job, not an engineer's. Format: *"handles ≥X% of cases with <Y% exceptions."* |
| **3** | **Golden dataset v1** — 150 rows, 20–30% edge cases, adversarial rows, versioned in git as `golden-dataset.md` | The highest-leverage artifact in the entire plan. Input · Expected output · Edge case? · Judge type (rule/LLM). This is what you screen-share when asked "how do you know it works?" |
| **4** | Wire LLM-as-judge scoring against the golden set. Enable agent **write** access — confined to approved directories, behind git, *after* testing rollback. | Verify recovery before granting write access, not after. |

**H1 gate — all four must be true:**
1. Three skills pass their stated thresholds against the golden set
2. You have deliberately broken something and rolled it back
3. You can screen-share eval results
4. Zero client-confidential data has entered the system

**What this proves to a client:** you don't guess whether AI works — you measure it, against a standard you defined.

---

### H2 · Weeks 5–9 — Validate (prove it's trustworthy)

**Goal:** the artifacts that turn a working system into a credible one.

| Week | Build | Why it earns its place |
|---|---|---|
| **5** | **Eval dashboard.** Metrics, judge setup, drift alerts, UX hooks. *"Like an SRE dashboard for your model."* | This is the screen you share. If it isn't screen-shareable, it isn't done. |
| **6** | **Reliability contract** — metric / target / measurement / alert-threshold table for the showcase workflow, plus escalation paths | Air Canada made this concrete: your AI's promises are your promises |
| **7** | **Confidence UX** — three bands (>90% / 50–90% / <50%), visible reasoning, override surface, corrections feeding back | The "trust ≠ accuracy" lesson made operational. **Build a deliberate low-confidence path — you will demo it on purpose.** |
| **8** | **Governance one-pager** — scope, autonomy boundaries, escalation triggers, audit cadence, regulatory exposure (EU AI Act / GDPR / sector), agent topology | *"One page your CISO wouldn't redline on sight."* This is the artifact that converts a technical demo into a commercial conversation. |
| **9** | **Model + hosting decision, made properly.** Benchmark 2–3 options — one frontier, one open-weight, one EU-hosted — against *your own golden dataset*. Document with the trade-off grid. | Deliberately late. You now decide with evidence, and "here's how I chose, and here's the data" is a stronger demo beat than any model name. |

**H2 gate:**
1. "How do you know it works?" is answered with a screen, not a sentence
2. HITL% is trending down across the period, not flat
3. The governance one-pager survives a hostile read by someone who isn't you

**What this proves:** you can make AI legible and governable — the Level 2→3 jump.

---

### H3 · Weeks 10–13 — Collaborate & package

**Goal:** the bridge from personal to client-deployable, plus a demo that doesn't fall over.

| Week | Build | Notes |
|---|---|---|
| **10** | **Multi-user layer (humans first).** Shared vs personal vault roots, RBAC as a metadata filter, apply S.M.A.R.T. memory governance (Scoped · Monitored · Auditable · Retrievable · Timed) | Get a second real human in — a colleague is enough. A two-person system that genuinely works beats a ten-person design that's theoretical. |
| **11** | **Second agent + supervisor pattern.** Only now. Add a critic/supervisor, log A2A messages, set explicit autonomy ceilings per role | Your own course: *refactor to multi-agent when you hit boundaries in skills, tools, or evaluations* — not before. Be able to name the boundary you hit. |
| **12** | **Security hardening + shadow-AI audit on yourself.** MCP posture (if any MCP at all), PII handling including in traces, TTL policy, data-leakage evals | Run the Discover → Signal → Prioritize → Decide audit on your own tool sprawl. The finding *is* content for the demo. |
| **13** | **Demo build and rehearsal.** Narrative, failure drills, artifact pack, twice-through dry run | Treat it as a board simulation, which is what Day 6 was training you for |

**H3 gate:** you can run the live demo twice consecutively without a failure you can't explain on the spot.

---

## 4. Architecture decisions — amended 1 October

Retain the storage and portability choices. Enforce permissions in code and isolate runtime state; future multi-user support requires its own design and tests.

| Decision | Choice | Rationale |
|---|---|---|
| **Storage** | Plain markdown + git | Portable knowledge and change history; durable jobs and access-control state live outside the vault. Git alone is neither authorization nor an independent backup |
| **Access classification** | `classification: public\|internal\|client` in frontmatter, from the very first note | Labels inform authorization; enforce scoped roots, tools and write permissions before content reaches a model. `client` remains prohibited |
| **Vault roots** | Keep current PARA roots; define permitted corpora and a canonical writer | Separate shared roots only when T10 is taken up; no directory migration in this amendment |
| **Skills** | Portable `SKILL.md` files, never tool-locked config | Open standard across Claude Code, Copilot, Cursor, Codex, OpenCode and others — no lock-in, and *demonstrating* portability is itself a credibility beat |
| **Retrieval** | Agentic file search. **No vector store initially.** | Right for a personal corpus. Add RAG only on a named trigger (corpus scale, sub-second latency need, synonym-heavy search) — see `03_Product_School_Playbook.md` §6.1 |
| **Client data** | **Never enters the system.** Demo on synthetic or anonymised material | Non-negotiable. Demoing trustworthiness using another client's confidential data is an instant, unrecoverable credibility failure. |
| **Secrets** | Never in the vault. Env vars or a keychain, with a pre-commit scan | You have already had one live token in your source material |

---

## 5. The demo — sketch it now, build toward it

Since you're driving it live, design the narrative in week 0 and let it pull the build.

| Beat | Content | Time |
|---|---|---|
| **1 · Cold open** | Capture by voice and answer from cited evidence; use the established running domain or a synthetic professional example. | 60 sec |
| **2 · "But how do I know it works?"** | Golden dataset → eval dashboard → regression history. **The differentiator.** | 3 min |
| **3 · "And when it's unsure?"** | Deliberately trigger a low-confidence case. Watch it decline, explain, and escalate. | 90 sec |
| **4 · "And is it safe?"** | Governance one-pager: autonomy ceilings, memory TTL, audit trail, regulatory exposure | 3 min |
| **5 · "Can you operate it?"** | Show scoped agent roles, an interrupted job, recovery and measured service behavior; multi-user is a later extension | 2 min |
| **6 · Close: judgment, not tools** | The decision rules — agentic vs RAG, open-weight vs frontier, agent vs RPA — each with the evidence you used | 2 min |

**Beat 3 is the one people remember.** A system that visibly declines to answer is more persuasive than one that always does. Rehearse it deliberately.

**Live-demo risk management:** rehearse against a fixed dataset; keep a recorded fallback; and pre-plan one honest failure to walk through. A director who says *"here's where this breaks, and here's how I'd contain it"* outsells one whose demo is flawless — particularly to a regulated buyer, who has learned to distrust flawless.

---

## 6. Deliberately out of scope

Amended scope protects the S1–S6 delivery sequence; essential local hosting and remote access are now included.

| Not building | Why |
|---|---|
| **Unnecessary orchestration platforms / public VPS deployment** | Start with one controlled local host. Add infrastructure only for a measured availability or workflow requirement. |
| **A dozen MCP servers** | Direct file access covers the vault. Every server added is attack surface and a tool-selection ambiguity — both documented failure modes. |
| **Vector RAG** | Wrong tool at this corpus size. Add on a named trigger. |
| **Full knowledge migration** | Collector's fallacy. Migrate what the showcase workflow needs. |
| **Full local inference on every client device** | Initial design uses one controlled inference host; local inference on that host is required at S2. |
| **Additional production domains and human users** | Preserve running as the domain; wiki maintenance is shared platform work. A small synthetic professional example is allowed for transfer demonstration at S6. |

---

## 7. What you'll actually instrument

Retain the original aspirations below, qualified by the evaluation contract in §0. Instrument the platform from S2 and report running results separately.

| Instrument | Target | Why this one |
|---|---|---|
| **Unsupported claims** | Original aspiration <1%; report observed counts, denominator and uncertainty | A small set cannot certify a population rate; no unsupported certainty |
| **Eval regression** | Required suites pass; changes in quality, safety and latency reviewed before release | Frozen final set and independent expected outputs prevent circular scoring |
| **Avoidable exceptions** | Trend down on comparable workloads; mandatory approvals reported separately | Preserve the human knowledge gate |
| **Retrieval recall** | Initial target ≥85% on a labelled evidence set, with denominator and sample size | Measure citation support and abstention separately |

Deliberately *not* instrumented at this volume: drift velocity per week, confidence distribution, inference ROI, deflection rate. They need volume you won't have. **Know the numbers, explain why you're not tracking them yet** — that distinction reads as judgment. Claiming a weekly drift figure on a personal system reads as theatre, and a sharp client CTO will catch it.

---

## 8. Risks

| Risk | Likelihood | Mitigation |
|---|---|---|
| **Scope creep into infrastructure** | High | One inference host first; benchmark before hardware purchases; avoid unneeded platforms. |
| **Evaluation work stalls** | High | Continue running labels alongside platform suites; reserve untouched acceptance cases. Do not block read-only platform experiments on 150 running labels. |
| **Vault becomes a reading list** | Medium | Six-week check: has anything *shipped* out of the system? If not, stop capturing. |
| **Demo fails live** | Medium | Rehearse twice, fixed dataset, recorded fallback, one planned honest failure |
| **Client data leaks in** | Severe | Enforce reachable-source boundaries and output checks; preserve exclusions; use synthetic professional demos. |
| **Model landscape shifts mid-build** | Expected | Benchmark at S2, pin model/runtime versions and rerun regressions before upgrades. |

---

## 9. Still open — tracked in OPEN_QUESTIONS

- Hardware capacity, actual device/OS coverage, host availability and offline expectations (OQ-4, OQ-14).
- Weekly build time, hardware budget and acceptance targets (OQ-15).
- Source retention/storage mapping and concrete schema (OQ-13); final tool choices follow benchmarks.
- F3 quality-work semantics for long runs with tempo work (OQ-16).
- Colleague participation is parked with T10 (OQ-3), not a current delivery blocker.

Showcase selection and the firm's-policy question were resolved (D14–D16). Do not reopen them as prerequisites.

---

## 10. Immediate next actions — amended 1 October

1. P1.1: inspect the current Mac's hardware and available capacity without changing it.
2. P1.2/P1.3: resolve device/time/budget questions and record measurable acceptance criteria and data boundaries.
3. T9/P2.1: benchmark local models against a bounded question-answering set; start the read-only slice.
4. Continue T3.1 batch 04 independently; T2.6 follows the 4 October race. P3.4/P3.5 track calculation and evaluation corrections.

*Originally written 7 September 2026; amended 1 October 2026. Original rationale and work packages retained. Current sequence: §0 and TASKS.*
