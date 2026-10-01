---
classification: public
status: draft
updated: 2026-10-01
tags: [product-school, advanced-agents, agents, multi-agent, patterns, days/1-3]
---

# Advanced AI agents: anatomy, design patterns and agent teams (days 1–3)

Product School **Advanced AI Agents** certification (6 live sessions, May 2026 cohort, with a final project; the build tool used in class was a low-code agent builder, with Langflow as an option). Hub: [[30 Resources/Product School/README|Product School hub]]. This page covers the PM's role, the building blocks, six reasoning patterns and multi-agent archetypes. Memory, retrieval, tool access, evals and deployment are in [[advanced-agents-memory-tools-evals-deploy]]. Own-words synthesis of David's course notes and slide captures.

## What an agent is

An agent is **not just an LLM**: it is a system wrapping an LLM with the ability to perceive, think and act. Four parts: the **brain** (reasoning engine), **planning** (strategy layer that breaks goals into steps), **tools** (arms and legs: real-world effects through APIs) and **memory** (context layer for future actions).

| Dimension | LLM product | Agentic system |
|---|---|---|
| Interaction | Responds to a single input | Executes a multi-step plan |
| State | Stateless; memory only within a conversation | Persistent; memory carries across conversations |
| Function | Primary output is generated content | Primary output is an **action or outcome** |
| Tool use | One directed API call | Selects and orchestrates multiple tools |
| Autonomy | Reactive | Proactive, acts on what the user wants to achieve |

Worked contrast: a CRM copilot with no persistent memory asks "which account?" every time, while an agent remembers the account, finds a recent support ticket and proactively suggests adding details to the follow-up.

## The evolving role of the AI PM

PMs now architect **probabilistic systems that reason, adapt and act**, not only deterministic user flows. Instead of just prompting a model, PMs define decision rights, trust boundaries and autonomy levels, much like managing a human team. Three layers:

| Core responsibility | Shift |
|---|---|
| **System intelligence** (interaction model, decision-making, adaptation/learning, state and memory) | From managing one conversation to architecting the product's **persistent memory** |
| **System capabilities** (architecture, autonomy and agency, tool use and environment, output type) | From delivering content for interpretation to executing **real-world outcomes** |
| **Product strategy** (value proposition, deployment context, evaluation complexity, governance need, supervision requirement) | From driving efficiency to unlocking new capabilities with a new level of governance |

In class the "agent era" PM was drawn as the meeting point of taste, judgement, problem shaping and agent orchestration, between pure strategy (no building) and pure code (no taste). A visible example: one popular open-source "AI startup team" skill pack maps slash commands to roles (CEO, strategist, engineer, designer, reviewer, QA, security officer, release manager).

## The agent autonomy spectrum

| Level | Name | Example | PM strategic focus |
|---|---|---|---|
| 0 | Reactive (no autonomy) | A chatbot answering from autocomplete, no memory or external actions | Safe, immediate value |
| 1 | Tool-using (assisted) | Assistant summarising a document or running a search | Fast ROI, minimal governance |
| 2 | Semi-autonomous (human in the loop) | Agent that researches, drafts and submits a report for human review | High leverage, manageable risk |
| 3 | Fully autonomous (goal-driven) | Agent that diagnoses and fixes a bug end to end | Maximum value, critical governance need |

PMs decide how much autonomy is safe *and* valuable. This is the "autonomy ladder" that later gates deployment ([[advanced-agents-memory-tools-evals-deploy]]).

## Blocks to standardise: the reusable agent platform

The PM's job is to define product requirements for the **stack**, creating a reusable, governable platform for all agents, not for each agent separately. Five blocks, each with "what you decide", a key anti-pattern and a ship check:

| Block | You decide | Anti-pattern | Ship check |
|---|---|---|---|
| **State and memory** | Mission lifecycle, memory and privacy policy, data requirements, stability/recovery | One giant prompt carrying all context: fragile, expensive, unscalable | Can you replay or resume a failed run? Are retries capped? Is PII isolated and deleted via TTL? |
| **Tooling fabric** | Permissions and scope, input/output rules, execution speed, vendor strategy | Free-text tool calls with no validated schema | Are tools schema-validated? Are sensitive tools (payments, deletes) behind a human gate? Timeouts and usage quotas set? |
| **Connectivity (MCP)** | Security and scope, compliance and audit trails, scalability and vendor strategy | Custom one-off connectors for every app, with no scoped, auditable access | Can you list exactly what data and actions the agent can access? Is every action logged? Security-reviewed? |
| **Multi-agent runtimes** | Orchestration and specialisation, data integrity at handoffs, conflict resolution and safety, deployment platform | One monolithic "do-everything" agent that cannot be debugged or scaled | Is there an "org chart" of agent roles? Are handoff data contracts defined? Is there an escalation path if agents loop? |
| **Governance hooks** | Audit trails and accountability, eval gate thresholds, transparency and debugging, safety and performance SLAs | Treating governance as an afterthought, so failures are found in production | Can security audit a full run end to end? Are intervention and rollback rates tracked? Are kill switches available? |

## Beyond the prompt: six agentic patterns (the "PM playbook")

A single long prompt is fragile for complex tasks. Choose the reasoning structure that balances **speed, safety and reliability**. Each pattern is analogous to a human working arrangement.

| # | Pattern | Analogy | What it does | Best for | Watch out |
|---|---|---|---|---|---|
| 1 | **Planner-Executor** | PM + engineer pairing | A planner breaks a goal into tasks; an executor does them one by one | Multi-step workflows needing auditability and a clear plan | A bad plan dooms the workflow; adds latency |
| 2 | **ReAct** | Think-do loop | Reason aloud, act, observe the result, repeat | Retrieving facts or using tools with a visible thought process (good for debugging) | Slower than direct generation |
| 3 | **Reflection** | Built-in editor | The agent critiques its own draft against standards and revises | Quality-critical output (a report or PRD) where quality beats speed | Each revision loop adds cost and time |
| 4 | **Tree of Thoughts** | Strategy brainstorming | Explore multiple branches in parallel, score each, pick the best | Complex planning and optimisation; avoids first-answer bias | Computationally expensive |
| 5 | **Routing** | Dispatcher | A dispatcher decides whether an AI agent, a tool or a human should handle the request | Triage by urgency, capability, cost and risk | Needs a good rubric for the dispatcher |
| 6 | **Multi-agent** | Cross-functional team | Specialised agents (researcher, writer, critic) collaborate and hand off | Complex end-to-end pipelines mirroring a human team | Coordination overhead; needs clear handoff contracts |

Real-world examples cited per pattern include trip planners and code planners (planner-executor), search-grounded answer engines (ReAct), terminal self-correction and brand-guideline critique (reflection), property-ranking and route simulation (tree of thoughts), support-ticket routing by urgency (routing), and software and research "squads" (multi-agent).

### Single vs multi-agent: when to split

- **Default:** start with **one agent** while scope is narrow and the workflow simple, to *discover the workflow*.
- **Move to multiple agents when** you can name distinct roles with different tools or policies, you struggle to debug or evaluate behaviour, or you need to iterate on one part without destabilising the rest. In other words, when you hit boundaries in skills, tools, data or failure modes.
- **Monolithic:** brittle, opaque, hard to scale (improving one part means retraining the whole). **Modular:** specialised, resilient, observable, scalable.
- **The generalist trap:** one agent asked to be both "viral" and "compliant" averages the conflicting instructions into mediocre output (context contamination). Splitting lets you tune one agent for creativity and another for strict precision, for example a creative agent proposes ten ideas and a compliance agent filters out the three risky ones.
- Two main reasons to use multi-agent systems: **increase revenue** or **reduce cost**.
- Downsides: cost, latency (communication breaks down), runaway loops. Guards from class: set a **maximum iteration count**, limit chat history, cap maximum tokens, and show **sources** to build trust.

### Six agent-system archetypes

| Archetype | Structure | Example | PM's governance role |
|---|---|---|---|
| **Sequential pipeline** | Each agent hands its output to the next, in order | Streaming homepage assembled from behaviour, content ranking, artwork, publishing | Eval gates after each handoff; consistent context sharing. Cons: latency, one bottleneck blocks all |
| **Parallel collaboration** | Agents work on facets simultaneously; an aggregator synthesises | Personalised shopping homepage from purchase history, cohort and browsing agents | Clear task boundaries; strong aggregator logic to remove redundancy |
| **Critic-executor loop** | Executor produces, critic reviews against standards, executor revises | Image generation with a second model critiquing for quality and safety | Cap review cycles; log the feedback loop; costs more compute and time |
| **Delegation tree** | A manager agent assigns subtasks to domain agents and consolidates | A ride platform's manager splitting matching, ETA and pricing | Supervisor evaluation gates; clear reporting logs per subtask. Hard to trace autonomy boundaries |
| **Negotiation and arbitration** | Agents with opposing goals propose; an arbitrator picks | Dynamic pricing balancing host revenue, guest budgets and demand | Define the arbitrator's rubric (often LLM-as-judge). Slower and costlier |
| **Hierarchical teams** | An org-chart structure: executive agent → department heads → specialists | An enterprise decision engine delegating to department agents | Logging, identity-based tracing and context summarisation at each level |

Strategic impact: **parallel** patterns unlock real-time personalisation without latency; **sequential and critic-executor** patterns guarantee safety by forcing a review loop (enterprise trust); **delegation and hierarchical** patterns let you sell complete results ("outcome as a service"); **negotiation** patterns balance competing goals such as price vs volume. Your role shifts from tuning prompts to designing aggregation logic, acceptance criteria, an "org design" and the incentives that let agents find the trade-off.

## The agent workflow spec (the PM's one-page blueprint)

A **PRD defines what the user experiences; the agent workflow spec defines how the agent operates behind the scenes.** Nine fields:

1. Business goal (outcome and KPI the agent drives)
2. Actors (agents, tools and humans, and their roles)
3. Plan (which core patterns and key steps)
4. Memory (what must persist, and its scope)
5. Tools (which APIs are allowed, with their schemas)
6. Eval gates (quality and safety checkpoints, including human in the loop)
7. Governance (what is logged, rollback procedures)
8. Metrics (task completion, intervention rate)
9. Risks and mitigations (what could go wrong, how to detect and recover)

## Managing agent teams: four layers

| Layer | What it does | What the PM defines |
|---|---|---|
| Communication | How agents exchange information | Rules for agent-to-agent messaging (A2A); clarity of context passing |
| Coordination | How tasks are assigned | Role boundaries; task-routing logic |
| Evaluation | How quality and progress are tracked | Eval metrics; human-in-the-loop checkpoints |
| Governance | How safety and compliance are ensured | Permissions; logging standards; oversight |

Frameworks mentioned (not mutually exclusive): CrewAI (role-based setup that makes teams explainable), Microsoft AutoGen (robust messaging for complex workflows), LangGraph (maps agent-to-agent handoffs and state changes for debugging) and MCP (standardises governable data access). Lessons from large vendors: orchestrate behind the scenes even for simple tool use; build internal critique loops for reliability; define roles and structured handoffs; use hierarchical teams with clear delegation.

### Multi-agent metrics

| Metric | Measures | What it tells the PM |
|---|---|---|
| **Collaboration accuracy** | Rate of successful handoffs | Process reliability |
| **Redundancy rate** | Amount of duplicated effort | Efficiency: are agents overlapping wastefully? |
| **Eval pass rate** | % of outputs passing quality gates | Stage quality |
| **Human intervention %** | Frequency of required overrides | Governance health: how often does the system need help? |

### Three governance rules for agent teams

1. Require a **supervisor or critic** agent for quality control, arbitration or final review.
2. **Log all agent-to-agent messages**: non-negotiable for traceability, debugging and auditing.
3. Define clear **"autonomy ceilings"** per agent role: how far it may act before requiring human review (the primary risk lever).

## Where to start

- Ask your assistant to review your last 30 days of conversations and identify where you spend the most time and what should be automated.
- Think of the chosen pattern as your **org chart**; pick it by answering "which reasoning structure delivers the best balance of speed, safety and reliability for my users?"
- Meet customers where they are (email, chat apps, Slack via an app and API endpoint) rather than inventing a new interface.
- Class prerequisite exercise: name your most time-consuming repetitive coordination task (ticket triage, data gathering, status summaries) and list what **data, tools and rules** you would standardise so an agent could execute it reliably.

Related: [[advanced-agents-memory-tools-evals-deploy]], [[ai-governance-and-compounding]] (four agent locks), [[10 Projects/AI Second Brain/03_Product_School_Playbook|03_Product_School_Playbook]].
