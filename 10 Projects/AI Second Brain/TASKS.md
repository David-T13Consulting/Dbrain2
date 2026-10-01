---
classification: internal
---
# Tasks — AI Second Brain Project

**Updated:** 1 Oct 2026 (session 7) · **Phase:** S1 architecture alignment; running validation in parallel · **Target:** December 2026, schedule to re-estimate

---

## ▶ Next action

> **P1.2/P1.3: settle devices, host availability and measurable service targets.** P1.1 is complete. Next independent experiment: P2.1 retrieval baseline and another local candidate in T9; first benchmark recorded in [[10 Projects/AI Second Brain/02_Architecture/local-benchmark-2026-10-01|local benchmark]].

**Parallel domain action:** T3.1 batch 04 (rows 41–60) scores rubric v1.4 blind. T2.6 follows 4 October; T0.7 precedes the next contract. T0.6, T1.2 and T1.4 are already complete.

## Current execution order — S1–S6

Approved planning amendment: [[10 Projects/AI Second Brain/04_Roadmap|04_Roadmap]] §0, D45–D48. Existing T IDs and completed work below are preserved. Week headings below are historical groupings, not execution order. P IDs fill gaps; references to T IDs schedule existing tasks without duplicate completion records. No stage passes merely because its checklist exists.

### S1 · Align architecture
- [x] **P1.0** Amend the roadmap and reconcile tracking pages, preserving historical decisions and completed tasks. ✅ 1 Oct; documentation only.
- [x] **P1.1** Hardware inventoried 1 Oct: M2, 24 GiB RAM, 8 CPU cores, about 90 GiB free before download. OQ-4 resolved; first supplied-evidence local benchmark complete. See [[10 Projects/AI Second Brain/02_Architecture/local-benchmark-2026-10-01|measurement record]]. T9/P2 gates remain open.
- [ ] **P1.2** Confirm devices/OSs, remote/offline expectations, host availability, weekly time and budget (OQ-14/OQ-15). No purchase implied.
- [ ] **P1.3** Record data flow, scoped roots/tools, initial corpus and acceptance targets: quality, latency, recovery time and acceptable data loss. Define source retention/schema and code/runtime separation (OQ-13). Begin T6/T8.

### S2 · Prove local read-only answers
- [ ] **P2.1** Build retrieval/citation/abstention cases with independent expected evidence and an untouched acceptance subset; establish index/file-search baseline. Does not wait for all T3.1 labels.
- [ ] **P2.2** After runtime selection in T9, implement a scoped read-only query service and local model adapter. Disable silent cloud fallback; verify normal inference without provider access.
- [ ] **P2.3** Measure quality, p50/p95 latency, memory and sustained performance; pin corpus/model/runtime/prompt versions. Recommend Air versus dedicated host on evidence.
- Existing tasks: **T9** moves here; **T4.1/T5/T6** begin with platform evaluation, redacted traces and service targets.

### S3 · Supervised wiki maintenance
- [ ] **P3.1** Implement agreed durable source IDs/versions, original evidence, derived claims, contradictions and review state. Preserve approved captures after triage under the agreed retention policy.
- [ ] **P3.2** Implement pending patches with evidence, exact diff, base revision and approval binding. Test rejected proposals and stale approvals after intervening edits.
- [ ] **P3.3** After T4.2, implement one deterministic writer: allowed paths, schema/link/classification validation, approved commit plus index/log updates. Test malicious source instructions, path escape and unauthorized writes.
- [ ] **P3.4** Independently regression-test and fix reviewed issues: `load-only` counted as runs (check both scripts), stream/moving-time coverage, per-activity zones, missing history vs inactivity, stale classifier instructions/examples. No code fixes are made by this amendment.
- [ ] **P3.5** Resolve OQ-16 before changing F3 quality-work semantics. Test strict tempo evidence versus the broad flag; version rule and expected-label changes.
- [ ] **P3.6** Freeze final running acceptance cases; preserve historical scores and label corrections; score arithmetic against independent expected outputs. Existing confidence values are heuristic, not calibrated probabilities.
- Existing tasks: **T4.2 → T4.3** gates runtime writes; **T3/T4.1** running validation continues alongside. **T7** adds evidence-state UI; existing skill escalation behavior stays until separately reviewed.

### S4 · Remote text and voice
- [ ] **P4.1** Implement private authenticated access and mobile text UI for agreed devices; keep the inference endpoint private. Specify canonical writer, vault sync and conflict policy separately.
- [ ] **P4.2** Add durable capture queue, pending/failure states, idempotent retries and cancellation. Test airplane mode, host sleep/restart and interrupted uploads without duplicate captures.
- [ ] **P4.3** Add local push-to-talk transcription and speech output; test French, English, mixed speech, names and noise. Define audio retention/deletion before recording.
- [ ] **P4.4** Test away from home on each agreed device class. Replace the interim Dispatch dependency and update CAPTURE only after the new route passes.

### S5 · Measurable multi-agent execution
- Existing task: **T11** introduces coordinator, curator and evidence checker with distinct permissions. The writer is deterministic; roles may share a model sequentially.
- [ ] **P5.1** Compare task success and unsupported-claim detection against the single-agent baseline, including latency and memory cost.
- [ ] **P5.2** Implement persistent jobs, bounded retries/time/tool budgets, cancellation and traceable handoffs. Test tool denial, checker failure, crash/resume and duplicate-write prevention.

### S6 · Operate and demonstrate
- [ ] **P6.1** Back up vault, source storage and required runtime state independently; restore after working-copy loss within T6 objectives. Distinguish rollback, sync and backup.
- [ ] **P6.2** Pin releases/model/runtime versions; document reproducible setup, restart, upgrade/rollback and incident handling. Run regressions before upgrades.
- [ ] **P6.3** Complete latency/error/queue/resource monitoring; verify redaction, access denial and retention. Instrumentation begins at S2.
- [ ] **P6.4** Package architecture, traces, evaluations and synthetic professional fixtures for a public-safe code/demo repository. Keep the personal vault private; publication requires its own authorization.
- Existing tasks: complete **T5/T6/T8/T12/T13** with normal, abstention, approved-update, failure and recovery demos. **T10** remains parked until the personal service is reliable.

**Exit evidence:** roadmap §0. Hardware/tools and numeric service targets remain open until measured or confirmed.

---

## LLM Wiki adoption (D41–D44, 1 Oct)

- [x] Create `index.md` and `log.md` at the vault root ✅ 1 Oct
- [x] Add "Wiki operations" to AGENTS.md ✅ 1 Oct
- [x] Write `90 System/lint-checklist.md` and run the baseline ✅ 1 Oct
- [x] **Decide on the 15 notes without `classification:`** ✅ 1 Oct, applied as proposed. Proposal: `internal` for project notes, Welcome.md `public`, the root CLAUDE.md stub exempt (one line, imports AGENTS.md)
- [ ] Triage the two Inbox items (`assistant-scope-ideas`, `how-to-automate-pm-job`) at the next weekly pass, and run lint then
- [x] Resolve OQ-12 via D47: running is the domain; supervised wiki maintenance is shared platform work. ✅ 1 Oct
- [ ] Resolve remaining OQ-13 retention/IDs/metadata details at P1.3/P3.1 (routing and provenance settled by D49, 1 Oct).
- [ ] Automate lint at S3; corrections/index/log changes stay approval-gated. Read-only inspection is available now.

---

## Week 0 — Foundations

*Historical foundations: gate met 29 Sep. T0.7 remains future-only; original 14 Sep deadline is superseded.*

- [x] **T0.1 · Revoke the Telegram bot token** ✅ done 8 Sep `5 min` `🔴 security`
  Token `8842032811:AAFH…` is in `00_Source_Material/Product_School/Product School - Advanced Agents.pdf` (p.2). Revoke via BotFather → `/mybots` → select → API Token → Revoke.
- [x] **T0.2 · Rotate the four Zoom recording passcodes** `10 min` `🔴 security` ✅ **closed 29 Sep — mitigated, not rotated.** Recordings are Product School's, not David's to rotate. PDF remains outside the vault, ungit-tracked (rule 7). **1 Oct qualification:** this location alone does not prove access isolation; verify reachable roots in P1.3 without exposing credentials.
  Same PDF. Lower severity than the token but they're recordings of paid course content.
- [x] **T0.3 · Run the 30-day audit prompt** `20 min` ✅ **closed 29 Sep — superseded.** Its only purpose was evidence for T0.4, which was locked 8 Sep from David's actual recent topics.
  In ChatGPT/Claude: *"Look at my last 30 days of conversations. Where am I spending most of my time, and what from that list should be automated?"* Evidence-led input to T0.4. (Source: Advanced Agents, Day 2.)
- [x] **T0.4 · Choose the showcase workflow** `45 min` `⭐ blocks everything` ✅ **LOCKED 8 Sep** (D14, D15 in PROGRESS.md)
  **"Classify each run's session type (easy / long / tempo / hills / intervals / race / recovery) from raw
  Strava data, then roll a week of classified sessions into a coaching assessment — trend, effort
  adequacy, and race-goal trajectory."**
  Evidence-led (David's actual last-few-weeks topics, not guessed from his job). No Runna connector
  exists and Strava's `get_training_plan` tool doesn't return real plan data — session-type
  classification from raw metrics (pace/HR/elevation/effort) is the workaround, and it's a cleaner
  golden-dataset task than plan-compliance checking would have been anyway.
  **H1 scope** (checkable core): session-type classification + trend/effort-adequacy.
  **H2 scope** (judgment layer, confidence bands): race-goal trajectory call.
  **Golden-dataset note:** no external plan to check against, so ground truth for T3.1 comes from
  David labeling a batch of his own historical runs by actual session type — flag this as real work
  he'll need to do, not just Claude's.
- [x] **T0.5 · Write `data-policy.md`** `45 min` ✅ **done 29 Sep** — v0.1 in `02_Architecture/data-policy.md`. §6 (Tower13 commercial) provisional pending T0.6.
  Three tiers (public / internal / client-confidential), red lines, what may never enter the system. Save to `02_Architecture/`.
- [x] **T0.6 · Check your firm's AI policy** `30 min` ✅ **closed 29 Sep — replaced by a rule (D16).** There's no firm policy above Tower13. David set the rule instead: every contract must state his AI agent use explicitly, and engagements without that stay out of the system entirely. data-policy.md → v0.2.
- [ ] **T0.7 · Add an AI-use disclosure clause to the Tower13 contract template, and to live contracts at renewal** `1 h` `needs David + lawyer review`
  David has no live contracts (29 Sep), so this only applies going forward: the clause goes in the template before the next engagement is signed. Claude can draft; a Belgian lawyer should check it.

**Week 0 gate:** you can state the showcase workflow and your red lines in one sentence each. Showcase workflow ✅ done (T0.4). Red lines ✅ done (T0.5, 29 Sep).

---

## H1 · Weeks 1–4 — Ship

*Goal: a working, instrumented vertical slice. Narrow and deep.*

### Week 1 — Vault
- [x] **T1.1** Create vault skeleton: `00 Inbox / 10 Projects / 20 Areas / 30 Resources / 40 Archive / 90 System` `30 min` ✅ done 8 Sep — built inside `~/Documents/Dbrain2` (the Obsidian vault), not this folder. See D11 in PROGRESS.md.
- [x] **T1.2** Write `AGENTS.md` for the vault — **by hand**, 20–30 lines `1 h` ✅ **29 Sep, v1 approved by David.** At the vault root, with a root `CLAUDE.md` importing it (D17). Every line passes the test: would the agent get this wrong without being told?
  Auto-generated ones measurably underperform (+23% cost, redundant content).
- [x] **T1.3** `git init` the vault, first commit `15 min` ✅ done 8 Sep — commit 377e8c2 in Dbrain2
- [x] **T1.4** Migrate a *bounded* subset of knowledge — only what the showcase workflow needs `2 h`
  ✅ **done 29 Sep:** `20 Areas/Running/athlete-baseline.md`, `30 Resources/Running/session-types.md`, `20 Areas/Running/race-goals.md`, all confirmed. Open: Gelbressoise distance. See D18.
  ⚠️ Resist importing everything. That's the collector's fallacy and it costs weeks.
- [x] **T1.5** Confirm agent is **read-only** at this stage. No MCP servers. `10 min` ✅ confirmed 8 Sep — documented in Dbrain2/90 System/README.md, no write MCP configured

### Week 2 — Skills
- [x] **T2.1** Write success thresholds for 3 skills — **before** writing the skills `45 min` ✅ **approved 29 Sep** → `02_Architecture/success-thresholds.md` (D19)
  Format: *"handles ≥X% of cases with <Y% exceptions."* Defining "good" is your job, not an engineer's.
- [x] **T2.2** Write `SKILL.md` #1 `1.5 h` ✅ **29 Sep, v0.2 approved** → `90 System/skills/classify-session/SKILL.md` (D20, D21)
- [x] **T2.3** Write `SKILL.md` #2 `1.5 h` ✅ **29 Sep, v0.2 approved** (median baseline, D23) → `90 System/skills/weekly-assessment/` (SKILL.md + compute_week.py) + `30 Resources/Running/weekly-flags.md` (D22)
- [x] **T2.4** Write `SKILL.md` #3 `1.5 h` ✅ **29 Sep, v0.1 drafted and smoke-tested** → `90 System/skills/race-readiness/` + `30 Resources/Running/readiness-rules.md` + `20 Areas/Running/readiness-calls.md` (D24). Time threshold approved.
- [x] **T2.5 · Log David's blind call for Dinant, then run race-readiness live** ✅ 29 Sep: David borderline / 1:35 → skill borderline (0.60), 1:38:54–1:45:01. Verdict agrees.
- [ ] **T2.6 · After 4 Oct: add Dinant chip time to `readiness-calls.md`, score the range** `2 min` `David`

### Week 3 — Golden dataset ⭐
- [ ] **T3.1** Draft golden dataset v1 — 150 rows `4 h` `⭐ the showcase artifact`
  🟡 **Updated 1 Oct:** batches 01–03 (50 runs) are now development data. Batch 04 is fresh for v1.4. P3.6 reserves final acceptance cases. Historical held-out scores below describe the versions originally tested:
  - [x] Batch 02 · 20 runs ✅ 30 Sep. First held-out score of v1.2: terrain 17/20 (85%), intent 10/20 (50%). Sampling order fixed in `03_Golden/heldout-order.md` (seed 20260930)
  - [x] Rubric v1.3 + classify-session v0.4 ✅ 30 Sep (D27–D32). Batch 02 is now dev
  - [x] Batch 03 · 20 runs ✅ 30 Sep. v1.3 held-out: terrain 18/20, intent 14/20, tempo_block 14/20, vertical 16/20
  - [ ] Batch 04 · 20 runs (scores v1.4)
  - [ ] Batch 05 · 20 runs
  - [ ] Batch 06 · 20 runs
  - [ ] Weeks · ~30 weekly assessments (~1 min each, split into 2 sessions)
  - [ ] Race times backtest (automatic from results; past readiness verdicts **not** labelled, because of hindsight bias)
  Columns: Input · Expected output · Edge case? · Judge type (rule/LLM). 20–30% edge cases.
- [ ] **T3.2** Add adversarial rows (≥3) and note coverage gaps `1 h`
- [ ] **T3.3** Commit as `golden-dataset.md`, versioned like code `15 min`

### Week 4 — Evals + write access
- [ ] **T4.1** Wire versioned evaluations: independent deterministic checks first; rubric-based model judges with human spot checks for judgment. Begin platform suites at S2 and running suites alongside T3.
- [ ] **T4.2** Before S3 runtime writes, test bad-change rollback and independent restore on a disposable copy against T6 objectives. P6.1 extends recovery testing to deployment.
- [ ] **T4.3** After T4.2 passes, enable the scoped deterministic writer for approved patches with base-revision/path validation. No blanket autonomous-write permission.

**H1 gate — all four must be true:**
1. Three skills pass their stated thresholds
2. You have deliberately broken something and rolled it back
3. You can screen-share eval results
4. Zero client-confidential data has entered the system

---

## H2 · Weeks 5–9 — Validate

- [ ] **T5** Eval dashboard: start results/redacted traces at S2, complete at S6. Separate platform/running suites, mandatory approvals and avoidable exceptions; avoid unsupported drift claims.
  Test: *can you screen-share it in a sales call?* If not, it isn't done.
- [ ] **T6** Reliability contract: set targets before acceptance runs at S1/S2; include latency, recovery time/data loss, measurements, alerts and escalation. Verify at S6.
- [ ] **T7** Evidence UX at S3: supported/incomplete/conflicting/withheld, concise evidence/citations, overrides and reviewed corrections. Existing skill confidence scores are heuristic; preserve escalation until reviewed.
  Build the low-confidence path deliberately — you will demo it on purpose.
- [ ] **T8** Governance one-pager: begin boundaries/data flow at S1, update with actual roles and permissions, review at S6. Include retention, escalation, authorization and agent topology.
- [ ] **T9 · S2** Benchmark local models on the current Mac against platform cases and available running development cases. Record quality, sustained latency, memory/context settings; decide hosting on evidence.
  External comparisons are optional and require explicit authorization; never a production fallback or prerequisite.

**Retained validation gate:** screen-shareable results, avoidable exceptions measured separately from mandatory approvals, governance review. Current delivery gates are roadmap §0.

---

## H3 · Weeks 10–13 — Collaborate & package

- [ ] **T10 · Parked after S6** Additional human users: scoped roots, enforced authorization and concurrency/sync tests. Metadata alone is not RBAC. Resolve OQ-3 first.
  A real second-user test is required when this extension is taken up; it does not block the personal service.
- [ ] **T11 · S5** Coordinator, curator and evidence checker with scoped tools, handoff traces and explicit autonomy limits. Compare with the single-agent baseline (P5.1).
  Name the quality or permission boundary each role addresses; implement bounded resumable execution (P5.2).
- [ ] **T12** Permissions/redaction from S2, source-injection/write tests before S3, remote-access checks before S4 exposure. Complete security/operational audit at S6.
- [ ] **T13 · S6** Rehearse twice: voice capture, cited answer, reviewed update, agent trace, controlled failure and recovery. Permitted running data and synthetic professional fixtures.

---

## Backlog / someday

- [ ] **Second domain: choose after the H1 gate** (see `00 Inbox/2026-09-30-1447-assistant-scope-ideas.md`). Proposed: family logistics, then knowledge digest. Parked questions: OQ-11

- [ ] Migrate Apple Notes → markdown (export route; no API exists)
- [ ] Retrieve the 4 Product School capstone tools from the LMS (Strategy Assembler, AI Bet Evaluator, Roadmap Builder, Pitch Builder)
- [ ] Decide relationship between this project and the Vibe Coding app+deck deliverable → OQ-5
- [ ] Infrastructure beyond the single controlled host: only on measured availability/workload need. Required local hosting evaluation is T9 at S2.

---

## Conventions

`🔴` security-sensitive · `⭐` high-leverage · `T0.x` week-0 · time estimates are working time, not elapsed.
Tick items as you go. Add anything that surfaces — an unrecorded task is a lost task.
