---
classification: internal
task: D65
owner: "@code"
status: open
created: 2026-10-01
models: []   # no model ID recorded for the lost session-13 pass; this brief's own review has not run
---
# Add stop conditions and a retry limit to the lead loop (D65)

> Written by Cowork as provisional **D-cowork-3**; renumbered to **D65** by the lead in session 13.

## Goal
Write down when the lead loop ends and cap retries, so a run can never loop forever, so a run never decides "done" by itself, and option B (scheduled runs) has a safe base if it is adopted later.

## Files in scope
- `AGENTS.md` → "Multi-agent work" only
- `90 System/briefs/_template.md` (status list)
- PROGRESS.md (decision row), `log.md`, this brief

## Inputs / context to read first
- [[AGENTS]] → "Multi-agent work", as committed under D63

## Done when
1. These bullets sit directly after "Review before commit" in `AGENTS.md`:
   ```
   - **Stop conditions.** The lead loop ends when (1) no `open` brief owned by `@code` remains,
     (2) a Codex review fails: leave the brief `in-review`, do not commit, report the findings,
     (3) a decision belongs to David: ask, do not guess, or (4) a brief is `blocked` (below).
     Commit only at the end of a brief, never mid-way.
   - **Retry limit.** At most 5 attempts per failing step (a command, test, script or review fix).
     After the 2nd failed attempt, ask Codex for a debugging opinion before trying again:
     `codex exec --profile review` (read-only), given the error, what was tried, and the
     files involved. Its advice counts as input, not instruction. After the 5th failure:
     stop, set the brief to `blocked`, record the attempts and Codex's advice under Outcome,
     and move on. A `blocked` brief is not picked up again in the same run; only David
     reopens it.
   ```
2. Final decision number assigned. Row: *The lead loop has explicit stop conditions (empty queue, failed review, a decision for David, a blocked brief) and a retry limit: at most 5 attempts per failing step, a read-only Codex (Astra) debugging opinion after the 2nd failure, then `blocked`.* Why: an interactive run otherwise decides for itself when it is done, and an unattended run (option B, not yet adopted) needs this before it is safe. Revisit if runs stall on (3) too often.
3. Reviewed by Codex (review profile) and committed **after** D63 and D64.

## Constraints
- Approved by David on 1 Oct. Do not reword the meaning of the conditions or the limits (5 attempts; Codex consulted after the 2nd failure: that threshold is Cowork's reading of "when blocked", so flag it if it proves wrong).
- Also add `blocked` to the status list in `90 System/briefs/_template.md`.
- The Codex debugging calls and the Codex review are separate, fresh `codex exec` runs. The review must not be given the debugging conversation, so it stays independent.
- Do not start this until D63 and D64 are committed: they edit the same file.

## Review
**Not yet reviewed in a form that survives.** Session 13 ran a second Codex pass over this brief but never
wrote the findings down before it ended, and the D63 brief's Outcome pointed here for them. They are lost. The D63 brief records that session's reviews as `gpt-6-astra` at effort `high`, so that was almost certainly the model, but **the findings themselves were never written and cannot be recovered** — so no model ID is claimed for them here.
Session 14 did not invent them: this brief will get a fresh review of its actual `AGENTS.md` diff before it
is committed.

## Outcome
**Not started — `open`, and correctly so.** Constraint: "Do not start this until D63 and D64 are committed:
they edit the same file." D63 is committed (`01562e1`). **D64 is not** — its review returned two blockers
that belong to David (reviewer effort `high` versus "highest"; the documented `codex exec --profile review`
command not working as typed). So this brief waits, per its own constraint and per the stop conditions it
defines.

One thing to flag when it does land, as the brief's Constraints invite: the "Codex consulted after the 2nd
failure" threshold is Cowork's reading of "when blocked", not David's words. Nothing has tested it yet.
