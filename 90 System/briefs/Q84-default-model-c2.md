---
classification: internal
task: Q84 / P2.4
owner: "@code"
status: done
models: ["claude-opus-5-5 (lead)"]
created: 2026-10-08
source: David, 8 Oct, Q84 (a) "adopt C2 (Gemma 4 E4B) as the default for the query service"; T9 run 2026-10-08-a
review_status: proposed
note_type: brief
---
# Switch the phone service's default model to C2 (Gemma 4 E4B)

## Goal (one sentence)
The MVP phone service (`Ask Brain.command` → `mvp/run-all.sh`) answers with Gemma 4 E4B QAT Q4_0, the model T9 picked and David adopted (Q84 (a)), run with the flags T9 measured it under, and the tests and dev cases pass on it.

## Files in scope (agent may touch only these)
- `~/Work/dbrain-runtime/`: `mvp/run-all.sh`, `mvp/prepare-model.sh`, `mvp/README.md` (model lines only), `dbrain/adapter.py` (the default model label only), `experiments/mvp_smoke.py` (model path and server flags only), `artifacts/` (evidence, not committed).
- This brief; TASKS (P2.4 and `@david` lines); PROGRESS; `log.md`.
- Recording David's answers Q84 (a) and Q83 (a): `10 Projects/AI Second Brain/DECISIONS.md` (D105), `90 System/for-david.md` (Answered).
- The four models' T9 numbers, as David asked in Q84 (a): `30 Resources/Local AI/benchmark-ledger.md` (new dated section) and `30 Resources/Local AI/text-and-vision.md` (status cells).
- **Not in scope:** the T9 runner and its pins; `measure.sh` (benchmark tool, keeps its own `DBRAIN_MODEL` override); the prompt; retrieval; anything on the new host.

## Inputs / context to read first
- [[10 Projects/AI Second Brain/02_Architecture/t9-model-comparison-2026-10-08|T9 results]]; [[90 System/briefs/T9-M6-model-comparison|T9/M6]] (server flags); [[90 System/briefs/MVP-phone|MVP-phone]].
- `models/MANIFEST.md` (C2 pin `676c3507…`, already on disk; no download).

## Done when (checkable)
1. `run-all.sh` starts `gemma-4-E4B_q4_0-it.gguf` after checking its SHA-256 against the C2 pin, with T9's server flags (`--reasoning off` added; context 4096 unchanged).
2. The adapter reports the C2 model name in traces; the request signature is unchanged (`3e00bced79dc`).
3. The full unit suite passes.
4. The 10 dev cases run against C2 on the service's pipeline (no-network sandbox), results saved under `artifacts/`.
5. The MVP smoke test runs end to end with C2 (loopback, no-network sandbox) and **passes** when: health answers 200; a wrong and a missing token get 401; with the model down the answer is 503 `unavailable` (no fallback); and on the questions shared with the last Qwen run (5 Oct, run d) C2 misses no question Qwen answered. Answer misses that Qwen also had are listed as known limitations, not as failures of the switch.
6. Codex review passes; committed and pushed. David restarts `Ask Brain.command` to pick it up (it is stopped now).

## Constraints
- No download (C2 is on disk and pinned). Reserved acceptance cases never run. Provider keys unset; the model endpoint stays loopback.

## Review
## Outcome
**8 Oct (session 39), before review.** Runtime working tree on `ae934d5`:
- `mvp/run-all.sh`: model `gemma-4-E4B_q4_0-it.gguf`, SHA-256 checked against `676c3507…` before start, `--reasoning off` added (T9's flags). `mvp/prepare-model.sh`: checks the C2 pin, never downloads it. `dbrain/adapter.py`: default label `gemma-4-E4B_q4_0-it` (traces). `experiments/mvp_smoke.py`: C2 and T9's flags. `mvp/README.md`: model lines.
- **Tests:** 202, OK (40 s), twice; transcript `artifacts/q84-c2-2026-10-08/unit-tests.log`; the exact commands for every run are in `commands.md` there. `prepare-model.sh` run after the fix: pin checks only, "ready".
- **Dev cases** (`artifacts/q84-c2-2026-10-08/dev-cases.json`, no-network sandbox, corpus `878a08ea6f57`): all 10 answers identical to T9's C2 block; p50 8.09 s, p95 10.26 s (n = 10); the report names the model `gemma-4-E4B_q4_0-it`; request signature unchanged.
- **MVP smoke** (`artifacts/q84-c2-2026-10-08/mvp-smoke/`, whole vault, sandbox): health 200, wrong or missing token 401, model down 503 `unavailable` (no fallback). 10/14 expected substrings; three of the four misses also missed with Qwen on 5 Oct (run d, 11/14 on its 14 questions): the network question (C2 now declines instead of answering wrongly), 13 Oct waste, this week's bins (C2 answers about meals: off-topic). The fourth is a format miss: the hot-lunch deadline is answered correctly as "Friday, October 16". p50 8.44 s, p95 18.16 s (n = 14; 5 Oct Qwen: 9.93 / 13.04 s).
- **Against criterion 5: pass.** Known limitations (listed for David, not regressions): the network, 13 Oct waste and this week's bins questions; the hot-lunch check is a wording mismatch on a correct answer.
- **Review round 1 (Codex `gpt-6.1-sol`, high, read-only, Tier 1): FAIL**, one blocker (scope narrower than the change) and four should-fixes (`prepare-model.sh` still required the old baseline; smoke pass criteria undefined; Local AI rows without a T9 link, p50 and token rates; commands and test output not preserved). All fixed: scope widened, the baseline made optional, criterion 5 defined, rows completed, `commands.md` and `unit-tests.log` saved.
- **For David:** restart `Ask Brain.command` to use C2 (it is stopped).
- **Committed:** runtime `7874b6f`, pushed; vault commit below. Review round 2 should-fixes (review_status on the two Local AI notes; README wording) applied.
