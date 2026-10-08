---
classification: internal
created: 2026-10-01
last_reviewed: 2026-10-08
next_review: 2026-10-15
---
# Models for text, reasoning, code and visual understanding

Vision-language models read images and produce answers about them. This does not make them image generators. OCR/document understanding also needs validation: a fluent answer can misread a number or omit a table row.

Capability descriptions below are publisher-reported; suitability and limitations are engineering assessments unless marked measured. All listed checkpoints declare Apache-2.0 in their model metadata checked on 1 October, except TwIL-LM3-Pro (webAI Non-Commercial License 1.0, checked 8 October). Exact revisions: [[30 Resources/Local AI/sources]].

| Model / checkpoint | Strengths and useful work | Weaknesses / selection implications | Local status |
|---|---|---|---|
| **Qwen3-4B**, Q4_K_M | Existing small text/reasoning baseline; useful for short, supplied-evidence answers | Measured citation, language and hostile-source failures. Keep as a regression baseline, not the “current best” | Measured on the M2; [[10 Projects/AI Second Brain/02_Architecture/local-benchmark-2026-10-01|first report]] |
| **[Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B)** | Compact text + vision model; document questions, multilingual answers and general coding/reasoning experiments | Default thinking differs from our test. Large advertised context is untested here. Small-model factual and instruction errors remain | Text-only Q4_K_M measured; no vision projector or image test |
| **[Gemma 4 E2B/E4B](https://huggingface.co/google/gemma-4-E4B-it)** | Text, image and audio inputs; compact multimodal assistant candidate | “Effective” size is not total weights: E4B has about 8B including embeddings. Input audio support does not prove speech output. Check the actual runtime's modality support | Not tested here; quantized variants are candidates |
| **[Ministral 3 8B Instruct 2512](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512)** | Multilingual instruction following, vision, structured output and function calling; French/English alternative | About 8.4B language parameters plus 0.4B vision encoder. Higher memory than a 4B baseline; publisher FP8/CUDA fit claims do not establish M2 performance | Not tested; evaluate a compatible quantization |
| **[Qwen3.8-27B](https://huggingface.co/Qwen/Qwen3.8-27B)** | Newer verified family entry; publisher emphasizes coding, research, professional tasks and image/video understanding | Considerably more memory; thinking and agent loops add latency. On this busy 24 GiB host, fit/performance need a separate experiment | Watchlist; not downloaded or selected |
| **[Qwen3-Coder-30B-A3B-Instruct](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)** | Coding and tool-use specialization; useful comparator for a future code agent | All experts count toward weight storage. Code benchmarks do not establish faithful note synthesis, safe actions or useful French voice interaction | Watchlist; not a lightweight 3B deployment |

| **[TwIL-LM3-Pro](https://huggingface.co/webAI-Official/TwIL-LM3-Pro)** (webAI, Granite 4.2 3B fine-tune) | Formal-logic reasoning (3.66B, text only); GGUF and LiteRT-LM builds | **Non-commercial license**; "not a general assistant"; vendor-only benchmarks (see ledger 8 Oct); thinking needs 2048+ output tokens; LiteRT bundles capped at 4,096 context | Watchlist, shortlisted for a bounded S5 trial **after David resolves the license**; not downloaded |
Qwen3.5-4B is being tested because of size and runtime fit, not because it is the newest Qwen generation. Do not infer that an architecture announcement or a Transformers integration proves downloadable small checkpoints exist.

## How to choose for the vault

Favor correct, cited short answers over an impressive general benchmark score. Test exact dates, contradictions, absent evidence and required language. For a proposed note update, require a source-supported patch; the model's confidence is not authorization.

Our unchanged-prompt comparison found Qwen3.5 omitted citation markers in seven of eight responses. A later explicit-citation prompt improved formatting in a different retrieval experiment, but one confidently wrong answer still carried valid citations. This distinguishes **citation syntax** from **evidence support**. See [[10 Projects/AI Second Brain/02_Architecture/local-comparison-retrieval-2026-10-01]].

A future comparison should add a different model family, hold workload and prompt conditions steady, and use independently checked expectations. No candidate has passed a final acceptance set.
