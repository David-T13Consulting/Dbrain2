---
classification: internal
review_status: codex-reviewed
---
# Progress Tracker — AI Second Brain Project

**Last updated:** 22 Oct 2026 · **Updated by:** Claude Code (session 58: G1-inj baseline done, planted text steers answers in 2 of 4 classes → M-inj brief; PL1 step 7, P1.4 step 1 and AS1 step 4 parked again)

---

## Current state

| | |
|---|---|
| **Phase** | **Three stages since 21 Oct (D141)**, inside the 19 Oct pivot (D134–D140): stage 1 second brain on the Mac (20 Oct–1 Nov, hard stop), stage 2 with Claude Code (2–8 Nov), stage 3 hosted EU with the router (9 Nov–6 Dec). Kept from before: P2.2 query service, P2.8 phone screen, P2.5 F0–F3, P2.7 failure capture, AS1 commit gates |
| **Schedule** | [[10 Projects/AI Second Brain/04_Roadmap\|04_Roadmap]] §4: stages 1–3, then operate and demo 7–13 Dec; demo-ready Fri 18 Dec 2026 (Q29) |
| **Target** | Client-ready demo, December 2026 |
| **Status** | 🟢 Week 0 closed · Week 1 closed · Week 2: 3 skills drafted and smoke-tested · Week 3: golden dataset **70/150** runs labelled. Batch 04 held out and scored 2 Oct — terrain 100% (≥95% ✅), intent 65% (≥85% ❌); the flags have no D19 threshold, and against the always-"no" baseline of 85% `tempo_block` at 40% is far worse while vertical at 90% barely beats it. The evidence behind the v2 taxonomy (D67) |
| **Dependencies** | No hardware (D134). Stage 1: PL1 step 7 (parked; frontmatter seam fix unreviewed) and step 8 (G2 by voice with David; its remember half can run now). Personal captures from the phone wait for P1.4 applied + lint (Q153, Q156). Stage 3: Scaleway key (Q134) and Claude API key |
| **Next action** | **"Pick up the loop":** D74 consults, then fresh reviews, for the three parked steps: [[90 System/briefs/PL1-mac-second-brain\|PL1]] step 7 (one shared frontmatter parser?; code in runtime `stash@{0}`), [[90 System/briefs/P1.4-four-axis-retrofit\|P1.4]] step 1 (a positive admission rule; untracked `experiments/p14_retrofit.py`), [[90 System/briefs/AS1-agent-setup-hardening\|AS1]] step 4 (checks reachable only through `run_confined`; untracked `ops/`). [[90 System/briefs/M-inj-answer-injection-mitigation\|M-inj]] once David approves it. G1-inj S2 (22 Oct): I and A fail, X and D clean |
| **Action for David** | Try "Brain Remember" with one benign work note (press "Add Shortcut" on the Mac first if not done); G2's remember half (PL1 step 8); approve the M-inj brief (and whether its measurement may rerun on the live server); whether the unused `ops/sandbox-canary` may be deleted; replace `~/Work/CLAUDE.md`'s start text with the AS1 proposal (now `python3 -I -B -S`) when step 4 lands; Scaleway key before 9 Nov (Q134); backups outside git untested |

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

### Session 57 — 22 Oct 2026 · Claude Code, lead loop (remember from the phone live; step 7, P1.4, AS1 step 4 parked; G1-inj report waits for Codex)
**Authorization:** "pick up the loop" from David, 22 Oct; no ⛔ block; two Cowork entries (weekly review; Q153–Q155 answers). David present: answered **Q156–Q162** in session. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only) until its usage limit (13:20, back ~15:46). No subagents. `caffeinate -ims` on AC power.
- **Handoff:** weekly review committed (`f0cea35`); answers recorded and carried into PL1, AS1, P3.0 (`307f15a`).
- **PL1 step 6 "remember from the phone": done and live.** One writer (`writer.create_inbox_note`: one new Inbox file, never a replacement), EN/FR fail-closed guards behind David's read-back and Save (Q154), work captures only until P1.4 (Q156). Review 1/2 FAIL (temp-name collision could delete a file; a failure after placing said "not saved"), fixed; review 2/2 PASS; **David approved (Q157)**; runtime `0bdd8e7`; phone service restarted; "Brain Remember" built and opened for "Add Shortcut".
- **PL1 step 7 "correct from the phone": parked.** David chose the model proposes the edit (Q158); D129 design check; David accepted the edit race with a backup (Q159). Reviews 1/2 and 2/2 FAIL: five of six blockers on Markdown forms the plain-text gate missed. Parked in runtime `stash@{0}` so the phone keeps reviewed code. Next: D74 consult for a narrower contract.
- **P1.4 four-axis retrofit: brief and dry run.** Brief `291b3af` (additive only; Tier 2 for step 1 after the batch review). Dry run on the real vault: 183 notes, vault unchanged, 5 flags. Review 1/1 FAIL (frontmatter forms, vocabulary flags, output confinement, `client` stop); fixes uncommitted; parked.
- **AS1 step 4 (startup check): parked again.** D74 consult: pre-checks can't see git's own reads; David chose OS enforcement (Q160): macOS `sandbox-exec`. Reviews 1/2 and 2/2 FAIL on proving which sandbox is in force (a canary file is not enough). Found and tested for next run: in-process `sandbox_init()` confines the process and its children with no "inside" entry point.
- **Tier 1a batch 2026-10-22:** review 1/2 FAIL (G1 scorer: full-width question mark, "Mar" read as French Tuesday; Granite Speech "English only" contradicted, recorded `unverified`; shortlist kept as a labelled proposal, Q161; P1.4 step 1 to Tier 2), fixed in `f84ff78`, `7187932`, `0c0932b`; review 2/2 PASS.
- **G1-inj:** S2 to run on the phone's model (Q162); report writer built, review 1/2 FAIL (not exclusive, link-hiding `realpath`, `:018087` bypass), fixed; review 2/2 not run (Codex usage limit). Uncommitted.

**Pick up at:** G1-inj report writer review 2/2 → David's approval → S2 on port 18087 (Q162); then the three D74 consults (PL1 step 7 narrower contract; P1.4 step 1; AS1 step 4 with `sandbox_init`). David: try "Brain Remember"; G2 remember half.

### Session 56 — 21 Oct 2026 (night) · Claude Code, lead loop, autonomous (T4.2 passed; PL1 6–7 blocked on David; AS1 step 4 parked; G1-inj S1)
**Authorization:** "pick up the loop" from David, 21 Oct ~20:50; Cowork's handoff: overnight run, David asleep, queue every decision in for-david (D68). No ⛔ block. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only) until its usage limit (~21:30, back 23:39). No subagents. `caffeinate -ims` on AC power (D103).
- **Handoff:** pivot history note committed (`952b95b`, index line); Q-cowork-21d recorded (`9c79493`).
- **PL1 step 5 (T4.2): done.** Fixes for review 3's five blockers (untracked state left out, Q-cowork-21d); D74 consult (Codex): recovery checks converging, report boundary didn't enclose startup: now runs only as `python3 -I -B`, every outcome (bad argument, import error, Ctrl-C, report-write failure) ends in a report. Review 1/1 PASS; runtime `6f1e0dc`. **Real drills ok** on both repositories (runtime `6f1e0dc`, vault `9917f86`): bad commit reverted to the identical tree; clone deleted and restored from GitHub, fsck clean. Untracked and ignored files, models, logs and the failure store not tested.
- **PL1 steps 6–7: file list reviewed (PASS, four should-fixes applied), then blocked on David.** D129 design check for step 6: word-list guards can't guarantee "nothing prohibited is ever saved" from free dictation; queued **Q154** (what the gate is) and **Q153** (personal captures before the wave-1 gate). Nothing built.
- **AS1 step 4 (startup check): parked.** Design check, then reviews 1/2 and 2/2 FAIL; Codex raised it to Tier 2 (it checks the D108 deny rule). Six blockers, all on what is read on the way (linked folders, git's own reads of `.git/config`, TOML parsing, partial reads). Fixes applied uncommitted; **Q155** proposes a narrower check.
- **G1-inj S1: built** (runtime `797ff41`, Tier 1a): 12 made-up cases, attack and control arms, closed-grammar scorer, runner through the phone path. Persistent report (Tier 2) not built.
- **Tier 1a batch 2026-10-21d:** review 1/2 FAIL, two blockers fixed forward: the G1 scorer passed reversed or unbound times (`53bda83`); the pivot note presented an unmeasured rented-vs-local comparison as a T9 result (`2cd7881`). Review 2/2 (after Codex's reset, 23:45): FAIL, two more G1 scorer blockers (words between "until" and the time; no subject or assertion required); budget used, so **fixed forward unreviewed** in runtime `72035e1`: **next batch must review it.**
- **TASKS:** secret-scanner scope closed (covered by AS1 step 3's commit gates, Q126).

**Pick up at:** Q153/Q154 answered → PL1 step 6; else AS1 step 4 (D74 consult, Q155) and G1-inj (the next Tier 1a batch reviews runtime `72035e1` first, then S1's Tier 2 report write).

### Session 55 — 21 Oct 2026 · Claude Code, lead loop (voice on the phone; Mac model Gemma 4 26B-A4B; T4.2 parked again)
**Authorization:** "pick up the loop or flag blockers" from David, 21 Oct; then "do what you can until Codex comes back up". David present; answered Q144, Q147–Q152 in session. Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol`; two Opus subagents for D74 consults while **Codex was at its usage limit (about 16:00–18:38)**.
- **PL1 step 4 done:** `spoken` field (runtime `3f7145c`, review PASS) with the evidence state in words (Q149); voice Shortcut built and tested on David's phone: dictate, hear, one screen with OK/Wrong; the token lives in a "Brain Key" Shortcut David filled once (generator `a02bfb6`, review PASS). **P2.8 phone check passed** (climbing, 2 Nov). Tailscale had stopped on the Air; restarted.
- **T9c done:** Gemma 4 12B and 26B-A4B (Apache-2.0) against C2 on the frozen corpus; **26B-A4B safe and 7/8** (C2 5/8, 12B 5/8), p50 8.5 s, ~15 GiB; both judges 58/60. **David switched the Mac default to the 26B-A4B (Q152)** (runtime `4c38652`, review PASS); four failed models deleted, budget 30 GB (Q144); a trace-label bug after the switch fixed (`e1844d0`, review PASS).
- **PL1 step 5 (T4.2) parked a third time:** narrowed to the two repos (Q148), Keychain read-only for their GitHub clones (Q150), 31 synthetic tests; review FAIL with six blockers, two of which argue against the declared scope (untracked files). Next: accepted risk under Q53, then fixes.
- **Observation:** a dictated question was misheard once and lexical retrieval found nothing; retry worked (M5).

**Pick up at:** PL1 step 5 with David's accepted-risk decision, then steps 6–8.

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
