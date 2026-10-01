---
classification: internal
---
# Handoff queue (Cowork → git agent)

Cowork edits files but cannot run git (D49). It lists uncommitted changes here. The git agent (Claude Code / Codex) commits each entry as its own commit with the suggested message, on `master` per the multi-agent rules, then deletes the entry. Empty queue = nothing pending.

**Queue empty.** Last processed 1 Oct 2026 (session 12). Four entries became three commits:

| Entry | Commit | Note |
|---|---|---|
| Source archive moved out of the Desktop (D51) | `a588bed` | — |
| Product School and NN/g ingest | `667902e` | Product School part only |
| NN/g round 2 | `2db69fc` | Both NN/g rounds in one commit: round 2 edited round 1's `README`, `sources` and `ux-in-the-ai-era-2026` in place, so they could not be separated without reconstructing intermediate file states. Carries the shared ingest bookkeeping (PROGRESS session 11, OQ-19) |

`index.md`, `log.md`, `PROGRESS.md` and `OPEN_QUESTIONS.md` each held edits belonging to more than one entry; they were split hunk by hunk and the working tree was verified byte-identical to Cowork's final versions afterwards.

Everything is pushed; `master` and `origin/master` match. The two stale topic branches are gone and history is linear, per D50.
