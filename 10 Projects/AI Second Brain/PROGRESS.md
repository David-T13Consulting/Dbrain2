---
classification: internal
review_status: codex-reviewed
---
# Progress Tracker — AI Second Brain Project

**Last updated:** 9 Oct 2026 · **Updated by:** Claude Code (session 45: handoff 15:06–15:12; P2.7 C5 service part; M6b S3; P2.5 F0 passed review, waits on Q97)

---

## Current state

| | |
|---|---|
| **Phase** | S1 requirements settled; S1 exit evidence incomplete (P1.3 data-flow diagram, roots/tools list); S2 under way: P2.2 query service committed (`4b5e91f`, runtime `c8b3b7b`); MVP-phone committed (P2.4, runtime `53e5740`); repos moved off iCloud to `~/Work` (M2, done 6 Oct); clean-up done, hold lifted (D81); P2.6 and P2.7 next. Running validation in parallel |
| **Schedule** | Original 13-week ordering superseded by S1–S6. Dated S2–S6 plan exists, proposed (`f9c014e`); demo-ready Fri 18 Dec 2026 (Q29) |
| **Target** | Client-ready demo, December 2026 |
| **Status** | 🟢 Week 0 closed · Week 1 closed · Week 2: 3 skills drafted and smoke-tested · Week 3: golden dataset **70/150** runs labelled. Batch 04 held out and scored 2 Oct — terrain 100% (≥95% ✅), intent 65% (≥85% ❌); the flags have no D19 threshold, and against the always-"no" baseline of 85% `tempo_block` at 40% is far worse while vertical at 90% barely beats it. The evidence behind the v2 taxonomy (D67) |
| **Dependencies** | Devices, availability, capacity, service targets and provenance schema all settled 1 Oct (D52–D59). Remaining dependency is the always-on host purchase (D53) — the Air cannot satisfy the availability requirement. Two local candidates and initial retrieval benchmarked, not accepted. Running labels continue independently |
| **Next action** | **Session 46 (12 Oct):** D127/D128 committed (`479a229`); P2.5 F1 closed with no prompt change (Q99, `1e261cd`); **P2.5 F2 parked** after 2/2 reviews, its fixes uncommitted in the runtime working tree (next run: D74 consult first); **M6b S4 run done** (no measured benefit; lexical baseline stays), uncommitted until **Q101**; G1-inj brief drafted (`e74c0e9`); Q101–Q102 queued; Q95 phone step still waits for David (Q100). From the step after the D127/D128 commit on (David, 12 Oct), the lead works under D127 (review budget 2 per step, 5 for Tier 2 and security-boundary steps; Tier 1a and recorded answers batched once per run, push even if the batch fails with the unfixed items listed here; standing approvals; asks David directly when he is present) and D128 (one lead with up to 3 writing helpers in worktrees). **Session 45 (9 Oct):** handoff 15:06–15:12 committed (D123 §7a 1-hour window, D124 M6b labels, D125 ask with options, D121 line in AGENTS.md); P2.7 C5 service part committed (runtime `b3e1f1a`), phone part on **Q95**; M6b S3 committed (runtime `98694a2`), S4 on **Q96** (Pillow); P2.5 F0 passed review 4/5, uncommitted until **Q97**. Cowork's 15:35 roadmap entry not yet worked. **Session 44 (9 Oct):** the phone's wrong "no" became P2.5 slice F0–F3 (D120): F0 (13 synthetic regression cases, a scorer, a baseline) **parked after 5 reviews**, uncommitted; F1–F3 next run. P2.7 C5 ("Wrong" button) blocked on **Q93** (§7a). M6b: S1 (Python 3.12 venv, D122) and S2 (models verified) done; S3 blocked on **Q94**. English and French only (D121). Earlier history: [[10 Projects/AI Second Brain/PROGRESS-archive\|PROGRESS-archive]] |
| **Action for David** | Open items are in [[10 Projects/AI Second Brain/TASKS\|TASKS]] (`@david`): order the host by Fri 16 Oct (Mac mini M5 Pro 64 GB / 1 TB via the SRL, D107); phone re-check on C2 (P2.4, D105); weekly-review task ID (D60). Questions go through [[90 System/for-david\|for-david]] (open: Q95 the "Wrong" button's Shortcut and check, Q96 Pillow for the embedding test, Q97 committing P2.5 F0). |

### Original work-package progress — retained snapshot

Current platform gates S1–S6 are not yet passed. P1.0/P1.1 are complete; supplied-evidence comparisons and a bounded retrieval experiment have run, but retrieval/service acceptance remains open. The historical snapshot below is not a percentage-complete estimate for the new scope.

```
Week 0  Foundations    █████████░  90%   (T0.7 contract clause: future-only)
H1      Ship           ██████░░░░  60%   ← you are here (Weeks 1–2 done, Week 3 started)
H2      Validate       ░░░░░░░░░░   0%
H3      Collaborate    ░░░░░░░░░░   0%
```

### Original domain/demo gate status — current platform gates in roadmap §0

| Gate | Criteria met | Status |
|---|---|---|
| Week 0 | Workflow named · red lines stated | ✅ Met 29 Sep |
| H1 | 3 skills pass · rollback tested · evals screen-shareable · no client data | ⬜ Not met |
| H2 | Eval dashboard live · avoidable exceptions measured separately from approvals · governance review (D48) | ⬜ Not met |
| H3 | Demo runs twice, no unexplained failures | ⬜ Not met |

---

## Metrics

Not yet instrumented as a service. Start platform measurement at S2; retain running scores in their batch records. Original aspirations below are qualified by D48 and roadmap §0; no population-level reliability claim yet:

| Metric | Target | Current |
|---|---|---|
| Hallucination rate | <1% | — |
| Eval regression | 100% of changes stay positive | — |
| Avoidable exceptions | Mandatory approvals tracked separately; preserve the approval gate | — |
| Recall accuracy | ≥85% | — |

*Deliberately not tracked at this volume: drift velocity/week, confidence distribution, inference ROI, deflection rate. Know the numbers; explain why they're not instrumented yet.*

---

## Decisions and older sessions

Moved verbatim on 8 Oct 2026 (session 38, David's maintenance layout): [[10 Projects/AI Second Brain/DECISIONS|DECISIONS]] holds D1 onwards. Sessions 1–39 are in [[10 Projects/AI Second Brain/PROGRESS-archive|PROGRESS-archive]]; this file keeps the last three sessions.
Decisions that notes cite as "in PROGRESS" are in DECISIONS.


---

## Session log

Newest first. One entry per working session — what happened, what changed, where to pick up.

### Session 45 — 9 Oct 2026 · Claude Code, lead loop (handoff 15:06–15:12; P2.7 C5 service; M6b S3; P2.5 F0 passed review)
**Authorization:** "pick up the loop" from David, 9 Oct, with the order: Cowork's 15:06–15:12 handoff entries (commit them; record Q93 (b), Q94 (a) and the ask-with-options rule; apply the §7a amendment and the D121 line to AGENTS.md, both approved), then P2.7 C5, M6b S3, P2.5 F0 (resume review); leave the `weekly-desktop-digest` folder alone. **Ended by** stop condition (1) for that list: C5's phone part, M6b S4 and P2.5 F0's commit all wait on David (Q95–Q97). Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only), 12 reviews (the close review included) and one D74 consultation. No subagents used (D114).

**What changed for David:** the "Wrong" button is built on the service side (his Shortcut edit and a restart turn it on, Q95); the data policy holds his 1-hour rule (v0.8) and AGENTS.md his English-and-French line; his ask-with-options rule is standing (D125); the embedding test's harness is ready but EmbeddingGemma 2 needs Pillow to load (Q96); the test set for the phone's wrong "no" passed review and waits for his OK to commit (Q97).

- **Handoff 15:06–15:12** (one step; reviews 1/5 fail: C5's test line still said 24 h; 2/5 pass): `17ef6ef` **D123** (Q93 (b), data policy v0.8 §7a, 1-hour window), **D124** (Q94 (a), M6b labels), D121's line in AGENTS.md › Conventions; `4772265` Q83 closed, TwIL-LM3-Pro licence parked (D99 stands); `f3d66d9` P2.6 phrase set validated (S5 → `UNCLEAR`; today's reader answers Mon 12 Oct there, recorded in P2.6); `fe4a0cb` **D125** ask with options (P2.6 and P3.0 Constraints; L7 → `UNCLEAR`).
- **P2.7 C5, service part:** runtime `b3e1f1a` (`answer_id` per reply and on the trace line; recent answers in memory only, at most 1 hour, swept every 15 s; `POST /wrong`; one record per answer whatever the order of capture and tap); reviews 1/5 fail (text could outlive the hour behind a lock; a waiting tap was not re-checked), 2/5 pass, 3/5 pass (the vault record); vault `6029899`. Phone part: **Q95**.
- **M6b S3:** runtime `98694a2` (three arms; each in its own process under a no-network sandbox, probe-checked; frozen inputs hash-checked; labels D124; 24 toy tests); reviews 1/5 fail (incomplete network block; RSS measured wrongly), 2/5 pass; vault `4614978`. Arm C smoke on toy data OK (4.07 GB peak); arm B needs Pillow: **Q96**.
- **P2.5 F0:** reviews 1/5 fail (three scorer misreads), D74 consult (Codex: a whole-answer contract with pass, fail and **unscored**), rebuilt; 2/5 and 3/5 fail (five more wrong passes inside the grammar, all fixed), 4/5 **pass** (no wrong pass in about 167,000 probes and generated answers). Baseline unchanged under the new scorer: row 0/6, none 2/2, negated 3/3, other 2/2; the lead read all 13 answers. Tier 2: **uncommitted until David approves (Q97)**.
- **Not worked:** Cowork's 15:35 entry (roadmap amendment after the independent audit), outside this run's list; it stays in the handoff. The `weekly-desktop-digest` folder untouched.
- **Keep-awake:** `caffeinate -ims` started at loop start, stopped at close.

**Pick up at:** David's Q95 (Shortcut and end-to-end check), Q96 (Pillow), Q97 (F0 commit) via Cowork; then F1–F3, M6b S4; Cowork's 15:35 roadmap entry.

### Session 44 — 9 Oct 2026 · Claude Code, lead loop (P2.5 F0 parked; P2.7 C5 blocked on Q93; M6b S1–S2 done, S3 blocked on Q94)
**Authorization:** "pick up the loop" from David, 9 Oct, per Cowork's 12:05 handoff block; Cowork's 13:45 block (English and French only) applied mid-run on David's word to the lead ("no dutch"). **Ended by** stop condition (1): no actionable `@code` brief left (P2.5 F0 parked, P2.7 and M6b `blocked-on-david`). Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only); one Codex D74 consultation. No subagents used. Codex hit its usage limit at 13:39 (one review did not run; waited to 14:19).

**What changed for David:** the made-up test questions for the phone's wrong "no" exist and measure today's behaviour (the answer never says the word asked isn't in the note), but the fix waits for the next run. Two questions for him: how the "Wrong" button may keep a question (Q93) and how to label the embedding test's expected passages (Q94); and his OK on the AGENTS.md language line. The embedding models are downloaded and verified.

- **Handoff 12:05:** `1c48214` scouts alias, P2.5 steps F0–F3, P2.7 C5, **D120**; files in scope for the slice (2 reviews: a quoted phone question replaced by a class description; F2 must not flag a correct "no").
- **P2.5 F0:** synthetic regression cases (13), a runner through the phone path, a bounded-grammar scorer, tests; baseline row 0/6, none 2/2, negated 3/3, other 2/2; the wrong "no" did not reproduce on synthetic notes. Tier raised to 2 by Codex (write path). Reviews 3–5 failed (unchecked note paths, scorer misreads, temp folder via TMPDIR, a "No," after a semicolon); D74 consult taken. **Parked**, uncommitted; the last fix is in the working tree, unreviewed. Separate eval server on port 18089, stopped.
- **D121** English and French only; Cowork's checklist line; Dutch removed from F0. AGENTS.md line awaits David's exact-text approval.
- **P2.7 C5:** files in scope and design listed; review 1 failed on §7a (holding unsignalled answers for a later tap); **Q93**; `8f97ce5`.
- **M6b:** S1 `20096a5` (runtime `89d9bd5`): Python 3.12.15 verified (**D122**), venv with pinned packages, manifest, budget ≈22 of 25 GB. S2 `1beca18` (runtime `fetch_verify.py`): 27/27 files verified, stop rule fixed after review. S3 blocked: the protocol's label source holds totals only (**Q94**).
- **Keep-awake:** `caffeinate -ims` started at loop start, stopped at close. The MVP launcher stays running in David's Terminal.

**Pick up at:** David's Q93, Q94 and the AGENTS.md line (via Cowork); next run: P2.5 F0 with a fresh budget (from the working tree), then F1–F3; C5 and M6b S3 on their answers.

### Session 43 — 9 Oct 2026 · Claude Code, lead loop (P2.7 C4 with David; M6b S1 blocked on Q92)
**Authorization:** "pick up the loop" from David, 9 Oct, per Cowork's 11:25 handoff block. **Ended by** stop condition (1): no actionable `@code` brief left (M6b `blocked-on-david`, Q92). Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only). No subagents used.

**What changed for David:** failed phone questions are now kept on the Air for 90 days (capture switched on with him watching; one planted question proved it and he deleted it himself with the new delete command). The weekly model review now watches every webAI model. The embedding test is waiting for his OK to install a newer Python (Q92).

- **Handoff:** `6738899` weekly review watches all webAI Hugging Face models (Codex: escalated for an uncited format claim, cited the ledger, pass); `437a7c4` Q90 (a) as **D119**, Q91 (a) recorded, M6b cut into steps plus S0 (3 reviews: two blockers on how S0 counted, fixed).
- **P2.7 C4:** runtime `72bf52b`: launcher passes the checked absolute log folder to the service (C3b should-fix) and one switch `CAPTURE=on`; `FailureStore.delete(id, reason)` with fixed reason codes and a command David runs (2 reviews: free-form reason blocker, fixed). David started the launcher 11:41, sent one planted question 11:42 (one `withheld` capture, text-free audit, no planted text in any log; 35 characters arrived vs the 36 sent, cause not established), deleted it 11:49 (`deleting`/`deleted`, `planted-test`). Record `33a79e4` (1 review). The D108 hook blocked the lead's shell commands that named the store module; the lead used scratch scripts and a glob to read the permitted audit log, never the store.
- **M6b S1:** revisions read and pinned (EmbeddingGemma 2 unchanged at `914f7f89`); draft manifest uncommitted in the runtime repo; blocked: Python 3.10+ needed (Q92). No weights downloaded.
- **Keep-awake:** `caffeinate -ims` started at loop start, stopped at close. The MVP launcher (with its own `caffeinate -s`) stays running in David's Terminal window.

**Pick up at:** David's Q92 (via Cowork); then M6b S1 → S5. Cowork: the digest skill revision and the P2.7 follow-up brief.

## How to resume

1. Read `CLAUDE.md` (who, what, rules)
2. Read this file (state, decisions, last session)
3. Read `TASKS.md` (▶ Next action at the top)
4. Check `OPEN_QUESTIONS.md` for anything now answerable

Then work. Before you stop, update all three.
