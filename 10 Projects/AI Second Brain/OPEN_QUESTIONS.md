---
classification: internal
---
# Open Questions

**Updated:** 1 Oct 2026 · Open questions block work. Resolve them or explicitly park them.

---

## 🔴 Blocking

No blocker to the read-only hardware inventory. Device/availability requirements and acceptance targets block final service design, not planning or bounded experiments. See OQ-4/OQ-14/OQ-15.

## 🟡 Needed soon

### OQ-18 · Activate weekly model review and bound local benchmarking
**Affects:** M4/M6 · **Owner:** David for scheduler access and resource preferences; assistant for task setup when available. Weekly source/benchmark review is requested. Procedure and task prompt are ready in [[90 System/weekly-local-model-review]], proposed Thursday 09:00 Europe/Brussels. No scheduler tool is exposed here, and desktop app access was denied. Activate in the desktop local-project scheduler and verify its first run; do not describe the checklist as active automation. Decide a time/download/storage budget before recurring local model downloads or compute-heavy comparisons. Until then weekly research can update published results and propose bounded tests, not silently upgrade models.

### OQ-17 · SAFe knowledge base: licence and currency before client use
The SAFe pages are built from lapsed-licence 5.1 toolkits (own-words synthesis, `internal`). Before any client-facing use: re-obtain current assets (SAFe membership / SPC)? And verify AI-Native SAFe (June 2026) and the 2024+ Disciplines against framework.scaledagile.com. Owner: David. See `30 Resources/SAFe/sources.md`.

### OQ-3 · Colleague for a future two-person test (parked)
**Affects:** T10 after S6 · **Owner:** David. Additional human users no longer precede multi-agent work. Revisit when the personal service is reliable; no simulated multi-user claim in the initial demo.

### OQ-4 · Current Mac hardware and capacity
**Resolved 1 Oct by read-only measurement:** M2, 24 GiB RAM, 8 CPU cores; about 90 GiB free before download. Initial local benchmark ran successfully but exposed answer-quality failures. See [[10 Projects/AI Second Brain/02_Architecture/local-benchmark-2026-10-01|measurement record]]. Model selection, availability and sustained performance remain open; no purchase proposed.

### OQ-14 · Devices, access and host availability
**Blocks:** final S2/S4 design · **Owner:** David, P1.2. Which phone/tablet/laptop operating systems must work? Must the service run while the Air travels or sleeps? Working architecture is one controlled inference host with remote clients and offline capture; confirm availability expectations and any stricter offline-inference requirement.

### OQ-15 · Time, budget and measurable service targets
**Blocks:** calendar commitments and acceptance runs · **Owner:** David, P1.2/P1.3/T6. Weekly build time, possible hardware budget, acceptable query/voice latency, recovery time and tolerable data loss remain unspecified. Define numeric targets before acceptance runs; December remains a target, not a validated schedule.

### OQ-16 · What counts as quality work in F3?
**Blocks:** P3.5 rule change only · **Owner:** David. The weekly script flags no quality for `long` + `tempo_block`. The flag is broader than strict tempo and also occurs on easy runs. Decide the qualifying evidence before changing F3; preserve and version historical expectations.

### OQ-5b · Is the Vibe Coding deliverable still active?
**Blocks:** nothing today, but determines whether a second workstream needs planning
**Owner:** David
Project scope now formally covers both workstreams (D10). What's still unknown is whether the Vibe Coding app + deck is live work, already delivered, or abandoned. If it's live, it needs its own tasks and timeline — the tool stack (Lovable / Supabase) shares nothing with the second-brain build.

---

### OQ-6 · Is LTHR really 166?
**Blocks:** nothing directly, but batch 02 (cause B) suggests it matters: 20 km de Bruxelles averaged 163 for 96 min
**Owner:** David · a 30-min solo all-out effort (LTHR = average HR of the last 20 min). Re-check zones against the golden dataset afterwards.

### OQ-7 · Should the post-race recovery window scale with race size?
**Affects:** rubric I6 (current D27: 7 days after races up to 21 km; 14 after marathon/ultra/mountain). The former flat-window description was stale.
**Owner:** decide from held-out batches. If short races (10 km) wrongly turn easy runs into "recovery", scale the window by km-effort.

### OQ-8 · Project instructions in claude.ai are stale — ✅ RESOLVED 1 Oct 2026 (David pasted the revised text; vault path, Source_Material location and D50 git convention)
**Owner:** David · they still point to `~/Desktop/AI_SecondBrain_Project/`; the vault has been `~/Documents/Dbrain2/10 Projects/AI Second Brain/` since 8 Sep. Replacement text is at the bottom of the project doc `claude/ai-second-brain-project.md`.

### OQ-11 · Second domain: family logistics inputs (parked)
**Blocks:** nothing in S1–S6; additional production domains remain parked · **Owner:** David. Context: `00 Inbox/2026-09-30-1447-assistant-scope-ideas.md`
- Where does each source live (commune trash calendar, school menus, kids' activity schedules: site, portal, email)?
- Who else would use it if the deferred multi-user extension is taken up?
- David's rule on children's data (proposal: minimised, first names/initials only, never demoed; synthetic family for demos)

### OQ-12 · Wiki versus domain showcase — resolved 1 Oct
D47: running remains the established domain; supervised wiki maintenance is shared platform work. Demonstrate the complete lifecycle, with a small synthetic professional example at S6. This is the explicit scope amendment, not an additional production domain.

### OQ-13 · Durable source storage, retention and schema
**Partly resolved 1 Oct (D49, David):** the wiki covers the entire vault (PARA + 90 System). Triage moves the processed content to Projects/Areas/Resources/Archive/System by purpose; the verbatim capture moves untouched to `40 Archive/Inbox/` and the new note cites it in `source:`. Moves happen only at requested triage.
**Still open:** retention/deletion (incl. audio, backups), stable IDs, minimum metadata.
**Blocks:** P3.1 implementation; design in P1.3 · **Owner:** David. The amended plan preserves source evidence after approved triage and covers approved knowledge across PARA, with 90 System as schema/policy. Still choose the physical source location, retention/deletion rules (including audio and backups), stable IDs and minimum metadata. No automatic move to `40 Archive/raw`; inbox items remain untouched until requested triage.

---

## Resolved

| # | Question | Answer | Date |
|---|---|---|---|
| R10 | (was OQ-10) Rubric v1.4 questions from batch 03 | G1 altitude mountain (D35) · G2 25 m/km (D39) · G3 broad flag / strict tempo (D36) · G4 uphill reps = hills (D37) · G5 long = over 15 km, long + tempo allowed (D40) · G6 misclick relabel (D38) | 30 Sep |
| R9 | (was OQ-9) Rubric v1.3 questions from batch 02 | A recovery post-race only (D27) · B two labels + race-pace tempo (D28, D29), HR off-road (D32) · C `vertical` flag (D31) · D unknown gear = no gear · E hikes aren't runs (D30) | 30 Sep |
| R8 | (was OQ-2) What does the firm's AI policy say? | No firm above Tower13. David's rule (D16): every contract must state his AI agent use explicitly, or the engagement stays out. Follow-up is T0.7 | 29 Sep |
| R7 | (was OQ-1) What is the showcase workflow? | **"Classify each run's session type from raw Strava data, roll a week into a coaching assessment — trend, effort adequacy, race-goal trajectory."** H1 = classification + trend/effort (checkable core). H2 = goal-trajectory judgment with confidence bands. Ground truth for the golden dataset comes from David labeling his own historical runs | 8 Sep |
| R1 | Showcase format? | Live system I drive, screen-shared | 7 Sep |
| R2 | "Collaborative" — which sense? | Original: humans first; amended by D45 on 1 Oct to multi-device personal service, then agents, additional humans later | 7 Sep / 1 Oct |
| R3 | Which sector to anchor security on? | Generic but strict, specialise later | 7 Sep |
| R4 | Timeline to client-ready? | 3 months | 7 Sep |
| R5 | Can Claude reach Apple Notes? | No — protected location, no API, no connector. Export to markdown is the route (and the better answer anyway) | 7 Sep |
| R6 | (was OQ-5) Does the Claude Project cover the second brain, or only Vibe Coding? | **Both.** Scope updated to carry two workstreams, second brain primary. Residual question about Vibe Coding status tracked as OQ-5b | 7 Sep |
