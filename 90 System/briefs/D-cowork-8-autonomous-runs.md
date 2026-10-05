---
classification: internal
task: D-cowork-8          # provisional; the lead assigns the final D-number
owner: "@code"
status: open
models: []
created: 2026-10-05
---
# Autonomous runs: keep working until the credit runs out or real work does (provisional D-cowork-8)

## Goal (one sentence)
Claude Code keeps working through a prioritised backlog without David, stopping only for real blockers and never for trivial ones, while every safety rule stays intact.

## David's decisions (5 Oct, via Cowork; queue Q37–Q40)
| Q | Rule | Replaces |
|---|---|---|
| Q37 | **Substantive review failure → fix and re-review up to the 5-attempt retry limit, then park the brief (`in-review`, findings recorded, nothing committed) and move to the next brief.** The run continues | D65 condition (2) / D70 "end the loop" |
| Q38 | **Bookkeeping-only failure → up to 5 fix-and-re-review rounds** (same cap) | D70's single re-review |
| Q39 | **Pre-approved safe command allowlist** in Claude Code permissions (below). The hard-limit list always asks | per-command prompts |
| Q40 | **No commit without a Codex pass, ever.** While Codex is rate-limited, work continues on branches and uncommitted drafts for one batched review | unchanged, made explicit |

## The run loop
1. **Start:** read AGENTS.md, this brief, PROGRESS, TASKS, handoff.md and for-david.md. Commit pending handoff entries if Codex is available.
2. **Pick** the highest actionable item from the backlog below. Actionable means: not `blocked`, not `blocked-on-david`, not parked this run, and inside the brief's file scope.
3. **Do it** → tests → Codex review → fix and retry up to 5 → commit on a pass, or park on the 5th failure.
4. **A question for David** → add it to for-david.md (recommended option first), mark that item `blocked-on-david`, go back to step 2. Never wait for an answer.
5. **Waiting on something slow** (a model download, a sweep, a Codex reset) → start the next item meanwhile, then come back.
6. **Repeat** until a stop condition below applies.

## Backlog, in priority order (re-read TASKS each pass; new `@code` work slots in by stage)
| # | Item | Done when |
|---|---|---|
| 1 | **MVP-phone fixes:** plain status line, quoted source lines, fact-first answers, readable `display` on every error | Tests pass; David's 4 smoke questions re-run |
| 2 | **Batched Codex review** of everything waiting: D69 apply, P2.2 round E, MVP-phone, T9/M6 brief, S2–S6 plan, TASKS tags | Each item committed or parked |
| 3 | **Answer quality:** a 20-question MVP regression set (include the negation cases; keep a held-out subset), plus the quote-first prompt measured against it | Before/after scores in the P2.2 results note |
| 4 | **P2.2 latency sweep analysis** | Findings in the results note (draft) |
| 5 | **T9/M6 model comparison** on the Air, once its brief passes review. Downloads only for models it names, within the 20 GB budget (Q8) | Ranked results; host sizing evidence for Q30 |
| 6 | **LTHR estimate from race data** (Q15) | Result to David via for-david.md; no zone changes |
| 7 | **P1.4 four-axis retrofit:** brief plus a dry-run diff report across the 114 notes. **Do not apply** (rule 8) | Dry-run report; approval queued for David |
| 8 | **Hygiene:** pre-commit secret scan, frontmatter lint (four axes, owner tags), handoff clean-up | Hooks run in tests |
| 9 | Any other open `@code` task in TASKS with no blocker | per its brief |

## Never stop for
- A question for David: queue it and continue.
- Codex being rate-limited: work uncommitted and batch the review.
- One brief blocked, parked or failing: move to the next.
- A bookkeeping review failure: fix and retry (up to 5).
- A flaky test or command: the retry limit and Codex debugging advice apply.
- A long-running job: do other work while it runs.
- A decision that already has a recorded default or answer in for-david.md, PROGRESS or a brief.

## Stop only when
1. The usage or credit limit is reached.
2. No actionable `@code` work remains: everything is blocked-on-david, blocked, parked or waiting for Codex with nothing else to do.
3. **Something unsafe is found:** a secret in a readable file, client data, or a data-policy breach. Stop, don't fix it silently, and report.

## Hard limits: always ask David, never pre-approved
Edits to `data-policy.md` or `AGENTS.md` · security or permission settings · the Keychain · launch agents, login items, Full Disk Access · deleting files · downloads not named in a brief or beyond budget · spending money · pushing to GitHub · anything touching `client`-classified material · applying P1.4 or any structured change across many notes.

## Permission allowlist (lead drafts `.claude/settings.json`; David approves once)
**Allow:** read anywhere in the vault and `dbrain-runtime` · `git status/diff/log/add/commit/branch/switch/merge` in both repos (merge to master only after a Codex pass) · `python`/`pytest`/project scripts inside `dbrain-runtime` · starting and stopping the local model and `/ask` · `codex exec --profile review` (read-only) · `tailscale status`, `curl` to the Air's own health endpoints.
**Ask:** everything on the hard-limit list, and any command not listed here.

## Reporting
- At the end of each run, append a **run summary** to `log.md`: items done, commits, items parked with reasons, questions queued, credit used if known.
- Add a one-line **"Since you last looked"** at the top of for-david.md, pointing to that summary.
- No mid-run pings to David unless a stop condition (3) fires.

## Launch (for David)
In Claude Code, start with `/loop` and the prompt below, so it paces itself and resumes after waits such as a Codex reset:
> Autonomous run per `90 System/briefs/D-cowork-8-autonomous-runs.md`. Follow its loop, backlog and stop rules. Questions go to for-david.md; never wait for an answer.

## Done when (checkable)
- AGENTS.md "Multi-agent work" is amended for Q37–Q38 (a hard-limit edit: David approves the diff) and records the final D-number.
- The `.claude/settings.json` allowlist exists and David has approved it once.
- One full autonomous run has completed, with its run summary in `log.md`.

## Review
## Outcome
