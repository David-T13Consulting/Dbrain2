---
classification: internal
task: D64
owner: "@code"
status: done
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
2. `codex exec --profile review` runs GPT-6 Astra at effort `high` with a read-only sandbox. Proved by one dry run on a trivial diff, with its output pasted under Outcome. *(Amended 2 Oct from "the highest reasoning effort" to `high`, on David's decision — see Outcome §3. The original wording and the config disagreed, and he resolved it in favour of the config.)*
3. The policy has a final decision number (after D63). Decision row: *Build-agent models follow a policy David sets: Opus for Cowork and the lead, smaller Claude models for simple subagents, GPT-6 Astra as the independent reviewer at effort `high`; config files apply it.* *(Same amendment as item 2.)* Why: removes per-session model choice from David, keeps the review independent, makes model use traceable. Revisit when a model is retired or reviews prove too slow or costly.
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
**Closing with this commit, 2 Oct 2026 (session 14).** Both blockers the first review raised were David's, and
he answered both the same session. `status: done` is set on the understanding that this commit lands; if it
does not, the brief is back to `in-review`. What follows is what was done, with the command behind each claim.

**1 · The lead's model is pinned.** `.claude/settings.json` (new, git-tracked, no secrets):

```json
{
  "model": "opus"
}
```

The alias `opus` is used rather than a pinned `claude-opus-5`, so "the lead runs Opus" stays true when a new
Opus ships. Per-session traceability stays where the template already puts it: each brief's `models:` field
records the IDs actually used.

**2 · The reviewer runs from the documented command.** David chose to install the standalone CLI rather than
point at the copy bundled in the ChatGPT desktop app:

| Step | Evidence |
|---|---|
| Install | `npm install -g --prefix ~/.local @openai/codex`. A plain `npm install -g` failed with `EACCES` on `/usr/local/lib/node_modules`; the user-prefix install needs no `sudo` and `~/.local/bin` is already on `PATH` |
| On `PATH` | `command -v codex` → `/Users/davidduchesne/.local/bin/codex`; `codex --version` → `codex-cli 0.160.0` |
| Documented command works | `codex exec --profile review` on a trivial diff — transcript below |

Dry run through the documented command, on a trivial diff (a `nmae` → `name` typo fix), verbatim:

```
$ codex exec --profile review --skip-git-repo-check "Review this trivial diff in one or two sentences.
  Does it fix a bug?
  --- a/greet.py
  +++ b/greet.py
  @@ -1,2 +1,2 @@
   def greet(name):
  -    return \"Hello \" + nmae
  +    return \"Hello \" + name"

provider: openai
approval: never
sandbox: read-only
reasoning effort: high
session id: 01a0fd36-063e-7f30-8c81-f1679ff87902

codex
Yes. It fixes a typo that caused a `NameError` for the undefined variable `nmae`; the function now
correctly uses its `name` parameter.
```

What had actually been wrong, recorded so it is not re-diagnosed: the CLI was never missing — it ships inside
the ChatGPT app at `/Applications/ChatGPT.app/Contents/Resources/codex-cli/bin/codex` (0.159.2) and was used
by absolute path for every review in this session. Two separate traps: it was not on `PATH`, and from 0.159 a
profile is **its own file** (`$CODEX_HOME/<name>.config.toml`) rather than a `[profiles.review]` section in
`config.toml`, so grepping `config.toml` made a perfectly good profile look absent. Both are now noted in
`AGENTS.md`.

**3 · Reasoning effort: resolved in favour of the config, and `AGENTS.md` changed.** David confirmed `high` is
the standard review level, with `ultra` reserved for when the lead and the reviewer are both stuck — which is
what `~/.codex/review.config.toml` already said. The model-policy table now reads "GPT-6 Astra at effort
`high`, escalating to `ultra` only when the lead and the reviewer are both stuck". `AGENTS.md` was outside
this brief's Files in scope; David's decision is what authorised the edit, and the table says it changes only
on his decision.

**4 · Condition 3.** D64's decision row and `log.md` entry are written, and the row no longer carries the
"implementation in review" caveat.

**5 · Condition 4.** Reviewed by Codex (`gpt-6-astra`, effort `high`, read-only) before commit, twice:

| Attempt | Verdict | What happened |
|---|---|---|
| 1 | changes required, 2 blockers | Effort `high` versus "highest", and the documented command not working. **Not committed** — the stop conditions doing their job before they are even written into `AGENTS.md`. Raised with David |
| 2 | changes requested, 3 medium | The dry-run transcript had been summarised instead of pasted; "Done when" items 2 and 3 still said "highest"; and the Outcome and `log.md` declared closure before the commit existed. All three are fixed above and in `log.md` |

Condition 4 is met when this commit lands. Nothing in it was committed before its review.

**Consequence for the next session:** the review gate is now reproducible from the command `AGENTS.md`
documents. Nothing else in the loop needs the absolute path.
