---
classification: internal
---
# Handoff queue (Cowork → the lead)

Cowork edits files but cannot run git (D49). It lists uncommitted changes here. **The lead (Claude Code) commits each entry as its own commit** with the suggested message, on `master` per the multi-agent rules, then deletes the entry. Codex never commits. Empty queue = nothing pending.

**Queue: 1 entry.**

| Entry | Files | Suggested commit message |
|---|---|---|
| T3.1 batch 04 prepared (rows 41–60, blind) and labelled by David, 2 Oct | `10 Projects/AI Second Brain/03_Golden/labels-batch-04.md` (new), this file | `Golden dataset: batch 04 labelled (held-out, rubric v1.4 not yet scored)` |

**Tracking updates for the lead (Cowork session, 2 Oct 2026). Write these into PROGRESS / TASKS / OPEN_QUESTIONS:**
- TASKS T3.1: batch 04 labelled ✅ 2 Oct, **not scored yet**. Next: score rubric v1.4 blind against these labels. It's running-domain work; owner `@cowork` or `@code`, and nobody touches `classify-session/` before then.
- Label process: intent asked as a single question with fixed options. A two-part intent form confused run 1, which was re-asked. A pre-scoring consistency check changed 4 rows (13, 18, 19, 20); the original labels are kept in the Note column. Report scores both ways, like D38.
- Label distribution: race 4 · long 7 · easy 5 · tempo 2 · intervals 1 · hills 1. Terrain: road 13 · trail 6 · mountain 1. Races (4, 9, 11, 15) all have tempo_block = no. **Decided by David, 2 Oct (provisional D-cowork-4):** a race is a race, not a tempo block. Races get `tempo_block = no` whatever the effort, and the batch 04 labels stand. Why: race is its own intent, and counting it twice would blur both labels. The rubric/session-types definition of `tempo_block` should state the exclusion explicitly, but only *after* v1.4 is scored on batch 04, so the held-out test isn't contaminated. No new OQ is needed.

---

Latest batch processed 2 Oct 2026 (session 14). One entry became one commit:

| Entry | Commit | Note |
|---|---|---|
| Two new briefs: P2.2 read-only query service (`@code`), P2.1 independent case review (`@codex`) | `2092ff2` | Committed verbatim. The TASKS.md owner tags the entry asked for are the lead's own work and land separately |

The entry was committed after the lead's own staged renumbering (`01562e1`), not before it, because `90 System/briefs/P2.2.md` → "Step 0" told the lead to finish that interrupted commit first. No files overlapped, so both stayed separable.

Previous batch, 1 Oct 2026 (session 13). Three entries became three commits:

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

History is linear and the two stale topic branches are gone, per D50. **Not pushed:** `master` is ahead of `origin/master` by several commits (the D63–D65 work of sessions 13 and 14). The session-13 note that said everything was pushed was wrong — that applied to the session-12 batch only.
