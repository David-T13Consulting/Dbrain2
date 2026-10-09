---
classification: internal
created: 2026-10-01
last_reviewed: 2026-10-08
next_review: 2026-10-15
automation_status: activated 2026-10-01 (D60); first run 2026-10-08 produced output; task ID and timezone still pending
---
# Weekly local-model review

Owner: David. Research and documentation can be delegated to an assistant; deployment remains evidence-gated. Requested 1 October 2026. Knowledge hub: [[30 Resources/Local AI/README]].

**Scheduling status: activated by David on 1 October 2026** in the desktop local-project scheduler (D60, OQ-18 resolved). Cadence Thursday 09:00 `Europe/Brussels`, first review 8 October 2026.

⚠️ **Partly evidenced.** The first scheduled run (8 Oct 2026) produced output (see the operating record below). The task ID, confirmed timezone and next-run time are still not recorded — David to paste them into the activation record below. Review the first two runs before relying on the cadence.

The [official scheduled-task documentation](https://learn.chatgpt.com/docs/automations?surface=app) explains that local-project tasks need the computer on and desktop app running; the IDE/CLI has no Scheduled management interface. Web tasks cannot directly update a local folder. Activate in the desktop app with the vault as the project, then verify timezone, next run, permissions and a test output. Local model benchmarking and this assistant's online research are different workloads; the maintenance assistant is not being represented as a local model.

## Weekly procedure

1. Read `AGENTS.md`, `index.md`, the Local AI hub, last ledger entry and source register. Use the handoff rules; never bundle another assistant's edits into this task.
2. Check every entry in the **Watchlist** section below first: **every model webAI publishes on Hugging Face** (`webAI-Official`), TwIL-LM3-Pro first. Then check the original publishers listed in [[30 Resources/Local AI/sources]], their model collections/release notes, and runtime releases. Look for new relevant models, revised benchmark recipes, corrected results, license changes, regressions and deprecations. Prefer downloadable artifacts suitable for the use case over announcements.
3. For each material change, retrieve the primary source, record date/revision and benchmark conditions, then amend the relevant capability page and append a dated ledger entry. Keep previous measurements; mark superseded interpretations. If nothing changes, append a brief “checked; no material change” record with coverage and gaps.
4. Distinguish reported benchmarks from independently reproduced results. Include inference budget, quantization, language and harness; missing details remain explicit. Never invent a result to fill a weekly row.
5. Produce a shortlist of at most two next local candidates with concrete reasons. Do not automatically download model weights, upgrade runtimes, change the active model or expand data access. Run local comparisons only in an authorized, bounded experiment; otherwise record “local benchmark not run this week” and why.
6. Check classifications, source links, wikilinks, stale dates and contradictions. Update the source register/index as needed, append `log.md`, and commit only this task's changes. Read changes back and summarize the implications for S2/S4/S5.

If the Mac was asleep or the job failed, show the missed date and error; perform one catch-up review when available, without fabricating intervening checks. Pause on inaccessible sources, conflicting license claims or corpus-policy violations; unaffected sources can still be reviewed. Exception (David, 9 Oct 2026): webAI's non-commercial licence is not a reason to pause, flag or drop a webAI model; record the licence as a plain fact and carry on. Review the first two successful scheduled runs before relying on the cadence.

## Watchlist (David, 2 Oct 2026)
Check every entry below from **primary sources** each week, in addition to step 2, and record changes in the ledger. Facts marked "as of 2 Oct" or "as of 8 Oct" were gathered by Cowork from public pages and are **not verified locally**.

### webAI: every model on Hugging Face (David, 9 Oct 2026), TwIL-LM3-Pro first
- **Scope: all repositories under [huggingface.co/webAI-Official](https://huggingface.co/webAI-Official)**, not only TwIL-LM3-Pro. Each week, list the organisation's models and compare against the last ledger entry: new repos, new revisions (commit hash and date), new formats (GGUF, MLX, LiteRT-LM), sizes, context limits, base models and model-card changes. Known as of 8 Oct: TwIL-LM3-Pro, TwIL-LM3-Pro-LiteRT-LM, TwIL-LM3, TwIL-LM2, TwIL-LM (see [[30 Resources/Local AI/sources]]). Community conversions of webAI models (e.g. mradermacher GGUF) are tracked too, with provenance noted.
- **Licence: record it as a fact (name, version, any change) and move on.** David's instruction, 9 Oct 2026: no licence warning, no flag to `for-david.md`, no exclusion from the shortlist on licence grounds. This governs the weekly monitoring and its shortlist only: it does not change D99 (the open licence question for the demo) or TwIL-LM3-Pro's watchlist-only status in the frozen T9/M6 protocol.
- **TwIL-LM3-Pro** (priority). As of 2 Oct: 3.66B parameters, derived from IBM Granite 4.2-3B through webAI's fine-tuning for **formal-logic reasoning**; text only; "not a general assistant". Official repo ships GGUF (found 8 Oct, [[30 Resources/Local AI/benchmark-ledger]], "TwIL-LM3-Pro formats") and LiteRT-LM bundles (INT4 2.19 GB, INT8 3.76 GB, context capped at 4,096 tokens; the source model supports 131k). Benchmarks are **vendor-only**: the model card says source-model scores must not be attributed to the quantized bundles until rerun.
  - **Why it might matter here:** formal-logic strength could suit rule application (the session rubric, evidence checking in S5). Test that only in an authorized bounded experiment, against the same cases as the current candidates, within the M6 budget (hash-pinned, named in a brief).
  - **Check weekly:** independent evaluations · new formats (GGUF/MLX from webAI itself) · longer-context bundles · revised model card · new TwIL versions.
- **webAI platform** (Navigator, Companion, webFrame). Proprietary edge platform for Apple silicon; its retrieval examples are vector-based, which conflicts with the stack choice (agentic file search). **Check weekly:** pricing/licensing, whether model and runtime versions can be pinned, and whether webFrame-style pooling across Apple devices is independently shown to work (relevant to the D53 host sizing, unproven).
- Sources: [huggingface.co/webAI-Official](https://huggingface.co/webAI-Official) · [TwIL-LM3-Pro-LiteRT-LM model card](https://huggingface.co/webAI-Official/TwIL-LM3-Pro-LiteRT-LM) · [mradermacher/TwIL-LM3-Pro-GGUF](https://huggingface.co/mradermacher/TwIL-LM3-Pro-GGUF) · [webai.com](https://www.webai.com/). Secondary commentary (orcarouter.ai) is not evidence.

## Prepared task prompt

Copy into a desktop local-project scheduled task, using the proposed timezone/cadence above:

> Maintain the Local AI knowledge base in `/Users/davidduchesne/Work/Dbrain2` weekly. Read AGENTS.md and index.md first, then 90 System/weekly-local-model-review.md and 30 Resources/Local AI/README.md. Follow that procedure. David requested weekly updates to these model notes and the benchmark ledger; scope factual documentation changes to 30 Resources/Local AI, this runbook's review/status dates, index.md and append-only log.md. Do not change vault policy, other knowledge domains, production configuration or personal facts. Research current primary sources for local text/vision/coding, image generation/editing, ASR, TTS and retrieval models. Preserve dated evidence and record exact artifacts, licenses, benchmark methods, uncertainty and Mac relevance. Keep publisher claims separate from local measurements. Do not download model weights, install software, run unbounded benchmarks, publish, send messages or make purchases. Report promising local experiments for a separate bounded run. Commit only the scoped authorized documentation changes; preserve unrelated work and report any blocked action. Return changed notes, meaningful model/benchmark changes, unresolved contradictions, what was not checked and the next review date. If nothing materially changed, record that honestly. Never claim a local benchmark ran without saved outputs.

## Activation and operating record

| Date | Event | Evidence |
|---|---|---|
| 2026-10-01 | Initial research/manual execution of the review's documentation workflow completed | [[30 Resources/Local AI/benchmark-ledger]] and pinned source register |
| 2026-10-01 | Scheduler activation blocked | No callable scheduler tool; desktop app access denied by computer-use tool |
| 2026-10-01 | Task created in the desktop local-project scheduler by David | D60; task ID and next-run confirmation **still to be pasted here** |
| 2026-10-08 | First scheduled run (Thu), session `session_01Dyiwy1hfwHSo73fG8E1Vjx` | Ran in a cloud session through the linked-computer tools; origin unreachable (no credentials), so branch `cowork/local-model-review-2026-10-08` is local only. Output: ledger entry 2026-10-08 and the notes in [[30 Resources/Local AI/benchmark-ledger]]. No missed run. Duration: not recorded. Coverage gap: metadata and revision checks only; step 2's review of publisher collections and release notes was not completed. Task ID and timezone still not pasted |
| Pending | Verify the second run (due 15 Oct 2026) | Record actual output, duration and any missed/failed run. Review the first two runs before relying on the cadence |

Weekly monitoring does not mean upgrading weekly. Candidate promotion requires the project's regression/acceptance gates and rollback plan.
