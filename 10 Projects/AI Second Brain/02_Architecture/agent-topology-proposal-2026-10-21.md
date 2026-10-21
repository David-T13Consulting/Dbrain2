---
classification: internal
domain: ai-second-brain
sensitivity: ordinary
sharing: private
source: Cowork session with David, 21 Oct 2026 (web research; David's decisions in session)
created: 2026-10-21
updated: 2026-10-21
review_status: approved
note_type: proposal
owner: "@david"
status: approved
---
# Agent topology: one router, one agent, skills (proposal, 21 Oct 2026)

**Status: approved by David 21 Oct 2026 (option A), recorded as D142; the evidence table and revisit rule approved as Tier 2 content (Q145, session 53).** Follow-ups Q-cowork-21a to 21c answered by David 21 Oct ~14:15 (see below and [[90 System/for-david|for-david]]). Builds on [[10 Projects/AI Second Brain/02_Architecture/sovereignty-router-proposal-2026-10-19|sovereignty router proposal]] (D135, D138) and the OQ-20 axes.

## David's idea (21 Oct, stated in session)
One organiser agent, with sub-agents per confidentiality level: public handled by Claude, private by a hosted agent, critical by a local agent. Possibly many role agents: coder, reviewer, organiser, email manager, calendar manager, writer, designer, software architect, business sounding board.

## Diagnosis (Cowork)
The idea mixes three independent axes:

| Axis | Question | Where it already lives |
|---|---|---|
| Trust boundary | Where may this data be processed? | Sovereignty router L0–L3, ceiling by rules only (D135, D138) |
| Capability | What job is being done? | Skills in `90 System/skills/` |
| Build vs runtime | Does this agent build the system or run inside it? | Build lanes in AGENTS.md (Cowork, Claude Code, Codex); runtime agents not yet defined |

Flaws in the idea as first stated:
1. An LLM organiser must read a request to route it. If it runs on Claude, critical data has left the Mac before routing. Router rule 3 (classifier at the floor level) exists for this. The organiser must be deterministic or run at L0.
2. Critical work would get the weakest model unless chosen deliberately (see David's answer 2).
3. Email and calendar are mainly an injection problem: untrusted input, private data and actions in one agent. Current answer: a quarantined reader with no tools that returns structured fields (dual-LLM / CaMeL pattern).

## Evidence (state of the art, as of Oct 2026)
| Finding | Source |
|---|---|
| Multi-agent earns its cost only for context pollution, parallel work, or specialised tools; otherwise coordination costs exceed benefits | Anthropic, "Building multi-agent systems: when and how to use them" (2026) |
| Role-based decomposition (planner, coder, reviewer) is often counterproductive: information degrades at each handoff. Split along context boundaries instead | Same |
| Multi-agent uses about 3–10x the tokens of a single agent for the same task | Same |
| Verification subagents are a recommended exception | Same |
| Sequential tasks degraded 39–70% under every multi-agent variant tested; parallel tasks improved about 81% | Google Research / MIT, "Towards a science of scaling agent systems" (arXiv 2512.08296) |
| Independent agents amplify errors 17.2x; a central coordinator holds it to 4.4x | Same |
| Isolation, not prompting, is the reliable defence against prompt injection for agents reading untrusted content | DeepMind CaMeL; Simon Willison's analysis |

## Options considered
| | A. Router + one agent + skills (**chosen**) | B. Coordinator + worker per tier | C. Role-agent mesh |
|---|---|---|---|
| Confidentiality | Code-enforced, one log line per request (D138) | Same if the coordinator is fixed at L0 or is code | Spread across prompts, not auditable |
| Fit with the 18 Dec plan | Is the current plan (D135) | Adds a coordinator to build and evaluate | No |
| Token cost | 1x | About 2–3x (`unverified`: Cowork's estimate, not in the sources above) | 3–10x |
| Demo story | Proves where every request ran, and when not to use multi-agent | Impressive, harder to defend | Fragile live |

## The chosen shape (option A)
| Item | Becomes |
|---|---|
| Organiser | The router (code), as D135 already says |
| Public / private / critical | L3 / L1 / L0, set by the OQ-20 processing-permission axis; no new taxonomy |
| Email, calendar | Current plan unchanged (David, 21 Oct): C1 personal calendar read-only in stage 3, cut first; email out of scope. When built, the reader is quarantined (no tools, structured output) |
| Reviewer | Separate agent, stays (Codex, independent verification) |
| Coder, software architect | Build-time lanes (Claude Code, Codex), not runtime agents |
| Writer, designer, business sounding board | Skills, loaded by the one runtime agent |

**Revisit threshold:** add a runtime agent only when a skill fails one of three tests: its context fills with irrelevant output; independent parts could run in parallel; one agent would need more than about 20 tools. Record the test result in the decision.

## David's answers (21 Oct, stated in session)
1. **Critical means:** health, financial, and transatlantic-move discussions.
2. **Critical processing:** no online model, but not the weakest local model either.
3. **Email and calendar:** keep the current plan.

## Consequences (Cowork; to confirm)
- **Critical = L0 only, and L0 = the Mac Air (D141, 24 GiB unified memory).** With no hardware purchase (D134) and no online model, the strongest critical-tier model is the strongest that fits the Air. A rented EU GPU would be online and is excluded. "Not the weakest" therefore becomes a selection criterion for T9b step 4 (Q-cowork-21c).
- **Critical requests fail when the Mac is asleep or off Tailscale.** Router rule 5 (no looser fallback) applies: the answer says so; nothing is sent elsewhere. Stage 3's "phone works with the Mac off" holds for public and internal only.
- **"No online model" also covers the build agents.** Cowork, Claude Code, Codex and the claude.ai Project are online models. The data policy's wave-2 gate (b) already says they must not reach local-only files, verified by an access test. Critical material therefore stays out of Dbrain2 until the wave-2 gates pass (Q-cowork-21b). A Cowork grep on 21 Oct found no relocation notes in the live vault.
- **Health versus training data.** Data policy §4 treats Strava/HR as health data but allows it to approved external processing; the wave-2 row says "health beyond training". Whether David's "health" includes training data decides whether the showcase workflow can still run at L1/L3 (Q-cowork-21a).
- **Protected-file edits needed after the answers:** data policy (critical categories, financial and move discussions as local-only), router ceiling rule in the PV1 brief. Both need a recorded David approval.

## Follow-up answers (David, 21 Oct ~14:15)
- **Q-cowork-21c, quality first:** T9b step 4 picks the strongest model that fits 24 GiB on the dev cases, latency second; L0 may exceed the D56 text p95 of 8 s.
- **Q-cowork-21a, Strava is not critical:** training data is workout data, not health for the critical tier; it stays approved for external processing. Critical health = health beyond training. Showcase and stage 3 demo unaffected.
- **Q-cowork-21b, yes:** critical material stays out of Dbrain2 until the wave-2 gates pass; the L0-only rule is built in stage 3 and tested on synthetic notes.
- Resulting edits, protected (David's approval is these answers): data policy names finances and transatlantic-move discussions as local-only alongside health beyond training, and states that training data is not critical; PV1 ceiling rules map processing=local-only to L0; D56 note that L0 latency may exceed 8 s.
