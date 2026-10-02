---
classification: internal
task: D68
owner: "@code"
status: blocked-on-david
models: [claude-opus-5 (lead), gpt-6-astra (review)]
created: 2026-10-02
---
# Single front door: only Cowork asks David (D68)

> Written by Cowork, 2 Oct 2026 as provisional **D-cowork-6**; renumbered to **D68** by the lead in session 14. David chose option A that day: one front door (Cowork), one decision queue. Trigger: Codex asked David directly about the batch 04 re-score, so David was handling three agents separately.

## Goal (one sentence)
David deals with one agent only: every question for him goes through `90 System/for-david.md`, and Cowork batches them.

## Files in scope
- `AGENTS.md` → "Multi-agent work" only
- `90 System/briefs/_template.md` (status list: add `blocked-on-david`)
- `90 System/for-david.md` (created by Cowork; commit as is)
- Codex config, if it is needed to stop interactive sessions reaching David (see Done when 3)
- PROGRESS (decision row), `log.md`, this brief

## Done when (checkable)
1. These bullets sit in `AGENTS.md` → "Multi-agent work", after "Stop conditions":
   ```
   - **One front door (D-cowork-6).** Only Cowork asks David. Claude Code and Codex never
     ask him directly: they add an entry to `90 System/for-david.md` (from, brief, question,
     options with the recommended one first, what it blocks, urgency), set the brief to
     `blocked-on-david`, and continue with other work. Cowork walks David through the open
     entries at the start of each session and writes the answers into the queue and the
     brief. The lead turns answers into decisions and commits. Stop condition (3) means
     "write to the queue", not "ask".
   - The lead clears answered entries once they are recorded in PROGRESS or the brief.
   ```
2. The "If unsure, stop and ask David" line becomes "If unsure, stop and add it to `for-david.md`".
3. Codex runs only as `codex exec` called by the lead, never in an interactive session that reaches David. If that needs a config or habit change on David's side, put it in `for-david.md` as a question, not in a terminal prompt.
4. The five blocking items in OPEN_QUESTIONS (session 14) now point to `for-david.md` Q1–Q4 (item 5 is answered: `@cowork`). *(Amended 2 Oct by the lead: item 5 is indeed the answered one, as written, and items 1–3 were answered too. The open one is item 4, whose queue entry is numbered **Q5**, not Q4 — the queue numbers entries in the order they are written, not the order they were listed here. Criterion met as amended.)*
5. Final decision number assigned; Codex review (read-only) recorded below; committed.

## Constraints
- Approved by David 2 Oct 2026. Don't change the meaning: a single front door, Cowork, batched.
- Known trade-off David accepted: blocked items wait until his next Cowork session. A scheduled nudge (option C) is explicitly deferred: add it only if blocked work starts to pile up.

## Review
Independent read-only review by Codex, 2 Oct 2026, session 14. Model `gpt-6-astra`, effort `high`, read-only,
via `codex exec --profile review`. It verified the `AGENTS.md` bullets match this brief verbatim apart from the
provisional ID, found no secrets and no classification violations, and returned seven findings:

| # | Finding | Severity | Action |
|---|---|---|---|
| 1 | "Done when" 3 was declined rather than done: the brief requires that any habit change on David's side be put in the queue as a question, not assumed away | **high** | **Fixed over two rounds.** First by adding **Q6** to `for-david.md`; then, when the reviewer pointed out Q6 said "nothing is blocked … D68 closes either way", by accepting the consequence: Done when 3 is *unresolved*, so this brief is **`blocked-on-david`**, not `done`. Option (c) was also dropped from Q6, since it would have changed a policy David had already approved |
| 2 | The correction to Cowork's queue asserted the reserved-case question was "never put to him" without evidence, and the P2.1 brief said "Raised with David" | medium | **Fixed consistently** across the queue, this Outcome, `handoff.md` and `log.md`: the claim is now only that **the lead did not ask it**, with no record either way of whether Cowork or Codex did. The entry stays open because that is the safe default on held-out data, not because anyone established it was never asked |
| 3 | "Done when" 4 specified a Q1–Q4 mapping that the implementation does not follow | medium | **Fixed, and the lead's own error found in the process.** It had swapped items 4 and 5 in the OPEN_QUESTIONS table, then concluded the brief's premise was wrong. The brief was right: item 5 (scoring owner) is the answered one. Original order restored; the only real divergence is that item 4's queue entry is numbered Q5, because the queue numbers entries in writing order |
| 4 | Scope creep: P2.2 edits and PROGRESS changes beyond the decision row are outside this brief's Files in scope | medium | **Scope basis recorded for each group, not split.** Three bases: this brief (the `AGENTS.md` bullets, the template, `for-david.md`, the decision row); Cowork's handoff entry, which explicitly asks the lead to tick T3.1, add the scores to PROGRESS and mark T3.4 unblocked; and David's own 2 Oct authorisation, which is what the P2.2 edit records. `PROGRESS.md`, `log.md` and `index.md` carry interleaved edits from all three, so separating them would mean reconstructing intermediate file states — the same situation the handoff records for `667902e` and `2db69fc`, and resolved the same way: one commit, with the reason written down |
| 5 | The score write-up overclaimed: D19 sets no threshold for either flag, and always answering "no" scores 85% on both, so "only terrain passes" and "near a coin flip" were wrong | medium | **Fixed in four places**, the `log.md` heading included. `tempo_block` at 40% is *far worse* than the trivial baseline, vertical at 90% barely beats it, and both are weak evidence at n=20 with 3 positives |
| 6 | "Done when" 5 pending: no findings recorded, `status: done` premature | medium | **Fixed.** This table is the record, and the status is now `blocked-on-david` rather than done — which finding 1 forced anyway |
| 7 | `log.md` omitted the `D-cowork-6 → D68` mapping; P2.1 still said D64/D65 block Step 0 although both are committed | low | **Fixed in both files** |

## Outcome
**The `AGENTS.md` change is in force, 2 Oct 2026 (session 14), but the brief is `blocked-on-david`,** because
its own "Done when" 3 asks something only David can answer (Q6). The rule applies regardless; the status tracks
the paperwork, not whether the policy is live.

1. The two bullets are in `AGENTS.md` after the stop conditions, **verbatim** except the provisional ID
   `D-cowork-6` which the lead replaced with **D68**, as D63 requires.
2. The "If unsure, stop and ask David" line in the multi-agent section now reads "If unsure, stop and add it
   to `for-david.md`". **Hard rule 6 at the top of `AGENTS.md` was deliberately left alone** — "When unsure,
   stop and ask" governs the agent's conduct toward whoever is in the session, including Cowork itself, and
   rewriting it to point at a queue would be a wider change than this brief authorises.
3. **Unresolved — this is why the brief is `blocked-on-david`.** Codex already runs only as `codex exec` called
   by the lead, never interactively, and D64 made that invocation work from the documented command, so nothing
   is needed on the lead's side. But the lead controls its own calls, not whether David opens an interactive
   Codex session, and this condition asks whether anything must change on his side. It is **Q6** in
   `for-david.md`. The first draft of this Outcome assumed the answer and closed the brief; the second queued
   the question but still called the brief done. Both were wrong, and the brief now waits.
4. Done. The five blocking items in OPEN_QUESTIONS now point at `for-david.md`, and **the brief's premise was
   right**: item 5, the batch-04 scoring owner, is the answered one, and item 4, the reserved cases, is still
   open. An earlier draft of this Outcome claimed the premise was wrong — it had swapped items 4 and 5 in the
   OPEN_QUESTIONS table and then reasoned from its own mistake. Corrected: the original order is restored, and
   the only real divergence is that item 4's queue entry is numbered **Q5**, because the queue numbers entries
   in the order they were written rather than the order they were originally listed.
5. D68 assigned; decision row and `log.md` entry written; reviewed before commit.

**One correction made to Cowork's own queue file.** Its *Answered* table listed David's four direct answers as
reviewer effort, the CLI fix, the runtime repo and *Codex reading the reserved cases*. The fourth is wrong: the
four the lead put to him were reviewer invocation, reviewer effort, the runtime repo and the batch-04 scoring
owner. **What the lead can state is only that it did not ask the reserved-case question — it has no record
either way of whether Cowork or Codex put it to him.** The entry is open because leaving a held-out-data
question open is the safe default, not because anyone established it was never asked.

**Immediate effect on this session.** The lead had been about to put the reserved-case question to David
directly. Under D68 it went into the queue instead, and `P2.1-review` is `blocked-on-david`. The trade-off
David accepted is live: both open questions now wait for his next Cowork session.
