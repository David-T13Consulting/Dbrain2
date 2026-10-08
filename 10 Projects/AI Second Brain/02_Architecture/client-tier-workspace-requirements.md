---
classification: internal
review_status: approved   # David, Q80 (a), 8 Oct: Tier 2 approval of the note as reviewed (legal points stay `unverified` for the T0.7 lawyer review)
note_type: requirements
source: David, Cowork session 7 Oct 2026 (decisions marked "David"); everything else is Cowork's proposal
created: 2026-10-07
updated: 2026-10-08
---
# Client-tier workspace: requirements that shape the Dbrain2 build

**Why this note exists.** From November David works as a Tower13 subcontractor and needs an AI-assisted workspace for client business development: dense notes on accounts, people, placements, signals, opportunities and meetings. That material is `client` tier, so it **never** enters Dbrain2 (data policy §1, §2.1, §6). It lives in a **separate, segregated vault**. This note records only what that means for how Dbrain2 and `dbrain-runtime` are built. It deliberately names no client, counterparty or person (§6: nothing about an engagement enters before its contract states AI use).

## Decisions (David, 7 Oct)
1. A separate vault for client-tier work, not a client tier inside Dbrain2.
2. AI processing for it: **Claude and Codex on commercial plans** (verify each plan's data terms, no training on inputs, before the first real note).
3. The system must **process meeting recordings** (Apple Voice Memos or other recorders).
4. Contract AI-use clause (T0.7, made concrete by this subcontract): Cowork drafts it **the week of 12 Oct**.
5. Scaffolding the client vault: **the week of 12 Oct**, not now.

## Requirements on Dbrain2 / dbrain-runtime (proposed by Cowork)
| # | Requirement | Why | Affects |
|---|---|---|---|
| R1 | **Multi-vault by configuration.** The runtime takes its vault root, policy and allowlist from config; one instance per vault; an instance never indexes, reads or writes another vault. No hard-coded Dbrain2 paths | The phone service indexes the whole vault today ([[90 System/briefs/MVP-phone|MVP-phone]], the `mvp-whole-vault` profile); pointed at the wrong root it would mix tiers | P2.2 config, P2.4 MVP, P6.2 |
| R2 | **Per-vault data policy and labels.** The client vault carries its own policy; the label allowlist is per vault (Dbrain2 refuses `client`; the client vault accepts it) | The Q46 allowlist is the right mechanism; it just has to be parameterised | P2.2 label check |
| R3 | **Recording ingest pipeline:** audio file → local transcription → transcript as evidence → proposed structured notes (interaction, signals, next steps) → David confirms (rule 8) → audio deleted | Meetings are the main input; rule 8 defines the shape. **Proposed client-vault rule, differs from D58:** D58 deletes Dbrain2 voice audio on successful transcription; here the audio would be kept until David confirms the notes | P4.3 (pull forward), P3.x writer |
| R4 | **Local transcription only** (whisper.cpp class), no cloud ASR | Client meeting audio is the most sensitive artifact; local is the cleanest answer | P4.3, M6 voice fixtures |
| R5 | **Languages: French, English and Dutch**, mixed within a meeting | Brussels business meetings; current P4.3 plans test FR/EN only | P4.3 test fixtures |
| R6 | **Speaker attribution** (who said what), at least "me / them" | Meeting notes are useless for stakeholder mapping without it; whisper alone does not diarise (`unverified`) | P4.3 design, new candidate in M6 |
| R7 | **Long files:** 30–90 min recordings, batch, resumable, with progress; measure time per audio hour on the Air and on the future host | Today's targets (D56) are for short voice queries | P2.3/P4.3 measurement, Q30 host sizing |
| R8 | **Capture path without iCloud.** Voice Memos syncs through iCloud by default (`unverified`); for client recordings either turn that sync off or use a recorder that keeps files local, then transfer by AirDrop or cable into the client vault's inbox | iCloud is an external processor that a client contract may not name (`unverified`: depends on each contract) | Capture design, P4.2 |
| R9 | **Transcript retention and minimisation:** transcripts kept only as evidence for confirmed notes, deleted at contract end with the vault | GDPR minimisation; contract return/deletion clause (`unverified`: no legal source cited; for the T0.7 lawyer review) | Client vault policy |
| R10 | **Agent isolation:** separate Claude project, separate Cowork folder connection; never both vaults in one session; Codex profile scoped to one vault | Cross-contamination through agents, not just through files | AGENTS.md (client vault), session setup |

## Open points (for David, not assumed)
- **Recording consent.** Recording client meetings needs the participants' knowledge (GDPR transparency; `unverified`, no legal source cited, for the T0.7 lawyer review) and some clients may forbid it. Default proposed: ask at the start of each meeting; otherwise dictate a summary right after (the same pipeline handles a dictated memo).
- **Plan impact.** R3–R7 pull P4.3 (S4, W8) forward to before November in a minimal form: a file-in, transcript-out tool. To be weighed against T9/P2.5 when the S2–S6 plan is re-baselined for reduced hours from November.
- **Method vs data.** Templates, qualification framework, offer catalogue and workflows are Tower13 method: a name-free master copy may live in Dbrain2 (`internal`); data never does.

## Related
- [[30 Resources/AI Vendors/eurouter|EUrouter]]: candidate to evaluate for the client-tier processing (T0.7).
