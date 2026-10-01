---
classification: internal
---
# Handoff queue (Cowork → git agent)

Cowork edits files but cannot run git (D49). It lists uncommitted changes here. The git agent (Claude Code / Codex) commits each entry as its own commit with the suggested message, on a branch per the multi-agent rules, then deletes the entry. Empty queue = nothing pending.

## [2026-10-01] History note, no file change
Local `master` is 2 commits ahead of `origin/master` and unpushed: `ec28796` (Cowork, LLM Wiki D41–D44) and `d4eed10` (Codex, roadmap S1–S6). Linear, no conflict. Recommended: do not rewrite history; push it as a branch (e.g. `integration/2026-10-01`) and open one PR into `master`.
