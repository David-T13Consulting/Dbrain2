---
classification: internal
---
# AGENTS.md: Dbrain2

David's personal second brain: an Obsidian vault of plain markdown, tracked in git.
PARA layout: 00 Inbox · 10 Projects · 20 Areas · 30 Resources · 40 Archive · 90 System.

## Hard rules
1. **Read-only.** Only create, edit, move or delete a file when David asks for that change in this session.
2. **Keep out:** client or counterparty confidential information, secrets (keys, tokens, passwords),
   and sensitive data about anyone but David. If you find any, stop and flag it.
   Full policy: `10 Projects/AI Second Brain/02_Architecture/data-policy.md`.
3. Every note has `classification: public | internal | client` in its frontmatter. A note tagged `client` is a violation, so flag it.
4. **Propose, don't populate.** Nothing enters 10–40 as structured knowledge until David confirms it.
5. Large files (PDFs, media, recordings) never go in the vault. Leave a pointer note (path and one-line summary) instead.
6. **When unsure, stop and ask.** This covers ambiguous requests, missing data and unclear classification. Don't guess.

## Conventions
- Write in English. Transcribe French captures as spoken; translate at triage.
- `00 Inbox/` holds raw captures named `YYYY-MM-DD-HHmm-<slug>.md`. Don't process them unless David asks for triage.
- Find things with file search (grep/glob). There is no vector index.
- Link notes with `[[wikilinks]]`.
- After each change David approves, commit with a message saying what changed and why.

## Wiki operations
- `index.md` (vault root) catalogs the notes in 10–40 and 90. `log.md` is append-only; each entry starts `## [YYYY-MM-DD] op | title`.
- Appending to either for a change David approved this session counts as part of that change.
- Ingest one source at a time: discuss takeaways with David, propose the pages to create or update, wait for approval, then write, update `index.md` and append to `log.md`.
- Query: read `index.md` first, then the pages. If an answer is worth keeping, propose it as a note (classification and sources included) and file it only after David confirms.
- Lint weekly with `90 System/lint-checklist.md`. Report findings read-only; fix only what David approves.

## Multi-agent work
- Cowork (Claude desktop) edits files but never runs git. Claude Code / Codex do all git work.
- **Commit straight to `master`; keep history linear.** Create a branch only for genuinely speculative work that may be discarded, and delete it as soon as it lands. Branch-per-agent is not the convention: on 1 Oct 2026 it produced two stale branches and a wandering HEAD in a single day, with no review benefit, because only one agent commits and the history never diverges.
- Before switching branches or deleting one, check for another agent's uncommitted work in the tree.
- Cowork lists its uncommitted changes in `90 System/handoff.md`. Before your own work, commit those as their own commit, then clear the entry.
- Never commit, revert or overwrite another agent's uncommitted files unless they are in the handoff. If unsure, stop and ask David.

## Where to start
- Active work lives in `10 Projects/<name>/`. Read that project's CLAUDE.md or README first.
- Conventions written for humans are in `90 System/README.md`.
