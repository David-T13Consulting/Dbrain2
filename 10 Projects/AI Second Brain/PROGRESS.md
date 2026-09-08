# Progress Tracker — AI Second Brain Project

**Last updated:** 7 Sep 2026 · **Updated by:** Claude (session 2)

---

## Current state

| | |
|---|---|
| **Phase** | Week 0 — Foundations |
| **Weeks elapsed** | 0 of 13 |
| **Target** | Client-ready demo, December 2026 |
| **Status** | 🟡 Planning complete, execution not started |
| **Blocked on** | T0.4 — showcase workflow not yet chosen (blocks all of H1) |
| **Next action** | T0.4 — choose the showcase workflow (T0.1 done, T1.1/T1.3/T1.5 done) |
| **Action for David** | Paste updated project instructions into claude.ai → project settings (see session 2 log) |

### Phase progress

```
Week 0  Foundations    ░░░░░░░░░░   0%   ← you are here
H1      Ship           ░░░░░░░░░░   0%
H2      Validate       ░░░░░░░░░░   0%
H3      Collaborate    ░░░░░░░░░░   0%
```

### Gate status

| Gate | Criteria met | Status |
|---|---|---|
| Week 0 | Workflow named · red lines stated | ⬜ Not met |
| H1 | 3 skills pass · rollback tested · evals screen-shareable · no client data | ⬜ Not met |
| H2 | Eval dashboard live · HITL% falling · governance one-pager survives review | ⬜ Not met |
| H3 | Demo runs twice, no unexplained failures | ⬜ Not met |

---

## Metrics

Not yet instrumented — begins week 3 with the golden dataset. Targets for reference:

| Metric | Target | Current |
|---|---|---|
| Hallucination rate | <1% | — |
| Eval regression | 100% of changes stay positive | — |
| HITL % | Trending down | — |
| Recall accuracy | ≥85% | — |

*Deliberately not tracked at this volume: drift velocity/week, confidence distribution, inference ROI, deflection rate. Know the numbers; explain why they're not instrumented yet.*

---

## Decision log

Append-only. Each entry: what, why, and what would change it.

| # | Date | Decision | Rationale | Revisit if |
|---|---|---|---|---|
| D1 | 7 Sep | Showcase = **live system I drive**, not a deck or artifact walkthrough | Highest credibility; forces a real vertical slice | — |
| D2 | 7 Sep | "Collaborative" = **humans sharing first**, multi-agent second | Enterprise reading; shared governed knowledge is the prerequisite | — |
| D3 | 7 Sep | Security designed **generic but strict**, sector-specialised later | Tightest common denominator makes everything else easier | A specific client engagement lands first |
| D4 | 7 Sep | **3-month horizon**, full arc | Room for eval infra + governance to be real, not illustrative | — |
| D5 | 7 Sep | Retrieval = **agentic file search**, no vector store | Right for a personal corpus; simpler, fresher, more secure | Corpus scale, sub-second latency need, or synonym-heavy search |
| D6 | 7 Sep | **Server/VPS out of scope** until month 4+ | Adds operational risk to a live demo; proves nothing to a client | An async workflow genuinely requires it |
| D7 | 7 Sep | Instrumentation moved from phase 4 → **week 3 gate** | It IS the showcase, not the polish. *"Golden datasets are your receipts."* | — |
| D8 | 7 Sep | Model/hosting decision deferred to **week 9**, benchmarked on own golden set | Decide with evidence, not opinion; the decision itself is a demo beat | — |
| D9 | 7 Sep | Storage = **plain markdown + git**, classification in frontmatter from note one | Makes the H3 multi-user layer a filter, not a rebuild | — |
| D10 | 7 Sep | **Claude Project scope broadened** to two workstreams — AI Second Brain (primary) + Vibe Coding training | Original instructions covered only Vibe Coding, so a fresh session couldn't see this work at all | Vibe Coding confirmed dead → drop to one workstream |
| D11 | 8 Sep | **Vault lives in `~/Documents/Dbrain2`** (existing Obsidian install) | David already had Obsidian set up there | Superseded same day by D12 |
| D12 | 8 Sep | **Project tracking merged into the vault**, under `10 Projects/AI Second Brain/`. Raw source material (67 screenshots + 3 PDFs, 239MB) stays at `~/Desktop/AI_SecondBrain_Project/00_Source_Material/`, deliberately outside the vault and not git-tracked | David: "should we move them all under my Vault?" Answer: split by nature. Tracking docs are themselves a PARA project (active, has an end state) so they belong in `10 Projects/`; large binaries would bloat git and clutter the Obsidian UI for no benefit — they're already distilled into the summary docs. Establishes a standing rule: large files never enter the vault, they live in a separate location with a maintained pointer note from the vault. Build history (this git log) now lives inside the second brain itself — deliberate, David confirmed no objection | If the source material needs re-processing regularly rather than as a one-time archive |
| D13 | 8 Sep | **Standing rule 8: fact-check before adding anything to the vault.** Claude proposes, David confirms, before a fact/note/inference becomes structured knowledge. Capture into `00 Inbox` is exempt (unprocessed by design); gate applies at triage | David: "you probably know things about me. Some may be false so you MUST always fact check things with me before adding info to my second brain... You're here to help me structure it properly, not to populate it for me." | — |
| D14 | 8 Sep | **Showcase workflow direction: fitness / running / trail running**, not a consulting-domain task | Ran evidence-led T0.4 properly this time — asked what David actually turned to notes/AI for in the last few weeks, rather than inferring from his job title. Of 8 real topics (parenting, home reno, fitness, supplements, personal finance, San Diego relocation, Tower 13 contract search, Phinest/KPMG conversations), running is the only one with real structured data behind it already (Strava-connected) and a genuinely checkable right answer (actual vs. planned pace/zone/distance). Phinest/KPMG contract review was the runner-up — more on-theme for the client pitch, but needs synthetic data and is a harder build. Exact task shape (the specific input→output transformation) still to be locked | If the exact task shape doesn't clear the checkability bar once specified |

---

## Session log

Newest first. One entry per working session — what happened, what changed, where to pick up.

### Session 2 — 7 Sep 2026 · Claude
**Did:**
- Set up project scaffolding: `CLAUDE.md`, `TASKS.md`, `PROGRESS.md`, `OPEN_QUESTIONS.md`, `CAPTURE.md`, `memory/` (glossary, project profile, stack/environment notes), capture inbox
- Established two-tier memory: durable orientation doc in the Claude Project (survives without device access) + volatile working state on disk
- Designed the on-the-go capture path around how Dispatch actually works — phone → desktop, `capture:` verb, inbox with frontmatter, weekly triage
- Re-committed `03_Product_School_Playbook.md` and `04_Roadmap.md`, which hadn't landed in session 1 when the device link dropped
- **Broadened the Claude Project scope** to cover both workstreams (D10)

**Needs David:** the project *instructions* can't be edited programmatically. Replacement text is in the project doc `claude/ai-second-brain-project.md` under "Proposed project instructions" — paste it into claude.ai → this project → settings. Until then, a fresh session that lands here without device access will still think this project is only about Vibe Coding.

**Pick up at:** T0.1, then T0.3 → T0.4. Bring 3–4 candidate workflows.

### Session 1 — 7 Sep 2026 · Claude
**Did:**
- Organised 67 webinar screenshots into `00_Source_Material/Prisme_One_Webinar/`
- Summarised the Prisme One webinar → `01_Key_Topics_Summary.md`
- Stress-tested it against current published practice → `02_Critical_Assessment.md`; corrected one error of my own in the summary (vendor ZDR landscape reversed Aug 2026)
- Integrated 3 Product School PDFs; extracted text locally, read key slides → `03_Product_School_Playbook.md`
- Reworked the plan into a 13-week roadmap → `04_Roadmap.md`

**Found:**
- 🔴 Live Telegram bot token + 4 Zoom passcodes in the Advanced Agents PDF → T0.1, T0.2
- Product School independently supplies the eval/governance layer the webinar entirely lacks — the two sources are near-complementary
- Two of three sources land on Obsidian-style plain-markdown central memory, independently

**Decided:** D1–D9 above.

---

## How to resume

1. Read `CLAUDE.md` (who, what, rules)
2. Read this file (state, decisions, last session)
3. Read `TASKS.md` (▶ Next action at the top)
4. Check `OPEN_QUESTIONS.md` for anything now answerable

Then work. Before you stop, update all three.
