# Progress Tracker — AI Second Brain Project

**Last updated:** 29 Sep 2026 · **Updated by:** Claude (session 4)

---

## Current state

| | |
|---|---|
| **Phase** | Week 0 — Foundations |
| **Weeks elapsed** | 0 of 13 |
| **Target** | Client-ready demo, December 2026 |
| **Status** | 🟢 Week 0 gate met (workflow ✅ T0.4, red lines ✅ T0.5). T0.6 open as a refinement |
| **Blocked on** | T0.6 needs David (contract scan) |
| **Next action** | T0.6 — David scans two live contracts for AI/subprocessor clauses; then T1.2 `AGENTS.md` |
| **Action for David** | Paste updated project instructions into claude.ai → project settings (see session 2 log). Still open. |

### Phase progress

```
Week 0  Foundations    ████████░░  83%   ← you are here (T0.1–T0.5 closed; T0.6 open)
H1      Ship           ░░░░░░░░░░   0%
H2      Validate       ░░░░░░░░░░   0%
H3      Collaborate    ░░░░░░░░░░   0%
```

### Gate status

| Gate | Criteria met | Status |
|---|---|---|
| Week 0 | Workflow named · red lines stated | ✅ Met 29 Sep |
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
| D15 | 8 Sep | **T0.4 locked:** "Classify each run's session type (easy/long/tempo/hills/intervals/race/recovery) from raw Strava data, then roll a week of classified sessions into a coaching assessment — trend, effort adequacy, and race-goal trajectory." No Runna connector exists (checked the MCP registry); Strava's `get_training_plan` tool doesn't return real plan data, only a signup link. Session-type classification from raw metrics is the workaround, and a cleaner golden-dataset task than plan-compliance checking would have been | David wants a weekly assessment coach, not a single-workout checker. Decomposed so the golden dataset still has a checkable core: H1 = classification + trend/effort-adequacy (objective). H2 = goal-trajectory judgment, using the confidence-UX pattern (>90%/50-90%/<50%) rather than forcing a binary call in week 1. Ground truth for T3.1 will come from David labeling his own historical runs — no external plan to check against | If Runna ships a real API/connector later, or if session-type classification proves too noisy without HR/lap data on most runs |

---

## Session log

Newest first. One entry per working session — what happened, what changed, where to pick up.

### Session 4 — 29 Sep 2026 · Claude
**Did:**
- Resumed after 3 weeks idle. David: ignore the timeline, work the backlog in sequence.
- T0.2 closed as mitigated: the Zoom recordings are Product School's, so not David's to rotate. The PDF stays outside the vault.
- T0.3 closed as superseded: its only purpose was evidence for T0.4, which was already decided.
- T0.5 done: `02_Architecture/data-policy.md` v0.1. David confirmed three calls: (1) his Strava/HR data is `internal` and may be demoed as-is, with its Art. 9 status stated out loud; (2) third-party data allowed only in minimised form and never demoed; (3) Tower13 material split by counterparty, so own rates and pipeline are internal and anything with counterparty terms is client (excluded). §6 provisional pending T0.6.
- Week 0 gate met.
- Housekeeping: git in the device VM can't clean its lock files, so they are removed after each commit.

**Pick up at:** T0.6 (David, contracts), then T1.2 `AGENTS.md`.

### Session 3 — 8 Sep 2026 · Claude
**Did:**
- T0.1 done: David revoked the Telegram bot token
- Built the vault skeleton in `~/Documents/Dbrain2` (David's existing Obsidian install) — PARA structure,
  git init, classification convention (T1.1, T1.3, T1.5)
- David caught an architecture error: project tracking was split from the vault it tracks. Corrected —
  moved `CLAUDE.md`/`TASKS.md`/`PROGRESS.md`/`OPEN_QUESTIONS.md`/`CAPTURE.md`/roadmap docs/`memory/`
  into `Dbrain2/10 Projects/AI Second Brain/` (D12). Raw source material (239MB, screenshots + PDFs)
  stays outside the vault, ungit-tracked, referenced via a maintained pointer note — new standing
  large-file policy (rule 7)
- Cleaned up `~/Documents/Claude/Projects/` at David's request: removed 42 OS/app junk files; restructured
  `Job search/Applications/` into `Active/` (10) and `Archive/` (14) by a 6-week-quiet cutoff; deduped
  3 near-identical resume PDFs; refiled loose/misplaced files. Documented all judgment calls in that
  folder's own README rather than silently deciding
- David set standing rule 8: Claude fact-checks with him before anything becomes structured vault
  knowledge (capture stays exempt — gate is at triage) (D13)
- **T0.4 locked** (D14, D15): showcase workflow is session-type classification (easy/long/tempo/hills/
  intervals/race/recovery) from raw Strava data, rolling into a weekly coaching assessment. Checked the
  MCP registry for a Runna connector — none exists; Strava's own `get_training_plan` tool doesn't return
  real plan data either, just a signup link. Pulled real Strava data (profile, zones, 15 recent
  activities, full lap data on one structured workout) to ground the decision instead of guessing

**Corrected mid-session:** first pass at T0.4 candidates was inferred from David's job title, not evidence
— he called it out ("I don't understand how this fits into my second brain strategy"). Redid it properly:
asked what he'd actually been thinking about the last few weeks, worked from that.

**Needs David:**
- Confirm whether the two `*_root-copy` CVs in the archived job-search folders (OMP, Lung Cancer Europe)
  are stale duplicates — flagged in that folder's README, low stakes since both are archived
- T0.2 (rotate 4 Zoom passcodes) still open
- Project instructions still need pasting into claude.ai settings (from session 2, still outstanding)
- For T3.1 (golden dataset, week 3): will need David to label a batch of his own historical runs by
  actual session type — no external plan to check ground truth against

**Pick up at:** T0.5 (`data-policy.md`) to clear the rest of the Week 0 gate, then T0.2/T0.6, then
T1.2/T1.4 (both unblocked now that T0.4 is locked).

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
