---
classification: public
status: draft
updated: 2026-10-01
---

# Billing rules — physicians

**Governing texts:** art. 1 (general) · 2 (consultations, visits, opinions) · 3 (medical technical
services) · 10 (trainees) · 11 (general special services) · 12 (anaesthesiology) · 13 (resuscitation) ·
14 a–n (surgery by specialty) · 15 (surgery application rules) · 16 (operative assistance) ·
25 (surveillance of hospitalised patients) · 26 (urgency supplements) · 34 (percutaneous interventional) ·
37 (telecare). **Key letters:** N (consultations/visits/opinions), K (other technical), D (availability),
E (GP travel), A/C (surveillance of inpatients), I (percutaneous interventional), Q (accreditation
supplement).

Rule semantics and encodings: [[billing-engine-rule-model]].

## Code selection

| Determinant | Rule |
|---|---|
| **Qualification** | Decides the code, not the nature of the work. A specialist attests `102012`, never `101010` (art. 2 RI 05, abrogated 1.5.2013 but still printed — resolve by date of service) |
| **Place** | Home visit vs practice consultation per art. 2 RI 01 (see below) |
| **Ambulatory vs hospitalised** | Paired numbers; status at the moment of delivery, except labs/anatomical pathology/in-vitro nuclear medicine, which use the moment of prescription |
| **Time** | Night, weekend, holiday and evening series, per art. 26 definitions |
| **Who called whom** | For night visits, art. 2 RI 02 |

### Place of care (art. 2 RI 01) — the counter-intuitive definitions

A **home visit** is care the patient requests where they *habitually, temporarily or accidentally* reside.
This explicitly includes a **home for the elderly**, a **childcare facility**, any establishment where the
patient stays for a purpose other than medical observation or treatment, and **the public highway after
an accident**. A **practice consultation** is one the patient travels to receive — including in a clinic
or polyclinic service. Consequently, **consultations given to workers inside companies are home visits**;
if a company practice also serves outsiders, care to outsiders is a practice consultation.

Two hard exclusions:

- **No cover for visiting a hospitalised patient**, except where the nomenclature provides otherwise.
- **Home visits by specialists other than paediatricians do not exist in the nomenclature**, so no
  reimbursement in any form — confirmed by art. 2 RI 03 even where the patient became unable to travel.

### Night, weekend, holiday (art. 26)

| Term | Definition |
|---|---|
| Night | 21:00 – 08:00 |
| Weekend | **Saturday 08:00 → Monday 08:00** |
| Public holiday | **21:00 the day before → 08:00 the day after** |
| GP evening urgent visit | 18:00 – 21:00 |

Night visits (art. 2 RI 02): both practitioners called **by the patient** → `104230` for the accredited
GP, `104834` for a paediatrician, **nothing** for any other specialist. Specialist called **in
consultation by the GP** → `104230` + `103014`.

Urgent technical supplements are payable at the practice, at home **or** in hospital. For urgent
anaesthesia supplements, reference the **relative value of the service that required the anaesthesia**.

## Cumulation

| Rule | Source |
|---|---|
| Fees for an **opinion** (*avis*) may **never** be cumulated with consultation or visit fees | art. 2 RI 06 |
| Consultation + **surveillance** not permitted where the patient is convoked by an establishment physician, sent by their treating doctor, or enters urgently, **to be hospitalised** | art. 2 RI 14, cited in art. 25 |
| **Teleconsultation** not cumulable with consultation/visit/opinion the same day by the same physician | INAMI guidance |
| Consultation + **vaccination** not cumulable in the same contact | INAMI reminder |
| `109701` not cumulable with technical services the same day by the same physician | art. 2 |
| `109351` / `109410` not cumulable the same day with technical services by the same psychiatrist, **nor with other article 2 services** | art. 2 |
| Radiodiagnostic consultation reimbursable **only** if unrelated to any radiodiagnostic act, whether it precedes, accompanies or follows | art. 17 §2, art. 2 RI 07 |
| Biologist's consultation not cumulable with clinical-biology services — but a physician recognised in **both** internal medicine and clinical biology may bill `102034` plus biology acts | art. 1 §6, art. 24 §5, art. 1 RI 02 |
| `114155` not cumulable the same day with `114133` | art. 3 |
| `596083` not cumulable with `599082, 599104, 596525, 596540, 599045` by an infectiology-titled specialist **during the same hospitalisation** | art. 25 |
| `599480` not cumulable with article 14 h) services | art. 25 |
| Article 22 II services not cumulable the same day with physiotherapy services | art. 23 |

### Telecare (art. 37)

| Rule |
|---|
| `101673`, `101695`, `101710` not cumulable the same day by the same physician with `101732` |
| `106956` not cumulable with article 2 services the same day by the **same or another** neurologist or paediatrician holding the neuro title |
| `107811` not cumulable with `109410, 109351, 597741, 590391, 590450` for a **2-month period for the same patient** |
| At most **5** of `109373, 109395, 101953, 106912` per year |
| At most **4** of `109432, 109454, 106934` per year |
| A report naming participants forms part of the patient file |

## Reductions and percentages

| Mechanism | Rule |
|---|---|
| **Operative association** (art. 15 §4) | Principal act full value; second act in a **clearly distinct operative field** at **half**, written `N 600/2`. Two incisions in one field are **not** two fields (art. 15 RI 03) |
| **Partial cumulation** (art. 25) | Surveillance fees cumulable only **at 50% of their value** with technical acts by the same physician or a physician of the same speciality during one hospitalisation |
| **Supervision** (art. 1 §4ter, art. 10 §2) | Candidate specialist's services attested at **100%** (by the internship master) or **75%** (by the candidate) depending on supervision conditions |
| **Setting threshold** (art. 15 §2) | Interventions at **K 120 / N 200 / I 200 or above** must, absent force majeure, be performed in an approved hospital with at least a C or D service |

## Frequency caps

| Cap | Source |
|---|---|
| `145250-145261` provisional contention appliance: **once per case** | art. 3 |
| A service capped at **four times per nosological episode** | art. 3 |
| At most **one concertation per week** | art. 25 |
| `597645` / `597660`: once per month months 1–24, once per 3 months months 25–72, once per 6 months thereafter | art. 25 |
| `599060` geriatric discharge exam: beneficiary **75+**, hospitalised in a G(300) geriatric service | art. 25 |
| Telecare annual caps (above) | art. 37 |

## Global exclusions

Article 1 §7: **purely aesthetic interventions are not reimbursed**, and the refusal extends to
anaesthesia, assistance and hospitalisation costs — *"l'accessoire suit le principal"* (art. 1 RI 01).

Services must be attested **in the name of the provider who performed them**, provided they hold the
required qualification. A GP holding an acute-medicine brevet attests under GP-accessible codes (art. 25
interpretative rules).

## Build implications

1. **Qualification resolution precedes code selection.** Resolve the physician's registered title first;
   everything downstream depends on it.
2. **Encode the art. 2 RI 01 place taxonomy literally**, including rest homes and the public highway, and
   hard-block specialist home visits other than paediatrics.
3. **Implement art. 26 time boundaries exactly** — Saturday 08:00 and holiday-eve 21:00 are off-by-one
   magnets.
4. **Night visits need a "who called whom" field.** It changes the code and can zero the specialist's fee.
5. **Surveillance needs hospitalisation-scoped state** for both the 50% partial cumulation and the
   tiered monthly/quarterly/biannual caps.
6. **Model the candidate-specialist 75/100% split** as an attestation attribute, not a discount.
7. **Rolling-window exclusions exist** (telecare's 2 months) — your cumulation checker needs date ranges,
   not just same-day comparison.

## Gaps and figures to verify

- Full application-rule text of articles 15 and 16 (worked from interpretative rules).
- Articles 14 a–n specialty-specific rules were mined only for density, not enumerated.
- Article 11 and article 20 (internal medicine, 36 age conditions, 23 cumulation prohibitions) not
  enumerated here.
- Accreditation (Q) supplement amounts and conditions.
- Conventioned vs non-conventioned supplement rules — outside the nomenclature itself.

Sources: [[sources]].
