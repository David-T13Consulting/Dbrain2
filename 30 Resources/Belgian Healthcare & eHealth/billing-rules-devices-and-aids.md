---
classification: public
status: draft
updated: 2026-10-01
---

# Billing rules — devices, aids and implants

**Governing texts:** art. 27 (bandagistes) · 27/1 (technologues orthopédiques — bandagisterie et
orthésiologie, 1.7.2025) · 28 §1–7 (fournisseurs d'implants) · 28 §8 (bandagistes — aides à la mobilité) ·
28/1 (technologues orthopédiques — prothésiologie, 1.7.2026) · 29 (orthopédistes) · 29/1 (technologues
orthopédiques — technologie de la chaussure, 1.7.2025) · 30 (opticiens, 1.5.2024) · 31 (audiciens,
1.8.2026) · 35 and 35bis (implants).
**Key letters: O** (orthopedic technologists), **U** (implant suppliers), **Z** (opticians),
**S** (audiologists).

> **Version warning.** For articles **27, 28 §1–7, 28 §8, 29, 35 and 35bis** the INAMI page offered no
> open-ended "current" PDF, so dated versions were retrieved — some from **2012–2014**. Everything below
> drawn from those six must be re-checked before implementation. Articles 27/1, 28/1, 29/1, 30 and 31 are
> current.

Rule semantics: [[billing-engine-rule-model]].

## What makes this domain different

These are **delivered goods**, not acts. So the rules are about entitlement, prescription, renewal
intervals and device identity rather than sessions and cumulation — though article 28 §8 alone carries
**77 cumulation prohibitions** and **32 explicit allowances**.

Three scopes appear here and nowhere else:

| Scope | Example |
|---|---|
| **Per device** | `677773-677784` torsion adaptor *"ne peut être tarifée qu'une seule fois par prothèse"*; same for `677795-677806` (rotation adaptor) and `677810-677821` (shock absorber) |
| **Per anatomical side** | Audiology complementary interventions **per fitted ear**; optics per eye/orbit |
| **Per supplier, per year** | Audiology forfait once per year per beneficiary **per audio centre** |

Coefficients here are large and carry decimal commas: `O 498,11`, `O 741,67`, `O 864,21`.

## Prescription is the gate

Article 30 (opticians) is the most prescription-driven article in the nomenclature — 54 prescription
conditions.

| Rule | Source |
|---|---|
| The medical prescription *"mentionne au moins la puissance de la correction et, si nécessaire l'affection des yeux"* | art. 30 |
| The prescription must use **the model fixed by the Comité de l'assurance** | art. 30 |
| Prosthetics: for groups 4 and 5, the evaluation is performed by the provider **in concertation with the prescribing specialist, who co-signs** the form *"Prescription médicale d'une prothèse du membre…"* | art. 28/1 |
| The regulatory document is **annexe 21bis of the Règlement of 28 July 2003**, comprising **the medical prescription and the evaluation attestation**; the provider completes the evaluation attestation | art. 28/1 |
| **No medical prescription is required** for an enumerated set — `677891-677902`, `677913-677924`, `677935-677946`, `677950-677961`, `675894-675905`, the annual `676535-676546` (stump socks), and services under A.1.1. 9°, A.1.3. 14°, A.1.4. 11° | art. 28/1 |

That last row matters: prescription-required is **not** a blanket rule even within one article. Model it
per code.

## Prior agreement depends on device classification

Article 28/1 shows a classification-driven agreement regime:

| Device | Prior agreement |
|---|---|
| Passive prosthesis, transfer prosthesis, evaluation prosthesis, and **definitive prosthesis without a mechatronic knee** | **No** prior médecin-conseil agreement required |
| **Definitive prosthesis with a mechatronic knee joint** — `675356-675360`, `675371-675382`, `675393-675404`, `675511-675522`, `675533-675544`, `675555-675566` | **Subject to médecin-conseil agreement before delivery** |

Beneficiaries are assigned to **groups** (3, 4, 5 and others, defined at A.5.2.), and *"tous les éléments
qui ont conduit au choix du groupe doivent être tenus à la disposition du médecin-conseil pour
information"* — the group classification itself is auditable.

## Renewal intervals and age bands

### Optics (art. 30)

| Rule |
|---|
| Each beneficiary **under 18** is entitled to a lump-sum frame intervention **at most twice** |
| A plastic artificial eye or a non-optical scleral contact lens may be renewed **at most twice a year** for beneficiaries **up to the 4th birthday** at the moment of renewal (longer intervals apply above that age) |
| The **orbit moulding** for those items follows the same renewal schedule |
| Mineral spectacle lenses with a high refractive index have an index of **at least 1.7**, except mineral bifocals with high index for beneficiaries **from the 65th birthday** |
| Supplements exist as their own groups — e.g. cylinders above 6.00 dioptres (`741635` Z 91, `741996` Z 25), prismatic lenses (`741650`, `742011` Z 21) |

### Audiology (art. 31)

| Rule |
|---|
| The lump-sum intervention *"ne peut être accordée qu'une seule fois par an, par bénéficiaire dans chaque centre auditif sollicité"* — **once a year per beneficiary per audio centre** |
| Appliance codes are **age-banded**: `679151-679162` monophonic for beneficiaries **under 18**; `705515-705526` for **18 to under 65**; `705530-705541` for **65+** — all S 416 |
| Complementary interventions **per fitted ear**: `705633-705644` bone conduction without bone anchoring (S 56); `705655-705666` first fitting with bone anchoring |
| For beneficiaries **under 18** with a permanent hearing loss observed for **at least three months** having a negative impact on speech or language development, or where a link is established between the hearing deficit and **school delay** |

### Clinical thresholds as eligibility

Audiology makes measurement itself the condition: speech audiometry in noise determining the
signal-to-noise ratio for a **50% speech index**, obtained under headphones with speech and noise in the
same ear (ipsilateral) at a noise level of **60 dB SPL**; and improvement criteria of **2 dB** of
signal-to-noise ratio for a 50% score, **or 10%** of speech intelligibility on the SRT (Speech Reception
Threshold).

These are instrument readings that gate reimbursement — they belong in structured clinical fields, not
free text.

## Oversight

Information and attestations in this domain *"peuvent être demandées par le médecin-conseil et/ou le
Service d'évaluation et de contrôle médicaux"* (SECM) — article 31 alone carries 18 such provisions. The
audit counterparty is both the fund's advising physician **and** the national inspection service.

## Build implications

1. **Model the device as an entity with identity and a lifetime**, because caps are per prosthesis, per
   ear, per eye and per orbit. A claim line referencing only a code cannot express these.
2. **Renewal schedules are age-dependent at the moment of renewal** — compute age at renewal date, not at
   first supply.
3. **Prescription-required is per code**, with an explicit exempt list. Do not apply it article-wide.
4. **Agreement requirement depends on device classification** (mechatronic knee vs not). Encode the
   device taxonomy, and require pre-delivery agreement where it applies — after delivery is too late.
5. **Store the group-classification rationale**, since it is auditable by the médecin-conseil.
6. **Capture audiometric and optical measurements structurally** — they are eligibility criteria.
7. **Count the audiology forfait per centre**, which means your counter needs the supplier dimension; a
   patient may legitimately trigger it at more than one centre.
8. **Treat the six stale articles as unverified** until re-downloaded.

## Gaps and figures to verify

- **Current versions of articles 27, 28 §1–7, 28 §8, 29, 35 and 35bis** — the retrieved texts date from
  2012–2014. Highest-priority re-check in this domain.
- Article 28 §8's 77 cumulation prohibitions and 32 allowances — not enumerated.
- Articles 27/1, 29, 29/1 supplement structures (43–44 supplement provisions each) — not enumerated.
- Articles 35 and 35bis implant lists and the **U** key-letter value *(art. 35 notes the U value and
  coefficient were pending fixing by convention at the version read — confirm current status)*.
- The full group taxonomy (A.5.2.) for prosthetics.
- Whether the implant notification services (`RCT`, `Sadmi` — see [[ehealth-platform-and-apis]]) are a
  billing precondition or a parallel registry obligation.

Sources: [[sources]].
