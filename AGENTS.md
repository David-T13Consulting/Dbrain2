---
classification: internal
---
# AGENTS.md: Dbrain2

David's personal second brain: an Obsidian vault of plain markdown, tracked in git.
PARA layout: 00 Inbox · 10 Projects · 20 Areas · 30 Resources · 40 Archive · 90 System.

## Hard rules
1. **Read-only.** Only create, edit, move or delete a file when David asks for that change in this session.
2. **Keep out:** client or counterparty confidential information, secrets (keys, tokens, passwords),
   and sensitive data about anyone but David. If you find any, stop and flag it.
   Full policy: `10 Projects/AI Second Brain/02_Architecture/data-policy.md`.
3. Every note has `classification: public | internal | client` in its frontmatter. A note tagged `client` is a violation, so flag it.
4. **Propose, don't populate.** Nothing enters 10–40 as structured knowledge until David confirms it.
5. Large files (PDFs, media, recordings) never go in the vault. Leave a pointer note (path and one-line summary) instead.
6. **When unsure, stop and ask.** This covers ambiguous requests, missing data and unclear classification. Don't guess.

## Conventions
- Write in English. Transcribe French captures as spoken; translate at triage.
- `00 Inbox/` holds raw captures named `YYYY-MM-DD-HHmm-<slug>.md`. Don't process them unless David asks for triage.
- Find things with file search (grep/glob). There is no vector index.
- Link notes with `[[wikilinks]]`.
- After each change David approves, commit with a message saying what changed and why.

## Wiki operations
- `index.md` (vault root) catalogs the notes in 10–40 and 90. `log.md` is append-only; each entry starts `## [YYYY-MM-DD] op | title`.
- Appending to either for a change David approved this session counts as part of that change.
- Ingest one source at a time: discuss takeaways with David, propose the pages to create or update, wait for approval, then write, update `index.md` and append to `log.md`.
- Query: read `index.md` first, then the pages. If an answer is worth keeping, propose it as a note (classification and sources included) and file it only after David confirms.
- Lint weekly with `90 System/lint-checklist.md`. Report findings read-only; fix only what David approves.

## Multi-agent work
Adopted 1 Oct 2026 (D63). Design record: [[40 Archive/agent-orchestration-proposal|agent-orchestration-proposal]].
- **Lanes.** Cowork: capture, specs, research, briefs; never runs git (to inspect the tree it may
  run only `git --no-optional-locks status`, because a plain `git status` leaves a stale
  `index.lock` that its sandbox cannot remove). Claude Code: lead, build, integration, git,
  session-close bookkeeping. Codex: independent reviewer and scoped side tasks given to it by
  the lead; never commits.
- **One queue.** Every open task in TASKS.md has an owner tag (@cowork @code @codex @david).
  Work handed between agents needs a brief in `90 System/briefs/<task-id>.md` (template:
  `_template.md`). Touch only the files the brief lists.
- **Commit straight to `master`; keep history linear.** Only the lead commits. Branch only
  for speculative work and delete the branch when it lands (D50).
- **Review before commit.** The lead runs Codex read-only on each diff against these rules
  and records its findings in the brief. Codex gets the rules and the diff, not the lead's reasoning.
- **IDs.** Only the lead hands out final D-, OQ- and session numbers. Other agents use
  provisional IDs (`D-cowork-1`); the lead renumbers them and logs the mapping in `log.md`.
- **Tracking files.** PROGRESS.md, TASKS.md and OPEN_QUESTIONS.md are updated by the lead.
  Other agents put their updates in the brief or in `handoff.md`.
- Cowork lists its uncommitted changes in `90 System/handoff.md`; the lead commits them
  first, as their own commit, then clears the entry.
- Never commit, revert or overwrite another agent's uncommitted files unless they are in the
  handoff. If unsure, stop and ask David.

## Model policy
Adopted 1 Oct 2026 (D64). David sets this policy; config files apply it; agents do not pick models outside it.

| Lane | Model | Where it is set |
|---|---|---|
| Cowork: thinking, specs, briefs | Strongest Claude model (Opus) | App model picker (David) |
| Claude Code: lead | Opus | `.claude/settings.json` in the vault (git-tracked) |
| Claude Code subagents: search, tagging, simple checks | Smaller Claude model | `model:` field in each subagent definition |
| **Codex: reviewer** | **GPT-6 Astra at effort `high`**, escalating to `ultra` only when the lead and the reviewer are both stuck | `~/.codex/review.config.toml`; the lead calls `codex exec --profile review` |

- The review is independent because it uses a different vendor's model. Do not swap the reviewer to a Claude model.
- Reviewer setup (D64, David 2 Oct): the standalone CLI is installed at `~/.local/bin/codex`, not the copy bundled inside the ChatGPT app. From Codex CLI 0.159 a profile is **its own file** (`$CODEX_HOME/<name>.config.toml`), not a `[profiles.<name>]` section in `config.toml` — look in the right place before concluding the profile is missing.
- Every brief records the model ID(s) actually used, under Review and Outcome.
- This is about the agents that build the vault. The local runtime model (T9 / P2.2) is chosen by evals against D56, not by this policy.
- Change this table only on David's decision.

## Where to start
- Active work lives in `10 Projects/<name>/`. Read that project's CLAUDE.md or README first.
- Conventions written for humans are in `90 System/README.md`.
