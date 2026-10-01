---
classification: internal
---
# Working Memory — AI Second Brain Project

> **START HERE** if you are a Claude session entering this folder.
> Read this file → then `PROGRESS.md` (state) → then `TASKS.md` (what's next).
> Deep detail lives in `memory/`. Don't re-read the source material unless asked.

## Me

**David Duchesne** — Director in management consulting, deep digital product management background.
Industries: EU and US banking, US asset management, Belgian healthcare/medtech.
Not an engineer or designer, but works with them and can hold an informed technical conversation.

**Preferences:** clarity over cleverness · make implicit assumptions explicit · structured output (tables, trees, numbered flows) · challenge me when requirements are ambiguous or flawed · offer 2–3 options with explicit trade-offs · 1–3 clarifying questions before big work.

## This project in one line

Build an Obsidian second brain with a local model, access across devices by text and voice, and measurable multi-agent operation. Demonstrate building, operating and maintaining it by the December 2026 target; re-estimate dates after hardware/time assessment. Current sequence: [[10 Projects/AI Second Brain/04_Roadmap|04_Roadmap]] §0.

> Sits inside the **"Learning AI"** Claude Project. **One workstream: this one.** The Product School **Vibe Coding** training (app + deck on Lovable / Supabase) was archived on 1 Oct 2026 (D62, OQ-5b) — it is not live work. If it revives it gets its own project folder. Historical references to a second workstream come from D10, which D62 supersedes.

**The thesis:** the personal system is the substrate; the eval + governance layer is the product. *Governance = GTM.*

**What I am NOT demoing:** that AI makes me faster. **What I AM demoing:** that I know how to make AI trustworthy enough to deploy in a regulated business, and I built the instrumentation to prove it on myself first.

## Confirmed parameters

| Decision | Answer | Set |
|---|---|---|
| Showcase format | Live system I drive, screen-shared | 7 Sep |
| Access and collaboration | David across devices first, then measured multi-agent execution; additional humans deferred | Amended 1 Oct, D45 |
| Devices | iPhone · iPad · MacBook Air committed. Apple Watch and Tesla browser are S4 stretch | 1 Oct, D52 |
| Hosting | Dedicated **always-on** host (Mac mini class, 24–32 GB, €800–1,500); the Air becomes a client. Not yet purchased; 32 GB recommended | 1 Oct, D53 |
| Offline | Capture only — durable queue. No on-device inference initially | 1 Oct, D54 |
| Capacity | 20+ h/week sustained | 1 Oct, D55 |
| Service targets | Text p95 < 8 s · voice to first word < 5 s · RTO < 8 h · RPO zero confirmed captures | 1 Oct, D56 |
| Security anchor | Generic but strict — tightest common denominator | 7 Sep |
| Horizon | 3 months (≈ Dec 2026); schedulable at D55 capacity | 7 Sep |

## Where this fits

This folder (`~/Documents/Dbrain2/10 Projects/AI Second Brain/`) is project tracking *about* the build,
living inside the vault it tracks, per PARA (`10 Projects` = active work with an end state).
The vault root also has `00 Inbox`, `20 Areas`, `30 Resources`, `40 Archive`, `90 System` — see
`../../90 System/README.md` for the vault-wide conventions.

## Key documents

| File | What |
|---|---|
| `04_Roadmap.md` | ⭐ **The plan.** S1–S6 delivery gates; original H1/H2/H3 retained as history |
| `03_Product_School_Playbook.md` | Frameworks, thresholds, checklists to reuse |
| `02_Critical_Assessment.md` | Why the webinar's plan was changed |
| `01_Key_Topics_Summary.md` | What the webinar said (1 correction applied) |
| `00_Source_Material.md` | Pointer to the raw source archive (screenshots, PDFs) — kept outside the vault, not git-tracked |
| `TASKS.md` · `PROGRESS.md` · `OPEN_QUESTIONS.md` | State — read these to resume |

## Terms

| Term | Meaning |
|---|---|
| **Prisme One** | French AI bootcamp (Eliott Meunier), source of the personal architecture. Screenshots in the source archive — see `00_Source_Material.md` in this folder |
| **Product School** | His AI Product Strategy + Advanced Agents courses — source of the rigour layer |
| **Golden dataset** | 150-row labelled truth set, versioned in git. *"Your receipts."* The core showcase artifact |
| **Reliability contract** | Metric / target / measurement / alert-threshold table for a workflow |
| **Evidence UX** | Supported / incomplete / conflicting / withheld. Existing skill confidence scores remain heuristic; preserve escalation until reviewed |
| **HITL** | Mandatory knowledge approvals stay; measure avoidable exception handling separately |
| **Showcase workflow** | Strava session classification → weekly assessment → race readiness (D14/D15). Skills in `90 System/skills/` |
| **Agentic search** | Agent greps/reads files directly. Our retrieval choice. Not vector RAG |
| **ZDR** | Zero data retention |
| **S.M.A.R.T. memory** | Scoped · Monitored · Auditable · Retrievable · Timed |
| **S1–S6 / H1–H3** | Current delivery gates / historical work-package labels. Running evaluation proceeds alongside platform work |

→ Full decoder ring: `memory/glossary.md`

## Standing rules — do not violate

1. **No client-confidential data enters this system.** Demos run on synthetic/anonymised material.
2. **No secrets in the vault.** One live credential was already found in source material.
3. **Depth over breadth.** One showcase workflow, provably excellent.
4. **Current scope (D45–D48):** local inference and controlled hosting now; remote text/voice next; multi-agent execution measured against a baseline. Defer MCP sprawl, unneeded vector infrastructure and additional human users. Knowledge writes remain approval-gated.
5. **Six-week honesty check:** has anything shipped *out* of the system? If not, stop capturing.
6. Every note gets `classification: public|internal|client` in frontmatter, from note one. **New notes also carry `source`, `review_status`, `note_type` and `created`/`updated`** (D59). Retrofitting the 114 existing notes is P1.4, held until OQ-20 decides whether `classification` splits into separate domain/sensitivity/processing/sharing axes.
7. **Large files (media, PDFs, recordings) never enter the vault.** They live outside it, ungit-tracked, with a pointer note (path + summary) left in the vault. See `00_Source_Material.md` for the current example.
8. **Fact-check before adding anything to the vault.** Claude proposes, David confirms — before any fact, note, or inference about him becomes structured knowledge (Projects / Areas / Resources). Raw `capture:` drops into `00 Inbox` are exempt (unprocessed by design); the gate applies at triage, when something moves from Inbox into the structured vault. Claude helps structure the second brain; it does not populate it unilaterally.

## Capture protocol (Dispatch / voice / on the go)

Dispatch is the interim route; the local remote text/voice service is planned for S4, not yet implemented.

If a message starts with **`capture:`** or is clearly a raw thought dump:

1. Write it to `00 Inbox/YYYY-MM-DD-HHmm-<slug>.md` **at the vault root** (`~/Documents/Dbrain2/00 Inbox/`, not inside this project folder)
2. Use the frontmatter template in `~/Documents/Dbrain2/00 Inbox/README.md`
3. Transcribe faithfully — light cleanup of dictation artifacts only
4. **Do not** process, expand, research, or ask follow-up questions
5. Confirm in one line: what was captured and where

Triage happens later, in a deliberate weekly pass. Capture ≠ processing.
→ Full protocol: `CAPTURE.md`

## Session close protocol

Before ending any working session, update:
- `PROGRESS.md` — session log entry, current state, any decision made
- `TASKS.md` — tick what's done, add what surfaced
- `OPEN_QUESTIONS.md` — resolve or add

Leave the project resumable by someone with no memory of the conversation. That someone is you.
