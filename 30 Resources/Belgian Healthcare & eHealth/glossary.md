---
classification: public
status: draft
updated: 2026-10-01
---

# Glossary

Belgian healthcare runs on acronyms, in two languages, often with a third English form. Entries marked
*(to verify)* are expansions or meanings not confirmed in the research pass behind this knowledge base.

## Institutions and bodies

| Term | Expansion | What it is |
|---|---|---|
| **INAMI / RIZIV** | *Institut national d'assurance maladie-invalidité* / *Rijksinstituut voor ziekte- en invaliditeitsverzekering* | National health and disability insurance institute. Nomenclature, tariffs, premiums |
| **OA / VI** | *Organisme assureur* / *Verzekeringsinstelling* | Sickness fund (insurer) that reimburses care |
| **NIC / CIN** | *Collège Intermutualiste National* / *Nationaal Intermutualistisch College* | The sickness funds' joint college. Operates MyCareNet |
| **Medicomut** | *Commission nationale médico-mutualiste* | Doctors–funds negotiating commission. Accepts software suites |
| **SPF / FOD** | *Service public fédéral* / *Federale Overheidsdienst* | Federal public service (ministry). SPF Santé publique owns practice law |
| **Smals** | — | Non-profit IT provider to social security and health institutions |
| **BCSS / KSZ** | *Banque Carrefour de la Sécurité Sociale* / *Kruispuntbank* | Crossroads Bank for Social Security |
| **AFMPS / FAGG** | *Agence fédérale des médicaments et des produits de santé* | Medicines and health products agency |
| **APD / GBA** | *Autorité de protection des données* / *Gegevensbeschermingsautoriteit* | Belgian Data Protection Authority |
| **AVIQ** | *Agence pour une Vie de Qualité* | Walloon health and welfare agency |
| **Iriscare** | — | Brussels bicommunity welfare and health body |
| **COCOM / GGC** | *Commission communautaire commune* | Brussels common community commission |
| **VSB** | *Vlaamse Sociale Bescherming* | Flemish social protection scheme |
| **FMM** | *Fédération des maisons médicales* | Federation of capitation-funded community health centres |
| **CEBAM** | Belgian Centre for Evidence-Based Medicine | Publishes the Evidence Linker, itself a premium criterion |
| **Ordomedic** | *Ordre des médecins* / *Orde der artsen* | Order of Physicians; medical deontology |
| **ABSyM / BVAS**, **GBO**, **AADM** | — | Doctors' unions |

## Platforms and infrastructure

| Term | What it is |
|---|---|
| **eHealth platform** | Federal institution providing secure health-data-exchange infrastructure |
| **MyCareNet** | The funds' platform for administrative and financial messages with providers |
| **CareNet** | MyCareNet's predecessor; still referenced in live layout specifications |
| **ProSanté** | INAMI provider portal, formerly MyInami. Used to claim the practice premium |
| **masante.belgique.be / Mijngezondheid** | Citizen portal for personal health data and consent |
| **Metahub** | Federal index of where a patient's health data is held (*répertoire des références*) |
| **Hub** | Regional network sharing health data: CoZo, VZN KU Leuven/nexuzhealth, Abrumet, RSW |
| **Vitalink** | Flemish regional data vault for regionally-regulated data |
| **CoZo** | Collaborative Care Platform, Flemish hub; includes the Antwerp Regional Hub (ARH) |
| **Abrumet / RSB** | *Réseau Santé Bruxellois* / Brussels Health Network |
| **RSW** | *Réseau Santé Wallon* |
| **VZN KU Leuven** | Flemish hospital network behind nexuzhealth |
| **CoBRHA** | *Common Base Registry for HealthCare Actors* — authentic source of healthcare actors |
| **MediPrima** | Scheme for medical costs covered through public social assistance |
| **Recip-e** | The electronic prescription system |
| **FHC** | **Free Health Connector** — open-source (AGPL-3.0) connector to Belgian eHealth services, by iCure/Taktik |
| **status.ehealth.fgov.be** | Live service status and incident history |

## Technical services

| Term | What it is |
|---|---|
| **I.AM** | eHealth integrated user and access management |
| **STS** | Security Token Service — issues the SAML tokens the estate requires |
| **SAML** | Security Assertion Markup Language — the assertion format for authorisation |
| **ETEE** | End-to-end encryption service group |
| **ETK** | eHealth Token Key — a recipient's encryption token, held in the **ETKDepot** |
| **KGSS** | Key Generation and Storage Service — symmetric keys for unknown recipients |
| **eHealthBox / ehBox** | Secure mailbox between healthcare actors |
| **PADAC** | Patient Data Access Control — consent, links, exclusions, matrix |
| **TherLink** | Therapeutic link: this clinician is involved in this patient's care |
| **TherExclusion** | Patient's exclusion of a named provider from access |
| **RN Consult** | National Register / BCSS register consultation services |
| **Seals** | Encode/decode sensitive data with eHealth-held keys |
| **UHMEP** | The eReferral service (FHIR R4) |
| **PSS** | *Plateforme de soutien à la prescription* — prescriber decision support (antimicrobials, radiology) *(to verify)* |
| **SAMv2** | *Source Authentique des Médicaments* — authentic medicines source |
| **DICS** | Service for authorised medicines and reimbursement data |
| **VIDIS** | Shared medication scheme interoperability project |
| **BIHR** | Belgian Integrated Health Record |
| **BeSafeShare** | Multidisciplinary data-sharing project |
| **BelRAI** | Standardised care assessment instrument and service |
| **Mult-eMediatt** | Electronic work-incapacity certificate transmission to the funds |

## Standards and codes

| Term | What it is |
|---|---|
| **KMEHR** | *Kind Messages for Electronic Healthcare Record* — Belgian clinical XML standard, 2002 |
| **Sumehr / SumEHR** | *Summarised Electronic Health Record* — the patient summary, in KMEHR |
| **FHIR** | HL7 Fast Healthcare Interoperability Resources; priority standard in the federal roadmap since 2019 |
| **R4** | The FHIR release used by the two Belgian FHIR APIs |
| **Nomenclature** | INAMI's catalogue of reimbursable services, with codes and fees |
| **NomenSoft** | INAMI's nomenclature database and search tool |
| **SNOMED CT** | International clinical terminology *(Belgian licence status — to verify)* |
| **ICPC-2** | Primary-care classification *(to verify)* |
| **ICD-10-BE** | Belgian hospital diagnosis/procedure coding *(to verify)* |
| **LOINC** | Laboratory observation codes *(to verify)* |
| **ATC** | Anatomical Therapeutic Chemical medicine classification *(to verify)* |
| **CNK** | Belgian pharmaceutical product code *(to verify)* |

## Identifiers

| Term | What it is |
|---|---|
| **NISS / INSZ** | National register number — the universal person identifier, 11 digits |
| **BIS number** | Identifier for a person without a NISS |
| **INAMI/RIZIV number** | A practitioner's billing identifier, with check digits (moduli 97, 83, 79, and 89) |
| **N° mutualité** | Three-digit sickness-fund identifier |
| **CBE / KBO** | *Banque-Carrefour des Entreprises* / *Kruispuntbank van Ondernemingen* — enterprise number |
| **eID** | Belgian electronic identity card |
| **itsme** | Mobile identity app accepted for authentication |
| **CSAM** | Federal identity and access gateway |

## Billing and financing

| Term | What it is |
|---|---|
| **eAttest** | Electronic care attestation under cash payment; synchronous, during the visit |
| **eFact** | Electronic third-party-payer invoicing to the funds; asynchronous batches |
| **eTar** | Tariff consultation service |
| **eAgreement** | Electronic agreement requests |
| **Chapitre IV / Chapter IV** | Medication reimbursement requiring prior agreement from the fund |
| **DMG / GMD** | *Dossier médical global* / *Globaal medisch dossier* — a patient's designated GP record arrangement, with an annual fee |
| **eDMG** | Electronic billing/notification of the DMG via MyCareNet |
| **Tiers payant** | Third-party payer: the fund pays the provider directly |
| **Paiement comptant** | Cash payment: the patient pays, then claims reimbursement |
| **Ticket modérateur** | The patient's co-payment |
| **MAF** | *Maximum à facturer* — annual ceiling on a household's co-payments |
| **BIM / OMNIO** | Statuses granting increased reimbursement (*intervention majorée*) |
| **Forfait (maison médicale)** | Capitation: a fixed monthly amount per registered patient per discipline |
| **Forfaits A / B / C / toilette** | Dependency-based lump sums for **home nursing** — a different mechanism from capitation |
| **PTS** | *Prestation technique spécifique* — specific technical nursing service |
| **Médecin conseil** | The fund's advising physician, who decides on certain agreements |
| **Prime de pratique intégrée** | Annual GP premium based on accepted software plus measured e-service use |
| **Document justificatif** | Proof-of-care document given to the patient, required in four defined scenarios |
| **Maison médicale / wijkgezondheidscentrum** | Community health centre, often capitation-funded, multidisciplinary |
| **Lettre-clé / key letter** | The scale a nomenclature code belongs to (`K`, `N`, `I`, `M`, `W`, `L`); the fee derives from coefficient × the letter's value |
| **Coefficient** | The relative weight of a service, e.g. `M 24`, `W 0,879`. Belgian decimal comma |
| **Règle interprétative** | Numbered official Q&A resolving a disputed billing case, published per nomenclature article, with effective and abrogation dates |
| **Journée de soins** | "Care day" — the billing unit for nursing forfaits and visit ranking |
| **Aide-soignant** | Care assistant; may perform delegated parts of a nursing service if the file shows competence per part |
| **Cumul** | Billing two services together. Much of the nomenclature consists of cumulation prohibitions |
| **Champ opératoire** | Operative field. A second act in a *distinct* field is billed at 50% (art. 15 §4); two incisions in one field are not two fields |

## Regulatory

| Term | What it is |
|---|---|
| **Quality Law** | Law of 22 April 2019 on the quality of healthcare practice; in force 1 July 2022. Art. 33 record contents, art. 35 retention 30–50 years |
| **Patient Rights Law** | Law of 22 August 2002 |
| **GDPR Art. 9** | Special-category data, including health |
| **MDR** | Medical Device Regulation (EU) 2017/745 |
| **SaMD** | Software as a Medical Device |
| **CDS** | Clinical decision support |
| **AI Act** | EU regulation on artificial intelligence; clinical CDS is likely high-risk |
| **MDCG** | Medical Device Coordination Group; published guidance on MDR/IVDR–AI Act interplay |
| **EHDS** | European Health Data Space |
| **NIS2** | EU cybersecurity directive covering healthcare *(Belgian transposition — to verify)* |
| **DPA** | Data Processing Agreement (also: Data Protection Authority — context decides) |

## Message numbers quick reference

| Number | Meaning |
|---|---|
| `801000` / `801900` | Insurability request / response (synchronous) |
| `920000` | eFact invoicing batch |
| `931000` | eFact reception acknowledgement |
| `920098` / `920099` | Informational error report / batch rejection (blocking errors or >5% error rate) |
| `920900` | eFact final settlement file |
| `410000` / `410900` / `410999` | Home-nursing forfait request / agreement / refusal |
| `410908` | Advising-physician decision, agreement closure, or rectification (fund-initiated) |
| `420000` / `420900` / `420999` | Palliative care notification / agreement / refusal |
| `430000` | Specific technical service notification |
| `891000` | Generic acknowledgement |

Full detail: [[mycarenet-services-and-flows]]. Billing rules: [[billing-rules-and-cumulation]].
