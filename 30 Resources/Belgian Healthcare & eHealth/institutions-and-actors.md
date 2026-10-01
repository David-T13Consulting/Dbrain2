---
classification: public
status: draft
updated: 2026-10-01
---

# Institutions and actors

Who decides, who pays, who operates the rails. Belgian healthcare is federal for compulsory
insurance and regional for prevention, welfare and parts of long-term care — which is why a practice
system faces several administrations rather than one.

## The short version

| Layer | Who | What they control that a software builder cares about |
|---|---|---|
| Financing & rules | **INAMI / RIZIV** | Nomenclature codes, tariffs, conventions, financial premiums |
| Technical rails | **eHealth platform** | Identity, encryption, mailboxes, document index, API catalogue |
| Payers | **Organismes assureurs (OA)** / mutualités | Insurability, reimbursement, invoice acceptance |
| Payer IT | **NIC / CIN** via **MyCareNet** | Every administrative and billing message a practice sends |
| Public health policy | **SPF Santé publique / FPS Public Health** | Professional recognition, patient rights, quality law |
| Regions | AVIQ · Iriscare/Vivalis · Zorg en Gezondheid / VSB | Prevention, long-term care, regional vaults and insurability |
| Build & operate | **Smals** | Much of the actual IT, vendor registration, test environments |

## Federal level

### INAMI / RIZIV

*Institut national d'assurance maladie-invalidité* / *Rijksinstituut voor ziekte- en
invaliditeitsverzekering*. The national health and disability insurance institute, and the single
most important counterparty for anyone billing healthcare in Belgium.

What it owns:

- **The nomenclature** — the catalogue of reimbursable services, each with a code, description,
  official fee and reimbursement amount. See [[reimbursement-and-financial-flows]].
- **Conventions and accords** — the negotiated agreements between providers and payers that set
  tariffs. For doctors this happens in the *Commission nationale médico-mutualiste* (the
  "medicomut"), which also **accepts software suites** for premium purposes.
- **Financial interventions** — notably the *prime de pratique intégrée*, the annual premium that
  pays GPs for measured e-service usage. See [[software-homologation-and-obligations]].
- **Provider-facing web programmes** — ProSanté (formerly MyInami), NomenSoft, the Health PRO
  provider directory.
- **A software-vendor track**, with its own registration process, technical notes and test sessions.
  Contacts published: `esante@riziv-inami.fgov.be`, and `healthcare-registration@smals.be` for
  practical registration questions.

Note the dual naming: `inami.fgov.be` and `riziv.fgov.be` serve the same content in FR and NL, and
official email addresses use `riziv-inami.fgov.be`. Expect both spellings in documentation.

### The eHealth platform

A federal public institution providing the secure-exchange infrastructure for health data. It is
explicitly plumbing: identity and access management, end-to-end encryption, a secure mailbox, a
timestamping authority, pseudonymisation, and an index saying where a patient's documents live. It
does not hold clinical records itself.

Its current strategy is the **interfederal eHealth action plan 2026–2029**, built on three axes:

1. Advance the foundational platform services that other projects depend on.
2. Operationalise the **BIHR** (Belgian Integrated Health Record) — authentic data sources plus
   optimised software interfaces for linking and visualising data.
3. Align digital initiatives with substantive care programmes (perinatal care, vulnerable
   populations, childhood obesity).

Governance is explicitly interfederal, with strategic and tactical/operational levels, and the plan
states it balances collective objectives against regional autonomy. For a vendor this matters
because it signals which projects will carry obligations over the next three years — BIHR, VIDIS,
eReferral, BeSafeShare, prescriber decision support.

Patient-facing counterpart: **masante.belgique.be** / *mijngezondheid*, where citizens see and manage
their own data and consent.

Operational detail worth bookmarking: **status.ehealth.fgov.be** publishes live service status and
incident history per service. In a domain where your software fails when a federal SOAP endpoint
fails, this is a dependency you monitor, not a page you read once.

### SPF Santé publique / FPS Public Health

`health.belgium.be`. Owns professional practice law rather than money: the visa and recognition of
health professionals, patient rights, and the 2019 Quality Law that sets what a patient record must
contain and how long it is kept. See [[regulatory-and-compliance]].

### Other federal bodies

| Body | Role |
|---|---|
| **Smals** | Non-profit IT provider to social security and health institutions. Builds and runs much of the infrastructure, hosts vendor registration and FHIR test servers, publishes technical reference material |
| **Sciensano** | National public health institute: epidemiological surveillance, registries, research |
| **AFMPS / FAGG** | Medicines and health products agency: authorisation, pharmacovigilance, device market surveillance |
| **BCSS / KSZ** | Crossroads Bank for Social Security. The eHealth platform is modelled on it and reuses its register access patterns (see RN Consult in [[ehealth-platform-and-apis]]) |
| **APD / GBA** | Data Protection Authority. Has published specific guidance on processing data from patient records |

## The payers

**Organismes assureurs (OA)** / *verzekeringsinstellingen* — the sickness funds that reimburse care.
Every Belgian resident must be affiliated to one. Structurally there are five national unions of
mutualities plus two public funds: the auxiliary fund (CAAMI / HZIV) and the HR Rail fund
*(exact current composition — to verify against INAMI's official list before quoting)*.

The commercially important point: **OAs are not a single integration target, but they are a single
message target.** Their shared IT college provides one entry point.

### NIC / CIN and MyCareNet

The *Collège Intermutualiste National* / *Nationaal Intermutualistisch College* is the OAs' joint
body. It operates **MyCareNet**, the platform through which providers exchange administrative and
financial messages with all OAs at once: insurability checks, third-party-payer invoicing,
attestations, agreements, global medical file notifications.

MyCareNet is the predecessor CareNet's successor, and both names appear in the specifications — the
flat-file layouts still reference "the CareNet documentation" for the transport segment. See
[[mycarenet-services-and-flows]].

MyCareNet publishes **per-sector and per-service lists of approved software** (*logiciels agréés*),
which is simultaneously the market map and the compliance checklist. See [[vendor-landscape]].

## Regional level

Prevention, welfare, long-term care and parts of residential care are regional competences. Each
region has built its own data infrastructure, and each has its own insurability or member-data
service — the eHealth API catalogue publishes `MyVSBNet-Insurability`, `WalCareNet-MemberData` and
`IrisCareNet-MemberData` alongside the federal MyCareNet equivalents.

| Region | Administration | Data infrastructure |
|---|---|---|
| Flanders | Zorg en Gezondheid; **VSB** (Vlaamse Sociale Bescherming) with the zorgkassen | **Vitalink** vault; **CoZo** and **VZN KU Leuven / nexuzhealth** hubs |
| Wallonia | **AVIQ** | **Réseau Santé Wallon (RSW)** hub |
| Brussels | **Iriscare** and Vivalis / COCOM | **Abrumet / Réseau Santé Bruxellois** hub, officially designated by COCOM |

See [[clinical-data-sharing-and-standards]] for how the hubs interconnect through the federal metahub.

## Registries of actors

**CoBRHA** — *Common Base Registry for HealthCare Actors*. The authentic source for who is a
healthcare actor: practitioners, their qualifications and recognitions, and organisations. The eHealth
platform publishes consultation, publication, full-search, historical and notification APIs over it.
Access rules for most services are evaluated against CoBRHA — for example, restricting an application
to physicians "in order at the level of the professional registry".

Alongside it: the **AddressBook** / Directory services for contact data and relationships between
actors, and a **Software Register** API giving access to centralised software-package data for the
eHealth domain.

## Professional bodies and federations

Not regulators, but they set tone, negotiate and act as distribution channels.

| Body | Who |
|---|---|
| **Ordre des médecins / Orde der artsen** (Ordomedic) | Medical deontology; publishes opinions, including on the Quality Law's practical difficulties |
| **ABSyM / BVAS**, **GBO**, **AADM** | Doctors' unions; negotiate in the medicomut and publish accessible explainers of premiums and DMG rules |
| **Fédération des maisons médicales (FMM)** | Federation of capitation-funded community health centres |
| **CEBAM** | Belgian Centre for Evidence-Based Medicine; its Evidence Linker is itself a premium criterion |

A practical note: the unions' and federations' sites are often **clearer and more current than the
official pages** on topics like premium conditions, because they translate circulars into plain
guidance quickly. They are secondary sources — useful for orientation, always confirm against INAMI.

## Build implications

1. **Model the payer as one interface, many counterparties.** Send through MyCareNet, but keep OA
   identity (`n° mutualité`, three digits) as first-class data, because acceptance, rejection and
   settlement all come back per OA.
2. **Expect at least four administrative masters.** Federal INAMI (money), federal eHealth
   (technical), the region (prevention and long-term care), plus the profession's own rules. A system
   serving a multidisciplinary centre may touch all of them for a single patient.
3. **Treat CoBRHA as the source of truth for provider identity**, not your own user table. Who may do
   what is decided against the professional registry, so your authorisation model should resolve
   against it rather than duplicate it.
4. **Put status.ehealth.fgov.be in your operational monitoring.** Institutional dependency failures
   are a daily operational reality, not an edge case; the product needs degraded modes, queueing and
   honest user messaging.
5. **Track the 2026–2029 action plan as your roadmap input.** BIHR, VIDIS and eReferral are where the
   obligations and the test sessions will be.

## Gaps and figures to verify

- Exact current list and count of OAs — stated from general knowledge, not confirmed against INAMI.
- Whether the *Commission nationale médico-mutualiste* remains the formal body accepting software
  suites, and the current acceptance procedure.
- The legal instrument establishing the eHealth platform (commonly cited as the law of 21 August
  2008) — not verified in this pass.
- Current regional competence split after the most recent state reform.

Sources: [[sources]].
