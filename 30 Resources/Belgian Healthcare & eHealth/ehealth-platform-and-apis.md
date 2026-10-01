---
classification: public
status: draft
updated: 2026-10-01
---

# The eHealth platform and its APIs

The federal technical layer. Understand it as **infrastructure, not a health record**: it supplies
identity, encryption, mailboxes, timestamping, pseudonymisation and an index of where documents live.
Clinical content stays with the hubs, regional vaults and the providers' own systems.

Each service is designed to be integrated into medical software or third-party applications rather
than used as a standalone tool.

## The eleven basic services

| Service | What it does |
|---|---|
| **IAM** — integrated user and access management | Decides who may use which service. The foundation of the whole security model |
| **End-to-end encryption (ETEE)** | Encrypts payloads for a specific recipient, or for an unknown one |
| **eHealthBox** | Secure electronic mailbox between healthcare actors |
| **eHealth certificates** | The digital certificates an organisation needs to talk to the platform at all |
| **Metahub / répertoire des références** | Index of where a patient's health data is held |
| **Timestamping** | Qualified electronic time-stamping of documents |
| **Pseudonymisation & anonymisation** | Coding and de-identification, notably for secondary use |
| **RN Consult** | Consultation of the National Register and the BCSS/KSZ registers |
| **Coordination of partial electronic processes** | Orchestration across partially electronic workflows |
| **Log management** | User activity and access logging |
| **Portal** | The web front door for providers and organisations |

## End-to-end encryption in practice

Two services, split by whether you know who the recipient is:

| Service | Case | Mechanism |
|---|---|---|
| **ETKDepot** | Recipient **known** | Retrieve the recipient's encryption token (ETK) and encrypt to it |
| **KGSS** | Recipient **unknown** | Obtain a symmetric key from the key-generation/storage service |

Supporting services register and revoke the key material: `ETEE-Ra-Etk` (register encryption and
authentication key pairs) and `ETEE-Ra-Cert` (request and revoke authentication certificates). A REST
`ETEE` v1.1 service exists alongside the SOAP ones.

ETEE is not optional plumbing you can skip: it underpins eHealthBox messaging and Recip-e
prescriptions. The "unknown recipient" case is what makes a prescription usable by *whichever*
pharmacy the patient eventually walks into.

Related: **Seals** (encode/decode sensitive data using keys held by eHealth) and **Pseudonymisation**
(convert, pseudonymise or re-identify records).

## The API catalogue

Published at **portal.api.ehealth.fgov.be**, roughly 80 APIs. The single most consequential
architectural fact: **almost all of them are SOAP/XML**. Only two are FHIR R4.

### Identity and access (IAM)

| API | Protocol | Purpose |
|---|---|---|
| `IAM-STS-SecurityTokenService` v1.3 | SOAP | SAML-based authorisation tokens — the workhorse |
| `IAM-STS-SingleSignOnService` v1.3 | SOAP | SSO from thick to thin clients |
| `IAM-AttributeAuthority` v1.1 | SOAP | SAML attribute authority supplying subject information |
| `IAM-Exchange` v2.0 | REST | Convert access tokens to SAML tokens |
| `IAM-Metadata` v1.1 | REST | Retrieve IAM metadata XML |

### Patient data access control (PADAC)

| API | Protocol | Purpose |
|---|---|---|
| `Consent` v2.3 / v1.4 / v1.0 | REST, SOAP | Patient's informed consent to electronic data sharing |
| `TherLink` v2.3 (REST) / v1.4 (SOAP) | both | Therapeutic links between provider and patient |
| `Link` v1.3 | REST | Therapeutic and care relationships |
| `TherExclusion` v2.3 | REST | A patient's exclusion of a specific provider |
| `Matrix` v1.1 | REST | Patient access matrices |

Notably, PADAC is the one area where REST is well represented. See [[identity-access-and-consent]].

### Registries of actors and people

| API | Protocol | Purpose |
|---|---|---|
| `CoBRHA-Consultation` / `-Publication` v1.7 | SOAP | Healthcare-actor data from authentic sources |
| `CoBRHA+` v1.6 variants | SOAP | Enhanced consultation, full search, historical data, notifications |
| `AddressBook` v1.2 (SOAP) / `Addressbook REST` v1.2 | both | Contact data for professionals and organisations; REST variant supports eHealthBox |
| `Directory` v1.3 | SOAP | Relationships between actors |
| `RNConsult` family | SOAP | National Register: person data, family composition, inscriptions, BCSS/BIS registers, legal representation, refugee waiting register, pseudo/encoded persons |
| `RNConsult Creabis` v1.0 | REST | Create BIS numbers (for people without a NISS) |
| `ConsultRN-SsinHistory` v1.0 | SOAP | Current and historical identifiers |
| `Software Register` v1.0 | REST | Centralised software-package data for the eHealth domain |

### Messaging

`ehBox` v1.2 (REST) · `ehBox-Consultation` v3.0 and `ehBox-Publication` v3.0 (SOAP) ·
`Eh2eBox-Publication` v1.2 (SOAP, to the Social Security eBox).

### Medicines and prescriptions

| API | Protocol | Purpose |
|---|---|---|
| `Recip-e-Prescriber` v4.0 | SOAP | Create and manage prescriptions (doctors) |
| `Recip-e-Executor` v4.0 | SOAP | Retrieve prescriptions and update status (pharmacists) |
| `Recip-e-Patient` v4.0 | SOAP | Patient access to their prescriptions |
| `Dics` v5.2 | SOAP | Authorised medicines and reimbursement data |
| `GFDDPP-PCDH` / `-TIP` v1.0 | SOAP | Medication delivery history |
| `Stock Monitoring Tool` v1.0 | REST | Periodic medicine stock declaration |

### Insurance and billing

The MyCareNet family plus MediPrima and the regional services — see
[[mycarenet-services-and-flows]] for the full list and the message flows behind them.

### Clinical data, decision support and referral

| API | Protocol | Purpose |
|---|---|---|
| `Metahub` v2.6 | SOAP | Consent, therapeutic exclusions and medical-file consultation |
| `BelRAI` v2.0 (SOAP) / v1.1 (REST) | both | Standardised care assessments |
| `PrescriptionSearchSupport` v1.0 | **REST, FHIR R4** | Evidence-based prescribing advice for imaging, antibiotics and lab requests |
| `UHMEP` v1.4 | **REST, FHIR R4** | eReferral: create referrals, assign caregivers, track prescription progress |
| `ChapIVInformationConsultation` v2.0 | SOAP | Reimbursement conditions from authentic sources |
| `TRIO` v1.0 | REST | Medical information exchange for return-to-work coordination |
| `IdSupport` v2.0 | SOAP | Validate patient identification documents |

### Devices, registries, births and emergencies

`RCT` v1.0 (SOAP and REST — implant and device lifecycle notifications) · `Sadmi` v2.0/v3.0 (implanted
device database) · `Ebirth-Notification` and `Ebirth-Medicalform` v1.0 · `EMSRConsultation` /
`EMSRRegistration` v1.0/v2.0 · `SmuregSDS` v1.1.

### Support and testing

`Timestamping-Authority` and `-Consult` v2.2 · `Seals` v1.1 · `Pseudonymisation` v1.0 (REST) ·
`DataAttributeService` v1.1 · **`PlatformIntegrationConsumerTest` v1.4** — a dedicated service for
testing integration including security scenarios, which is the right first call for a new integration.

## Environments and operations

Endpoint hostnames visible in the catalogue indicate separate environments —
`preview.api.ehealth.fgov.be`, `services.ehealth.fgov.be`, `api.ehealth.fgov.be` — and the portal
itself has an acceptance twin at `portal-acpt.api.ehealth.fgov.be`. Formal onboarding, account
requirements and the ACC/PROD split are **not documented on the portal index**; expect to obtain them
through the registration route in [[software-homologation-and-obligations]].

**status.ehealth.fgov.be** publishes per-service status and incident history, with procedure-specific
pages (for example a GP-facing page for the hubs/metahub reference directory). Treat it as a
production dependency feed.

## Strategy: where this is heading

The **interfederal eHealth action plan 2026–2029** sets three axes: advance the foundational platform
services; operationalise the **BIHR** (Belgian Integrated Health Record) through authentic data
sources and better software interfaces for linking and visualising data; and align digital work with
substantive care programmes. Named projects include BIHR, **VIDIS**, eReferral, **BeSafeShare** and
prescriber decision support.

Read that as the forward obligation list. The FHIR R4 APIs that exist today — `PrescriptionSearchSupport`
and `UHMEP` — both come from this generation of projects, which is a reasonable signal that new
services will be FHIR and REST while the existing SOAP estate persists.

## Build implications

1. **Budget for SOAP as a first-class citizen.** WS-Security, SAML assertions, XML signing and WSDL
   tooling are not legacy detours here; they are the mainstream path. Either adopt a connector that
   absorbs this (see [[integration-architecture]]) or accept the cost directly.
2. **Isolate the platform behind an adapter.** Version drift is per service (`v1.0` through `v5.2`
   across the catalogue), so a single façade with per-service versioning beats scattered clients.
3. **Start with `PlatformIntegrationConsumerTest`.** It exists precisely to validate security
   integration before touching a real service.
4. **Certificates and key material are operational infrastructure.** ETEE registration, revocation and
   renewal need owners, monitoring and runbooks — a lapsed certificate is a total outage.
5. **Do not build your own provider registry.** Resolve against CoBRHA and AddressBook.
6. **Expect to handle people without a NISS.** `RNConsult Creabis` exists to mint BIS numbers; a
   patient model that assumes a NISS will break on real populations.
7. **Design for partial availability.** With ~80 upstream services, degraded operation is normal.
   Queue, retry, show honest state, and keep documented manual fallbacks.

## Gaps and figures to verify

- Onboarding procedure, contractual prerequisites and the exact ACC/PROD endpoint map.
- Whether the eleven basic services are still the canonical list, and what "coordination of partial
  electronic processes" covers concretely.
- Rate limits, SLAs and authentication specifics per service.
- The legal basis of the platform (commonly cited as the law of 21 August 2008) — unverified.
- Whether any additional FHIR R4 services have gone live since the snapshot.

Sources: [[sources]].
