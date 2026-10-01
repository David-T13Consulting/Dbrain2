---
classification: internal
---
# Log

Append-only. Oldest first, newest at the bottom. Each entry starts `## [YYYY-MM-DD] op | title`, where op is capture, ingest, query, lint or decision. Recent activity: `grep "^## \[" log.md | tail -5`.
Appends follow rule 8: Claude proposes, David approves. Scope: structured notes. Routine edits inside a project (tasks, labels) stay in that project's own PROGRESS.md.

## [2026-10-01] capture | How to automate the PM job
Raw French summary of a Fountain senior PM's agentic PM system, dropped verbatim into `00 Inbox/2026-10-01-1037-how-to-automate-pm-job.md`. Unprocessed.

## [2026-10-01] ingest | Second Brain Best Practices
Created `30 Resources/Second Brain Best Practices.md` (draft) from the Karpathy LLM Wiki gist and Tina Huang's video. Fact-checked first pass; superseded a template and a scale figure after the gist text arrived.

## [2026-10-01] decision | Adopt the LLM Wiki pattern in governed form (D41–D44)
David approved: index.md and log.md, gated by rule 8 (D41); supervised ingest as the governance demo (D42); weekly manual lint (D43); good answers filed back via the gate (D44). Added a "Wiki operations" section to AGENTS.md and `90 System/lint-checklist.md`.

## [2026-10-01] lint | baseline (first run, mechanical checks only)
M1 orphans 3 · M2 broken links 1 (Obsidian's Welcome.md placeholder) · M3 not in index 3 · M4 index entries to missing files 0 · **M5 notes without `classification:` 15** (every PROGRESS/TASKS/OPEN_QUESTIONS/roadmap-type note in the AI Second Brain project, plus Welcome.md and the root CLAUDE.md stub) · M6 stale inbox items 0 · M7 large files 0 · M8 secrets 0. Nothing fixed: awaiting David (rule 8). Orphans and M3 are the same 3 notes: README, memory/context/stack, memory/projects/ai-second-brain.

## [2026-10-01] lint | fix M5 (classification frontmatter)
David approved: `classification: internal` added to 13 notes in `10 Projects/AI Second Brain/`, `public` to Welcome.md. Root `CLAUDE.md` stub exempt (recorded in lint-checklist). M5 now 0.

## [2026-10-01] decision | Amend build plan for local, remote and multi-agent operation
David requested amendments, reordering, missing steps and contradiction fixes without replacing the plan. Added S1–S6 and P tasks; retained original rationale/work packages, T IDs, completed work and decision history. Local benchmarking moves first; running evaluation continues alongside; additional human users deferred. Added source provenance, exact-patch approval, scoped tools, voice/text access, durable jobs, independent recovery and operational evidence. Reconciled planning summaries/capture guidance; data-policy v0.3 updates implementation timing and clarifies enforcement without expanding allowed data. D45–D48 and session 7 record the change. Updated index entries for the amended project summaries. This change implements documentation only; reviewed code issues remain open tasks.
