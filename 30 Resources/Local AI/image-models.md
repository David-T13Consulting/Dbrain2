---
classification: internal
created: 2026-10-01
last_reviewed: 2026-10-08
next_review: 2026-10-15
---
# Local image generation and editing

These models create pixels; [[30 Resources/Local AI/text-and-vision|vision-language models]] primarily interpret images. Useful jobs include illustrations, visual concepts, backgrounds and image edits. Exact diagrams, tables and data charts often remain better as SVG, Mermaid or plotting code because labels and values must stay correct.

All capability claims below come from the linked publishers. **None has been benchmarked on this Mac.** Memory and speed statements from CUDA hardware are not Apple measurements.

| Model | Strengths / useful work | Weaknesses / local implications | Exact license metadata |
|---|---|---|---|
| **[FLUX.2 klein 4B](https://huggingface.co/black-forest-labs/FLUX.2-klein-4B)** | Compact generation plus multi-reference editing; suitable candidate for interactive image work | Publisher reports roughly 13 GB VRAM for its consumer-GPU setup. That is not a 13 GB total application budget or proof of sub-second generation on an M2 | Apache-2.0 for **4B**; do not transfer this to the 9B variant |
| **[Z-Image-Turbo](https://huggingface.co/Tongyi-MAI/Z-Image-Turbo)** | 6B distilled generator, eight function evaluations; publisher emphasizes realistic images and English/Chinese text | Published sub-second latency uses an H800. French typography and Apple runtime support need tests; Turbo and editing/base variants have distinct roles | Apache-2.0 |
| **[Qwen-Image-2.1](https://huggingface.co/Qwen/Qwen-Image-2.1)** | Recently verified generation/editing entry; native RGBA/transparency, local edits and multiple reference images | 7B refers to the visual generation component, not necessarily the whole pipeline. New dependencies and Apple fit are unverified | **Qwen Research License**, custom; do not assume prior Qwen image licenses carry forward |
| **[Qwen-Image-2.1-PE-I2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-I2I) / [PE-T2I](https://huggingface.co/Qwen/Qwen-Image-2.1-PE-T2I)** | Companion prompt-rewriter (fine-tuned Qwen3.5-VL 9B, BF16) that turns vague edit or generation instructions into precise prompts for Qwen-Image-2.1; both created 20 Sep 2026 (PE-I2I rev `72927bc0`, PE-T2I rev `f3ed7985`) | Adds a 9B model to the 7B generator; no benchmarks reported; CUDA/transformers examples only, Apple fit unverified | Qwen Research License (as reported 8 Oct); same caution as the parent |
| **[FLUX.1 schnell](https://huggingface.co/black-forest-labs/FLUX.1-schnell)** | Established 12B few-step text-to-image baseline | Larger weights than compact candidates; fast sampling does not imply low total memory. Keep as a historical comparator rather than assuming it is current best | Apache-2.0; distinct from FLUX.1 dev terms |

Check the exact license file before selecting a professional-use artifact; model availability and permission to deploy it are separate questions. No legal conclusion about the custom Qwen license is made here.

## Meaningful comparison

Freeze prompts, seeds, resolution, sampling steps, quantization and runtime. Score prompt adherence, visible artifacts, exact text, subject consistency and edit preservation separately. Record time per image and peak memory at that resolution. Use a fixed prompt set spanning realistic photos, illustrations, French/English labels and a controlled edit; retain failures as well as attractive outputs.

Publisher showcase pictures are curated examples, not a reproducible accuracy benchmark. Do not rank these models by a single selected image, or compare a small-resolution distilled run with a full-resolution high-step run without stating the difference.

Generated images, model weights and reference media remain outside the vault. Only pointers and the evaluation record belong here. Image generation is an optional capability track, not a prerequisite for the initial local second-brain query service.
