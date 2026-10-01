---
classification: internal
created: 2026-10-01
last_reviewed: 2026-10-01
next_review: 2026-10-08
---
# Local model fundamentals

## The components

| Component | Meaning | Example |
|---|---|---|
| Model weights | Learned numerical parameters | Qwen3.5-4B |
| Model artifact | A specific format, revision and precision of those weights | A pinned Q4_K_M GGUF file |
| Runtime | Software that loads weights and performs inference | llama.cpp or MLX LM |
| Application | Retrieval, prompts, interface, storage and error handling | The planned second-brain service |
| Agent | A bounded workflow that chooses actions using a model and permitted tools | Curator or evidence checker |

A model capable of producing tool calls does not itself have file access. The application decides whether to execute a request. Different agent roles do not require separate model weights or simultaneous inference.

[llama.cpp](https://github.com/ggml-org/llama.cpp) supports local inference, GGUF artifacts and Apple acceleration. [MLX LM](https://github.com/ml-explore/mlx-lm) is an Apple-silicon language-model inference/fine-tuning toolkit. Compatibility is specific to the architecture and runtime version. An API with a familiar request format can still point to a local server; inspect the endpoint and fallback configuration.

## Reading names and memory claims

**B means billions of parameters.** Dense models use their main network for each token. A mixture-of-experts model activates a subset, reducing some computation, but normally still needs storage and memory for the full weights. For example, Qwen3-Coder-30B-A3B has about 30.5B total and 3.3B active parameters. Treating it as a 3B memory requirement would be wrong. [Publisher card](https://huggingface.co/Qwen/Qwen3-Coder-30B-A3B-Instruct)

**Quantization** reduces numerical precision to lower weight memory, often with some quality change. Q4_K_M is a mixed quantization format, not a guarantee that every parameter costs exactly four bits. Different conversions of the same base model can behave differently. Record the publisher, converter, revision and checksum.

Approximate weight-only arithmetic is `parameters × bits / 8`. At ideal four-bit storage, 4B parameters need about 2 GB and 27B about 13.5 GB, before metadata and higher-precision tensors. **This is a lower-order estimate, not a fit guarantee.** Runtime buffers, encoders, conversation state, the OS and other apps add memory. GB and GiB are different units.

**Context window** is how much input/history/output a configuration can handle. An advertised large maximum is neither the memory allocation we tested nor a guarantee of reliable recall. Our first experiments used 4,096 tokens. Longer prompts also take time to process before the first answer token. Hybrid attention changes memory behavior, so do not extrapolate one architecture's cache costs to all models.

**Thinking mode** spends additional generated tokens on reasoning. It can help some tasks and increase latency; more reasoning is not always more reliable. Compare thinking/non-thinking settings explicitly. The local experiments so far disabled thinking.

## Practical boundaries

“Open weights” means weights are available under stated terms. It does not automatically mean open training data, unrestricted commercial use or an identical license across a family. Check the exact checkpoint and dependencies.

“Local” describes where inference runs. It does not establish privacy for the entire application: downloads, telemetry, plugins, remote clients, logs and fallback calls are separate data flows. The temporary tests used local files and an offline-mode localhost server; that is not a packet-level audit of the whole Mac. The vault's [[10 Projects/AI Second Brain/02_Architecture/data-policy|data policy]] still applies.

For this 24 GiB Mac, start with one small quantized language model and measure speech components separately. A model loading successfully is weaker evidence than acceptable sustained latency while ordinary applications are open. Process RSS is useful but is not a complete measure of unified CPU/GPU memory.

Related: [[30 Resources/Local AI/benchmark-ledger]] · [[30 Resources/Local AI/README]]
