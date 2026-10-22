---
classification: internal
review_status: codex-reviewed
---
# Progress Tracker — AI Second Brain Project

**Last updated:** 21 Oct 2026 · **Updated by:** Claude Code (session 55: voice on the phone; Mac model now Gemma 4 26B-A4B; T4.2 parked)

---

## Current state

| | |
|---|---|
| **Phase** | **Three stages since 21 Oct (D141)**, inside the 19 Oct pivot (D134–D140): stage 1 second brain on the Mac (20 Oct–1 Nov, hard stop), stage 2 with Claude Code (2–8 Nov), stage 3 hosted EU with the router (9 Nov–6 Dec). Kept from before: P2.2 query service, P2.8 phone screen, P2.5 F0–F3, P2.7 failure capture, AS1 commit gates |
| **Schedule** | [[10 Projects/AI Second Brain/04_Roadmap\|04_Roadmap]] §4: stages 1–3, then operate and demo 7–13 Dec; demo-ready Fri 18 Dec 2026 (Q29) |
| **Target** | Client-ready demo, December 2026 |
| **Status** | 🟢 Week 0 closed · Week 1 closed · Week 2: 3 skills drafted and smoke-tested · Week 3: golden dataset **70/150** runs labelled. Batch 04 held out and scored 2 Oct — terrain 100% (≥95% ✅), intent 65% (≥85% ❌); the flags have no D19 threshold, and against the always-"no" baseline of 85% `tempo_block` at 40% is far worse while vertical at 90% barely beats it. The evidence behind the v2 taxonomy (D67) |
| **Dependencies** | No hardware (D134). Stage 1: David for the T4.2 scope (untracked files) and the PL1 step 8 G2 check; T9c is done (Q152). Stage 3: Scaleway key (Q134) and Claude API key |
| **Next action** | **"Pick up the loop" → [[90 System/briefs/PL1-mac-second-brain\|PL1]] step 5 (T4.2):** ask David to record untracked files as an accepted risk (Q53), fix the other blockers of review 3, D74 consult, review; then steps 6–7 (file list reviewed first), then step 8 (G2 by voice with David). Untracked on purpose in the runtime: `experiments/restore_test.py`, `tests/test_restore_test.py`; the README line as a patch in `~/Library/Application Support/dbrain/parked/` |
| **Action for David** | say if the Air feels slow with the 26B-A4B (Q152); PL1 step 8 (G2) when steps 5–7 are done; Scaleway key before 9 Nov (Q134); backups outside git untested (Time Machine has no destination). Nothing open in [[90 System/for-david\|for-david]] |

### Original work-package progress — retained snapshot

Current platform gates S1–S6 are not yet passed. P1.0/P1.1 are complete; supplied-evidence comparisons and a bounded retrieval experiment have run, but retrieval/service acceptance remains open. The historical snapshot below is not a percentage-complete estimate for the new scope.

```
Week 0  Foundations    █████████░  90%   (T0.7 contract clause: future-only)
H1      Ship           ██████░░░░  60%   ← you are here (Weeks 1–2 done, Week 3 started)
H2      Validate       ░░░░░░░░░░   0%
H3      Collaborate    ░░░░░░░░░░   0%
```

### Original domain/demo gate status — current platform gates in roadmap §0

| Gate | Criteria met | Status |
|---|---|---|
| Week 0 | Workflow named · red lines stated | ✅ Met 29 Sep |
| H1 | 3 skills pass · rollback tested · evals screen-shareable · no client data | ⬜ Not met |
| H2 | Eval dashboard live · avoidable exceptions measured separately from approvals · governance review (D48) | ⬜ Not met |
| H3 | Demo runs twice, no unexplained failures | ⬜ Not met |

---

## Metrics

Not yet instrumented as a service. Start platform measurement at S2; retain running scores in their batch records. Original aspirations below are qualified by D48 and roadmap §0; no population-level reliability claim yet:

| Metric | Target | Current |
|---|---|---|
| Hallucination rate | <1% | — |
| Eval regression | 100% of changes stay positive | — |
| Avoidable exceptions | Mandatory approvals tracked separately; preserve the approval gate | — |
| Recall accuracy | ≥85% | — |

*Deliberately not tracked at this volume: drift velocity/week, confidence distribution, inference ROI, deflection rate. Know the numbers; explain why they're not instrumented yet.*

---

## Decisions and older sessions

Moved verbatim on 8 Oct 2026 (session 38, David's maintenance layout): [[10 Projects/AI Second Brain/DECISIONS|DECISIONS]] holds D1 onwards. Sessions 1–39 are in [[10 Projects/AI Second Brain/PROGRESS-archive|PROGRESS-archive]]; this file keeps the last three sessions.
Decisions that notes cite as "in PROGRESS" are in DECISIONS.


---

## Session log

Newest first. One entry per working session — what happened, what changed, where to pick up.

### Session 55 — 21 Oct 2026 · Claude Code, lead loop (voice on the phone; Mac model Gemma 4 26B-A4B; T4.2 parked again)
**Authorization:** "pick up the loop or flag blockers" from David, 21 Oct; then "do what you can until Codex comes back up". David present; answered Q144, Q147–Q152 in session. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol`; two Opus subagents for D74 consults while **Codex was at its usage limit (about 16:00–18:38)**.
- **PL1 step 4 done:** `spoken` field (runtime `3f7145c`, review PASS) with the evidence state in words (Q149); voice Shortcut built and tested on David's phone: dictate, hear, one screen with OK/Wrong; the token lives in a "Brain Key" Shortcut David filled once (generator `a02bfb6`, review PASS). **P2.8 phone check passed** (climbing, 2 Nov). Tailscale had stopped on the Air; restarted.
- **T9c done:** Gemma 4 12B and 26B-A4B (Apache-2.0) against C2 on the frozen corpus; **26B-A4B safe and 7/8** (C2 5/8, 12B 5/8), p50 8.5 s, ~15 GiB; both judges 58/60. **David switched the Mac default to the 26B-A4B (Q152)** (runtime `4c38652`, review PASS); four failed models deleted, budget 30 GB (Q144); a trace-label bug after the switch fixed (`e1844d0`, review PASS).
- **PL1 step 5 (T4.2) parked a third time:** narrowed to the two repos (Q148), Keychain read-only for their GitHub clones (Q150), 31 synthetic tests; review FAIL with six blockers, two of which argue against the declared scope (untracked files). Next: accepted risk under Q53, then fixes.
- **Observation:** a dictated question was misheard once and lexical retrieval found nothing; retry worked (M5).

**Pick up at:** PL1 step 5 with David's accepted-risk decision, then steps 6–8.

### Session 54 — 21 Oct 2026 · Claude Code, lead loop (PV1 step 4 committed; PL1 steps 4 and 5 parked)
**Authorization:** "pick up the loop" from David, 21 Oct; no ⛔ block, no new handoff entries. David present (Q146). Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol`. No subagents. `caffeinate -ims` on AC power.
- **PL1 step 1 = PV1 step 4: done** (runtime `46b702b`). D74 consult → no caller-supplied URL at all: a port-only test mode with fixed host, scheme and path, the Keychain refused in test mode, the endpoint rebuilt from the registry per call. Review 1/2 PASS; suite 574 OK.
- **PL1 step 5 (T4.2): parked again.** D74 consult applied in full (regular files only without following links, report outside every git tree, snapshot before the drills, dirty or unpushed state fails, https on `github.com` only, sanitised git env, refusals for submodules, LFS, shallow, alternates, sparse). Review 1/1 FAIL with three narrower blockers (separate git dir for `--out`, repository-local fsmonitor, nested `.gitattributes`); fixed uncommitted; failure-path tests still to write.
- **PL1 step 4 (voice), service part: parked.** `spoken` field (same answer as the screen, up to three titles). Review 1/1 FAIL: 423/503 kept "No answer." as spoken; fixed. Saved as a patch outside git and the files restored (Q146), so the phone runs committed code only. Shortcut generator not written: the 6 Oct temp-file token pattern is ruled out (data policy §2.2); David to decide how the token reaches the Shortcut.
- **Observation:** step 5 has now failed two reviews (sessions 53 and 54), the second on narrower edge cases; the next consult asks whether it converges or needs a different cut (for example, a narrower contract).

**Pick up at:** PL1 step 4 (re-apply patch, consult, review, Shortcut with David), then step 5.

### Session 53 — 21 Oct 2026 · Claude Code, lead loop (D141/D142 handoffs; T9b done, C2 stays; M6b closed; two steps parked)
**Authorization:** "pick up the loop" from David, 21 Oct; no ⛔ block in the handoff. David present; answered Q138–Q143 in session. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only). No subagents. On AC power: `caffeinate -ims` for the loop (D103), T9b under `caffeinate -dimsu`.
- **Handoffs:** Cowork's ~13:45 entry (three stages, D141) `f4bcdda` + bookkeeping `fb1f6c5`; ~14:15 entry (agent topology option A) `7989553`, numbered **D142**; Q-cowork-21a–c kept their IDs.
- **Tier 1a batch 2026-10-19, review 2/2:** FAIL, one blocker (PL1 steps 6–7 had no file list); fixed forward `2daf21b` with the should-fixes; D135/D140's "rented models outclass local" wording left (DECISIONS is append-only; the roadmap marks it `unverified`).
- **PL1 step 1 (= PV1 step 4): PARKED.** Reviews 1/2 and 2/2 failed on the test-only URL override (`[::1%30]` decoded to `::10`; `@127.0.0.1`), both a parser differential; the root-cause fix (ask urllib and http.client which host they would use) is applied **uncommitted, unreviewed**.
- **PL1 step 2: done** (runtime `a9b8746`). Q138: the dev cases read the three files byte for byte as C2 read them (vault `8990bbe`, corpus `878a08ea6f57` reproduced); review 1/1 PASS; suite 564 OK.
- **PL1 step 3 = T9b step 4–6: done** (`5f4e009`). All seven blocks ok; TwIL fails the safety gate in both configurations (6/8 vs C2's 5/8); Codex blind judge stricter and right on two answers. **Q141:** C2 stays; T9c brief for larger models (blocked on David). Phone service stopped for the window and restarted.
- **PL1 step 5 (T4.2): PARKED.** Review 1/1 FAIL, five blockers (symlink overwrite path, `--out` guard, rewound remote, dirty files omitted, remote into the repo). Real drills ran ok but do not count. Steps 6–8 not started.
- **M6b S5: done, M6b closed** (`eaf3e4c`): no measured benefit, lexical stays; review 1/2 PASS; approved Q142; embedding models and venv deleted on Q143.
- **Settings:** `.claude/settings.json` committed on Q140 (`70ea3b3`).
- **Not done, for later:** the protected edits approved by Q-cowork-21a–c (data policy, PV1 ceiling rule, D56 note; TASKS stage 3); project `CLAUDE.md` still says W1–W8 and "L0 own rented GPU" (protected; needs David's word); runtime README's "never pushed" line is out of date.

**Pick up at:** D74 consults on PV1 step 4 and PL1 step 5, then PL1 step 4.

### Cowork — 21 Oct 2026 · agent topology (option A)
- David proposed an organiser agent with sub-agents per confidentiality level and many role agents. Cowork checked it against current research (Anthropic 2026, Google/MIT scaling study, CaMeL) and the existing router; David chose **option A: router + one runtime agent + skills**, with a quarantined reader for untrusted input and Codex as the separate reviewer. Decision number for the lead to assign.
- David defined the critical tier: health, financial and transatlantic-move discussions; no online model, but not the weakest local one; email and calendar stay on the current plan.
- Answered 14:15: 21c quality-first model pick for T9b step 4; 21a Strava/training data is not critical; 21b critical material stays out of the vault until wave 2. Record: [[10 Projects/AI Second Brain/02_Architecture/agent-topology-proposal-2026-10-21|agent-topology proposal]]. No runtime or stage 1 scope change.

### Cowork — 21 Oct 2026 · three stages, small wins (D141)
**David present.** He asked whether the Mac Air version could move first, then set the sequence: (1) a second brain on the Mac, with voice and vault updates from the phone over Tailscale; (2) a second brain with Claude Code working in the vault; (3) the hosted GDPR/EU second brain. Cowork's condition, accepted: three levels of one system, same vault, query service and evaluation set. **Recorded as D141**, with L0 redefined as the own machine (Mac Air). **Answers:** Q136 (a) frozen copy of the pre-pivot section 0; Q137 (a) Scaleway approved, after David asked why Mistral and not Gemma or Qwen (the question was about the host; Scaleway hosts all three; Gemma 4 26B-A4B added to the measurement); Q119 approved again so T9b step 4 runs in stage 1; stage 1 two weeks, hard stop 1 Nov.

**Done:** roadmap §2–§5 rewritten in three stages; TASKS regrouped by stage; new brief [[90 System/briefs/PL1-mac-second-brain|PL1]]; PV1 brief re-sequenced; session 52's should-fixes for Cowork applied: the demo (classification at L0 when the ceiling is L0, no looser override after withholding, L0 = Mac, Dutch removed; artifact republished), "CLOUD Act: None" for L1 marked `unverified`, rented-model superiority marked `unverified`, Dutch out of scope per D121, archive banners no longer say "verbatim" (git `e7b558e` is authoritative). **Not touched:** runtime, protected files.

**Pick up at:** "pick up the loop" → handoff, Tier 1a review 2/2, PL1.

### Cowork — 19 Oct 2026 · research, sovereignty router, pivot (D134–D140)
**David present** (afternoon and evening). **Research:** reusable building blocks on GitHub, Reddit-cited sources and vendor pages; result in the [[10 Projects/AI Second Brain/02_Architecture/sovereignty-router-proposal-2026-10-19|sovereignty router proposal]] and the demo `05_App_Prototype/sovereignty-router-demo.html` (simulated data; also a private Claude artifact).

**David's decisions:** no hardware, rent compute (Q121 → D134); pivot now with option A, EU APIs by default (Q127 → D135); Open WebUI + Open Relay (Q128 → D136); 1 review per step, 2 for security (Q129 → D137); automatic routing, stricter-only override, soft cap (Q130 → D138); client tier at L1 or stricter until G3 and the lawyer review (Q131 → D139); T9b parked for an offline level, M6b closes with its note (Q119 replaced → D140). D-numbers assigned by Cowork at David's request; the lead may renumber.

**Six-week honesty check (Q120, rule 5):** since 7 Sep the system has shipped phone question-and-answer only, nothing client-facing. Capture continues; the pivot is the response.

**Done:** roadmap rewritten (§4 weekly plan W1–W8); TASKS rebuilt around the weeks; delivery plan S2–S6 superseded; pre-pivot roadmap, delivery plan, TASKS and PROGRESS archived verbatim in `40 Archive/AI Second Brain/`; PV1 brief written. **Correction:** no data-policy change is needed (§1 and §5 already allow `internal` to a provider once its terms are verified); the earlier proposal text said D46 had to change, which was wrong. **Not touched:** data policy, AGENTS.md and project CLAUDE.md (protected; PV1 step 1 edits them with David's approval cited), runtime.

**Pick up at:** "pick up the loop" → PV1.

## How to resume

1. Read `CLAUDE.md` (who, what, rules)
2. Read this file (state, decisions, last session)
3. Read `TASKS.md` (▶ Next action at the top)
4. Check `OPEN_QUESTIONS.md` for anything now answerable

Then work. Before you stop, update all three.
