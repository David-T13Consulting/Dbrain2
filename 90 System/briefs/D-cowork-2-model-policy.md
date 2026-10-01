---
classification: internal
task: D-cowork-2
owner: "@code"
status: open
created: 2026-10-01
models: []
---
# Set up the model policy in config (D-cowork-2)

## Goal
Make the AGENTS.md "Model policy" section true in configuration, so no session needs a manual model choice.

## Files in scope
- `.claude/settings.json` (vault root, new): default `model` for the lead
- `~/.codex/config.toml`: **outside the vault, not committed.** Add a `review` profile only; leave other settings alone
- PROGRESS.md (decision row), `log.md`, `index.md`, this brief

## Inputs / context to read first
- `AGENTS.md` → "Model policy" and "Multi-agent work"
- Codex CLI's own model list and config reference, for the **exact** model ID and the name of the highest reasoning-effort value. David calls the model "Astra" (GPT-6 Astra). Do not guess the ID string.

## Done when
1. `.claude/settings.json` pins the lead's default model. It contains no secrets.
2. `codex exec --profile review` runs GPT-6 Astra at the highest reasoning effort with a read-only sandbox. Proved by one dry run on a trivial diff, with its output pasted under Outcome.
3. The policy has a final decision number (after D-cowork-1). Decision row: *Build-agent models follow a policy David sets: Opus for Cowork and the lead, smaller Claude models for simple subagents, GPT-6 Astra at highest reasoning effort as the independent reviewer; config files apply it.* Why: removes per-session model choice from David, keeps the review independent, makes model use traceable. Revisit when a model is retired or reviews prove too slow or costly.
4. Codex has reviewed the diff (the first review using the new profile), and the change is committed.

## Constraints
- No API keys or tokens in any vault file.
- If the Codex config already has profiles, add to them and do not overwrite.

## Review

## Outcome
