# Context — stack, environment, constraints

## Environment

| | |
|---|---|
| **Machine** | MacBook Air (`macbook-air-local`), macOS, Apple Silicon. RAM unknown — OQ-4 |
| **Connected folders** | `~/Documents/Dbrain2` (the vault, git-tracked) and `~/Desktop/AI_SecondBrain_Project` (source-material archive, not git-tracked) |
| **Project root** | `~/Documents/Dbrain2/10 Projects/AI Second Brain/` |
| **Timezone** | Europe/Brussels |
| **Reachable via Claude** | Desktop files, shell (sandboxed to connected folders), built-in browser, Chrome extension, Dispatch from phone |
| **Not reachable** | Apple Notes (protected location, no API, no connector — R5). `~/Library` generally |

## Tool decisions

| Layer | Choice | Status |
|---|---|---|
| Knowledge store | Plain markdown + git | Decided (D9) |
| Retrieval | Agentic file search — no vector store | Decided (D5) |
| Skills format | `SKILL.md` (portable open standard) | Decided |
| Agent instructions | Hand-written `AGENTS.md` in the vault | Week 1 (T1.2) |
| Model + hosting | **Undecided by design** — benchmarked week 9 against own golden set | Deferred (D8) |
| Server / VPS | Out of scope until month 4+ | Decided (D6) |
| MCP servers | None for now. Direct file access suffices | Decided |
| Vector DB | None initially. Trigger conditions in playbook §6.1 | Decided (D5) |

## Standing constraints

1. **No client-confidential data in the system.** Demos use synthetic or anonymised material.
2. **No secrets in the vault.** One live Telegram token was already found in the source PDFs (T0.1).
3. Every note carries `classification: public|internal|client` in frontmatter from note one — makes H3 RBAC a filter rather than a rebuild.
4. Depth over breadth: one showcase workflow, provably excellent.

## Known environmental gotchas

- **Dispatch requires the Mac awake with Claude Desktop open.** Capture from the phone won't execute against a sleeping machine. Belt-and-braces: a native voice memo as buffer. See `CAPTURE.md`.
- The Air is **fanless** — it throttles on sustained load. A reason local inference is a poor bet for a live demo.
- The remote-device bridge drops occasionally. If a file write fails, the content is still in the chat; re-commit when the link returns.
- Large PDFs: extract text on-device with `pdftotext` rather than staging 50MB files. `pdftotext`, `pdfinfo`, `qpdf`, `gs`, `python3` + `pypdf` are all available on the device.

## Vocabulary note

David works across French and English sources. The Prisme One material is French — *capacités* = skills, *fiches process* = process sheets, *second cerveau* = second brain, *contexte dynamique* = dynamic context. Full list in `memory/glossary.md`.
