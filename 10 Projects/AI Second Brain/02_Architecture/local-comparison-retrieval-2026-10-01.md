---
classification: internal
created: 2026-10-01
status: development evidence; not acceptance
---
# Local comparison and first retrieval baseline — 1 October 2026

David authorized continuing the local experiments and documenting the model landscape. This extends [[10 Projects/AI Second Brain/02_Architecture/local-benchmark-2026-10-01|the first hardware/model report]]; it does not replace its results.

**Conclusion:** a second small model runs on the existing Mac, but neither tested configuration is accepted. Retrieval coverage and evidence faithfulness need work before a read-only service is considered reliable. No cloud inference, voice/image test, autonomous agent or vault-writing service was introduced.

## Same-prompt comparison

The second artifact is **Qwen3.5-4B Q4_K_M**, converted by Unsloth from the Qwen model. It is a community conversion, not an official Qwen GGUF release. [Original card](https://huggingface.co/Qwen/Qwen3.5-4B) · [Artifact publisher](https://huggingface.co/unsloth/Qwen3.5-4B-GGUF)

- Repository revision: `e87f176479d0855a907a41277aca2f8ee7a09523`.
- File: `Qwen3.5-4B-Q4_K_M.gguf`, 2,740,937,888 bytes.
- Download verified against repository LFS SHA-256: `00fe7986ff5f6b463e62455821146049db6f9313603938a70800d1fb69ef11a4`.
- Same M2/24 GiB host and llama.cpp build b11146; eight existing development cases and **unchanged prompt-v2** from the first report; one sequential pass per model, not an interleaved controlled trial.
- Context 4,096, one slot, GPU layers 99, four CPU threads, temperature 0, seed 42, maximum 220 generated tokens, prompt cache disabled, thinking disabled. Text only; no visual projector.

| Measure | Qwen3-4B, previous prompt-v2 run | Qwen3.5-4B, same prompt |
|---|---:|---:|
| Requests / distinct cases | 8 / 8 | 8 / 8 |
| Median full API response | 6.76 s | 7.41 s |
| p95 nearest-rank / observed maximum | 12.28 s | 9.58 s |
| Median first answer content | 4.86 s | 4.44 s |
| Median generation rate | 22.72 tokens/s | 22.66 tokens/s |
| Maximum sampled server RSS | 3.35 GiB | 3.66 GiB |
| Responses with nonempty, allowed citation IDs only | 7/8 | 1/8 |
| Token-limit truncations | 0 | 0 |

At eight requests, p95 is simply the slowest observed request, not a dependable tail-latency estimate. Desktop workload and memory pressure were not controlled. RSS does not represent all unified GPU/CPU memory. These runs do not establish a speed or quality winner.

**Qualitative review (Codex, not independent human grading):** Qwen3.5 correctly denied client-data permission and ignored the hostile source in the single supplied-evidence example. It omitted citations on seven answers, invented an extra requirement to complete all stages before multi-agent work, and omitted restore from the write-gate answer. The shared prompt specified valid citation markers but did not explicitly require one on every factual answer; that prompt weakness is part of this configuration's result. A model upgrade does not remove the need for pipeline validation.

## First index/file-search baseline

The experiment read `index.md`, verified the allowlisted paths were cataloged, then snapshotted:

- `AGENTS.md`;
- `02_Architecture/data-policy.md` in this project;
- only §0 of `04_Roadmap.md`, the current amendment. Historical packages were intentionally outside this prototype corpus.

No arbitrary file access or model-selected tools were provided. The script rejects symlink/path mismatches and missing/invalid classification for these files. This is a bounded experiment, not an audited production sandbox or automatic index navigation.

The script splits the corpus into **26 heading/size-based chunks**, applies a simple BM25 implementation and returns the top three positive-scoring passages. Each has a source ID, path, line span and file hash. There is no vector database or embedding model.

Ten development questions exercised seven answerable in-corpus requests, one required fact outside the chosen corpus, and two deliberately absent facts. An initial exact-phrase probe returned 5/8. Review found equivalent client-policy evidence was actually present, while the archival destination was absent from the entire corpus. Corrected interpretation: **6/7 in-corpus answerable questions had supporting evidence retrieved; one French query missed it.** Across the eight desired factual questions, coverage was 6/8. The raw probe and correction are both preserved.

Generation used Qwen3.5 and a **new explicit-citation prompt**. This is a different pipeline experiment, not an improved same-prompt comparison score:

| Measure | Retrieval-to-answer development run |
|---|---:|
| Requests | 10 |
| Median / p95-nearest-rank API response time | 6.14 / 7.97 s |
| Median first answer content | 4.21 s |
| Median generation rate | 20.59 tokens/s |
| Maximum sampled server RSS | 4.06 GiB |
| Responses with nonempty, allowed citation IDs only | 8/10 |
| Token-limit truncations | 0 |

Latency here measures the generation API request after retrieval; it excludes retrieval, startup, mobile networking and speech. The server remained loaded after the comparison run. Citation counts include abstentions and measure syntax only; the French and password abstentions had no markers.

**Important failures:** the archival question received a confidently wrong answer—triaged captures were placed in `00 Inbox/`—with valid citation IDs. The correct D49 archive rule was outside the corpus. The French query correctly received an insufficient-evidence response, so abstention worked while end-to-end retrieval failed. The write-gate answer covered exact patch and restore but omitted base-revision binding. The media answer imprecisely said “outside the system” instead of “outside the vault.” Missing GPU-count and password questions correctly abstained.

Six additional cases were reserved in a separate file and **never executed**. They are provisional, agent-authored cases requiring independent label review; this is not yet an acceptance dataset. P2.1 and P2.3 remain open. No deterministic semantic-support guard was implemented by this experiment.

## Preserved artifacts and reproduction

Durable external directory: `/Users/davidduchesne/Documents/Dbrain2-artifacts/local-models/2026-10-01/` — benchmark inputs, scripts, raw responses, measurements, manual review, public model-card snapshots and metadata. Root `SHA256SUMS.json` inventories the evidence. No weights or runtime binaries were copied into this archive or the vault.

Within `benchmark/`: original baseline files, `prompt-v2/`, `qwen35-v2/` and `retrieval-v1/`. `continuation_manual_review.json` explains the corrected retrieval denominator and observed failures. The saved runners retain the exact temporary paths used for execution: copy to a fresh experiment directory, adjust output/root paths explicitly and verify the frozen cases/prompt before a rerun. Do not append a new run to old `results.jsonl`.

Temporary runtime: `/private/tmp/dbrain2-local-benchmark/llama-b11146/llama-server`. Both model files remain under `/private/tmp/dbrain2-*.gguf`; they can be removed by OS cleanup and are not durable installations. Reacquire from pinned revisions/checksums if needed. Runtime download provenance is in the first report.

The comparison server used `--host 127.0.0.1 --port 18087 --offline --no-ui --no-agent --cors-origins http://localhost`, with the inference flags above. This temporary endpoint had no authentication; it was not exposed as a remote service. The process was terminated after testing and exited successfully. Offline mode and no configured cloud fallback are not a complete network audit.

## Next bounded work

1. Add the authoritative D49 retention decision to a declared corpus, without broadening to arbitrary personal notes. Test bilingual query expansion against the frozen lexical baseline.
2. Separate retrieval coverage, citation syntax, citation support, completeness and abstention scoring. Add independent expected-evidence review and freeze acceptance criteria before acceptance runs.
3. Compare another model family; repeat comparable trials under recorded workload conditions and then test sustained performance.
4. Keep T9/P2 open until requirements and acceptance evidence support a selection. Remote availability/device requirements remain OQ-14/OQ-15.

Related: [[30 Resources/Local AI/README]] · [[30 Resources/Local AI/benchmark-ledger]]
