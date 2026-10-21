---
classification: internal
review_status: codex-reviewed
---
# Progress Tracker — AI Second Brain Project

**Last updated:** 21 Oct 2026 · **Updated by:** Claude Code (session 53: D141/D142 handoffs, T9b done, M6b closed; PV1 step 4 and PL1 step 5 parked)

---

## Current state

| | |
|---|---|
| **Phase** | **Three stages since 21 Oct (D141)**, inside the 19 Oct pivot (D134–D140): stage 1 second brain on the Mac (20 Oct–1 Nov, hard stop), stage 2 with Claude Code (2–8 Nov), stage 3 hosted EU with the router (9 Nov–6 Dec). Kept from before: P2.2 query service, P2.8 phone screen, P2.5 F0–F3, P2.7 failure capture, AS1 commit gates |
| **Schedule** | [[10 Projects/AI Second Brain/04_Roadmap\|04_Roadmap]] §4: stages 1–3, then operate and demo 7–13 Dec; demo-ready Fri 18 Dec 2026 (Q29) |
| **Target** | Client-ready demo, December 2026 |
| **Status** | 🟢 Week 0 closed · Week 1 closed · Week 2: 3 skills drafted and smoke-tested · Week 3: golden dataset **70/150** runs labelled. Batch 04 held out and scored 2 Oct — terrain 100% (≥95% ✅), intent 65% (≥85% ❌); the flags have no D19 threshold, and against the always-"no" baseline of 85% `tempo_block` at 40% is far worse while vertical at 90% barely beats it. The evidence behind the v2 taxonomy (D67) |
| **Dependencies** | No hardware (D134). Stage 1: David for T9c step 1 (candidates, disk budget, window; Q141) and the PL1 step 8 phone check. Stage 3: Scaleway key (Q134) and Claude API key |
| **Next action** | **"Pick up the loop" → [[90 System/briefs/PL1-mac-second-brain\|PL1]]: D74 consults first on the two parked steps** (PV1 step 4 URL override; PL1 step 5 restore test, five blockers), then fresh reviews; then PL1 step 4 (voice in the Shortcut); steps 6–7 after step 5 passes and their file list is reviewed. T9c after David's step 1 answer. Uncommitted on purpose in the runtime: `dbrain/provider.py`, `tests/test_provider.py`, the README "Rented providers" hunk, `experiments/restore_test.py`, `tests/test_restore_test.py` |
| **Action for David** | **T9c step 1:** pick at most two larger local models, the disk budget (17 of 25 GB used after Q143) and a window; PL1 step 8 (G2 by voice, P2.8 check); Scaleway key before 9 Nov (Q134); **backups:** nothing outside git has an independent copy (models, logs, failure store; Time Machine has no destination), found by the T4.2 drill. Nothing open in [[90 System/for-david\|for-david]] |

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

### Session 53 — 21 Oct 2026 · Claude Code, lead loop (D141/D142 handoffs; T9b done, C2 stays; M6b closed; two steps parked)
**Authorization:** "pick up the loop" from David, 21 Oct; no ⛔ block in the handoff. David present; answered Q138–Q143 in session. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only). No subagents. On AC power: `caffeinate -ims` for the loop (D103), T9b under `caffeinate -dimsu`.
- **Handoffs:** Cowork's ~13:45 entry (three stages, D141) `f4bcdda` + bookkeeping `fb1f6c5`; ~14:15 entry (agent topology option A) `7989553`, numbered **D142**; Q-cowork-21a–c kept their IDs.
- **Tier 1a batch 2026-10-19, review 2/2:** FAIL, one blocker (PL1 steps 6–7 had no file list); fixed forward `2daf21b` with the should-fixes; D135/D140's "rented models outclass local" wording left (DECISIONS is append-only; the roadmap marks it `unverified`).
- **PL1 step 1 (= PV1 step 4): PARKED.** Reviews 1/2 and 2/2 failed on the test-only URL override (`[::1%30]` decoded to `::10`; `@127.0.0.1`), both a parser differential; the root-cause fix (ask urllib and http.client which host they would use) is applied **uncommitted, unreviewed**.
- **PL1 step 2: done** (runtime `a9b8746`). Q138: the dev cases read the three files byte for byte as C2 read them (vault `8990bbe`, corpus `878a08ea6f57` reproduced); review 1/1 PASS; suite 564 OK.
- **PL1 step 3 = T9b step 4–6: done** (`5f4e009`). All seven blocks ok; TwIL fails the safety gate in both configurations (6/8 vs C2's 5/8); Codex blind judge stricter and right on two answers. **Q141:** C2 stays; T9c brief for larger models (blocked on David). Phone service stopped for the window and restarted.
- **PL1 step 5 (T4.2): PARKED.** Review 1/1 FAIL, five blockers (symlink overwrite path, `--out` guard, rewound remote, dirty files omitted, remote into the repo). Real drills ran ok but do not count. Steps 6–8 not started.
- **M6b S5: done, M6b closed** (`eaf3e4c`): no measured benefit, lexical stays; review 1/2 PASS; approved Q142; embedding models and venv deleted on Q143.
- **Settings:** `.claude/settings.json` committed on Q140 (`70ea3b3`).
- **Not done, for later:** the protected edits approved by Q-cowork-21a–c (data policy, PV1 ceiling rule, D56 note; TASKS stage 3); project `CLAUDE.md` still says W1–W8 and "L0 own rented GPU" (protected; needs David's word); runtime README's "never pushed" line is out of date.

**Pick up at:** D74 consults on PV1 step 4 and PL1 step 5, then PL1 step 4.

### Cowork — 21 Oct 2026 · agent topology (option A)
- David proposed an organiser agent with sub-agents per confidentiality level and many role agents. Cowork checked it against current research (Anthropic 2026, Google/MIT scaling study, CaMeL) and the existing router; David chose **option A: router + one runtime agent + skills**, with a quarantined reader for untrusted input and Codex as the separate reviewer. Decision number for the lead to assign.
- David defined the critical tier: health, financial and transatlantic-move discussions; no online model, but not the weakest local one; email and calendar stay on the current plan.
- Answered 14:15: 21c quality-first model pick for T9b step 4; 21a Strava/training data is not critical; 21b critical material stays out of the vault until wave 2. Record: [[10 Projects/AI Second Brain/02_Architecture/agent-topology-proposal-2026-10-21|agent-topology proposal]]. No runtime or stage 1 scope change.

### Cowork — 21 Oct 2026 · three stages, small wins (D141)
**David present.** He asked whether the Mac Air version could move first, then set the sequence: (1) a second brain on the Mac, with voice and vault updates from the phone over Tailscale; (2) a second brain with Claude Code working in the vault; (3) the hosted GDPR/EU second brain. Cowork's condition, accepted: three levels of one system, same vault, query service and evaluation set. **Recorded as D141**, with L0 redefined as the own machine (Mac Air). **Answers:** Q136 (a) frozen copy of the pre-pivot section 0; Q137 (a) Scaleway approved, after David asked why Mistral and not Gemma or Qwen (the question was about the host; Scaleway hosts all three; Gemma 4 26B-A4B added to the measurement); Q119 approved again so T9b step 4 runs in stage 1; stage 1 two weeks, hard stop 1 Nov.

**Done:** roadmap §2–§5 rewritten in three stages; TASKS regrouped by stage; new brief [[90 System/briefs/PL1-mac-second-brain|PL1]]; PV1 brief re-sequenced; session 52's should-fixes for Cowork applied: the demo (classification at L0 when the ceiling is L0, no looser override after withholding, L0 = Mac, Dutch removed; artifact republished), "CLOUD Act: None" for L1 marked `unverified`, rented-model superiority marked `unverified`, Dutch out of scope per D121, archive banners no longer say "verbatim" (git `e7b558e` is authoritative). **Not touched:** runtime, protected files.

**Pick up at:** "pick up the loop" → handoff, Tier 1a review 2/2, PL1.

### Session 52 — 19 Oct 2026 · Claude Code, lead loop (pivot committed; PV1 steps 1–2)
**Authorization:** "pick up the loop" from David, 19 Oct; no ⛔ block in the handoff; Cowork's 19 Oct ~20:30 pivot entry worked first. David present; he closed the session for the night mid-step 4. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only): PV1 step 1 review 1/2, one D129 design consult, the Tier 1a batch. No subagents. On battery: no caffeinate (D103).

**Done:** Cowork's pivot committed as two commits (`8356d89` decisions, answers and archive; `3d4b608` roadmap, TASKS, PV1 brief, proposal, demo), D134–D140 kept as numbered. **PV1 step 1** (Tier 2): D137 review budget in AGENTS.md and the brief template, D135 lines in the project CLAUDE.md; Codex 1/2 PASS, David approved the diff (Q132), `8220e1a`; stray `.githooks/__pycache__/` deleted (Q133). **PV1 step 2** (Tier 1a): [[30 Resources/AI Vendors/scaleway]], go for `internal` on Scaleway (no training, zero retention by default, incident retention up to two weeks, Paris); Mistral direct only after its API training toggle is off; `de85fe8`. Answers Q134 (key later this week) and Q135 (cap €50).

**In progress:** PV1 step 4, provider adapter: `dbrain/provider.py` and `tests/test_provider.py` uncommitted in the runtime, 25 tests pass, not reviewed (0/2). **Found:** the roadmap rewrite removed section 0, which the dev-case corpus reads: two runtime read-only tests fail and the C2 baseline cannot be reproduced (Q136); the archived roadmap and PROGRESS copies come from Cowork's ~15:40 working copy, not HEAD. **Not done:** PROGRESS oldest-session archiving (four sessions remain listed). **Left for David:** `.claude/settings.json` carries an uncommitted harness edit from tonight's web-fetch permission approvals (five WebSearch/WebFetch allows added; the deny list and `model` key only moved): keep or revert, his call (protected file).

**Tier 1a batch 2026-10-19 (session 52):** Review 1/2 **FAIL**, one blocker: PV1 step 2 raised to Tier 2 (its go/no-go is a domain conclusion); fixed forward (assessment marked proposed, **Q137** for David's approval); review 2/2 not taken, as David closed the session, so the fix is unreviewed. **Unfixed should-fix, for Cowork (owner of these texts):** (1) the demo classifies at L1 even when the ceiling is L0 and offers a looser override after withholding, against D138; (2) "CLOUD Act exposure: None" for L0/L1 in the roadmap and proposal needs a source or `unverified` (Mistral's privacy policy §7 allows some non-EU service providers); (3) the archive copies (roadmap, TASKS, PROGRESS) are not verbatim pre-pivot, correct the "verbatim" wording; (4) the proposal and demo list Dutch, against D121; (5) D135/D140's "rented models outclass the local ones" is an expectation until PV1 step 5: label it `unverified`. Fixed: the Mistral feedback-training citation, and for-david's "Nothing is open".

**Pick up at:** Tier 1a batch review 2/2 on the fix, then PV1 step 4 (README, Review 1/2, commit), then step 6; Q136 and Q137 before step 5.

### Cowork — 19 Oct 2026 · research, sovereignty router, pivot (D134–D140)
**David present** (afternoon and evening). **Research:** reusable building blocks on GitHub, Reddit-cited sources and vendor pages; result in the [[10 Projects/AI Second Brain/02_Architecture/sovereignty-router-proposal-2026-10-19|sovereignty router proposal]] and the demo `05_App_Prototype/sovereignty-router-demo.html` (simulated data; also a private Claude artifact).

**David's decisions:** no hardware, rent compute (Q121 → D134); pivot now with option A, EU APIs by default (Q127 → D135); Open WebUI + Open Relay (Q128 → D136); 1 review per step, 2 for security (Q129 → D137); automatic routing, stricter-only override, soft cap (Q130 → D138); client tier at L1 or stricter until G3 and the lawyer review (Q131 → D139); T9b parked for an offline level, M6b closes with its note (Q119 replaced → D140). D-numbers assigned by Cowork at David's request; the lead may renumber.

**Six-week honesty check (Q120, rule 5):** since 7 Sep the system has shipped phone question-and-answer only, nothing client-facing. Capture continues; the pivot is the response.

**Done:** roadmap rewritten (§4 weekly plan W1–W8); TASKS rebuilt around the weeks; delivery plan S2–S6 superseded; pre-pivot roadmap, delivery plan, TASKS and PROGRESS archived verbatim in `40 Archive/AI Second Brain/`; PV1 brief written. **Correction:** no data-policy change is needed (§1 and §5 already allow `internal` to a provider once its terms are verified); the earlier proposal text said D46 had to change, which was wrong. **Not touched:** data policy, AGENTS.md and project CLAUDE.md (protected; PV1 step 1 edits them with David's approval cited), runtime.

**Pick up at:** "pick up the loop" → PV1.

### Session 51 — 19 Oct 2026 · Claude Code, lead loop (WIP clean-up; AS1 step 3 committed, gates installed)
**Authorization:** "pick up the loop to finalize what's WIP. let's not start anything new but make sure we're cleaning up everything that's needed" from David, 19 Oct; no ⛔ block in the handoff. David present: he answered Q122–Q126 in session. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only): one D74 consult, AS1 step 3 review 1/5, the Tier 1a batch. No subagents (D114).

**What changed for David:** commits and pushes in both repos now pass through gates: a secret in staged content, a commit message or a pushed commit is refused; a vault note without a valid `classification:` is refused; a change to AGENTS.md, any CLAUDE.md, the data policy, `.claude/`, `.gitignore`, sandbox profiles, the secret scanner or the gates themselves needs a `David-approved:` trailer naming a recorded decision or answer; merges are refused; a push may only update master/main (no new branches or tags on GitHub). The old P2.8 worktree, stash and settings edit are gone.

- **Cowork's 19 Oct entry (weekly course map):** committed as `bf8ec65` (Tier 0); its lint notes worked under Q123.
- **Clean-up (Q122):** worktree `~/Work/dbrain-runtime-p28`, branch `p28-b1` (at `88103ab`) and the B1 stash removed; the vault's `.claude/settings.json` restored to its committed version.
- **Lint drift (Q123, `1676560`):** PROGRESS Phase and Action for David, TASKS host-order and T9b lines, ticked T9/M6 lines removed, T9 brief `done`, OQ-15 pointer to D107, for-david's "Since you last looked", 14 notes added to `index.md` (the eurouter capture sits in `40 Archive/Inbox/`, which the index does not list one by one), Welcome.md's placeholder link. Not touched: the five stale Inbox items, the digest skill, D63 and D-cowork-8 `in-review`.
- **AS1 step 3 (Q124, Q126):** D74 consult (Codex): drop the destination listing; the stdin remote value is authoritative; git packs tips of updates it rejects itself without passing them to the hook; replacement objects hide content. All taken: no lookup of the destination, new remote refs refused, unknown remote value refused, every local branch and tag counted, `GIT_NO_REPLACE_OBJECTS`, shallow and grafts refused. 50 gate tests (three fail on the previous gate), runtime suite 537 OK, scan clean. Review 1/5 PASS. Committed in the vault (`409a06b` record, `b039c63` gates) and the runtime (`c664ce4`), both with `David-approved: Q126`; `gates.py install` run in both (check passes); this run's pushes went through the gates.
- **Not touched:** the `weekly-desktop-digest` folder (Cowork's); the runtime's M6b `manifest-draft.json` (kept on purpose); T9b step 4 and the P2.8 phone check (Q125).

**Pick up at:** with David: P2.8 phone check, Q119 and T9b step 4. Then AS1 steps 4–5, G1-inj S1, M6b S5.

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

## How to resume

1. Read `CLAUDE.md` (who, what, rules)
2. Read this file (state, decisions, last session)
3. Read `TASKS.md` (▶ Next action at the top)
4. Check `OPEN_QUESTIONS.md` for anything now answerable

Then work. Before you stop, update all three.
