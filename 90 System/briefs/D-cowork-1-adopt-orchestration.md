---
classification: internal
task: D-cowork-1
owner: "@code"
status: open
created: 2026-10-01
---
# Finish adopting the lead/queue orchestration (D-cowork-1)

## Goal
Make the approved agent-orchestration decision official in the tracking files, then commit it as the first run of the new lead loop.

## Files in scope
- `10 Projects/AI Second Brain/PROGRESS.md`: decision row + session log entry
- `10 Projects/AI Second Brain/TASKS.md`: owner tags on every open task
- `index.md`, `log.md`
- `90 System/handoff.md`: clear the entry once committed
- this brief

## Inputs / context to read first
- `AGENTS.md` → "Multi-agent work" (already updated by Cowork)
- `40 Archive/agent-orchestration-proposal.md` (approved design record)

## Done when
1. D-cowork-1 has a final number (expected **D63**, unless taken). PROGRESS has the decision row: *Build agents run as lead + queue: Claude Code is the lead and only committer, Codex reviews read-only before each commit, Cowork is the front door and writes briefs; only the lead hands out D/OQ/session IDs.* Why: routing load on David, plus the D51/OQ-19 ID collision on 1 Oct. Revisit if David is still re-briefing agents by hand after two weeks, or briefs go stale for more than three days.
2. Every open task in TASKS.md has one owner tag (@cowork @code @codex @david). Ask David if a tag is ambiguous.
3. `log.md` records the renumbering (`D-cowork-1 → Dnn`); `index.md` lists `40 Archive/agent-orchestration-proposal.md` and `90 System/briefs/`.
4. Codex has reviewed the diff read-only (see Review), and the change is committed to master.

## Constraints
- Do not change the meaning of any task while tagging it.
- Replace `D-cowork-1` with the final number everywhere: AGENTS.md, the archived proposal, this brief.

## Review

## Outcome
