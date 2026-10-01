---
classification: public
status: draft
updated: 2026-10-01
---

# Billing rules — dental

**Governing texts:** art. 4 (qualifications) · art. 5 (prestations) · art. 6 (**règles d'application**),
all in force 1 June 2026. **Key letters: L** (dental technical services) and **N** (consultations/visits),
plus **P**, a *coefficient de pondération* attributed by AR 2.6.2015 *(its exact function — to verify)*.
50 interpretative rules across articles 5–6.

Rule semantics: [[billing-engine-rule-model]].

## Age is the dominant axis

Dental is the most age-conditioned article in the nomenclature — 89 age expressions in article 5 alone.
Whole sections are structured as *"PRESTATIONS JUSQU'AU 19e ANNIVERSAIRE"*, with parallel code series for
adults.

| Threshold | Effect |
|---|---|
| **Up to the 19th birthday** | Dedicated code series across consultations, conservative care, extractions, sealing, radiology |
| Panoramic radiograph `377296-377300` | **From the 7th to the 19th birthday** |
| Removable prostheses up to the 19th birthday | Only grantable by the **Conseil technique dentaire** on stated conditions |
| Teeth lost / dental anomalies after chemotherapy or radiotherapy **before the 12th birthday** | Specific entitlement route |
| Adhesive bridges, target group A.1.d | Beneficiaries **under 19** |
| **From the 50th birthday** | Certain interventions reimbursable only from this age |

A billing engine must resolve age **at the date of service**, and handle "up to the Nth birthday" as
strictly before that date.

## Anatomical scope: tooth, quadrant, location

Dental introduces scope dimensions no other article uses as heavily.

| Rule | Source |
|---|---|
| Insurance intervention for **fissure and pit sealing** is due **once per tooth** | art. 5 |
| `374356-374360` may be performed **only once per tooth**, so the intervention is due once per tooth | art. 5 |
| Where several **quadrants** do not each contain three teeth and/or implants, they **may be combined and attested as a single quadrant** under `371770-371781`, `372433-372444`, `372234-372245` or `372632-372643` | art. 5 |
| **Bridge** codes `302654-302665`, `302676-302680`, `302691-302702`, `302713-302724` may **not** be cumulated **at the same location** with **crown** codes `302735-302746`, `302750-302761` | art. 6 |
| Sealing another definitive tooth in the **same session and same quadrant** has its own "per additional tooth" codes (`372536-372540`, `372470-372481`) | art. 5 |

So lines need **anatomical sub-identity** — tooth number, quadrant, location — or these rules cannot be
evaluated at all.

## Frequency caps

| Cap | Codes |
|---|---|
| **Once per 7 calendar days**, per patient **and** per provider | `379411-379422`, `379433-379444`, `309411-309422`, `309433-309444` |
| Max **20 times per calendar month** per provider | `379411-379422` and/or `309411-309422` |
| On days worked in an **approved organised guard service**: max **20 times per day** | `379433-379444` and/or `309433-309444` |
| **Once per calendar year** | `377230-377241` |
| Once per tooth | sealing codes (above) |

Note the two distinct denominators: *per patient per provider* for the 7-day rule, versus *per provider*
for the monthly and daily volume caps.

## Cumulation

| Rule | Source |
|---|---|
| `371254-371265` may be cumulated **only** with a semestrial buccal examination, consultation `371114-371125` or `371033-371044`, and radiographs — **and only when performed by a candidate-dentist specialist in periodontology or a holder of that title** | art. 5 |
| `371276-371280`, `371291-371302`, `371313-371324`, `371335-371346`, `371350-371361` may be cumulated **only** with radiographs and a scaling service (`372153-372164`, `372175-372186`, …) | art. 5 |
| `371372-371383` may be cumulated **only with radiographs** | art. 5 |
| `377230-377241`, `307230-307241`, `307252-307263` **not** cumulable with the radiology services of **articles 5, 17 and 17ter** | art. 6 |
| `377112-377123`, `377134-377145` **not** cumulable with `455630-455641` | art. 6 |
| Bridge/crown same-location exclusion (above) | art. 6 |

Dental is where the **whitelist** pattern dominates: rather than listing what is forbidden, the text
states the only permitted companions. Encode as an allow-list with a compound qualification condition.

## Milestone percentages — staged payment

Prosthetic work pays in stages, expressed as percentages of the insurance intervention:

- **50%** if, in addition, the occlusion has been determined and the prosthesis is at the **trial stage**;
- **50%** of the insurance intervention for `309610-309621`, `309632-309643`, `309654-309665`,
  `309676-309680`, `309691-309702`, `309713-309724`, `302654-302665`, `302676-302680`, `302691-302702`,
  `302713-302724`, `302735-302746`, `302750-302761`, **after the definitive impressions**.

This is a distinct rule type from every other reduction in the nomenclature: payment tied to **treatment
progress milestones**, not to association, repetition or supervision.

## Time of day

| Code | Condition |
|---|---|
| `371055-371066`, `301055-301066` | Consultation on a **Saturday, Sunday, public holiday, or during an organised guard service on a bridging day**, **between 08:00 and 21:00** |
| Urgency supplement | Payable **only** where the patient's condition requires the care or consultation to be performed urgently during the stated hours and days (art. 6) |

Note dental's window (08:00–21:00) is the inverse of the physicians' night definition — do not reuse one
for the other.

## Documentation as a payment condition

| Requirement | Source |
|---|---|
| Data kept by the practitioner **in the patient file**, claimable for consultation by the médecin-conseil | art. 6 |
| Except for single-rooted milk teeth, the practitioner **demonstrates by radiograph**, kept in the patient file and claimable by the médecin-conseil | art. 6 |
| **Justification for using amalgam** kept in the patient file, claimable by the médecin-conseil | art. 6 |
| *Compte rendu* claimable for consultation by the médecin-conseil | art. 6 |

## Build implications

1. **Lines need anatomical sub-identity** — tooth, quadrant, location. Without it, per-tooth caps,
   quadrant aggregation and the bridge/crown exclusion are unimplementable.
2. **Implement quadrant aggregation as a derivation**, not data entry: detect quadrants with fewer than
   three teeth/implants and emit the combined code.
3. **Age resolution at date of service**, with "up to the Nth birthday" as strictly before.
4. **Whitelist-first cumulation model** for dental, with compound qualification conditions attached.
5. **Model prosthetic treatment as a staged workflow** with milestone-triggered partial claims.
6. **Two cap denominators**: per patient per provider, and per provider per period. Both need counters.
7. **Dental's own time window** (08:00–21:00 weekend/holiday) is separate reference data.
8. **Radiograph retention is a billing artefact**, not just a clinical one — link images to claim lines.

## Gaps and figures to verify

- The function of the **P** weighting coefficient.
- Article 4's qualification definitions and which titles unlock which code series.
- The full conservative-care, prosthetic and orthodontic code structures (not enumerated).
- Orthodontics specifically, including its agreement regime.
- The *Conseil technique dentaire* route for prostheses under 19.
- Whether the oral-hygienist codes (`372470-372481`) carry their own qualification gate.

Sources: [[sources]].
