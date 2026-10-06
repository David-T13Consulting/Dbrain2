---
classification: internal
---
# Tasks — AI Second Brain Project

**Updated:** 6 Oct 2026 (session 29) · **Phase:** S1 closing, S2 under way (dated plan: [[10 Projects/AI Second Brain/06_Delivery_Plan_S2-S6|S2–S6]], proposed) · **Target:** demo-ready Fri 18 Dec 2026 (Q29)

---

## ▶ Next action

> **Stopped for clean-up (David, 6 Oct 08:57; brief [[90 System/briefs/L1-lint-cleanup|L1]]).** No new work until David lifts it in writing. Released 10:05: **M1** (back up and push every repo) is done (6 Oct, session 22): every repo in scope is on private GitHub, gate met. **M2 done** (6 Oct, session 27): repos in `~/Work`, off iCloud; medispring-infi archive in `~/Archive` (data policy v0.5, D75); paths re-pointed; D76. **Q65 clean-up run (session 29):** answers, review tiers (D77) and Inbox committed; both repos pushed; M2 follow-up done (`1fd0c53`). **Next:** `@david` Q71 (M3 stopped at its reference check), then `@code` **M3** (archive ui-design-agent, claude-blueprint, agentic-ios-app; [[90 System/briefs/M3-archive-three-repos|brief]], `blocked-on-david`); then David lifts the hold. **Then:** MVP-phone (P2.4, parked after round 9; consult first) and the Q51 order. P2.2 is done (`4b5e91f`, runtime `c8b3b7b`); T9 was stopped after 2 of 9 blocks, no result.

**Parallel domain action:** batch 04 is scored (2 Oct); its independent Codex re-score waits for Cowork's fixes to the re-score brief. T3.4 rubric v2.0 wording (`@cowork`, David approves). T2.6 is done (Dinant, Q22). T0.7 precedes the next contract.

**Action for David:** paste the weekly-review task ID and first-run output into [[90 System/weekly-local-model-review]] after the 8 Oct run (D60, Q11) · decide the host purchase (D53; Q30 open, a 64 GB host under evaluation) · finish the MVP-phone acceptance checks (P2.4).

- [ ] `@david` **Six-week honesty check (rule 5), due ~19 Oct** (six weeks after 7 Sep): has anything shipped *out* of the system? If not, stop capturing. Cowork raises it at the session nearest 19 Oct; the answer goes in PROGRESS.

## Current execution order — S1–S6

Approved planning amendment: [[10 Projects/AI Second Brain/04_Roadmap|04_Roadmap]] §0, D45–D48. Existing T IDs and completed work below are preserved. Week headings below are historical groupings, not execution order. P IDs fill gaps; references to T IDs schedule existing tasks without duplicate completion records. No stage passes merely because its checklist exists.

### S1 · Align architecture
- [x] **P1.0** Amend the roadmap and reconcile tracking pages, preserving historical decisions and completed tasks. ✅ 1 Oct; documentation only.
- [x] **P1.1** Hardware inventoried 1 Oct: M2, 24 GiB RAM, 8 CPU cores, about 90 GiB free before download. OQ-4 resolved; first supplied-evidence local benchmark complete. See [[10 Projects/AI Second Brain/02_Architecture/local-benchmark-2026-10-01|measurement record]]. T9/P2 gates remain open.
- [x] **P1.2** Devices/OSs, offline expectations, host availability, weekly time and budget. ✅ 1 Oct, structured interview → **D52** (iPhone/iPad/Air committed; Watch and Tesla browser are S4 stretch) · **D53** (always-on dedicated host, Mac mini class 24–32 GB, €800–1,500; 32 GB recommended; purchase still a separate decision) · **D54** (offline = capture only) · **D55** (20+ h/week). OQ-14 and the capacity half of OQ-15 resolved.
- [x] **P1.3** Acceptance targets and source schema. ✅ 1 Oct → **D56** (text p95 < 8 s · voice to first word < 5 s · RTO < 8 h · RPO zero confirmed captures) · **D57** (source IDs `src-<YYYYMMDDTHHmm>-<hash>`) · **D58** (audio deleted on successful transcription) · **D59** (minimum frontmatter). OQ-13 and OQ-15 resolved. ⚠️ Still to document as part of T8, not blocking S2: the data-flow diagram, scoped roots/tools enumeration, bounded initial corpus and code/runtime separation.
- [ ] **P1.4** `@code` *(Gates personal-data wave 1, D69; flags any existing note that would now be wave 2 for David.)* Retrofit the D59 frontmatter (`source`, `review_status`, `note_type`, `created`/`updated`) across the 114 existing structured notes. **Scheduled W1 (S2–S6 plan) for a brief and a dry-run diff report only; applying the retrofit waits for David's approval (rule 8, hard limit). OQ-20 was answered 5 Oct (queue Q10):** `classification` splits into four axes (domain · sensitivity · processing · sharing), labels only, no vault split, so the retrofit targets that shape once. Current coverage: 7 notes have `source`, 10 have `created`, none have `review_status` or `note_type`.

### S2 · Prove local read-only answers
- [ ] **P2.1** Build retrieval/citation/abstention cases with independent expected evidence and an untouched acceptance subset; establish index/file-search baseline. **Started 1 Oct:** 26 chunks / 10 dev cases, coverage and faithfulness failures recorded; six provisional cases reserved, independent review still needed. Does not wait for all T3.1 labels. `@codex` — the independent case review is briefed in [[90 System/briefs/P2.1-review|P2.1-review]].
- [x] **P2.2** ✅ 5 Oct (`4b5e91f`, runtime `c8b3b7b`). Behind a swappable model adapter, so T9 stays open, implement a scoped read-only query service and local model adapter. Disable silent cloud fallback; verify normal inference without provider access. `@code` — brief: [[90 System/briefs/P2.2|P2.2]]. Label check redesigned as an allowlist, Q46 applied; round O's two findings accepted as risks (Q53); rounds P–Q: **PASS, committed**.
- [ ] **P2.3** `@code` Measure quality, p50/p95 latency, memory and sustained performance; pin corpus/model/runtime/prompt versions. Recommend Air versus dedicated host on evidence.
- [ ] **P2.4** `@code` **MVP-phone (S4 slice pulled into S2, David Q32–Q34, 5 Oct):** ask from the iPhone over Tailscale with an Apple Shortcut; `/ask` on the Air calls the P2.2 service over the whole vault, read-only, bearer token in the Keychain. Brief: [[90 System/briefs/MVP-phone|MVP-phone]]. Code (display fixes and date awareness) on top of P2.2's `c8b3b7b` in `dbrain-runtime`; Codex review round 5 failed (five blockers, fixed); rounds 6–8 failed and were fixed (logging and date reading redesigned after a Codex consultation); round 9, the fifth, failed on three date forms → **parked 6 Oct, uncommitted** (brief). David's phone gets it after a restart of `Ask Brain.command`.
- Existing tasks: **T9** moves here; **T4.1/T5/T6** begin with platform evaluation, redacted traces and service targets.

### S3 · Supervised wiki maintenance
- [ ] **P3.1** `@code` Implement agreed durable source IDs/versions, original evidence, derived claims, contradictions and review state. Preserve approved captures after triage under the agreed retention policy.
- [ ] **P3.2** `@code` Implement pending patches with evidence, exact diff, base revision and approval binding. Test rejected proposals and stale approvals after intervening edits.
- [ ] **P3.3** `@code` After T4.2, implement one deterministic writer: allowed paths, schema/link/classification validation, approved commit plus index/log updates. Test malicious source instructions, path escape and unauthorized writes.
- [ ] **P3.4** `@code` Independently regression-test and fix reviewed issues: `load-only` counted as runs (check both scripts), stream/moving-time coverage, per-activity zones, missing history vs inactivity, stale classifier instructions/examples. No code fixes are made by this amendment.
- [ ] **P3.5** `@cowork` **Subsumed by T3.4 (David, Q14, 5 Oct):** the quality-work definition lands in the rubric v2.0 wording. Kept for history: resolve OQ-16 before changing F3 quality-work semantics. Test strict tempo evidence versus the broad flag; version rule and expected-label changes.
- [ ] **P3.6** `@code` Freeze final running acceptance cases; preserve historical scores and label corrections; score arithmetic against independent expected outputs. Existing confidence values are heuristic, not calibrated probabilities.
- Existing tasks: **T4.2 → T4.3** gates runtime writes; **T3/T4.1** running validation continues alongside. **T7** adds evidence-state UI; existing skill escalation behavior stays until separately reviewed.

### S4 · Remote text and voice
- [ ] **P4.1** `@code` *(Private authenticated access built early as P2.4; uncommitted until P2.2 lands, acceptance incomplete.)* Implement private authenticated access and mobile text UI for agreed devices; keep the inference endpoint private. Specify canonical writer, vault sync and conflict policy separately.
- [ ] **P4.2** `@code` Add durable capture queue, pending/failure states, idempotent retries and cancellation. Test airplane mode, host sleep/restart and interrupted uploads without duplicate captures.
- [ ] **P4.3** `@code` Add local push-to-talk transcription and speech output; test French, English, mixed speech, names and noise. Define audio retention/deletion before recording.
- [ ] **P4.4** `@code` Test away from home on each agreed device class. Replace the interim Dispatch dependency and update CAPTURE only after the new route passes.

### S5 · Measurable multi-agent execution
- Existing task: **T11** introduces coordinator, curator and evidence checker with distinct permissions. The writer is deterministic; roles may share a model sequentially.
- [ ] **P5.1** `@code` Compare task success and unsupported-claim detection against the single-agent baseline, including latency and memory cost.
- [ ] **P5.2** `@code` Implement persistent jobs, bounded retries/time/tool budgets, cancellation and traceable handoffs. Test tool denial, checker failure, crash/resume and duplicate-write prevention.

### S6 · Operate and demonstrate
- [ ] **P6.1** `@code` Back up vault, source storage and required runtime state independently; restore after working-copy loss within T6 objectives. Distinguish rollback, sync and backup.
- [ ] **P6.2** `@code` Pin releases/model/runtime versions; document reproducible setup, restart, upgrade/rollback and incident handling. Run regressions before upgrades.
- [ ] **P6.3** `@code` Complete latency/error/queue/resource monitoring; verify redaction, access denial and retention. Instrumentation begins at S2.
- [ ] **P6.4** `@code` Package architecture, traces, evaluations and synthetic professional fixtures for a public-safe code/demo repository. Keep the personal vault private; publication requires its own authorization.
- Existing tasks: complete **T5/T6/T8/T12/T13** with normal, abstention, approved-update, failure and recovery demos. **T10** remains parked until the personal service is reliable.

**Exit evidence:** roadmap §0. Hardware/tools and numeric service targets remain open until measured or confirmed.

---

## Local model knowledge and weekly maintenance

- [x] **M1** Create a dated, sourced model guide across language/vision/code, ASR, TTS, images and retrieval. ✅ 1 Oct; [[30 Resources/Local AI/README]].
- [x] **M2** Record a second local candidate and first bounded lexical-retrieval experiment. ✅ 1 Oct; [[10 Projects/AI Second Brain/02_Architecture/local-comparison-retrieval-2026-10-01|results and limitations]]. This is development evidence, not P2 acceptance.
- [x] **M3** Prepare weekly research/benchmark review procedure, source revisions and scheduling prompt. ✅ [[90 System/weekly-local-model-review]].
- [x] **M4** Weekly local-project scheduling activated by David ✅ 1 Oct (D60, OQ-18 resolved). ⚠️ Open thread, not a blocker: the task ID and first-run output still need pasting into [[90 System/weekly-local-model-review]]'s activation record. Review the first two runs before relying on the cadence.
- [ ] **M5** `@code` Extend retrieval corpus with authoritative D49 retention evidence; compare controlled bilingual query expansion. Review expected evidence independently; retain original failures and untouched provisional cases.
- [ ] **M6** `@code` Compare another model family under comparable conditions. Set separate voice fixtures and local benchmark resource budgets before downloading additional modality models. Published benchmark review can proceed without downloads.

---

## LLM Wiki adoption (D41–D44, 1 Oct)

- [x] Create `index.md` and `log.md` at the vault root ✅ 1 Oct
- [x] Add "Wiki operations" to AGENTS.md ✅ 1 Oct
- [x] Write `90 System/lint-checklist.md` and run the baseline ✅ 1 Oct
- [x] **Decide on the 15 notes without `classification:`** ✅ 1 Oct, applied as proposed. Proposal: `internal` for project notes, Welcome.md `public`, the root CLAUDE.md stub exempt (one line, imports AGENTS.md)
- [ ] `@cowork` Triage the two Inbox items (`assistant-scope-ideas`, `how-to-automate-pm-job`) at the next weekly pass, and run lint then
- [ ] `@david` Triage `00 Inbox/2026-10-01 New-project scaffold.md` later (Q12: parked untouched, no brief and no guardrail work from it for now). Its `source:` line is not valid YAML; fix it at triage, not before
- [x] Resolve OQ-12 via D47: running is the domain; supervised wiki maintenance is shared platform work. ✅ 1 Oct
- [ ] `@code` Resolve remaining OQ-13 retention/IDs/metadata details at P1.3/P3.1 (routing and provenance settled by D49, 1 Oct).
- [ ] `@code` Automate lint at S3; corrections/index/log changes stay approval-gated. Read-only inspection is available now.

---

## Week 0 — Foundations

*Historical foundations: gate met 29 Sep. T0.7 remains future-only; original 14 Sep deadline is superseded.*

- [x] **T0.1 · Revoke the Telegram bot token** ✅ done 8 Sep `5 min` `🔴 security`
  Token `8842032811:AAFH…` is in `~/Documents/Source_Material/AI_Second_Brain/Product_School/Product School - Advanced Agents.pdf` (p.2). Revoke via BotFather → `/mybots` → select → API Token → Revoke.
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
- [ ] **T0.7 · Add an AI-use disclosure clause to the Tower13 contract template, and to live contracts at renewal** `@david` `1 h` `needs David + lawyer review`
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
- [x] **T2.6 · After 4 Oct: add Dinant chip time to `readiness-calls.md`, score the range** `2 min` `David` ✅ 5 Oct (Q22): chip 1:39:06, in range (1:38:54–1:45:01), committed `ee43923`

### Week 3 — Golden dataset ⭐
- [ ] **T3.1** `@cowork` Draft golden dataset v1 — 150 rows `4 h` `⭐ the showcase artifact`
  🟡 **Updated 1 Oct:** batches 01–03 (50 runs) are now development data. Batch 04 is fresh for v1.4. P3.6 reserves final acceptance cases. Historical held-out scores below describe the versions originally tested:
  - [x] Batch 02 · 20 runs ✅ 30 Sep. First held-out score of v1.2: terrain 17/20 (85%), intent 10/20 (50%). Sampling order fixed in `03_Golden/heldout-order.md` (seed 20260930)
  - [x] Rubric v1.3 + classify-session v0.4 ✅ 30 Sep (D27–D32). Batch 02 is now dev
  - [x] Batch 03 · 20 runs ✅ 30 Sep. v1.3 held-out: terrain 18/20, intent 14/20, tempo_block 14/20, vertical 16/20
  - [x] Batch 04 · 20 runs **labelled and scored** ✅ 2 Oct. Labelled by David blind (one run per screen, prepared by Cowork), then scored against rubric v1.4 by `@cowork` and validated by David the same day: [[10 Projects/AI Second Brain/03_Golden/labels-batch-04|labels-batch-04]]
    - **Held-out result, rubric v1.4:** terrain **100%** (D19 threshold ≥95% ✅) · intent **65%** (D19 threshold ≥85% ❌) · `tempo_block` **40%** · vertical **90%**. D19 sets no threshold for the two flags, so only terrain and intent are pass/fail.
    - **Read the flags against the trivial baseline, not against zero.** David labelled `tempo_block` and `vertical` as `no` on 17 of 20 runs each, so a rule that always answered "no" would score **85%** on both. `tempo_block` at **40% is far worse than that baseline** — the rule is actively harmful, firing on sustained Z3+ effort and so marking races and steady long runs as tempo blocks. Vertical at **90% barely beats it** (one run better than always-"no"), so it is close to uninformative on this sample. Both numbers are weak evidence either way at n=20 with 3 positives.
    - This is the evidence behind the v2 taxonomy (D67): the `tempo_block` failures are the race/tempo collision D66 settled by decision and v2 settles by construction, and the intent misses cluster the same way — `tempo` scored as `intervals` because reps with jog recoveries match I3 first, `long` scored as `easy` because runs fell just under the 15 km line.
    - [ ] **Independent Codex re-score of batch 04** `@codex` — asked for by David, 2 Oct; the lead hands it over, Codex never commits. The caveat is in the labels file: Cowork both prepared and scored the batch, so the scoring is not vendor-independent.
    - **This closes the last held-out test of the v1 schema, so T3.4 (taxonomy v2) is unblocked.**
    - Label process (Cowork, 2 Oct): intent was asked as one question with fixed options, after a two-part form confused run 1 and it had to be re-asked. A pre-scoring consistency check changed rows 13, 18, 19 and 20; the original labels are kept in the Note column, so **report scores both ways, as D38 did**.
    - Label distribution: intent — race 4 · long 7 · easy 5 · tempo 2 · intervals 1 · hills 1. Terrain — road 13 · trail 6 · mountain 1. All four races (rows 4, 9, 11, 15) are labelled `tempo_block = no`, which **D66** confirms is correct: a race is a race, not a tempo block.
  - [ ] `@cowork` Batch 05 · 20 runs
  - [ ] `@cowork` Batch 06 · 20 runs
  - [ ] `@cowork` Weeks · ~30 weekly assessments (~1 min each, split into 2 sessions)
  - [ ] `@code` Race times backtest (automatic from results; past readiness verdicts **not** labelled, because of hindsight bias)
  Columns: Input · Expected output · Edge case? · Judge type (rule/LLM). 20–30% edge cases.
- [ ] `@cowork` **After batch 04 is scored:** state the race exclusion explicitly in the `tempo_block` definition (rubric and [[30 Resources/Running/session-types|session-types]]), per D66. Deliberately **not** done before scoring — editing the rubric first would contaminate the held-out test.
- [ ] **T3.4 · Session taxonomy v2 (D67)** `@cowork` — proposal in [[90 System/briefs/T3.4-taxonomy-v2|T3.4-taxonomy-v2]]. Splits the mixed `intent` axis into terrain · format · dominant intensity · stacking context flags. **Approved in principle; the rubric v2.0 wording still needs David.** Strict sequence: score v1.4 on batch 04 first, then approve v2.0 wording, then rewrite the rubric and re-derive batches 01–04 by rule as v2 *development* data (05–06 become the first v2 held-out tests). v1.x scores stay in the record and are not comparable.
- [ ] **T3.2** `@cowork` Add adversarial rows (≥3) and note coverage gaps `1 h`
- [ ] **T3.3** `@code` Commit as `golden-dataset.md`, versioned like code `15 min`

### Week 4 — Evals + write access
- [ ] **T4.1** `@code` Wire versioned evaluations: independent deterministic checks first; rubric-based model judges with human spot checks for judgment. Begin platform suites at S2 and running suites alongside T3.
- [ ] **T4.2** `@code` Before S3 runtime writes, test bad-change rollback and independent restore on a disposable copy against T6 objectives. P6.1 extends recovery testing to deployment.
- [ ] **T4.3** `@code` After T4.2 passes, enable the scoped deterministic writer for approved patches with base-revision/path validation. No blanket autonomous-write permission.

**H1 gate — all four must be true:**
1. Three skills pass their stated thresholds
2. You have deliberately broken something and rolled it back
3. You can screen-share eval results
4. Zero client-confidential data has entered the system

---

## H2 · Weeks 5–9 — Validate

- [ ] **T5** `@code` Eval dashboard: start results/redacted traces at S2, complete at S6. Separate platform/running suites, mandatory approvals and avoidable exceptions; avoid unsupported drift claims.
  Test: *can you screen-share it in a sales call?* If not, it isn't done.
- [ ] **T6** `@code` Reliability contract: set targets before acceptance runs at S1/S2; include latency, recovery time/data loss, measurements, alerts and escalation. Verify at S6.
- [ ] **T7** `@code` Evidence UX at S3: supported/incomplete/conflicting/withheld, concise evidence/citations, overrides and reviewed corrections. Existing skill confidence scores are heuristic; preserve escalation until reviewed.
  Build the low-confidence path deliberately — you will demo it on purpose.
- [ ] **T8** `@cowork` (Q28) Governance one-pager: begin boundaries/data flow at S1, update with actual roles and permissions, review at S6. Include retention, escalation, authorization and agent topology.
- [ ] **T9 · S2** `@code` *(6 Oct: the three candidates named in the [[90 System/briefs/T9-M6-model-comparison|T9/M6 brief]] are downloaded and hash-verified, 15.65 GB (decimal; the four model files 15.59 GB, runtime copies 0.06 GB) of the 20 GB budget; the run was stopped after 2 of 9 blocks by David's clean-up directive, so there is no result yet. Restart the protocol from block 1.)* Benchmark local models against platform cases and available running development cases. Record quality, sustained latency, memory/context settings.
  **Rewritten 1 Oct (session 12):** this task used to ask "Air versus dedicated host, decided on evidence." D53 already answered it — an always-on requirement rules out a travelling laptop — so a gate phrased that way could no longer fail. The live question is now **which host spec and which model meet the D56 targets**: measure on the Air to choose the model and to size memory, then confirm on the host once it exists. Report peak memory explicitly, since it drives the 24 vs 32 GB call.
  External comparisons are optional and require explicit authorization; never a production fallback or prerequisite.

**Retained validation gate:** screen-shareable results, avoidable exceptions measured separately from mandatory approvals, governance review. Current delivery gates are roadmap §0.

---

## H3 · Weeks 10–13 — Collaborate & package

- [ ] **T10 · Parked after S6** `@code` Additional human users: scoped roots, enforced authorization and concurrency/sync tests. Metadata alone is not RBAC. Resolve OQ-3 first.
  A real second-user test is required when this extension is taken up; it does not block the personal service.
- [ ] **T11 · S5** `@code` Coordinator, curator and evidence checker with scoped tools, handoff traces and explicit autonomy limits. Compare with the single-agent baseline (P5.1).
  Name the quality or permission boundary each role addresses; implement bounded resumable execution (P5.2).
- [ ] **T12** `@code` Permissions/redaction from S2, source-injection/write tests before S3, remote-access checks before S4 exposure. Complete security/operational audit at S6.
- [ ] **T13 · S6** `@code` Rehearse twice: voice capture, cited answer, reviewed update, agent trace, controlled failure and recovery. Permitted running data and synthetic professional fixtures.

---

## Backlog / someday

- [ ] `@david` **Second domain: choose after the H1 gate** (see `00 Inbox/2026-09-30-1447-assistant-scope-ideas.md`). Proposed: family logistics, then knowledge digest. Parked questions: OQ-11
- [ ] **Personal data wave 1** `@david` (D69, Q26; data-policy §4a): ordinary personal material, first use case kids' schedules without names (§3a). **Gated on P1.4** plus a lint check of the four axes on new notes. Data, not a feature: no family-logistics build before the H1 gate.
- [ ] **Personal data wave 2** `@code` (D69, Q26; data-policy §4a): health beyond training, finances, journal; local-only. Gated on all five: (a) P2.2/P2.3 local answers with no cloud fallback · (b) access test proving cloud agents cannot reach the files (T12) · (c) synthetic leak test (T12) · (d) trace redaction live (T12) · (e) deletion rule tested on working copy, git history and backups (T8/P6.1).

- [ ] `@david` Migrate Apple Notes → markdown (export route; no API exists)
- [ ] `@david` Retrieve the 4 Product School capstone tools from the LMS (Strategy Assembler, AI Bet Evaluator, Roadmap Builder, Pitch Builder)
- [x] ~~Decide relationship between this project and the Vibe Coding app+deck deliverable~~ ✅ 1 Oct: **archived** (D62, OQ-5b resolved). One workstream — the second brain. If it revives it gets its own project folder.
- [ ] `@code` Infrastructure beyond the single controlled host: only on measured availability/workload need. Required local hosting evaluation is T9 at S2.

---

## Knowledge base follow-ups

- [ ] `@david` **Product School / NN/g follow-ups** (1 Oct): 🔴 revoke the bot token and redact meeting passcodes in the Advanced Agents PDF (all copies); export Apple Notes "Vibe Coding", "AI Product Management", "ProdSchool - MCPs" to PDF and ingest; ingest remaining NN/g decks (done 1 Oct: journey mapping, personas, persuasion, lean UX; workshops are image-only, needs OCR; ~20 other folders remain); review draft notes and promote status; git agent to commit the handoff entry.
- [x] ~~**SAFe KB follow-up**: verify 6.0 / 2024+ deltas, close AI-Native gaps~~ **Closed 1 Oct without doing it (D61, David's call):** the 5.1-era content is too old to be worth re-verifying. ⚠️ **Consequence: the SAFe pages are historical reference only and must not be used client-facing** — nobody has checked them against AI-Native SAFe or the 2024+ Disciplines. Re-obtaining current assets is a prerequisite if a client engagement ever needs them.

---

## Conventions

`🔴` security-sensitive · `⭐` high-leverage · `T0.x` week-0 · time estimates are working time, not elapsed.

`@code` `@cowork` `@codex` `@david` = owner tag (D63). **Every open task carries one since 5 Oct**, assigned by David's default rule (Q17): build/test/infra (P*, T4–T13, M*) → `@code` · independent reviews and re-scores → `@codex` · labelling, rubric wording, briefs, research → `@cowork` · personal/admin → `@david`. David confirmed the five edge cases on 5 Oct (Q28): T8 → `@cowork`, the other four as tagged.
Tick items as you go. Add anything that surfaces — an unrecorded task is a lost task.
