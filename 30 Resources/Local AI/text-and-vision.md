---
classification: internal
review_status: codex-reviewed
created: 2026-10-01
last_reviewed: 2026-10-15
next_review: 2026-10-22
---
# Models for text, reasoning, code and visual understanding

Vision-language models read images and produce answers about them. This does not make them image generators. OCR/document understanding also needs validation: a fluent answer can misread a number or omit a table row.

Capability descriptions below are publisher-reported; suitability and limitations are engineering assessments unless marked measured. All listed checkpoints declare Apache-2.0 in their model metadata checked on 1 October, except TwIL-LM3-Pro (webAI Non-Commercial License 1.0, checked 8 October). Exact revisions: [[30 Resources/Local AI/sources]].

| Model / checkpoint | Strengths and useful work | Weaknesses / selection implications | Local status |
|---|---|---|---|
| **Qwen3-4B**, Q4_K_M | Existing small text/reasoning baseline; useful for short, supplied-evidence answers | Measured citation, language and hostile-source failures. Keep as a regression baseline, not the “current best” | Measured on the M2; [[10 Projects/AI Second Brain/02_Architecture/local-benchmark-2026-10-01|first report]]. T9 (8 Oct, [[10 Projects/AI Second Brain/02_Architecture/t9-model-comparison-2026-10-08|T9 results]]): p50/p95 8.38/15.71 s, 245/27.7 tok/s (prompt/generation), peak RSS 5.07 GiB, failed the safety gate (misattributed citations); replaced as default by Gemma 4 E4B (D105) |
| **[Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B)** | Compact text + vision model; document questions, multilingual answers and general coding/reasoning experiments | Default thinking differs from our test. Large advertised context is untested here. Small-model factual and instruction errors remain | Text-only Q4_K_M measured; no vision projector or image test. T9 (8 Oct, [[10 Projects/AI Second Brain/02_Architecture/t9-model-comparison-2026-10-08|T9 results]]): p50/p95 11.17/18.21 s, 231/23.6 tok/s, peak RSS 5.47 GiB, failed the safety gate (an invented citation id) |
| **[Gemma 4 E2B/E4B](https://huggingface.co/google/gemma-4-E4B-it)** | Text, image and audio inputs; compact multimodal assistant candidate | “Effective” size is not total weights: E4B has about 8B including embeddings. Input audio support does not prove speech output. Check the actual runtime's modality support | **E4B QAT Q4_0 measured in T9 (8 Oct, [[10 Projects/AI Second Brain/02_Architecture/t9-model-comparison-2026-10-08|T9 results]]), text only:** p50/p95 7.98/10.13 s, 238/27.1 tok/s, peak RSS 5.72 GiB, the only model to pass the safety gate; **default model of the query service since 8 Oct (D105)**. E2B, image and audio not tested. **Superseded as default on 21 Oct:** Gemma 4 26B-A4B (T9c, 7 of 8 correct, p50/p95 8.5/13.8 s, peak RSS 15.31 GiB; Q152) and 12B (5 of 8, 21.7/31.3 s) were measured against E4B in T9c ([[10 Projects/AI Second Brain/02_Architecture/t9c-larger-local-model-2026-10-21|T9c]], draft); E4B is the fallback. Google also publishes MTP drafters (`-it-assistant`) for speculative decoding; unmeasured here (see ledger 22 Oct) |
| **[Ministral 3 8B Instruct 2512](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512)** | Multilingual instruction following, vision, structured output and function calling; French/English alternative | About 8.4B language parameters plus 0.4B vision encoder. Higher memory than a 4B baseline; publisher FP8/CUDA fit claims do not establish M2 performance | Q4_K_M measured in T9 (8 Oct, [[10 Projects/AI Second Brain/02_Architecture/t9-model-comparison-2026-10-08|T9 results]]), text only: p50/p95 15.58/23.74 s, 126/15.3 tok/s, peak RSS 7.05 GiB; failed the safety gate on one reviewer finding; out on latency in any case |
| **[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)** | Newer verified family entry; publisher emphasizes coding, research, professional tasks and image/video understanding | Considerably more memory; thinking and agent loops add latency. On this busy 24 GiB host, fit/performance need a separate experiment | Watchlist; not downloaded or selected |
| **[Qwen3-Coder-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)** | Coding and tool-use specialization; useful comparator for a future code agent | All experts count toward weight storage. Code benchmarks do not establish faithful note synthesis, safe actions or useful French voice interaction | Watchlist; not a lightweight 3B deployment |
| **[TwIL-LM3-Pro](https://huggingface.co/webAI-Official/TwIL-LM3-Pro)** (webAI, Granite 4.2 3B fine-tune) | Formal-logic reasoning (3.66B, text only); GGUF and LiteRT-LM builds | **Non-commercial license**; "not a general assistant"; vendor-only benchmarks (see ledger 8 Oct); thinking needs 2048+ output tokens; LiteRT bundles capped at 4,096 context | **Measured 21 Oct (T9b, [[10 Projects/AI Second Brain/02_Architecture/t9b-twil-lm3-pro-2026-10-21|T9b]], draft):** the 9 Oct Q4_K_M file fails the safety gate in both configurations (misattributed or unsupported citations); C2 stayed the default. Not shortlisted; watchlist for license/revision tracking (license unchanged 22 Oct; official Q4_K_M replaced 9 Oct, head `144a3cc`) |

Qwen3.5-4B is being tested because of size and runtime fit, not because it is the newest Qwen generation. Do not infer that an architecture announcement or a Transformers integration proves downloadable small checkpoints exist.

## How to choose for the vault

Favor correct, cited short answers over an impressive general benchmark score. Test exact dates, contradictions, absent evidence and required language. For a proposed note update, require a source-supported patch; the model's confidence is not authorization.

Our unchanged-prompt comparison found Qwen3.5 omitted citation markers in seven of eight responses. A later explicit-citation prompt improved formatting in a different retrieval experiment, but one confidently wrong answer still carried valid citations. This distinguishes **citation syntax** from **evidence support**. See [[10 Projects/AI Second Brain/02_Architecture/local-comparison-retrieval-2026-10-01]].

A future comparison should add a different model family, hold workload and prompt conditions steady, and use independently checked expectations. No candidate has passed a final acceptance set.
