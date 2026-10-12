---
classification: internal
source: roadmap §0 (D45–D48); D52–D59; D55 (20+ h/week); TASKS and PROGRESS as of 5 Oct 2026; P2.2 brief and results note
review_status: proposed
note_type: decision
created: 2026-10-05
updated: 2026-10-09
---
# Delivery plan S2–S6, dated (draft, 5 Oct 2026)

**Status: proposed by the lead, not approved as a whole.** It turns roadmap §0's stage order into dated weeks. The order, the stages and their exit evidence are roadmap §0's; this note adds dates, owners, decision deadlines and a cut order. **David has answered:** demo-ready **Fri 18 Dec** (Q29), the cut order as listed (Q31), T8 → `@cowork` (Q28). **Still open:** the host purchase (Q30; David is evaluating a 64 GB host).

**Amended 5 Oct (MVP-phone, Q32–Q34):** a **remote-text slice moves from S4 into S2**: ask from the iPhone over Tailscale, typed or dictated, with a cited answer from the Air (task P2.4, brief [[90 System/briefs/MVP-phone|MVP-phone]]). S4 keeps the mobile UI, durable capture and offline queue, voice beyond dictation, and the away-from-home tests on every device class.

**Amended 9 Oct (independent audit, David's end goal; roadmap §0 "Amendment of 9 October"):** no week is removed and no cut is triggered. Added: **W · data policy v1.0 (usable security)** drafted by `@cowork` in W2–W3, David approves; **G1 read-path injection suite** joins the S2 exit (lead to confirm it fits, ⚑); **S3 exit re-anchored** on remember → recall → correct from the phone (W6); **stage C, context connectors**: C1 personal calendar W7, C2 personal mail W8, C3 work calendar and mail W9–W10 into the client-tier instance only after G3; documents after the demo. Proposed **cut 0**: C3 moves after the demo if G3 has not passed by Fri 13 Nov. Pace is David's call ("move a little faster than planned"); the plan is already about a week behind on S1/S2 evidence.

## The arithmetic first
- **Window:** Mon 5 Oct to **Fri 18 Dec**, the demo-ready date David confirmed (Q29): **11 weeks**.
- **Capacity:** 20+ h/week (D55), so about **220 hours**, plus agent time that still needs David's review.
- **Slack: none.** Every stage below gets its weeks with no buffer, and S4 (voice) and S6 (drills) are the likeliest to run over. Hence the **cut order** at the end, approved by David in advance (Q31) rather than improvised in December. The MVP-phone slice adds about a week of work to S2 without moving S2's exit; it pays for itself by taking the access-and-auth half of P4.1 out of S4.
- **Evidence so far:** P2.2 went from brief to a measured service in four days (2–5 Oct), but its code has been through nine review rounds and is still uncommitted (parked after round I, 5 Oct). Expect review, not build, to set the pace.

## Weeks

| Week | Dates | Stage | Work (owner) | Exit or checkpoint (Friday) |
|---|---|---|---|---|
| W1 | 5–9 Oct | **S1 close + S2 slice** | **P2.4 MVP-phone** (`@code`): built 5 Oct and used by David from the iPhone on Wi-Fi and 4G; **code uncommitted** (it sits on P2.2) and acceptance incomplete (five questions per network, off-tailnet test, re-run after the display fixes); the Air-asleep check moved to the always-on host (Q36) · **P2.2: parked after its fifth failed review (round I), three findings open**: fix and re-review in the next run, then the first `dbrain-runtime` commit (`@code`) · T9/M6 brief committed 5 Oct; runs after P2.2 is committed (`@code`) · T8 data-flow diagram and scoped-roots list, including the Tailscale hop (`@cowork`, Q28) · **P1.4: brief and dry-run diff report only; applying the retrofit waits for David's approval (rule 8, hard limit)** (`@code`) | **S1 exit (roadmap §0):** one authoritative plan, bounded initial corpus, data-flow and permission design, measurable acceptance criteria. The authoritative plan is roadmap §0; this note only dates it and is itself proposed |
| W2 | 12–16 Oct | **S2** | T9/M6 comparison run (`@code`) · P2.1 independent case review (`@codex`) · T12 permission/redaction checks, T5 trace store (`@code`) · **D53 host ordered by 16 Oct** (`@david`, Q30) | Model recommendation in the queue for David |
| W3 | 19–23 Oct | **S2** | P2.3 measurement with the chosen model, sustained protocol (`@code`) · M5 corpus widening with its own cases (`@code`) · **six-week honesty check, 19 Oct** (`@david`) | **S2 exit, Fri 23 Oct (roadmap §0):** reproducible local question-answering run, source citations and abstention cases, measured resource use; evidence for retaining the Air or considering a dedicated host. Plus, from P2.4: reachable from the iPhone over the tailnet. If the host has not arrived, the numbers are Air numbers and the host confirmation moves into W4 |
| W4 | 26–30 Oct | **S3** | T4.2 rollback and independent restore on a disposable copy (`@code`) · host set-up and S2 re-measure on it, if delivered (`@code`) | Restore drill passes on a copy |
| W5 | 2–6 Nov | **S3** | P3.1 source IDs and evidence records · P3.2 pending patches with approval bound to patch and base revision (`@code`) | Stale approval rejected in a test |
| W6 | 9–13 Nov | **S3** | P3.3 one deterministic writer · T4.3 enable it for approved patches · T7 evidence UX (`@code`) | **S3 exit, Fri 13 Nov (roadmap §0):** one source safely updates connected notes; rejection produces no knowledge changes; stale approval is rejected; rollback and independent restore demonstrated |
| W7 | 16–20 Nov | **S4** | P4.1 remainder: mobile text UI beyond the Shortcut, the service moved to the always-on host, the iMessage brief if its leak test passes (Q33) (`@code`). Private authenticated access was **built early as P2.4 (uncommitted until P2.2 lands, acceptance incomplete)** | Text answer from the phone through the host, not the Air |
| W8 | 23–27 Nov | **S4** | P4.2 durable capture queue · P4.3 push-to-talk ASR and spoken answers, French/English tests (`@code`) | Capture survives host sleep; voice first-word time measured against D56's 5 s |
| W9 | 30 Nov–4 Dec | **S4** | P4.4 away-from-home tests on iPhone, iPad, Air (`@code` prepares, David runs) | **S4 exit, Fri 4 Dec (roadmap §0):** text and voice work away from home on agreed devices; captures survive host and network loss; retry does not duplicate; pending and error states are visible |
| W10 | 7–11 Dec | **S5** | T11 coordinator, curator and evidence checker with scoped tools · P5.1 compare against the single-agent baseline · P5.2 persistent jobs with bounded retries, time and tool use (`@code`). **If cut 1 has been triggered** (slippage rule below), S5 shrinks to the evidence checker only and its exit is restated accordingly | **S5 exit, Fri 11 Dec (roadmap §0):** checker benefit and latency cost measured; unauthorised tool actions denied; interrupted work resumes without double writes; David can inspect an execution trace |
| W11 | 14–18 Dec | **S6** | P6.1 backup/restore drill · P6.2 pins and runbooks · P6.3 monitoring · T13 two rehearsals with a controlled failure · P6.4 public-safe package (`@code`, rehearsals with David) | **S6 exit, demo-ready Fri 18 Dec (roadmap §0):** rebuild and restore drills pass; upgrade regression results recorded; two repeatable demos include a controlled failure and recovery |

**Running track, in parallel and not on the critical path:** T3.4 rubric v2.0 wording (`@cowork`, David approves) → P3.4 regression fixes against v2 semantics (`@code`) → T3.1 batches 05–06 and weekly assessments (`@cowork`, David labels) → P3.6 freeze the running acceptance cases (`@code`). Personal data wave 1 waits for P1.4 (D69).

## Decision deadlines

| By | Decision | Why then |
|---|---|---|
| Fri 16 Oct | **D53 host purchase** (Q30) | S3 onwards assumes an always-on host; a week's delivery and set-up lands it in W4. Later than this, S2 acceptance and S3 run on the Air and the host confirmation slips into S4 |
| Fri 16 Oct | Model choice from T9/M6 | P2.3 measures the chosen model in W3 |
| Mon 19 Oct | Six-week honesty check (rule 5) | Six weeks after 7 Sep |
| 13 Nov | Voice stack (ASR and TTS candidates) | P4.3 starts W8; the speech candidates need their own brief and fixtures first (M6 says so) |

## Slippage rule and cut order (Q31)
A stage exit that misses its Friday by **more than three working days** triggers the next cut below, recorded in PROGRESS, and an entry in the queue. Order approved by David (Q31), cheapest loss first; the three-working-day trigger is the lead's proposal:
1. **S5 to the evidence checker only:** no coordinator or curator before the demo. The single-agent baseline comparison stays.
2. **Spoken answers (TTS) become stretch:** voice *capture* (ASR) stays, since D58 and capture depend on it.
3. **P4.4 on two device classes** (iPhone and Air), iPad after the demo.
4. **P6.4 public package after the demo:** the private demo still runs.
Never cut: the restore drill, the stale-approval and permission tests, the no-cloud-fallback guarantee, or the controlled failure in T13. They are the governance story.

## What this plan does not change
Roadmap §0 stays the authority on stages and exit evidence; TASKS stays the checklist; nothing else here is a commitment until David approves it; the demo-ready date (Q29) and the cut order (Q31) are already his decisions, and approving it does not approve any of the decisions in the table above.
