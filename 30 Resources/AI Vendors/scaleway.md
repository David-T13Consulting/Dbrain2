---
classification: internal
domain: professional
sensitivity: ordinary
sharing: private
source: Scaleway and Mistral pages read by the lead on 19 Oct 2026 (session 52, PV1 step 2); URLs per row below
created: 2026-10-19
updated: 2026-10-19
review_status: unreviewed
note_type: reference
owner: "@david"
---
# Scaleway Generative APIs (and Mistral, for Voxtral)

Provider check for PV1 step 2 (D135): can `internal` notes be sent to these APIs under [[10 Projects/AI Second Brain/02_Architecture/data-policy|data policy]] §5? §5 assumes inputs and outputs are kept up to about 30 days and allows `public` and `internal` only, once the provider's real terms are verified.

## Scaleway Generative APIs: what the provider says
| Item | Provider's statement | Source |
|---|---|---|
| Training | "Your data is not used for training, retraining, or improving the base models." The AI conditions add: not accessible by LLM model providers, not used to improve the service, not accessible by third-party services | [1] (posted 2024-09-19, validated 2025-10-03); [2] art. 4.4 |
| Retention of prompts and outputs | "By default we apply a Zero Data Retention Policy." "Scaleway does not retain any requests or generated Content after processing … does not log this data" | [1]; [2] art. 4.4 |
| Exception | On misuse, errors or activity affecting service quality, Scaleway "may store temporarily and access the full content of HTTP requests"; "Data is stored for up to two weeks" | [1]; [2] art. 4.4 |
| Batch mode | Inputs stored for the processing time, 24 hours, then deleted (we do not use batch) | [2] art. 4.4 |
| Metadata | Request metadata (HTTP calls, status codes, timestamps) and token counts; aggregated and anonymised data kept up to 6 months | [1] |
| Ownership | Inputs and outputs "are considered data belonging to the Client" | [2] art. 4.4 |
| Location | "Your personal data may be stored in the following region: Paris, France"; models hosted "on its infrastructure in Europe without interaction with third-party services" | [1] |
| Sub-processors | Data-centre colocation in France: Op Core (EU HQ, processing EU/France). The list does not map sub-processors to Generative APIs. Last reviewed July 2025 | [3] |
| DPA | Version of 1 June 2024: services in the EU by default; no transfer or storage outside the EU without prior notice; SCCs where a transfer happens. Read from the search summary only, not the full PDF | [4] `unverified` |
| Conditions version | Specific Conditions applicable to AI Services, version of 7 Apr 2026 | [2] |
| Models for PV1 step 5 | `mistral/mistral-small-3.2-24b-instruct-2506:fp8`, `qwen3.8-27b` (exact API string to read from the model list), `qwen/qwen3-235b-a22b-instruct-2507`; audio `openai/whisper-large-v3:bf16` | [5] (validated 2026-08-14) |
| Silent model substitution | After a model's end of life, requests to it are routed to a successor (Mistral Small 3.1 → 3.2; Voxtral Small → whisper-large-v3) | [5] |

## Mistral (direct API, for Voxtral in W2)
| Item | Provider's statement | Source |
|---|---|---|
| Retention | API inputs and outputs kept for the time needed to answer, then 30 rolling days for abuse monitoring, unless zero data retention (ZDR) is active | [6] |
| Training | Pay-as-you-go API customers can opt out at any time, in the Admin panel › Privacy ("Anonymous improvement data"); the API and Vibe toggles are separate. Feedback (thumbs) can send data to training regardless | [7] |
| ZDR | On request to support, paid plans, stateless endpoints only; covers `/v1/audio/transcriptions`; not batch, files, agents | [8] |
| Location | Not stated on the pages read | — |

## Assessment against data policy §5 (lead, 19 Oct)
- **Scaleway: go for `public` and `internal`.** No training; nothing retained by default; the longest stated retention of content is two weeks (incident case), inside §5's 30-day assumption; processed in Paris by a French company. `client` stays excluded as always (red line, §1).
- **Mistral direct: go only once David has switched off the API training toggle** (Admin › Privacy); retention of 30 days matches §5 exactly. Not needed in W1 (no Voxtral call this week); revisit in W2. Data location not stated: `unverified`.
- **For the adapter (PV1 step 4):** Scaleway may silently answer with a successor model after an end of life. The adapter must compare the model named in each response with the configured model and fail closed on a mismatch, so the level badge never names a model that did not answer.
- **Open, not blocking W1:** read the full DPA PDF and the current sub-processor list against the T0.7 lawyer review; confirm whisper-large-v3's price.

## Sources
1. Scaleway, Generative APIs › Data privacy: https://www.scaleway.com/en/docs/generative-apis/reference-content/data-privacy/ (read 19 Oct 2026)
2. Scaleway, Specific Conditions applicable to AI Services, version of 7 Apr 2026: https://www-uploads.scaleway.com/Specific_Conditions_AI_Services_275907180f.pdf (read 19 Oct 2026)
3. Scaleway, sub-processor list: https://scaleway.com/en/subprocessorlist (read 19 Oct 2026)
4. Scaleway, Data Processing Agreement, version of 1 June 2024: https://www-uploads.scaleway.com/DPA_2024_ENG_b0abb5cc26.pdf (search summary only)
5. Scaleway, Generative APIs › Supported models: https://www.scaleway.com/en/docs/generative-apis/reference-content/supported-models/ (read 19 Oct 2026)
6. Mistral AI, Privacy Policy: https://legal.mistral.ai/terms/privacy-policy/ (search summary, 19 Oct 2026)
7. Mistral AI help centre, opting out of training: https://help.mistral.ai/en/articles/455207-can-i-opt-out-of-my-input-or-output-data-being-used-for-training (search summary, 19 Oct 2026)
8. Mistral AI docs, Zero data retention: https://docs.mistral.ai/admin/monitor-comply/zero-data-retention (read 19 Oct 2026)
