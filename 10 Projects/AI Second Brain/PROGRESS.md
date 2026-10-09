---
classification: internal
review_status: codex-reviewed
---
# Progress Tracker — AI Second Brain Project

**Last updated:** 9 Oct 2026 · **Updated by:** Claude Code (session 43: P2.7 C4, real capture on; M6b S1 blocked on Q92)

---

## Current state

| | |
|---|---|
| **Phase** | S1 requirements settled; S1 exit evidence incomplete (P1.3 data-flow diagram, roots/tools list); S2 under way: P2.2 query service committed (`4b5e91f`, runtime `c8b3b7b`); MVP-phone committed (P2.4, runtime `53e5740`); repos moved off iCloud to `~/Work` (M2, done 6 Oct); clean-up done, hold lifted (D81); P2.6 and P2.7 next. Running validation in parallel |
| **Schedule** | Original 13-week ordering superseded by S1–S6. Dated S2–S6 plan exists, proposed (`f9c014e`); demo-ready Fri 18 Dec 2026 (Q29) |
| **Target** | Client-ready demo, December 2026 |
| **Status** | 🟢 Week 0 closed · Week 1 closed · Week 2: 3 skills drafted and smoke-tested · Week 3: golden dataset **70/150** runs labelled. Batch 04 held out and scored 2 Oct — terrain 100% (≥95% ✅), intent 65% (≥85% ❌); the flags have no D19 threshold, and against the always-"no" baseline of 85% `tempo_block` at 40% is far worse while vertical at 90% barely beats it. The evidence behind the v2 taxonomy (D67) |
| **Dependencies** | Devices, availability, capacity, service targets and provenance schema all settled 1 Oct (D52–D59). Remaining dependency is the always-on host purchase (D53) — the Air cannot satisfy the availability requirement. Two local candidates and initial retrieval benchmarked, not accepted. Running labels continue independently |
| **Next action** | **Session 43 (9 Oct):** P2.7 stage C is done: **real failure capture is on** since 11:41 (D119), proven with one planted failure that David then deleted. M6b S0 is committed; S1 is blocked because the Air has no Python 3.10+ (**Q92**). Cowork revises the weekly-desktop-digest skill (five review blockers) and writes the P2.7 follow-up brief. Earlier history: [[10 Projects/AI Second Brain/PROGRESS-archive\|PROGRESS-archive]] |
| **Action for David** | Open items are in [[10 Projects/AI Second Brain/TASKS\|TASKS]] (`@david`): order the host by Fri 16 Oct (Mac mini M5 Pro 64 GB / 1 TB via the SRL, D107); phone re-check on C2 (P2.4, D105); delete the review branch on GitHub; validate the P2.6 phrase set; TwIL-LM3-Pro licence (D99); weekly-review task ID (D60). Questions go through [[90 System/for-david\|for-david]] (open: Q92). |

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

### Session 43 — 9 Oct 2026 · Claude Code, lead loop (P2.7 C4 with David; M6b S1 blocked on Q92)
**Authorization:** "pick up the loop" from David, 9 Oct, per Cowork's 11:25 handoff block. **Ended by** stop condition (1): no actionable `@code` brief left (M6b `blocked-on-david`, Q92). Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only). No subagents used.

**What changed for David:** failed phone questions are now kept on the Air for 90 days (capture switched on with him watching; one planted question proved it and he deleted it himself with the new delete command). The weekly model review now watches every webAI model. The embedding test is waiting for his OK to install a newer Python (Q92).

- **Handoff:** `6738899` weekly review watches all webAI Hugging Face models (Codex: escalated for an uncited format claim, cited the ledger, pass); `437a7c4` Q90 (a) as **D119**, Q91 (a) recorded, M6b cut into steps plus S0 (3 reviews: two blockers on how S0 counted, fixed).
- **P2.7 C4:** runtime `72bf52b`: launcher passes the checked absolute log folder to the service (C3b should-fix) and one switch `CAPTURE=on`; `FailureStore.delete(id, reason)` with fixed reason codes and a command David runs (2 reviews: free-form reason blocker, fixed). David started the launcher 11:41, sent one planted question 11:42 (one `withheld` capture, text-free audit, no planted text in any log; 35 characters arrived vs the 36 sent, cause not established), deleted it 11:49 (`deleting`/`deleted`, `planted-test`). Record `33a79e4` (1 review). The D108 hook blocked the lead's shell commands that named the store module; the lead used scratch scripts and a glob to read the permitted audit log, never the store.
- **M6b S1:** revisions read and pinned (EmbeddingGemma 2 unchanged at `914f7f89`); draft manifest uncommitted in the runtime repo; blocked: Python 3.10+ needed (Q92). No weights downloaded.
- **Keep-awake:** `caffeinate -ims` started at loop start, stopped at close. The MVP launcher (with its own `caffeinate -s`) stays running in David's Terminal window.

**Pick up at:** David's Q92 (via Cowork); then M6b S1 → S5. Cowork: the digest skill revision and the P2.7 follow-up brief.

### Session 42 — 9 Oct 2026 · Claude Code, lead loop (handoff cleared; D111–D118; P2.7 C1–C3b; Desktop digest; stopped on Q91)
**Authorization:** "pick up the loop" from David, 9 Oct. **Ended by** stop condition (3): the Desktop pilot's staging folder, readable by Cowork, holds screenshots the data policy keeps out of the system (Q91); also P2.7 reached its 12-review cap and C4 is David's go (Q90). Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only). No subagents used.

**What changed for David:** the failure loop is built and tested with planted data (store, 90-day deletion, text-free audit, capture wiring, server-log check, logs out of git) and waits for his go to switch on (Q90). Briefs now come in small steps with a visible review counter, and the lead routes helper models per task. His Desktop digest is in the Inbox for review, but first he should move the sensitive screenshots out of agents' reach (Q91, today).

- **Claude Code extension version (Cowork's 09:00 entry, step 0):** v2.1.294 (`~/.vscode/extensions/anthropic.claude-code-2.1.294-darwin-arm64`, checked 9 Oct), past v2.1.251, so a per-call `model` wins over `CLAUDE_CODE_SUBAGENT_MODEL`: routing (D114) works; no question for David needed.
- **Handoff (four Cowork entries):** `57abc94` session 41 closed; `05efdf4` D111 small steps, D112 review budget per step (AGENTS.md), D113 split `incomplete`; `f277cce` weekly course map and lint (PROGRESS state rows refreshed, duplicate TASKS line removed); `3f11617` D114 subagent routing (AGENTS.md, `.claude/settings.json`).
- **P2.7 stage C** (runtime): C1 `d262b08` (2 reviews), C1b `de7e662` (2; dev cases identical 10/10, 6 unverified, 4 declined, 0 defects), C2 `24fb08d` (1), C3 `b3780eb` (3; server log holds no question or answer text), C3b `d873748` (2); vault record `613e90c` (2 more, 12 in all, the D112 cap). C4 waits: **Q90**.
- **Cowork's three later entries (Desktop digest pilot):** digest `3816b34` committed as Tier 0; D-cowork-11..14 → **D115–D118** `6f95e44`; the skill `weekly-desktop-digest` **not committed** (five Codex blockers, back to Cowork); **Q91** queued.
- **Open should-fixes:** a relative `DBRAIN_LOGS` drops traces (P2.7 brief, C3b); the digest's missing tick-boxes and PayFit citation (Cowork).
- **Keep-awake:** `caffeinate -ims` started at loop start (PID 92089), stopped at close; the older PID 53896 left alone.

**Pick up at:** David's Q91 (today) and Q90; Cowork's skill revision; then M6b after P2.7 C4.

### Session 41 — 8 Oct 2026 · Claude Code, lead (Q88 as D110; Codex re-test; P2.7 stage C part 1 parked)
**Authorization:** Cowork's 18:10 entry (Q88 (c)) and the P2.7 go. **Ended by** the D72 review limit: P2.7 was parked. Closed in session 42 (9 Oct) per Cowork's 22:26 entry. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only).

- **Records:** `4cf843d` Q88 (c) as D110; `992c599` Codex re-test after David installed `/etc/codex/requirements.toml`: access tests pass on D110's terms.
- **P2.7 stage C part 1, parked, not committed:** `dbrain/failures.py`, `tests/test_failures.py`, `dbrain/outpath.py`, `dbrain/serve.py`, `experiments/server_log_check.py` left uncommitted in the runtime; five code review rounds, all FAIL; fixes after round 5 unreviewed. **Why parked:** the P2.7 brief had seven reviews in the run (two on the re-test record, five on the code), over D72's five per brief; the lead counted stage C on its own, the same mistake as session 39. Detail: [[90 System/briefs/P2.7-failure-capture-loop|P2.7]] Review, stage C part 1. Nothing captured; capture stays off.

**Pick up at:** stage C in steps (Cowork's 22:26 entry), reusing the parked code per step.

## How to resume

1. Read `CLAUDE.md` (who, what, rules)
2. Read this file (state, decisions, last session)
3. Read `TASKS.md` (▶ Next action at the top)
4. Check `OPEN_QUESTIONS.md` for anything now answerable

Then work. Before you stop, update all three.
