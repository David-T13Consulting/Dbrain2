---
classification: internal
task: D-cowork-3
owner: "@code"
status: open
created: 2026-10-01
models: []
---
# Add stop conditions and a retry limit to the lead loop (D-cowork-3)

## Goal
Write down when the lead loop ends and cap retries, so a run can never loop forever, so a run never decides "done" by itself, and option B (scheduled runs) has a safe base if it is adopted later.

## Files in scope
- `AGENTS.md` → "Multi-agent work" only
- `90 System/briefs/_template.md` (status list)
- PROGRESS.md (decision row), `log.md`, this brief

## Inputs / context to read first
- `AGENTS.md` → "Multi-agent work", as committed under D-cowork-1

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
3. Reviewed by Codex (review profile) and committed **after** D-cowork-1 and D-cowork-2.

## Constraints
- Approved by David on 1 Oct. Do not reword the meaning of the conditions or the limits (5 attempts; Codex consulted after the 2nd failure: that threshold is Cowork's reading of "when blocked", so flag it if it proves wrong).
- Also add `blocked` to the status list in `90 System/briefs/_template.md`.
- The Codex debugging calls and the Codex review are separate, fresh `codex exec` runs. The review must not be given the debugging conversation, so it stays independent.
- Do not start this until D-cowork-1 and D-cowork-2 are committed: they edit the same file.

## Review

## Outcome
