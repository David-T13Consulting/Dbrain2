---
classification: internal
source: Cowork session, 1 Oct 2026 (David's request to orchestrate Cowork, Claude Code and Codex)
review_status: approved
note_type: decision
archived: 2026-10-01
created: 2026-10-01
updated: 2026-10-01
---
# Proposal: one lead, one queue for the three build agents (Cowork · Claude Code · Codex)

> **Status: APPROVED by David, 1 Oct 2026**, adopted as **D63** (written as provisional `D-cowork-1` until the lead renumbered it at integration, session 13). Decisions: option B (Claude Code as lead) · Codex as reviewer · this record archived once adopted. §5 is now live in `AGENTS.md`.

## 1 · The problem as stated

- **Real pain:** routing and context switching. David decides which agent gets each task, re-briefs each one, and keeps the state in his head.
- **Not a real pain:** git conflicts. David reports almost none. D50 (single committer, linear `master`) already works.
- **Observed friction (from PROGRESS, 1 Oct):** six agent sessions on a single day (Codex 7, 9, 10 · Cowork 8, 11 · Claude Code 12). Two of them claimed the same IDs: Cowork took D51/OQ-19 while Claude Code was working, so session 12 had to renumber. Sequential IDs are the only shared counter, so that is where agents collide.

**Out of scope:** this is about the agents that *build* the system. It is not the runtime multi-agent design in S5/T11 (coordinator, curator, evidence checker). Keep them separate. Evidence from this process may feed S5, but it is not S5.

## 2 · Options considered

| Option | How it works | Removes routing load? | Cost | Verdict |
|---|---|---|---|---|
| A · Lanes + shared queue | Fixed role per agent; owner tag on every task; David still starts each agent | Partly | Very low | The base layer |
| **B · A + Claude Code as lead** | Claude Code is the one session David opens in VS Code. It reads the queue, does the build work, and calls Codex itself from the terminal (`codex exec`) for review or for well-scoped side tasks | **Mostly** | Low: both CLIs already sit in the same VS Code terminal | **Recommended** |
| C · Relay / baton | Only one agent active at a time, handing over strictly | No | Slower, loses parallel work | Rejected: conflicts are not the problem |

## 3 · Recommended design (option B)

### 3.1 Lanes

| Agent | Lane | Writes | Never |
|---|---|---|---|
| **Cowork** | Front door: phone captures, thinking and specs, research, interviews with David, **writing briefs** | `00 Inbox/`, `90 System/briefs/`, `handoff.md`, and notes David approves | git; IDs from the shared sequences (§3.4) |
| **Claude Code** | **Lead.** Build work (skills, scripts, eval harness), integration, git, session-close bookkeeping (PROGRESS / TASKS / OPEN_QUESTIONS), handing out IDs | Anything in scope of a brief it holds; the only one to commit | Committing without the review step in §3.3 |
| **Codex** | **Independent reviewer** (second model), plus well-scoped side tasks given to it by the lead | Only the files listed in its brief | Committing; changing the shared tracking files |

### 3.2 One queue

- Every open task in `TASKS.md` carries an owner tag: `@cowork` · `@code` · `@codex` · `@david`. David's own actions are already listed in TASKS; this makes them filterable.
- Work handed from one agent to another gets a brief at `90 System/briefs/<task-id>.md` (template in §4). The TASKS line links to it. **No brief, no hand-off.**
- Status lives in the brief's frontmatter: `open → claimed → in-review → done`. When a brief is done, the lead moves it to `40 Archive/briefs/` while integrating.

### 3.3 Lead loop (Claude Code, one session)

1. Commit the `handoff.md` entries (existing D50 rule).
2. Read open briefs tagged `@code` and `@codex`; claim one.
3. Do the work, or hand a well-scoped side task to Codex: `codex exec "<brief path>: do X, touch only the listed files"`.
4. **Review step:** before each commit, the lead runs Codex read-only on the diff against the vault rules: `classification:` present, no secrets, no client data, D59 frontmatter on new notes, nothing outside the brief's scope. Findings go into the brief, under `## Review`.
5. Commit, then update PROGRESS / TASKS / OPEN_QUESTIONS once, at the end of the session.

*Check the exact `codex exec` sandbox and approval flags for your installed version before scripting step 4.*

### 3.4 Shared IDs (fixes the D51/OQ-19 collision)

- **Only the lead hands out final D-, OQ- and session numbers.**
- Other agents write provisional IDs: `D-cowork-1`, `OQ-codex-1`. The lead renumbers them at integration and adds the old→new mapping to `log.md`.
- New IDs do not need to follow this pattern: D57 source IDs are hash-based and never collide.

### 3.5 David's loop

| When | Where | What |
|---|---|---|
| Throughout the day, on any device | Cowork | Capture, think, decide; Cowork turns decisions into briefs |
| One build block a day | VS Code → Claude Code | "Run the lead loop." It pulls briefs, uses Codex, reviews, commits, updates tracking |
| Session start, any agent | — | "where am I?" reads TASKS (with owner tags) and the open briefs |

### 3.6 Guardrails

- **Cap the setup at about one session.** This is plumbing, not the showcase. The demo is still the running pipeline and the S2 query service.
- The review step only counts as governance evidence if Codex reviews **independently**: it gets the rules and the diff, not the lead's own reasoning.
- **Revisit trigger:** if two weeks pass and David still re-briefs agents by hand, or briefs go stale for more than three days, the queue is overhead. Fall back to owner tags only.

## 4 · Brief template (`90 System/briefs/_template.md`, created only on approval)

```markdown
---
classification: internal
task: P2.2            # TASKS.md ID
owner: "@code"        # @code | @codex | @cowork | @david
status: open          # open | claimed | in-review | done
created: YYYY-MM-DD
---
# <task title>
## Goal (one sentence)
## Files in scope (agent may touch only these)
## Inputs / context to read first
## Done when (checkable)
## Constraints (vault rules that especially apply)
## Review   ← filled by Codex: findings, verdict
## Outcome  ← filled by owner: commit hash, open issues
```

## 5 · Proposed replacement for `AGENTS.md` → "Multi-agent work"

```markdown
## Multi-agent work
- **Lanes.** Cowork: capture, specs, research, briefs; never runs git (to inspect the tree it may
  run only `git --no-optional-locks status`, because a plain `git status` leaves a stale
  `index.lock` that its sandbox cannot remove). Claude Code: lead,
  build, integration, git, session-close bookkeeping. Codex: independent reviewer and
  scoped side tasks given to it by the lead; never commits.
- **One queue.** Every open task in TASKS.md has an owner tag (@cowork @code @codex @david).
  Work handed between agents needs a brief in `90 System/briefs/<task-id>.md`. Touch only
  the files the brief lists.
- **Commit straight to `master`; keep history linear.** Only the lead commits. Branch only
  for speculative work and delete the branch when it lands (D50).
- **Review before commit.** The lead runs Codex read-only on each diff against these rules
  and records its findings in the brief.
- **IDs.** Only the lead hands out final D-, OQ- and session numbers. Other agents use
  provisional IDs (`D-cowork-1`); the lead renumbers them and logs the mapping in `log.md`.
- Cowork lists its uncommitted changes in `90 System/handoff.md`; the lead commits them
  first, as their own commit, then clears the entry.
- Never commit, revert or overwrite another agent's uncommitted files unless they are in the
  handoff. If unsure, stop and ask David.
```

## 5b · Incident found while drafting (1 Oct)

While drafting this proposal, Cowork ran a plain `git status`. Git tried to refresh the index, and Cowork's sandbox could not remove the `.git/index.lock` it created. That empty, stale lock would have blocked the next commit. With David's permission it was deleted at once. The `--no-optional-locks` rule in §5 prevents a repeat.

## 6 · Decisions (answered 1 Oct by David)

Answers: 1 → option B approved · 2 → Codex as reviewer · 3 → archive.


1. Approve option B (Claude Code as lead), or stay with A (owner tags only)?
2. Codex's main job: **reviewer** (recommended) or **parallel builder**?
3. Should this proposal move to `40 Archive/` once adopted, or stay here as the design record?
