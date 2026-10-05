---
classification: internal
task: D72                # was provisional D-cowork-8
owner: "@code"
status: in-review          # rounds 7-8 failed, round 9 at David's instruction; open after commit until one full autonomous run
models: ["claude-opus-5-5 (lead, AGENTS.md and settings)", "gpt-6.1-sol (review)"]
created: 2026-10-05
---
# Autonomous runs: keep working until the credit runs out or real work does (D72, was D-cowork-8)

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
*Historical: the proposal as approved. The rules actually committed are narrower; see Outcome.*
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
Proposal and answer records: Codex PASS (`6985ee1`), its should-fixes carried into the lead's drafts (activation gate, retry accounting, per-item scope, narrower Python permissions, model IDs). The AGENTS.md amendment and settings: round 1 (`gpt-6.1-sol`) FAIL — runtime rules files and `.claude/` not protected; the `curl` ask rule overrode the health-check allows; the brief closed before its run; Bash rules lack directory scope; log wording. Round 2 FAIL — sandbox profiles pre-approved for editing; directory scope only documented; overstated wording on unlisted commands; title. Fixed: `*.sb` edits ask; git and scripts allowed only with absolute repository paths; wording corrected; title updated. Round 3 FAIL — prefix rules still pre-approved dangerous flags (`switch --orphan`, `diff --output`, Codex sandbox overrides) and the ask/deny rules missed the `git -C` form. Fixed by narrowing the allowlist and adding ask/deny rules. Round 4 FAIL — pre-approved test and scan runs execute lead-editable code; the runtime's security-boundary files were editable unasked; scanner working directory; wording. Fixed: no execution of editable code is pre-approved; boundary files ask; wording corrected. Round 5 FAIL → **parked for this run, nothing committed** (D72). Codex confirmed AGENTS.md implements Q37–Q40 and D73 faithfully and the D72/D73 bookkeeping is accurate. Open for the next run, all of them **more ask rules, no new allows**:
1. **blocker:** edits to the MVP start-up scripts (`mvp/run-all.sh`, `mvp/Ask Brain.command`, `mvp/make-shortcut.sh`, `mvp/make-token.sh`, `mvp/prepare-model.sh`) must ask: they set the bind address, offline mode and the token handling.
2. **blocker:** edits under both repositories' `.git/` (config, hooks) must ask explicitly, not rely on Claude Code's built-in protected paths (which go to the classifier in auto mode); and nested `CLAUDE.md` / `AGENTS.md` files anywhere in the vault (e.g. the project's own `CLAUDE.md`), not only the roots.
**Round 6, at David's explicit instruction ("have Codex pass what's needed before the commits"), lifting the run's park for this item:** both gaps closed with ask rules only: edits under `dbrain-runtime/mvp/`, under both repositories' `.git/`, and to any `CLAUDE.md` or `AGENTS.md` at any depth in either repository now ask. Round 6 FAIL: `.claude/` folders below the roots were not covered. Rather than find one gap per round, the lead asked Codex (as a consultant, separately from review) for the complete rule set; its answer is recorded below (Outcome). Fixed: nested `.claude/` asks; the brief now states what the file guarantees and what it cannot. Round 7 (fresh) FAIL: existing scripts embedding sandbox and bind settings (`measure.sh`, `experiments/`) were editable unasked; data-policy and `.gitignore` coverage overstated; the historical allowlist section unmarked. Fixed from a grep inventory of every file embedding a security setting (recorded in Outcome); exact coverage stated; historical section marked. Round 8 (fresh) FAIL: Obsidian's plugin settings (`.obsidian/`) were editable unasked. Fixed by closing the class: every hidden file or folder in both repositories asks (the dot-folders present are `.claude`, `.git`, `.obsidian` and `.gitignore`). Round 9 is a fresh review.

## Outcome
**5 Oct, lead (`claude-opus-5-5`):** **D72.** David approved both drafts unchanged, plus pre-approved edits in the vault and `dbrain-runtime`, and asked the lead to commit them. Applied:
- `AGENTS.md`: stop conditions rewritten (stop only on no actionable work, the usage limit, or something unsafe); review failures fixed and re-reviewed up to **5 reviews per brief per run, the first included**, then parked `in-review`; "no commit without a Codex pass"; the backlog orders work but each item runs under its own brief and file list; the hard-limit list; the retry limit now covers commands, tests and scripts only. Also **D73**: the reviewer line now names GPT-6.1 Sol.
- `.claude/settings.json`, **narrowed during review from the approved draft** (it pre-approves less, never more). **Allow:** reads and edits in both repositories; five exact read-only git commands per repository (`git -C <repo> status`, `--no-optional-locks status --short`, `diff --stat`, `diff --cached --stat`, `log --oneline -10`; exact matches, so no added flag is approved); `tailscale status`; the two loopback health checks. **Nothing that executes code the lead can edit is pre-approved:** not the test suite, the secret scan, the project scripts, commit, merge, switch or the Codex call; those go through the auto-mode classifier or a prompt. **Ask (exact coverage):** edits to **any hidden file or folder at any depth in either repository** (`.obsidian/` plugin settings, `.claude/`, `.git/`, `.gitignore`, and any future config folder), to any `AGENTS.md`, `CLAUDE.md`, `data-policy*.md`, `.gitignore` and `.claude/` at any depth in either repository, and anything under either repository's `.git/`; any `*.sb` sandbox profile; in `dbrain-runtime`, the security-boundary code (`dbrain/config.py`, `scope.py`, `outpath.py`, `index.py`, `adapter.py`, `serve.py`, `trace.py`), everything under `mvp/` and `experiments/`, `measure.sh` and `secret_scan.sh`; `~/.codex/` and `~/.claude/`. **Inventory behind it (5 Oct, reproducible):** `grep -rlE "sandbox-exec|deny network|--host|--offline|127\.0\.0\.1|0\.0\.0\.0|find-generic-password|security add-generic|Bearer|ProxyHandler|RefuseRedirects|O_NOFOLLOW|classification|launchctl|caffeinate|tailscale"` over the runtime's `.py`, `.sh`, `.sb` and `.command` files lists only those files plus tests. Commands, in the `git -C <repo>` form: push, reset, rm, clean, branch deletion, orphan checkouts, restore, filter-branch, update-ref, config; in the plain form: push, reset, rm, clean, branch deletion, config; and Keychain (`security`), `launchctl`, `sudo`, `wget`, `huggingface-cli`, `open`. **Deny:** force push, both forms.
- **What the allowlist is, and is not (Codex consultation, 5 Oct).** Asked for a complete rule set in one step, Codex answered that **no selective rule file can guarantee the hard-limit list while pre-approving ordinary edits**: paths cannot recognise future security code, a `client` label inside a file, or a bulk change accumulated over many calls, and Bash patterns match command text, not what a program does. The only complete rule set is "ask for every call", which ends unattended work. So the settings file is a **convenience layer with one firm property: it pre-approves no known hard-limit target** (policy and rules files and `.claude/` at any depth, `.git/`, sandbox profiles, the runtime's security-boundary code and start-up scripts, Keychain, launch agents, deletion, push, downloads). The hard limits are enforced in layers: the AGENTS.md rules the lead follows, the Codex review before every commit (Q40), the auto-mode classifier, and David's prompts on the listed asks.
- **Residual risks, stated:** a new security-relevant file in an unlisted place is editable unasked until it is added (re-run the inventory grep when adding code); tests that check the boundaries are editable unasked, though editing a test does not change what the service does and every test change passes Codex before commit; approved commands can have indirect effects through code, git configuration, hooks or running services; activity outside tool calls (start-up hooks, plugins, loaded instructions, the running MVP service) is not gated by this file; wildcard and sandbox behaviour depend on the installed Claude Code version and have not been tested against it.
- **Trade-off, for David:** an autonomous run will meet more prompts (or classifier decisions in auto mode) than the draft promised: every test run, commit and review call. That is the price of not letting code the lead writes run unasked. Loosening it again is David's call.
- **Activation:** the runbook applies from a **fresh Claude Code session** started after this commit, so the new permissions are loaded.
