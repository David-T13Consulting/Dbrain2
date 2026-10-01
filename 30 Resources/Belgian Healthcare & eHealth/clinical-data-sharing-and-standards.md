---
classification: public
status: draft
updated: 2026-10-01
---

# Clinical data sharing and standards

How clinical content — as opposed to billing — moves between providers. This stack is separate from
[[mycarenet-services-and-flows]] in standards, governance and history. Expect to implement both.

## The architecture: decentralised, indexed federally

There is no national clinical database. Documents stay where they were produced; a federal index says
where to look.

```
            ┌──────────────────────── Metahub (federal index) ────────────────────────┐
            │  "which hub holds documents for this patient?"                           │
            └───┬──────────────┬──────────────────┬─────────────────────┬──────────────┘
                │              │                  │                     │
            CoZo (+ ARH)   VZN KU Leuven     Brussels Health        Réseau Santé
            Flanders       / nexuzhealth     Network (Abrumet)      Wallon (RSW)
                │              │                  │                     │
            hospitals, GPs, specialists, and their document repositories

   Vitalink (Flemish regional vault) — data in regional competences: welfare, prevention
```

**Metahub** is "an index of personal data relating to patients' health". It is reachable by hubs,
individual providers, certain institutions such as hospitals and pharmacies, and by patients
themselves. It operates alongside **Consent**, **Therlink** and **Exclusions** — together the set of
services governing access to a patient's medical data. See [[identity-access-and-consent]].

### The hubs

Four hubs where GPs and specialists share health data:

| Hub | Region | Notes |
|---|---|---|
| **CoZo** (Collaborative Care Platform) | Flanders | Includes the Antwerp Regional Hub (ARH) |
| **VZN KU Leuven** / nexuzhealth | Flanders | Flemish hospital network |
| **Brussels Health Network / Abrumet** | Brussels | Officially designated by COCOM as *the* platform for electronic health-data exchange in Brussels |
| **Réseau Santé Wallon (RSW)** | Wallonia | |

**The key property: you query one hub and the metahub federates.** A provider consults a single hub and
receives information from all of them. This is the single most useful fact about the clinical stack —
you integrate with the federation, not with four networks.

**Vitalink** is distinct from the hubs: a Flemish-region **vault** for data in regional competences
(welfare and health prevention), where providers share rather than merely index. Patient-facing
counterparts include *Mijngezondheid* / `masante.belgique.be`.

## KMEHR — the incumbent standard

**KMEHR** (*Kind Messages for Electronic Healthcare Record*), introduced in **2002**, is the Belgian
clinical messaging standard. It comprises:

- an **XML message format** defined by the KMEHR XML Schema,
- a set of **reference tables**, and
- a set of **recognised medical transactions**.

Published at `ehealth.fgov.be/standards/kmehr`.

### Sumehr

The patient summary, in KMEHR terms the **SumEHR** (*Summarised Electronic Health Record*): the
condensed, shareable view of a patient — problems, medication, allergies, risks — intended for another
clinician picking the patient up.

Two reasons it matters disproportionately:

1. **Producing, exporting and importing Sumehr messages has been mandatory for the labelling of EHR
   systems since 2005.** It is a homologation requirement, not a feature choice.
2. **Sumehr publication is a premium criterion.** The practice premium measures the ratio of patients
   with an uploaded Sumehr (via RSW, Abrumet or Vitalink) to patients generating DMG fees — at least
   60% for the 2025 premium. See [[software-homologation-and-obligations]].

So Sumehr sits at the intersection of homologation, clinical usefulness and the doctor's income. If
one clinical artefact has to be excellent, it is this one.

## FHIR — the stated direction

**HL7 FHIR** was chosen as the priority standard in the federal eHealth roadmap **in 2019**.

The Belgian profiling initiative ("Belgianisation" of international resources) began with basic
profiles and guidelines for: **Patient, Practitioner, PractitionerRole, Organization, Observation,
Provenance, AllergyIntolerance** — plus the necessary **ValueSets, CodeSystems and NamingSystems**.

Reality check, from the API catalogue in [[ehealth-platform-and-apis]]: **only two production APIs are
FHIR R4** — `PrescriptionSearchSupport` and `UHMEP` (eReferral). Both come from the newest project
generation. Vitalink is migrating from KMEHR to FHIR over coming years.

**The honest summary: KMEHR is what you implement, FHIR is what you plan for.** New federal projects
arrive as FHIR REST; the installed estate stays KMEHR and SOAP. A system built now needs both, and
should put its internal clinical model closer to FHIR so the direction of travel is cheap.

## Current and incoming projects

Collected from INAMI's software-vendor track and the 2026–2029 action plan. These are where the
obligations, test sessions and registration deadlines live.

| Project | What it is | Relevance |
|---|---|---|
| **BIHR** — Belgian Integrated Health Record | Axis 2 of the action plan: authentic data sources plus better software interfaces for linking and visualising data | The strategic direction for the record itself |
| **VIDIS** | Shared medication scheme interoperability | Medication is the most-shared clinical object; a premium criterion counts medication schemes created or adapted |
| **SAMv2** | *Source Authentique des Médicaments* — authentic medicines source | Prescribing and dispensing reference data; vendor criteria published |
| **Recip-e** | Electronic prescription | Mandatory. See below |
| **eReferral** (home nursing; radiology) | Electronic referral prescriptions, via `UHMEP` FHIR R4 | Live registration test sessions ran **6 April – 16 October 2026**, retests **19–30 October 2026**, registration closed **14 September 2026**. Technical documentation and reference files via the Smals GitHub |
| **PSS Antimicrobiens** | Decision support for rational antibiotic use | Integration by web component, FHIR API, or hybrid |
| **PSS Radiologie** | Decision support for imaging | Paired with radiology eReferral |
| **BeSafeShare** | Multidisciplinary data sharing | Named in the action plan |
| **BelRAI** | Standardised care assessments | APIs in SOAP and REST |

Integration modes for the newer projects are explicitly **web component, FHIR API, or hybrid**, and
registration testing happens by **video demonstration or live videoconference** depending on
complexity. Practical contact: `healthcare-registration@smals.be`.

The web-component option is strategically interesting: it lets a vendor satisfy a requirement by
embedding someone else's UI rather than implementing a specification. Cheaper to comply, less control
over experience — a real trade-off for a product whose pitch is fluency.

## Recip-e — electronic prescription

- **Mandatory** for doctors, dentists and midwives in ambulatory care.
- Since **1 October 2020** you must use the **Recip-e v4 connector** to create prescriptions.
- Prescriptions are sent to a server where they are **encoded and stored until the patient uses them
  at a pharmacy** — which is why the "unknown recipient" encryption path (KGSS) exists.
- APIs: `Recip-e-Prescriber`, `-Executor`, `-Patient`, all v4.0 SOAP.
- Documentation at `recip-e.be/fr/documentation/`; registration via `info@recip-e.be`.
- A new proof/receipt model took effect **15 September 2021**.
- Cross-border caveat: the French pharmacists' order has publicly clarified that **Belgian electronic
  prescription receipts are not prescriptions** for dispensing in France. Useful to know before
  promising anything about patient mobility.

## Terminologies and code systems

Reference data a clinical system needs. **This section is from general domain knowledge and was not
verified in this research pass — confirm each before relying on it.**

| System | Typical use |
|---|---|
| **SNOMED CT** | Clinical terminology; Belgium holds a national licence *(to verify)* |
| **ICPC-2** | Primary-care encoding of reasons for encounter and problems |
| **ICD-10-BE** | Hospital diagnosis and procedure coding |
| **LOINC** | Laboratory observations |
| **ATC** | Medicine classification |
| **CNK** | Belgian pharmaceutical product codes |
| **INAMI nomenclature** | Billing — see [[reimbursement-and-financial-flows]] |

Note that **billing codes and clinical codes are different systems with different owners**, and
mapping between them is a genuine product problem rather than a lookup.

## Build implications

1. **Integrate the federation, not the hubs.** One hub plus metahub gives national reach. Do not build
   four integrations.
2. **Make Sumehr a first-class, continuously-maintained artefact**, not an export button. It is a
   labelling requirement, a premium criterion and the clinical handover unit all at once. Quality of
   the underlying structured data is what makes it good.
3. **Model internally in FHIR-shaped resources, serialise to KMEHR at the boundary.** This is the
   cheapest posture given that KMEHR is today's requirement and FHIR is the direction.
4. **Separate clinical coding from billing coding in the data model**, with an explicit mapping layer.
   Conflating them is a long-term trap.
5. **Treat reference data (SAMv2, nomenclature, CNK, ATC) as versioned, dated datasets** with ingestion
   pipelines and effective dates. Not configuration.
6. **Decide the web-component vs native-FHIR question per project.** For decision-support obligations,
   embedding is the fast path to compliance; building native is the path to a coherent experience.
   A product differentiating on fluency will want native for high-frequency journeys.
7. **Watch the registration calendar.** Test sessions have fixed windows and closing dates; missing one
   can cost a year.

## Gaps and figures to verify

- Whether four hubs remains current, and the exact CoZo/ARH/VZN relationship.
- Current state of the Belgian FHIR profiling programme beyond stage 1, and the published IG location.
- Every row of the terminologies table.
- Whether Sumehr labelling requirements have been updated since 2005, and the current content spec.
- VIDIS, SAMv2 and BIHR concrete vendor obligations and timelines.
- Whether additional eReferral or PSS test windows are scheduled after October 2026.

Sources: [[sources]].
