---
classification: public
status: draft
updated: 2026-10-01
---

# Billing rules and cumulation

The nomenclature is not a price list. It is a **rules engine**: which code applies depends on the
practitioner's qualification, the place of care, the time of day, what else was billed that day, how
long the session lasted, and whether an advising physician agreed. This page documents those rules
from the primary texts.

Everything below is from the official INAMI nomenclature articles and their *règles interprétatives*,
retrieved 1 October 2026 — see [[sources]]. Versions are stated per article because they differ.

> **This page is the primer.** It covers the cross-cutting concepts using four professions as worked
> examples. For the complete picture: [[nomenclature-map]] maps all 63 articles to professions and key
> letters; [[billing-engine-rule-model]] specifies the 19 constraint types an engine must implement; and
> there is a page per profession — [[billing-rules-physicians]], [[billing-rules-physiotherapy]],
> [[billing-rules-nursing]], [[billing-rules-dental]], [[billing-rules-midwifery]],
> [[billing-rules-speech-therapy]], [[billing-rules-labs-and-imaging]],
> [[billing-rules-devices-and-aids]].

## How a code resolves to a fee

A nomenclature line has three parts:

| Part | Example | Meaning |
|---|---|---|
| **Code** | `560011` | Six digits, identifying the service |
| **Key letter** (*lettre-clé*) | `M`, `W`, `K`, `N`, `I`, `L` | The category/scale the service belongs to |
| **Coefficient** | `24`, `0,879`, `600` | The relative weight of the service |

The fee derives from the coefficient multiplied by the monetary value of its key letter, which is
negotiated and indexed *(the exact conversion mechanism was not verified in this pass — to verify)*.

Two implementation notes that bite immediately:

- **Coefficients use a comma as decimal separator** (`W 0,879`, `M 14,5`). Any parser or import must
  handle Belgian decimal notation.
- **Key letters are not interchangeable.** `M 24` (physiotherapy) and `W 0,879` (nursing) are not
  comparable magnitudes. Store the key letter with the coefficient, always.

## Where the rules live

A layered structure, and you need all four layers to bill correctly:

| Layer | What it contains | Example |
|---|---|---|
| **Article 1** | General rules applying across the nomenclature | §7: purely aesthetic interventions are not reimbursed |
| **Discipline articles** | The codes themselves, with their own application paragraphs (§§) | Article 2 doctors · 7 physiotherapy · 8 nursing |
| **Application-rule articles** | Rules governing a whole domain | **Article 15** — surgery application rules |
| ***Règles interprétatives*** | Numbered Q&A resolving real disputed cases, published per article | Article 2 RI 01–… |

The *règles interprétatives* are the most practically valuable and the least known. They are written as
a question from the field and an authoritative answer, each carrying a *Moniteur* date and an effective
date, and some are explicitly **abrogated** while remaining in the document. A rules engine must
therefore version them and respect effective dates — article 2's RI 05, for instance, is abrogated from
1 May 2013 but still printed.

## The question everyone asks: a second service on the same day

There is **no single rule**. Each profession handles it differently, and conflating them is the most
common source of wrong assumptions. Here are the four patterns, from the primary texts.

### Pattern A — Doctors (article 2): prohibition, not reduction

Article 2 contains **no percentage reduction** for a second consultation or visit. Instead it carries
**cumulation prohibitions**:

| Rule | Source |
|---|---|
| Fees for an **opinion** (*avis*) may **never** be cumulated with fees for a consultation or a visit | Art. 2, RI 06 |
| **Teleconsultation** services may not be cumulated with consultation, visit or opinion fees by the same physician **on the same day** | INAMI teleconsultation guidance |
| A **consultation and a vaccination** may not be cumulated during the same patient contact | INAMI reminder to physicians |
| `109701` is not cumulable with technical services performed **the same day by the same physician** | Art. 2 |
| `109351` / `109410` may not be cumulated the same day with technical services by the same psychiatrist, **nor with other article 2 services** | Art. 2 |
| Radiodiagnostic consultation is reimbursable **only** if unrelated to any radiodiagnostic act, whether it precedes, accompanies or follows | Art. 17 §2, art. 2 RI 07 |
| A biologist's consultation may not be cumulated with clinical-biology services — but a doctor recognised in **both** internal medicine and clinical biology may bill consultation `102034` plus biology acts | Art. 1 §6, art. 24 §5, art. 1 RI 02 |

### Pattern B — Surgery (article 15 §4): the real 100% / 50% rule

**This is where the "second act at 50%" rule actually lives.** When several acts are performed in the
same operative session, the principal act is billed at full value and a second act **in a clearly
distinct operative field** at half.

The nomenclature expresses this as a **fraction notation**, not a percentage. From article 15 RI 02 —
an iliac endarterectomy plus a femoro-popliteal venous graft, two distinct fields:

```
237090 – 237101   Revascularisation of one abdominal artery …        N 600
235115 – 235126   Revascularisation of a limb artery by bypass …     N 600/2
```

`N 600/2` *is* the 50% rule, written as a denominator under the coefficient.

The decisive condition is **distinct operative fields**, and it is interpreted strictly. Article 15
RI 03: after surgery for a bimalleolar fracture, removing the synthesis material is reimbursable
**once only** under `280055–280066` (N 100) **even though there are two incisions** — one field, one
fee. So "two incisions" is not "two fields".

Also note article 15 §2: interventions valued at **K 120 / N 200 / I 200 or above** must, except in
force majeure, be performed in a hospital approved by the competent authority with at least a C or D
service. Value thresholds carry setting obligations.

### Pattern C — Physiotherapy (article 7): a separate, halved code, with conditions

Physiotherapy **does** reduce the second session of the day — by giving it its **own code at half the
coefficient**.

| Code | Service | Coefficient |
|---|---|---|
| `567011` / `567055` | Individual session, average personal input **30 minutes** (lead codes in the current 1.7.2026 text) | **M 24** |
| `560011` | Individual session, 30 minutes — fallback where §10 limitations block `567011` | M 24 |
| `560523` | Individual session, average personal input 15 minutes | M 12 |
| `560696` | Individual session, 15 min: **2nd session of the day** per §11 | **M 12** |
| `561396` | Same, in another setting | M 12 |
| `561433` / `561455` / `561470` | Individual session, 15 min: **2nd session of the day** per §12 — practice outside hospital / in hospital / in an organised medical service | M 12 |
| `561352` | Individual session, 20 minutes | M 16 |
| `561411` | Written report | M 14,5 |

So **M 24 → M 12 is literally 50%**. But read the descriptions before calling it a penalty: the first
session is specified at *30 minutes* of personal input and the second-of-day code at *15 minutes*. It
is half the coefficient for half the specified time — a different, shorter service, not a discount on
the same one.

*(Corrected 1 Oct 2026: an earlier draft of this page cited `560011` as the lead 30-minute code, from the
text in force since 2014. The current 1 July 2026 text leads with a `567xxx` series and keeps `560011`
as a §10-limited fallback. Detail: [[billing-rules-physiotherapy]].)*

The conditions on it are strict, and they are a workflow specification (article 7, §§11–12):

1. Unless the nomenclature or the advising physician says otherwise, a second session **may** be
   attested the same day.
2. It **may only be charged if performed at least 3 hours after the previous one**.
3. It can be justified **only if indispensable to the beneficiary's state of health**.
4. The **motivation must be kept available to the advising physician and must appear in the patient's
   file**.
5. The advising physician **may intervene at any time and refuse reimbursement** of the second session
   if unjustified, notifying a motivated decision to the beneficiary with a copy to the
   physiotherapist, **taking effect at the latest the day after notification**.

Other article 7 constraints worth knowing, as examples of the shape of these rules:

- Cerebral-palsy codes (`560755`, `560873`, `560991`, `561116`, `561212`, `564476`, `561304`) are
  restricted to patients **under 21 whose condition began before age 7**, proven by a medical report
  held for the advising physician and referenced in the file. They may be attested **once per day** and
  **not cumulated the same day** with other article 7 §1 services — **except** the "written report"
  codes (`560711`, `560836`, `560954`, `561072`, `561190`, `564454`, `561411`), with which cumulation
  **is** allowed.
- Lymphoedema drainage codes are capped at **120 sessions per calendar year, once per day**, with a
  higher-coefficient set (M 96 vs M 48) for exceptional cases showing **>30% perimetric difference**
  versus the contralateral limb — and the **combined total across both sets** may not exceed 120
  sessions per calendar year.

### Pattern D — Nursing (article 8): equal value, but a forfait may replace everything

Nursing distinguishes visits by **rank within the care day** — and does **not** reduce them:

| Code | Service | Coefficient |
|---|---|---|
| `425014` | **First** basic service of the care day | W 0,879 |
| `425036` | **Second** basic service of the care day | W 0,879 |
| `425051` | **Third or more** basic service of the care day | W 0,879 |

Same value for all three. Anyone porting an assumption from physiotherapy to nursing will get this
wrong.

The real nursing complexity is the **forfait per care day**, which replaces per-act billing for
dependent patients. It is granted **once per care day for the whole of the nursing care** given:

| Code | Forfait | Coefficient | Dependency criteria (Katz-style scoring, score 3 or 4) |
|---|---|---|---|
| `425272` | **A** | W 3,825 | Dependent for washing **and** dressing; **and** for transfer/mobility **and/or** toileting |
| `425294` | **B** | W 7,371 | Washing **and** dressing; **and** transfer/mobility **and** toileting; **and** continence **and/or** eating |
| `425316` | **C** | W 10,083 | Washing (score 4) **and** dressing (4); **and** transfer/mobility (4) **and** toileting (4); **and** continence **and** eating (one scored 4, the other at least 3) |

Palliative patients have their own set, also once per care day, requiring both the dependency criteria
**and** the palliative-patient definition in §5bis, 1°:

| Code | Forfait | Coefficient |
|---|---|---|
| `427011` | **PC** | W 14,422 |
| `427033` | **PB** | W 11,750 |
| `427055` | **PA** | *(criteria as B-level dependency)* |
| — | **PP** | once per care day |

Plus `425375` — a forfait per care day covering one or more **specific technical acts** (placing and/or
monitoring IV or subcutaneous perfusions; administering and/or monitoring parenteral nutrition) at
**W 8,934** — and supplementary honoraria per care day for certain cases.

Two article 8 interpretative rules with direct software consequences:

- **RI 01:** **No** article 8 service may be attested when delivered during a hospital's "first
  emergency care" or "specialised urgent care". And placing/monitoring an IV or subcutaneous perfusion
  may **not** be attested via article 8 when performed in a hospital, **including its consultation
  service**. Place of care invalidates the whole article, not just a code.
- **RI 02:** Preparing and administering medication for chronic psychiatric patients
  (`425736`, `425751`, `425073`) **may** be attested as delivered by a *aide-soignant* and reimbursed,
  provided the **nursing file shows each part was performed by a provider competent for it** —
  preparation is outside a care assistant's competence, administration is within it. A systematic
  refusal in that case is unjustified. **The file is the evidence that makes the claim payable.**

### Summary of the four patterns

| Profession | Second service same day | Mechanism |
|---|---|---|
| Doctors (art. 2) | Often **forbidden** | Cumulation prohibitions |
| Surgery (art. 15) | **50%** if a distinct operative field; **nothing** if the same field | Fraction notation `N x/2` |
| Physiotherapy (art. 7) | **50%** coefficient, for a shorter specified session | Dedicated code + ≥3h gap + justification |
| Nursing (art. 8) | **Full value**, ranked 1st/2nd/3rd+ | Separate equal-value codes; or absorbed by a care-day forfait |

## Place, time and qualification change the code

### Place of care

Article 2 RI 01 defines the boundary precisely, and it is not where intuition puts it:

- A **home visit** is a service the patient requests **where they habitually, temporarily or
  accidentally reside** — including a home for the elderly, a childcare facility, or any establishment
  where they stay for a purpose **other than** undergoing medical observation or treatment, and
  including **on the public highway after an accident**.
- A **consultation at the practice** is one for which **the patient travels** to receive it —
  including a consultation in a clinic or polyclinic service.
- Therefore **consultations given to workers inside companies count as home visits**.
- If a company practice is also open to non-employees, care to outsiders counts as practice
  consultations.
- There is **no reimbursement for visiting a patient staying in a hospital**, except where the
  nomenclature provides otherwise.

Two hard consequences:

- **Home visits by specialists other than paediatricians are not in the nomenclature at all**, so they
  attract no reimbursement in any form — article 2 RI 03 confirms this even for a patient who became
  unable to travel (hemiplegia) and whose ophthalmologist continued care at home.
- Physiotherapy codes differ by setting: practice **outside** a hospital, practice **inside** a
  hospital, practice in an **organised medical service**, and the **patient's home** each have their own
  code series for the same clinical act.

### Time of day

Night visits (requested and performed **between 21:00 and 08:00**) have their own codes, and which code
applies depends on **who called whom** — article 2 RI 02:

| Situation | Accredited GP | Specialist |
|---|---|---|
| Both called **by the patient** | `104230` | `104834` for a paediatrician; **no reimbursement** for any other specialist |
| Specialist called **in consultation by the GP** | `104230` | `103014` |

INAMI also publishes rules on correctly invoicing **supplements for urgent consultations and visits**.

### Qualification

Article 2 RI 05 (abrogated 1 May 2013, still printed): **the physician's qualification determines the
code, not the character of the consultation**. A specialist bills `102012`, not `101010`, even for work
that feels like general medicine.

## Other general rules

- **Article 1 §7 — purely aesthetic interventions are not reimbursed**, and the refusal extends to
  anaesthesia, assistance and the hospitalisation costs, "the accessory following the principal"
  (art. 1 RI 01).
- Nomenclature changes arrive through the *Moniteur belge* and INAMI circulars, with **effective dates
  distinct from publication dates** — a point the interpretative rules make explicit by printing both.

## Build implications

1. **Build a rules engine, not a price table.** The inputs are: code, practitioner qualification, place
   of care, date and time, patient status, what else was billed in the same day/session, session
   duration, and any advising-physician agreement. A product that only stores tariffs cannot bill
   correctly.
2. **Model the "same day" dimension explicitly, per profession.** Doctors prohibit, surgery halves,
   physiotherapy substitutes a halved code with a 3-hour gap test, nursing ranks at equal value. One
   generic "already billed today?" check is wrong for at least three of the four.
3. **Implement the 3-hour test as a hard validation**, computed from actual session timestamps, and
   capture the justification text at the point of care — not later. The advising physician can demand it.
4. **Make the patient file the billing evidence.** Article 7's second-session motivation and article 8's
   aide-soignant delegation both make reimbursement contingent on what the record shows. Structure
   those fields; don't leave them to free text.
5. **Treat place of care as a first-class billing attribute**, with its own code mapping, and encode the
   counter-intuitive cases (rest home = home visit; hospital consultation service excluded from
   article 8).
6. **Version the interpretative rules with effective and abrogation dates**, and resolve against the
   date of service.
7. **Store coefficient *and* key letter**, parse Belgian decimal commas, and never compare across key
   letters.
8. **Encode annual and per-day caps with their aggregation scope** — the lymphoedema case caps the
   *combined* total of two code sets at 120 per calendar year, which a naive per-code counter misses.
9. **Surface forfait eligibility from the dependency scoring**, since a qualifying patient's whole
   nursing day collapses into one code. Getting the Katz-style scoring wrong changes revenue
   materially, in both directions.
10. **Validate before submission.** Every rule here is a rejection waiting to happen, and eFact rejects
    an entire batch at a 5% error rate — see [[mycarenet-services-and-flows]].

## Gaps and figures to verify

- The key-letter → euro conversion mechanism, and current key-letter values.
- The exact definition of a *journée de soins* (care day) and whether it equals a calendar day.
- Full text of article 15 §§3–4 (worked from the interpretative rules, not the article text).
- Article 7 §§11 and 12 in full, and what distinguishes them (both govern a second daily session).
- The complete palliative forfait set including PP's code and coefficient, and PA's coefficient.
- Whether article 2 contains any reduced-fee mechanism for multiple patients visited at one address
  (searched; none found in the current text — worth confirming, as it is widely believed to exist).
- Dentists (article 5), medical imaging (article 17), clinical biology (article 24) — not covered here.
- Current accreditation supplements, and conventioned vs non-conventioned supplement rules.

Sources: [[sources]]. Related: [[reimbursement-and-financial-flows]] for who pays,
[[mycarenet-services-and-flows]] for how the claim travels.
