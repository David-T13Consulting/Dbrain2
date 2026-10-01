---
classification: public
status: draft
updated: 2026-10-01
---

# Belgian healthcare & eHealth — knowledge base

Reference knowledge on how Belgian ambulatory healthcare works institutionally, financially and
technically. Written for someone building software for healthcare centres: a multi-user practice
system that talks to the institutional rails (eHealth platform, MyCareNet, Recip-e, the regional
hubs) and runs the practice itself.

**Classification `public`.** Every page here is built from published documentation — INAMI/RIZIV, the
eHealth platform, the Collège Intermutualiste National (MyCareNet), official journals and vendor
documentation. No client or counterparty material, no confidential product internals of any employer
or vendor. See [[sources]] for the full source register and [[#What this deliberately excludes]].

## Reading order

| # | Page | What it answers |
|---|---|---|
| 1 | [[institutions-and-actors]] | Who the players are and who decides what |
| 2 | [[reimbursement-and-financial-flows]] | How money actually moves: nomenclature, fee-for-service vs forfait, DMG |
| 3 | [[mycarenet-services-and-flows]] | The billing and administrative rails, message by message |
| 4 | [[billing-rules-and-cumulation]] | Cross-cutting primer: the four same-day patterns, place, time, qualification |
| 4a | [[nomenclature-map]] | **All 63 articles**, mapped to professions and key letters, with rule density |
| 4b | [[billing-engine-rule-model]] | **The engine spec**: 19 constraint types, evaluation order, schemas, test cases |
| 4c | Per profession | [[billing-rules-physicians]] · [[billing-rules-physiotherapy]] · [[billing-rules-nursing]] · [[billing-rules-dental]] · [[billing-rules-midwifery]] · [[billing-rules-speech-therapy]] · [[billing-rules-labs-and-imaging]] · [[billing-rules-devices-and-aids]] |
| 5 | [[ehealth-platform-and-apis]] | The federal technical platform and its ~80 APIs |
| 6 | [[identity-access-and-consent]] | Who is allowed to see a record, and how that is proven |
| 7 | [[clinical-data-sharing-and-standards]] | KMEHR, FHIR, hubs, Sumehr, VIDIS, Recip-e |
| 8 | [[software-homologation-and-obligations]] | What a product must do to be legal and fundable |
| 9 | [[regulatory-and-compliance]] | GDPR, Quality Law, MDR, AI Act, EHDS |
| 10 | [[vendor-landscape]] | Who already sells into this market |
| 11 | [[integration-architecture]] | How a modern system plugs into SOAP-era rails |
| — | [[glossary]] | Acronym decoder. This domain is dense with them |
| — | [[sources]] | Primary sources, with URLs and retrieval dates |

## The eleven things that matter most

1. **Two parallel worlds, one patient.** Clinical data sharing (hubs, Sumehr, KMEHR/FHIR) and
   administrative/financial exchange (MyCareNet, INAMI layouts) are separate stacks with separate
   standards, separate governance and separate history. A practice system has to span both.
2. **The eHealth platform is plumbing, not a database.** It supplies identity, encryption, mailboxes,
   timestamping and an index of where documents live. Clinical content sits in hubs, regional vaults
   and the providers' own systems. See [[ehealth-platform-and-apis]].
3. **It is SOAP underneath.** Of roughly 80 published APIs, almost all are SOAP/XML; only two are
   FHIR R4 today. FHIR is the stated direction, not the current reality. See [[integration-architecture]].
4. **Message numbers are the lingua franca of billing.** `801000` asks whether a patient is insured,
   `920000` submits an invoice batch, `920900` settles it. Learn the numbering and the billing domain
   becomes legible. See [[mycarenet-services-and-flows]].
5. **Electronic billing is no longer optional.** Since 1 September 2025 GPs, specialists and dentists
   must bill compulsory-insurance services electronically.
6. **Two incompatible revenue models coexist.** Fee-for-service (acte) and capitation (forfait, used by
   maisons médicales). They produce entirely different data, workflows and cashflow.
   See [[reimbursement-and-financial-flows]].
7. **Homologation is a commercial gate, not just a badge.** A GP's annual practice premium scales with
   measured e-service usage, and only accepted software lets them hit the thresholds. The software's
   job is to make a doctor score well. See [[software-homologation-and-obligations]].
8. **Access control is a first-class clinical feature.** Consent, therapeutic links and patient-set
   exclusions decide who may read what. These are federal services, not application logic.
   See [[identity-access-and-consent]].
9. **Clinical decision support drags in MDR and the AI Act.** The moment software interprets rather
   than records, it risks being a medical device and a high-risk AI system simultaneously.
   See [[regulatory-and-compliance]].
10. **Reference data is downloaded, not queried.** Nomenclature arrives as published files and
    circulars; there is no documented public nomenclature API. Software must ingest and version it.
11. **The nomenclature is a rules engine, not a price list.** The same clinical act carries different
    codes by qualification, place, time of day and what else was billed that day — and "a second
    service on the same day" is handled four incompatible ways across doctors, surgery,
    physiotherapy and nursing. **The key letter encodes the profession; paired code numbers encode
    ambulatory vs hospitalised.** All 63 articles are mapped in [[nomenclature-map]]; the 19 constraint
    types a billing engine must implement are specified in [[billing-engine-rule-model]].

## How to use this with a build

Each page ends with a **Build implications** section: what the facts on that page force a system to
do. Those sections are the bridge from domain knowledge to architecture, and are the parts most
likely to need revisiting as the regulatory picture moves.

## Status and confidence

Written 1 October 2026 in one research pass. Confidence varies by page and is stated inline:

- **High** — anything cited to INAMI, the eHealth platform, the eHealth API portal or MyCareNet pages.
- **Medium** — figures from the medical press, federation sites or vendor documentation.
- **To verify** — flagged inline and collected per page under *Gaps and figures to verify*. Nothing
  flagged should be quoted to a third party without checking the primary source first.

Amounts, thresholds, deadlines and message versions in this domain change at least annually. Treat
every number as "as at the retrieval date in [[sources]]", not as a standing fact.

## What this deliberately excludes

- Confidential internals of any vendor or employer — code, architecture, roadmaps, customer lists,
  unpublished pricing, internal metrics. Confidentiality obligations outlive other contract terms.
- Any contract terms, including David's own restrictive covenants. Barred by `data-policy.md` §2.1.
- Patient data and any third-party health data, in any form, synthetic or otherwise (§2.4).
- Venture-specific strategy: positioning, pricing, ICP, targets. That belongs in a project note at
  `internal`, not in a public reference folder.

Related: [[Second Brain Best Practices]] for how pages here are meant to be written.
