---
classification: internal
task: D63
owner: "@code"
status: done
models: ["claude-opus-5 (lead)", "gpt-6-astra, high (review)"]
created: 2026-10-01
---
# Finish adopting the lead/queue orchestration (D63)

> Written by Cowork as provisional **D-cowork-1**; renumbered to **D63** by the lead in session 13.

## Goal
Make the approved agent-orchestration decision official in the tracking files, then commit it as the first run of the new lead loop.

## Files in scope
- `10 Projects/AI Second Brain/PROGRESS.md`: decision row + session log entry
- `10 Projects/AI Second Brain/TASKS.md`: owner tags on every open task
- `index.md`, `log.md`
- `90 System/handoff.md`: clear the entry once committed
- `AGENTS.md` and `40 Archive/agent-orchestration-proposal.md`: **the ID replacement in Constraints only**, no other edit
- `90 System/briefs/_template.md`: the Review-line correction Codex raised, below
- this brief
  *(the two `AGENTS.md` / proposal entries were added by the lead in session 13: Codex's review found the
  Constraints required edits to files the original scope list did not permit.)*

## Inputs / context to read first
- [[AGENTS]] → "Multi-agent work" (already updated by Cowork)
- [[40 Archive/agent-orchestration-proposal|agent-orchestration-proposal]] (approved design record)

## Done when
1. D-cowork-1 has a final number (expected **D63**, unless taken). PROGRESS has the decision row: *Build agents run as lead + queue: Claude Code is the lead and only committer, Codex reviews read-only before each commit, Cowork is the front door and writes briefs; only the lead hands out D/OQ/session IDs.* Why: routing load on David, plus the D51/OQ-19 ID collision on 1 Oct. Revisit if David is still re-briefing agents by hand after two weeks, or briefs go stale for more than three days.
2. Every open task in TASKS.md has one owner tag (@cowork @code @codex @david). Ask David if a tag is ambiguous.
3. `log.md` records the renumbering (`D-cowork-1 → Dnn`); `index.md` lists `40 Archive/agent-orchestration-proposal.md` and `90 System/briefs/`.
4. Codex has reviewed the diff read-only (see Review), and the change is committed to master.

## Constraints
- Do not change the meaning of any task while tagging it.
- Replace `D-cowork-1` with the final number everywhere: AGENTS.md, the archived proposal, this brief.

## Review
Independent read-only review by Codex, 1 Oct 2026, session 13. Model `gpt-6-astra`, reasoning effort `high`,
read-only sandbox, via `codex exec --profile review`. Codex was given the vault rules and the diff only, not
the lead's reasoning. **Verdict: changes required** — five should-fix findings, no blockers. No secrets, no
client data, no missing `classification`, nothing outside the change's stated scope.

| # | File | Finding | Action |
|---|---|---|---|
| 1 | this brief | Constraints require replacing the provisional ID in `AGENTS.md` and the archived proposal, but neither file was in Files in scope — the two instructions could not both be followed | Fixed: both added to Files in scope, limited to the ID replacement |
| 2 | `90 System/handoff.md` | Header still said "the git agent (Claude Code / Codex)" commits each entry, contradicting the new rule that only the lead commits and Codex never does | Fixed in `27ef6be` |
| 3 | `90 System/handoff.md` | Pending entry said "One commit" but listed a second and third | Resolved by clearing the queue; the record now states three commits |
| 4 | `90 System/briefs/_template.md` | "`## Review ← filled by Codex`" contradicts Codex being read-only; AGENTS.md says the lead records the findings | Fixed: the line now reads "filled by the lead from Codex's read-only review" |
| 5 | the briefs | Cross-references to notes used backticked paths, not `[[wikilinks]]` | Fixed in "Inputs / context to read first", which are reading links. "Files in scope" keeps literal paths: those are edit targets, not links |

A second review pass covered the `D65` brief, which arrived after the first pass. Its findings are in that brief.

## Outcome
Done. Cowork's three handoff entries were committed verbatim first, as their own commits, then the lead's
integration work followed:

| Commit | What |
|---|---|
| `08ea191` | Handoff entry 1: the `AGENTS.md` "Multi-agent work" replacement, design record, brief template, this brief |
| `1931d8e` | Handoff entry 2: Model policy section, `models:` field, D64 brief |
| `892146e` | Handoff entry 3: D65 brief |
| `27ef6be` | Handoff queue cleared; its header corrected (finding 2) |
| — | This commit: provisional IDs renumbered `D-cowork-1/2/3 → D63/D64/D65`, briefs renamed to their final IDs, findings 1, 4 and 5 fixed |
| — | Session close: PROGRESS decision row and session 13 entry, TASKS owner tags, `index.md`, `log.md` |

`AGENTS.md` and `_template.md` each carried edits belonging to two handoff entries; they were split hunk by
hunk so each entry is its own commit, and the tree was verified byte-identical to Cowork's versions in
between.

**Open, not blocking:** the `codex` CLI is not on `PATH` — see D64's Outcome.
