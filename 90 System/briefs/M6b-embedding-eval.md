---
classification: internal
task: M6b   # final ID, assigned by the lead 8 Oct (session 37)
owner: "@code"
status: open   # David approved the 25 GB budget and the Python environment on 8 Oct; starts after T9/M6 (D94)
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

## Done when
Manifest committed; raw rankings and scores saved; results note written with per-case outcomes for all three arms; the decision rule above applied step by step; Codex pass on the note; PROGRESS/TASKS updated; follow-up rows proposed to David.

## Constraints
- **Approved by David, 8 Oct ("raise disk budget to 25GB, install required Python environment"; recorded as D100):** the Q8 weights-and-runtimes budget is raised from 20 GB to **25 GB** (T9/M6's ≈18.25 GB plus about 2.7 GB here leaves about 4 GB spare), and an isolated Python venv with `sentence-transformers` and `torch` may be created on the Air outside the vault and outside iCloud, with pinned package versions recorded in the manifest. Both apply only to the models and packages named in this brief. The text below is the question as asked.
- **(Was blocked on David; hard limits):** (1) disk budget: T9/M6 already uses about 18.25 of the 20 GB (Q8). Embedding weights add roughly 1.5 GB (EmbeddingGemma 2 bf16, estimated from 740M parameters; text-only loading may avoid fetching the other encoders only if the repository allows partial files, which it does not appear to) and 1.2 GB (Qwen3-Embedding-0.6B bf16), about 2.7 GB, which exceeds the budget by about 1 GB. Options for David: raise Q8 by 3 GB; or free 2.5 GB by deleting the duplicate `/private/tmp` Qwen3-4B (offered earlier, Q42 only covered another copy); or use a Q8_0 GGUF of Qwen3-Embedding-0.6B from the official `Qwen/Qwen3-Embedding-0.6B-GGUF` repository (to be verified, ~0.6 GB). (2) A Python environment with `sentence-transformers` and `torch` on the Air, needed because EmbeddingGemma 2 ships safetensors only. Use an isolated venv outside the vault.
- Sequence after T9/M6 (D94): the T9 window needs David present and sizes the host (deadline 16 Oct); do not run both at once, since contention would corrupt T9's latency data.
- Data policy: no client data; secrets never in files an agent can read.

## Review
(lead, from Codex)

## Outcome
(owner)
