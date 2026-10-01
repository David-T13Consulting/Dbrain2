---
classification: internal
---
# Progress Tracker — AI Second Brain Project

**Last updated:** 1 Oct 2026 · **Updated by:** Codex (session 10, local models/retrieval)

---

## Current state

| | |
|---|---|
| **Phase** | S1 architecture alignment; running validation in parallel |
| **Schedule** | Original 13-week ordering superseded by S1–S6; re-estimate after hardware/time assessment |
| **Target** | Client-ready demo, December 2026 |
| **Status** | 🟢 Week 0 closed · Week 1 closed · Week 2: 3 skills drafted and smoke-tested · Week 3: golden dataset 50/150 runs labelled (all dev now); rubric v1.4 awaiting its held-out test (batch 04) |
| **Dependencies** | Hardware measured; device/time/budget/acceptance decisions open. Two local candidates and initial retrieval benchmarked, not accepted. Running labels continue independently |
| **Next action** | P1.2/P1.3 requirements/targets; improve retrieval, compare another family and activate weekly model review. Parallel: T3.1 batch 04; T2.6 after 4 Oct |
| **Action for David** | Paste updated project instructions into claude.ai → project settings (see session 2 log). Still open. |

### Original work-package progress — retained snapshot

Current platform gates S1–S6 are not yet passed. P1.0/P1.1 are complete; supplied-evidence comparisons and a bounded retrieval experiment have run, but retrieval/service acceptance remains open. The historical snapshot below is not a percentage-complete estimate for the new scope.

```
Week 0  Foundations    █████████░  90%   (T0.7 contract clause: future-only)
H1      Ship           ██████░░░░  60%   ← you are here (Weeks 1–2 done, Week 3 started)
H2      Validate       ░░░░░░░░░░   0%
H3      Collaborate    ░░░░░░░░░░   0%
```

### Original domain/demo gate status — current platform gates in roadmap §0

| Gate | Criteria met | Status |
|---|---|---|
| Week 0 | Workflow named · red lines stated | ✅ Met 29 Sep |
| H1 | 3 skills pass · rollback tested · evals screen-shareable · no client data | ⬜ Not met |
| H2 | Eval dashboard live · avoidable exceptions measured separately from approvals · governance review (D48) | ⬜ Not met |
| H3 | Demo runs twice, no unexplained failures | ⬜ Not met |

---

## Metrics

Not yet instrumented as a service. Start platform measurement at S2; retain running scores in their batch records. Original aspirations below are qualified by D48 and roadmap §0; no population-level reliability claim yet:

| Metric | Target | Current |
|---|---|---|
| Hallucination rate | <1% | — |
| Eval regression | 100% of changes stay positive | — |
| Avoidable exceptions | Mandatory approvals tracked separately; preserve the approval gate | — |
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
| D16 | 29 Sep | **Every client contract must state explicitly that David uses a personal AI agent.** Engagements under silent or ambiguous contracts stay fully out of the system, including David's own notes. A disclosure clause permits own notes only; client data stays excluded regardless | David: "assume all contracts must be very clear that I use a personal AI agent." Replaces T0.6: there's no firm policy above Tower13, so David sets the rule. Turns a compliance check into a standard Tower13 clause (T0.7), which is itself a governance-as-GTM signal | A client refuses the clause and the engagement matters more than the system coverage |
| D17 | 29 Sep | **AGENTS.md at the vault root, with a one-line root `CLAUDE.md` (`@AGENTS.md`) importing it.** Agents write notes in English, and stop and ask when unsure | AGENTS.md is the cross-tool standard, which keeps the T9 model decision open; Claude only auto-loads CLAUDE.md, so the stub keeps a single source of truth. English keeps search and evals in one language. Stop-and-ask matches rule 8, read-only mode and the <50% confidence band | The T9 model/tool choice drops AGENTS.md support |
| D18 | 29 Sep | **Showcase modelling choices:** (1) HR zones are threshold-based (Friel), LTHR 166 derived from race data, provisional; the vault note is the source of truth, not Strava or Apple. (2) Session types have two axes, terrain (road/trail/mountain) × intent, scored separately; terrain comes from shoes plus climbing per km, never from Strava's sport_type. (3) H2 = readiness for the next minor race; no big target race exists. (4) Hikes, walks and rides count as load and aren't classified | Evidence: max HR unconfirmed (175 observed vs 182 age-derived), and race averages cluster at 163–167. Strava's sport_type is mislabelled on at least 2 activities, and climbing per km alone confuses hilly road races with trail. David chose race readiness over a fitness trend | Re-test LTHR with a 30-min effort; at T3.1, test the zone model against the labelled data |
| D19 | 29 Sep | **Success thresholds approved** for the 3 showcase skills: classify-session (terrain ≥95%, intent ≥85%, <10% unsure) · weekly-assessment (numbers 100% match a deterministic recalculation, verdict ≥90% judge pass, zero made-up numbers, <5% exceptions) · race-readiness (≥80% agreement with David, 100% of <50% confidence cases escalated, 6-week window) | Written before the skills, per the roadmap. Separates what code can check from what needs a judge | Golden dataset shows a threshold is unreachable or trivially easy |
| D20 | 29 Sep | **Skill conventions:** skills live in `90 System/skills/<name>/SKILL.md`; each outputs structured JSON (one line per item) with confidence, the rule IDs that fired and evidence; skills receive their data rather than fetching it (no API calls inside the eval loop); thresholds live only in the rubric and baseline notes, which skills reference and never copy | Structured output is what makes scoring possible. A pure-function skill can be tested repeatedly. One source of truth for thresholds prevents drift | A skill genuinely needs to fetch its own data |
| D21 | 29 Sep | **Rubric v1.1:** (1) long is checked before tempo, and tempo blocks inside a long run are noted, not reclassified; (2) new I8 fallback, unsure, when no rule matches; (3) race = named events only, the vague "race-effort HR profile" clause removed. IDs renumbered (I4 long, I5 tempo) while nothing yet cites them | Gaps found while writing the skill: 8 Nov 2025 Runna long run would have been labelled tempo; unstructured hard runs had no rule; the HR-profile race clause couldn't be checked | Golden dataset shows I8 exceeds the 10% exception budget |
| D22 | 29 Sep | **weekly-assessment design:** a Python script (`compute_week.py`) computes every number and the model only writes the verdict; load = moving time + distance + climbing + time in each zone (Strava Relative Effort excluded because it can't be recalculated); flags F1 load ±30% vs 4-wk baseline, F2 <75% Z1–Z2, F3 no quality session, F4 no long run, with F3/F4 suppressed in race and post-race weeks. Thresholds sit in the `weekly-flags.md` frontmatter and zones in the baseline table; the script parses both and fails loudly if it can't | Meets the 100% numeric-match threshold by design. "The model doesn't do maths" is a governance point for the demo | T3 labelled weeks show the flag thresholds misfire |
| D23 | 29 Sep | **Load baseline = median of the previous 4 weeks**, not the mean | Smoke test: the Dents du Midi week (641 min) lifted the 4-week mean to 280 min against a typical week of ~160, so every week after a big race would look like a collapse. The median gives 169. Races still count as load | Labelled weeks at T3 show the median hides real load build-ups |
| D24 | 29 Sep | **race-readiness design:** 4 criteria computed by `compute_readiness.py`: C1 endurance coverage, C2 terrain specificity (off-road only), C3 recovery (the 1-day-per-mile heuristic on km-effort), C4 recent comparable finished race. A predicted time range (Riegel 1.06 from the C4 reference's chip time, ±3% road / ±8% trail) is withheld when there's no reference. **Blind-call protocol:** David logs his call in `readiness-calls.md` before seeing any output | David picked all 4 criteria, blind logging, and adding time prediction. Blind logging keeps the ≥80% agreement metric uncontaminated. Smoke test: Haversin correctly withholds the time (Dents du Midi at 99 km-effort is outside the 0.5–2× reference window) | C3 heuristic disagrees with David's blind calls systematically |
| D25 | 29 Sep | **Dev/test split for the golden dataset.** Batch 01 (10 runs) is the dev set, used to tune the rubric, and is excluded from headline scores. Accuracy is claimed only on held-out batches. **Rubric v1.2** from batch 01: climbing ≥50 m/km → mountain whatever the shoes; hills before intervals; tempo before long (reverts D21); Runna's "Long Run" label ignored; recovery also = Z1–Z2 within 14 days after a race | Blind score of v1.1 on batch 01: terrain 90%, intent 56%, both below threshold. D21 was Claude inferring David's definition instead of asking; David labels progression and pace-block runs as tempo. Scoring the same rows used for tuning would overstate accuracy | Held-out batches show v1.2 overfit to batch 01 |
| D26 | 29 Sep | **Labelling workflow:** multiple choice (terrain, then intent group, then a split question), facts only, no predictions shown; **20-run batches** | Pilot pace ~1 min per run. David asked for choices over free text | Pace drops or fatigue shows in label consistency |
| D27 | 30 Sep | **Recovery = post-race only.** Easy effort within 7 days after a race up to 21 km, 14 days after a marathon, ultra or mountain race (7/14 split proposed by Claude). I6a (≤45 min + HR ≤140) removed | David: "only after a race, for 1 or 2 weeks". Batch 02: 0 of 8 easy runs labelled recovery; I6a caused 3 misses | Short races wrongly turn easy runs into recovery (OQ-7) |
| D28 | 30 Sep | **Intent gets two labels:** main label + a separate `tempo_block` flag. Main label: long if road ≥75 min or trail/mountain ≥2 h, else tempo if a tempo block exists, else easy/recovery. Label-format change made after seeing results; existing labels stand, the flag is asked only where it applies | David: long runs "tend to be tempo runs, but not always", so one label forced a false choice. Duration-first matched 8/9 long/tempo rows vs 5/9 for v1.2 | The flag can't reach its own accuracy threshold |
| D29 | 30 Sep | **Tempo = target race pace for the distance** (David): ~5:10/km marathon, ~4:40 half, a little faster for 5–10 km. Tempo block = ≥15 min continuous at ≤5:10/km, not in reps. Strict 5:10: David's easy runs sit at 5:15–5:20 | Replaces HR-based tempo, which fired on David's normal long-run HR (150–155 = Z3). Where pace is meaningless (trail, mountain, sustained climbs) the fallback is still open (OQ-9 B2) | Target paces change with fitness |
| D30 | 30 Sep | **Hikes are not runs** (count toward load, no session type). **Unknown gear = no gear** (T4) | David, OQ-9 D and E | — |
| D31 | 30 Sep | **Terrain = surface; `vertical` flag for steep climbing work.** Terrain: road / trail, mountain only for real mountains (T1 ≥50 m/km kept). `vertical` = one sustained climb ≥15%, or ≥2 climbs ≥8%. Terrain relabel for 3 batch 02 rows (#16, #18, #19: mountain → surface + flag) | David: Tiennes and Citadelle repeats "simulate mountain runs" (a purpose, not a surface). Max gradient alone didn't reproduce his labels (Grospierres ~14% = trail; Citadelle loop ~10% = mountain). Feeds race-readiness C2 (Haversin ~1,100 m) | Flag thresholds misfire on held-out batches; altitude noise near 8% |
| D32 | 30 Sep | **Off-road tempo = HR.** On trail, mountain or sustained climbs, a tempo block is ≥15 min at HR ≥157 (Z4+), or Runna race-pace blocks. Flat road keeps race pace (D29) | David chose it after the test: on the 4 labelled off-road easy/tempo runs, average pace (raw or climb-adjusted) got 3/4 with 1–3 s margins; HR got 4/4 | LTHR re-test (OQ-6) moves Z4 |
| D33 | 30 Sep | **No athlete values hardcoded.** HR zones and target race paces live only in dated tables in `athlete-baseline.md` (`effective_from`; add a row on change, never edit old rows). Rubric and skills refer to zones by name and read the row in effect on the run's date; `compute_week.py` does the same and reports `zones_effective_from` / `zones_assumed` | David: values will change as he improves. Dating them keeps historical golden-dataset rows judged by the zones that applied then | — |
| D34 | 30 Sep | **Race paces come from Strava Performance Predictions**, updated monthly: a scheduled task asks David on the 1st of each month and a new dated row is added only when a value changes. First row 30 Sep 2026: marathon 5:06, half 4:34, 10 km 4:16, 5 km 4:03 /km. The tempo-block threshold (marathon pace) moves from 5:10 to 5:06 for runs from 30 Sep | Predictions track fitness as David improves, without manual target-setting. Strava's API doesn't expose them and has no zone history (age-formula only before 29 Sep 2026) | David's easy runs creep within a few s/km of marathon pace |
| D35 | 30 Sep | **Mountain = altitude, not climbing rate** (G1). T1 becomes: terrain above ~1,000 m, not in road shoes → mountain. Replaces ≥50 m/km, which contradicted D31 | David OK. Profondeville hill repeats (121 m/km) are trail for him | A road-shoe run at altitude (e.g. Montvalezan, Mar 2026) is labelled mountain |
| D36 | 30 Sep | **Two tempo thresholds** (G3, David chose "any sustained ≥15 min at tempo HR or faster, including climbs"). The `tempo_block` flag uses that broad definition (Z3+ HR, or ≤ marathon pace on flat, ≥15 min continuous, not reps). The **main intent** `tempo` keeps the strict test (race pace on flat, Z4+ off-road, D29/D32), otherwise David's easy runs at HR 150–155 would all become tempo | Consistent with his own labels: batch 03 #19 = easy + tempo_block. Under this definition reps don't count, so his "yes" on batch 03 #5 and #18 stay as labelled | Flag false positives on easy runs |
| D37 | 30 Sep | **Reps on a climb = hills** (G4): I2 also fires when ≥3 work reps are done uphill (work parts averaging ≥5% grade), not only on ≥3 climb/descend cycles | David, batch 03 #5 (2 × 20 × 30/30 up the Citadelle) | Flat reps with one short rise get called hills |
| D38 | 30 Sep | **Batch 03 #1 relabelled** intervals → long: David, "most likely misclick". Recorded as a ground-truth correction, not a rubric change | Laps showed no reps | — |
| D39 | 30 Sep | **Unknown-gear cut-off 25 m/km** (G2): ≥25 → trail, <25 → road | David chose 25 after 75 was checked against his labels (75 would flip two trail runs to road); 25 fits all three batch 03 unknown-gear rows | Unknown-gear rows near 25 disagree |
| D40 | 30 Sep | **Long = over 15 km** (road, trail); km-effort over 15 on mountain terrain. **A long run can also be tempo** → `long` + `tempo_block` (David: "a 15+ km long run can also be tempo"). Scoring rule for the golden set: David's `tempo` on a run over 15 km counts as agreement when v1.x outputs `long` + `tempo_block`; labelling from batch 04 offers "Long with tempo" as its own answer so he never has to choose | Replaces the 75 min / 2 h durations. Checked on dev rows: km-effort only in the mountains, otherwise the 11 km / 458 m easy trail run of 4 Aug 2026 would become long | A >15 km run that David calls tempo has no tempo block in the data |
| D41 | 1 Oct | **`index.md` and `log.md` at the vault root, gated by rule 8.** Claude proposes each entry, David approves. Log prefix `## [YYYY-MM-DD] op | title`. Index is the retrieval layer (agentic search, no vector RAG). Seeded from file names and existing summaries | Karpathy's LLM Wiki gist: the index replaces embedding RAG at moderate scale, the log gives a greppable timeline. Vault had neither. David chose "both now, gated" | Approval overhead per entry slows the Strava work |
| D42 | 1 Oct | **Supervised ingest = the governance demo:** "LLM Wiki with a human gate and an audit log". Reading to confirm (OQ-12): the Strava workflow stays the showcase content, and the gate plus log are the governance wrapper | The gist allows supervised, one-source-at-a-time ingest. That is rule 8 turned into a demo, and it fits Governance = GTM. Risk: competes with "depth over breadth" if treated as a second showcase | OQ-12 answer says it is a second showcase, or H1 slips |
| D43 | 1 Oct | **Lint = weekly triage step with a manual checklist** (`90 System/lint-checklist.md`), read-only, countable. Agent-run lint after Week 4 (T4.2) | Gist lint: orphans, contradictions, stale claims, missing pages, gaps. Counts make it measurable. First baseline run: 15 notes lack `classification:` (rule 3) | Checklist yields no findings for 4 weeks |
| D44 | 1 Oct | **Good query answers get filed back as notes, through the rule 8 gate.** Added to AGENTS.md under "Wiki operations" together with the index/log/ingest/lint rules | The gist's compounding effect depends on answers not disappearing into chat. The gate keeps David as the populator | Triage load becomes the bottleneck |
| D45 | 1 Oct | **Amend the existing build plan to S1–S6:** architecture, local read-only slice, supervised wiki maintenance, remote text/voice, measured agents, operations/demo. Benchmark the Air first; one controlled inference host is the working architecture. Additional humans deferred. Supersedes D2 ordering, D6 local-host exclusion and D8 week-9 timing | David requested the plan be amended/reordered after the review; local models, cross-device access and voice are central goals | Hardware, availability and weekly time change scope or dates |
| D46 | 1 Oct | **Plan enforced runtime boundaries and one deterministic writer.** Bind approval to exact patch/base revision; scoped roots/tools; restore test before writes; independent backups and redacted traces from the first service | Classification labels alone do not enforce permissions. Preserve existing data exclusions and human knowledge approval | Threat tests or restore drills expose missing controls |
| D47 | 1 Oct | **Running remains the domain; supervised wiki maintenance is shared platform work.** Preserve source evidence, provenance and contradictions; plan code/runtime separation outside the vault. Small synthetic professional demo at S6. Resolves OQ-12; OQ-13 storage/retention detail remains open | Demonstrate a complete knowledge lifecycle while preserving existing skills and avoiding a second production domain | A new domain is explicitly approved |
| D48 | 1 Oct | **Platform and running evaluation proceed alongside each other.** Freeze acceptance sets; independent arithmetic checks; evidence-state UI; heuristic confidence is not probability; mandatory approvals are distinct from avoidable exceptions | The 150 running labels must not block local feasibility experiments; review exposed calculation/rule inconsistencies. Corrections are planned, not performed here | Measured performance or test coverage changes acceptance criteria |
| D49 | 1 Oct | **Triage routing and raw-capture provenance** (OQ-13, part): the wiki covers the entire vault; triaged content goes to PARA by purpose; the verbatim capture is archived untouched in `40 Archive/Inbox/` and cited in the new note's `source:`. `00 Inbox` itself stays out of `index.md` (raw, unchecked). **Agent split (David, option C):** Cowork edits files only; Claude Code / Codex do all git work (commit, branch, push, PR) | Keeps the gist's immutable raw layer and an audit trail for lint, without a separate raw/ tree. Cowork's sandbox has no GitHub credentials, and adding a token would breach "no secrets an agent can read" | Archive growth becomes a burden, or Cowork gets safe git access |

---

## Session log

Newest first. One entry per working session — what happened, what changed, where to pick up.

### Session 10 — 1 Oct 2026 · Codex
**Authorization:** David asked to continue the local experiments, document local models across modalities, and maintain weekly benchmark updates.
**Changed:** eight notes in `30 Resources/Local AI/`, weekly review runbook, and a second local evaluation report. Pinned 17 publisher model-card revisions; kept published scores separate from local measurements. Preserved a small external evidence archive, with scripts and raw results.
**Measured:** Qwen3.5-4B Q4_K_M, eight same-prompt development requests (median 7.41 s; valid citation IDs in 1/8). Ten retrieval development requests (median generation API time 6.14 s; evidence retrieved for 6/7 in-corpus answerable questions). French search missed evidence; missing archival policy led to a wrong cited answer. Six provisional cases reserved and not run. Neither candidate accepted; P2.1/P2.3/T9 remain open.
**Operations:** temporary localhost server stopped. Weekly task prompt ready, but no active automation: no exposed scheduler tool and desktop app access denied. SAFe handoff staging was rejected by automatic approval review; its queue and edits were preserved. This work's commit must exclude them and Obsidian settings.
**Next:** activate the weekly local-project review, define bounded benchmark time/download budgets, add D49 evidence and bilingual query handling, independently review evaluation labels, then compare another model family. Requirements OQ-14/OQ-15 remain open.

### Session 9 — 1 Oct 2026 · Codex, hardware and local benchmark
**Scope:** David said proceed with hardware assessment/benchmark, then resume after the usage-limit interruption. Completed P1.1, with OQ-4 answered by measurement. Local candidates and service targets remain open.
**Evidence:** M2 / 24 GiB / 8 CPU cores; Qwen3-4B Q4_K_M under llama.cpp b11146. Baseline 16 requests: median 6.37 s, p95 9.72 s. One development prompt revision: 8 requests, median 6.76 s, p95 12.28 s. Invalid citations and a contradictory hostile-source answer prevent acceptance; v2 improves those seen cases but fails language/citation handling on another case.
**Artifacts:** [[10 Projects/AI Second Brain/02_Architecture/local-benchmark-2026-10-01|measurement record]]; raw artifacts/models outside vault in temporary storage. Local server stopped. No retrieval, voice or agent writes implemented; no hardware purchase or final runtime choice.
**Coordination:** D49 handoff committed separately as fe43f6f. Subsequent Cowork/healthcare/SAFe changes left separate; this commit contains only benchmark work and its tracking.
**Next:** answer P1.2/P1.3 requirements, build retrieval baseline and compare another local candidate on defined development/acceptance splits. Running labels continue independently.

### Session 8 — 1 Oct 2026 · Claude (Cowork)
**Authorization:** David asked to pull SAFe knowledge into Resources for his Product Leader / Program Manager / Transformation Consultant roles, approved all 17 pages, chose toolkits as source despite licence risk, asked for 6.0+ currency.
**Changed:** created `30 Resources/SAFe/` (17 notes, `internal`, draft); updated `index.md`, `log.md`, `90 System/handoff.md`. Toolkits extracted to a temp folder outside the vault, then deleted; nothing copied in (rule 5, pointer in `sources.md`).
**Found:** SAFe moved twice since the 5.1 toolkits — Oct 2024 "SAFe Disciplines" restructure and AI-Native SAFe (23 Jun 2026). AI-Native details are secondary-source only. A read-only `git status` left an empty `.git/index.lock` (no delete permission at the time); removed after David granted delete access. Cowork should avoid git commands entirely.
**Also:** added `30 Resources/SAFe/ai-native-safe.md` (dedicated AI-Native SAFe page, claims tiered A/B/C, gaps listed).
**Pick up at:** git agent commits the handoff entry. OQ-17 (SAFe licence / AI-Native verification) when David wants client use.

### Session 7 — 1 Oct 2026 · Codex
**Authorization:** David asked to amend, reorder and extend the existing build plan, preserving it and fixing contradictions. Planning/documentation scope only.
**Changed:** added S1–S6 to the roadmap; retained original rationale/work packages, T IDs and completed checkboxes; added P tasks for local QA, supervised updates, remote voice/text, bounded agents and operations. Reconciled current-state summaries, open questions and scheduling references. D45–D48 appended; historical decision/session entries preserved.
**Review evidence:** prior read-only synthetic checks reproduced load-only hikes counted as runs, 200% HR coverage on an inconsistent stream and F3 firing for long + tempo work. Source inspection found weekly zone selection, missing-history ambiguity and stale classifier guidance. P3.4/P3.5 track fixes; no code/rubric changes made.
**Validation scope:** documentation diff, links/task references and preservation of completed work/history. No model installed, hardware purchased, service deployed, inbox triaged or data policy scope expanded.
**Pick up at:** P1.1 read-only hardware inventory; P1.2/P1.3 settle requirements/targets. T3.1 batch 04 remains the next independent labelling action.

### Session 6 — 1 Oct 2026 · Claude
**Summary:** adopted the Karpathy LLM Wiki pattern in governed form. D41–D44 logged. Two Inbox/Resources notes created, vault-root `index.md` and `log.md` added, AGENTS.md gained a "Wiki operations" section, lint checklist written and run once.
**Did:**
- Inbox: dropped "how to automate the PM job" (French PM-agent guide) verbatim. Unprocessed.
- `30 Resources/Second Brain Best Practices.md` (draft): digest of the Karpathy gist (primary) and Tina Huang's video (secondary). Superseded an AI-written CLAUDE.md template and a 150–200 page scale claim. Qmd and any search layer stay deferred to month 4+ (rule 4).
- David decided D41–D44 by multiple choice (all four recommended options).
- Created `index.md`, `log.md`, `90 System/lint-checklist.md`. Edited AGENTS.md (hand-written v1 from D17): added 5 lines under "Wiki operations".
- Baseline lint: 15 notes missing `classification:`, 3 orphans, 0 secrets, 0 large files. Nothing fixed.
- David approved the M5 fix: 13 project notes → `internal`, Welcome.md → `public`, root CLAUDE.md stub exempt. M5 = 0. Committed.
**Pick up at:** T3.1 batch 04 unchanged as the next labelling action. First weekly lint due with the next triage.

### Session 5 — 30 Sep 2026 · Claude
**Summary:** held-out scores v1.2 → v1.3: intent 50% → 75%, terrain 85% → 90%. D27–D40 logged. Rubric v1.4, classify-session v0.5, dated baseline (zones + Strava pace predictions), monthly pace-check scheduled task (1st of month, 08:52). Session closed by David (tired).
**Did:**
- David asked whether the golden dataset could be skipped or handed to another LLM. Answer: it's on the critical path (H1 gate, T4.1, T5, T9 all read from it), and LLM-written labels would score model-vs-model agreement, not correctness. David chose to label the full batch himself.
- Fixed a reproducible held-out sampling order: 133 eligible runs (Jan 2025 – 29 Sep 2026, minus dev batch, worked examples, kid runs), seeded shuffle (20260930) → `03_Golden/heldout-order.md`. Batches 02–06 = rows 1–100, 101–133 spare.
- T3.1 batch 02: 20 held-out runs, facts only, labelled by David via multiple choice (terrain, intent group, split) → `03_Golden/labels-batch-02.md`.
- Blind score of rubric v1.2 on batch 02: **terrain 17/20 (85%), intent 10/20 (50%)**, 0 unsure. Dev re-score had been 100%/100%: v1.2 overfit to batch 01, exactly the D25 revisit condition. The dev/test split paid for itself on first use.
- Five failure causes logged as hypotheses (A recovery too eager, B tempo firing on long/easy runs — possibly LTHR set too low, C mountain = steep climbs per David, D unlisted gear, E hike logged as run). Not tuned: needs David's answers first (OQ-9).

- David answered OQ-9 → D27–D32. Two of his answers were tested against his own labels before being written as rules: "maximum gradient" for mountain (didn't reproduce his labels → `vertical` flag instead, D31) and "average pace" for off-road tempo (3/4 vs HR 4/4 → HR, D32).
- Rubric **v1.3** (`30 Resources/Running/session-types.md`) and **classify-session v0.4** written; target race paces added to athlete-baseline. Batch 02 is now dev (D25 protocol). v1.2's held-out score stays 85% / 50%.
- Dev re-score of v1.3, main intent, done by hand: batch 02 20/20, batch 01 8/9 (the 23 Aug progression run is long + tempo_block, David said tempo). Tuned rows, so this proves consistency, not accuracy.

- D33: removed hardcoded HR/pace values from rubric v1.3 and skill v0.4 at David's request; baseline zones and paces now dated; compute_week.py made date-aware and tested (2026 week → current row; Dec 2024 week → earliest row, flagged as assumed).

- T3.1 batch 03 labelled (one run per screen after David objected to two runs sharing a question). v1.3 held-out: terrain 90%, intent 70% (up from 50%), tempo_block 70%, vertical 80%. Six causes G1–G6 logged in `labels-batch-03.md`; questions to David as OQ-10.

- OQ-10 answered → D35–D40; rubric **v1.4** and classify-session **v0.5** written. Batch 03 is now dev.

- Scope question: David asked when to add domains (family logistics, energy, vacations, knowledge digest). Captured to the inbox (unprocessed), one gated backlog line, OQ-11 parked. Nothing built (rule 8, depth over breadth).

**Pick up at:** batch 04 = rows 41–60 of `heldout-order.md`, one run per screen, intent split with a "Long with tempo" answer. T2.6 after 4 Oct.

**Pick up at (superseded):** batch 03 = rows 21–40 of `heldout-order.md`, blind. Labelling now also asks the two flags for every run (not only where the rule might fire, which would hide false negatives). Expect ~25–30 min. Flags on the dev rows are not labelled; the terrain of 3 batch 02 rows (#16, #18, #19) is superseded by D31 and left as history. T2.6 after 4 Oct.

### Session 4 — 29 Sep 2026 · Claude
**Did:**
- Resumed after 3 weeks idle. David: ignore the timeline, work the backlog in sequence.
- T0.2 closed as mitigated: the Zoom recordings are Product School's, so not David's to rotate. The PDF stays outside the vault.
- T0.3 closed as superseded: its only purpose was evidence for T0.4, which was already decided.
- T0.5 done: `02_Architecture/data-policy.md` v0.1. David confirmed three calls: (1) his Strava/HR data is `internal` and may be demoed as-is, with its Art. 9 status stated out loud; (2) third-party data allowed only in minimised form and never demoed; (3) Tower13 material split by counterparty, so own rates and pipeline are internal and anything with counterparty terms is client (excluded). §6 provisional pending T0.6.
- Week 0 gate met.
- Housekeeping: git in the device VM can't clean its lock files, so they are removed after each commit.

- D16: contracts must state AI agent use explicitly; T0.6 closed, T0.7 added; data-policy → v0.2.

- T1.2: AGENTS.md v1 written at the vault root with a CLAUDE.md stub (D17). Approved by David. T0.7 is future-only: no live contracts.

- T1.4 in progress: 3 notes drafted (athlete-baseline, session-types, race-goals) from David's Strava data and his decisions (D18).

- T1.4 closed: David confirmed the long-run rule, delegated the hills definition (structured repeats only), said Tuesday trail runs are usually intervals, and listed 3 races (Dinant half 4 Oct, Gelbressoise 11 Nov, Haversin 32 km 21 Nov). David is setting his HR zones manually in Strava and on his Apple Watch to match.

- T2.1 approved (D19). Gelbressoise details added (all three distances are "course nature"); distance still undecided.

- T2.2: classify-session v0.1 drafted (D20). Rule IDs (T1–T4, I1–I7) added to the rubric so outputs can cite them. Gelbressoise working assumption: 12 km.

- David applied all 3 review fixes (D21); classify-session v0.2 approved.

- T2.3: weekly-assessment v0.1 + compute_week.py drafted and smoke-tested on real 21–27 Sep summaries (D22). The test exposed the Dents du Midi week (641 min) inflating the 4-week mean baseline.

- Baseline switched to the median (D23); weekly-assessment v0.2 approved.

- T2.4: race-readiness v0.1 drafted and smoke-tested (D24). Dinant output computed but deliberately **not shown to David** until his blind call is logged.

- T2.5: first blind call logged. David borderline / 1:35; skill borderline (0.60) / 1:38:54–1:45:01, so the verdict agrees. Time threshold approved. Known road-elevation limitation logged before the race, not tuned after seeing David's guess.

- T3.1 pilot: batch 01 labelled by David in ~9 min via multiple choice. Blind v1.1 score: terrain 90%, intent 56%. Four failure causes → rubric v1.2 + classify-session v0.3 (D25). Batch 01 designated the dev set. 20-run batches agreed (D26).

**Session summary:** D16–D26 logged this session. Week 0 gate met; vault has AGENTS.md, a data policy, a running baseline, a rubric, 3 skills (2 with deterministic scripts), success thresholds, a blind-call log and the first golden-dataset batch.

**Pick up at:** T3.1 batch 02 (Claude prepares 20 held-out runs, blind). T2.6 after Dinant (4 Oct). Open items: LTHR re-test (OQ-6), stale project instructions (action for David).

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
