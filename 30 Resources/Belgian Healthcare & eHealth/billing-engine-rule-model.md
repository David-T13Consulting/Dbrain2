---
classification: public
status: draft
updated: 2026-10-01
---

# Billing engine — rule model

A specification for encoding Belgian nomenclature rules in software. Derived from the primary legal
texts of all 63 nomenclature articles and 648 interpretative rules, mined 1 October 2026. Every
constraint type below is evidenced by a citation from the law.

Article index and profession mapping: [[nomenclature-map]].

## 1 · What a billable line actually is

```
BillableLine
  code              numéro d'ordre (6 digits) — often one of a PAIR
  key_letter        N K D E B F A C I L V M W R Z S O U Q   (art. 1 §2)
  coefficient       relative value; Belgian decimal comma  ("W 0,879")
  p_weight          dental only: coefficient de pondération P
  fee               = euro_value(key_letter) × coefficient
```

Three consequences that are easy to get wrong:

1. **The key letter is the profession selector**, not decoration. `M 24` (physio) and `W 0,879`
   (nursing) are magnitudes on different scales and are never comparable. Store the letter with the
   coefficient; never collapse to a bare number.
2. **Coefficients use a comma decimal separator.** Parse accordingly.
3. **Key-letter euro values are set by convention and vary per letter** (art. 1 §3), so they are
   reference data with effective dates, not constants.

### The paired numbers = ambulatory vs hospitalised

Most services are published as a pair (`237090 - 237101`). The selection rule, from the article 25
interpretative rules citing circular OA 84/382 of 7 December 1984:

> *"en règle générale, c'est la situation du patient au moment où la prestation est effectivement
> dispensée qui est déterminante pour le choix du numéro d'ordre; toutefois pour les prestations de
> biologie clinique, d'anatomo-pathologie ou de médecine nucléaire in vitro, le caractère « ambulant »
> ou « hospitalisé » doit être déterminé en fonction du moment de l'établissement de la prescription."*

| Rule | Encoding |
|---|---|
| Default: patient's status **at the moment of delivery** | `pair_selector: delivery_time_status` |
| Clinical biology, anatomical pathology, in-vitro nuclear medicine: status **at the moment the prescription was established** | `pair_selector: prescription_time_status` |
| Hospitalised status begins at the **admission date and time on the hospitalisation notification document** | authoritative timestamp, not a clinical judgement |
| Emergency analyses may use ambulatory numbers **if results are known before admission and contributed to the admission decision** — but this must not be systematic for patients clearly requiring admission | a justified exception flag, auditable |
| Patient admitted, examined, then transferred to another hospital: the first hospital's analyses use **hospitalised** codes | |

## 2 · The constraint taxonomy

Nineteen types cover what the texts actually contain.

### T1 · Qualification gate

The provider's recognised title determines which code may be used — *not* the character of the work.
Article 2 RI 05: a specialist attests `102012`, never `101010`, even for general-feeling work. Article 25
RI: services are attested in the name of the provider who performed them, provided they hold the
required qualification; a GP holding an acute-medicine brevet attests under GP-accessible codes.

```yaml
- type: qualification_gate
  codes: [102012]
  requires_title: [medecin_specialiste]
  forbids_title: [medecin_generaliste]
```

### T2 · Supervision percentage

Article 1 §4ter and article 10 §2: services performed by a **candidate specialist** are attested at
**100% (by the internship master) or 75% (by the candidate specialist)** depending on the supervision
conditions.

```yaml
- type: supervision_percentage
  when: provider_is_candidate_specialist
  options: [{attested_by: master, pct: 100}, {attested_by: candidate, pct: 75}]
```

### T3 · Place of care

Article 2 RI 01 draws the boundary counter-intuitively and precisely: a **home visit** is care where the
patient habitually, temporarily **or accidentally** resides — including a rest home, a childcare
facility, any establishment where they stay for a purpose other than medical observation or treatment,
and **the public highway after an accident**. A **practice consultation** is one the patient travels to —
including a clinic or polyclinic. Therefore **care given to workers inside companies is a home visit**.
There is no cover for visiting a hospitalised patient except where the nomenclature says so, and
specialist home visits other than paediatrics do not exist in the nomenclature at all (RI 03).

Article 8 RI 01 shows place can invalidate an **entire article**: no article 8 nursing service may be
attested during a hospital's first-emergency or specialised-urgent care, and perfusions may not be
attested via article 8 in a hospital **including its consultation service**.

```yaml
- type: place_condition
  place_enum: [home, practice, practice_in_hospital, organised_medical_service,
               hospital_inpatient, hospital_consultation, public_highway, rest_home]
  effect: selects_code | forbids_article | forbids_code
```

### T4 · Time of day and calendar

Article 26 supplies exact definitions — implement these verbatim:

| Term | Definition (art. 26) |
|---|---|
| **Night** | 21:00 – 08:00 |
| **Weekend** | **Saturday 08:00 → Monday 08:00** |
| **Public holiday** | **21:00 the day before → 08:00 the day after** |
| GP evening urgent visit | 18:00 – 21:00 |
| Dental weekend/holiday/guard consultation | between 08:00 and 21:00 |

Article 2 RI 02 adds that for night visits the applicable code depends on **who called whom**: both
called by the patient → `104230` GP, `104834` paediatrician, nothing for other specialists; specialist
called in consultation by the GP → `104230` + `103014`.

Urgent-technical-service supplements are payable whether the act happened at the practice, at home or in
hospital. For urgent anaesthesia supplements, the reference is the **relative value of the service that
required the anaesthesia**.

### T5 · Cumulation prohibition

The most common rule in the corpus. Scope varies and must be modelled explicitly.

| Scope | Example |
|---|---|
| Same **day**, same provider | `109701` not cumulable with technical services the same day by the same physician (art. 2) |
| Same day, **any** provider of a speciality | `106956` not cumulable with article 2 services the same day by the same **or another** neurologist/paediatrician with the neuro title (art. 37) |
| **Never** | *Avis* fees may never be cumulated with consultation or visit fees (art. 2 RI 06) |
| Same **session** | Art. 15 field rules |
| Same **hospitalisation** | `596083` not cumulable with `599082, 599104, 596525, 596540, 599045` by an infectiology-titled specialist during the same hospitalisation (art. 25) |
| **Rolling window** | `107811` not cumulable with `109410, 109351, 597741, 590391, 590450` for **2 months** for the same patient (art. 37) |
| Across **articles** | Article 22 II services not cumulable the same day with physiotherapy services (art. 23); `599480` not cumulable with article 14 h) services (art. 25) |
| Within a **set**, mutually | `541531-541542, 542113-542124, 542135-542146` "ne sont pas cumulables entre elles" (art. 24) |

```yaml
- type: cumul_forbidden
  codes: [107811]
  against: [109410, 109351, 597741, 590391, 590450]
  scope: rolling_window
  window: P2M
  same_patient: true
```

### T6 · Cumulation whitelist

The inverse: a code may be cumulated **only** with an enumerated set. Article 5: `371254-371265` may be
cumulated only with a semestrial buccal examination, consultation `371114-371125` or `371033-371044`, and
radiographs — **and only when performed by a candidate-dentist specialist in periodontology or a holder
of the title**. Note the compound condition: whitelist **plus** qualification.

```yaml
- type: cumul_whitelist
  code: 371254
  allowed_with: [371114, 371033, "radiographies/*"]
  additional_condition: {requires_title: [parodontologie]}
```

### T7 · Partial cumulation at a percentage

Article 25: surveillance fees *"ne peuvent être cumulés qu'à 50 % de leur valeur avec les honoraires pour
actes techniques effectués par le même médecin ou par un médecin appartenant à la même spécialité pendant
une même période d'hospitalisation."*

Not a prohibition and not a code substitution — the **same code at half value**, conditioned on same
physician *or same speciality*, within one hospitalisation.

### T8 · Fraction on association (operative fields)

Article 15 §4: in one operative session, the principal act at full value and a second act **in a clearly
distinct operative field** at half, written as fraction notation:

```
237090 – 237101   Revascularisation, one abdominal artery     N 600
235115 – 235126   Revascularisation, limb artery by bypass    N 600/2
```

Strictly interpreted. Article 15 RI 03: after bimalleolar fracture surgery, removing synthesis material
is reimbursable **once** under `280055–280066` **despite two incisions** — one field, one fee. Two
incisions are not two fields.

Article 15 §2 adds a value→setting obligation: interventions at **K 120 / N 200 / I 200 or above** must,
except in force majeure, be performed in an approved hospital with at least a C or D service.

### T9 · Code substitution at a reduced coefficient

Distinct from T7 and T8: a **different code** exists for the repeat event, at a lower coefficient.
Article 7 physiotherapy: first individual session `560011` **M 24** (30 minutes) vs second session of the
day `560696` / `561433` **M 12** (15 minutes). Half the coefficient for half the specified time.

### T10 · Minimum interval

Article 7 §§11–12: a second daily physiotherapy session *"ne peut être porté en compte que si elle a été
effectuée au minimum 3 heures après la précédente."*

```yaml
- type: min_interval
  between: [first_session_of_day, second_session_of_day]
  interval: PT3H
  source_timestamp: actual_session_time   # not scheduled time
```

### T11 · Duration-determined code

The code follows measured duration, not intent. Physiotherapy publishes 15 / 20 / 30-minute variants;
article 23 states a service is *"attestée sous le numéro d'ordre qui correspond à la durée effective"*;
speech therapy has ≥30 and ≥60-minute sessions, and **no 60-minute session is reimbursable for a
beneficiary under 10**, whatever the disorder (art. 36).

### T12 · Frequency cap — with scope and window

The richest dimension. Observed scopes, all from primary texts:

| Scope | Example |
|---|---|
| per day | cerebral-palsy physio codes, once per day (art. 7) |
| per **care day** (*journée de soins*) | nursing forfaits, once per care day for all care (art. 8) |
| per week | max one concertation per week (art. 25) |
| per month | max 5 school speech sessions per calendar month (art. 36) |
| per **calendar year** | lymphoedema 120 sessions/year; dental `377230-377241` once per calendar year |
| per **pregnancy** | midwife prenatal codes max **12 times per pregnancy** (art. 9) |
| per **tooth** | fissure sealing due once per tooth; `374356-374360` once per tooth (art. 5) |
| per **quadrant** | dental quadrant aggregation (art. 5) |
| per **case** | `145250-145261` once per case (art. 3) |
| per **nosological episode** | max four times per *épisode nosologique* (art. 3) |
| per **insured, lifetime** | series `558994` only once per insured (art. 23) |
| per hospitalisation | art. 25 |
| per year **per centre** | audiology forfait once per year per beneficiary **per audio centre** (art. 31) |
| per **disorder treated** | max 5 times per *trouble traité* (art. 36) |
| per eye / ear / orbit | artificial eye renewals, by age band (art. 30) |
| **capped count within a duration** | `558095-558106`, `558132-558143` max **60 times over a maximum of six months** (art. 23) |
| **time-tiered** | `597645`/`597660` once per month from month 1–24, once per 3 months from 25–72, once per 6 months thereafter (art. 25) |
| per **7 calendar days**, per patient **and** per provider | dental `379411-379422`, `379433-379444`, `309411-309422`, `309433-309444` (art. 6) |
| per **provider per calendar month** | dental `379411-379422` / `309411-309422` max **20 per month** (art. 6) |
| per **provider per day**, conditional on context | on approved guard-service days, dental `379433-379444` / `309433-309444` max **20 per day** (art. 6) |
| per **prescription** | an imaging fee payable *"qu'une fois par prescription quel que soit le nombre de prestations pratiquées"* (art. 17) |
| per **rolling 24 hours** | an imaging fee *"payable au maximum une fois par 24 heures"* — not a calendar day (art. 17) |
| per **device** | prosthetic accessories `677773-677784`, `677795-677806`, `677810-677821` once **per prosthesis** (art. 28/1) |
| per **supplier per year** | audiology forfait once per year per beneficiary **per audio centre** (art. 31) |
| per **anatomical side** | audiology complementary interventions **per fitted ear**; optics per eye and per orbit |

```yaml
- type: frequency_cap
  codes: [422030, 428094, 428116, 428750, 422052, 428131, 428153, 428772]
  max: 12
  scope: per_pregnancy
```

The time-tiered case is the one that breaks naive counters:

```yaml
- type: frequency_cap_tiered
  codes: [597645, 597660]
  tiers:
    - {from_month: 1,  to_month: 24, every: P1M, max: 1}
    - {from_month: 25, to_month: 72, every: P3M, max: 1}
    - {from_month: 73, to_month: null, every: P6M, max: 1}
  anchor: hospitalisation_start
```

### T13 · Set cardinality

Article 24 is built on this: *"Au maximum trois des prestations 540013-540024, 541693-541704,
541715-541726, 541774-541785, 542172-542183, 542334-542345 et 542356-542360 peuvent être portées en
compte."* Also *"Au maximum deux…"*, *"Au maximum 2…"*. With 134 cumulation prohibitions, article 24 is
effectively a large constraint-satisfaction problem.

```yaml
- type: set_cardinality
  max: 3
  set: [540013, 541693, 541715, 541774, 542172, 542334, 542356]
```

### T14 · Prior agreement, notification and retroactivity

Speech therapy (art. 36) is the clearest worked example of a full agreement regime:

- The request, on a Comité-approved form, must be submitted **without delay** by the therapist to the
  **médecin-conseil** of the beneficiary's fund.
- **Reimbursement is refused for any assessment or treatment session performed more than 60 calendar
  days before the médecin-conseil received the request.** A hard retroactivity limit.
- Extension requires the médecin-conseil to hold a **valid notification**; the same 60-day rule applies
  to extension notifications.
- An agreement *"ne peut porter que sur un traitement de deux ans au maximum"*; specific disorder
  categories have their own session allowances (e.g. up to 55 individual treatment sessions).
- Age interacts: for beneficiaries aged 0–2 completed, a single agreement may run to the eve of the third
  birthday; for 3–19, treatment may be extended at most eight times when it began before the third
  birthday.
- A copy of the medical prescription and the request form are attached **electronically via eAgreement**
  at each treatment start.

Article 23 requires the treating physician to send the médecin-conseil a standard notification form
carrying the **affection code from a limitative list**, plus the start date.

```yaml
- type: prior_agreement
  authority: medecin_conseil
  channel: eAgreement
  retroactivity_limit: P60D        # sessions before this are refused
  max_agreement_duration: P2Y
```

### T15 · Prescription requirement

Physiotherapy, speech therapy, opticians, audiologists and device suppliers are prescription-driven.
Specificity matters: for opticians the medical prescription *"mentionne au moins la puissance de la
correction et, si nécessaire l'affection des yeux"*, on a model fixed by the Comité de l'assurance.
Speech therapy requires a prescriber drawn from a table in the article, and (per an earlier provision) a
prescriber holding an **active INAMI number**.

### T16 · Documentation as a condition of payment

Not administrative hygiene — a payment condition.

| Requirement | Source |
|---|---|
| Motivation for a second daily physio session kept available to the médecin-conseil **and recorded in the patient file**; the médecin-conseil may refuse reimbursement, with effect at the latest the day after notification | art. 7 §§11–12 |
| Nursing file must show that **each part** of a delegated service was performed by a provider competent for it; a systematic refusal is unjustified when it does | art. 8 RI 02 |
| Midwife must **motivate extra care in the beneficiary's file**, and supply the motivation to the médecin-conseil and/or treating physician on request | art. 9 |
| Report naming participants forms part of the patient file (telecare concertation) | art. 37 |
| Register per calendar year, available to the médecin-conseil, the SECM medical inspector and peer-review bodies | art. 23 |
| Proof of diagnostic/perimetric/volumetric criteria held for the médecin-conseil and referenced in the file | art. 7 |

### Also: clinical thresholds as billing conditions

Eligibility is sometimes a measurement. Nursing forfaits turn on dependency scores of 3 or 4 across
washing, dressing, transfer/mobility, toileting, continence and eating (art. 8). Higher-coefficient
lymphoedema codes require **>30% perimetric difference** versus the contralateral limb (art. 7).
Audiology uses dB signal-to-noise and SRT intelligibility thresholds (art. 31). These belong in the
clinical record and feed the billing decision — a genuine integration point, not a billing-only field.

### T17 · Anatomical-position exclusivity

Two services may be individually legal yet mutually exclusive **at the same anatomical site**.

| Rule | Source |
|---|---|
| Bridge codes `302654-302665`, `302676-302680`, `302691-302702`, `302713-302724` may not be cumulated **at the same location** with crown codes `302735-302746`, `302750-302761` | art. 6 |
| `425375`, `425773`, `426171`, `429155`, `430393` are cumulable with `423113`, `423312`, … **only when the injection sites differ** | art. 8 |

```yaml
- type: position_exclusivity
  set_a: [302654, 302676, 302691, 302713]
  set_b: [302735, 302750]
  scope: same_location          # tooth / site / quadrant / injection site
```

Claim lines therefore need **anatomical sub-identity**: tooth number, quadrant, site, side. Without it
these rules are unevaluable, and so are the per-tooth and per-ear caps in T12.

### T18 · Milestone percentage (staged payment)

Distinct from every other percentage: payment tied to **treatment progress**, not to association,
repetition or supervision. Dental prosthetics (art. 6):

- **50%** where the occlusion has been determined and the prosthesis is at the **trial stage**;
- **50%** of the insurance intervention for `309610-309621` … `302750-302761`, **after the definitive
  impressions**.

```yaml
- type: milestone_percentage
  codes: [309610, 309632, 302654, 302735]
  milestones:
    - {state: trial_stage_occlusion_determined, pct: 50}
    - {state: definitive_impressions_taken,     pct: 50}
```

This needs a **treatment-stage state machine** per prosthetic case, not a single billable event.

### T19 · Classification-driven agreement

Whether prior agreement is needed can depend on the **classification of the device or the beneficiary**,
not on the service code alone. Article 28/1:

| Device class | Prior agreement |
|---|---|
| Passive, transfer, evaluation prosthesis; definitive prosthesis **without** mechatronic knee | **Not** required |
| Definitive prosthesis **with** mechatronic knee (`675356-675360`, `675371-675382`, `675393-675404`, `675511-675522`, `675533-675544`, `675555-675566`) | **Required before delivery** |

Beneficiaries are also assigned to **groups** (3, 4, 5 …, defined at A.5.2.), and all elements leading to
the group choice must be held available to the médecin-conseil. So the classification is itself an
auditable artefact.

### And one global exclusion

Article 1 §7: purely aesthetic interventions are not reimbursed, and the refusal extends to anaesthesia,
assistance and hospitalisation costs — *"l'accessoire suit le principal"* (art. 1 RI 01).

## 3 · Evaluation order

Order matters: later stages depend on earlier selections.

```
 1. Eligibility          insurability, entitlement status, third-party-payer route
 2. Qualification        provider title vs code (T1); supervision percentage (T2)
 3. Code selection       place (T3) · time (T4) · duration (T11) · pair: ambulatory
                         vs hospitalised (§1) · setting-specific series
 4. Preconditions        prescription present and sufficient (T15); prior agreement
                         valid and within retroactivity limit (T14); sequencing
                         predecessors satisfied; clinical thresholds met
 5. Exclusions           purpose-based (aesthetic), article-level place bans
 6. Cumulation           prohibitions (T5) · whitelists (T6) · set mutual exclusion
 7. Counting             frequency caps by scope and window (T12) · set
                         cardinality (T13) · minimum intervals (T10)
 8. Valuation            coefficient × key-letter value; fraction on association
                         (T8); partial cumulation percentage (T7); substituted
                         reduced code (T9)
 9. Supplements          urgency by time definitions (T4); accreditation Q
10. Assertions           documentation present (T16); write the audit trail
11. Submission           validate, then batch — eFact rejects at a 5% error rate
```

Stages 6 and 7 need the patient's **billing history**, not just the current encounter: same day, same
session, same hospitalisation, rolling windows, per-pregnancy, per-tooth, lifetime. A line is not
billable in isolation.

## 4 · Data model implications

| Requirement | Why |
|---|---|
| Every rule **versioned with effective and abrogation dates** | Texts print abrogated rules (art. 2 RI 05, abrogated 1 May 2013, still published). Resolve against the **date of service** |
| Reference data as dated datasets, not config | Nomenclature, key-letter values, limitative affection lists |
| Billing history queryable by **many scopes** | day, care day, session, hospitalisation, pregnancy, tooth, quadrant, eye, ear, episode, calendar year, lifetime |
| Anatomical sub-identity on lines | per-tooth, per-quadrant, per-eye, per-ear, per-site caps and T17 position exclusivity are unrepresentable otherwise |
| Device identity with a lifetime | per-prosthesis caps and renewal intervals (T12, art. 28/1, art. 30) |
| Treatment-stage state machine | milestone percentages (T18) |
| Supplier dimension on counters | "per audio centre per year" (art. 31) |
| Real timestamps, not scheduled ones | the 3-hour interval test |
| Structured justification fields | T16 makes prose a payment condition |
| Agreement state machine | requested / granted / extended / expired, with retroactivity windows |
| Provider identity resolved to **title**, with check digits | moduli 97, 83, 79 and 89 — see [[identity-access-and-consent]] |

## 5 · Test cases worth writing first

1. Specialist bills `101010` → must fail (T1).
2. Second physio session 2h55m after the first → must fail; at 3h01m with motivation → pass (T10, T16).
3. Nursing 1st/2nd/3rd visit in a care day → three distinct codes, **equal** value, no reduction.
4. Patient on nursing forfait C → per-act lines suppressed; one care-day forfait.
5. Two surgical acts, same field → one fee. Distinct fields → full + half (T8).
6. Surveillance + technical act by same speciality in one hospitalisation → surveillance at 50% (T7).
7. Lab prescribed pre-admission, resulted pre-admission, contributed to admission → ambulatory code.
8. Same lab prescribed post-admission → hospitalised code.
9. Speech session 61 days before the médecin-conseil received the request → refused (T14).
10. 60-minute speech session for a 9-year-old → refused (T11).
11. Midwife's 13th prenatal session in one pregnancy → refused (T12).
12. Fissure sealing on an already-sealed tooth → refused (per-tooth cap).
13. Four of a 3-max article 24 set → one must drop (T13).
14. Visit on Saturday 07:30 → **not** weekend; 08:30 → weekend (T4).
15. Visit the evening before a public holiday at 21:30 → holiday rate (T4).
16. GP visit in a rest home → **home visit**, not practice consultation (T3).
17. Ophthalmologist home visit → no cover at all (T3).
18. Aesthetic procedure → whole claim including anaesthesia refused.

## 6 · What should not be automated

Three things in this corpus are judgement, and an engine should prompt rather than decide:

- **"Indispensable to the patient's state of health"** (second physio session). The system captures the
  clinician's reasoning; it does not generate it.
- **Distinct operative fields.** A clinical determination the interpretative rules show to be contested.
- **Whether an emergency analysis "contributed to the admission decision."** Explicitly not a systematic
  rule.

Encode these as **required human attestations with structured capture and full audit**, and surface the
rule text at the point of decision. That is also the defensible posture if the médecin-conseil or the
SECM asks later.

## Gaps and figures to verify

- Euro value of every key letter, and its indexation mechanism.
- Whether an official machine-readable rule set exists (none found; NomenSoft offers reference tables,
  not rule logic).
- Full application-rule paragraphs of articles 15 and 16 (worked partly from interpretative rules).
- Articles 27, 28 §1–7, 28 §8, 29, 35, 35bis: versions retrieved are dated 2012–2014 — re-check.
- Whether `P` (dental weighting) affects reimbursement or only statistics.
- Interaction with the capitation (*forfait*) model, where per-act billing is replaced entirely — see
  [[reimbursement-and-financial-flows]].

Sources: [[sources]]. Message transport: [[mycarenet-services-and-flows]].
Cross-cutting concepts: [[billing-rules-and-cumulation]].
