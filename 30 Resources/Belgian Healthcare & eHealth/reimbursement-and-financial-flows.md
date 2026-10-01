---
classification: public
status: draft
updated: 2026-10-01
---

# Reimbursement and financial flows

How a clinical act becomes money. This is the page that determines most of the data model of a
practice system, because billing drives what must be recorded, when, and with which identifiers.

## The nomenclature

The *nomenclature des prestations de santé* is the catalogue of services reimbursable under
compulsory health insurance. Each service has:

- a **code** (the number that appears on every invoice and attestation),
- a description and the conditions under which it may be billed,
- an **official fee** (*honoraire*), and
- the **reimbursement amount** paid by the OA, the remainder being the patient's co-payment.

### How it is published and consumed

| Channel | What |
|---|---|
| **NomenSoft** | INAMI's nomenclature database and search engine — codes, descriptions, fees, reimbursements. `webappsa.riziv-inami.fgov.be/Nomen/fr/search` |
| **Moniteur belge** | Legal publication of changes |
| **INAMI circulars** | Operational communication of changes to providers and vendors |
| **Downloads** | Full nomenclature text (Word/PDF in ZIP), interpretation rules, and **reference tables extracted from NomenSoft** |

**There is no documented public nomenclature API.** INAMI's nomenclature page points to downloadable
reference tables and to specialist contacts by profession (`mednom@riziv-inami.fgov.be` for
physicians, `nomen@riziv-inami.fgov.be` for NomenSoft questions). A software product therefore has to
ingest, version and ship reference data rather than query it live. That is an architectural fact, not
a temporary inconvenience.

A structural reform of the nomenclature has been running since 2019, with scientific teams and
continuous sector consultation — so expect churn beyond ordinary annual indexation.

### Codes are context-dependent

The same clinical act can carry different codes depending on the practice setting. A documented
example, from INAMI's communication to software vendors about the type-2 diabetes starter pathway
(*trajet de démarrage*), effective 1 January 2024:

| Setting | Old code | New code |
|---|---|---|
| Private practice | 102852 | 400374 |
| Medical homes (*maisons médicales*) | 109594 | 400396 |

Two lessons for a builder. First, **setting is part of the billing key**, not a cosmetic attribute —
a system serving both private practices and maisons médicales needs setting-aware code resolution.
Second, **INAMI pushes dated code changes directly at vendors** with implementation deadlines, and in
the same communication required medication prescription lists to be updated by 1 February 2024. Code
maintenance is an ongoing release obligation with external deadlines.

INAMI also publishes rules on **rounding the amount paid by the patient** and on the mandatory
**document justificatif** (proof of care given), required in four scenarios: electronic attestation,
electronic invoicing, mixed reimbursable/non-reimbursable services, and non-reimbursable services.

## Who pays whom: the two settlement routes

### Route 1 — Cash payment (*paiement comptant*)

The patient pays the full fee, then claims reimbursement from their OA. Historically the patient
carried a paper attestation to the fund; now the provider transmits it electronically with **eAttest**
and hands the patient a justificative document carrying the receipt number.

### Route 2 — Third-party payer (*tiers payant* / *derdebetalersregeling*)

The OA pays the provider directly; the patient pays only the co-payment (*ticket modérateur*). The
provider invoices the OA electronically with **eFact**.

Third-party payer is mandatory in defined situations — notably for patients entitled to the
**increased intervention** (*intervention majorée*, the BIM/OMNIO status) *(the exact mandatory scope
and its start date — to verify)*. The practical consequence is that **insurability determines the
billing route**, which is why an insurability check precedes everything:

```
Patient presents
  └─ Insurability check (801000 → 801900)
       ├─ Third-party payer applies/allowed  → eFact  (920000 …)
       └─ Third-party payer not allowed      → eAttest (synchronous, during the visit)
```

See [[mycarenet-services-and-flows]] for the messages.

Other patient-side mechanisms that affect amounts but are administered by the OA rather than the
provider: the **maximum à facturer (MAF)**, an annual ceiling on a household's co-payments, and
various preferential statuses.

## Fee-for-service vs capitation

Belgium runs two incompatible financing models for primary care simultaneously. A system serving
"healthcare centres" will meet both, and they are not variations of one another — they produce
different data, different workflows and different cashflow.

| | Fee-for-service (*à l'acte*) | Capitation (*au forfait*) |
|---|---|---|
| Trigger for revenue | Each billable act | Patient registration, then time passing |
| Paid by | OA and/or patient, per act | OA, monthly, per registered patient |
| Core administrative object | The attestation / invoice line | The registration (*inscription*) and its lifecycle |
| Revenue risk | Coding accuracy, rejections | Registration completeness and continuity |
| Who uses it | Most practices | Maisons médicales / wijkgezondheidscentra |

### How the forfait works

The OA pays the centre a **fixed monthly amount per registered patient, per discipline**. Mechanics:

- The patient **registers** by signing a contract with the centre, on paper or **with their eID**.
- Registration takes effect on the **first day of the month following the request**.
- The forfait is paid from the first month following registration, **conditional on the centre having
  notified the patient's OA** of the registration. Notification is therefore revenue-critical.
- The patient must be in order with their mutuality for the month to be paid.

A published worked example — Maison Médicale Couleurs Santé, at 1 February 2026 — shows the
per-discipline decomposition:

| Discipline | Monthly amount per registered patient |
|---|---|
| General medicine | €20.79 |
| Nursing | €18.34 |
| Physiotherapy | €9.54 |
| **Total** | **€48.67** |

The three covered disciplines are general medicine, nursing and physiotherapy. Amounts are per centre
and per year — this one example is illustrative, not a general tariff.

Scale of the segment: roughly 250 maisons médicales with more than 600,000 registered patients, as at
2023 *(secondary source — to verify against INAMI)*.

Registrations and closures are notified to the OA through MyCareNet's medical-house service
(`MyCareNet-MHM`, "medical house subscription and closure notifications"). Do not confuse this
capitation forfait with the **home-nursing forfaits A/B/C/toilette**, which are a different mechanism
entirely — dependency-based lump sums for home nursing, requiring the OA advising physician's
agreement, carried by the `410000` message family. See [[mycarenet-services-and-flows]].

**Critical consequence for an administrative-first product:** in a forfait centre, most financial
administration — registrations, capitation reconciliation, provider remuneration, subsidies — does not
depend on act-level billing from the clinical record. That decoupling is real and is what makes the
segment addressable without replacing a clinical system.

## The DMG / GMD and its electronic form

The **DMG** (*dossier médical global* / GMD, *globaal medisch dossier*) is the arrangement by which a
patient designates one GP as holder of their consolidated record. It carries an annual fee per
patient, and it gives the patient reduced co-payments.

Key facts for software:

- Since **1 January 2021**, a GP must use a **recognised electronic medical record** to manage the DMG.
- The DMG fee is billed electronically as **eDMG** via MyCareNet; the platform publishes a
  `MyCareNet-GlobalMedicalFile` service to consult and notify DMG ownership.
- The DMG population is the denominator for premium criteria — for example, the Sumehr threshold is
  expressed as a ratio of patients with an uploaded Sumehr to patients for whom DMG fees were received.
  See [[software-homologation-and-obligations]].

So the DMG is simultaneously a clinical responsibility, a revenue line, and the measurement base for
the practice premium. It deserves to be a first-class entity in a data model.

## The practice premium as a revenue line

The *prime de pratique intégrée* pays a GP annually for using accepted software and hitting measured
e-service thresholds. 2025 amounts:

| Situation | Condition | Amount |
|---|---|---|
| 1 | Active, but no accepted software **or** below thresholds | €1,000 |
| 2 | Accepted software + 5 of 7–8 parameters | €3,500 |
| 3 | Accepted software + 6 of 7–8 parameters | €4,500 |
| 4 | Accepted software + 7+ of 7–8 parameters | €6,000 |
| — | Trainees (*médecins en formation*) using accepted software | €800 |

Medical-home GPs are measured on 7 parameters, fee-for-service GPs on 8. Applications for the 2025
premium run **28 August – 30 November 2026**, submitted through ProSanté, and payment goes to a
registered bank account in at least biannual instalments.

Why this belongs on a financial-flows page: for the practice, the premium is a predictable annual
receipt whose size is a direct function of software behaviour. For a vendor it is the clearest
quantified willingness-to-pay anchor in the market — the delta between situation 1 and situation 4 is
€5,000 per GP per year, and software is the mechanism that captures it. Full parameter list in
[[software-homologation-and-obligations]].

## Flow summary: act to cash

```
Registration / identification
  NISS → insurability (801000/801900) → route decision
        │
        ├── Cash route
        │     act → code (nomenclature, setting-aware)
        │          → eAttest, synchronous, during the visit
        │          → acknowledgement in seconds
        │          → justificative document to patient (with receipt number)
        │          → patient reimbursed by OA
        │
        └── Third-party route
              acts accumulate → invoice batch (920000, INAMI layout, record types 10–90)
                   → 931000 reception acknowledgement
                   → 920098 informational errors / 920099 rejection (blocking errors or >5% error rate)
                   → 920900 final settlement: accepted amounts and definitive rejections
                   → reconcile settlement against batch, re-invoice rejections

Forfait centres, in parallel:
  registration/closure notified to OA (410000 family / MyCareNet-MHM)
    → monthly capitation per registered patient per discipline
    → reconcile capitation receipts against the registered population
```

## Build implications

1. **Insurability is the gate, not an enrichment step.** The billing route, the applicable tariff and
   the patient's co-payment all derive from it. Cache it with an explicit validity period and
   re-check; never assume last month's answer.
2. **Version the nomenclature as reference data with effective dates.** Bill-time code resolution must
   use the code valid on the date of service, and must be setting-aware (private practice vs medical
   home). Plan for externally-imposed change deadlines.
3. **Make rejection handling a first-class workflow, not an error path.** The 5% error-rate threshold
   means one bad field pattern can reject an entire batch. Validate before submission, keep a
   per-line audit trail, and support partial re-invoicing after settlement.
4. **Model forfait registration as a lifecycle with month-boundary semantics.** Effective dates on the
   first of the following month, dependence on OA notification, and continuity of mutuality status are
   all revenue-affecting states, not attributes.
5. **Reconcile three ways.** Submitted batch, settlement file, and bank receipt. Practices lose real
   money in the gaps, which is exactly where an administrative product earns its keep.
6. **Treat the premium as a product feature.** Instrument the eight parameters and show a GP their
   live score. That turns an abstract compliance feature into a visible euro amount.
7. **Keep the DMG as an entity, not a flag.** It drives fees, premium denominators and clinical
   responsibility.

## Gaps and figures to verify

- Exact mandatory scope and start date of third-party payer for increased-intervention patients.
- Whether forfait disciplines are limited to GP/nursing/physiotherapy in all agreements, or vary.
- Current DMG annual fee amount; current MAF ceilings.
- The 250 centres / 600,000 patients figures (secondary source).
- Whether the pattern "`1098xx`/`1096xx`-style codes for medical homes vs `1028xx` for private
  practice" generalises, or whether the diabetes example is specific.
- 2026 premium amounts and whether the parameter set changed (the 2026 criteria were reported as
  unchanged by a doctors' union — unconfirmed).

Sources: [[sources]].
