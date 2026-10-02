---
classification: internal
---
# Handoff queue (Cowork → the lead)

Cowork edits files but cannot run git (D49). It lists uncommitted changes here. **The lead (Claude Code) commits each entry as its own commit** with the suggested message, on `master` per the multi-agent rules, then deletes the entry. Codex never commits. Empty queue = nothing pending.

**Queue: 2 entries.**

| Entry | Files | Suggested commit message |
|---|---|---|
| Batch 04 scored against rubric v1.4 by Cowork, validated by David 2 Oct. Terrain 100% · intent 65% · tempo_block 40% · vertical 90% | `10 Projects/AI Second Brain/03_Golden/labels-batch-04.md` | `Golden dataset: score batch 04 against rubric v1.4 (held-out, validated by David)` |
| Single front door (D-cowork-6, David chose option A on 2 Oct): new decision queue + brief for the AGENTS.md change, which is the lead's own work | `90 System/for-david.md` (new), `90 System/briefs/D-cowork-6-single-front-door.md` (new), this file | `Add single-front-door decision queue and brief (D-cowork-6)` |

Tracking for the lead:
- Tick T3.1 batch 04 as scored; the scoring owner was `@cowork` (David, 2 Oct).
- Add the batch 04 held-out scores to PROGRESS.
- The v1 held-out test is now closed, so **T3.4 (taxonomy v2) is unblocked**.
- Suggested follow-up for David: an independent Codex re-score of batch 04 (the caveat is in the file).

Latest batch processed 2 Oct 2026 (session 14). Three entries became three commits:

| Entry | Commit | Note |
|---|---|---|
| Taxonomy v2 proposal brief (provisional `D-cowork-5` / `T3.5`) | `9c7ed8b` | Committed verbatim with Cowork's own message and provisional IDs, then renumbered by the lead in the following commit: **`T3.5` → `T3.4`** (next free task ID) and **`D-cowork-5` → `D67`**. The brief stays a *proposal*: David approved option B and its five sub-points, but the rubric v2.0 wording still needs him, per rule 8 |

The taxonomy brief's sequencing is recorded in [[10 Projects/AI Second Brain/TASKS|TASKS]] as given: **score rubric v1.4 on batch 04 first**, because that is the last held-out test of the v1 schema. Nothing in `classify-session/` or `session-types.md` may move before then.

The other two entries of the same day:

| Entry | Commit | Note |
|---|---|---|
| T3.1 batch 04 prepared blind (rows 41–60) and labelled by David, 2 Oct | `d0505d0` | Committed with the files and message the entry specified. The lead's first message claimed `labels-batch-04.md` was not named in the entry's file list and had been committed as a judgement call — wrong: the entry names it explicitly. The lead had read this file *before* Cowork added the file list and did not re-check after Cowork revised it mid-session. Codex's review caught it and the message was amended (hence the hash change from `6eb3919`). No scope exception was ever needed |
| Two new briefs: P2.2 read-only query service (`@code`), P2.1 independent case review (`@codex`) | `2092ff2` | Committed verbatim. The [[10 Projects/AI Second Brain/TASKS|TASKS]] owner tags the entry asked for are the lead's own work and landed separately in `8fb68d0` |

The briefs entry was committed after the lead's own staged renumbering (`01562e1`), not before it, because `90 System/briefs/P2.2.md` → "Step 0" told the lead to finish that interrupted commit first. No files overlapped, so both stayed separable. Codex flagged the ordering: a Cowork brief does not override "the lead commits handoff entries first", so it is on the list for David.

**The tracking updates were all applied in session 14.** Batch 04 is ticked as labelled-not-scored in [[10 Projects/AI Second Brain/TASKS|TASKS]] with the label-process and distribution notes; the race/`tempo_block` call David made during labelling is recorded as **D66** (Cowork's provisional `D-cowork-4`, renumbered by the lead per D63) with the rubric-wording follow-up deferred until after scoring; a session-14 entry is in [[10 Projects/AI Second Brain/PROGRESS|PROGRESS]] and a `label` entry in [[log]]. No open question was raised, as the entry said none was needed.

**One thing Cowork left open and the lead did not guess:** who scores batch 04. The entry proposed "`@cowork` or `@code`" without choosing. [[10 Projects/AI Second Brain/TASKS|TASKS]] records the owner as unsettled and it is on the list for David.

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
