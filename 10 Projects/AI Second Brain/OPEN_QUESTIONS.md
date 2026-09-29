# Open Questions

**Updated:** 29 Sep 2026 · Open questions block work. Resolve them or explicitly park them.

---

## 🔴 Blocking

*Nothing currently blocking.*

## 🟡 Needed soon

### OQ-3 · Is a colleague available for the week-10 two-person test?
**Blocks:** T10 design (multi-user layer)
**Owner:** David
If not, I'll design a single-user simulation of the multi-user layer instead — weaker, but workable. Decide by week 8.

### OQ-5b · Is the Vibe Coding deliverable still active?
**Blocks:** nothing today, but determines whether a second workstream needs planning
**Owner:** David
Project scope now formally covers both workstreams (D10). What's still unknown is whether the Vibe Coding app + deck is live work, already delivered, or abandoned. If it's live, it needs its own tasks and timeline — the tool stack (Lovable / Supabase) shares nothing with the second-brain build.

---

### OQ-6 · Is LTHR really 166?
**Blocks:** nothing, but zones stay provisional
**Owner:** David · a 30-min solo all-out effort (LTHR = average HR of the last 20 min). Re-check zones against the golden dataset afterwards.

### OQ-7 · Should the post-race recovery window scale with race size?
**Affects:** rubric I6b (currently a flat 14 days after any race)
**Owner:** decide from held-out batches. If short races (10 km) wrongly turn easy runs into "recovery", scale the window by km-effort.

### OQ-8 · Project instructions in claude.ai are stale
**Owner:** David · they still point to `~/Desktop/AI_SecondBrain_Project/`; the vault has been `~/Documents/Dbrain2/10 Projects/AI Second Brain/` since 8 Sep. Replacement text is at the bottom of the project doc `claude/ai-second-brain-project.md`.

## 🟢 Nice to know

### OQ-4 · How much RAM does the MacBook Air have?
**Affects:** whether a local-inference story is available for the demo
**Owner:** David · one command: `system_profiler SPHardwareDataType | grep Memory`
My recommendation is against local inference for a live demo regardless — the Air is fanless and throttles under sustained load — but it's your call.

---

## Resolved

| # | Question | Answer | Date |
|---|---|---|---|
| R8 | (was OQ-2) What does the firm's AI policy say? | No firm above Tower13. David's rule (D16): every contract must state his AI agent use explicitly, or the engagement stays out. Follow-up is T0.7 | 29 Sep |
| R7 | (was OQ-1) What is the showcase workflow? | **"Classify each run's session type from raw Strava data, roll a week into a coaching assessment — trend, effort adequacy, race-goal trajectory."** H1 = classification + trend/effort (checkable core). H2 = goal-trajectory judgment with confidence bands. Ground truth for the golden dataset comes from David labeling his own historical runs | 8 Sep |
| R1 | Showcase format? | Live system I drive, screen-shared | 7 Sep |
| R2 | "Collaborative" — which sense? | Humans sharing first, multi-agent second | 7 Sep |
| R3 | Which sector to anchor security on? | Generic but strict, specialise later | 7 Sep |
| R4 | Timeline to client-ready? | 3 months | 7 Sep |
| R5 | Can Claude reach Apple Notes? | No — protected location, no API, no connector. Export to markdown is the route (and the better answer anyway) | 7 Sep |
| R6 | (was OQ-5) Does the Claude Project cover the second brain, or only Vibe Coding? | **Both.** Scope updated to carry two workstreams, second brain primary. Residual question about Vibe Coding status tracked as OQ-5b | 7 Sep |
