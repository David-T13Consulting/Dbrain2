---
classification: internal
task: M6b   # final ID, assigned by the lead 8 Oct (session 37)
owner: "@code"
status: blocked-on-david # S2 done 9 Oct (session 44); S3 blocked on Q94: protocol item 2's label source holds totals only
models: []
created: 2026-10-08
source: David, 8 Oct ("Yes", run the EmbeddingGemma 2 evaluation); desk note [[30 Resources/Local AI/embeddinggemma-2-evaluation]]
review_status: proposed
note_type: brief
---
# Retrieval test: EmbeddingGemma 2 vs Qwen3-Embedding-0.6B vs the lexical baseline (M6b)

## Goal (one sentence)
Measure whether either embedding model recovers evidence the lexical baseline misses, on the frozen cases, before any embedding infrastructure is considered (S2 rule: no embeddings without a measured miss).

## Why this is a brief and not a Cowork run
Cowork's computer shell is a 3 GB Linux VM (Cowork's own report of its environment, 8 Oct): Hugging Face is blocked by its allowlist, there is no torch, and the frozen cases live outside the connected folder. The test must run on the Air by the lead, like the 1 Oct runs.

## Gemma 4 is already covered
Gemma 4 E4B (official QAT Q4_0 GGUF, Google repo `google/gemma-4-E4B-it-qat-q4_0-gguf`) is candidate #2 in [[90 System/briefs/T9-M6-model-comparison|T9/M6]], already downloaded and hash-verified. Do not duplicate it here and do not change the frozen T9 protocol. Only if T9 results are wanted for the embedding side: nothing to add. Gemma 4 E2B stays the T9 reserve.

## Files in scope
- `~/Work/dbrain-runtime/experiments/` (a new `embedding-eval/` folder) and `artifacts/` for pins and raw rankings.
- A dated results note in `10 Projects/AI Second Brain/02_Architecture/` (`review_status: draft`) with `index.md` / `log.md` entries.
- This brief, TASKS (M6b line), `10 Projects/AI Second Brain/PROGRESS.md`, `90 System/for-david.md`.
- `10 Projects/AI Second Brain/DECISIONS.md`: only the rows recording David's answers for this brief (D122, Q92; added 9 Oct, session 44, after review).
- Not in scope until David confirms: `30 Resources/Local AI/` rows (propose them in the queue).

## Inputs to read first
[[30 Resources/Local AI/embeddinggemma-2-evaluation]], [[30 Resources/Local AI/retrieval-models]], `local-comparison-retrieval-2026-10-01` (frozen 26-chunk corpus, 10 lexical cases, the French miss, the corpus gap), the evidence archive `Source_Material/AI_Second_Brain/local-models/2026-10-01/benchmark/retrieval-v1/`.

## Protocol (frozen before any result is seen)
1. **Arms:** (A) the lexical baseline as in `retrieval-v1`; (B) `google/embeddinggemma-2`, text path only, bfloat16 or float32 (never float16), documented task prefixes, 768 d and 256 d re-normalized; (C) `Qwen/Qwen3-Embedding-0.6B` with its query instruction, full dimension. Same chunks, same cases, no generation step.
2. **Cases:** the 10 retrieval-v1 cases, the French-query cases, and the corpus-gap case, with expected evidence labels fixed from `continuation_manual_review.json`. Reserved acceptance cases are never used.
3. **Corpus:** the same 26 chunks first. A second pass on the whole-vault index files is allowed only for `classification: public|internal` notes passing the label allowlist (Q46); never client material.
4. **Metric:** expected-evidence recall at top 3 and top 5, per case and in total, plus wrong-evidence hits in the top 3. Cold and warm load time and peak RSS are recorded but are not the selection criterion. Small n: report counts, no percentages as proof.
5. **Pins:** before any download, a manifest with repository, immutable revision, file names, sizes and full SHA-256 read from the publisher at that moment. `embeddinggemma-2` was a single squashed commit (`914f7f89142e`, 8 Oct): record whatever revision is current, and treat a change after the manifest as a new candidate.
6. **Boundaries:** weights outside the vault, no HF cache copy kept in the vault, network blocked during scoring, raw rankings saved with hashes; no run counts unless its saved outputs exist.
7. **Accept as a retrieval candidate only if:** it recovers at least one miss the lexical baseline had (including the French query against the English plan) without adding wrong-evidence hits in the top 3. Otherwise record "no measured benefit" and keep the lexical baseline.

## Steps (D111, D112: each step committed before the next; 5 reviews per step, `Review n/5 · M6b Sx` before each Codex call; 12 per run)
Cut by Cowork, 9 Oct. The protocol above is frozen and applies to every step; a step changes nothing in it.
0. **S0 · Bookkeeping (lead, 9 Oct, session 43).** Record Cowork's step cut, David's Q90/Q91 answers (`for-david.md`) and D119 (DECISIONS); commit on its own before S1 starts. No experiment work.
1. **S1 · Manifest and environment.** Read the publishers' current revisions and write the manifest (protocol item 5: repository, immutable revision, file names, sizes, full SHA-256), plus the pinned package versions; create the isolated venv outside the vault and iCloud (D100). Check free disk against the 25 GB budget and record it. **No weights downloaded.** Commit the manifest.
2. **S2 · Download and verify.** Fetch both models outside the vault (no HF cache copy in the vault); verify every file against the S1 manifest; a mismatch or a newer revision stops the step and is reported (protocol item 5: a change is a new candidate). Record disk used. Commit the verification record.
3. **S3 · Harness, toy data only.** `experiments/embedding-eval/`: the three arms (protocol item 1), the frozen case list and labels loaded read-only (item 2), metrics (item 4), network blocked during scoring, raw rankings saved with hashes (item 6). Tests on a tiny made-up corpus only; the real cases are not scored in this step. Commit.
4. **S4 · Scored run.** One run on the 26-chunk corpus, all three arms; raw outputs, scores, cold/warm load and peak RSS saved. Not alongside any other measurement run. A run without saved outputs does not count. Commit the artifacts.
5. **S5 · Results note and decision.** Dated note in `02_Architecture/` (`review_status: draft`), per-case outcomes for all three arms, protocol item 7 applied step by step, `index.md`/`log.md` entries, follow-up rows to David in `for-david.md`. The note's measured claims and any new decision are Tier 2: after the Codex pass the note waits **uncommitted** for David's batched approval (queued in `for-david.md`); `review_status: draft` does not replace that approval. Commit only after he approves. **Stop and report.**
6. *(Optional, only if S5 shows a recovered miss and David says so)* **S6 · Whole-vault second pass** under protocol item 3 (label allowlist, never client material).

## Done when
Manifest committed; raw rankings and scores saved; results note written with per-case outcomes for all three arms; the decision rule above applied step by step; Codex pass on the note; PROGRESS/TASKS updated; follow-up rows proposed to David.

## Constraints
- **Approved by David, 8 Oct ("raise disk budget to 25GB, install required Python environment"; recorded as D100):** the Q8 weights-and-runtimes budget is raised from 20 GB to **25 GB** (T9/M6's ≈18.25 GB plus about 2.7 GB here leaves about 4 GB spare), and an isolated Python venv with `sentence-transformers` and `torch` may be created on the Air outside the vault and outside iCloud, with pinned package versions recorded in the manifest. Both apply only to the models and packages named in this brief. The text below is the question as asked.
- **(Was blocked on David; hard limits):** (1) disk budget: T9/M6 already uses about 18.25 of the 20 GB (Q8). Embedding weights add roughly 1.5 GB (EmbeddingGemma 2 bf16, estimated from 740M parameters; text-only loading may avoid fetching the other encoders only if the repository allows partial files, which it does not appear to) and 1.2 GB (Qwen3-Embedding-0.6B bf16), about 2.7 GB, which exceeds the budget by about 1 GB. Options for David: raise Q8 by 3 GB; or free 2.5 GB by deleting the duplicate `/private/tmp` Qwen3-4B (offered earlier, Q42 only covered another copy); or use a Q8_0 GGUF of Qwen3-Embedding-0.6B from the official `Qwen/Qwen3-Embedding-0.6B-GGUF` repository (to be verified, ~0.6 GB). (2) A Python environment with `sentence-transformers` and `torch` on the Air, needed because EmbeddingGemma 2 ships safetensors only. Use an isolated venv outside the vault.
- Sequence after T9/M6 (D94): the T9 window needs David present and sizes the host (deadline 16 Oct); do not run both at once, since contention would corrupt T9's latency data.
- Data policy: no client data; secrets never in files an agent can read.

## Review
(lead, from Codex)

**Run of 9 Oct (session 43).** Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only).
- **S0 · bookkeeping before S1** (a step of its own, committed before S1 starts: this Steps section as cut by Cowork, Q90/Q91 recorded, D119; the separate webAI weekly-review entry was reviewed in the same call).
  - Review 1/5 · M6b S0: **fail**, 1 blocker (the review was counted against S1, which would commit mid-step; fixed by making S0 its own step). Should-fix, applied: S5 keeps the Tier 2 gate; the status line names the C4 fallback.
  - Review 2/5 · M6b S0: **fail**, 1 blocker (S0 was not in the Steps section; added). Should-fix, applied: S5's Tier 2 note waits uncommitted for David's approval.
  - Review 3/5 · M6b S0: **pass**, no findings. Committed.
- **S1 · blocked, nothing committed (session 43).** Read 9 Oct ~11:55 from the Hugging Face API: `google/embeddinggemma-2` revision `914f7f89142e33e77833254d9c9b90c3cef7303b` (unchanged since 8 Oct; 1,525,810,123 bytes; `model.safetensors` SHA-256 `197a3296…5d79`), `Qwen/Qwen3-Embedding-0.6B` revision `97b0c614be4d77ee51c0cef4e5f07c00f9eb65b3` (1,207,489,041 bytes; `model.safetensors` `0437e45c…23fd`); the small files were fetched at those revisions and matched their git ids (no weights downloaded). Weights about 2.73 GB; models folder now 15 GB, so about 17.7 of the 25 GB budget; 79 GiB free on the disk. **Blocker:** EmbeddingGemma 2 requires `sentence-transformers` >= 6.1.0, and that version, `transformers` 5.19, `torch` 2.14.1, `tokenizers` and `safetensors` all need Python >= 3.10 (PyPI metadata, read 9 Oct: [sentence-transformers 6.1.0](https://pypi.org/pypi/sentence-transformers/6.1.0/json), [transformers 5.19.0](https://pypi.org/pypi/transformers/5.19.0/json), [torch 2.14.1](https://pypi.org/pypi/torch/2.14.1/json)); the requirement >= 6.1.0 is in `~/Work/dbrain-runtime/experiments/embedding-eval/evidence-embeddinggemma-2-914f7f89-config_sentence_transformers.json` (fetched from https://huggingface.co/google/embeddinggemma-2/resolve/914f7f89142e33e77833254d9c9b90c3cef7303b/config_sentence_transformers.json); the Air has only Python 3.9.6, and installing another Python is a download no brief names. Queued as **Q92**. The full draft manifest (every file, size and SHA-256) is **uncommitted** at `~/Work/dbrain-runtime/experiments/embedding-eval/manifest-draft.json`; the next run re-reads the revisions before using it (protocol item 5). The record of this block (this entry, Q92, TASKS, PROGRESS, session close) is bookkeeping, not S1's output: S1's manifest and venv stay uncommitted until S1 finishes.
  - Review 1/5 · M6b S1 (the block record and session-close bookkeeping)
    PASS. Should-fix, applied: Q91's stale task line removed; version-specific PyPI links and the saved config evidence cited; the Homebrew size marked `unverified`.

**Run of 9 Oct (session 44): S1, fresh step budget.** Lead `claude-opus-5-5`; reviewer Codex `gpt-6.1-sol` (review profile, high, read-only).
- **S1 · done (pending review).** Python: Homebrew `python@3.12` 3.12.15, arm64, installed by David 9 Oct 11:59 (Q92 → **D122**). Revisions re-read from the Hugging Face API at 14:32: `google/embeddinggemma-2` `914f7f89142e33e77833254d9c9b90c3cef7303b`, `Qwen/Qwen3-Embedding-0.6B` `97b0c614be4d77ee51c0cef4e5f07c00f9eb65b3`, both unchanged since session 43, so its file list, sizes and SHA-256 stand. Venv `~/Library/Application Support/dbrain/venvs/m6b-py312` (outside the vault, iCloud and git), pins `sentence-transformers==6.1.0`, `transformers==5.19.0`, `torch==2.14.1`, 41 packages frozen in the manifest, 1.0 GB, Apple GPU backend available. Disk: 78 GiB free before the venv, 76 GiB after. **Budget (D100, weights and runtimes, 25 GB):** T9/M6's allocation ≈18.25 GB (the models folder measures 15 GB today) + this venv 1.0 GB + S2's weights 2.73 GB ≈ **22.0 GB**, about 3 GB spare. **No weights downloaded.** Manifest: runtime `experiments/embedding-eval/manifest.json` (commit `89d9bd5`) (the session 43 draft beside it stays uncommitted).
- **Run notes (D114):** no subagents used this run.
- Review 1/5 · M6b S1
  FAIL. Blocker: DECISIONS.md (D122) was not in the brief's files in scope. Should-fix: the budget counted only the models folder, not T9/M6's allocation and the venv. Fixed: DECISIONS.md listed for this brief's answer rows; the budget restated against D100 (≈22.0 of 25 GB) in this record and the manifest. Verified by Codex read-only: Python 3.12.15 arm64 from Homebrew, the venv's location and 41 pins, a clean `pip check`, both model records equal to session 43's, no weights on disk. Apple GPU availability could not be confirmed from Codex's sandbox (the lead's own check: available).
- Review 2/5 · M6b S1
  PASS. Nit, applied: the log says no model *weights* were downloaded (packages and a config file were).
- **S2 · done (pending review).** Revisions re-read just before the fetch: unchanged. `experiments/embedding-eval/fetch_verify.py` (new) fetched only the manifest's files at its revisions with the venv's `huggingface_hub`, into `~/Library/Application Support/dbrain/models/embeddings/<org>__<name>@<rev12>/` (Hugging Face's cache pointed there too; nothing in `~/.cache/huggingface`, nothing in the vault), and checked every file's size and full SHA-256: `google/embeddinggemma-2` 15/15 files, 1,525,810,123 bytes; `Qwen/Qwen3-Embedding-0.6B` 12/12 files, 1,207,489,041 bytes; **all match**. Record: runtime `experiments/embedding-eval/verification.json` (commit `cfb665a`). Disk: folders 1.4 GB and 1.1 GB on disk; 74 GiB free after. Budget as in S1: ≈22.0 of 25 GB. Unauthenticated requests (no token used or stored).
- Review 1/5 · M6b S2
  FAIL. Blocker: a revision change or a mismatch on the first model did not stop the step: the second model was still downloaded. Should-fix: an inherited `HF_HOME` or `HF_XET_CACHE` could point the cache into the vault. Fixed: each file is verified right after its download and the first problem records itself and ends the step (nothing more is fetched); `HF_HOME`, `HF_HUB_CACHE`, `HF_XET_CACHE` and `HF_ASSETS_CACHE` are forced into the app folder. Checked with mocks: a changed revision → 0 downloads; a mismatch on the first file → 1 download, then stop; a vault-pointing `HF_XET_CACHE` is overridden (no folder appeared in the vault). The real fetch re-run with the fixed script: 27/27 files match again.
- Review 2/5 · M6b S2
  PASS, no findings. Committed runtime `cfb665a`.
- **S3 · blocked-on-david (Q94), nothing built.** Protocol item 2 fixes the expected evidence "from `continuation_manual_review.json`"; that file holds totals only (`retrieval`: 7 answerable, 6 present in the top 3, 1 French miss, 1 rule outside the corpus, 2 unanswerable), no per-case passages. A mechanical table from `dev.json`'s expected fragments is proposed in Q94; client_policy (the 1 Oct review accepted equivalent wording without naming the passage) and media_storage (fragment in three passages) are the judgment points, and "French-query cases" exists as one case. Changing what the frozen protocol counts is not the lead's call.
- Review 1/5 · M6b S3 (the record of this block: this brief and Q94; with session 44's close: TASKS, PROGRESS, handoff, log)
  PASS. Should-fix, applied in Q94: C23 is not a media_storage label (same words, other topic); under (a) client_policy counts on C9 only for item 7, the 1 Oct credit quoted, not scored. The verbatim move of the handoff blocks could not be checked against git (the blocks were never committed).

## Outcome
(owner)
