---
classification: internal
note_type: checklist
source: cowork
review_status: approved   # David approved Q55 (5 Oct) and the AGENTS.md text (Q65, Q68, 6 Oct); set by the lead when it applied that text (D77, session 29)
created: 2026-10-05
---
# Codex review checklist

What the reviewer (`codex exec --profile review`, read-only) checks on every Tier 1 and Tier 2 diff. Defined in [[90 System/briefs/D-cowork-10-review-tiers|D-cowork-10]]. The reviewer gets this checklist, the vault rules, the brief (goal, files in scope, Done when, accepted risks, proposed tier) and the diff. Not the lead's reasoning.

## Output format
1. **Tier check:** confirm the proposed tier, or raise it (never lower it) with the reason.
2. **Findings table:** `# · check · file:line · finding · severity (blocker / should-fix / nit)`.
3. **Verdict:** `pass` (no blockers) · `fail` (≥ 1 blocker) · `escalate` (needs David's judgment: becomes Tier 2).

Only blockers fail a review. Do not re-raise a finding listed as an accepted risk in the brief; mention it only if the diff makes it worse.

## Checks
| # | Check | Blocker when | Should-fix when |
|---|---|---|---|
| R1 | **Scope:** only files listed in the brief changed | Any file outside scope changed | — |
| R2 | **Data policy:** no client or counterparty material, no secrets, no sensitive data about third parties or children beyond data-policy §3/§3a | Any instance (also a loop stop condition), including any detail that could identify a child or the household under §3a (names, places, region codes, club or uniform details, or a combination of details that identifies); and any child detail beyond what the logistics need (§3a.2a, §3a.6) | — |
| R3 | **Classification:** every new or changed note has `public` or `internal` | Missing, or `client` | — |
| R4 | **Provenance:** every factual claim cites a wikilink, a Source_Material path or a URL, or is tagged `unverified` | Uncited claim in a Tier 2 note; a cited source that does not exist or contradicts the claim | Uncited claim in a Tier 1 note (fix: cite it, or tag it `unverified`, which makes it Tier 2); source supports the claim only partly |
| R5 | **Tier 2 content inside a Tier 1 diff:** domain claims David would repeat to a client, decisions David has not yet taken (recording his own answers stays Tier 1), rule changes, client-facing or demo material | — | → verdict `escalate`, not fail |
| R6 | **Done when:** each item in the brief's Done when is met and checkable | An item claimed done is not met | Done-when item vague or untestable |
| R7 | **Consistency:** no contradiction with AGENTS.md, active D-numbers, data policy or another note in the diff | Contradicts a hard rule or the data policy | Contradicts another note or an older decision without saying it supersedes it |
| R8 | **Code (runtime, scripts, evals):** runs, tests pass, errors fail closed, no network or write path the brief does not name | Security boundary weakened (scope, write guard, cloud refusal, redaction); tests fail; error swallowed silently | Missing test for a new path; unclear error message |
| R9 | **Bookkeeping:** IDs provisional unless the lead assigned them; PROGRESS/TASKS/log updated when the brief says so | — | Missing or wrong ID, missing log line |
| R10 | **Clarity:** plain English, no ambiguity in a rule or instruction an agent will follow | A rule that two agents could read two ways | Wording that could be clearer |

Style preferences, formatting taste and alternative designs are `nit` at most.

## Out of scope for the reviewer
- **Languages other than English and French** (David, 9 Oct 13:39). The product and its tests support EN and FR only. Missing Dutch, German or any other language is never a finding; do not ask for it. Existing NL coverage in committed code is left as it is.
- Deciding whether a claim is true (R4 checks the source, not the world).
- Tier 0 changes, once the deterministic pre-commit check is installed: they get the deterministic checks only. Until it is installed, Tier 0 changes get a Codex pass like Tier 1 (Q65); until AGENTS.md carries the review tiers, every commit needs a Codex pass (Q40).
- Choosing models, changing rules, or committing.
