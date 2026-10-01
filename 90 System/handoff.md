---
classification: internal
---
# Handoff queue (Cowork → the lead)

Cowork edits files but cannot run git (D49). It lists uncommitted changes here. **The lead (Claude Code) commits each entry as its own commit** with the suggested message, on `master` per the multi-agent rules, then deletes the entry. Codex never commits. Empty queue = nothing pending.

**Queue: empty.** Latest batch processed 1 Oct 2026 (session 13). Three entries became three commits:

| Entry | Commit | Note |
|---|---|---|
| Lead/queue orchestration in `AGENTS.md` + design record + brief template + first brief (D63) | `08ea191` | `AGENTS.md` and `_template.md` held edits belonging to two entries and were split hunk by hunk |
| Model policy section + its brief + `models:` field (D64) | `1931d8e` | — |
| Stop-conditions brief (D65) | `892146e` | Brief only. The `AGENTS.md` change it specifies is the lead's own work and lands separately, because all three entries edit the same section |

Provisional IDs were committed as Cowork wrote them (`D-cowork-1/2/3`) and renumbered by the lead in a following commit; the mapping is in `log.md`.

Previous batch, 1 Oct 2026 (session 12). Four entries became three commits:

| Entry | Commit | Note |
|---|---|---|
| Source archive moved out of the Desktop (D51) | `a588bed` | — |
| Product School and NN/g ingest | `667902e` | Product School part only |
| NN/g round 2 | `2db69fc` | Both NN/g rounds in one commit: round 2 edited round 1's `README`, `sources` and `ux-in-the-ai-era-2026` in place, so they could not be separated without reconstructing intermediate file states. Carries the shared ingest bookkeeping (PROGRESS session 11, OQ-19) |

`index.md`, `log.md`, `PROGRESS.md` and `OPEN_QUESTIONS.md` each held edits belonging to more than one entry; they were split hunk by hunk and the working tree was verified byte-identical to Cowork's final versions afterwards.

Everything is pushed; `master` and `origin/master` match. The two stale topic branches are gone and history is linear, per D50.
