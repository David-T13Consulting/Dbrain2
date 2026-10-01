---
classification: public
status: draft
updated: 2026-10-01
---

# MyCareNet: services and message flows

MyCareNet is the platform through which a care provider exchanges administrative and financial
messages with **all** sickness funds at once. It is operated by the NIC/CIN, the sickness funds' joint
college. If you are building practice software, this is the integration that pays the bills.

Successor to **CareNet**; both names appear in live specifications, and the flat-file layouts still
refer the reader to "the CareNet documentation" for the transport segment.

## Service catalogue

### General services

| Service | What it does |
|---|---|
| **Assurabilité** | Is this patient insured, with which fund, with what entitlements and preferential statuses |
| **Member Data** | Patient administrative/billing data as the fund holds it |
| **Consultation des tarifs (eTar)** | The applicable tariff for a service and this patient |
| **Facturation Tiers Payant (eFact)** | Electronic invoicing to the fund under third-party payer |
| **eAttest** | Electronic care attestation under cash payment |
| **eAgreement** | Electronic agreement requests (e.g. physiotherapy pathways) |
| **Médico-administratif** | Chapter IV medication agreements; **eDMG** global medical file |
| **Pharmanet** | Pharmacy delivery data |
| **Soins intégrés** | Integrated-care programmes |

### Sectors with their own service variants

Dentists · hospitals · nurses · physiotherapists · laboratories · rest homes · **maisons médicales** ·
doctors · tarification offices · pharmacists · other sectors.

Insurability in particular is published per sector (*Assurabilité Médecin*, *Assurabilité
infirmier*, …) because the questions asked and entitlements returned differ by profession. Do not
assume one generic call serves every discipline in a multidisciplinary centre.

## Two generations of interface, both live

| | Legacy | Modern |
|---|---|---|
| Transport | Flat file (fixed-position records) over CareNet/MyCareNet | SOAP web services via the eHealth platform |
| Alternative | XML with published XSDs (MyCareNet only) | — |
| Published as | Per-message "brochures" with zone-level layouts | APIs on the eHealth API portal |
| Still used | Yes, notably in nursing message families | Yes, the default for new work |

Published MyCareNet SOAP services (versions as at the API-portal snapshot):

`MyCareNet-GenericInsurability` v1.1 · `MyCareNet-eAttest` v3.2 · `MyCareNet-eAgreement` v2.0/v1.1 ·
`MyCareNet-ChapterIVAgreement` v1.0 · `MyCareNet-GlobalMedicalFile` v1.1 · `MyCareNet-MemberData`
v1.0 · `MyCareNet-MHM` v1.0 (medical-house subscription and closure notifications) ·
`MyCareNet-Tarification` v1.0 · `MyCareNet-Registration` v1.0.

Adjacent, same family of problems: `MediPrima-Consult` and `MediPrima-UMA` (medical card data and
urgent medical aid, for people covered through public social assistance), plus the regional
`MyVSBNet-Insurability`, `WalCareNet-MemberData` and `IrisCareNet-MemberData`.

## The message numbering system

Once you see the pattern, the whole domain becomes readable.

| Pattern | Meaning | Examples |
|---|---|---|
| `XXX000` | Provider → OA: request or notification | `801000`, `410000`, `420000`, `430000`, `920000` |
| `XXX900` | OA → provider: positive answer, agreement or settlement | `801900`, `410900`, `420900`, `920900` |
| `XXX999` | OA → provider: refusal or non-acceptance | `410999`, `420999`, `920999` |
| `XXX9xx` | OA → provider: other messages in the family | `410908` |
| the original number, returned | **Data rejection**: your own message comes back with error codes in the error zones | `410000`, `420000`, `430000`, `801000` |
| `891000` | Generic acknowledgement | — |
| `931000` | eFact reception acknowledgement | — |

That last mechanic is worth dwelling on: **for data errors the OA echoes your message back to you
with per-field error codes filled in**, rather than sending a separate error document. The layouts
pair each data zone with an error zone — zone `300` NISS is followed by zone `3001` *code erreur*,
zone `301` fund number by `3011`, and so on. A client implementation has to be able to parse its own
outbound message shape as an inbound error carrier.

## Flow 1 — Insurability (`801000` / `801900`)

**Synchronous.** The provider sends patient identification and a period; the fund answers with the
insurability information, or returns `801000` annotated with the erroneous fields.

Transport: flat format over CareNet or MyCareNet; XML (per published XSD) over MyCareNet only.

This call is the gate for everything downstream — it decides whether you bill with eFact or eAttest,
which tariff applies, and what the patient owes. See [[reimbursement-and-financial-flows]].

## Flow 2 — Third-party-payer invoicing (eFact)

**Asynchronous**, built on INAMI's invoicing layout with record types 10–90, the same structure as
INAMI's own directives. It replaced both magnetic media and the accompanying paper documents.

```
Provider ──920000──▶ OA        submit invoicing batch
         ◀──931000── OA        reception acknowledged
         ◀──920999── OA        batch not accepted
         ◀──920098── OA        informational error report (batch continues)
         ◀──920099── OA        batch rejected: blocking errors, or error rate > 5%
         ◀──920900── OA        final file: accepted amounts and definitive rejections
```

| Message | Direction | Meaning |
|---|---|---|
| `920000` | → OA | The invoicing file |
| `931000` | ← OA | Preliminary acknowledgement of receipt |
| `920999` | ← OA | Non-acceptance of the `920000` |
| `920098` | ← OA | Informational error report |
| `920099` | ← OA | Rejection: blocking errors present, or **errors exceed 5%** of records |
| `920900` | ← OA | Final processing file: settlement and definitive rejections |

**The 5% rule is the single most operationally important number here.** A systematic field-level
defect across many lines will reject a whole batch, delaying all of its cash. Validate locally before
submitting, and treat batch composition as a risk-management decision.

## Flow 3 — eAttest (cash payment)

**Synchronous, and it happens during the visit.** The attestation must be transmitted while the
patient is there.

1. Check insurability; confirm third-party payer does *not* apply.
2. Complete the consultation.
3. Generate the attestation in the practice software.
4. Transmit to MyCareNet, which routes to the patient's fund.
5. Receive an automated acknowledgement **within seconds**.
6. The software produces the patient's justificative document, carrying the receipt number.

Resilience: a backup environment exists for platform unavailability, and **paper attestations remain
permissible when technical problems prevent electronic submission** — so the product needs a
deliberate, auditable fallback path, not an error dialog.

Rollout: GPs from 2018, dentists from 2019, specialists from 2021. Since **1 September 2025**, GPs,
specialists and dentists are obliged to invoice all compulsory-insurance services electronically.
Current service version on the platform: `MyCareNet-eAttest` v3.2.

## Flow 4 — Nursing notification families (`4xxxxx`)

These are home-nursing mechanisms, distinct from maison-médicale capitation. They matter because
nurses are often part of a multidisciplinary centre, and because they show the general notification
pattern clearly.

### Forfaits A, B, C and toilette (`410000`)

Dependency-based lump sums for home nursing, subject to the fund's advising physician
(*médecin conseil*).

| Message | Direction | Meaning |
|---|---|---|
| `410000` | → OA | New request, or closure of a forfait A/B/C/toilette |
| `410900` | ← OA | Agreement (*accord*) |
| `410999` | ← OA | Refusal (*refus*) |
| `410000` returned | ← OA | Data rejection, with error zones filled |
| `410908` | ← OA | **Sent spontaneously by the fund**: decision of the advising physician after a visit; closure of a previous agreement after modification or replacement by another provider; or rectification of a decision following a circumstantial report |

`410900` and `410999` repeat, in their first part, all the data the provider supplied in `410000` —
convenient for matching without local correlation state.

`410908` carries an explicit software obligation: the specification states the nursing software must
ensure the nurse **receives all `410908` messages** and must draw particular attention to them. This
is a documented example of a regulator specifying UI behaviour, not just data exchange. Unsolicited
inbound messages need a real inbox with escalation, not a log table.

### Palliative care (`420000`)

| Message | Direction | Meaning |
|---|---|---|
| `420000` | → OA | Notification of a request for palliative care |
| `420900` | ← OA | Agreement |
| `420999` | ← OA | Refusal |
| `420000` returned | ← OA | Data rejection |

### Specific technical services (`430000`)

Notification of a new request for *prestations techniques spécifiques*, an extension of a
previously accepted notification, or additional wound-care services.

| Message | Direction | Meaning |
|---|---|---|
| `430000` | → OA | Notification |
| `891000` | ← OA | Acknowledgement of receipt |
| `430000` returned | ← OA | Data rejection |

### `891000` — the generic acknowledgement

Issued for any message that was transmitted and accepted but **does not induce a specific response
message**. Its zone `307` names the message being acknowledged, copied from the acknowledged
message's zone 200 content. At the version documented locally it was used only in response to
`430000`.

## Flat-file anatomy

Worth understanding even when you integrate over SOAP, because the field semantics, error codes and
business rules were designed around it.

A message is three concatenated segments:

| Zones | Segment | Type | Length | OA positions | Provider positions |
|---|---|---|---|---|---|
| `1xx` | 100 — transport | A/N | 123 | 1–123 | *(not present)* |
| `2xx` | 200 — MyCareNet header | A/N | 67 | 124–190 | 1–67 |
| `3xx` | 300 — message body | A/N | 833 | 191–1024 | 68–901 |

**Segment 100 is filled by the MyCareNet platform**, so the provider never populates it. Hence two
record lengths for the same message: **1024 characters as the fund sees it, 901 as the provider
writes it** (1024 − 123 = 901). Getting this offset wrong is the classic first-integration bug.

Documentation is split across three brochures, which is why a single message is never fully specified
in one document:

- zones `1xx` → the *principes et généralités* brochure,
- zones `2xx` → *MyCareNet: description du segment 200*,
- zones `3xx` → the individual message's own brochure.

The provider may choose **XML (per published XSD)** instead of flat file.

### A real zone layout

Segment 300 of `891000`, which doubles as a tour of the standard patient-identification block:

| Zone | Field | Type | Length | OA pos. | Provider pos. |
|---|---|---|---|---|---|
| 300 | Patient NISS | n | 11 | 191–201 | 68–78 |
| 301 | Fund number (*n° mutualité*) | n | 3 | 202–204 | 79–81 |
| 302 | Patient's membership number | a/n | 13 | 205–217 | 82–94 |
| 303 | Sex | n | 1 | 218 | 95 |
| 304 | Nursing reference | a/n | 15 | 219–233 | 96–110 |
| 305 | Beneficiary surname | a | 48 | 234–281 | 111–158 |
| 306 | Beneficiary first name | a | 24 | 282–305 | 159–182 |
| 307 | Number of the acknowledged message | n | 6 | 306–311 | 183–188 |
| 308 | Reserve | a/n | 713 | 312–1024 | 189–901 |

Zones 300–304 are copied from the `430000` being acknowledged; 305–306 return the patient's identity
**as the fund knows it**, which is a useful reconciliation signal — a mismatch against your own
record is a data-quality alarm worth surfacing.

Note the scale of zone 308: 713 of 833 body characters are reserve. These layouts were designed for
decades of extension, which is also why they resist clean object mapping.

## Approved software

MyCareNet publishes, per sector and per service, the list of **approved software** (*logiciels
agréés*) — more than 30 packages for doctors, with separate certification per service (Member Data,
Chapter IV, DMG, tariff consultation, invoicing, eAttest V3, insurability). Approval is granted
service by service, not product by product. See [[vendor-landscape]].

## Build implications

1. **Implement insurability first.** It gates routing, tariffs and patient charges. Everything else
   depends on it.
2. **Build the error-echo parser early.** Your outbound message shape is also an inbound error
   carrier, with paired `XXXn` error zones. Teams that treat errors as a separate format rewrite this.
3. **Validate before submitting, because of the 5% rule.** Pre-flight validation against the layout
   and business rules is cheaper than a rejected batch and a cash delay.
4. **eAttest is a real-time, in-consultation dependency.** Seconds matter, the clinician is watching,
   and you need an auditable paper fallback. Design for the failure case explicitly.
5. **Unsolicited inbound messages need an inbox with escalation.** `410908` is specified as something
   the clinician *must receive and notice*. Generalise that: fund-initiated messages are workflow
   items, not logs.
6. **Model record length and offsets as configuration, not constants**, if you touch flat files at
   all — the 1024/901 asymmetry exists per message family.
7. **Certify per service, and sequence accordingly.** Approval is per service, so a roadmap can ship
   insurability and invoicing before Chapter IV or eAgreement.
8. **Don't conflate the two "forfaits".** Home-nursing forfaits A/B/C/toilette (`410000`, advising
   physician) and maison-médicale capitation (`MyCareNet-MHM`, registration-driven) are different
   mechanisms with different data.

## Gaps and figures to verify

- Current versions of the nursing message families. The locally-held brochures are dated 2009–2023
  (`891000` v01R00 2009, `420000` v01R02 2012, `410908` v02R01 2014, `410000` v02R02 2017,
  `430000` v01R08 2023) — **treat all layout detail above as structurally illustrative, not current**.
  Confirm against the live NIC/CIN documentation before implementing.
- Whether flat-file transport remains available for new integrations, or is accepted only for legacy.
- The `920098` numbering break from the `XXX9xx` pattern — likely a sub-series for reports.
- Full zone layouts for `801000`/`801900` and the `920000` record types 10–90 (not retrieved).
- Whether eAttest v3.2 changes any of the flow described (the flow is from the service description).
- Whether `891000` now acknowledges messages beyond `430000`.

Sources: [[sources]], including the locally-held specification archive noted there.
