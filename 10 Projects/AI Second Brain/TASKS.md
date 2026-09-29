# Tasks — AI Second Brain Project

**Updated:** 29 Sep 2026 · **Phase:** Week 0 — Foundations · **Target:** client-ready December 2026

---

## ▶ Next action

> **Review weekly-assessment v0.1** (open point: mean vs median baseline), then T2.4 — `SKILL.md` #3: race-readiness. T0.7 before the next contract is signed.

After that: T0.6 (check firm's AI policy — needs you, not me). T0.2 and T0.3 closed 29 Sep.
Then T1.2 (`AGENTS.md`, by hand) and T1.4 (bounded knowledge migration) are unblocked — both were waiting on T0.4.

---

## Week 0 — Foundations

*Everything here blocks H1. Target: complete by 14 Sep.*

- [x] **T0.1 · Revoke the Telegram bot token** ✅ done 8 Sep `5 min` `🔴 security`
  Token `8842032811:AAFH…` is in `00_Source_Material/Product_School/Product School - Advanced Agents.pdf` (p.2). Revoke via BotFather → `/mybots` → select → API Token → Revoke.
- [x] **T0.2 · Rotate the four Zoom recording passcodes** `10 min` `🔴 security` ✅ **closed 29 Sep — mitigated, not rotated.** Recordings are Product School's, not David's to rotate. Exposure contained: the PDF stays outside the vault, ungit-tracked (rule 7).
  Same PDF. Lower severity than the token but they're recordings of paid course content.
- [x] **T0.3 · Run the 30-day audit prompt** `20 min` ✅ **closed 29 Sep — superseded.** Its only purpose was evidence for T0.4, which was locked 8 Sep from David's actual recent topics.
  In ChatGPT/Claude: *"Look at my last 30 days of conversations. Where am I spending most of my time, and what from that list should be automated?"* Evidence-led input to T0.4. (Source: Advanced Agents, Day 2.)
- [x] **T0.4 · Choose the showcase workflow** `45 min` `⭐ blocks everything` ✅ **LOCKED 8 Sep** (D14, D15 in PROGRESS.md)
  **"Classify each run's session type (easy / long / tempo / hills / intervals / race / recovery) from raw
  Strava data, then roll a week of classified sessions into a coaching assessment — trend, effort
  adequacy, and race-goal trajectory."**
  Evidence-led (David's actual last-few-weeks topics, not guessed from his job). No Runna connector
  exists and Strava's `get_training_plan` tool doesn't return real plan data — session-type
  classification from raw metrics (pace/HR/elevation/effort) is the workaround, and it's a cleaner
  golden-dataset task than plan-compliance checking would have been anyway.
  **H1 scope** (checkable core): session-type classification + trend/effort-adequacy.
  **H2 scope** (judgment layer, confidence bands): race-goal trajectory call.
  **Golden-dataset note:** no external plan to check against, so ground truth for T3.1 comes from
  David labeling a batch of his own historical runs by actual session type — flag this as real work
  he'll need to do, not just Claude's.
- [x] **T0.5 · Write `data-policy.md`** `45 min` ✅ **done 29 Sep** — v0.1 in `02_Architecture/data-policy.md`. §6 (Tower13 commercial) provisional pending T0.6.
  Three tiers (public / internal / client-confidential), red lines, what may never enter the system. Save to `02_Architecture/`.
- [x] **T0.6 · Check your firm's AI policy** `30 min` ✅ **closed 29 Sep — replaced by a rule (D16).** There's no firm policy above Tower13. David set the rule instead: every contract must state his AI agent use explicitly, and engagements without that stay out of the system entirely. data-policy.md → v0.2.
- [ ] **T0.7 · Add an AI-use disclosure clause to the Tower13 contract template, and to live contracts at renewal** `1 h` `needs David + lawyer review`
  David has no live contracts (29 Sep), so this only applies going forward: the clause goes in the template before the next engagement is signed. Claude can draft; a Belgian lawyer should check it.

**Week 0 gate:** you can state the showcase workflow and your red lines in one sentence each. Showcase workflow ✅ done (T0.4). Red lines ✅ done (T0.5, 29 Sep).

---

## H1 · Weeks 1–4 — Ship

*Goal: a working, instrumented vertical slice. Narrow and deep.*

### Week 1 — Vault
- [x] **T1.1** Create vault skeleton: `00 Inbox / 10 Projects / 20 Areas / 30 Resources / 40 Archive / 90 System` `30 min` ✅ done 8 Sep — built inside `~/Documents/Dbrain2` (the Obsidian vault), not this folder. See D11 in PROGRESS.md.
- [x] **T1.2** Write `AGENTS.md` for the vault — **by hand**, 20–30 lines `1 h` ✅ **29 Sep, v1 approved by David.** At the vault root, with a root `CLAUDE.md` importing it (D17). Every line passes the test: would the agent get this wrong without being told?
  Auto-generated ones measurably underperform (+23% cost, redundant content).
- [x] **T1.3** `git init` the vault, first commit `15 min` ✅ done 8 Sep — commit 377e8c2 in Dbrain2
- [x] **T1.4** Migrate a *bounded* subset of knowledge — only what the showcase workflow needs `2 h`
  ✅ **done 29 Sep:** `20 Areas/Running/athlete-baseline.md`, `30 Resources/Running/session-types.md`, `20 Areas/Running/race-goals.md`, all confirmed. Open: Gelbressoise distance. See D18.
  ⚠️ Resist importing everything. That's the collector's fallacy and it costs weeks.
- [x] **T1.5** Confirm agent is **read-only** at this stage. No MCP servers. `10 min` ✅ confirmed 8 Sep — documented in Dbrain2/90 System/README.md, no write MCP configured

### Week 2 — Skills
- [x] **T2.1** Write success thresholds for 3 skills — **before** writing the skills `45 min` ✅ **approved 29 Sep** → `02_Architecture/success-thresholds.md` (D19)
  Format: *"handles ≥X% of cases with <Y% exceptions."* Defining "good" is your job, not an engineer's.
- [x] **T2.2** Write `SKILL.md` #1 `1.5 h` ✅ **29 Sep, v0.2 approved** → `90 System/skills/classify-session/SKILL.md` (D20, D21)
- [x] **T2.3** Write `SKILL.md` #2 `1.5 h` ✅ **29 Sep, v0.1 drafted and smoke-tested, pending David's review** → `90 System/skills/weekly-assessment/` (SKILL.md + compute_week.py) + `30 Resources/Running/weekly-flags.md` (D22)
- [ ] **T2.4** Write `SKILL.md` #3 `1.5 h`

### Week 3 — Golden dataset ⭐
- [ ] **T3.1** Draft golden dataset v1 — 150 rows `4 h` `⭐ the showcase artifact`
  Columns: Input · Expected output · Edge case? · Judge type (rule/LLM). 20–30% edge cases.
- [ ] **T3.2** Add adversarial rows (≥3) and note coverage gaps `1 h`
- [ ] **T3.3** Commit as `golden-dataset.md`, versioned like code `15 min`

### Week 4 — Evals + write access
- [ ] **T4.1** Wire LLM-as-judge scoring against the golden set `3 h`
- [ ] **T4.2** Test backup/rollback — deliberately break something and restore it `1 h`
- [ ] **T4.3** Only after T4.2 passes: enable agent **write** access, confined to approved dirs `30 min`

**H1 gate — all four must be true:**
1. Three skills pass their stated thresholds
2. You have deliberately broken something and rolled it back
3. You can screen-share eval results
4. Zero client-confidential data has entered the system

---

## H2 · Weeks 5–9 — Validate

- [ ] **T5** Eval dashboard — metrics, judge setup, drift alerts, UX hooks `1 wk`
  Test: *can you screen-share it in a sales call?* If not, it isn't done.
- [ ] **T6** Reliability contract — metric/target/measurement/alert-threshold + escalation paths `1 wk`
- [ ] **T7** Confidence UX — 3 bands, visible reasoning, override surface, corrections feed back `1 wk`
  Build the low-confidence path deliberately — you will demo it on purpose.
- [ ] **T8** Governance one-pager — scope, autonomy boundaries, escalation triggers, audit cadence, regulatory exposure, agent topology `1 wk`
- [ ] **T9** Model + hosting decision, benchmarked against your own golden dataset `1 wk`
  2–3 options: one frontier, one open-weight, one EU-hosted. Document with the trade-off grid.

**H2 gate:** "How do you know it works?" answered with a screen. HITL% trending down. Governance one-pager survives a hostile read.

---

## H3 · Weeks 10–13 — Collaborate & package

- [ ] **T10** Multi-user layer — shared vs personal roots, RBAC as metadata filter, S.M.A.R.T. memory `1 wk`
  Get a second real human in. Two people working beats ten people designed.
- [ ] **T11** Second agent + supervisor/critic pattern, A2A logging, autonomy ceilings `1 wk`
  Only after naming the boundary you hit (skills / tools / evals).
- [ ] **T12** Security hardening + shadow-AI audit on yourself `1 wk`
- [ ] **T13** Demo build + rehearsal — twice through, no unexplained failures `1 wk`

---

## Backlog / someday

- [ ] Migrate Apple Notes → markdown (export route; no API exists)
- [ ] Retrieve the 4 Product School capstone tools from the LMS (Strategy Assembler, AI Bet Evaluator, Roadmap Builder, Pitch Builder)
- [ ] Decide relationship between this project and the Vibe Coding app+deck deliverable → OQ-5
- [ ] Self-hosted server evaluation — month 4+, only if an async workflow justifies it

---

## Conventions

`🔴` security-sensitive · `⭐` high-leverage · `T0.x` week-0 · time estimates are working time, not elapsed.
Tick items as you go. Add anything that surfaces — an unrecorded task is a lost task.
