---
classification: internal
task: D64
owner: "@code"
status: in-review
created: 2026-10-01
models: [claude-opus-5 (lead), gpt-6-astra (review)]
---
# Set up the model policy in config (D64)

> Written by Cowork as provisional **D-cowork-2**; renumbered to **D64** by the lead in session 13.

## Goal
Make the AGENTS.md "Model policy" section true in configuration, so no session needs a manual model choice.

## Files in scope
- `.claude/settings.json` (vault root, new): default `model` for the lead
- `~/.codex/config.toml`: **outside the vault, not committed.** Add a `review` profile only; leave other settings alone
- PROGRESS.md (decision row), `log.md`, `index.md`, this brief

## Inputs / context to read first
- [[AGENTS]] → "Model policy" and "Multi-agent work"
- Codex CLI's own model list and config reference, for the **exact** model ID and the name of the highest reasoning-effort value. David calls the model "Astra" (GPT-6 Astra). Do not guess the ID string.

## Done when
1. `.claude/settings.json` pins the lead's default model. It contains no secrets.
2. `codex exec --profile review` runs GPT-6 Astra at the highest reasoning effort with a read-only sandbox. Proved by one dry run on a trivial diff, with its output pasted under Outcome.
3. The policy has a final decision number (after D63). Decision row: *Build-agent models follow a policy David sets: Opus for Cowork and the lead, smaller Claude models for simple subagents, GPT-6 Astra at highest reasoning effort as the independent reviewer; config files apply it.* Why: removes per-session model choice from David, keeps the review independent, makes model use traceable. Revisit when a model is retired or reviews prove too slow or costly.
4. Codex has reviewed the diff (the first review using the new profile), and the change is committed.

## Constraints
- No API keys or tokens in any vault file.
- If the Codex config already has profiles, add to them and do not overwrite.

## Review
Independent read-only review by Codex, 2 Oct 2026, session 14. Model `gpt-6-astra`, reasoning effort
`high`, read-only sandbox, via `codex exec --profile review`. Codex was given `AGENTS.md` and the diff
only, not the lead's reasoning. Findings bearing on this brief:

| # | Finding | Action |
|---|---|---|
| 4 | `AGENTS.md` promises the reviewer runs at the **highest** reasoning effort, but the profile runs at `high`, and no brief established that `high` is the highest | **Flagged for David, not fixed.** `review.config.toml` records David's own 1 Oct instruction: `high` is the standard review level and `ultra` is reserved for when lead and reviewer are both stuck. So the config follows David; the `AGENTS.md` wording does not match it. The model-policy table may change only on David's decision, so the wording is left as-is and raised with him |
| 3, 4 | This brief's Review, Outcome and `models:` were empty although the work had been done | Fixed here |

## Outcome
**Not done — `in-review`.** The review above returned two blockers that are David's to settle, so per the
D65 stop conditions this brief is not closed and nothing here is committed. What follows is what session 14
observed and did in the working tree, with the command that produced each claim, so David can verify rather
than take it on trust.

**1 · Condition 1 is met, but held out of git.** `.claude/settings.json` is written in the working tree and left **untracked**, because the review failed and stop condition (2) says the change does not get committed. It will be committed when David answers the two questions below:

```json
{
  "model": "opus"
}
```

The alias `opus` is used rather than a pinned `claude-opus-5`, so the policy line "the lead runs Opus" stays
true when a new Opus ships. Per-session traceability stays where the template already puts it: each brief's
`models:` field records the model IDs actually used. **This is the lead's choice, not David's instruction** —
if he wants the exact ID pinned instead, it is a one-line change.

**2 · Condition 2 is partly met, and the gap is David's call.** The "`codex` CLI is not on `PATH`" note in
the D63 brief had one cause: the `PATH`. The CLI is not missing — it ships inside the ChatGPT desktop app.

| Claim | Evidence (session 14) |
|---|---|
| Binary location | `/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex`, found with `find /Applications/ChatGPT.app -type f -name 'codex*'` |
| Version | `codex --version` → `codex-cli 0.159.2` |
| Not on `PATH` | `command -v codex` → absent; `$PATH` contains no Codex directory |
| Profile format | `codex exec --help` → `-p, --profile <CONFIG_PROFILE_V2>  Layer $CODEX_HOME/<name>.config.toml on top of the base user config`. In 0.159.2 a profile is a **separate file**, not a `[profiles.review]` section in `config.toml`. Grepping `config.toml` for that section is what made the profile look absent on 1 Oct |
| Profile contents | `~/.codex/review.config.toml`, dated 1 Oct — correct in form, though whether `high` satisfies "highest" is question 1 below, so "already correct" would be too strong: `model = "gpt-6-astra"`, `model_reasoning_effort = "high"`, `sandbox_mode = "read-only"`, `approval_policy = "never"`, no secrets |

Dry run on a trivial diff (a `nmae` → `name` typo fix), verbatim:

```
model: gpt-6-astra · provider: openai · approval: never · sandbox: read-only · reasoning effort: high
Yes. It fixes a typo: `nmae` would raise a `NameError`, while `name` correctly references the
function's parameter.
```

So the reviewer runs, and it reviewed its own enabling diff. But it runs **only by absolute path**:
`codex exec --profile review`, the command `AGENTS.md` and these briefs all specify, still fails as typed.

**3 · Condition 3 is partly met.** The decision number D64 is assigned, and session 14 wrote its PROGRESS
decision row and `log.md` entry — the *decision* is on the record, and was David's on 1 Oct regardless of
whether the config lands. What is **not** done is the *implementation* that row depends on: the config change
is held out of git, and the row says so rather than implying the policy is fully in force.

**4 · Condition 4 is not met.** The closing diff was reviewed (above) and the review did not pass, so there
is no commit.

### Two decisions for David

| # | Question | Why it is his and not the lead's |
|---|---|---|
| 1 | **Reasoning effort: is `high` the review standard, or must it be the highest available?** `AGENTS.md` says "highest reasoning effort"; the profile runs `high`; `review.config.toml` records his own 1 Oct instruction that `high` is standard and `ultra` is for when lead and reviewer are both stuck. Either the `AGENTS.md` wording changes to match, or the profile changes to `ultra`. | The model-policy table says it changes only on David's decision, and the two records disagree about what he decided |
| 2 | **How should the lead invoke the reviewer?** Either symlink the bundled binary into `~/.local/bin` (already on `PATH`, so the documented command works), or amend `AGENTS.md` to record the absolute path. | The symlink is outside the vault and outside this brief's Files in scope; amending `AGENTS.md`'s model policy is his call |
