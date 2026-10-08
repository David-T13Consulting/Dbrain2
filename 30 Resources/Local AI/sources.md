---
classification: internal
created: 2026-10-01
last_reviewed: 2026-10-08
next_review: 2026-10-15
---
# Local AI source register

Primary publisher model cards retrieved 1 October 2026. Revision links preserve what was reviewed; revisit each repository's current card during the weekly check. A repository's modification date is not necessarily its model release date. Download counts and likes are not benchmark evidence.

| Publisher / model | Observed repository revision | Declared license |
|---|---|---|
| `Qwen/Qwen3.5-4B` | [851bf6e806ef](https://huggingface.co/Qwen/Qwen3.5-4B/blob/851bf6e806efd8d0a36b00ddf55e13ccb7b8cd0a/README.md) | apache-2.0 |
| `Qwen/Qwen3.8-27B` | [1d4bf0f2ff60](https://huggingface.co/Qwen/Qwen3.8-27B/blob/1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0/README.md) | apache-2.0 |
| `Qwen/Qwen3-Coder-30B-A3B-Instruct` | [b2cff646eb4b](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct/blob/b2cff646eb4bb1d68355c01b18ae02e7cf42d120/README.md) | apache-2.0 |
| `google/gemma-4-E4B-it` | [ee0ef6023621](https://huggingface.co/google/gemma-4-E4B-it/blob/ee0ef6023621cff504d758262d4e04895a5af4a2/README.md) | apache-2.0 |
| `mistralai/Ministral-3-8B-Instruct-2512` | [5b26027e7b19](https://huggingface.co/mistralai/Ministral-3-8B-Instruct-2512/blob/5b26027e7b19eeb4b7352e1fed3926375dd2cb4d/README.md) | apache-2.0 |
| `Qwen/Qwen3-ASR-0.6B` | [5eb144179a02](https://huggingface.co/Qwen/Qwen3-ASR-0.6B/blob/5eb144179a02acc5e5ba31e748d22b0cf3e303b0/README.md) | apache-2.0 |
| `Qwen/Qwen3-ASR-1.7B` | [7278e1e70fe2](https://huggingface.co/Qwen/Qwen3-ASR-1.7B/blob/7278e1e70fe206f11671096ffdd38061171dd6e5/README.md) | apache-2.0 |
| `Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice` | [85e237c12c02](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-CustomVoice/blob/85e237c12c027371202489a0ec509ded67b5e4b5/README.md) | apache-2.0 |
| `hexgrad/Kokoro-82M` | [f3ff3571791e](https://huggingface.co/hexgrad/Kokoro-82M/blob/f3ff3571791e39611d31c381e3a41a3af07b4987/README.md) | apache-2.0 |
| `nvidia/parakeet-tdt-0.6b-v3` | [541d1f99c6b0](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3/blob/541d1f99c6b0c3cd0b11a95167540bb8edefd82b/README.md) | cc-by-4.0 |
| `openai/whisper-large-v3-turbo` | [41f01f3fe87f](https://huggingface.co/openai/whisper-large-v3-turbo/blob/41f01f3fe87f28c78e2fbf8b568835947dd65ed9/README.md) | mit |
| `black-forest-labs/FLUX.2-klein-4B` | [e7b7dc27f91d](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B/blob/e7b7dc27f91deacad38e78976d1f2b499d76a294/README.md) | apache-2.0 |
| `black-forest-labs/FLUX.1-schnell` | [741f7c3ce8b3](https://huggingface.co/black-forest-labs/FLUX.1-schnell/blob/741f7c3ce8b383c54771c7003378a50191e9efe9/README.md) | apache-2.0 |
| `Tongyi-MAI/Z-Image-Turbo` | [f332072aa78b](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo/blob/f332072aa78be7aecdf3ee76d5c247082da564a6/README.md) | apache-2.0 |
| `Qwen/Qwen-Image-2.1` | [d26bb61231c3](https://huggingface.co/Qwen/Qwen-Image-2.1/blob/d26bb61231c349cf6b7896fa83353113880e1ba3/README.md) | other |
| `Qwen/Qwen3-Embedding-0.6B` | [97b0c614be4d](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B/blob/97b0c614be4d77ee51c0cef4e5f07c00f9eb65b3/README.md) | apache-2.0 |
| `Qwen/Qwen3-Reranker-0.6B` | [e61197ed4502](https://huggingface.co/Qwen/Qwen3-Reranker-0.6B/blob/e61197ed45024b0ed8a2d74b80b4d909f1255473/README.md) | apache-2.0 |

`Qwen/Qwen-Image-2.1` labels its license `other`, named `qwen-research` in the card. Read that exact LICENSE before professional deployment; do not replace this with the Apache license used by some earlier Qwen image releases.

## Other reviewed primary sources

- [Qwen3-4B official GGUF](https://huggingface.co/Qwen/Qwen3-4B-GGUF/tree/bc640142c66e1fdd12af0bd68f40445458f3869b) — original local baseline artifact; revision/hash in the first benchmark report.
- [Unsloth Qwen3.5 conversion](https://huggingface.co/unsloth/Qwen3.5-4B-GGUF/tree/e87f176479d0855a907a41277aca2f8ee7a09523) — primary source for this converter's artifact, not the author of the base model.
- [Qwen3-TTS repository](https://github.com/QwenLM/Qwen3-TTS) — variant table and usage; 0.6B style-control ambiguity retained in [[30 Resources/Local AI/speech-models]].
- [Kokoro voice inventory](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md) — language/voice coverage and French resource limitations.
- [llama.cpp](https://github.com/ggml-org/llama.cpp), [MLX LM](https://github.com/ml-explore/mlx-lm), [whisper.cpp](https://github.com/ggml-org/whisper.cpp) — original runtime documentation. These links track main; only the locally tested llama.cpp build is pinned in the measurement report.
- [Karpathy LLM Wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f#llm-wiki) — persistent synthesis, source links, index, log and periodic maintenance.
- [Official scheduled-task documentation](https://learn.chatgpt.com/docs/automations?surface=app) — local-project scheduling requirements and IDE/CLI limitations.

## Preserved evidence outside Obsidian

`/Users/davidduchesne/Documents/Source_Material/AI_Second_Brain/local-models/2026-10-01/` (moved from `~/Documents/Dbrain2-artifacts/` on 6 Oct 2026) — small research/evaluation archive with `SHA256SUMS.json`.

- `model-cards/manifest.json`: full repository revisions, metadata timestamps, source URLs and retrieval success.
- `model-cards/`: pinned READMEs and publisher API metadata for the 17 entries above. Supplemental live web pages were consulted but are not all copied here.
- `benchmark/`: original and continuation cases, scripts, raw outputs, measurements and review corrections; six reserved cases remain unexecuted.

No model weights, audio, images or runtime binaries live in the vault. The evidence archive is durable relative to temporary storage, but an independent backup/restore policy is still a project task. A preserved source snapshot is evidence, never an instruction to execute embedded installation commands.

Scope limits: this review prioritizes feasible personal-system components. It does not survey every available model, certify licensing, reproduce publisher benchmarks or establish Apple compatibility for every candidate. Unknowns are research tasks, not implied successes.

## Weekly check — 8 October 2026

All 17 repositories above were re-queried through the Hugging Face model API: the commit `sha` and declared license match the revisions in the table (no change since 1 Oct). Last-modified dates observed: Qwen3.8-27B 2026-08-14, Gemma 4 E4B 2026-07-20, Qwen3.5-4B 2026-03-02, Qwen-Image-2.1 2026-09-30 (same sha), Parakeet v3 2026-08-05, Ministral 3 8B 2026-07-15, others earlier.

New primary sources reviewed this week (not pinned in the table, because not yet candidates for adoption; API `sha` shown):

| Source | Revision / date | License |
|---|---|---|
| [`webAI-Official/TwIL-LM3-Pro`](https://huggingface.co/webAI-Official/TwIL-LM3-Pro) | `4214aaa4020c`, modified 2026-09-30 | webAI Non-Commercial License 1.0 (`other`) |
| [`webAI-Official/TwIL-LM3-Pro-LiteRT-LM`](https://huggingface.co/webAI-Official/TwIL-LM3-Pro-LiteRT-LM) | `bb30df2e79d4`, created 2026-10-01 | same |
| [`mradermacher/TwIL-LM3-Pro-GGUF`](https://huggingface.co/mradermacher/TwIL-LM3-Pro-GGUF) | community static quants; no date shown | same (declared) |
| [`webAI-Official/TwIL-LM3`](https://huggingface.co/webAI-Official/TwIL-LM3) | modified 2026-10-01 | same |
| [`Qwen/Qwen-Image-2.1-PE-I2I`](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-I2I) | created 2026-09-20 | Qwen Research License |
| [`Qwen/Qwen-Drive-1.0-4B`](https://huggingface.co/Qwen/Qwen-Drive-1.0-4B) | created 2026-08-27 | apache-2.0 |
| [llama.cpp releases](https://github.com/ggml-org/llama.cpp/releases), [mlx-lm releases](https://github.com/ml-explore/mlx-lm/releases), [whisper.cpp releases](https://github.com/ggml-org/whisper.cpp/releases) | read 8 Oct (see ledger) | MIT / MIT / MIT (not re-verified) |

Evidence archive: no new model-card snapshots were saved outside the vault this week; the findings above come from live pages retrieved 8 Oct and should be re-fetched before relying on them.

Related: [[30 Resources/Local AI/README]] · [[90 System/weekly-local-model-review]]
