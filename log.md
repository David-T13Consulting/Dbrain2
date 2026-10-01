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

## [2026-10-01] decision | Triage routing and raw-capture provenance (D49)
David: wiki covers the whole vault; triaged content goes to PARA by purpose; verbatim captures archived untouched in `40 Archive/Inbox/` and cited via `source:`. Agent split: Cowork edits, Claude Code / Codex commit (option C). Handoff queue created at `90 System/handoff.md`.

## [2026-10-01] ingest | Belgian healthcare & eHealth knowledge base
David asked for an industry knowledge base on Belgian eHealth/healthcare to support building an AI-first, multi-user system for healthcare centres. Approved: `30 Resources/Belgian Healthcare & eHealth/`, classification `public`, full 13-page set. Built from primary sources (INAMI, eHealth platform and its API portal, MyCareNet/NIC-CIN, the Quality Law) plus flagged secondary sources; a locally-held archive of NIC/CIN message brochures supplied the flat-file anatomy and is recorded as a pointer note in `sources.md` per rule 5. Confidence tiers and *Gaps and figures to verify* sections are stated per page; 2009–2023 spec versions are flagged as structurally illustrative only. Corrected one error found against the primary spec: the `410000` family is home-nursing forfaits A/B/C/toilette, not maison-médicale capitation (which uses `MyCareNet-MHM`). Two policy flags raised to David: counterparty contract terms in his own source notes (kept out, §2.1/§6) and third-party health data in `~/Downloads/Medical/` (not read, must never enter the vault, §2.4). Venture strategy, pricing and positioning deliberately excluded from these public pages; David confirmed the knowledge itself is his to restructure, and was advised that vendor-confidential internals stay out regardless of timing and that the build-vs-launch question is for his lawyer.

## [2026-10-01] ingest | Billing rules and cumulation (Belgian nomenclature)
David asked for the billing rules to be understood and documented, citing "2nd doctor visit same day at 50%". Added `30 Resources/Belgian Healthcare & eHealth/billing-rules-and-cumulation.md` (`public`, draft) from the primary nomenclature PDFs: article 1 and 2 interpretative rules, article 2 text, article 7 (physiotherapy) text, article 8 (nursing) text in force 1.9.2026, article 15 interpretative rules. Source register and glossary extended; hub reading order renumbered.
Finding worth recording: there is no single same-day rule, and the premise needed correcting. Doctors (art. 2) use cumulation *prohibitions*, with no percentage reduction in the article. The real 100%/50% rule is surgery (art. 15 §4), written as fraction notation (`N 600/2`) and conditional on a *distinct operative field* — two incisions in one field are not two fields. Physiotherapy does halve: `560011` M 24 (30 min) vs second-of-day `560696`/`561433` M 12 (15 min), requiring a ≥3-hour gap, indispensability, motivation in the patient file, and revocable by the advising physician. Nursing does *not* reduce: `425014`/`425036`/`425051` (first/second/third+ basic service of the care day) are all W 0,879, and a care-day forfait A/B/C or palliative PA–PC can absorb all per-act billing instead.
Also flagged in the page: general web search on this topic returns mostly French (France) rules that do not apply in Belgium; none were used.
