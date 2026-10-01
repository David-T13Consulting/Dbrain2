---
classification: internal
---
# Context — stack, environment, constraints

## Environment

Recorded environment, not a fresh inventory. Verify installed tools, reachable roots and capacity in P1.1/P1.3; an external archive is not automatically inaccessible to agents.

| | |
|---|---|
| **Machine** | MacBook Air, Apple M2, 24 GiB RAM, 8 CPU cores, macOS 27.2; measured 1 Oct (OQ-4 resolved). See [[10 Projects/AI Second Brain/02_Architecture/local-benchmark-2026-10-01|benchmark]] |
| **Connected folders** | `~/Documents/Dbrain2` (the vault, git-tracked) and `~/Documents/Source_Material` (bulky source material, outside the vault, not git-tracked; moved from `~/Desktop/AI_SecondBrain_Project` on 1 Oct, D51) |
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
| Agent instructions | `AGENTS.md` with root CLAUDE import | Completed T1.2, 29 Sep |
| Model + hosting | Qwen3-4B Q4_K_M / llama.cpp b11146 tested locally; quality failures remain | Initial T9 evidence only; no final choice. Temporary server stopped |
| Inference host / remote access | One controlled local host; private remote access at S4; no unnecessary VPS/platforms | Planned; D45 amends D6 |
| MCP servers | None for now. Direct file access suffices | Decided |
| Vector DB | None initially. Trigger conditions in playbook §6.1 | Decided (D5) |

## Standing constraints

1. **No client-confidential data in the system.** Demos use synthetic or anonymised material.
2. **No secrets in the vault.** One live Telegram token was already found in the source PDFs (T0.1).
3. Every note carries `classification: public|internal|client` in frontmatter from note one; labels inform authorization but tools must enforce actual root/path permissions.
4. Depth over breadth: one showcase workflow, provably excellent.

## Known environmental gotchas

- **Dispatch requires the Mac awake with Claude Desktop open.** Capture from the phone won't execute against a sleeping machine. Belt-and-braces: a native voice memo as buffer. See `CAPTURE.md`.
- Benchmark sustained latency, memory and context limits on the actual Air before judging local feasibility (P1.1/T9); fanless design alone does not settle the choice.
- The remote-device bridge drops occasionally. If a file write fails, the content is still in the chat; re-commit when the link returns.
- Large PDFs: extract text on-device with `pdftotext` rather than staging 50MB files. `pdftotext`, `pdfinfo`, `qpdf`, `gs`, `python3` + `pypdf` are all available on the device.

## Vocabulary note

David works across French and English sources. The Prisme One material is French — *capacités* = skills, *fiches process* = process sheets, *second cerveau* = second brain, *contexte dynamique* = dynamic context. Full list in `memory/glossary.md`.
