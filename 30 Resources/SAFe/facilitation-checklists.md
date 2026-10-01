---
classification: internal
status: draft
updated: 2026-10-01
tags: [safe, facilitation, checklists, events, lens/pgm]
---

# Facilitation checklists

One-page run sheets per event: **prepare → run → after → if it goes wrong**. They are condensed and
rewritten from the Facilitator's Guides to SAFe, the Remote ART toolkit checklists and the PI
Execution checklists. Purposes and owners are in [[events-and-cadence]]. PI Planning and I&A in depth
are in [[pi-planning-and-execution]].

**Universal rules for every event:** publish the agenda and purpose in advance; reuse an adjustable
agenda template; timebox and use **meet-afters** for anything deep (with only the people involved;
run the biggest meet-after first so others can leave); rotate facilitators; for remote, cameras on,
mute by default, a raise-hand mechanism and a shared live document.

---

## Iteration Planning (SM/TC; ≤4h, usually 1–2h)

**Prepare:** enough refined stories in the team backlog; capacity tracker updated (holidays, PTO);
re-read the team PI objectives; know which features land this iteration.

**Run:**

1. **Close out the last iteration** (5 min). Accept or move leftover stories.
2. **Establish capacity** (5 min). Start from historical velocity minus unavailability.
3. **Analyse and estimate stories** (20–30+ min) with the PO, in priority order, including
   dependencies. Stop when capacity runs out.
4. **Draft iteration goals** (5–10 min). Some teams write goals first.
5. **Commit.** Fist of five or Roman vote. Explore any vote below 3 with curiosity.

**After:** publish the goals; update the tool; plan conversations with teams you depend on or that
depend on you.

**If…**
- the team is chronically over capacity → show the data and plan *under* capacity (celebrate it);
- one person is always over-loaded → swarm, split, or defer that person's stories;
- the confidence vote is low → good, it's transparency: discuss and replan.

## Daily Stand-up (team; 15 min)

**Prepare:** same time and place daily; board or tool current; risks and impediments from yesterday;
updates from dependent teams.

**Run:** start on time. Each person takes under a minute on three questions: what I did toward the
goal, what I'll complete today, what is blocking me or the team. Name the meet-afters at the end.

**After:** SM/TC follows up impediments; PO adjusts goals if needed; flag impacts to dependent teams
or PI objectives.

**If…**
- updates run long → ask everyone to stand, use "popcorn" order, enforce the 1-minute norm;
- there is conflict → take it to a meet-after or a 1:1;
- work is blocked → swarm in a meet-after; SM/TC escalates.

**Remote:** start 10 minutes early for social chat so it doesn't eat the DSU; keep the iteration goals
on screen.

## Backlog Refinement (PO; 1–2× per week, ≥1× per iteration)

**Prepare:** a prioritised backlog in a shared tool; features, PI objectives and dependencies to hand.

**Run:**

1. Make sure next iteration's stories are **ready**: 3Cs (Card, Conversation, Confirmation),
   INVEST, acceptance criteria.
2. Brainstorm future stories (features, enablers, maintenance, dependencies).
3. Do initial sizing and ranking.

**Outcomes:** estimated stories ready for the next iteration; spikes identified; dependencies resolved
or actioned; risks surfaced.

**If…**
- stories are ≥8 points → split them using the patterns in [[product-management-and-po]];
- enabler work is invisible → reserve standing time for enabler stories.

## Iteration Review (SM/TC facilitates, team demos; ~1h)

**Run:**

1. Review iteration goals (and PI objectives).
2. Demo each completed story, including spikes (as findings) and NFRs.
3. Reflect on incomplete stories. They reveal impediments, false assumptions, changing priorities,
   estimation errors and over-commitment.
4. Refine the backlog from feedback.

**After:** feed the findings into the retrospective; pick items for the **System Demo**.

**If…**
- "nothing to show" → demo work in progress, a spike's learning, or a partial feature;
- goals are routinely missed → check WIP, story size and capacity planning.

**Rules:** limit demo prep to 1–2 hours; no slides, demo working product.

## Iteration Retrospective (SM/TC; ≤1h)

**Run:**

1. Set the goal and format (5 min). Formats: individual sticky notes, appreciation, one word,
   1–5 rating, well/not well/suggestions.
2. Silent writing (10 min).
3. Review the input (10–15 min).
4. Brainstorm actions (5 min).
5. Vote on 1–2 improvement items for the team backlog (5 min).

**After:** assign an owner for each action; track completion and effect; send ART-level issues to the
RTE via the PO.

**Keep it fresh:** rotate the facilitator, vary formats and themes.

---

## ART Sync / Coach Sync / PO Sync (RTE; weekly, 30–60 min)

**Prepare:** cadence fixed for the whole PI; every team represented (SM/TC, PO or lead), plus a proxy
or written update if someone can't attend; architecture/engineering invited; topics sent in advance;
ongoing shared notes document.

**Run:**

- **Coach Sync** (5.1: SoS): each team covers what it achieved since the last meeting, what it will
  achieve by the next, blockers, and "am I about to put a block in someone else's way?"
- **PO Sync:** features in flight, scope adjustments, PI objective risk, ART backlog refinement and
  WSJF for the next PI.
- Keep the **ART planning board and PI objectives on screen**, then move to meet-afters.

**If…**
- it turns into a status report → restate the purpose and send stakeholders to the System Demo;
- enabler detail is missing → invite the SA;
- updates run long or there are many meet-afters → hold it more often, with tighter facilitation;
- people disengage → rotate facilitators and themes, celebrate wins, run a retro on the sync itself.

## System Demo (PM/RTE; end of every iteration, ~60 min)

**Prepare:** decide what will be demoed **at the start** of the iteration; agenda template; named
facilitator plus a tech check; a production-like environment.

**Run:**

1. Business context and PI objectives (5–10 min).
2. Each feature: a short description (≈5 min), then an end-to-end demo (5–10 min per feature,
   20–30 min in total).
3. Risks and impediments.
4. Open feedback.
5. Wrap-up: progress, feedback and actions.

**If…**
- teams avoid presenting → find the root cause (TTA maturity, components not integrable, anxiety)
  and coach; partial features, NFR work or prototypes are acceptable;
- demos overrun → show features and benefits, not stories, with visible timers;
- demos don't show working, tested capability → coach on the CDP.

**Creative:** have teams demo *problems* as well as solutions; hold "no slides, all demo" days.

## Architect Sync (STE / chief architect; weekly, 30–60 min)

**Prepare:** agenda based attendance (solution leadership every week; ART PM/SA; others by topic:
quality, security, UX); agenda published early.

**Run:** enabler progress → design reviews → significant design issues → feature/story technical
approach → runway versus long-term vision → runway backlog.

**If…**
- key stakeholders don't come → schedule around them or appoint a proxy with authority;
- it becomes status → refocus, or have the STE/RTE facilitate;
- there is no technical agenda → cancel it.

---

## PI Planning (RTE; 2 days): checklist

**T-8 to T-4 weeks:**

- [ ] Dates set and published
- [ ] Readiness workbook checked (scope, RTE, cadence, teams with SM/PO, BO alignment, vision, top ~10
  features, system team, shared services, tooling, environments, quality strategy)
- [ ] Executive presenter confirmed
- [ ] Venue or remote set-up booked

**T-4 to T-1 weeks:**

- [ ] Briefings drafted: business context, vision + feature handout, architecture + NFRs, development
  practices
- [ ] Features WSJF-ranked at PO Sync
- [ ] Capacity data per team
- [ ] Event calendar for the next PI
- [ ] Facilitator briefing and dry run (pair a first-time RTE with an SPC)

**Day 1:** briefings → planning context → breakouts → draft plan review → management review.
**Day 2:** adjustments → breakouts (BOs score business value) → final plan review → ROAM →
confidence vote → rework → retro. Detail in [[pi-planning-and-execution]].

**Distributed additions:**

- [ ] Timezone-fair agenda ("share the pain")
- [ ] Facilitator per location
- [ ] Tooling cheat sheet; boards set up and access tested
- [ ] Channels: one per team plus a main room
- [ ] Stakeholder consultation slots booked
- [ ] Day-1 facilitator debrief; Coach Sync before Day 2
- [ ] Work-from-home guidance shared

## Inspect and Adapt (RTE; end of PI, ~half day): checklist

**Before:**

- [ ] Scheduled at the start of the PI
- [ ] BOs score **actual** business value with each team *before* the event
- [ ] PI System Demo prepared (PM/PO/SA frame each part)
- [ ] Metrics pack with the *why* behind each metric
- [ ] Facilitators per group
- [ ] Plan for turning improvement items into backlog items

**Run:** PI System Demo (≤60 min) → quantitative and qualitative review (20–45 min) → retro (≤30 min)
→ problem-solving workshop (≥60 min: problem → fishbone → 5 Whys → dot vote and Pareto → restate →
brainstorm → improvement items).

**Distributed:**

- Team retros run in advance generate candidate problem statements, which are voted on ahead of time.
- People are grouped by affinity per problem, with your strongest facilitators on virtual groups.
- Coach Sync checkpoints at **0:30 / 1:00 / 1:30** (see [[pi-planning-and-execution#7. Inspect and Adapt (end of PI)]]).

## Use it as…

- **PgM (primary):** copy these into your RTE/SM onboarding pack, adapted to client vocabulary.
- **TC:** observing an event against these sheets gives a fast maturity read during discovery.
- **PL:** the PO-led events (refinement, PO Sync, System Demo) are where product quality is won.

## Related

[[events-and-cadence]] · [[pi-planning-and-execution]] · [[roles]] · [[product-management-and-po]]
