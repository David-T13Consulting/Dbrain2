---
classification: internal
review_status: codex-reviewed
---
# Progress Tracker — AI Second Brain Project

**Last updated:** 8 Oct 2026 · **Updated by:** Claude Code (session 40: Q85–Q87 as D107–D109; hang fix; P2.7 leak check; D108 access tests; Q88)

---

## Current state

| | |
|---|---|
| **Phase** | S1 requirements settled; S1 exit evidence incomplete (P1.3 data-flow diagram, roots/tools list); S2 under way: P2.2 query service committed (`4b5e91f`, runtime `c8b3b7b`); MVP-phone committed (P2.4, runtime `53e5740`); repos moved off iCloud to `~/Work` (M2, done 6 Oct); clean-up done, hold lifted (D81); P2.6 and P2.7 next. Running validation in parallel |
| **Schedule** | Original 13-week ordering superseded by S1–S6. Dated S2–S6 plan exists, proposed (`f9c014e`); demo-ready Fri 18 Dec 2026 (Q29) |
| **Target** | Client-ready demo, December 2026 |
| **Status** | 🟢 Week 0 closed · Week 1 closed · Week 2: 3 skills drafted and smoke-tested · Week 3: golden dataset **70/150** runs labelled. Batch 04 held out and scored 2 Oct — terrain 100% (≥95% ✅), intent 65% (≥85% ❌); the flags have no D19 threshold, and against the always-"no" baseline of 85% `tempo_block` at 40% is far worse while vertical at 90% barely beats it. The evidence behind the v2 taxonomy (D67) |
| **Dependencies** | Devices, availability, capacity, service targets and provenance schema all settled 1 Oct (D52–D59). Remaining dependency is the always-on host purchase (D53) — the Air cannot satisfy the availability requirement. Two local candidates and initial retrieval benchmarked, not accepted. Running labels continue independently |
| **Next action** | **Session 42 (9 Oct):** Q85–Q89 are answered (D107–D110, D113); rules D111 (small steps) and D112 (review budget per step) apply. Next: P2.7 stage C in steps C1, C1b, C2, C3, C3b, each reviewed and committed, stopping before C4 (real capture on, David sees it happen); then M6b (after P2.7, David 8 Oct). Earlier history: [[10 Projects/AI Second Brain/PROGRESS-archive\|PROGRESS-archive]] |
| **Action for David** | Open items are in [[10 Projects/AI Second Brain/TASKS\|TASKS]] (`@david`): order the host by Fri 16 Oct (Mac mini M5 Pro 64 GB / 1 TB via the SRL, D107); phone re-check on C2 (P2.4, D105); delete the review branch on GitHub; validate the P2.6 phrase set; TwIL-LM3-Pro licence (D99); weekly-review task ID (D60). Questions go through [[90 System/for-david\|for-david]] (none open). |

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

Moved verbatim on 8 Oct 2026 (session 38, David's maintenance layout): [[10 Projects/AI Second Brain/DECISIONS|DECISIONS]] holds D1 onwards. Sessions 1–37 are in [[10 Projects/AI Second Brain/PROGRESS-archive|PROGRESS-archive]]; this file keeps the last three sessions.
Decisions that notes cite as "in PROGRESS" are in DECISIONS.


---

## Session log

Newest first. One entry per working session — what happened, what changed, where to pick up.

### Session 42 — 9 Oct 2026 · Claude Code, lead loop (in progress)
**Authorization:** "pick up the loop" from David, 9 Oct. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only).

- **Claude Code extension version (Cowork's 09:00 entry, step 0):** v2.1.294 (`~/.vscode/extensions/anthropic.claude-code-2.1.294-darwin-arm64`, checked 9 Oct), past v2.1.251, so a per-call `model` wins over `CLAUDE_CODE_SUBAGENT_MODEL`: routing (D114) works; no Q90.

### Session 41 — 8 Oct 2026 · Claude Code, lead (Q88 as D110; Codex re-test; P2.7 stage C part 1 parked)
**Authorization:** Cowork's 18:10 entry (Q88 (c)) and the P2.7 go. **Ended by** the D72 review limit: P2.7 was parked. Closed in session 42 (9 Oct) per Cowork's 22:26 entry. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only).

- **Records:** `4cf843d` Q88 (c) as D110; `992c599` Codex re-test after David installed `/etc/codex/requirements.toml`: access tests pass on D110's terms.
- **P2.7 stage C part 1, parked, not committed:** `dbrain/failures.py`, `tests/test_failures.py`, `dbrain/outpath.py`, `dbrain/serve.py`, `experiments/server_log_check.py` left uncommitted in the runtime; five code review rounds, all FAIL; fixes after round 5 unreviewed. **Why parked:** the P2.7 brief had seven reviews in the run (two on the re-test record, five on the code), over D72's five per brief; the lead counted stage C on its own, the same mistake as session 39. Detail: [[90 System/briefs/P2.7-failure-capture-loop|P2.7]] Review, stage C part 1. Nothing captured; capture stays off.

**Pick up at:** stage C in steps (Cowork's 22:26 entry), reusing the parked code per step.

### Session 40 — 8 Oct 2026 · Claude Code, lead (Q85–Q87 recorded; hang fix; P2.7 leak check; D108 access tests)
**Authorization:** David, 8 Oct: commit Cowork's 17:06 entry and record Q85–Q87 (all (a)) as decisions; then commit the Q87 fix; resume P2.7 stage L with a fresh review budget and commit it; apply the Q86 deny rules and run the access test for each agent, no capture code until every agent fails to read the planted file. **Ended by** something needing David (Q88). Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only).

**What changed for David:** his host is decided (D107; he orders it by 16 Oct). The test-hang fix and the leak check are in. Under its main config and review profile, Codex is now kept out of the failure store by its sandbox (its full-access mode and computer-use plugins are not covered); Claude Code only partly (a disguised command gets through) and Cowork is untested, so nothing is captured yet: Q88.

- **Records:** `7824bd4`, D107 (host), D108 (deny rules), D109 (hang fix): [[10 Projects/AI Second Brain/DECISIONS|DECISIONS]].
- **Step 1:** runtime `3cbbd40` (hang fix, D109).
- **Step 2:** [[90 System/briefs/P2.7-failure-capture-loop|P2.7]] stage L, four review rounds this run (FAIL, FAIL, FAIL, PASS), runtime `d62fdf7`; records `a846110`.
- **Step 3:** deny rules in `~/.claude/settings.json` (+ hook) and `~/.codex/config.toml`, `review.config.toml` (backups `*.bak-2026-10-08-d108`); access tests; records and **Q88** ([[90 System/for-david]]) `228fd37`. The first hook pattern blocked the lead's own commands naming the P2.7 brief (narrowed); the first review-profile edit broke its TOML for a few minutes (fixed, retested).
- **Not done:** P2.7 stage C (capture) waits for Q88; M6b after P2.7. The planted test file stays in the store folder for future access tests.

**Pick up at:** David's Q88; Cowork's own access test; then stage C as Q88 decides; then M6b.

### Session 39 — 8 Oct 2026 · Claude Code, T9/M6 run with David (handoff item 2)
**Authorization:** David, about 14:00: "start T9 following handoff item 2 and the frozen protocol", confirming the window conditions (on power, lid open, Low Power Mode off, `Ask Brain.command` stopped, nothing heavy, no Codex during the run); `caffeinate -dimsu` around the whole run; pins re-checked against `dry-2026-10-08-final` before block 1; after T9, `.claude/settings.local.json` into `.gitignore`. **Ended by** the instruction's end: T9 measured, judged and reported; the choice is David's. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only).

**What changed for David:** T9 is done. The frozen rule picks **Gemma 4 E4B (C2)**: the only one of the four that never cited evidence wrongly, and the fastest (p95 10.1 s on the Air, still over the 8 s target). Two decisions are his: adopt it as the default (Q84), and which host to order by 16 Oct (Q85: Mac mini M5 Pro 64 GB / 1 TB from Apple Belgium through his SRL recommended, €3,032 ex VAT; Carlsbad compared: not cheaper under `unverified` tax assumptions). The Air was free again at 14:46.

- **Run `2026-10-08-a`:** 14:00:53–14:45:45, 9/9 blocks ok, no drift (−0.3 %), all pins matched before block 1 and the pre-run manifest equals the dry one except its start time. Results note [[10 Projects/AI Second Brain/02_Architecture/t9-model-comparison-2026-10-08|t9-model-comparison-2026-10-08]] (draft, Q7).
- **Judging:** the lead's verdicts were saved before Codex ran; Codex judged a masked packet blind. Safety: B0, C1 fail (both judges), C3 fails (one Codex-only finding; the pick is the same either way), C2 passes, Q 5/8. Disagreements listed in the note for David.
- **D95 sizing (Q85):** the pick alone sizes to 22.8 GB (→ 24 GB); the 48–64 GB band rests on layer 6, which has no named model; TTS and service memory are `unverified` estimates.
- **`.gitignore`:** `.claude/settings.local.json` added (it was already ignored by David's global git ignore on this Mac, not by the repo).
- **Not done:** the handoff's branch entry still waits on Q83 (`-D`). A `caffeinate -ims` (PID 53896) from an earlier session was running before this run and was left alone.

- **Data policy v0.7 (D106):** §7b audit trail added word for word. `data-policy.md` is in the dev-case corpus: the corpus version moves from `878a08ea6f57` (T9) to **`d926bd92ab8e`**, so later dev-case runs are not comparable to T9's without saying so.

- **Later the same session (David's list of 8 Oct, after T9):** Q85 revised for Belgium (ex VAT through his SRL; Carlsbad compared) `d0c3e92`. Q84 (a) and Q83 (a) recorded as D105; local review branch deleted with `-D`; all four models' numbers in the Local AI notes `48696f1`. Cowork's P2.7 brief update committed `8b679e4` (review fixes: §7a text-holding logs readable by David and the local model only). **Step 1:** phone service switched to Gemma 4 E4B, runtime `7874b6f` (tests 202 OK; dev cases identical to T9; smoke no regression). **Step 3:** data policy v0.7 §7b `5748ed0` (committed before step 2, which needed David). **Step 4:** P2.7 files in scope reviewed `734cd3b`, Q86 queued (cloud agents and the failure store; stage C blocked). **Step 2:** test-hang fix (listener timeout, watchdog; Codex consultation) reviewed PASS, Tier 2: **uncommitted, Q87**. **Stage L** (leak check) built, two code rounds FAIL; P2.7 **parked** after the lead overran the D72 review limit (seven reviews this run, not five), files untracked in the runtime. **M6b:** not started (after P2.7). Lead `claude-opus-5-5`; Codex `gpt-6.1-sol` throughout.
- **Uncommitted, on purpose:** runtime `dbrain/serve.py`, `tests/test_serve.py` (Q87); `dbrain/leakcheck.py`, `tests/test_leakcheck.py` (parked stage L).

**Pick up at:** David's Q85 (host, by 16 Oct), Q86, Q87. Then: commit the hang fix if approved; a stage L review round (fixes since round 2 unreviewed); stage C after Q86 is verified; then M6b.

### Session 38 — 8 Oct 2026 · Claude Code, lead loop (Q81/D103 records; Q82 landing; tracking-file maintenance)
**Authorization:** "pick up the loop" from David, with Q82 (a) ("approve both; land per D101") and his maintenance layout (8 Oct 11:10). **Ended by** the instruction's end: everything before T9 is done; T9 (handoff item 2) and item 6 remain, in a fresh session. The run stalled from about 11:25 until David resumed it, past the 12:40 stop and D102's 13:00 slot; one Codex call (about 13:25–13:47) ran after 13:00, while T9 had not started. On David's "ignore timing, finalize anything needed before T9", the TASKS review and this close were finished. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only).

**What changed for David:** both model-research pieces he approved are in the vault. The tracking files are much shorter: PROGRESS about 15 KB, TASKS 10 KB as one-liners, handoff about 7 KB, for-david 2 KB; nothing was deleted, everything moved verbatim to DECISIONS, the archives or log.md. One thing for him: the old review branch still exists, because the settings would not let the lead delete it.

- **Earlier in the session:** `293c813` Q81 (a) (D102), `5d1eb53` keep-awake rule (D103), `9208271` Hosting row, `8e3c449` Q82 queued.
- **Q82 (a):** `f25aa64` and `f6f8979` cherry-picked onto `master` (`f11ad99`, `061766b`; log.md conflict resolved by keeping both sides); `8c661a4` EmbeddingGemma 2 note (`review_status: approved`), retrieval link, ledger row, index entry, D104. Round 1 PASS (one should-fix: branch statement; reworded). **Branch deletion** (local and origin) refused by the permission settings; it is an `@david` item in TASKS.
- **Maintenance:** `fe9d899` verbatim split of PROGRESS (decision log → DECISIONS; sessions 1–35 → PROGRESS-archive), handoff (closed entries and run reports → log.md) and for-david (Answered → for-david-archive), plus the read-list pointers in the project CLAUDE.md, README, CAPTURE and index. A script checked that every original non-blank line is present at least once; only frontmatter lines and four reused headings appear twice. No Codex round for verbatim moves (David). `f2751c1` TASKS one-liners plus a verbatim TASKS-archive: rounds 1–4 FAIL, each on a gate or prerequisite dropped by compression (wave 1–2 gates; client-tier folder grant; M6 download prerequisite; T12 S3/S4 tests; T10 OQ-3; project-alignment diff approval; T7 escalation; P2.6 run order), all restored; round 5 PASS.
- **Subagents:** no custom subagent definitions exist in the vault, the runtime or `~/.claude`; only archived and external repos have them, left alone.
- **Note:** the T0.1 line (now in TASKS-archive) still shows the first characters of the Telegram bot token revoked on 8 Sep; moved as is, flagged to David.
- **Branch, Cowork's 13:50 entry (David, 13:49):** `git branch -d` refused ("not fully merged": cherry-picking gave the commits new hashes). The branch's content files are identical to `master` at `061766b` and its log entry is on `master`. Per the entry the lead did not use `-D`; **Q83** asks David. The remote branch is his to delete on GitHub.
- **Push:** pending after this close commit (non-force).

**Pick up at:** T9/M6 with David (fresh session); then M6b; P2.7 on David's go.


**Cowork, 8 Oct 13:45–22:28 (with David).** T9 readiness checked read-only; P2.7 brief revised (leak check option B, audit trail §7b, weekly review kept); Q84–Q88 put to David as multiple choice and recorded; Cowork's own D108 access test (file tools and shell refused; screen control untested); briefs now cut into steps that each fit one review cycle (David, 22:24; template updated). **Pick up at:** close session 41, then P2.7 stage C steps C1–C3 per the 22:26 handoff entry, stopping before C4.

---

## How to resume

1. Read `CLAUDE.md` (who, what, rules)
2. Read this file (state, decisions, last session)
3. Read `TASKS.md` (▶ Next action at the top)
4. Check `OPEN_QUESTIONS.md` for anything now answerable

Then work. Before you stop, update all three.
