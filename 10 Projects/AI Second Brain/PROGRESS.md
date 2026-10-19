---
classification: internal
review_status: codex-reviewed
---
# Progress Tracker — AI Second Brain Project

**Last updated:** 15 Oct 2026 · **Updated by:** Claude Code (session 50: P2.8 B1 and B2 committed and live; T9b steps 1–3 done)

---

## Current state

| | |
|---|---|
| **Phase** | S1 requirements settled; S1 exit evidence incomplete (P1.3 data-flow diagram, roots/tools list); S2 under way: P2.2 query service committed (`4b5e91f`, runtime `c8b3b7b`); MVP-phone committed (P2.4, runtime `53e5740`); repos moved off iCloud to `~/Work` (M2, done 6 Oct); clean-up done, hold lifted (D81); P2.7 failure capture and the Wrong button live (13 Oct); P2.5 F0–F3 done (15 Oct); P2.8 live (15 Oct, phone check open); T9b step 4, AS1 steps 3–5, G1-inj S1, M6b S5, P2.1, P2.3 and P2.6 open; S2 exit proposed Fri 23 Oct. Running validation in parallel |
| **Schedule** | Original 13-week ordering superseded by S1–S6. Dated S2–S6 plan exists, proposed (`f9c014e`); demo-ready Fri 18 Dec 2026 (Q29) |
| **Target** | Client-ready demo, December 2026 |
| **Status** | 🟢 Week 0 closed · Week 1 closed · Week 2: 3 skills drafted and smoke-tested · Week 3: golden dataset **70/150** runs labelled. Batch 04 held out and scored 2 Oct — terrain 100% (≥95% ✅), intent 65% (≥85% ❌); the flags have no D19 threshold, and against the always-"no" baseline of 85% `tempo_block` at 40% is far worse while vertical at 90% barely beats it. The evidence behind the v2 taxonomy (D67) |
| **Dependencies** | Devices, availability, capacity, service targets and provenance schema all settled 1 Oct (D52–D59). Remaining dependency is the always-on host purchase (D53) — the Air cannot satisfy the availability requirement. Two local candidates and initial retrieval benchmarked, not accepted. Running labels continue independently |
| **Next action** | **With David:** the P2.8 phone check ("is there climbing class on november 2?" from "Ask Brain 5"), his window for **T9b step 4** (about 45–75 min, at most about 3.5 h), his word on removing worktree `~/Work/dbrain-runtime-p28` and the old B1 stash, and keep-or-revert of the harness edit in the vault's `.claude/settings.json`. **Then:** **AS1 step 3** (parked; D74 consult on the push-destination blocker; a draft consult proposing to drop the destination listing and refuse new remote refs is in the session 50 entry), steps 4–5; **G1-inj S1** (design check taken; build a closed-grammar scorer). **Session 50 (15 Oct, David present):** Cowork's T9b brief committed; **T9b** steps 1–3 (Q115; pin moved, Q116; file verified; loads on b11146; runner `c573ff2`, dry check OK); **P2.8 B1** committed after 5 reviews, Tier 2 (Q117 residuals, Q118 approval; runtime `6e51e4b`) and **B2** (`88103ab`); phone service restarted on it; P2.5 F0–F3 reported to David. **Session 49 (14–15 Oct, David present):** **P2.8 A1 and A2 committed** (runtime `5392cd1`, `2dd4d45`) and **live**: the phone's profile leaves out the system's working notes, the 14 Oct climbing question cites the climbing note; **B1 parked** after 2/2 reviews (stash); Tailscale had stopped (Q111). **P2.5 F2 committed** (`9ef5989`) after a D74 consult; **F3 committed** (`e17da04`, aliases; French "chorale" case now answers; no score gained). **Scouts note** was invisible to the phone since 9 Oct (backslash escapes in frontmatter), fixed (Q113, `b65a927`). **AS1 step 3 parked again** after 5/5 reviews (closed frontmatter grammar now fuzz-clean against PyYAML; open: git URL rewriting in the push re-check). Answers Q108–Q113. **Session 48 (13–14 Oct, David present):** **P2.5 F2 parked a fourth time** after reviews 1–2 and two one-off reviews (Q104 widened Q103 to wording that shifts a day or year; Q105 corrected the lead's over-broad contract wording); its last fixes are unreviewed in worktree `~/Work/dbrain-runtime-f2`; next run: D74 consult, one review under the Q105 contract, commit; then F3. **AS1 step 1 committed** (`235361f`: one current rulebook across ten files, scope widened by Q106, text approved word for word); **step 2 committed** (`8660c18`: AGENTS.md hard rule 7, data not instructions, **D132**); **step 3 (commit gates) parked** after 5/5 reviews (Q107: accidents + detection contract); gates built in both repos' `.githooks/` with 37 tests, uncommitted and not installed; steps 4–5 wait. One-time scan of the vault's 194 tracked files: no credential-shaped strings; all 180 notes pass the label rule. **Session 47 (13 Oct):** David's answers committed (`0d292ff`); **D130** scratch-folder deletes (`6c4a8c1`); **M6b S4 committed** (runtime `0736b29`, vault `b3e6054`), S5 next; **Q95 done**: the C2 phone re-check passed and the Wrong button works end to end (Shortcut "Ask Brain 5"); **P2.5 F2** narrowed per David and parked again after 2/2 reviews, uncommitted in worktree `~/Work/dbrain-runtime-f2` (next: D74 consult, one review under Q103, commit; then F3); Cowork's AS1 brief committed with **D131** (`03a811d`). **Session 46 (12 Oct):** D127/D128 committed (`479a229`); P2.5 F1 closed with no prompt change (Q99, `1e261cd`); **P2.5 F2 parked** after 2/2 reviews, its fixes uncommitted in the runtime working tree (next run: D74 consult first); **M6b S4 run done** (no measured benefit; lexical baseline stays), uncommitted until **Q101**; G1-inj brief drafted (`e74c0e9`); Q101–Q102 queued; Q95 phone step still waits for David (Q100). From the step after the D127/D128 commit on (David, 12 Oct), the lead works under D127 (review budget 2 per step, 5 for Tier 2 and security-boundary steps; Tier 1a and recorded answers batched once per run, push even if the batch fails with the unfixed items listed here; standing approvals; asks David directly when he is present) and D128 (one lead with up to 3 writing helpers in worktrees). **Session 45 (9 Oct):** handoff 15:06–15:12 committed (D123 §7a 1-hour window, D124 M6b labels, D125 ask with options, D121 line in AGENTS.md); P2.7 C5 service part committed (runtime `b3e1f1a`), phone part on **Q95**; M6b S3 committed (runtime `98694a2`), S4 on **Q96** (Pillow); P2.5 F0 passed review 4/5, uncommitted until **Q97**. Cowork's 15:35 roadmap entry not yet worked. **Session 44 (9 Oct):** the phone's wrong "no" became P2.5 slice F0–F3 (D120): F0 (13 synthetic regression cases, a scorer, a baseline) **parked after 5 reviews**, uncommitted; F1–F3 next run. P2.7 C5 ("Wrong" button) blocked on **Q93** (§7a). M6b: S1 (Python 3.12 venv, D122) and S2 (models verified) done; S3 blocked on **Q94**. English and French only (D121). Earlier history: [[10 Projects/AI Second Brain/PROGRESS-archive\|PROGRESS-archive]] |
| **Action for David** | Open items are in [[10 Projects/AI Second Brain/TASKS\|TASKS]] (`@david`): confirm the host order, due Fri 16 Oct (Mac mini M5 Pro 64 GB / 1 TB via the SRL, D107; **Q121**); weekly-review task ID (D60). Questions go through [[90 System/for-david\|for-david]]: **Q119** (T9b runner as Tier 2), **Q120** (six-week honesty check), **Q121** (host order) open after session 51. Optional: delete the test Shortcuts "Ask Brain 2", "3" and "4" (no token in them); "Ask Brain 5" has the Wrong button, the original "Ask Brain" still works. |

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

### Session 50 — 15 Oct 2026 · Claude Code, lead loop (T9b steps 1–3; P2.8 B1 and B2 committed and live)
**Authorization:** "pick up the loop" from David, 15 Oct, no ⛔ block in the handoff. David present: he answered Q115–Q118 in session. **Ended by** David ("let's stop for today, wrap up") before the phone check. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only): P2.8 two D74 consults and 7 reviews, G1-inj one D129 design check, the Tier 1a batch. No subagents (D114). Codex hit its usage limit 14:27–14:41 (one review did not run); one call hung on stdin after moving to the background (no review; later calls close stdin).

**What changed for David:** the phone screen is now readable: the answer, then each source as its note's title with one line from it, a plain status line, and the time only when it is over 8 s; no file paths, pipes or codes. When the notes do not answer, it says "No clear answer. Closest in your notes:" and shows the closest lines, never a half-answer. TwIL-LM3-Pro is downloaded (the 9 Oct build he chose), checked and ready to measure beside today's model in a ~1–3.5 h window with him.

- **Cowork's T9b entry:** brief committed (`e2e9898`, Tier 1a).
- **T9b steps 1–3:** Q115 (a). The pin had moved: the publisher replaced the Q4_K_M file on 9 Oct (`144a3ccb`); David chose the new file (**Q116**). Disk 19.50 GB → 21.74 GB of 25. One file fetched and verified (size and SHA-256 equal to the manifest). Loads on b11146 under the no-network sandbox; thinking switches off for TW-B. Runner `experiments/t9b_compare.py` (runtime `c573ff2`, Tier 1a, 11 tests; T9's runner gained hooks with unchanged defaults); dry check OK for all three configurations. Vault `c95a84e`. The D108 tripwire refused one download command because curl's `--fail` put "fail" after "Application Support"; rerun with `-f`.
- **P2.8 B1:** D74 consult; built in worktree `~/Work/dbrain-runtime-p28` so the live service kept committed code. Review 1 **raised the tier to 2** (the title re-read skipped the label check: now used only if the bytes hash to what the query indexed) and found a quote cut hiding "CANCELLED" (no display cut now). Reviews 2–4 each found markdown structure shown as the line (header rows, tables without outer pipes, blockquote tables, comments); after review 4 a second D74 consult; David accepted the one-line residuals (**Q117**); containers, comments and definitions handled; **review 5/5 PASS**; David approved (**Q118**); runtime `6e51e4b`.
- **P2.8 B2:** withheld answers show no model sentence (Q110). Review 1 failed (the leading date came from model-writable text; now the service's own label); review 2/2 PASS; runtime `88103ab`. Phone service restarted on it; in-process check on the real notes good (the 14 Oct question cites the climbing note, 10.0 s shown). **Phone check with David not done.**
- **P2.5 F0–F3 reported to David** (session close message).
- **G1-inj S1:** D129 design check taken and recorded (closed whole-answer forms; canary absence alone is not a pass). Not started.
- **AS1 step 3:** not worked. Draft for its D74 consult (scratch, not sent): drop the destination listing; for an existing remote ref check `rev-list <local> ^<remote sha from stdin>`; refuse creating new remote refs (D50: push to master); ask what that misses (follow-tags, submodule recursion, protocol details).
- **Not touched:** `weekly-desktop-digest`, AS1's uncommitted `.githooks/` and `tests/test_gates.py`, the M6b draft manifest. **Uncommitted, not the lead's:** the vault's `.claude/settings.json` (harness edit from a permission approval at 14:20: one added `additionalDirectories` entry, keys reordered); left for David.
- **Keep-awake:** `caffeinate -ims` started at loop start, stopped at close.

**Pick up at:** with David: P2.8 phone check, T9b window, worktree and stash removal, settings edit; then AS1 step 3 (D74 consult first), G1-inj S1.

### Session 47 — 13 Oct 2026 · Claude Code, lead loop (Q95 with David; D130; M6b S4 committed; P2.5 F2 parked again; AS1/D131)
**Authorization:** "pick up the loop" from David, 13 Oct, with the order: Cowork's 13 Oct handoff, Q95 phone step first (David present), then Q101 (AGENTS.md line word for word) and the M6b S4 commit, then P2.5 F2 per D127 and F3. **Ended by** stop condition (1): F2 parked (F3 waits on it), M6b S5 is Tier 2 and comes after F2/F3 in David's order. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only): 5 reviews, one D74 consult, the Tier 1a batch. No subagents (D114).

**What changed for David:** the phone's "Wrong" button works (he tapped it; the service recorded it), and the phone answers on the new default model (C2) were good; the lead may now delete its own scratch files without asking (D130); the embedding test is on record (no gain over plain keyword search); the code check for the wrong "no" is narrower and never hides an answer, but is not live yet; the AS1 hardening brief is queued for this week.

- **Q95:** the service had been down since a reboot (Tailscale off on the Air; David reconnected it); F2's unreviewed edits were stashed first so the restarted service runs committed code only (`d584f13`). Hand-edit steps were too tedious for David; the lead built token-free Shortcuts from the Mac (`shortcuts sign`): "Ask Brain 2"–"4" failed (a variable-carried token never reached the header; then the menu-item format), "Ask Brain 5" works once David pasted the Keychain token into its two headers. C2 re-check: three good answers. End to end: `POST /wrong wrong-recorded` 14:47:09. David's standing preference (13 Oct): never ask him to edit Shortcuts by hand.
- **Q101 / D130:** AGENTS.md standing approval (5) and the hard-limits exception, text approved word for word by David; Codex 1/5 pass; `6c4a8c1`.
- **M6b S4:** review 2/2 pass (review 1's only blocker ratified); runtime `0736b29`, vault `b3e6054`.
- **P2.5 F2:** D74 consult (Codex: the free-text design will not converge; narrow it); David chose "narrow + keep the answer"; rebuilt; reviews 1/2 and 2/2 fail, each on two more ways a note marks an event off; **parked** (D127), fixes uncommitted in worktree `~/Work/dbrain-runtime-f2` (branch `p25-f2`); David's **Q103**: such markers are should-fixes from now on. F3 not started.
- **AS1:** Cowork's 11:20 entry committed with **D131** (Q54 reaffirmed, protected-file commit gate, AS1 scope) as `03a811d`.
- **Not touched:** the `weekly-desktop-digest` folder; the old `manifest-draft.json` in the runtime.

**Pick up at:** P2.5 F2 (D74 consult, one review under Q103, commit, then F3); M6b S5 (results note, Tier 2); AS1 this week.

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

## How to resume

1. Read `CLAUDE.md` (who, what, rules)
2. Read this file (state, decisions, last session)
3. Read `TASKS.md` (▶ Next action at the top)
4. Check `OPEN_QUESTIONS.md` for anything now answerable

Then work. Before you stop, update all three.
