---
classification: public
status: draft
captured: 2026-10-01
updated: 2026-10-01
source: Karpathy "LLM Wiki" gist (primary, https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#llm-wiki, text pasted by David 1 Oct 2026) · Tina Huang "Obsidian in 24 Minutes" (YouTube, via secondary write-up and AI summary)
tags: [second-brain, llm-wiki, obsidian, claude-code, karpathy]
---

# Second Brain Best Practices — the "LLM Wiki" pattern

> Primary source = Karpathy's gist. Tina Huang's video is a popularisation (her "Level 3"). Where they differ, the gist wins.

## Verification status
| Claim | Status |
|---|---|
| Gist text as pasted by David | **Primary source.** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#llm-wiki |
| Tina Huang frames AI + Obsidian as 3 levels (L1 you write, AI retrieves · L2 AI writes, you read · L3 LLM Wiki: AI writes and maintains, you rarely touch it) | Secondary write-up only, video not watched |
| Earlier AI-written `CLAUDE.md` template (from the first summary) | **Superseded.** Not from Karpathy. Do not use as-is |
| Earlier "limit of ~150–200 pages" claim | **Superseded.** The gist says the index works to roughly ~100 sources / hundreds of pages, then add search |

## The core idea
RAG re-derives knowledge from raw documents on every question. The LLM Wiki **compiles knowledge once and keeps it current**: a persistent, interlinked markdown wiki sits between you and the raw sources. New sources are integrated into existing pages (entities, topics, contradictions flagged), so the synthesis compounds. The human curates sources, explores, asks questions. The LLM does the bookkeeping (summaries, cross-references, filing, consistency). Metaphor: Obsidian = IDE, LLM = programmer, wiki = codebase. Maintenance cost near zero is why it survives where human wikis die.

## Architecture (3 layers)
1. **Raw sources** — curated, immutable, source of truth. LLM reads, never edits.
2. **Wiki** — LLM-owned markdown: summaries, entity pages, concept pages, comparisons, overview, synthesis.
3. **Schema** — `CLAUDE.md` / `AGENTS.md`: structure, conventions, workflows. Co-evolved by you and the LLM. This is what makes the LLM a disciplined maintainer, not a chatbot.

## Operations
| Op | What the gist says |
|---|---|
| **Ingest** | LLM reads source → discusses takeaways with you → writes summary page → updates index → updates entity/concept pages (one source can touch 10–15 pages) → appends to log. Karpathy **prefers one source at a time, staying involved** (reads summaries, checks updates, steers emphasis). Batch with less supervision is optional. Document the chosen workflow in the schema |
| **Query** | Search wiki, read pages, synthesise with citations. Output can be markdown, table, Marp deck, matplotlib chart, canvas. **Good answers get filed back into the wiki** so explorations compound (missing from the first summary) |
| **Lint** | Periodic health check: contradictions, stale claims superseded by newer sources, orphan pages, concepts mentioned but without a page, missing cross-references, data gaps fillable by web search. LLM also suggests new questions and sources |

## Navigation files
- **`index.md`** — content catalog by category (entities, concepts, sources…): link + one-line summary + optional metadata (date, source count). Updated on every ingest. Queries read it first, then drill down. Replaces embedding RAG at moderate scale.
- **`log.md`** — append-only chronology of ingests, queries, lint passes. Use a parseable prefix: `## [2026-04-02] ingest | Article Title`, so `grep "^## \[" log.md | tail -5` returns recent activity.

## Optional tooling (all modular, none required)
| Tool | Use | Our stance |
|---|---|---|
| Obsidian Web Clipper | Web article → markdown into raw | Fine, low risk |
| Local images (attachment path e.g. `raw/assets/` + "Download attachments" hotkey) | LLM can see images, URLs don't rot. LLM reads text first, then images separately | Fine, mind large-file rule 7 |
| Graph view | See hubs and orphans | Fine |
| Dataview | Dynamic tables from YAML frontmatter | Fits our frontmatter discipline |
| Marp | Slides from wiki content | Later, relevant to the showcase |
| Git | History, branching, collaboration for free | Already in place |
| **qmd** (local markdown search, BM25 + vector + LLM re-rank, CLI + MCP server) | Search once the index is not enough | Deferred until retrieval measurements justify additional search. Start with index/file search; no requirement to add vectors or MCP |

## Fit with Dbrain2
| Pattern element | Our vault | Assessment |
|---|---|---|
| Raw sources, immutable | `00 Inbox` + source archive outside vault | Close. Inbox gets triaged, raw is permanent. Decide whether triaged inbox items move to a raw/archive area |
| Wiki, LLM-owned | PARA `10/20/30/40`, David populates | **Softer conflict than first thought.** The gist itself endorses supervised, one-source-at-a-time ingest, which matches rule 8 (Claude proposes, David confirms). What we reject is the *unsupervised* variant |
| Schema | `AGENTS.md` + `CLAUDE.md` | Aligned. The gist expects it to evolve |
| `index.md` | Created 1 Oct, D41 | Maintain with approved changes; source navigation plus file search |
| `log.md` | Created 1 Oct, D41 | Parseable operation history; project session history remains in PROGRESS |
| Lint | Checklist and baseline added 1 Oct | Weekly read-only reporting; fixes require approval; automation planned at S3 |
| File answers back | Defined in AGENTS.md, D44 | Propose useful answers as notes through the approval gate |
| Agent writes | Read-only default; explicitly approved session edits allowed | Runtime writer planned at S3 after T4.2; exact changes remain approval-gated |
| `classification:` frontmatter | Mandatory on every note | **Our addition.** Not in the gist. This is the regulated-industry differentiator |
| Human in the loop | Rule 8 | The gist allows it explicitly ("possibly with humans in the loop reviewing updates") for team/business use |

## Decisions (David, 1 Oct 2026) — logged as D41–D44 in PROGRESS.md
1. **D41 · index.md + log.md at vault root, gated.** Created today. Claude proposes entries, David approves (rule 8). Log prefix `## [date] op | title`.
2. **D42 · Supervised ingest as the governance demo.** "LLM Wiki with a human gate and an audit log". Clarified by D47: running stays the established domain; supervised wiki maintenance is shared platform work. OQ-12 resolved.
3. **D43 · Lint = weekly triage step, manual checklist.** `90 System/lint-checklist.md`, read-only, countable. Read-only inspection is available now; scheduled automation is planned at S3, with fixes still approval-gated.
4. **D44 · File good answers back via the rule 8 gate.** Added to AGENTS.md "Wiki operations".
5. **Search tooling:** the original month-4 deferral is superseded by the 1 Oct plan amendment. Add tooling on measured retrieval need; no tool selected.

## Open questions
- (resolved 1 Oct) Gist URL captured.
- Durable source evidence: verbatim captures are archived untouched in `40 Archive/Inbox/` and cited via `source:` (D49). Retention, IDs and metadata remain open (OQ-13).
- Scope clarified by D47: approved PARA knowledge; 90 System holds schema/policy. Start with a bounded corpus, not a full migration.
