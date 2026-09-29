# Open Questions

**Updated:** 29 Sep 2026 · Open questions block work. Resolve them or explicitly park them.

---

## 🔴 Blocking

*Nothing currently blocking.*

## 🟡 Needed soon

### OQ-2 · What does your firm's AI policy actually say?
**Blocks:** final version of `data-policy.md` §6 (v0.1 done 29 Sep), governance one-pager (T8)
**Reframed 29 Sep:** David is independent (Tower13), so there's no firm policy above him. The real input is the AI/subprocessor clauses in his live contracts. David reads them himself: under data-policy §5 the contract text must not go to a model API.
**Owner:** David — I cannot research this
Also: scan two live client contracts for AI / subprocessor clauses. Constrains the standing rule on client data.

### OQ-3 · Is a colleague available for the week-10 two-person test?
**Blocks:** T10 design (multi-user layer)
**Owner:** David
If not, I'll design a single-user simulation of the multi-user layer instead — weaker, but workable. Decide by week 8.

### OQ-5b · Is the Vibe Coding deliverable still active?
**Blocks:** nothing today, but determines whether a second workstream needs planning
**Owner:** David
Project scope now formally covers both workstreams (D10). What's still unknown is whether the Vibe Coding app + deck is live work, already delivered, or abandoned. If it's live, it needs its own tasks and timeline — the tool stack (Lovable / Supabase) shares nothing with the second-brain build.

---

## 🟢 Nice to know

### OQ-4 · How much RAM does the MacBook Air have?
**Affects:** whether a local-inference story is available for the demo
**Owner:** David · one command: `system_profiler SPHardwareDataType | grep Memory`
My recommendation is against local inference for a live demo regardless — the Air is fanless and throttles under sustained load — but it's your call.

---

## Resolved

| # | Question | Answer | Date |
|---|---|---|---|
| R7 | (was OQ-1) What is the showcase workflow? | **"Classify each run's session type from raw Strava data, roll a week into a coaching assessment — trend, effort adequacy, race-goal trajectory."** H1 = classification + trend/effort (checkable core). H2 = goal-trajectory judgment with confidence bands. Ground truth for the golden dataset comes from David labeling his own historical runs | 8 Sep |
| R1 | Showcase format? | Live system I drive, screen-shared | 7 Sep |
| R2 | "Collaborative" — which sense? | Humans sharing first, multi-agent second | 7 Sep |
| R3 | Which sector to anchor security on? | Generic but strict, specialise later | 7 Sep |
| R4 | Timeline to client-ready? | 3 months | 7 Sep |
| R5 | Can Claude reach Apple Notes? | No — protected location, no API, no connector. Export to markdown is the route (and the better answer anyway) | 7 Sep |
| R6 | (was OQ-5) Does the Claude Project cover the second brain, or only Vibe Coding? | **Both.** Scope updated to carry two workstreams, second brain primary. Residual question about Vibe Coding status tracked as OQ-5b | 7 Sep |
