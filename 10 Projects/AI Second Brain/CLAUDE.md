---
classification: internal
review_status: codex-reviewed
---
# Working Memory — AI Second Brain Project

> **START HERE** if you are a Claude session entering this folder.
> Read this file → then `PROGRESS.md` (state, last three sessions) → then `TASKS.md` (open items, one line each) → then `../../90 System/handoff.md` (open entries) and `../../90 System/for-david.md` (open questions).
> Look up decisions in `DECISIONS.md`. Open the archives (`PROGRESS-archive.md`, `TASKS-archive.md`, `../../90 System/for-david-archive.md`, closed handoff entries in `../../log.md`) only when you need history.
> Deep detail lives in `memory/`. Don't re-read the source material unless asked.

## Me

**David Duchesne** — Director in management consulting, deep digital product management background.
Industries: EU and US banking, US asset management, Belgian healthcare/medtech.
Not an engineer or designer, but works with them and can hold an informed technical conversation.

**Preferences:** clarity over cleverness · make implicit assumptions explicit · structured output (tables, trees, numbered flows) · challenge me when requirements are ambiguous or flawed · offer 2–3 options with explicit trade-offs · 1–3 clarifying questions before big work.

## This project in one line

Build an Obsidian second brain on rented models behind a sovereignty router (levels L0–L3, EU provider by default; D134–D135), access across devices by text and voice, and measurable multi-agent operation. Demonstrate building, operating and maintaining it by the December 2026 target. Current sequence: [[10 Projects/AI Second Brain/04_Roadmap|04_Roadmap]] §4 (weeks W1–W8).

> Sits inside the **"Learning AI"** Claude Project. **One workstream: this one.** The Product School **Vibe Coding** training (app + deck on Lovable / Supabase) was archived on 1 Oct 2026 (D62, OQ-5b) — it is not live work. If it revives it gets its own project folder. Historical references to a second workstream come from D10, which D62 supersedes.

**The thesis:** the personal system is the substrate; the eval + governance layer is the product. *Governance = GTM.*

**What I am NOT demoing:** that AI makes me faster. **What I AM demoing:** that I know how to make AI trustworthy enough to deploy in a regulated business, and I built the instrumentation to prove it on myself first.

## Confirmed parameters

| Decision | Answer | Set |
|---|---|---|
| Showcase format | Live system I drive, screen-shared | 7 Sep |
| Access and collaboration | David across devices first, then measured multi-agent execution; additional humans deferred | Amended 1 Oct, D45 |
| Devices | iPhone · iPad · MacBook Air committed. Apple Watch and Tesla browser are S4 stretch | 1 Oct, D52 |
| Hosting | **No hardware purchase; compute is rented online.** Models through EU provider APIs by default (L1: Scaleway, Mistral), other levels per question within the ceiling rules; always-on availability from a rented EU server (Open WebUI, gateway); the Air is a client | 19 Oct, D134–D136 (supersede D53's purchase, D92, D95, D107) |
| Offline | Capture only — durable queue. No on-device inference initially | 1 Oct, D54 |
| Capacity | 20+ h/week sustained | 1 Oct, D55 |
| Service targets | Text p95 < 8 s · voice to first word < 5 s · RTO < 8 h · RPO zero confirmed captures | 1 Oct, D56 |
| Security anchor | Generic but strict — tightest common denominator | 7 Sep |
| Horizon | 3 months (≈ Dec 2026); schedulable at D55 capacity | 7 Sep |

## Where this fits

This folder (`~/Work/Dbrain2/10 Projects/AI Second Brain/`) is project tracking *about* the build,
living inside the vault it tracks, per PARA (`10 Projects` = active work with an end state).
The vault root also has `00 Inbox`, `20 Areas`, `30 Resources`, `40 Archive`, `90 System` — see
`../../90 System/README.md` for the vault-wide conventions.

## Key documents

| File | What |
|---|---|
| `04_Roadmap.md` | ⭐ **The plan.** Rented compute, sovereignty levels, router rules, weekly plan W1–W8 (19 Oct pivot); the S1–S6 version is archived in `40 Archive/AI Second Brain/` |
| `03_Product_School_Playbook.md` | Frameworks, thresholds, checklists to reuse |
| `02_Critical_Assessment.md` | Why the webinar's plan was changed |
| `01_Key_Topics_Summary.md` | What the webinar said (1 correction applied) |
| `00_Source_Material.md` | Pointer to the raw source archive (screenshots, PDFs) — kept outside the vault, not git-tracked |
| `TASKS.md` · `PROGRESS.md` · `OPEN_QUESTIONS.md` | State — read these to resume |
| `DECISIONS.md` | The decision log (D1 onwards); the lead appends new rows here |
| `PROGRESS-archive.md` · `TASKS-archive.md` | Sessions 1–35 and the pre-8 Oct task list, verbatim; history only |

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
| **W1–W8 / L0–L3** | Current delivery weeks / sovereignty levels (L0 own rented GPU, L1 EU provider, L2 US cloud in an EU region, L3 US frontier). S1–S6 and H1–H3 are historical labels. Running evaluation proceeds alongside platform work |

→ Full decoder ring: `memory/glossary.md`

## Standing rules — do not violate

1. **No client-confidential data enters this system.** Demos run on synthetic/anonymised material.
2. **No secrets in the vault.** One live credential was already found in source material.
3. **Depth over breadth.** One showcase workflow, provably excellent.
4. **Current scope (D135–D139, replacing D45's local inference):** rented models behind the switchboard with ceiling rules and no looser fallback now; Open WebUI and phone text/voice next; read-only connectors one at a time behind G4; multi-agent execution measured against a baseline. Defer unneeded vector infrastructure and additional human users. Knowledge writes remain approval-gated.
5. **Six-week honesty check:** has anything shipped *out* of the system? If not, stop capturing.
6. Every note gets `classification: public|internal|client` in frontmatter, from note one. **New notes also carry `source`, `review_status`, `note_type` and `created`/`updated`** (D59). Retrofitting the 114 existing notes is P1.4, held until OQ-20 decides whether `classification` splits into separate domain/sensitivity/processing/sharing axes.
7. **Large files (media, PDFs, recordings) never enter the vault.** They live outside it, ungit-tracked, with a pointer note (path + summary) left in the vault. See `00_Source_Material.md` for the current example.
8. **Fact-check before adding anything to the vault.** Claude proposes, David confirms — before any fact, note, or inference about him becomes structured knowledge (Projects / Areas / Resources). Raw `capture:` drops into `00 Inbox` are exempt (unprocessed by design); the gate applies at triage, when something moves from Inbox into the structured vault. Claude helps structure the second brain; it does not populate it unilaterally.
9. **Keep the Mac awake during lead loops on power (D103).** At loop start, if `pmset -g batt` shows AC Power, start `caffeinate -ims` in the background, note its PID, and kill it at loop close (`-s` holds only on AC). T9 still wraps its own run in `caffeinate -dimsu`.

## Capture protocol (Dispatch / voice / on the go)

Dispatch is the interim route; phone text and voice through Open WebUI and Open Relay are planned for W2 (D136), not yet implemented.

If a message starts with **`capture:`** or is clearly a raw thought dump:

1. Write it to `00 Inbox/YYYY-MM-DD-HHmm-<slug>.md` **at the vault root** (`~/Work/Dbrain2/00 Inbox/`, not inside this project folder)
2. Use the frontmatter template in `~/Work/Dbrain2/00 Inbox/README.md`
3. Transcribe faithfully — light cleanup of dictation artifacts only
4. **Do not** process, expand, research, or ask follow-up questions
5. Confirm in one line: what was captured and where

Triage happens later, in a deliberate weekly pass. Capture ≠ processing.
→ Full protocol: `CAPTURE.md`

## Session close protocol

Before ending any working session, update:
- `PROGRESS.md` — session log entry and current state; move the oldest session to `PROGRESS-archive.md` so three remain
- `DECISIONS.md` — any decision made
- `TASKS.md` — tick what's done, add what surfaced
- `OPEN_QUESTIONS.md` — resolve or add

Leave the project resumable by someone with no memory of the conversation. That someone is you.
