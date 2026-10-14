---
classification: internal
---

# Dbrain2 — vault system notes

PARA structure:
- `00 Inbox` — unprocessed capture. Nothing here is triaged yet.
- `10 Projects` — active, dated, has an end state.
- `20 Areas` — ongoing responsibilities, no end state.
- `30 Resources` — reference material, topic-based.
- `40 Archive` — inactive projects/areas, kept for record.
- `90 System` — notes about the system itself (this file, templates). The agent-facing rules live in `/AGENTS.md` at the vault root, with `/CLAUDE.md` importing them.

## Rules
- Every note carries `classification: public | internal | client` in frontmatter. No exceptions, from note one.
- No client-confidential data enters this vault. Synthetic/anonymised material only.
- Agent access is **read-only by default**; David may authorize specific edits in a session. Runtime writes are planned for S3 only after T4.2 rollback/restore tests, through a scoped writer applying approved patches. No blanket write permission follows from passing a test.
- **Large files never enter the vault.** Media, PDFs, recordings, anything bulky: keep them in a plain
  folder elsewhere on disk (standing home: `~/Documents/Source_Material/<project-or-topic>/`), never git-tracked, and leave a pointer note in the vault (path + one-line
  summary) so they stay findable. Example: `10 Projects/AI Second Brain/00_Source_Material.md`.
  Update the pointer note if the file ever moves — a stale path is worse than no note.
- **Fact-check before adding anything.** Tier 2 content (domain claims, decisions David has not yet
  taken, rule changes, client-facing content) becomes structured knowledge (Projects / Areas /
  Resources / Archive, folders 10–40) only after David confirms it; Tier 0 and Tier 1 changes follow `AGENTS.md` › Review tiers. Raw capture into `00 Inbox` is exempt — the gate is
  at triage. Claude structures the second brain; David populates it.

## Capture
Messages starting `capture:` land in `00 Inbox/` as dated markdown, untouched until weekly triage.
Full protocol: `10 Projects/AI Second Brain/CAPTURE.md`.

## Provenance
Vault skeleton created 8 Sep 2026, session 3. Project tracking (roadmap, tasks, decision log) moved
into `10 Projects/AI Second Brain/` the same day (D12) — it's an active project with an end state,
so per PARA it belongs here, not in a separate folder. Only large raw source material stays outside
the vault; see the large-files rule above.
