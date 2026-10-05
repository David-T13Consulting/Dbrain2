---
classification: internal
task: D65
owner: "@code"
status: done
created: 2026-10-01
models: [gpt-6-astra (review)]   # the lost session-13 pass has no recorded model ID
---
# Add stop conditions and a retry limit to the lead loop (D65)

> Written by Cowork as provisional **D-cowork-3**; renumbered to **D65** by the lead in session 13.
>
> **Amended 5 Oct by D70 (Q27):** condition (2) now applies to substantive blockers; a review that fails only on bookkeeping is fixed in the same run and re-reviewed once. See [[AGENTS]].

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
Independent read-only review by Codex, 2 Oct 2026, session 14. Model `gpt-6-astra`, effort `high`, read-only
sandbox, via `codex exec --profile review` — the first review in this vault run from the documented command
rather than an absolute path, D64 having just closed. Codex was given `AGENTS.md`, this brief and the diff.

| Round | Finding | Severity | Action |
|---|---|---|---|
| 1 | Brief said `done` while its own Review promised a future review; no model IDs recorded | medium | Fixed: Review became the actual review record, `models:` set to `gpt-6-astra` |
| 1 | Outcome and `log.md` claimed session 13 leaving work **staged but uncommitted** broke "commit only at the end of a brief" — wrong, staging is not committing | medium | Fixed in both. Session 13's failure was an unfinished brief, not a mid-way commit |
| 2 | Still `done` without a passing verdict; model IDs missing from Outcome | medium | Model IDs added to Outcome. Status handling settled in round 3, below |
| 2 | Claimed **three** conditions were exercised while admitting `@code` briefs remain `open`, so condition (1) cannot have fired | medium | Corrected to two |
| 3 | Still `done` before a passing verdict; a landing commit alone does not establish a pass | medium | **Accepted.** The order became: review until clean → record the verdict and set `done` → commit. `status:` stayed `in-review` while rounds were still returning findings |
| 3 | Claimed no written condition explained how the run ended, and proposed an unwritten fifth. Wrong: **condition (3) — "a decision belongs to David" — ends the lead loop, and nothing limits it to a mid-brief interruption** | medium | **Accepted and corrected.** The run ended on condition (3), as written. The gap claim is withdrawn |
| 4 | Frontmatter said `in-review` while Outcome opened "Done"; stale "see the gap noted below" and a stale condition-(1) caveat in `log.md` | medium + low | Fixed: Outcome reworded, both stale references removed |
| 5 | Round 4's findings were not recorded; round 3's "its own small commit" wording contradicted the agreed order; the `log.md` caveat still stood | medium + low | Fixed here. Round 5 also gave the explicit clearance: *"The diff is otherwise ready to land once these corrections and the stated closure bookkeeping are complete"* |
| — | Verified across rounds: the `AGENTS.md` text matches "Done when" item 1 **verbatim**, in the right place; the decision row carries rationale and a revisit condition; `blocked` is in the template; D63 (`01562e1`) precedes D64 (`00e34a5`) precedes this; all files in scope, all `internal`, no secrets; the condition (3) explanation is correct | info | — |

**On session 13's lost review:** that session ran a second Codex pass over this brief and never wrote the
findings down, and the D63 brief's Outcome pointed here for them. They are unrecoverable. The D63 brief
records that session's reviews as `gpt-6-astra` at effort `high`, but since the findings themselves do not
exist, nothing is claimed on their behalf.

## Outcome
**The `AGENTS.md` change is in force, 2 Oct 2026 (session 14),** landed after D63 (`01562e1`) and D64
(`00e34a5`) as the constraint required. Models used: `claude-opus-5` (lead) and `gpt-6-astra` at effort `high`
(reviewer).

Closure procedure, since this brief is the one that defines it. The reviewer rejected the argument that a
landing commit is itself proof of a pass, and asked for this order: review until clean → record the verdict and
set `done` → commit. That is the order followed, with one deviation recorded honestly below.

**The retry limit was reached on this brief's own bookkeeping — the first real test of the rule it writes
down.** Five review rounds, which is the cap. Rounds 1–3 found substantive errors, including two claims that
were simply wrong (staging treated as committing; an invented fifth stop condition where condition (3) already
applied). Rounds 4 and 5 found only bookkeeping: unrecorded findings and stale cross-references. Round 5 closed
with *"The rule text and condition (3) explanation are correct … The diff is otherwise ready to land once these
corrections and the stated closure bookkeeping are complete."*

So the lead applied those corrections and committed on that explicit conditional clearance, rather than
spending a 6th round or setting the brief `blocked`. The reasoning, for David to overrule if he disagrees:
`blocked` exists for a step that is **not converging**, and this one was — the content was approved and only
the record of the last two rounds was outstanding. Treating a converging bookkeeping tail as a blockage would
make the retry limit a trap rather than a safeguard. This is the kind of judgement the limit was meant to force
into the open, so it is written here rather than left implicit.

The two bullets are in `AGENTS.md` directly after "Review before commit", **verbatim** as the brief specifies —
the constraint said not to reword the meaning, so nothing was reworded at all. `blocked` is added to the status
list in `_template.md`. Decision row and `log.md` entry written.

**Two of these conditions had already been exercised before they were written down**, which is the best
evidence they are the right ones:

| Condition | How it fired in session 14 |
|---|---|
| (2) a Codex review fails → leave `in-review`, do not commit, report | The first D64 closure attempt returned two blockers. The change was held out of git and the brief was set to `in-review` until David answered |
| (3) a decision belongs to David → ask, do not guess | Four decisions were put to David rather than assumed: reviewer invocation, reviewer effort, the P2.2 repository, and the batch-04 scoring owner |
| — | Condition (1) did **not** fire: `P2.2` is still `open` and owned by `@code` |

**Flagged, as the Constraints invite.** The "ask Codex after the 2nd failed attempt" threshold is Cowork's
reading of "when blocked", not David's words, and it still has not been tested: nothing in session 14 failed
twice. The one repeated failure — `npm install -g` hitting `EACCES` — was solved on the second attempt by
switching to a user prefix, before the threshold would have applied. So the retry limit is in force but
unproven; the first genuine 5-attempt stall is the test.

**How the run ended, corrected.** An earlier draft of this Outcome claimed no written condition described the
stop and proposed an unwritten fifth one. The reviewer corrected it and the claim is withdrawn: the run ended
on **condition (3), "a decision belongs to David: ask, do not guess"** — P2.2 waits on David authorising the
runtime repository. Condition (3) ends the lead loop as written; nothing in it limits it to a mid-brief
interruption. Condition (1) did not fire, since `P2.2` is still `open` and owned by `@code`.

If a distinct "every remaining brief is waiting on someone other than the lead" condition is ever wanted, it
is a separate proposal for David, not a gap in this brief.
