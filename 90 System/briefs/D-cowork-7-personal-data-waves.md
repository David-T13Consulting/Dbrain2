---
classification: internal
task: OQ-11 / P1.4 / T8   # provisional; the lead assigns the final task and D-number
owner: "@code"            # David approved 5 Oct (Q20); lead amends data-policy and TASKS
status: open
models: []
created: 2026-10-05
---
# Data-policy v0.4 proposal: personal data enters in gated waves (provisional D-cowork-7)

## Goal (one sentence)
Define when and under which gates personal data beyond training/HR may enter Dbrain2, starting with children's schedules (no names) in wave 1.

## Decisions already taken by David (5 Oct, via Cowork; queue Q18–Q19)
- Wave gating **accepted as proposed** (below).
- First wave-1 use case: **kids' schedules without names**: school lunches/menus, climbing practice and similar activity timetables. Mostly wave 1, on top of wave 0.

## Proposed policy text (for David to approve or edit, rule 8 / policy §8)

### Waves

| Wave | Content | Labels (Q10 axes: domain · sensitivity · processing · sharing) | Gate before entry |
|---|---|---|---|
| 0 (in force) | David's own training and HR data | personal · sensitive · approved external · approved for demo (§4, David's explicit choice) | none, already permitted |
| 1 | Ordinary personal material: routines, family logistics without names, reading, goals, non-financial planning | personal · ordinary · approved external · private | **P1.4 four-axis retrofit complete** and the lint check validates the four axes on new notes |
| 2 | Sensitive personal material: health beyond training, finances, journal | personal · sensitive · **local-only** · private | All five: (a) P2.2/P2.3 local query service answers with no silent cloud fallback; (b) cloud agents (Cowork, Claude Code, Codex, claude.ai Project) **cannot reach** wave-2 files, verified by an access test, not by labels; (c) synthetic sensitive-note leak test passes (titles, search, listings, logs, traces, agent handoffs); (d) trace redaction live; (e) deletion rule for git history and backups decided |
| never | Others' sensitive data, client material, secrets | policy §2, unchanged | — |

### Children's data rule (new §3a)
1. **No names, initials or nicknames.** Use neutral labels ("child A", "child B") or none at all.
2. **No identifying places.** No school, club or gym names, no addresses. Use generic nouns ("school", "climbing club").
3. **No health, behaviour, performance or photos** of children, whatever the tier (extends §2.4).
4. **Never shown in a demo.** Demos use a synthetic family.
5. **Manual capture only** for now (Inbox → triage). No portal, email or website integrations before month 4 (no MCP sprawl).
6. Logistics only: what, when, what to bring or prepare. This feeds the parked second domain (OQ-11) as **data, not a built feature**. No family-logistics features until the H1 gate.

### Known tension
Gate (b) will probably need a separate local-only store outside the paths granted to cloud agents. That revisits Q10 (labels only, no vault split) **at wave 2, not now**. A separate purgeable repo would also satisfy gate (e).

## Files in scope (once approved)
- `10 Projects/AI Second Brain/02_Architecture/data-policy.md` → v0.4 (the lead edits; only David changes policy)
- `10 Projects/AI Second Brain/OPEN_QUESTIONS.md` → OQ-11: children's-data rule answered; second domain stays parked
- `10 Projects/AI Second Brain/TASKS.md` → wave-1 entry gated on P1.4; wave-2 gates linked to P2.2/P2.3, T8, T12, P6.1

## Done when (checkable)
- David approves or edits the text above.
- data-policy.md is at v0.4 with the waves table and §3a, and the decision is recorded in PROGRESS with a final D-number.
- No personal data beyond wave 0 has entered the vault before P1.4 is ticked.

## Constraints
- Rule 8: Cowork proposes; nothing is populated until David confirms.
- Policy §8: only David changes the policy.
- Labels inform controls; they never grant access by themselves.

## Review
**David approved the proposed text as written on 5 Oct 2026 (queue Q20).**
## Outcome
