---
classification: internal
created: 2026-10-01
last_reviewed: 2026-10-08
next_review: 2026-10-15
---
# Finding evidence: lexical search, embeddings and rerankers

A language model cannot reliably answer from a note it never receives. Improve source coverage and retrieval separately from generation. Current vault practice is index-first file search, with no vector index.

| Technique | What it does well | Limitation |
|---|---|---|
| Index + file search | Transparent routing, exact names/IDs, low infrastructure cost | Synonyms and cross-language questions can miss relevant text |
| BM25 lexical ranking | Ranks passages using query terms and their rarity/length normalization | Different wording or French questions over English notes can fail |
| Embedding model | Encodes text into vectors to retrieve semantically related passages | Can miss exact identifiers; index versions, updates and permissions must be managed |
| Reranker | Scores a query against a short candidate list more carefully | Adds latency and cannot recover a passage absent from the candidates |

**[Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B)** is a multilingual embedding candidate: publisher specifications include 32K context, up to 1,024-dimensional vectors and instruction-aware queries. Apache-2.0. It creates representations, not cited answers.

**EmbeddingGemma 2** (Google, Apache-2.0) is a second embedding candidate, read from publisher pages only: see [[30 Resources/Local AI/embeddinggemma-2-evaluation|the 8 Oct desk evaluation]]. Its local test is defined by [[90 System/briefs/M6b-embedding-eval|M6b]].

**[Qwen3-Reranker-0.6B](https://huggingface.co/Qwen/Qwen3-Reranker-0.6B)** is a candidate for ranking query/document pairs. Apache-2.0. A relevance score is not a probability that the answer is true. Neither model is installed or locally tested here.

Seen 8 Oct, not evaluated: webAI's [ColVec1.1 4B/8B](https://huggingface.co/webAI-Official/webAI-ColVec1.1-4b) multi-vector visual-document retrievers (Qwen3.5 based, license `other`, updated Aug 2026). They embed page images, which conflicts with the current plain-markdown, no-vector-RAG stack; record only.

## What the first retrieval experiment found

The [[10 Projects/AI Second Brain/02_Architecture/local-comparison-retrieval-2026-10-01|1 October experiment]] searched 26 chunks from three allowlisted, index-listed files. Human-style agent navigation across the whole vault was not tested.

- Evidence was present in the top three chunks for **6 of 7 in-corpus answerable development questions**, based on Codex's qualitative review.
- A French voice question missed the English plan; the model appropriately abstained.
- The corpus omitted the D49 archival destination. The model nevertheless asserted the wrong location using real citation IDs.

The automated exact-phrase probe initially reported 5/8, because it missed equivalent policy wording and included an out-of-corpus question in its answerable denominator. Keep the raw result and the review correction; do not mistake a string matcher for semantic grading.

**Next experiment:** expand the declared corpus to include the authoritative retention decision; add controlled bilingual query expansion and compare against this frozen baseline. Only add embedding/reranking infrastructure if it solves measured misses at acceptable cost. Keep source hashes, paths/line spans, permitted roots and citations attached through the pipeline. Source text must never expand tool permissions.

Related: [[30 Resources/Local AI/benchmark-ledger]] · [[30 Resources/Local AI/model-fundamentals]]
