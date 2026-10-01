---
classification: public
status: draft
updated: 2026-10-01
---

# Regulatory and compliance

The legal frame around health software in Belgium: data protection, professional practice law, medical
device law, AI law, and the European layer arriving on top.

**This page is orientation, not legal advice.** Every item below needs a lawyer before it becomes a
design commitment.

## Data protection

### GDPR and health data

Health data is **special-category data under GDPR Article 9**: processing is prohibited unless a
specific exception applies. In practice, care provision relies on Art. 9(2)(h) (health care and
treatment) with Art. 9(3) professional-secrecy conditions, alongside a lawful basis under Art. 6
*(mapping to be confirmed with counsel)*.

Consequences that shape architecture rather than paperwork:

- **Purpose separation.** Care delivery, practice administration, quality improvement, research and
  product analytics are different purposes with different bases. A single undifferentiated data lake
  is a compliance problem.
- **Access logging and minimisation.** Who saw what, and why they needed to.
- **Processor relationships.** A software vendor hosting clinical data is a processor to the practice;
  a DPA is mandatory, and sub-processors (hosting, model providers) must be covered.

The Belgian **Data Protection Authority (APD/GBA)** has published specific guidance on the processing
of data originating from patient records — worth reading before designing secondary use.

### The model-provider question

Sending clinical content to a commercial model API is a transfer to a processor, under that provider's
retention terms. This is the concrete reason administrative AI and clinical AI have different
compliance profiles: a rejected-invoice explanation is not the same risk object as a differential
diagnosis. Design the boundary deliberately, and keep clinical inference behind a different, stricter
gate than administrative automation.

## Professional practice law

### Patient rights (law of 22 August 2002)

Establishes the patient's rights: quality service, free choice of practitioner, information, consent,
a carefully-kept record, access to and copies of that record, privacy, complaint mediation. FPS Public
Health publishes a citizen brochure, updated 2025.

For software: **patient access to the record is a right, not a feature request.** Access, copy, and the
handling of personal notes and third-party data within a record all need designed answers.

### The Quality Law (law of 22 April 2019)

*Loi relative à la qualité de la pratique des soins de santé.* In force **1 July 2022**, applying to
all health professionals. It covers therapeutic freedom, the practice visa, record-keeping, continuity
of care and more.

Two articles matter directly to a record system:

| Article | Requirement |
|---|---|
| **Art. 33** | The **minimum elements** that must be recorded in the patient record, grouped in three broad categories |
| **Art. 35** | **Retention: minimum 30 years, maximum 50 years** from the last patient contact — a uniform rule for hospital and non-hospital records |

Art. 35 is a hard architectural constraint. Thirty to fifty years means: format durability, migration
across technology generations, a documented export path independent of the vendor, legal-hold
semantics, and a deletion policy that distinguishes retention obligation from GDPR erasure rights.
A startup must answer "what happens to this data if you disappear" with something better than good
intentions — and practices will ask.

Art. 33 is the clinical equivalent of a required-fields specification: the record template should map
to it explicitly, and be demonstrably complete.

The Order of Physicians (Ordomedic) has published opinions on the law's practical and deontological
difficulties, which are a useful read on where implementation is genuinely contested.

## Medical device and AI regulation

### MDR — when does software become a medical device?

Under **MDR (EU) 2017/745**, software with a medical purpose is a medical device — *Software as a
Medical Device* (SaMD). Medical purposes include diagnosis, monitoring of physiological parameters, and
**support for therapeutic decision-making**.

The practical line for a practice system:

| Function | Likely status |
|---|---|
| Recording, storing, transmitting, displaying data | Generally **not** a device |
| Billing, scheduling, administration, accounting | **Not** a device |
| Drug–drug interaction alerts, dosing advice, diagnostic suggestion, risk scoring | **Likely a device**, with classification and CE marking |

*(Qualification is function-by-function and fact-specific — this table is orientation only.)*

The design consequence is clear: **isolate decision-support functionality into a separable module**, so
that the regulatory status of one feature does not contaminate the whole product, and so the module can
be assessed, versioned and if necessary withheld independently.

### The AI Act, and its interaction with MDR

A clinical AI tool supporting diagnostic decisions is likely to be **high-risk under the EU AI Act**,
while also being a medical device under MDR.

Where both apply, **both apply simultaneously.** The AI Act expects its obligations to be integrated
into the existing MDR conformity assessment where possible, and the MDCG has published guidance on the
MDR/IVDR–AI Act interplay.

Genuinely new obligations the AI Act adds on top of MDR include:

- **data governance with bias testing**,
- specific **human oversight** requirements, and
- **expanded logging**.

For an AI-first product, the sequencing implication is strong: **administrative AI first, clinical AI
later and feature by feature.** Automating invoice-rejection triage, coding suggestions, correspondence
and reconciliation keeps you outside device territory while delivering measurable value. Human
confirmation on every output is both a product principle and an alignment with the human-oversight
requirement.

## The European layer

| Instrument | Relevance |
|---|---|
| **EHDS** — European Health Data Space | Named by the eHealth platform as a key initiative. Will shape primary-use interoperability requirements and secondary-use access across the EU |
| **NIS2** | Cybersecurity obligations; healthcare is a covered sector *(Belgian transposition and applicability to a software vendor — to verify)* |
| **eIDAS** | Underlies qualified timestamping and signatures *(to verify)* |

## Licensing: a compliance topic too

The **Free Health Connector** is **AGPL-3.0** licensed — the only open-source implementation of the
Belgian eHealth connectors. AGPL's network-use provision makes the deployment topology a licensing
question, not merely a technical one. The conventional low-risk posture is to run it **unmodified, as a
separate service**, and keep your own code out of its licensing boundary. See
[[integration-architecture]]. **Get this reviewed by counsel** — it is a foreseeable diligence question
in any future investment or acquisition.

## A compliance checklist for a practice system

| Area | Must have |
|---|---|
| Lawful basis | Documented bases per purpose; DPAs with the practice and all sub-processors |
| Record content | Mapping to Quality Law art. 33 |
| Retention | 30–50 year strategy, with migration and exit paths |
| Patient rights | Access, copy, rectification, mediation support |
| Access control | Consent, therapeutic link, exclusion, per-person identity, full read logging |
| Security | Encryption at rest and in transit, key management, penetration testing, breach procedure |
| Device status | Per-feature MDR qualification; decision support isolated and separately assessed |
| AI | Human confirmation; logging; bias testing where high-risk; clear admin/clinical boundary |
| Hosting | EU hosting appropriate to health data; documented sub-processors |
| Licensing | AGPL boundary reviewed; dependency licence inventory |

## Build implications

1. **Isolate the clinical core and the decision-support module**, so regulatory status, access rules
   and audit obligations can differ from the administrative product.
2. **Sequence AI administrative-first**, with human confirmation as a product invariant.
3. **Design retention for 30–50 years on day one**, including a vendor-independent export.
4. **Map the record template to Quality Law art. 33** and be able to demonstrate it.
5. **Make patient access a built feature.**
6. **Log all clinical reads**, and make break-glass access exceptional, dual-controlled and auditable.
7. **Settle the AGPL topology before writing connector-adjacent code.**

## Gaps and figures to verify

- Precise GDPR Art. 6/9 basis combination for each purpose in a practice system.
- NIS2 applicability to a healthcare software vendor under Belgian transposition.
- Whether any current Belgian guidance addresses AI in patient records specifically.
- MDR classification likely to apply to common interaction/alerting features.
- AI Act implementation timeline as it applies to this product category.
- Professional-secrecy rules as they constrain vendor staff access to production data.

Sources: [[sources]].
