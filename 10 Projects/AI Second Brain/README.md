---
classification: internal
---
# AI Second-Brain Project

Building a personal AI system that works — and that stands up as proof of expertise in front of a client.

**Goal:** an Obsidian second brain using a local model, reachable across devices by voice and text, with measurable multi-agent operation. December 2026 remains the demo target, subject to hardware/time assessment.
**Thesis:** the personal system is the substrate. The eval and governance layer is the product. *Governance = GTM.*

---

## 🚀 Resuming? Start here

1. **`CLAUDE.md`** — who, what, standing rules *(a Claude session should read this first)*
2. **`PROGRESS.md`** — current state, decision log, last session
3. **`TASKS.md`** — ▶ Next action is at the top
4. **`OPEN_QUESTIONS.md`** — anything now answerable?

**Right now:** S1 architecture alignment. Foundations are complete; three running skills are drafted and 50 labelled runs are development data. Next platform action: P1.1 hardware inventory. Parallel domain action: T3.1 batch 04. See [[10 Projects/AI Second Brain/TASKS|TASKS]].

---

## Where things live

This project-tracking folder sits **inside the vault it tracks** (`~/Documents/Dbrain2/10 Projects/AI Second Brain/`),
per PARA — an active project with an end state belongs under `10 Projects`. One exception: raw source
material (large binaries) lives *outside* the vault entirely and isn't git-tracked. See `00_Source_Material.md`.

```
~/Documents/Dbrain2/                      ← the vault (Obsidian, git-tracked)
├── 00 Inbox/                             ← captures land here (root level, not project-scoped)
├── 10 Projects/
│   └── AI Second Brain/                  ← you are here
│       ├── CLAUDE.md                     ← working memory · START HERE
│       ├── TASKS.md                      ← to-do list, phase-organised
│       ├── PROGRESS.md                   ← state, decisions, session log
│       ├── OPEN_QUESTIONS.md             ← what's blocking, who can answer
│       ├── CAPTURE.md                    ← talking to the system on the go (Dispatch)
│       ├── 00_Source_Material.md         ← pointer to the archive below (path + summary, kept current)
│       ├── 01_Key_Topics_Summary.md      ← what the webinar covered
│       ├── 02_Critical_Assessment.md     ← webinar vs. current practice
│       ├── 03_Product_School_Playbook.md ← frameworks, checklists, metrics
│       ├── 04_Roadmap.md                 ← ⭐ THE PLAN — S1–S6 + original history
│       ├── memory/                       ← long-term memory
│       │   ├── glossary.md               ← decoder ring, 3 vocabularies
│       │   ├── projects/ai-second-brain.md
│       │   └── context/stack.md          ← environment, tool decisions, gotchas
│       ├── 02_Architecture/              ← design decisions (data-policy.md goes here)
│       ├── 04_Model_Config/              ← planned benchmark records, S2
│       └── 05_App_Prototype/             ← original placeholder; runtime repo planned outside vault
├── 20 Areas/
├── 30 Resources/
├── 40 Archive/
└── 90 System/                            ← vault-wide conventions, read this too
    └── README.md

~/Desktop/AI_SecondBrain_Project/         ← NOT the vault. Source archive only.
└── 00_Source_Material/                   ← 239MB — 67 webinar screenshots + 3 course PDFs
                                             not git-tracked, already distilled into the summary
                                             docs above. Findable via 00_Source_Material.md.
```

## The three sources

| Source | Contributes | Its weakness |
|---|---|---|
| **Prisme One webinar** | Personal architecture — vault, skills, context layers | No evals, no security, no governance; solo-creator scope |
| **Product School** | Rigour and commercial framing — golden datasets, eval dashboards, reliability contracts, agent governance, S.M.A.R.T. memory | Enterprise framing; assumes a team; RAG-default retrieval |
| **Current published practice** | Mechanics and reality — agentic retrieval, Agent Skills / AGENTS.md, MCP threat model, vendor retention shifts, EU AI Act | No view on your specific goal |

Two of the three land on Obsidian-style plain-markdown central memory, independently. That convergence is the reason to trust the substrate choice.

## Current delivery order

S1 architecture → S2 local read-only answers → S3 supervised wiki updates → S4 remote text/voice → S5 measured multi-agent execution → S6 operations/demo. Running validation continues alongside; T10 additional users is deferred. Code/runtime/source locations are planned boundaries, not migrations completed by the amendment.

## Original 13-week framing — historical reference

The table below preserves the September plan; roadmap §0 and TASKS now govern order and dependencies.

| Horizon | Weeks | Outcome |
|---|---|---|
| **Week 0** | — | Data policy, secrets cleanup, choose the showcase workflow |
| **H1 · Ship** | 1–4 | Working vertical slice + golden dataset + evals wired |
| **H2 · Validate** | 5–9 | Eval dashboard, reliability contract, confidence UX, governance one-pager, model decision |
| **H3 · Collaborate** | 10–13 | Multi-user layer, supervisor agent, security hardening, demo rehearsal |

## Standing rules

1. **No client-confidential data enters this system.** Demos run on synthetic or anonymised material.
2. **No secrets in the vault.** One live credential has already been found in the source material.
3. **Depth over breadth.** One showcase workflow, provably excellent.
4. **Current scope (D45–D48):** local inference and controlled hosting now; remote text/voice next; multi-agent execution measured against a baseline. Defer MCP sprawl, unneeded vector infrastructure and additional human users. Knowledge writes remain approval-gated.
5. **Six-week honesty check:** has anything shipped *out* of the system? If not, stop capturing.
6. **Large files never enter the vault** — outside, ungit-tracked, with a maintained pointer note.

*Last updated: 1 October 2026 — amended, original framing retained.*
