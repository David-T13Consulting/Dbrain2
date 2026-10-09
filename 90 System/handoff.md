---
classification: internal
---
# Handoff queue (Cowork → the lead)

Cowork edits files but cannot run git (D49). It lists uncommitted changes here. **The lead (Claude Code) commits each entry as its own commit** with the suggested message, on `master` per the multi-agent rules, then deletes the entry. Codex never commits. Empty queue = nothing pending.

> ## ▶ Cowork → lead, 9 Oct 09:00: subagent model routing (David, 9 Oct 08:54: "#5 now ok… the lead (Opus) must properly assess the model for its sub agents. Intelligent routing is important.")
> **Done by Cowork, uncommitted:** `.claude/settings.json` gains `"env": {"CLAUDE_CODE_SUBAGENT_MODEL": "sonnet"}` (JSON validated). That is only the **default** for a subagent call that names no model. Per Claude Code's docs (code.claude.com/docs/en/sub-agents, read 9 Oct): a per-call `model` parameter wins over a definition's `model:`, which wins over this variable, which wins over the main model; **the built-in Explore and Plan agents ignore the variable and run on the lead's model unless the call names one**; `CLAUDE_CODE_SUBAGENT_MODEL_FORCE` is **not** set, so routing stays possible.
> **0. First thing this run:** read the Claude Code extension's version and record it in PROGRESS. **Before v2.1.251 the variable overrode the per-call parameter**, so routing would silently be off (everything Sonnet). If older: do not rely on routing, write `for-david.md` Q90 (update the extension or remove the variable), carry on.
> **1. Record as a decision (next D number), amends D64, source David 9 Oct 08:54. Edit AGENTS.md › Model policy (it asks David; this is the change):** replace the row *"| Claude Code subagents: search, tagging, simple checks | Smaller Claude model | `model:` field in each subagent definition |"* with *"| Claude Code subagents | Routed per call by the lead (rules below); default Sonnet | `model` on each Agent call; default `CLAUDE_CODE_SUBAGENT_MODEL` in `.claude/settings.json` |"* and add after the table's bullets:
> *"**Subagent routing (D-next, David 9 Oct).** The lead picks the model on every Agent call, Explore and Plan included (they run on Opus unless a model is named), by what the result will be used for:*
> *- **Haiku:** mechanical lookups whose output is locations or counts, not judgment: find files, grep sweeps, list references, check that a string is present.*
> *- **Sonnet (default):** reading and summarising code or notes, drafting tests from a written spec, routine edits outside the security boundary, bookkeeping drafts.*
> *- **Opus:** anything touching the security boundary (failure store, `outpath`, leak check, deny rules, data policy), choosing between design options, diagnosing a failure that survived two rounds, and every D74 second-opinion consult.*
> *- **Escalate, never downgrade:** a subagent result that is incomplete, contradicts the lead or other evidence, or is a second attempt is redone one tier up; security-boundary work never goes below Opus. When unsure between two tiers, take the higher.*
> *- **Unchanged:** the lead stays Opus; Codex stays the reviewer; subagents never commit.*
> *- **Logged:** one line per subagent call in the brief's run notes: task, model, reason. The weekly review samples these lines; misroutes (a lower tier that had to be redone) are counted."*
> Suggested message: `Subagent routing per call, default Sonnet (D-next, David 9 Oct)`; commit with `.claude/settings.json`. Tier 2 (rule change).
