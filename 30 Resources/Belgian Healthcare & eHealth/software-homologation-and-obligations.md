---
classification: public
status: draft
updated: 2026-10-01
---

# Software homologation and obligations

What a product must do to be legally usable, commercially viable and fundable in Belgian ambulatory
care. This is the page that turns the domain into a requirements list.

## Three separate gates, often conflated

| Gate | Granted by | What it unlocks |
|---|---|---|
| **Accepted / labelled software suite** | The *Commission nationale médico-mutualiste* (medicomut) | The doctor's eligibility for the practice premium; recognition as a usable EHR |
| **Registration with the eHealth platform** | eHealth platform | Technical access to the platform's services; a record in the Software Register |
| **MyCareNet approval, per service** | NIC/CIN | The right to use each MyCareNet service in production |

They are independent. A product can be technically connected and still not "accepted"; it can be
accepted and still lack approval for a specific MyCareNet service. **MyCareNet approval is granted
service by service** — Member Data, Chapter IV, DMG, tariff consultation, invoicing, eAttest V3,
insurability are listed separately — which means the roadmap can be sequenced rather than
all-or-nothing. See [[vendor-landscape]].

## Hard legal obligations on providers (and therefore on software)

| Obligation | Since | Applies to |
|---|---|---|
| **Electronic prescription** of medicines | Mandatory in ambulatory care | Doctors, dentists, midwives |
| **Recip-e v4 connector** required to create prescriptions | 1 October 2020 | Prescribers' software |
| **Recognised electronic medical record** to manage the DMG | 1 January 2021 | GPs |
| **Electronic invoicing** of all compulsory-insurance services | **1 September 2025** | GPs, specialists, dentists |
| **Sumehr** production, export and import | 2005 | EHR labelling requirement |

If your software cannot do these, your user is non-compliant. That reframes them: they are not
features competing for roadmap space, they are preconditions.

## Technical requirements published to vendors

From INAMI's software-vendor pages:

- **INAMI number check digits** — implement **modulo 89** alongside the existing **97, 83 and 79**.
  Formula and detail in **annex 16.3 of the electronic billing instructions**.
- **Document justificatif** (proof of care given) — required in four scenarios: electronic attestation,
  electronic invoicing, mixed reimbursable/non-reimbursable services, and non-reimbursable services.
  INAMI publishes a summary of the regulatory obligations specifically for software.
- **Rounding** of the amount paid by the patient — published rules.
- **Dated nomenclature code changes**, pushed directly at vendors with deadlines. Documented example:
  the type-2 diabetes starter pathway, effective 1 January 2024, changing `102852` → `400374` (private
  practice) and `109594` → `400396` (medical homes), with medication prescription lists to be updated
  by 1 February 2024.

Contacts: `esante@riziv-inami.fgov.be` (eHealth projects) and `healthcare-registration@smals.be`
(practical registration).

## Registration and testing

For the newer projects, INAMI and Smals run a structured registration process:

- Integration modes: **web component, FHIR API, or hybrid**.
- **Pre-registration testing** against a FHIR test server.
- Validation by **video demonstration or live videoconference**, depending on integration complexity.
- **Fixed registration and testing windows.** The eReferral (home nursing) example: live test sessions
  6 April – 16 October 2026, retests 19–30 October 2026, registration closing 14 September 2026.
- Technical documentation and reference files published via the **Smals GitHub**.

Operationally: missing a window can cost a year. Treat the registration calendar as a dependency in
release planning, not as paperwork.

## The practice premium as the real specification

The *prime de pratique intégrée* is where homologation becomes money. It pays a GP annually based on
**measured e-service usage**, and the measurement is of outcomes in the real world — not of features
your software possesses.

### Amounts (2025)

| Situation | Condition | Amount |
|---|---|---|
| 1 | Active GP, but no accepted software **or** below thresholds | €1,000 |
| 2 | Accepted software + **5** of 7–8 parameters | €3,500 |
| 3 | Accepted software + **6** of 7–8 parameters | €4,500 |
| 4 | Accepted software + **7 or more** of 7–8 parameters | €6,000 |
| — | Trainees using accepted software | €800 |

Eligibility also requires being effectively active as a GP (or trainee) during the premium year.
Applications for 2025 run **28 August – 30 November 2026**, submitted via **ProSanté**, paid to a
registered bank account in at least biannual instalments. Contact: `medecins-dentistes@riziv-inami.fgov.be`.

### The 2025 parameters

Fee-for-service GPs are measured on **8** parameters; GPs in medical groups or homes on **7**.

| # | Parameter | Threshold (2025) |
|---|---|---|
| 1 | Chapter IV medication reimbursement requests via the MyCareNet "Chapitre IV" service | ≥ **50%** of requests, during H2 2025 |
| 2 | Billing for patients entitled to increased intervention, via **eFact**, or attestations via **eAttest** | ≥ **50%** of consultations |
| 3 | **Sumehr** uploaded via RSW, Abrumet or Vitalink, by 31 December 2025, relative to patients generating DMG fees for 2025 | ratio ≥ **60%** |
| 4 | **Medication schemes** created or adapted | ≥ **5**, during H2 2025 |
| 5 | **CEBAM Evidence Linker** used | ≥ **5** times, during H2 2025 |
| 6 | Electronic *"Évaluation du handicap – SPF Sécurité sociale"* forms sent | ≥ **3** |
| 7 | Electronic work-incapacity certificate to the funds via **Mult-eMediatt** | ≥ **1**, during Q4 2025 |
| 8 | Registration to the **barometers** — diabetes, antibiotics, kidney insufficiency | ≥ **2 of 3**, before the respective end-2025 deadlines |

*(Which parameter is dropped for medical-home GPs is not stated on the pages consulted; parameter 2 is
the plausible candidate, since forfait centres do not bill per act — **inference, to verify**.)*

### Why this is the most useful page in the whole knowledge base

Read the table again as a product specification. It tells you, with thresholds:

- the **exact services** the software must support end to end (Chapter IV, eFact/eAttest, Sumehr
  upload to three hubs, medication schemes, CEBAM, two federal e-forms, barometer registration),
- that success is **measured as a rate**, so adoption and workflow fit matter more than capability —
  a feature nobody uses scores zero,
- that there are **deadlines inside the year** (H2, Q4, 31 December), so the software should be nagging
  the user in November, and
- that the delta between the bottom and top tier is **€5,000 per GP per year**.

A product that instruments these eight numbers and shows a doctor their live score, with "do these
three things to reach €6,000", is selling a measurable financial outcome rather than software. That is
the clearest value proposition available in this market, and it falls straight out of public policy.

## Build implications

1. **Treat the eight parameters as the acceptance criteria of the product**, and instrument each one as
   a live metric per practitioner.
2. **Sequence MyCareNet certification by service**, and pick the order from the premium parameters —
   insurability and eFact/eAttest first, then Chapter IV, then the rest.
3. **Sumehr quality is a revenue feature.** The 60% ratio is against the DMG population, so the system
   must know that denominator and actively close the gap.
4. **Build the obligations in before the differentiators.** E-prescription, recognised EHR for DMG and
   electronic invoicing are table stakes; without them the user cannot legally operate.
5. **Make reference-data and code-change updates a routine release train** with external deadlines.
   Validate check digits locally against all moduli, configurably.
6. **Put registration windows in the roadmap** as hard dates.
7. **Consider web components for decision-support obligations** as a compliance shortcut, while
   building native integrations where experience is the selling point.

## Gaps and figures to verify

- Whether the medicomut remains the accepting body, and the current acceptance procedure and criteria.
- Which parameter is excluded for medical-home GPs.
- 2026 amounts and parameters (reported unchanged by a doctors' union — unconfirmed), and the 2026
  application window.
- The full published criteria for the "accepted software suite" label.
- Whether the eHealth platform's own registration imposes additional functional criteria.
- The practice-premium budget envelope (a figure of ≈ €59.8M for 2024 circulates in the medical press —
  unverified, deliberately not stated as fact here).

Sources: [[sources]].
