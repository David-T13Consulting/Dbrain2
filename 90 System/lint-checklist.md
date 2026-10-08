---
classification: internal
---
# Lint checklist (weekly, with triage)

Purpose: keep the vault healthy as it grows (D43). Claude runs it read-only and reports counts; David approves any fix. Append the result to `log.md` as `## [date] lint | weekly`.

## Mechanical checks (scriptable, exact counts)
| # | Check | Scope | Count means |
|---|---|---|---|
| M1 | Orphans: notes with no inbound `[[wikilink]]` | 10–40, 90 | Unreachable by graph or index |
| M2 | Broken wikilinks | all | Target missing or renamed |
| M3 | Notes missing from `index.md` | 10–40, 90 | Index drift |
| M4 | Index entries pointing to missing files | `index.md` | Index drift |
| M5 | Missing `classification:` frontmatter, or value `client` | all | Rule violation. `client` = stop and flag |
| M6 | Untriaged Inbox items older than 14 days | `00 Inbox` | Triage backlog |
| M7 | Files over 1 MB, or PDF/media extensions | all | Rule 5 violation |
| M8 | Secret-like strings (tokens, keys) | all | Stop and flag |

## Judgment checks (Claude proposes, David decides)
| # | Check | Output |
|---|---|---|
| J1 | Contradictions between pages | Pairs with the conflicting claims quoted |
| J2 | Stale claims superseded by newer notes or decisions | Note, claim, superseding source |
| J3 | Concepts mentioned in 3+ notes with no page of their own | Candidate pages (proposals, rule 8) |
| J4 | Data gaps worth a web search or a new source | Questions to investigate |

## Exemptions
- Root `CLAUDE.md`: one-line stub (`@AGENTS.md`) that only imports AGENTS.md. Exempt from M5.
- HTML render sources (for example `90 System/reports/course-map.html`): YAML frontmatter would show on the rendered page, so they carry none. Exempt from M5. Each takes the classification of the procedure note that owns it ([[90 System/reports/course-map-procedure|course-map-procedure]] for the course map); an HTML source with no owning procedure note is an M5 finding (Q69 (a), D93).

## Reporting
One table: check · count · fixed · skipped. Track the trend over weeks. Target for M1–M5, M7, M8: zero, or each exception explained.
