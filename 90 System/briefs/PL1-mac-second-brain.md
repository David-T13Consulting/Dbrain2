---
classification: internal
task: PL1
owner: "@code"
status: in-review
models: []
created: 2026-10-21
---
# PL1 · Stage 1: a second brain on the Mac (20 Oct–1 Nov, hard stop)

## Goal (one sentence)
From the iPhone over Tailscale, by voice, David asks and hears a cited answer, and remembers, approves, recalls and corrects a fact, with nothing leaving the Mac (level L0).

## Files in scope (agent may touch only these)
- Runtime: the query service and phone service (`dbrain/`, `mvp/`), a frozen dev-case evidence file and the config that points to it (Q136), the T9b runner and artifacts (as in the T9b brief), the restore-test script and its tests (step 5), README.
- **Steps 6–7 (writes) have no file scope yet.** Before either starts, the lead lists here every file it may change (writer and capture modules, tests, Shortcut recipe, bookkeeping) and Codex reviews that list, as [[90 System/briefs/P3.0-update-my-brain|P3.0]] › Files in scope requires. Until then no file may be changed for steps 6–7 (Tier 1a batch review 2/2 of 21 Oct, blocker).
- Vault: this brief, [[90 System/briefs/P3.0-update-my-brain|P3.0]], [[90 System/briefs/T9b-twil-lm3-pro-trial|T9b]], [[90 System/briefs/PV1-rented-models-and-switchboard|PV1]] (step 4 record only), PROGRESS, TASKS, for-david, handoff, log, index, a results note in `02_Architecture/`.
- iPhone Shortcuts: built and edited by the lead, never by David by hand (his preference, 13 Oct).

## Inputs / context to read first
- [[10 Projects/AI Second Brain/04_Roadmap|04_Roadmap]] §2–§4 (three stages, D141); DECISIONS D134–D141.
- P3.0 brief (write path, Q67: read back and save only on "save"); data policy §7 (scoped writer only after T4.2), §7a, §4a (admission waves).
- T9b brief (protocol, Q115–Q116; Q119 approved 21 Oct).
- P2.8 brief (phone answer screen).

## Steps (D137: 1 review per step; 2 for Tier 2 and security-boundary steps)
1. **Finish PV1 step 4** (provider adapter, already in progress, uncommitted): README section, review, commit. It stays unused until stage 3.
2. **Freeze the dev-case evidence (Q136 (a)).** Copy the pre-pivot roadmap section 0 from git `e7b558e` into a fixed evidence file outside the live roadmap; point the dev-case corpus at it; the two failing read-only tests pass again and the C2 baseline reproduces.
3. **Pick the Mac's model (T9b step 4, with David, about 1 h; Q119 approved).** Run as the T9b brief says. TwIL-LM3-Pro's licence question stays open (D99): a private research trial is unaffected; whether it may appear in the December demo is unresolved until webAI confirms in writing or a lawyer reads the licence. Outcome to David; he chooses the default.
4. **Voice on the phone.** The Shortcut takes iPhone dictation in and speaks the answer out (on-device speech, no server ASR); a short spoken form of the answer with the sources' titles; the screen keeps the P2.8 layout. Away-from-home check over Tailscale.
5. **Restore test first (T4.2).** Rollback of a bad commit and restore after loss of the working copy, on a disposable copy; required by data policy §7 before any runtime write.
6. **Remember from the phone (P3.0 Part 1, security boundary).** "Remember …" → the Shortcut reads the note back → saved only on "save" (Q67), as one new dated file in `00 Inbox/` with classification and the four D69 axes (asks "personal or work?"), via one writer; no other write path; admission per data policy §4a.
7. **Correct from the phone (P3.1–P3.3 minimal, security boundary).** "That's wrong: …" → a proposed exact change to that note, bound to its base revision, read back, applied only on "save"; a stale approval is refused; the old version does not resurface in answers.
8. **G2 check with David.** From the phone, by voice: remember a benign fact, recall it in a fresh session with its source, correct it, recall again; plus a rejection, a concurrent Obsidian edit and an interrupted save. P2.8 phone check in the same session.

## Done when (checkable)
- Steps 1–7 committed; step 8 passed with David and recorded in PROGRESS.
- Nothing leaves the Mac: no provider call in stage 1 (the adapter of step 1 is not wired in).
- Hard stop Sun 1 Nov: unfinished steps move to stage 3 and are listed in PROGRESS.

## Constraints (vault rules that especially apply)
- Red line and data policy unchanged; family logistics only within the current waves; no client data.
- One writer; exact-change approval; read-back before save; no silent writes.
- English and French only (D121).

## Review
- **Step 1 (= PV1 step 4, security boundary): PARKED 21 Oct** after reviews 1/2 and 2/2 failed (two host-parsing blockers in the test-only URL override); record in the PV1 brief. Not blocking stage 1: the adapter is wired into nothing.
- **Step 2 (Tier 1b).** Q138 (David, 21 Oct) refined Q136: the dev cases read the three corpus files byte for byte as the C2 baseline read them (vault `8990bbe`), not section 0 of `e7b558e`. Runtime: `evidence/devcase-corpus-8990bbe/` (three copied files, sha256 equal to C2's record), `Profile.vault`, `DEFAULT` and `DEVCASES` read it, `index.build` uses the profile's vault when the caller names none; a test pins corpus version `878a08ea6f57` and the three hashes. The two failing read-only tests pass again. Same corpus as T9 (`878a08ea6f57`), so T9b's C2 blocks compare like for like with T9.
  - Review 1/1 · PL1 step 2 — Codex `gpt-6.1-sol` (review profile, high, read-only): **PASS**. Should-fix applied: `serve.py`'s title reread uses the same effective root as `index.build`. Suite 564 OK. Committed runtime `a9b8746` (`David-approved: Q138`, as the gate treats the copied AGENTS.md and data policy as protected).
- **Step 3 (T9b step 4, with David): done 21 Oct.** C2 stays the Mac's default; TwIL fails the safety gate in both configurations (6/8 correct vs C2's 5/8). David, **Q141**: keep C2, measure one or two larger models that fit 24 GiB next (T9c brief). Record in the T9b brief and [[10 Projects/AI Second Brain/02_Architecture/t9b-twil-lm3-pro-2026-10-21|results note]].
- **Step 5 (T4.2 restore test, Tier 1b: runs on the real repositories, read-only).** `experiments/restore_test.py` and `tests/test_restore_test.py` (7 synthetic tests). Two drills on disposable copies in a temporary folder: (1) a synthetic bad commit (one note overwritten, one deleted) reverted in a local clone, tree identical to the original; (2) the clone deleted, then restored by cloning the GitHub remote, the only off-machine copy (no Time Machine destination is configured), compared with the remote branch as last fetched, `git fsck --full`, clean checkout; unpushed local commits reported, not hidden. Real runs 21 Oct: vault and runtime both **ok** (vault 7 commits and runtime 1 not yet pushed at the time). **Not covered, not tested:** git-ignored and untracked files, models, logs and the failure store; whether any independent copy exists was not checked (Time Machine has no destination; for David). Runtime README's "never pushed" is out of date: the runtime has a GitHub `origin`.
  - Review 1/1 · PL1 step 5 — Codex `gpt-6.1-sol` (review profile, high, read-only): **FAIL**, five blockers: (1) a tracked `.md` symlink could redirect the synthetic overwrite into the original repository or vault; (2) `--out` is guarded only against the vault, so it could overwrite the tested runtime's files or `.git/config` (the real reports sit in its ignored `artifacts/`); (3) a rewound remote passes with the wrong checkout when the expected commit survives elsewhere in the clone; (4) dirty tracked files are silently omitted, so `ok` can be true while uncommitted edits would be lost; (5) a remote pointing into the original repository is accepted, so a pass need not show independent recovery. Should-fix: failure-path and cleanup-on-error tests; "no independent copy exists" is asserted, not checked (say "not tested").
  - **Step 5 PARKED (21 Oct, budget used).** Nothing committed; `experiments/restore_test.py` and `tests/test_restore_test.py` stay untracked in the runtime. The real runs' "ok" does **not** count as T4.2 passed. Steps 6–8 not started this run (park rule). **Next run:** D74 consult on step 5 first, then fix all five and a fresh review.

## Outcome
