---
classification: public
status: draft
updated: 2026-10-01
---

# Identity, access and consent

Who is this person, who is this clinician, and is this clinician allowed to open this record. In
Belgium these are answered by **federal services**, not by application logic — which is good news for
a builder, because the hard parts are externalised, and bad news, because you cannot shortcut them.

> **Policy note.** This page describes identifier *formats and semantics* only. Government
> identification numbers never enter this vault, in any form, real or example — `data-policy.md` §2.3.
> No specimen NISS or INAMI numbers appear below, deliberately.

## Identifiers

| Identifier | Belongs to | Shape | Notes |
|---|---|---|---|
| **NISS / INSZ** (*numéro de registre national*) | A person | 11 digits | The universal patient key. Encodes date of birth and a check component |
| **BIS number** | A person without a NISS | Same shape, different series | Minted through `RNConsult Creabis`. Non-residents, some newborns, certain insured persons |
| **INAMI/RIZIV number** | A practitioner | Numeric, with qualification-bearing structure and a check digit | The billing identity of the clinician |
| **N° mutualité** | A sickness fund | 3 digits | Appears in every MyCareNet message |
| **Membership number** (*n° d'inscription mutualiste*) | A person at a fund | 13 alphanumeric | Fund-side patient key |
| **CBE/KBO number** | An organisation | 10 digits | The legal entity behind the practice |

### INAMI number check digits — a concrete requirement

INAMI's software-vendor communications specify check-digit validation using **modulo 97, 83 and 79**,
with a **new modulo 89** to be implemented alongside them. The validation formula and details are
published in **annex 16.3 of the electronic billing instructions**.

Two things follow. First, validate practitioner numbers locally — you will otherwise discover invalid
numbers at batch-rejection time (see the 5% rule in [[mycarenet-services-and-flows]]). Second, note
that *multiple moduli coexist and new ones get added*: hard-coding one algorithm is a known-future
defect. Treat check-digit validation as versioned, configurable reference logic.

## Authenticating people

The eHealth platform's **I.AM** service is described as the foundation of its entire data-exchange
security process: ensuring only authorised providers and organisations reach services they may use.

Supported authentication means include **eID** (card plus reader), **itsme** (mobile identity app) and
**TOTP**. Federal authentication is fronted by **CSAM**, the government's identity gateway *(CSAM's
exact role in the provider flows — to verify)*.

The generic authorisation model, as the platform describes it:

1. The application declares its own access rules.
2. I.AM consults those rules for the target application.
3. It verifies the user against them.
4. It grants or denies access.

Rules are evaluated against the **professional registry** — the published example restricts an
application to physicians "in order at the level of the professional registry", i.e. resolved through
CoBRHA. So *authorisation is a property of the clinician's registered professional status*, not of a
role you assign in your own user table.

### The token flow

| Step | Service |
|---|---|
| Obtain a SAML authorisation token | `IAM-STS-SecurityTokenService` v1.3 (SOAP) |
| Single sign-on from a thick to a thin client | `IAM-STS-SingleSignOnService` v1.3 (SOAP) |
| Retrieve subject attributes | `IAM-AttributeAuthority` v1.1 (SOAP) |
| Exchange a modern access token for a SAML token | `IAM-Exchange` v2.0 (REST) |
| Fetch IAM metadata | `IAM-Metadata` v1.1 (REST) |

`IAM-Exchange` is the bridge worth knowing about: it lets an OAuth/OIDC-shaped application obtain the
SAML assertion the rest of the estate expects. That is the seam where a modern front end meets a
SAML-era back end.

Mandates matter too: a practice administrator or a secretary may act for a practitioner, and services
may require an **eHealth mandate** rather than a direct professional qualification. Model delegation
explicitly.

## Authorising access to a record: PADAC

**PADAC** — Patient Data Access Control — is the service group that decides whether a given clinician
may see a given patient's data. Four concepts, each with its own API:

### 1. Consent

The patient's **informed consent** to the electronic sharing of their health data. Without it, the
sharing infrastructure does not open. Patients can give, consult and withdraw it themselves, including
through the citizen portal (`masante.belgique.be` / *mijngezondheid*), as well as through a provider
or a fund.

APIs: `Consent` v2.3 and v1.0 (REST), v1.4 (SOAP).

### 2. Therapeutic link (*lien thérapeutique* / TherLink)

Consent says "data may be shared"; the **therapeutic link** says "*this* clinician is involved in
*this* patient's care". It is the per-relationship authorisation.

What is published about it:

- The service lets an authorised provider **create** a therapeutic relationship — between themselves
  and the patient, or **between the patient and another provider** — and **search** existing ones.
- Creation can be evidenced by the patient's **identity card**, and the eHealth platform published
  specific guidance (2026) on how relationships come about, their duration, and the use of the eID.
- Links are related to the **DMG**: holding a patient's global medical file is itself a basis for a
  relationship. See [[reimbursement-and-financial-flows]].
- Links have **finite duration** and types that vary by discipline and context *(exact durations —
  to verify; a commonly cited figure is 15 months for a GP link, which this pass did not confirm)*.

APIs: `TherLink` v2.3 (REST) / v1.4 (SOAP); `Link` v1.3 (REST) for therapeutic and care relationships.

### 3. Therapeutic exclusion (TherExclusion)

The patient's veto: excluding a **named provider** from access to their data. This is a patient right
expressed in infrastructure, and it overrides a clinician's otherwise valid link.

API: `TherExclusion` v2.3 (REST). The platform also exposes exclusion management through `Metahub` v2.6.

### 4. Access matrix (Matrix)

`Matrix` v1.1 (REST) manages patient access matrices — the mapping of which categories of actor may
reach which categories of data *(detailed semantics — to verify)*.

### The resulting access decision

```
May this clinician read this patient's data?

  Is the clinician authenticated?                  (I.AM: eID / itsme / TOTP)
    └─ Is their professional status valid?          (CoBRHA / professional registry)
         └─ Has the patient given consent?          (Consent)
              └─ Is there a valid therapeutic link? (TherLink / Link)
                   └─ Has the patient excluded them?(TherExclusion)  ─── if yes: DENY
                        └─ Does the access matrix permit this data category? (Matrix)
                             └─ ALLOW — and log the access
```

Every step is a federal service call. None of it is yours to decide.

## Logging is part of the contract

The platform provides a **log management** basic service for user activity and access tracking, and
access logging is an expectation of the model rather than an optional feature. Patients can ask who
looked at their data.

For a multi-user practice system this has a hard design consequence: **shared accounts are
incompatible with the model**. If three clinicians and a secretary share a login, you cannot produce a
truthful access log, cannot resolve professional status per actor, and cannot honour an exclusion.
Per-person identity is not a nice-to-have.

## Build implications

1. **Resolve authorisation against the registry, don't replicate it.** Your roles layer sits *on top
   of* CoBRHA-derived professional status, never instead of it.
2. **Per-person authentication, always.** Shared logins break logging, exclusions and professional
   resolution simultaneously. In a centre, that includes receptionists and administrators.
3. **Model delegation and mandates as first-class.** Secretaries acting for clinicians is the normal
   case in a practice, not an exception.
4. **Treat consent, link and exclusion as live state, not setup.** Check at access time, cache
   defensively with short validity, and handle "link expired" as an ordinary workflow (prompt to
   re-establish with the eID) rather than an error.
5. **An exclusion must be able to deny an otherwise-valid user.** Make sure your permission model can
   express a patient-driven negative override; many role-based designs cannot.
6. **Log every read, with who/what/when/on-what-basis.** This is both a legal expectation and, for a
   clinical core, the thing that makes break-glass access defensible.
7. **Validate identifiers at entry.** NISS shape, INAMI check digits (all moduli, configurable),
   fund number, membership number. Cheap locally, expensive at batch rejection.
8. **Plan the OIDC↔SAML seam deliberately.** `IAM-Exchange` is where a modern SPA or mobile app meets
   the SAML estate; put it in one place.

## Gaps and figures to verify

- Exact therapeutic-link durations by link type and discipline, and renewal mechanics.
- CSAM's precise role in professional (as opposed to citizen) authentication flows.
- Access-matrix semantics and who defines the categories.
- Whether consent is now universal/opt-out in effect, and the current registered-consent coverage.
- Mandate types available to practice staff, and how they are granted.
- Retention periods for access logs, and the patient-facing route to request them.

Sources: [[sources]].
