---
classification: internal
domain: professional
sensitivity: ordinary
sharing: private
source: David's capture 6 Oct 2026, archived verbatim at [[40 Archive/Inbox/2026-10-06-1512-eurouter]] (D49); facts read by Cowork from https://www.eurouter.ai/ on 8 Oct 2026
created: 2026-10-08
review_status: codex-reviewed
note_type: reference
owner: "@david"
---
# EUrouter

**David's capture (6 Oct, verbatim):** "à rajouter dans la inbox: https://www.eurouter.ai/ utiliser les modèles frontiere en restant compliant avec l'EU AI act"

## What the site says (read 8 Oct 2026, not independently verified)
| Item | Site statement |
|---|---|
| Company | EUrouter B.V., Amsterdam (KVK 42054357) |
| Product | OpenAI-compatible API gateway to 100+ models (Anthropic, OpenAI, Mistral, DeepSeek, Qwen, Google Gemma, others); routing on price/quality/latency, failover, per-key budgets, logs |
| EU residency | "EU servers", "EU data perimeter", "Region: EU-West". **Does not say** where non-EU providers' models are actually served |
| Retention | "Zero Data Retention" badge; FAQ answer empty, so the scope is unknown |
| EU AI Act | Discussed generally; **no explicit compliance claim** for EUrouter itself |
| GDPR | "GDPR ready / by default" |
| DPA | Linked in the footer; not read yet |
| Pricing | Free €0 (15% markup, 10K req/mo) · Plus €39/mo (9%) · Pro €99/mo (3%), plus token costs; enterprise on request |

## Where it fits
- **Dbrain2 runtime:** no. Local inference, no silent cloud fallback ([[10 Projects/AI Second Brain/02_Architecture/data-policy|data policy]] §5; D46).
- **Client-tier workspace / T0.7:** candidate, to be evaluated alongside direct EU-region access to the same models.
- **Thought leadership:** a possible angle on EU residency and AI Act compliance, once question 4 is answered (personal-brand priority).

## Open questions (before any use)
1. Where are Anthropic/OpenAI models actually served for EU requests (which cloud, which region)?
2. Scope of "zero data retention": EUrouter only, or also downstream providers?
3. DPA: sub-processor list, transfer mechanism, and audit rights.
4. What does routing through EUrouter change for David's obligations under the EU AI Act and under GDPR, and what would a client contract need to say about it? For the T0.7 lawyer review.
