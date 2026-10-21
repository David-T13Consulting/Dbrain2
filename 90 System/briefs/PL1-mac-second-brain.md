---
classification: internal
task: PL1
owner: "@code"
status: open
models: []
created: 2026-10-21
---
# PL1 · Stage 1: a second brain on the Mac (20 Oct–1 Nov, hard stop)

## Goal (one sentence)
From the iPhone over Tailscale, by voice, David asks and hears a cited answer, and remembers, approves, recalls and corrects a fact, with nothing leaving the Mac (level L0).

## Files in scope (agent may touch only these)
- Runtime: the query service and phone service (`dbrain/`, `mvp/`), a frozen dev-case evidence file and the config that points to it (Q136), the T9b runner and artifacts (as in the T9b brief), the capture and writer modules P3.0 Part 1 and P3.1–P3.3 need, their tests, README.
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
3. **Pick the Mac's model (T9b step 4, with David, about 1 h; Q119 approved).** Run as the T9b brief says. TwIL-LM3-Pro may serve David's personal use only; its licence keeps it out of any client demo (D99). Outcome to David; he chooses the default.
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

## Outcome
