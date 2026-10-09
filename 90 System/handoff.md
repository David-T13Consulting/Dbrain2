---
classification: internal
---
# Handoff queue (Cowork → the lead)

Cowork edits files but cannot run git (D49). It lists uncommitted changes here. **The lead (Claude Code) commits each entry as its own commit** with the suggested message, on `master` per the multi-agent rules, then deletes the entry. Codex never commits. Empty queue = nothing pending.
