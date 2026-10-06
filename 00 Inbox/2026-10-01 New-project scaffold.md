---
captured: 2026-10-01
source: claude.ai chat (Project: AI Second brain setup), Claude-authored proposal
classification: internal
status: unprocessed
tags: []
---

# New-project scaffold: template + skill + guardrails

> Claude-authored proposal, not yet confirmed by David. Triage before promoting to the vault (rule 8).

Context: follows the decision that the vault holds *what and why* (knowledge, read-only reference for builds) and each dev repo holds *how and running*. Two separate git repos, never nested. Standing home for builds: `~/Documents/Code/<project>/`.

## Core idea
Instructions get forgotten. Encode the structure once as a scaffold skill, then enforce it with settings. Three layers: template, skill, guardrails.

## 1. Template (in vault: `90 System/templates/new-repo/`)

| File | Content |
|---|---|
| `CLAUDE.md` | Build commands, structure, conventions, and the line "Spec and decisions live in `<vault path>`. Read, don't edit." |
| `.claude/settings.json` | Allow Read on the vault path, deny Edit/Write on it |
| `.gitignore` | `.env*`, `data/`, `*.key`, large-file patterns |
| `.env.example` | Variable names only, no values |
| `README.md` | Purpose, how to run, link to the vault pointer note |
| `data/README.md` | "Fixtures only. Real or personal data stays in `Source_Material`" |
| pre-commit secret scan | Enforces rule 2 mechanically (e.g. gitleaks) |

## 2. Skill: `new-project` (SKILL.md in the vault, runs in Claude Code, not Cowork, because Cowork never runs git, D50)

1. Ask 3 questions: project name, one-line purpose, data classification (`public|internal|client`).
2. Refuse to proceed if the answer is "client" (rule 1).
3. Create `~/Documents/Code/<name>/` from the template and run `git init`.
4. Fill placeholders (vault path, project name, classification).
5. Install the pre-commit hook and make the first commit on `master`.
6. Draft a pointer note (repo path, purpose, status, how to run) into `00 Inbox/`, not the vault proper. David confirms at triage (rule 8).
7. Print a checklist of what was created, so it can be verified rather than trusted.

## 3. Guardrails

| Layer | Mechanism | Catches |
|---|---|---|
| Trigger | One line in project instructions: "Starting a new build → use the `new-project` skill, never create repos ad hoc" | Forgetting the procedure exists |
| Rule | Same line in the vault's `AGENTS.md` | Agents improvising in the vault |
| Permissions | Deny Write on the vault path in the template settings | Build sessions editing knowledge directly |
| Secrets | Pre-commit scan plus git-ignored env | Tokens in a repo (Telegram token incident) |
| Audit | Monthly check: every repo in `~/Documents/Code/` has a pointer note, and every pointer note has a repo | Drift and orphaned projects |

## Options and trade-offs

| Option | Pro | Con |
|---|---|---|
| A. Template folder only | Simple, no skill needed | Manual copy, placeholders get skipped |
| B. Skill + template | Repeatable, includes the gate and checks | Upfront build time, skill needs testing |
| C. GitHub template repo | Standard, one click | Doesn't create the vault pointer or vault-side permissions |

Claude's recommendation: **B**. Build the skill by scaffolding the first real project (the Strava harness), then extract what worked.

## Caveats
1. Permission settings are enforcement, instructions are not. Test once: ask an agent to edit the vault from the repo and confirm it's blocked.
2. The skill is itself a governed artifact. Version it in the vault and note changes in the decision log.
3. Don't build this before the Week 0 gate items are done (depth over breadth, rule 3).

## Related decision proposed in the same discussion
Golden set split (option C): rubric lives in the vault (definition of "good" is a decision); labeled Strava data lives in the repo (personal and bulky, kept out of the vault per the large-file rule).

## Open question
Write the first draft of the template and SKILL.md now, or after the Strava harness provides a real project to extract from?
