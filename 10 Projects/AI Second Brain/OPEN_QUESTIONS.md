# Open Questions

**Updated:** 7 Sep 2026 · Open questions block work. Resolve them or explicitly park them.

---

## 🔴 Blocking

### OQ-1 · What is the showcase workflow?
**Blocks:** all of H1 (skills, golden dataset, evals — everything downstream)
**Owner:** David · **Task:** T0.4

The single most consequential decision in the plan. Criteria:
- Genuinely recurrent (you actually do it repeatedly)
- Has a **checkable right answer** — without this, no golden dataset is possible, and without a golden dataset there is no showcase
- Legible to a client in under 30 seconds
- Demonstrable with **no** client-confidential data

*Good shape:* "turn a messy discovery-call transcript into a structured findings memo in my house format."
*Bad shape:* "help me think" — unmeasurable, undemoable.

**8 Sep — partially resolved (D14):** domain chosen — fitness / running / trail running, evidence-led
from David's actual recent topics rather than guessed. **Still open:** the precise task shape
(input → output). Continuing now.

---

## 🟡 Needed soon

### OQ-2 · What does your firm's AI policy actually say?
**Blocks:** `data-policy.md` (T0.5), governance one-pager (T8)
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
| R1 | Showcase format? | Live system I drive, screen-shared | 7 Sep |
| R2 | "Collaborative" — which sense? | Humans sharing first, multi-agent second | 7 Sep |
| R3 | Which sector to anchor security on? | Generic but strict, specialise later | 7 Sep |
| R4 | Timeline to client-ready? | 3 months | 7 Sep |
| R5 | Can Claude reach Apple Notes? | No — protected location, no API, no connector. Export to markdown is the route (and the better answer anyway) | 7 Sep |
| R6 | (was OQ-5) Does the Claude Project cover the second brain, or only Vibe Coding? | **Both.** Scope updated to carry two workstreams, second brain primary. Residual question about Vibe Coding status tracked as OQ-5b | 7 Sep |
