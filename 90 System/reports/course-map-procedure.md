---
classification: internal
note_type: procedure
source: cowork
review_status: approved
created: 2026-10-02
updated: 2026-10-02
---
# Course map: weekly update procedure

David asked on 2 Oct 2026 for the progress visual to be saved and refreshed every week **without changing the format**.

- **Published page (keep this URL):** https://claude.ai/artifact/GP3R3dCXrrFyxK2Brv1mxH
- **Source (the only file to edit):** `90 System/reports/course-map.html`
- **Schedule:** Cowork scheduled task "Weekly course map", Mondays 08:59 Brussels

## Frozen format: do not change
- The section order: header → 4 stat tiles → Course profile (SVG + legend + calendar bar) → Platform track (6 stage cards) → Running showcase table → Next checkpoints | Waiting on you → Lint result (Fixed now | Flagged to the lead) → Who runs what → footer.
- The `<style>` block, tokens, fonts, SVG geometry, class names and the title "Second Brain Course Map". Don't add or remove sections, cards or columns.
- Only **text, chip states, numbers, the marker position and the calendar-bar width** change.

## What to update, and from where
| Element | Update rule | Source |
|---|---|---|
| Header eyebrow | "status at <date>, <time>" | today |
| Stat tiles | current stage · week N/17 (7 Sep = week 1) · labelled runs /150 · count of "Waiting on you" items | PROGRESS, TASKS T3.1, `for-david.md` |
| Profile marker | Passed stages: filled `--done` circles, solid line. Current stage: the `--blaze` "you are here" marker. Ahead: hollow circles, dashed. Move the marker by changing which circle gets which style; never move the coordinates | TASKS S1–S6, roadmap §0 exit evidence |
| Calendar bar | `.gone` width = elapsed days from 7 Sep / 116 days (to 31 Dec) | today |
| Stage cards | chip: Done <date> · Starting/In progress · Needs host · Ahead · December; 1–2 sentences of state; exit line | TASKS, briefs, git log |
| Running table | One row per checkpoint; append new held-out results as rows; never delete past rows | `03_Golden/`, TASKS T3.x |
| Next checkpoints | Next 5 dated or ordered items | TASKS, PROGRESS "Pick up at", race-goals |
| Waiting on you | Open `for-david.md` entries plus standing "Action for David" items | `for-david.md`, PROGRESS |
| Lint result | Replace with this week's lint: run `90 System/lint-checklist.md` read-only plus a brief/plan consistency check. Fixes Cowork made in briefs go left; items for the lead go right | lint |
| Who runs what | Each agent's next item | open briefs, handoff |

## Rules
- Facts only from the vault; never invent dates. Undated stages stay "Ahead" with no date.
- Cowork never runs git (D63): after editing the source, add an entry to `90 System/handoff.md` for the lead to commit.
- Publish with the Artifact tool to the URL above (read it first), never as a new artifact.
- New questions for David go to `for-david.md` (D68), not into the report.
