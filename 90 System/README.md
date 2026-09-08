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
- `90 System` — notes about the system itself (this file, templates, later: AGENTS.md).

## Rules
- Every note carries `classification: public | internal | client` in frontmatter. No exceptions, from note one.
- No client-confidential data enters this vault. Synthetic/anonymised material only.
- Agent access is **read-only** until Week 4 (T4.2 rollback test passes). No MCP write access before then.

## Capture
Messages starting `capture:` land in `00 Inbox/` as dated markdown, untouched until weekly triage.
Full protocol: see `CAPTURE.md` in the AI_SecondBrain_Project folder (project tracking lives there, not here).

## Provenance
Vault skeleton created 8 Sep 2026, session 3. Project tracking (roadmap, tasks, decision log) lives
separately in `~/Desktop/AI_SecondBrain_Project/` — that folder is project management *about* this vault,
this vault is the second brain itself.
