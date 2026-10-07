---
classification: internal
---
# Progress Tracker — AI Second Brain Project

**Last updated:** 7 Oct 2026 · **Updated by:** Claude Code (session 30, lead loop, M3 done)

---

## Current state

| | |
|---|---|
| **Phase** | S1 requirements settled; S1 exit evidence incomplete (P1.3 data-flow diagram, roots/tools list); S2 under way: P2.2 query service committed (`4b5e91f`, runtime `c8b3b7b`); MVP-phone parked; repos moved off iCloud to `~/Work` (M2, done 6 Oct); remaining clean-up before new work. Running validation in parallel |
| **Schedule** | Original 13-week ordering superseded by S1–S6. Dated S2–S6 plan exists, proposed (`f9c014e`); demo-ready Fri 18 Dec 2026 (Q29) |
| **Target** | Client-ready demo, December 2026 |
| **Status** | 🟢 Week 0 closed · Week 1 closed · Week 2: 3 skills drafted and smoke-tested · Week 3: golden dataset **70/150** runs labelled. Batch 04 held out and scored 2 Oct — terrain 100% (≥95% ✅), intent 65% (≥85% ❌); the flags have no D19 threshold, and against the always-"no" baseline of 85% `tempo_block` at 40% is far worse while vertical at 90% barely beats it. The evidence behind the v2 taxonomy (D67) |
| **Dependencies** | Devices, availability, capacity, service targets and provenance schema all settled 1 Oct (D52–D59). Remaining dependency is the always-on host purchase (D53) — the Air cannot satisfy the availability requirement. Two local candidates and initial retrieval benchmarked, not accepted. Running labels continue independently |
| **Next action** | **M3 done (session 30, D78):** ui-design-agent, claude-blueprint and agentic-ios-app are in `~/Work/_archive/` (fsck clean, heads unchanged) and archived on GitHub. Every step of the Q65 clean-up run is now done. **The 08:57 hold stays until David lifts it**; the lead does not lift it. Vault commits of this run are not pushed (a push needs David's OK). **Next:** David lifts the hold (via Cowork); then answer quality (P2.5, T9) is what he will feel first. Host decision (D53) gates sustained-performance numbers |
| **Action for David** | **All six session-14 questions are answered and recorded** — his standing actions below are unaffected: D64 closed, the `dbrain-runtime` repository authorised (now `~/Work/dbrain-runtime/`), batch 04 scored by `@cowork`, and Q5/Q6 answered through the [[90 System/for-david|for-david]] queue on its first use — Codex may read the 6 reserved cases read-only (P2.1 unblocked), and nothing changes on David's side for interactive Codex (D68 closed). Then: paste the weekly-review task ID and first-run output into [[90 System/weekly-local-model-review|weekly-local-model-review]] (D60). Decide the always-on host purchase (D53; 32 GB recommended). OQ-20 is answered (queue Q10, 5 Oct); OQ-21 was not needed — David decided it himself as D66. |

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
| D50 | 1 Oct | **Commit straight to `master`; keep history linear.** Branch only for genuinely speculative work and delete it as soon as it lands. Branch-per-agent is not the convention. *(Row added 1 Oct, session 12: the decision was recorded in `log.md` and `AGENTS.md` but never indexed here)* | Only one agent commits at a time and history never diverges, so branch-per-agent produced two stale branches and a wandering HEAD in a day with no review benefit | Genuine parallel review need, or more than one agent gaining git access |
| D51 | 1 Oct | **Bulky source material gets one standing home outside the vault: `~/Documents/Source_Material/<project-or-topic>/`.** The 239MB archive moved there from `~/Desktop/AI_SecondBrain_Project/00_Source_Material/` (now `~/Documents/Source_Material/AI_Second_Brain/`); pointer note, README, stack and glossary updated | David wanted the Desktop cleaned up and a general place for bulky material. `~/Documents` already holds the vault, is a sibling of it (outside git and outside Obsidian indexing), and avoids a second top-level location. Desktop folder name also collided with the vault as "second brain" | If Documents sync becomes a problem for large binaries, move the whole `Source_Material` root and update the pointer note |
| D52 | 1 Oct | **Committed client devices: iPhone, iPad, MacBook Air.** Apple Watch and the Tesla in-car browser are S4 **stretch** surfaces, not commitments: the Watch needs a companion iOS app or a Shortcut, and the Tesla has no CarPlay, so it is a browser against the same web UI | All three ride the same private authenticated endpoint, so neither stretch surface changes the architecture or S1 design. Resolves OQ-14, device half | A stretch surface turns out to need its own client or endpoint |
| D53 | 1 Oct | **The service must answer any time, any place, so a dedicated always-on host replaces the Air as the inference host.** Mac mini class, 24–32 GB, budget €800–1,500. The Air becomes a client. **Purchase is a separate decision; nothing is bought by this entry.** Recommendation on record: take 32 GB | A travelling laptop cannot be always-on, so the availability requirement decides the hosting question. 24 GB equals the Air already benchmarked and leaves no headroom once model, retrieval, local ASR and local TTS must be resident together, before S5 adds roles | Measured S2 memory use shows 24 GB is comfortable, or availability relaxes |
| D54 | 1 Oct | **Offline means capture only.** Durable queue, idempotent retries, visible pending/failure state. No on-device inference in the initial target | Matches roadmap §0 and keeps the capture habit trustworthy without a second model, second eval suite and a quality gap to manage. Resolves OQ-14, offline half | A device class must answer questions with the host unreachable |
| D55 | 1 Oct | **Sustained capacity: 20+ hours a week.** December 2026 becomes a schedulable target rather than an aspiration | David's own commitment, materially above the 5–8 h this plan had assumed. Resolves OQ-15, capacity half | Actual logged hours fall below it for three consecutive weeks |
| D56 | 1 Oct | **Service targets, now measurable (T6 inputs):** cited text answer **p95 < 8 s** · voice push-to-talk to first spoken word **< 5 s** · recovery time **< 8 h, same day** · recovery point **zero confirmed captures**. Report p50/p95 with sample counts and conditions, never an average alone | Acceptance runs cannot pass or fail without numbers. 8 s is reachable locally with retrieval plus a mid-size model and still leaves room for an S5 checker pass. Resolves OQ-15, targets half | **The < 5 s voice target is the one expected to break first:** ASR, retrieval, generation and speech on one always-on box. S4 reports the real p95 and renegotiates; a miss there is a renegotiation, not a failure |
| D57 | 1 Oct | **Durable source IDs: `src-<YYYYMMDDTHHmm>-<short content hash>`** | Survives renames and triage moves, which the D49 triage flow performs by design; the hash detects both duplicates and silent edits; no central counter for concurrent agents to collide on. Resolves OQ-13, IDs | Hash collisions or a need for human-quotable IDs in conversation |
| D58 | 1 Oct | **Voice audio is deleted on successful transcription.** The transcript becomes the retained original evidence; the note records that audio was discarded | Minimises the most sensitive artifact the system will hold. **Consequence accepted: transcription quality is now an evidence-integrity concern, not just UX** — there is no original to re-read, and David's captures are bilingual. Resolves OQ-13, audio retention | Transcription proves unreliable on French/mixed speech, in which case a short re-transcription window returns with a provable purge job |
| D59 | 1 Oct | **Minimum frontmatter on structured notes:** `classification` + `source` + `review_status` (proposed/approved/stale/conflicting) + `note_type` (fact/synthesis/decision/reference) + `created`/`updated`. **New notes only**; retrofit is P1.4, unscheduled | `source` is the spine of the evidence story — without it a claim cannot be followed back and AI summaries become circular evidence. Current coverage across 114 structured notes: 7 have `source`, 10 have `created`, zero have `review_status` or `note_type`. Resolves OQ-13, metadata | OQ-20 splits `classification` into several axes, in which case design the schema once and retrofit against the final shape |
| D60 | 1 Oct | **Weekly local-model review is active** (David activated it in the desktop scheduler). M4 closed, OQ-18 resolved. Task ID and first-run output still to be pasted into the runbook's activation record | David confirmed activation. The evidence row stays open rather than being filled with an invented ID | The first two scheduled runs do not actually produce output |
| D61 | 1 Oct | **OQ-17 closed without the SAFe currency check** — the 5.1-era content is too old to be worth re-verifying. **Consequence: the SAFe pages are historical reference only and must not be used client-facing**, since nobody has checked them against AI-Native SAFe or the 2024+ Disciplines | David's call: the effort does not pay back. Closing the question is not the same as resolving it, so the constraint it was protecting against is recorded instead | A client engagement actually needs current SAFe material, which means re-obtaining the assets first |
| D62 | 1 Oct | **Vibe Coding workstream archived.** The project carries one workstream: the second brain. Supersedes D10's two-workstream scope; resolves OQ-5b. No files to move — it existed only as scope references, and the Product School resource notes are genuine knowledge that stays | The app + deck deliverable is not live work. Carrying it in scope made every status read ambiguous | David revives it, in which case it gets its own project folder rather than a share of this one |
| D63 | 1 Oct | **One lead, one queue for the three build agents.** Claude Code is the lead (build, integration, git, bookkeeping); Cowork captures, specs and briefs and never runs git; Codex reviews read-only and never commits. Every open task in TASKS.md carries an owner tag, work handed between agents needs a brief in `90 System/briefs/`, and only the lead assigns final D-, OQ- and session numbers | Three agents were writing into one tree with no owner, which produced two stale branches, tangled uncommitted work and provisional IDs nobody renumbered. Option B (the committing agent and the integrating agent are the same) was chosen over a separate integrator | The review gate proves too slow to be worth it, or a second agent needs commit rights |
| D64 | 1 Oct | **Build-agent models follow a policy David sets:** Opus for Cowork and the lead, smaller Claude models for simple subagents, GPT-6 Astra as the independent reviewer at effort `high`, escalating to `ultra` only when the lead and reviewer are both stuck; config files apply it, agents do not pick models outside it. **Closed 2 Oct** — the standalone CLI is installed at `~/.local/bin/codex`, so `codex exec --profile review` works as documented, and the `AGENTS.md` wording now matches the config David set. See [[90 System/briefs/D64-model-policy\|D64 brief]] | Removes the per-session model choice from David, keeps the review independent by using a different vendor's model, and makes model use traceable through each brief's `models:` field | A model is retired, or reviews prove too slow or too costly |
| D65 | 1 Oct | **The lead loop has explicit stop conditions** — no `open` `@code` brief left, a failed review, a decision that belongs to David, or a `blocked` brief — **and a retry limit:** at most 5 attempts per failing step, a read-only Codex debugging opinion after the 2nd failure, then `blocked`. **In force 2 Oct**, written into `AGENTS.md` verbatim after D64 closed, with `blocked` added to the brief template. Its own closure took five review rounds, hitting the retry limit it defines — the judgement call that ended it is recorded in the brief | An interactive run otherwise decides for itself when it is done, and an unattended run (option B, not yet adopted) needs this before it is safe | Runs stall on "a decision for David" too often |
| D66 | 2 Oct | **A race is not a `tempo_block`.** Races are labelled `tempo_block = no` whatever the effort, and the batch 04 labels stand as David gave them. The `tempo_block` definition in the rubric and [[30 Resources/Running/session-types\|session-types]] must state the exclusion explicitly — but only **after** rubric v1.4 is scored on batch 04, so the held-out test is not contaminated | Race is already its own intent; counting a race as a tempo block as well would blur both labels. David decided it during the batch 04 labelling rather than leaving it as an open question. Written by Cowork as provisional `D-cowork-4`, renumbered by the lead | The scored batch shows the exclusion costs more than it buys |
| D68 | 2 Oct | **One front door: only Cowork asks David.** Claude Code and Codex never ask him directly — they add an entry to [[90 System/for-david\|for-david]] (from, brief, question, options with the recommended first, what it blocks, urgency), set the brief to `blocked-on-david`, and carry on with other work. Cowork walks David through the open entries each session; the lead turns answers into decisions and commits, then clears the entry. Stop condition (3) now means "write to the queue", not "ask" | David was handling three agents separately: Codex asked him directly about the batch-04 re-score while the lead was putting four other questions to him. Batching through one agent is option A; a scheduled nudge (option C) is deferred until blocked work actually piles up | Blocked items start waiting too long for his next Cowork session — the trade-off he accepted |
| D67 | 2 Oct | **Session taxonomy v2: split the mixed `intent` axis into orthogonal axes** — terrain · format (continuous/progression/reps/hill reps) · dominant intensity by Friel HR zone (recovery-base/steady/threshold/VO2max+) · stacking context flags (race, competition, time trial, post-race, long). Minutes per intensity band replace `tempo_block`. David also settled five sub-points: no purpose axis, a track is road, the threshold boundary comes from HR zones with pace as the short-rep fallback, batches 01–04 get re-derived by rule with David resolving only disagreements, and fartlek and strides are dropped. **Approved in principle only** — the rubric v2.0 wording still needs his sign-off (rule 8), and nothing changes until batch 04 is scored under v1.4 | The single `intent` axis mixes format, intensity and context, which is why five decisions so far (D28, D37, D40, D66 and the batch 04 relabels) have had to patch it. An axis earns its place only if a weekly-assessment rule uses it *and* a deterministic rule can reproduce David's label; industry alignment with Runna, Strava, Campus and Garmin is a bonus. Written by Cowork as provisional `D-cowork-5`, renumbered by the lead | The rule-derived relabelling of batches 01–04 disagrees with David often enough that the axes are not actually checkable. Note this makes the LTHR re-test (OQ-6) urgent: the whole intensity axis depends on it |
| D70 | 5 Oct | **Two-tier stops: D65 condition (2) is amended.** A failed Codex review still ends the lead loop when any blocker is substantive (security, data boundaries, correctness, policy wording). If every blocker is bookkeeping only (owner tags, frontmatter, tracking text, IDs), the lead fixes it in the same run and re-reviews once; a second failure, or a substantive blocker, stops the loop as before. The 5-attempt retry limit still applies. David's answer Q27 | Session 17 stopped D69 on a single blocker covering two missing owner tags, which cost a whole run for a two-word fix; the review's independence is kept because the fix is still re-reviewed | A bookkeeping fix turns out to hide a substantive problem, or the lead starts classifying real blockers as bookkeeping |
| D69 | 5 Oct | **Data policy v0.4: personal data beyond training/HR enters in gated waves, and children's data gets its own rule.** Wave 0 (own training/HR) is in force; wave 1 (ordinary personal, e.g. family logistics without names) waits for the P1.4 four-axis retrofit and a lint check on the axes; wave 2 (health beyond training, finances, journal; local-only) waits for five gates: local answers with no cloud fallback, cloud agents provably unable to reach the files, a synthetic leak test, trace redaction, and a tested deletion rule covering working copy, git history and backups. The waves govern material added from 5 Oct; existing personal notes are relabelled in P1.4. New §3a: no names, initials, nicknames, identifying places or town; minimise before capture; no health, behaviour, performance or photos; never demoed; manual capture only; logistics only. Approved by David as Q20, revised after Codex's review (Q24) and approved again as Q25. Written by Cowork as provisional `D-cowork-7`, renumbered by the lead | David wants kids' schedules in the system (Q19) without loosening the red line; gating each wave on controls that are tested, not on labels, keeps sensitive material out until the system can actually protect it | A wave-2 gate proves impossible without a vault split, which would reopen OQ-20 |
| D72 | 5 Oct | **Autonomous runs: review failures park, they don't stop the run.** A failed Codex review is fixed and re-reviewed, bookkeeping or substantive, up to 5 reviews of the same brief per run (the first included); then the brief is parked `in-review` with its findings and the run moves on. The loop stops only when no actionable `@code` brief remains, the usage limit is reached, or something unsafe is found. No commit without a Codex pass, ever. Hard-limit actions always ask David. A pre-approved command and edit allowlist in `.claude/settings.json` (edits to AGENTS.md, data-policy and `.claude/` still ask). Replaces D70's single re-review; amends D65 | David's answers Q37–Q40 (brief `D-cowork-8-autonomous-runs`, provisional `D-cowork-8`, renumbered by the lead); David approved the drafts and pre-approved edits in both repos. Runs were ending on small, fixable findings and on prompts for safe commands; the review gate itself is unchanged | A parked brief turns out to hide a real problem the run should have stopped on, or the allowlist lets through something on the hard-limit list |
| D73 | 5 Oct | **Reviewer model: Codex GPT-6.1 Sol (`gpt-6.1-sol`) at effort `high`**, replacing GPT-6 Astra; `ultra` stays the escalation. Set in `~/.codex/review.config.toml` and the AGENTS.md model-policy table. Still a different vendor from the build agents, as D64 requires | David's decision, 5 Oct. Briefs keep `gpt-6-astra` for the rounds it actually ran | The new model's reviews prove weaker or unavailable; David changes it back |
| D74 | 5 Oct | **Second pair of eyes when stuck; "pick up the loop"; accepted risks don't block.** When the same failure or finding returns after 2 attempts, 2 rounds pass without progress, the lead is about to guess, or it is reworking the same files without converging, it consults Codex read-only (or a fresh Claude Code instance) before the next attempt; advice is input, recorded in the brief, not counted toward retries (Q45). "Pick up the loop" from David starts an autonomous lead run per D72, reading the handoff's Cowork → lead section first (Q52). Accepted risks recorded in a brief are passed to the reviewer and don't block (Q53). AGENTS.md, committed `c56bd74`; Cowork's provisional `D-cowork-9`, renumbered by the lead | David's answers Q45, Q52, Q53 (via Cowork). Session 19's P2.2 rounds converged only once Codex was consulted as an adviser, not as a reviewer | Consultations turn into a way of deferring decisions, or accepted-risk lists start to cover blockers |
| D71 | 5 Oct | **One-off exception to the wave-1 gate (D69): four logistics captures may enter `00 Inbox` before P1.4** — kids' school lunch menus, household waste calendar, child A climbing, child A scouts. Minimised per §3a, labelled on the four OQ-20 axes, originals not kept; triage still waits for P1.4. The gate stands for everything else | David wanted the MVP-phone test to answer real family logistics now; a named, bounded exception keeps the gate meaningful instead of quietly opening it. Granted by David via Cowork, recorded by the lead from the handoff | A further capture is added under "the same exception": that would be a second exception, which needs its own answer |
| D75 | 6 Oct | **Temporary §7 exception for `~/Archive/medispring-infi` until P1.3 or 31 Dec 2026; data policy v0.5.** Scoped to that folder only. The boundary there is the configured-roots check (the folder and its ancestors are outside every folder configured for Claude Code, Codex and Cowork, checked by realpath, failing closed) plus the no-access rule (no agent opens, reads, lists, runs git in or links to it). Ends when P1.3 verifies enforcement or on 31 Dec 2026, whichever is first; if P1.3 hasn't verified it by then, David decides again. Recorded per §8 | David's answer Q63 (b), via Cowork, with the exact v0.5 wording approved by him. No check the agents can run proves they are blocked from a folder (they run as David, with shell access), so M2 could move the archive only under an exception or after verified enforcement | P1.3 verifies enforcement (the exception ends); the deadline passes unverified; or any agent touches the archive |
| D76 | 6 Oct | **Repos move to `~/Work`, off iCloud; models stay in Application Support; projects go to `~/Documents/AI Projects/`; the medispring-infi archive goes to `~/Archive`.** Code root `~/Work` absorbs `~/dev`: Dbrain2, dbrain-runtime, claude-blueprint, agentic-ios-app, ui-design-agent, `_external/Equipe-5`, `_archive/agentic-hackathon`. Models stay in `~/Library/Application Support/dbrain/models/` (not iCloud-synced; manifest in git, M1). Lead sessions run from VS Code with only `~/Work` open (Q61) | David's decisions of 6 Oct in brief M2 (Q59–Q64): iCloud sync had produced `* 2` conflict copies inside the vault's `.git` and evicted files (dataless) under agents mid-run; repos need a local, non-synced home | A backup or sync service replaces what iCloud gave (Backblaze is parked); or the Mac mini (D53) becomes the code host |
| D77 | 6 Oct | **Review tiers.** Tier 0 (handoff bookkeeping, frontmatter/link/format fixes, Inbox captures, lint file moves): deterministic checks only, plus a Codex pass until the pre-commit check is installed. Tier 1 (briefs, drafts, specs, skills, eval scripts, runtime code outside the security boundary, notes in 10–40 with no Tier 2 claim, and recording David's answers): Codex pass against `90 System/codex-review-checklist.md`, then commit; Tier 1 notes in 10–40 carry `review_status: codex-reviewed`. Tier 2 (domain claims, decisions David has not yet taken, rule changes, client-facing, security-boundary code, `unverified`, Codex `escalate`): Codex pass and David's batched approval. Only `blocker` findings fail a review. Hard rule 4, "Review before commit", ingest and query now follow the tiers. Calibration: David samples 1 in 5 Tier 1 commits until agreement is at least 90% over 20 samples, then 1 in 10. Replaces the Q40 bullet. AGENTS.md text approved word for word by David (Q65, Q68 (a)); Cowork's provisional `D-cowork-10`, renumbered by the lead | David's answers Q55, Q65 and Q68 (via Cowork). Uniform review was the bottleneck: every change, however trivial, paid the same Codex round and often a David round | Calibration falls below 90%; a Tier 0 or Tier 1 change turns out to have needed David |
| D78 | 7 Oct | **ui-design-agent, claude-blueprint and agentic-ios-app are archived:** moved to `~/Work/_archive/<name>` and archived on GitHub (`David-T13Consulting/UI-Design-Agent`, `CLAUDE-Blueprint`, `agentic-ios-app`; read-only, private). `~/Work` now holds only live projects (Dbrain2, dbrain-runtime) plus `_archive`, `_external`, `_snapshots`. Reversible: move back, `gh repo unarchive` | David's answers Q66 (local move and GitHub archive) and Q71 (a) (the 13 dead `~/.claude/settings.json` lines are exempt), via Cowork. The three are not part of the second-brain work | David wants one of them active again (unarchive and move back) |

---

## Session log

Newest first. One entry per working session — what happened, what changed, where to pick up.

### Session 30 — 7 Oct 2026 · Claude Code, lead loop, M3 done
**Authorization:** "pick up the loop" from David; the handoff's Cowork → lead note of 7 Oct 09:55 releases: commit Cowork's Q71 entry after review, run M3 (step 2 re-check first; stop on any hit outside the Outcome list), close records, clear Q71. Run from VS Code with `~/Work` open. **Ended by stop condition (1):** M3 done; nothing else is actionable under the hold. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile), high, read-only.

**What changed for David:** the three inactive repos are out of `~/Work`'s top level (now in `~/Work/_archive/`) and archived on GitHub (read-only, reversible), so the only active project repos in `~/Work` are the vault and the runtime. Every step of the clean-up run he set on 6 Oct is now done. **The hold stays until he lifts it.**

- **Committed:** `a0e0726` Cowork's Q71 entry (Q71 (a) recorded, M3 step 2 amended, M3 `open`), Tier 1, PASS with no findings · this close.
- **M3 (D78):** pre-flight PASS; step 2 re-check found only the session 29 hits (13 exempt `settings.json` lines, 7 VS Code history entries); moved all three to `~/Work/_archive/`, `git fsck --full` exit 0, heads unchanged; `gh repo archive` for all three, `isArchived=true`. Details in [[90 System/briefs/M3-archive-three-repos|M3]].
- **Codex call hung once:** the first review call made no progress for 41 minutes (0% CPU; stdin left open, output hidden behind a pipe). The lead killed it and reran with stdin closed, output to a file and a 15-minute cap; it passed. Counts as one failed attempt; noted for later runs.
- **Answers recorded and cleared:** Q71 (in M3's Outcome and here).
- **Not pushed:** `a0e0726` and this close. Q65's one push per repo was used in session 29; pushing needs David's OK.
- **Uncommitted, documented:** runtime parked MVP-phone code, `mvp/make-shortcut.sh` (Q56), `experiments/t9_compare.py`; vault `.claude/settings.local.json` is untracked by design.

**Pick up at:** David lifts the hold (via Cowork) and OKs a push of the vault's two commits. Then the Q51 order. Should-fixes waiting: Cowork's course-map refresh, the project-alignment capture at triage, the S2–S6 plan to the Q50/Q51 order (held). David's own tidy of `~/.claude/settings.json` (Q71) whenever he likes.

### Session 29 — 6 Oct 2026 · Claude Code, lead loop, Q65 clean-up run
**Authorization:** "pick up the loop" from David, directly to the lead in this session, with the run's steps listed: verify his Q70 fix; commit his answers; Q55/Q65 step 3 with Q68 (a) (D77); Inbox; one push per repo, no force; M3 per its brief and stop rules; close. Out of scope: the parked MVP-phone code, `.claude/settings.local.json`, T9, P2.5 work, the Q51 order. Run from VS Code with `~/Work` open. **Ended by stop condition (1):** after M3 went `blocked-on-david` (Q71), no actionable `@code` brief remains under the hold. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile), high, read-only.

**What changed for David:** the review tiers he approved are now the rules (D77): bookkeeping will stop waiting on Codex once the pre-commit check exists, and Tier 2 work comes back to him, batched, plus a 1-in-5 sample of Tier 1 commits for calibration. His fix to the project-alignment capture worked: the counterparty is gone and the capture passed review. Everything is pushed to GitHub. **The hold stays:** M3 stopped at its own safety check (Q71), and he set the hold's lift on this run ending clean.

- **Q70:** line 34 of `00 Inbox/2026-10-06-1505-project-alignment-1to1.md` no longer names the counterparty or its agreements (checked by the lead, then by Codex in the Inbox review).
- **Committed:** `9013735` David's answers Q67/Q68, Q70 note (round 1 FAIL: Q70 option (c) implied outside-the-vault was enough under §7; fixed; round 2 PASS) · `7b73210` Cowork's weekly course map and Q69 (PASS; should-fixes for Cowork's next refresh in the commit message) · `4dde18c` AGENTS.md review tiers, **D77** (PASS, every change matches Q65 and Q68 (a) word for word) · `451ed03` Inbox: Q12 scaffold note (`@david` in TASKS), eurouter, project-alignment (PASS) · this close.
- **Pushed (Q65):** Dbrain2 `7b8053d..451ed03`, dbrain-runtime `44abb90..1fd0c53` (the M2 follow-up). Both 0 ahead. This close commit is pushed too, under David's step 6 ("final commit and push").
- **M3:** pre-flight PASS (all three clean, 0 ahead, no stashes); step 2 found 13 `Read` rules and directories for absent ui-design-agent paths in `~/.claude/settings.json` and 7 VS Code recent-workspace entries. Codex, consulted under D74, advised STOP (permission grants in active config; the brief exempts only `settings.local.json`). Nothing moved or archived. **Q71.**
- **Hold:** David's 6 Oct instruction: the 08:57 hold lifts when this run ends clean (all steps done, both repos 0 ahead, only the documented parked items uncommitted). Not met (M3). Not recorded as a decision; the lift is recorded when it happens.
- **Q65 (David, 6 Oct, via Cowork), recorded here:** the AGENTS.md text approved exactly as shown (applied as D77 with Q68 (a)); commit the five Cowork drafts and the M2 follow-up (done in session 28); one push per repo after those commits, no force (done this run); David emptied the `_to_delete` folders and updated the weekly model-review task prompt to `~/Work/Dbrain2` himself; the hold stays until he lifts it after this run.
- **Answers recorded and cleared:** Q65 (above), Q66 (M3), Q67 (P3.0, now `open`, held), Q68 (D-cowork-10, D77), Q70 (here).
- **Uncommitted, documented:** runtime parked MVP-phone code, `mvp/make-shortcut.sh` (Q56), `experiments/t9_compare.py`; vault `.claude/settings.local.json` is untracked by design.

**Pick up at:** Q71 with David (Cowork), then M3 from step 3; then David lifts the hold. Should-fixes waiting: Cowork's course-map refresh, the project-alignment capture at triage, the S2–S6 plan to the Q50/Q51 order (held).

### Session 27 — 6 Oct 2026 · Claude Code, lead loop, M2 done
**Authorization:** David's "I just switched off cowork" after session 26's close, taken as his answer to Q64 (a) and a restart of the loop (D72); Cowork was off, so it came directly to the lead. Run from VS Code with `~/Work` as the working directory. **Ended by stop condition (1)** after M2: no other actionable `@code` brief; everything else is under the 08:57 hold. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile), high, read-only.

**What changed for David:** his repos now live in `~/Work`, off iCloud, with nothing lost: every repo's history, current commit and uncommitted work is identical to before the move, and backups were refreshed first. The medispring-infi archive sits in `~/Archive`, outside every agent folder (checked before it moved; his own file count matches). Obsidian opens the vault at its new place, the phone service runs from the new folder at login, and a phone question was answered from a cited note. The answers were wrong, but the right notes were found: that is the known answer-quality gap (P2.5, T9), not the move.

- **Steps 1–7:** freeze met; snapshots, bundles and tars; eight moves, each after a target-absent check; reachability check PASS; fsck, head and status identical for all six git repos; David's archive check equal (2518 files). Paths rewritten in live text and config only (list in M2); `dbrain/config.py`'s vault default, missed by the brief's grep, found by the tests (3 failures → 191/191 OK). `/health` OK on the Tailscale address. David: Obsidian re-pointed, Login Item added (no old one existed), iPhone question cited a note.
- **Deferred:** the four live `Dbrain2-artifacts` references (the folder hasn't moved yet; the P2.2 note's line on where its runs first wrote is history and stays); Cowork's reconnection (David can't see Cowork in the Claude app, though its VM runs and has `~/Work` open); claude.ai project instructions and the weekly-review task prompt (Cowork); stale `settings.local.json` entries; `~/dev/Agentic hackathon Team/.claude` left in `~/dev`.
- **To commit after the Codex pass:** the vault records and path rewrite in one commit, the runtime `config.py` fix in another (its parked MVP hunks stay uncommitted; HEAD plus the fix alone: 123/123 tests); then one push of each repo, no force. Hashes go in the next session's records.

**Pick up at:** Cowork reconnects (`~/Work/Dbrain2`, `~/Work/dbrain-runtime`; never `~`, `~/Archive` or `~/dev`), updates the claude.ai project text and the weekly task prompt, moves `Dbrain2-artifacts`; the lead then rewrites the four deferred references. Clean-up with David's OK. Then David lifts the hold.

### Session 26 — 6 Oct 2026 · Claude Code, lead loop, M2 stopped at freeze
**Authorization:** "pick up the loop" (D72), scoped by Cowork's update after session 25: review data policy v0.5 with its PROGRESS decision row and the M2 amendment, commit on a pass, then run M2. Run from VS Code with `~/Work` as the working directory. **Ended by stop condition (1):** M2 is `blocked-on-david` (Q64) after its step 1 stop rule; everything else is under the 08:57 hold. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile), high, read-only; the reviews checked the data policy.

**What changed for David:** his §7 exception is now policy: data policy v0.5, decision D75, committed with the final M2 brief (`53e655d`). The move itself stopped at the safety check before anything was touched: the Claude desktop app was open again, and Cowork's virtual machine had files open inside both repos M2 moves. He quits the app, then says "pick up the loop" (Q64).

- **Entry review:** round 1 FAIL (check (ii) let a root inside the archive pass and Cowork's roots weren't realpath-tested; no pre-move collision check, so `mv` could nest into an existing folder or follow a symlink). The lead fixed both and three should-fixes; round 2 PASS. The lead added D75 (below) per §8. Committed `53e655d`.
- **M2:** step 0 met; **step 1 freeze broken** (Claude desktop app started 12:20:21; its VM holds `Dbrain2/.git/objects` and `dbrain-runtime` files open). Stopped per step 1: nothing moved, no snapshot, `~/Archive` not created. Q64 queued.
- **Not done:** M2 steps 2–9, everything under the 08:57 hold.

**Pick up at:** Cowork records Q64; David quits the Claude desktop app (Cmd-Q); "pick up the loop" in the VS Code `~/Work` window → the lead re-checks the freeze and runs M2 from step 2.

### Session 25 — 6 Oct 2026 · Claude Code, lead loop, M2 not started
**Authorization:** "pick up the loop" (D72), scoped by Cowork's update to the 11:45 block: review the reworked M2 amendment; on a pass, commit it and run M2. Run from VS Code with `~/Work` as the working folder. **Ended by stop condition (1):** no actionable `@code` brief left; M2 is `blocked-on-david` (Q63), everything else under the 08:57 hold. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile), high, read-only; the reviews checked the data policy.

**What changed for David:** nothing moved. His Q62 answer (archive to `~/Archive`) and the freeze confirmation are recorded. The review then found the core problem: the agents run as David with shell access, so no check they run can prove they are blocked from the archive, and data-policy §7 requires that now. David decides (Q63): move the other seven folders now and split medispring-infi off (recommended), grant a temporary §7 exception (a policy change under §8), or require verified enforcement first.

- **Amendment review 2: FAIL** (1 of 5 this run). The front-door blocker and the three session 24 should-fixes are resolved. New blockers: the reachability check doesn't prove unreachability; the post-move check and "locks stay for clean-up" gave agents access to the archive. The lead fixed blocker 2 and both should-fixes in Cowork's working-tree brief and proposed a fail-closed check over configured roots (not yet re-reviewed); blocker 1's remainder is David's call (Q63). The close then failed two reviews: Q63 framed a §7 exception as plain risk acceptance and its option (b) overstated the sandbox; then the brief didn't record that round. Both fixed; the third close review (4 of 5 this run) is the one this commit carries. Rounds in M2's Review.
- **Committed:** the lead's records and Cowork's for-david answers (Q62, Q56). The M2 step amendment and the handoff header line stay uncommitted until a review passes.
- **Not done:** M2, everything under the 08:57 hold.

**Pick up at:** David answers Q63 via Cowork; Cowork amends M2 to match (under (a), drop the medispring-infi move; under (b), the §8 decision and policy diff first) and sets `open`; "pick up the loop" → review the amendment, commit on a pass, run M2.

### Session 24 — 6 Oct 2026 · Claude Code, lead loop, M2 not started
**Authorization:** "pick up the loop" (D72), scoped by Cowork's amended 11:45 block in the handoff: (a) review the briefs entry, commit on a pass; (b) run M2 if its status is `open`. Run from VS Code with `~/Work` as the working folder (Cowork's amended step 0, uncommitted; the committed step 0 still says Terminal). **Ended by stop condition (1):** no actionable `@code` brief remains; M2 is `blocked-on-david` (Q62) and everything else is under the 08:57 hold. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile), high, read-only; the review checked the data policy.

**What changed for David:** nothing moved. Before starting M2, the lead had Cowork's new wording for steps 0–1 (VS Code with only `~/Work` open) reviewed. Codex found that M2 would put the medispring-infi archive inside the very folder the agents now work from, although the brief promises no agent access to it. David picks where the archive goes (Q62); then M2 can run.

- **(a) Briefs entry:** already committed in session 23 (`fa1a0f9`). Cowork's later amendment (M2 status comment and steps 0–1, the handoff header's session-location line) was reviewed: **FAIL**, left uncommitted. Blockers: medispring-infi under `~/Work` (Q62); step 1's "check with David" bypasses D68 (Cowork's wording fix). Should-fixes in M2's Review.
- **(b) M2:** `open` on arrival, not started because its amended steps failed review. Freeze state checked read-only: Obsidian, the Claude desktop app, the ChatGPT app and the MVP service not running; a ChatGPT background helper and the VS Code Codex extension's idle app-server running; no process held files in either repo. No snapshot written. Status → `blocked-on-david`.
- **Not done:** M2, everything under the 08:57 hold.

**Pick up at:** David answers Q62 via Cowork; Cowork updates M2 (archive location, freeze confirmation via Cowork, should-fixes) and sets it `open`; David says "pick up the loop" in the VS Code `~/Work` window.

### Session 23 — 6 Oct 2026 · Claude Code, lead loop, M2 brief
**Authorization:** "pick up the loop" (D72), scoped by Cowork's 11:45 amendment in the handoff: (a) review the briefs entry (M2, L1) and commit it on a pass; (b) run M2 only if its status is `open`. **Ended by Cowork's directive,** not one of D72's three stop conditions. M2 is actionable, but David's answer to Q61 puts it in a Terminal session started in `~/Work`, not this VS Code one; everything else is under the 08:57 hold. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile), high, read-only; every review checked the data policy.

**What changed for David:** the M2 brief (the move off iCloud) is reviewed and committed, with his push approval (Q60) in it. The move itself didn't start. Step 1 has him quit VS Code, but the lead runs inside VS Code from the folder being moved. He chose (Q61): Claude Code in Terminal, started in `~/Work`.

- **Briefs entry (M2, L1, Q60 answer, handoff header):** round 1 FAIL (`log.md` and closing records outside M2's scope; step 4's status diff compared against a file that also held the hash). The lead fixed both blockers and the four should-fixes in Cowork's handoff files rather than return them, since David was at the Mac. Round 2 PASS, committed `fa1a0f9`. Round 2's two should-fixes are recorded in M2's Outcome.
- **M2:** `open` on arrival; freeze check failed (VS Code, Claude desktop app, ChatGPT/Codex app running; Obsidian and the MVP service stopped). Nothing moved, no snapshot written. Q61 queued, then answered by David via Cowork during the close (Terminal in `~/Work`); recorded in M2 (step 0), M2 back to `open`.
- **Not done:** M2, everything under the 08:57 hold.

**Pick up at:** David quits VS Code, the Claude desktop app and the ChatGPT app, opens Terminal, `cd ~/Work && claude`, says "pick up the loop" → M2 from step 0.

### Session 22 — 6 Oct 2026 · Claude Code, lead loop, M1 remainder
**Authorization:** "pick up the loop" (D72), scoped by Cowork's 10:50 amendment in the handoff: finish M1 if Q57 and Q58 are answered (both were, (a)), review the briefs entry (M1, M2, L1) and commit it on a pass, then stop. **Ended by that directive**, not by one of D72's three stop conditions. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile), high, read-only; every review checked the data policy.

**What changed for David:** everything in M1's scope is now backed up on private GitHub, including ui-design-agent's 31 leftover files and a manifest that lets the four local models be downloaded again and verified by hash. M2 (the move off iCloud) can't lose committed work. Its brief still needs Cowork's fixes and David's answer on pushing (Q60).

**Did:**
- **M1 remainder:** `models/MANIFEST.md` and `.DS_Store` ignore in dbrain-runtime (`6c7763e`, Codex PASS, its license should-fix applied); ui-design-agent's 31 entries committed as they are (`d4dfc44`, Codex PASS); both pushed, no force. Secret scans clean. Gate met; M1 `done` (counts in the brief).
- **Briefs entry (M1, M2, L1): Codex FAIL** on re-review. Prior findings 2–8 resolved; finding 1 (M1 step 2 said "commit") fixed by the lead. New blockers, all in M2: push approval scope (Q60), `~/Work/_snapshots/` outputs not in Files in scope, medispring-infi inspected despite being move-only. **M1 is committed with this close; M2 and L1 go back to Cowork, uncommitted.**
- **Queued for David:** Q60. Q57 and Q58 recorded in M1 and cleared from the queue.
- **Not done:** M2, L1, everything under the 08:57 hold.

**Pick up at:** Cowork fixes M2 (three blockers, one should-fix) and L1 (two should-fixes) → one fresh review → commit. David answers Q60. Then M2 with David present.

### Session 21 — 6 Oct 2026 · Claude Code, lead loop, M1 only
**Authorization:** "pick up the loop" (D72), scoped by Cowork's 10:05 release in the handoff: brief M1 to its gate, plus the briefs entry (M1, M2, L1) on a Codex pass; nothing else. **Ended by that directive** (run M1 to its gate, then stop), not by one of D72's three stop conditions. **The gate is not fully met:** ui-design-agent keeps 31 uncommitted files (Q58) and dbrain-runtime an undocumented `.DS_Store`; M1 is `blocked-on-david`.

**What changed for David:** GitHub now holds a private copy of the vault's 50 unpushed commits (plus this run's), the runtime code (new private repo `dbrain-runtime`) and the claude-blueprint leftovers. So the move off iCloud (M2) can't lose committed work. **Not backed up:** ui-design-agent's 31 leftover files, because a test fixture may contain a real patient's name (Q58), and the parked uncommitted work (it moves with `mv` in M2).

**Did:**
- **M1 step 1:** re-check matched Cowork's snapshot except two covered cases (brief Outcome).
- **B1 bookkeeping** (session 20, the 6 Oct findings fixed): Codex PASS, committed `1c5038c`.
- **Secret scans** clean on every range and file set pushed.
- **Pushed:** `dbrain-runtime` to the new private repo (`main`, `c8b3b7b`); claude-blueprint `3ed6463` on `feature/new-branch` (Codex PASS); the vault with this close commit.
- **Briefs entry (M1, M2, L1): Codex FAIL**, 4 blockers (mid-brief commits; manifest outside scope; review limited to scope and secrets; M2 asks David directly). Back to Cowork, uncommitted. The lead ran M1 within those findings: full data-policy review on every item, no manifest.
- **ui-design-agent: Codex FAIL** on the fixture; not committed, not pushed (Q58).
- **Queued for David:** Q57 (model manifest scope), Q58 (the fixture).
- **Not done (outside the release):** Cowork's new `.claude/settings.json` handoff entry (permission settings; not in the 10:05 release); M2; everything under the 08:57 hold.

**Pick up at:** David answers Q58 (and Q57) via Cowork → the lead finishes M1 for ui-design-agent. Cowork fixes the M1/M2/L1 blockers → one fresh review → commit. Then M2 with David present.

### Session 20 — 5–6 Oct 2026 (night to morning) · Claude Code, lead loop; stopped for clean-up
**Authorization:** "pick up the loop" (D72). **Ended by David's directive of 6 Oct 08:57** (handoff ⛔ block, brief L1): finish the current step, do L1 phases 0–1 only, then stop. Not one of D72's three stop conditions; David's directive overrides the run.

**What changed for David:** the query service under the phone (P2.2) is committed at last (runtime `c8b3b7b`), so the code that answers is now versioned and reviewed. **The phone itself is unchanged:** the date fix ("menu tomorrow") is built but parked after its fifth failed review, so his Shortcut still runs yesterday's code.

**Did:**
- **P2.2:** round O's two findings accepted as risks (Q53); round P failed on two false sentences in the bookkeeping, fixed; **round Q PASS** (Codex `gpt-6.1-sol`, high, read-only). Committed: runtime `c8b3b7b` (first commit), vault `4b5e91f`.
- **Handoff entries reviewed (one batch):** Q54 settings `377757e`, AGENTS.md Q45/Q52/Q53 (D74) `c56bd74`, Q46 `d4fae04` passed and were committed. P2.5, P4.1, P3.0 briefs and Q13 failed on blockers (findings in the Lead → Cowork note in the handoff).
- **MVP-phone:** review rounds 5–9 on the runtime code (display fixes, date awareness). Rounds 5–8's blockers were fixed; round 9's three are open; after round 7 the lead consulted Codex (D74) and redesigned logging (only server-generated text in logs and error replies) and date reading (components, composition, "unclear" asks again, the asked date always stated). Round 9, the fifth, failed on three more date forms → **parked**, uncommitted (brief). `mvp/make-shortcut.sh` is left out: it writes the token into temporary files (Q56 for David).
- **T9 (started before the stop directive):** pre-download manifest; the three named models downloaded from pinned revisions and hash-verified (disk 15.65 GB (decimal; the four model files 15.59 GB, runtime copies 0.06 GB) of the 20 GB budget; Qwen3.5-4B re-fetched because `/private/tmp` had been cleared); all four load on b11146; Qwen3.5 needs the server's `--reasoning off`. The 9-block run was **stopped after 2 blocks** on David's directive: no result, evidence kept in `dbrain-runtime/artifacts/t9-2026-10-06/`.
- **L1 Phase 0:** 0 dataless files after forcing the 12 `* 2` copies local; `git fsck --full` exit 0 in both repos (no missing or corrupt objects; vault: 316 dangling blobs, 16 dangling trees, 1 dangling commit, plus "bad sha1 file" for the 12 `* 2` names; runtime: 74 dangling blobs); all 12 `* 2` copies identical to their originals; bundles of both repos verified in `~/Work/_snapshots/`; uncommitted files copied there with their paths.

- **L1 Phase 1 (6 Oct):** handoff reconciled with git; D-e and D-c applied as David approved; one Codex batch review with a verdict per item. **Committed:** MVP-phone parked record + Q56 `5117908` · AGENTS.md `D-cowork-9` → `D74` `e00c4a4` · the four wave-1 captures, lunch with D71 `b7db7da`, waste `28d3697`, climbing `88eef41`, scouts `a53a6d7`. **Parked, uncommitted:** this bookkeeping (B1: handoff reconcile, this entry, D74 row, header, P2.2 `done`, TASKS, Q13–Q17), after five reviews, each on a different inaccurate statement, all fixed: §3a values quoted in lead handoff text; a missing Lead → Cowork note; the fsck summary; the disk figure; a session 19 claim. **Failed, back to Cowork:** L1 brief, the 5 Oct lint log entry, D-cowork-10 + checklist + Q55, P2.5/P4.1/P3.0 with Q47–Q51 (findings in the handoff note). *(Later on 6 Oct: the lint entry, fixed by Cowork, passed a fresh review and is committed, `0f81cac`.)*

**Incident (lead):** the round 7 bookkeeping for MVP-phone ran inside a backgrounded command, stopped on an assertion and went unnoticed, so rounds 7–8 were missing from the brief until round 9's review caught it. Bookkeeping edits now run in the foreground and are checked.

**Pick up at (after David lifts the stop):** L1 Phase 2 (with David present) → MVP-phone (consult first; the parked brief's note) → Q51 order. Uncommitted items and why: the Lead → Cowork note of 6 Oct in `90 System/handoff.md`.

### Session 19 — 5 Oct 2026 (late evening) · Claude Code, lead loop
**Authorization:** "pick up the loop" (autonomous run per D72; Cowork's handoff directives Q46 read first).

**What changed for David:** the phone's "What's on the menu tomorrow?" now answers correctly in testing (Tue 6 Oct, cites the lunch note), and every dated answer starts with its date. **This isn't on his phone yet:** nothing could be committed, because the query service under it (P2.2) was parked after five reviews this run, four of them failed (round L passed before Q46 changed the check). The label check behind it is now an allowlist that skips odd notes instead of stopping every question (Q46).

**Did:** P2.2 rounds K–O (Codex `gpt-6.1-sol`, high, read-only): after K failed, consulted Codex (D-cowork-9) and redesigned the label check as an allowlist (round L passed); applied Q46 (skip and trace; a recognisable `client` label still stops); rounds M, N and O failed on progressively narrower forms → **parked**, two findings open (brief). MVP-phone: date awareness in `serve.py`, tests on a fixed date, smoke run d on the real model (p50 9.9 s, p95 13.0 s, 11/14 expected). Handoff note to Cowork; Q52 queued.

**Incident:** a lead script emptied `TASKS.md` (opened for writing before reading); restored from `f9c014e` and the lead's edits reapplied; no other work lost.

**Pick up at:** P2.2 round O findings (brief) → one review → first `dbrain-runtime` commit → MVP-phone review and merge (display fixes + dates) → Cowork's Q51 order (voice step A, P2.5 …). Nothing from this session is committed.

Superseded the same evening: session 20 passed round Q and committed P2.2 (`4b5e91f`, runtime `c8b3b7b`).

### Session 14 — 2 Oct 2026 · Claude Code, lead loop
**Authorization:** David: "pick up the loop."

**Did:** finished session 13's interrupted integration commit (`01562e1`, the D63–D65 renumbering), committed Cowork's queued briefs verbatim (`2092ff2`), cleared the queue and tagged the first owners (`8fb68d0`). Then **restored the review gate** and ran it: Codex (`gpt-6-astra`, effort `high`, read-only) reviewed the three commits and this session's D64 diff.

**Found:** the review gate could not be run from the command `AGENTS.md` documents, and the cause was `PATH`. The `codex` CLI is not missing; it ships inside the ChatGPT desktop app at `/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex` (0.159.2), and `~/.codex/review.config.toml` already existed from 1 Oct. The profile looked absent because 0.159.2 moved profiles out of `config.toml` into separate `<name>.config.toml` files. Two things stay separate here: session 13 *did* run reviews, so the gate was never dead, but it was not reproducible from the documented command — and whether the profile *complies* with the policy is still open, since it runs effort `high` where `AGENTS.md` says the highest. Also found: three commits in this session were made **before** the gate was restored, so Codex reviewed them after the fact rather than before; its findings are recorded and nothing in them was a blocker.

**Decided:** nothing new. D63–D65 were David's decisions of 1 Oct and are only now recorded in this log — the gap Codex's review flagged.

**Blocked, for David:** D64 cannot close (two blockers: `high` versus "highest" effort, and the documented `codex exec --profile review` command not working as typed). D65 waits on D64. **P2.2 cannot start** — its Step 0 requires D65 landed, and Codex raised a blocker on the brief itself: it directs creating a repository it says is not yet authorised.

**Also landed late in the session:** Cowork's taxonomy v2 proposal (D67, brief T3.4), committed verbatim then renumbered. It is a proposal, not a change — and it must not touch `classify-session/` or `session-types.md` until batch 04 is scored under v1.4, which is the last held-out test of the v1 schema.

**Pick up at:** **P2.2** — the scoped read-only query service. Its gates are cleared: D63, D64, D65 and D68 are in force, and David authorised `~/Documents/dbrain-runtime/`. Also unblocked: **T3.4** (taxonomy v2), now that the v1 held-out test is closed. No session-14 question waits on David, though his standing actions remain (OQ-20 before P1.4, the D53 host purchase, the D60 weekly-review evidence). `P2.1-review` part A can go to Codex; T3.4 is `@cowork`'s.

### Session 13 — 1 Oct 2026 · Claude Code, orchestration adoption
**Authorization:** David approved the orchestration proposal and the model policy, and asked for them to be adopted.

**Did:** committed Cowork's three handoff entries verbatim (`08ea191`, `1931d8e`, `892146e`), splitting `AGENTS.md` and `_template.md` hunk by hunk because they held edits belonging to two entries, then cleared the queue (`27ef6be`). Ran the first Codex review and recorded five should-fix findings in the D63 brief. Set up `~/.codex/review.config.toml`.

**Did not finish:** the integration commit was staged but never made, the session-close bookkeeping (this log, `log.md`, `index.md`, owner tags) was never written, and the D64 and D65 briefs were left with empty Review and Outcome sections while the D63 brief pointed at them. Session 14 closed the commit, the bookkeeping and the dangling pointers. Still open from D63: the owner tags, and D64's two questions.

### Session 12 — 1 Oct 2026 · Claude Code, S1 requirements interview
**Authorization:** David asked to pick up the implementation plan, then to run the P1.2/P1.3 questions as a structured interview and record the result.

**Did:** pushed the backlog to `origin/master`. Found four uncommitted Cowork entries in the handoff queue and committed them first, per the multi-agent rules — three commits (`a588bed` D51 move, `667902e` Product School, `2db69fc` both NN/g rounds), splitting `index.md`, `log.md`, `PROGRESS.md` and `OPEN_QUESTIONS.md` hunk by hunk and verifying the tree byte-identical to Cowork's versions afterwards. Queue cleared (`45750ad`). Then ran the twelve-question P1.2/P1.3 interview and recorded D52–D62.

**Found:** `D50` was recorded in `log.md` and `AGENTS.md` but never indexed in this decision log — row added. `D51` and `OQ-19` were already taken by Cowork's concurrent session, so this session's decisions are D52–D62 and its new question is OQ-20.

**Decided:** D52–D62. S1 requirements are closed; the only open S1 item is the host purchase.

**Flagged, not resolved:** the < 5 s voice target is the likeliest to break (D56). `classification` may need splitting into four axes before the D59 schema is retrofitted (OQ-20). T9 was rewritten because D53 had already decided the question it was asking.

**Pick up at:** S2 — P2.2, the scoped read-only query service, measured against D56.

### Session 11 — 1 Oct 2026 · Claude (Cowork), knowledge ingest
David overrode the "propose, don't populate" rule and chose `public` classification. Ingested the three Product School courses (AI Product Strategy, Advanced Agents, Product Strategy) as 11 own-words notes in `30 Resources/Product School/`, and six NN/g conference decks (2015–17) plus 2025–26 nngroup.com articles as 7 notes in `30 Resources/NNg UX/`. `index.md`, `log.md` and `90 System/handoff.md` updated; links and secret scan verified. Flagged: the Advanced Agents PDF contains live credentials (revoke and redact). Not done: Apple Notes Vibe Coding, AI Product Management, ProdSchool - MCPs (unreadable; need PDF export); NN/g journey mapping, personas, workshops, persuasion, lean UX decks. Uncommitted: awaits git agent via handoff.

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
