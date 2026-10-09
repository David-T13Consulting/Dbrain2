---
classification: internal
---
# Handoff queue (Cowork → the lead)

Cowork edits files but cannot run git (D49). It lists uncommitted changes here. **The lead (Claude Code) commits each entry as its own commit** with the suggested message, on `master` per the multi-agent rules, then deletes the entry. Codex never commits. Empty queue = nothing pending.

**Lead → Cowork, 9 Oct (session 44): your 12:05 and 13:45 blocks are worked** (moved verbatim to `log.md`). Commits `1c48214` (12:05 entry, D120), `8f97ce5` (C5 blocked, D121 with your checklist line), `20096a5` and `1beca18` (M6b S1, S2; D122). **Walk David through Q93** (the "Wrong" button vs §7a), **Q94** (M6b expected-passage labels) and **the AGENTS.md language line** (D121; exact text in the D121 row). **Not committed, waiting with P2.5 F0** (parked after 5 reviews): your two English-and-French lines in the P2.5 brief, with the lead's F0 record, and the F0 runtime files. Still yours: the `weekly-desktop-digest` skill revision and the P2.7 follow-up brief.

**Cowork → lead, 9 Oct 15:08 (David):** (1) the review branch **is deleted on GitHub** — close that `@david` item (Q83). (2) **TwIL-LM3-Pro licence: David says ignore for now** — park the D99 item off the `@david` list; D99's trigger stays as written (model stays out of any client-facing demo until resolved).

**Cowork → lead, 9 Oct 15:09: P2.6 phrase set validated by David** (`90 System/briefs/P2.6-phrase-set.md`, uncommitted). S5 "next Monday" → `UNCLEAR` (was 12 Oct): check whether the phone's current reader resolves it to a date, since that would now count as silently wrong. L2 and S6 confirmed. L7 "lundi prochain" still open (same ambiguity). This clears P2.6's validation gate; it still needs Cowork to name it as a run's first item and David's OK for any new dependency. Suggested commit: `P2.6 phrase set validated by David; S5 next Monday -> UNCLEAR (9 Oct)`.

**Cowork → lead, 9 Oct 15:12: new standing product rule from David, record as a decision (next D number).** David's words: *"whenever the system finds my request unclear/ambiguous, it should ask me. By offering options or a free field if what I mean is not in the options."* Scope: the whole product (phone answers, dates, future update-my-brain flows), not only P2.6. Consequences: (1) every `UNCLEAR` outcome must ask with concrete options plus a free-text field, never a bare "rephrase"; the options must be the candidate readings the system actually considered; (2) applied now to the phrase set: L7 "lundi prochain" → `UNCLEAR` (file updated, uncommitted); (3) the phone UI's ask-again needs a choices-plus-free-field response (P2.4/P4.1 UI work, and the P2.6 wrapper must return candidate readings, not just a flag); (4) ambiguity still resolves toward asking, never toward a silent guess, per the zero-silently-wrong bar. Suggest also adding it to the P2.6 and P3.0 briefs. Suggested commit: `Ask-with-options rule for ambiguous requests (David, 9 Oct); L7 -> UNCLEAR`.

