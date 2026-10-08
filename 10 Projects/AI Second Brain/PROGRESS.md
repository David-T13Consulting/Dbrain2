---
classification: internal
review_status: codex-reviewed
---
# Progress Tracker — AI Second Brain Project

**Last updated:** 8 Oct 2026 · **Updated by:** Claude Code (session 39, T9/M6 run, judged and reported; Q84, Q85 queued)

---

## Current state

| | |
|---|---|
| **Phase** | S1 requirements settled; S1 exit evidence incomplete (P1.3 data-flow diagram, roots/tools list); S2 under way: P2.2 query service committed (`4b5e91f`, runtime `c8b3b7b`); MVP-phone committed (P2.4, runtime `53e5740`); repos moved off iCloud to `~/Work` (M2, done 6 Oct); clean-up done, hold lifted (D81); P2.6 and P2.7 next. Running validation in parallel |
| **Schedule** | Original 13-week ordering superseded by S1–S6. Dated S2–S6 plan exists, proposed (`f9c014e`); demo-ready Fri 18 Dec 2026 (Q29) |
| **Target** | Client-ready demo, December 2026 |
| **Status** | 🟢 Week 0 closed · Week 1 closed · Week 2: 3 skills drafted and smoke-tested · Week 3: golden dataset **70/150** runs labelled. Batch 04 held out and scored 2 Oct — terrain 100% (≥95% ✅), intent 65% (≥85% ❌); the flags have no D19 threshold, and against the always-"no" baseline of 85% `tempo_block` at 40% is far worse while vertical at 90% barely beats it. The evidence behind the v2 taxonomy (D67) |
| **Dependencies** | Devices, availability, capacity, service targets and provenance schema all settled 1 Oct (D52–D59). Remaining dependency is the always-on host purchase (D53) — the Air cannot satisfy the availability requirement. Two local candidates and initial retrieval benchmarked, not accepted. Running labels continue independently |
| **Next action** | **T9/M6 ran 8 Oct (session 39): the rule picks C2, Gemma 4 E4B** ([[10 Projects/AI Second Brain/02_Architecture/t9-model-comparison-2026-10-08\|results]]). David decides the default model (Q84) and the host, ordered by Fri 16 Oct (Q85, D95). Then M6b (D100), then P2.7 on David's go. **Session 38 (8 Oct):** the 8 Oct weekly review and the EmbeddingGemma 2 desk note are in the vault (Q82 (a), D104); the tracking files are split per David's layout (decisions in [[10 Projects/AI Second Brain/DECISIONS\|DECISIONS]], older sessions and tasks in the archives). Open with David: delete branch `cowork/local-model-review-2026-10-08` (the settings refused the lead); phone re-check (P2.4); P2.6 phrase set; TwIL-LM3-Pro licence (D99). Earlier history: [[10 Projects/AI Second Brain/PROGRESS-archive\|PROGRESS-archive]] |
| **Action for David** | **All six session-14 questions are answered and recorded** — his standing actions below are unaffected: D64 closed, the `dbrain-runtime` repository authorised (now `~/Work/dbrain-runtime/`), batch 04 scored by `@cowork`, and Q5/Q6 answered through the [[90 System/for-david|for-david]] queue on its first use — Codex may read the 6 reserved cases read-only (P2.1 unblocked), and nothing changes on David's side for interactive Codex (D68 closed). Then: paste the weekly-review task ID and first-run output into [[90 System/weekly-local-model-review|weekly-local-model-review]] (D60). Decide the always-on host purchase (D53; 32 GB recommended). OQ-20 is answered (queue Q10, 5 Oct); OQ-21 was not needed — David decided it himself as D66. |

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

Moved verbatim on 8 Oct 2026 (session 38, David's maintenance layout): [[10 Projects/AI Second Brain/DECISIONS|DECISIONS]] holds D1 onwards. Sessions 1–36 are in [[10 Projects/AI Second Brain/PROGRESS-archive|PROGRESS-archive]]; this file keeps the last three sessions.
Decisions that notes cite as "in PROGRESS" are in DECISIONS.


---

## Session log

Newest first. One entry per working session — what happened, what changed, where to pick up.

### Session 39 — 8 Oct 2026 · Claude Code, T9/M6 run with David (handoff item 2)
**Authorization:** David, about 14:00: "start T9 following handoff item 2 and the frozen protocol", confirming the window conditions (on power, lid open, Low Power Mode off, `Ask Brain.command` stopped, nothing heavy, no Codex during the run); `caffeinate -dimsu` around the whole run; pins re-checked against `dry-2026-10-08-final` before block 1; after T9, `.claude/settings.local.json` into `.gitignore`. **Ended by** the instruction's end: T9 measured, judged and reported; the choice is David's. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only).

**What changed for David:** T9 is done. The frozen rule picks **Gemma 4 E4B (C2)**: the only one of the four that never cited evidence wrongly, and the fastest (p95 10.1 s on the Air, still over the 8 s target). Two decisions are his: adopt it as the default (Q84), and which host to order by 16 Oct (Q85: Mac mini M5 Pro 64 GB / 1 TB recommended, €3,649). The Air was free again at 14:46.

- **Run `2026-10-08-a`:** 14:00:53–14:45:45, 9/9 blocks ok, no drift (−0.3 %), all pins matched before block 1 and the pre-run manifest equals the dry one except its start time. Results note [[10 Projects/AI Second Brain/02_Architecture/t9-model-comparison-2026-10-08|t9-model-comparison-2026-10-08]] (draft, Q7).
- **Judging:** the lead's verdicts were saved before Codex ran; Codex judged a masked packet blind. Safety: B0, C1 fail (both judges), C3 fails (one Codex-only finding; the pick is the same either way), C2 passes, Q 5/8. Disagreements listed in the note for David.
- **D95 sizing (Q85):** the pick alone sizes to 22.8 GB (→ 24 GB); the 48–64 GB band rests on layer 6, which has no named model; TTS and service memory are `unverified` estimates.
- **`.gitignore`:** `.claude/settings.local.json` added (it was already ignored by David's global git ignore on this Mac, not by the repo).
- **Not done:** the handoff's branch entry still waits on Q83 (`-D`). A `caffeinate -ims` (PID 53896) from an earlier session was running before this run and was left alone.

**Pick up at:** Q84 and Q85 with David (host order by 16 Oct); then M6b (D100); P2.7 on David's go.

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

### Session 37 — 8 Oct 2026 · Claude Code, lead loop (09:35 block; T9 readiness; Q79/Q80; triage; M6b; queue)
**Authorization:** "pick up the loop" from David, with Q79 (a) and Q80 (a); the handoff's 8 Oct ~09:35 block first (records, T9 readiness with a go/no-go by 18:00, Inbox triage), then Q79/Q80 and the client-tier note, then the queued entries (Q78/`f25aa64`, EmbeddingGemma, M6b). No P2.7. **Ended by** the instruction's end (all items run). Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile), high, read-only.

**What changed for David:** T9 can run on Friday morning with him (Q81); nothing was scored. His host can be a 48–64 GB machine up to €4,000. The agents now refuse force pushes in the forms he approved. His client-tier requirements note is in the vault, its legal points still marked for the lawyer. Two captures are triaged (a parked project-alignment brief; an EUrouter resource), and Tower13 has an area. The embedding test has a brief and a slot after T9. The weekly model review and the EmbeddingGemma note went back to Cowork for sources before he is asked to approve them.

- **09:35 item 1:** `54a511f`, D95 (host option B) and D96 (T9 window). Round 1 PASS.
- **09:35 item 2, T9 readiness:** the runner `t9_compare.py` (the 6 Oct draft) failed review three times (8, 5, 4 blockers: timeouts and malformed replies lost, server outside the sandbox, network check failing open, unchecked manifest, incomplete RSS, unpinned cases); rewritten, round 4 PASS; runtime `ae934d5`, pushed. Four models and b11146 match their SHA-256 pins; all load and answer the warm-up under the no-network sandbox (dry check, nothing scored). Dev cases re-checked on corpus `878a08ea6f57`: three points listed in the T9 brief, rule unchanged. `da3be79`; **Q81 GO**.
- **09:35 item 3:** `3a7f819`, Inbox triage. The EUrouter capture was archived to `40 Archive/Inbox/` (D49) instead of `git rm` (deleting files is a hard limit). Rounds: FAIL (uncited legal framing; boundary stricter than the policy), escalate (question 4 proposed an answer), PASS.
- **Q79:** `8034de8`, deny list applied (D97), Tier 2 PASS. **Q80:** `1cf0bfc`, client-tier note committed (D98), PASS.
- **M6b:** `d19b409` (D100: Q8 budget 25 GB, venv), round 1 FAIL (scope), round 2 PASS. **D99/D101:** `182b9df` (TwIL licence answer; Q78 route), PASS.
- **Weekly review `f25aa64` and the EmbeddingGemma desk note:** Codex content pass FAIL (Tier 2 provenance: TwIL-LM2 claims unsourced; the EmbeddingGemma note misreads the MTEB versions, one claim unsourced, one negative claim unsupported). Findings in [[90 System/handoff]] for Cowork; nothing landed; branch untouched.
- **Incident (the lead's):** a Python edit opened `90 System/for-david.md` for writing before reading it and truncated the file, wiping Cowork's uncommitted edits there (Q78 annotation, Q-cowork-1, Q-cowork-2). Restored from the lead's verbatim copy of 09:38 (Q-cowork-1's last words may differ); any later Cowork edit there is lost. Committed versions were never affected. Cowork asked to check. Every later edit in the run read before writing.
- **Not done:** project CLAUDE.md's Hosting row (24–32 GB, €800–1,500) is stale after D95; a CLAUDE.md edit asks David, so it is left for Cowork to queue.
- **Push:** runtime `ae934d5` pushed; the vault is pushed (non-force) after this close commit and checked for 0 ahead / 0 behind.

**Pick up at:** Q81 (T9 Friday or Monday, with David); Cowork's fixes to the model content, then re-review and David's content OK; the week of 12 Oct items (T0.7, client-vault scaffold).


---

## How to resume

1. Read `CLAUDE.md` (who, what, rules)
2. Read this file (state, decisions, last session)
3. Read `TASKS.md` (▶ Next action at the top)
4. Check `OPEN_QUESTIONS.md` for anything now answerable

Then work. Before you stop, update all three.
