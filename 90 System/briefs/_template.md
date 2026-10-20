---
classification: internal
task: P2.2            # TASKS.md ID
owner: "@code"        # @code | @codex | @cowork | @david
status: open          # open | claimed | in-review | blocked | blocked-on-david | done
models: []            # model IDs actually used, e.g. [opus-…, gpt-6-astra (review)]
created: YYYY-MM-DD
---
# <task title>
## Goal (one sentence)
## Files in scope (agent may touch only these)
## Inputs / context to read first
## Steps (David, 8 Oct 22:24: each step fits one review cycle)
Cut the work into numbered steps small enough that each passes Codex within its review budget (1 review; 2 for Tier 2 and security-boundary steps; a Tier 1a step is committed once its tests pass and reviewed in the run's batch; D127, amended by D137), and is committed on its own before the next starts. As a rule of thumb, one step is one module plus its tests, or one wiring change. A run that hits the limit parks only the current step; every earlier step is already committed, and the brief's later steps are not started that run. Tier 0 steps need no Codex pass. AGENTS.md (Review tiers, Review failures) governs budgets, brief caps, the Tier 1a batch, the consult before a parked step is retried, and David's approval of Tier 2 steps.
1. …
## Done when (checkable)
## Constraints (vault rules that especially apply)
## Review   ← filled by the lead from Codex's read-only review: findings, verdict, model used
## Outcome  ← filled by owner: commit hash, open issues
