---
classification: internal
note_type: resource
source: David's request, 8 Oct 2026; publisher pages read by Cowork on 8 Oct 2026 (Google model cards for embeddinggemma-2 and embeddinggemma-300m, Google launch blog, Qwen3-Embedding-0.6B card), linked inline
review_status: approved
created: 2026-10-08
updated: 2026-10-08
last_reviewed: 2026-10-08
next_review: 2026-10-15
---
# EmbeddingGemma 2: desk evaluation (8 Oct 2026)

Added at David's request on 8 Oct after the weekly review missed it. **Desk evaluation only: nothing was downloaded or run locally.** Fits the retrieval track in [[30 Resources/Local AI/retrieval-models]]; scores belong in [[30 Resources/Local AI/benchmark-ledger]] once the lead lands the 8 Oct branch (see handoff). **The local test is defined only by [[90 System/briefs/M6b-embedding-eval|M6b]]**; this note neither grants nor changes its scope, budget or environment.

**Sources read 8 Oct 2026** (all publisher-reported, none reproduced):
- [W1] [`google/embeddinggemma-2` model card](https://huggingface.co/google/embeddinggemma-2)
- [W2] [Google launch blog, "EmbeddingGemma 2: an open, lightweight multimodal embedding model"](https://blog.google/innovation-and-ai/technology/developers-tools/embeddinggemma-2), 6 Oct 2026, Sahil Dua and Henrique Schechter Vera (Google DeepMind)
- [W3] [`google/embeddinggemma-300m` model card](https://huggingface.co/google/embeddinggemma-300m) (the predecessor; [W1] calls it "EmbeddingGemma 1")
- [W4] [`Qwen/Qwen3-Embedding-0.6B` model card](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B)

## Artifact (registry metadata, retrieved 8 Oct)

| Field | Observation | Source |
|---|---|---|
| Repository | `google/embeddinggemma-2`, not gated | [W1] |
| Revision | `914f7f89142e`, last modified 2026-10-06, created 2026-09-14 | [W1] registry metadata |
| History | One commit, "Super-squash branch 'main'". A pinned commit hash stays immutable; what the squash hides is earlier history, and `main` can still move. **Pin the exact revision before any run** | [W1] |
| License | Apache-2.0 ([W1] tag; [W2] "commercially permissive"). The predecessor uses the `gemma` licence and is gated behind accepting Google's usage licence [W3], so this is a licence change. [W1]'s licence link resolves to Google's Apache License 2.0 text for Gemma (`ai.google.dev/gemma/apache_2`), so it is not a licence mismatch; the repository's own LICENSE file was not read | [W1] [W2] [W3] |
| Format | `model.safetensors` + sentence-transformers config in the Google repo. [W2] also lists GGUF via llama.cpp, Ollama and MLX as supported; **who publishes those GGUF files, and their hashes, not checked** | [W1] [W2] |
| Launch date | 6 Oct 2026 | [W2] |

## Publisher-reported specification

- 740M parameters in total: 270M text backbone (130M transformer + 140M embedder), 170M vision encoder, 300M audio encoder; encoders load selectively [W1]. [W2] cites about 191 MB RAM for text-only use on a phone with quantization (not measured here).
- One 768-dimensional space for text, code, images, video and audio; Matryoshka truncation to 512, 256 or 128 [W1] [W2]. Re-normalize after truncating.
- Context 8,192 tokens [W1] (predecessor: 2,048 [W3]). "100+ languages" [W1]; French not named in [W1] or [W2].
- Task prefixes on text (e.g. `task: search result | query:`); none for images, video or audio [W1].
- **Do not use float16** (NaN or silently degraded vectors); use bfloat16 or float32 [W1]. Check under Apple-silicon runtimes.
- No post-training safety tuning; the deployer owns retrieval filtering [W1].

## Publisher-reported scores, not reproduced

The two Gemma columns are at 768 d, full precision. The Qwen column's dimension and precision are not stated for these results (its native dimension is 1,024 [W4]).

| Benchmark | EmbeddingGemma 2 [W1] | Predecessor `embeddinggemma-300m` [W3] | `Qwen3-Embedding-0.6B` [W4] |
|---|---|---|---|
| MTEB (Multilingual, v2), Mean(Task) | 61.36 | 61.15 | **not comparable:** 64.33 on "MTEB (Multilingual)", version not stated; [W4] dates the *compared models'* scores to the online leaderboard of 24 May 2025 and does not explicitly date Qwen's own result |
| MTEB (English, v2), Mean(Task) | 68.46 (truncation table, 768 d) | 69.67 | 70.70 ("MTEB (Eng v2)", no date stated) |
| MTEB (Code, v1), Mean(Task) | 78.68 | 68.76 | not reported |

**Reading.**
- **Multilingual:** +0.21 points over its predecessor. No variability estimate is given, so its **statistical significance is unknown**. Read it as "no demonstrated change".
- **English:** **−1.21 points** versus its predecessor. Same caveat on significance.
- **Code:** +9.92 points ([W2] states the same figure), on the same benchmark version (code v1) for both. Harness and run differences remain unknown, but the version is not a confound.
- **Versus Qwen3-Embedding:** do not rank from these numbers. For the multilingual figures, benchmark-version and run-date comparability is not established ([W4] does not state its version); the English figures share a v2 label but come from different reports.
- **No French-specific or note-retrieval result is reported in [W1]–[W4]**, and no independent evaluation was searched for.
- Multimodal scores (MIEB-lite, MMEB v2, MSEB) are not relevant to a markdown vault.

## Fit for this project

- **Stack rule:** no embeddings until a measured retrieval miss justifies them (S2). The 1 Oct lexical baseline found evidence in the top three chunks for 6 of 7 answerable cases and failed on a French query and a corpus gap ([[10 Projects/AI Second Brain/02_Architecture/local-comparison-retrieval-2026-10-01|1 Oct retrieval comparison]]). Embeddings address the French-query part only if cross-lingual matching is the cause; a corpus gap is not an embedding problem.
- **Advantages to test:** Apache-2.0 [W1] [W2]; 8k context [W1]; small text path [W1]; multilingual claim [W1].
- **Costs and risks:** multimodal weights are unneeded (text-only loading). Runtime path: Python sentence-transformers from the Google repo, or a GGUF through the llama.cpp already used for T9 if a verified-provenance file exists [W2]; M6b decides. The float16 restriction needs checking. The English score is slightly lower than the predecessor's.
- **Versus Qwen3-Embedding-0.6B** [W4]: 32k context, user-defined 32–1024 dimensions, instruction-aware, Apache-2.0, higher reported but non-comparable multilingual score. The practical question is French/English recall on David's own notes, which only the M6b test answers.

## Local test

Defined and authorized only by [[90 System/briefs/M6b-embedding-eval|M6b]]: label allowlist, corpus passes, network blocking, manifest and output locations as written there. Starts after T9/M6 (D94).

Status: **candidate for the retrieval track; not shortlisted for the two text-model slots.** Open gaps: LICENSE text, GGUF provenance, French results, any independent evaluation, Apple-silicon runtime behaviour.
