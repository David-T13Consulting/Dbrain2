---
classification: internal
status: draft
updated: 2026-10-01
tags: [safe, principles, mindset, lens/tc]
---

# Principles and mindset

The "why" layer. When a client asks whether they can drop or adapt a SAFe practice, the principles
are the test: you can change a practice if the principle behind it still holds.

## Core values

| 5.1 core values (toolkits) | 6.0 core values (current) | What changed |
|---|---|---|
| Alignment | **Alignment** | Kept |
| Transparency | **Transparency** | Kept |
| Built-in Quality | **Respect for People** | Built-in Quality moved down to a team/technical practice (see [[devops-and-architecture]]) |
| Program Execution | **Relentless Improvement** | "Program" retired as a term; execution became the outcome, not a value |

The 6.0 change matters when you coach. The values are now about *culture*, not delivery mechanics,
which is closer to how a consultant actually diagnoses a stalled transformation.

How the LACE operationalises the values (from the LACE toolkit, restated):

| Value | What the change team does about it |
|---|---|
| Alignment | Communicates the business need and urgency, owns the implementation roadmap, sets objective metrics |
| Transparency | Shows transformation progress openly, extends SAFe into budgeting/HR/contracts, runs Lean-Agile events |
| Built-in quality *(5.1)* | Keeps practices consistent, sources training and coaching, runs communities of practice |
| Execution *(5.1)* | Identifies value streams, launches ARTs, supports PI Planning / System Demo / I&A |

## Lean-Agile mindset

Two halves: **think Lean** and **embrace agility**.

- **House of Lean** (5.1 picture, still the teaching device). The roof is the goal: value, meaning the
  shortest sustainable lead time with the best quality and value to people and society. The pillars are
  **Respect for people and culture**, **Flow**, **Innovation** and **Relentless improvement**. The foundation
  is **Leadership**. The Toyota motto quoted in the toolkits, "there is a constant sense of danger",
  is the intent behind relentless improvement.
- **Agile Manifesto.** Four values and twelve principles. The "individuals and interactions" and "responding
  to change" values are the ones regulated clients find hardest. Pair them with
  [[regulated-environments]].

## The ten SAFe principles

| # | Principle (6.0 wording) | What it means in practice | Where it shows up |
|---|---|---|---|
| 1 | **Take an economic view** | Decide by cost of delay and lifecycle economics, not utilisation or project budgets | WSJF, lean budgets, epic business cases |
| 2 | **Apply systems thinking** | Optimise the whole value stream. The solution, the enterprise and the flow are all systems | ARTs, value streams, I&A problem-solving |
| 3 | **Assume variability; preserve options** | Keep design and requirement options open until you have enough knowledge. Set-based design | Solution intent, enablers, spikes |
| 4 | **Build incrementally with fast, integrated learning cycles** | Short PDCA loops on integrated increments. Learn and pivot early | Iterations, PIs, MVPs |
| 5 | **Base milestones on objective evaluation of working systems** | Use demos of integrated systems as milestones, not phase-gate documents | System Demo, PI System Demo |
| 6 | **Make value flow without interruptions** **[6.0]** | Find and remove flow impediments using the eight flow accelerators | ART/team Kanban, flow metrics |
| 7 | **Apply cadence; synchronise with cross-domain planning** | Rhythm makes routine things predictable. Synchronisation surfaces conflicts early | PI cadence, PI Planning |
| 8 | **Unlock the intrinsic motivation of knowledge workers** | Autonomy, mastery and purpose. No individual incentives that fight team goals | Team charters, leadership behaviours |
| 9 | **Decentralise decision-making** | Centralise only decisions that are infrequent, long-lasting and have significant economies of scale. Push everything else to where the information is | Guardrails, PO/PM authority |
| 10 | **Organise around value** | Organise around value streams, not functions. The dual operating system | Value stream and ART identification |

**[5.1] → [6.0]:** principle #6 was "Visualise and limit WIP, reduce batch sizes, and manage queue
lengths". 6.0 widened it into *flow* and added the **eight flow accelerators**:

1. Visualise and limit WIP
2. Address bottlenecks
3. Minimise handoffs and dependencies
4. Get faster feedback
5. Work in smaller batches
6. Reduce queue length
7. Optimise time "in the zone"
8. Remediate legacy policies and practices

### Principle 9: the decentralisation test

A decision should be **centralised** when it is:

- **infrequent**: not made often, and not urgent;
- **long-lasting**: hard to reverse;
- **economies of scale**: one answer serves many.

Examples are the tech stack, the portfolio epic threshold and compensation policy. All other
decisions go to the teams. A simple way to use this with executives: ask them to list their last ten
decisions and score each one against the three criteria.

## The dual operating system

From the Executive Workshop (Kotter's *Accelerate*):

- The **hierarchy** gives stability and efficiency. Keep it for people management, compliance and budgets.
- The **network** gives speed of innovation. It is made of value streams and ARTs that cut across the
  hierarchy.

SAFe *adds* the network. It does not replace the hierarchy. This framing defuses fear of
reorganisation: "We're not redrawing the org chart, we're organising the builders around value."

## Use it as…

- **PL:** principles 1, 3, 4 and 5 are the product-discovery principles. Use them to argue for
  MVPs and against big upfront specs.
- **PgM:** principles 6 and 7 are your levers. Cadence plus flow is what you are managing.
- **TC:** principles 2, 9 and 10 are the transformation thesis. Lead executive conversations with
  them, not with events.

## Related

[[configurations-and-competencies]] · [[lean-agile-leadership]] · [[metrics-and-assessments]] · [[30 Resources/SAFe/glossary|glossary]]
