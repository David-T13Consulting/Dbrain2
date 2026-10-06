---
classification: internal
task: M3
owner: "@code"
status: open
models: [claude-opus-5-5 (Cowork, draft)]
created: 2026-10-06
---
# M3 · Archive ui-design-agent, claude-blueprint and agentic-ios-app

## Goal (one sentence)
Take three inactive repos out of `~/Work` and out of active use on GitHub, reversibly and without losing anything.

## Why (David, 6 Oct, via Cowork, Q66)
They are not part of the second-brain work. Archiving keeps `~/Work` down to live projects. Q66 = local move **and** GitHub archive.

## Facts checked by Cowork (6 Oct, read-only)
- No live reference to the three in the vault or `dbrain-runtime`; only dated history (log, PROGRESS, M1/M2 briefs, handoff notes). Leave those as they are.
- M1 gate: all three were 0 ahead / 0 uncommitted on 6 Oct (ui-design-agent `d4dfc44`, claude-blueprint `3ed6463`, agentic-ios-app `fac922b`). Q58: the ui-design-agent patient fixture is invented (David).
- Not checked (Cowork can't see it): `~/.claude`, `~/.codex`, VS Code, launch agents, symlinks into `claude-blueprint`.

## Steps
1. **Pre-flight, per repo:** `git --no-optional-locks status --short` empty and `@{u}..HEAD` = 0. Anything else → stop, queue for David (D68), do not commit on his behalf.
2. **Reference check, named files only:** `grep -n` for the three names and their `~/Work/...` paths in these configuration files, where they exist: `~/.claude/settings.json`, `~/.claude/settings.local.json`, `~/.claude/CLAUDE.md`, `~/.codex/config.toml`, `~/.codex/*.config.toml`, `~/Library/LaunchAgents/*.plist`, both repos' `.claude/settings*.json`, and VS Code's `~/Library/Application Support/Code/User/settings.json` and `.../User/globalStorage/storage.json` (recent workspaces). **Never read** `~/.codex/auth.json`, session or history folders, or any credential store. Symlinks: `find ~/Work -maxdepth 3 -type l` and `find ~ -maxdepth 1 -type l`, which lists no folder's contents and never enters `~/Archive` (data policy v0.5). Any live hit other than dated history or dead `settings.local.json` entries → stop and queue it.
3. **Move:** each to `~/Work/_archive/<name>` (target-absent and real-parent check first, as in M2). Verify: source gone, target present, `git fsck --full` exit 0, HEAD unchanged.
4. **GitHub:** `gh repo archive <owner>/<name> --yes` for each (reversible with `gh repo unarchive`). Confirm with `gh repo view <owner>/<name> --json isArchived` for each. This is a remote change: David approved it in Q66; it still goes through the permission prompt.
5. **Record:** Outcome below (before/after heads, gh results), a PROGRESS decision row (final D-number), `log.md`, handoff note.

## Files in scope
This brief; `log.md`; PROGRESS; TASKS; `90 System/handoff.md`; `90 System/for-david.md` (clear Q66). Outside the vault: the three folders' location only. No edits inside the three repos.

## Done when
- [ ] Three folders in `~/Work/_archive/`, fsck clean, heads unchanged.
- [ ] All three `isArchived: true` on GitHub.
- [ ] No live reference left (step 2 output recorded).

## Constraints
No deletion, no force-push, no commit inside the three repos. Reversible only.

## Review
**Lead review of Cowork's entry (Q65, Q66, this brief, handoff block), 6 Oct (session 28), Codex `gpt-6.1-sol` (review profile), high, read-only.** Round 1 FAIL on this brief: (1) `find ~ -maxdepth 3` would traverse `~/Archive/medispring-infi`, which data policy v0.5 forbids agents to list; (2) a recursive `grep` over `~/.codex` would read its credential store (`auth.json`). Should-fix: name the repository in `gh repo view`; include VS Code in step 2; and, in the handoff, the BENCH check (`--help` doesn't load `dev.json`), the committed M2 follow-up row, and the old block's "no push beyond M2" line. The lead fixed step 2 (named files only, no credential stores, no traversal into `~/Archive`) and step 4 here; the handoff points go in the lead's close note.

## Outcome
