---
classification: internal
task: D-cowork-6 (provisional; the lead assigns the final ID)
owner: "@code"
status: open
models: []
created: 2026-10-02
---
# Single front door: only Cowork asks David (D-cowork-6)

> Written by Cowork, 2 Oct 2026. David chose option A that day: one front door (Cowork), one decision queue. Trigger: Codex asked David directly about the batch 04 re-score, so David was handling three agents separately.

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
4. The five blocking items in OPEN_QUESTIONS (session 14) now point to `for-david.md` Q1–Q4 (item 5 is answered: `@cowork`).
5. Final decision number assigned; Codex review (read-only) recorded below; committed.

## Constraints
- Approved by David 2 Oct 2026. Don't change the meaning: a single front door, Cowork, batched.
- Known trade-off David accepted: blocked items wait until his next Cowork session. A scheduled nudge (option C) is explicitly deferred: add it only if blocked work starts to pile up.

## Review

## Outcome
