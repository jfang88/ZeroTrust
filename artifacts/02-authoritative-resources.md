# Authoritative Zero Trust Resources

*Checked September 2026. Primary sources first; vendor material is listed separately and should be treated as secondary.*

## How the sources fit together

| Role in the programme | Source | Weight |
|---|---|---|
| Definition and logical architecture | NIST SP 800-207 | **Backbone** |
| Maturity scoring per pillar | CISA Zero Trust Maturity Model v2.0 | **Backbone** |
| Cloud-native / multi-cloud access control | NIST SP 800-207A | Reference |
| Worked example implementations | NIST SP 1800-35 | Reference |
| Phased, activity-level implementation | NSA Zero Trust Implementation Guidelines (ZIGs), 2026 | Reference (activity checklist) |
| UK design principles | NCSC Zero Trust Architecture collection | Regional reference |
| Mainland China reference architecture | GB/T 43696-2024 | Regional reference |
| Hong Kong regulatory context | HKMA supervisory guidance; critical infrastructure ordinance | Regional context |
| Privacy and cross-border data rules that shape telemetry design | PIPL and related PRC data laws; UK GDPR; HK PDPO | Constraint |

The backbone is deliberately two documents: NIST SP 800-207 for the model and vocabulary, CISA ZTMM for scoring. Where sources differ, the backbone decides. The NSA ZIGs are used as an activity checklist rather than a third backbone; they are written for defence and are heavier than most enterprises need.

## United States

### NIST SP 800-207 — Zero Trust Architecture (2020)
The foundational definition: policy engine, policy administrator, policy enforcement point, and the tenets of per-session, least-privilege access. Use it for slide 1 and for common vocabulary.
https://csrc.nist.gov/pubs/sp/800/207/final

### NIST SP 800-207A — A Zero Trust Architecture Model for Access Control in Cloud-Native Applications in Multi-Location Environments (2023)
Extends 800-207 to service-to-service identity and policy in cloud-native / service-mesh environments. Relevant to the Applications & Workloads pillar and multi-cloud estates.
https://csrc.nist.gov/pubs/sp/800/207/a/final

### NIST SP 1800-35 — Implementing a Zero Trust Architecture (final, June 2025)
NCCoE practice guide built with 24 vendors, demonstrating 19 example ZTA implementations with configuration detail and mappings to the NIST CSF and SP 800-53r5. Released as a high-level PDF and a full web document. Use it to show the architecture is buildable with commercial products and to map controls.
- Project page: https://www.nccoe.nist.gov/zerotrust
- High-level PDF: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1800-35.pdf

### CISA Zero Trust Maturity Model v2.0 (April 2023)
Five pillars (Identity, Devices, Networks, Applications & Workloads, Data), three cross-cutting capabilities (Visibility & Analytics, Automation & Orchestration, Governance), and four maturity stages (Traditional, Initial, Advanced, Optimal). Written for US federal agencies but CISA recommends it to all organisations. Use it to score the baseline and set per-pillar targets.
https://www.cisa.gov/zero-trust-maturity-model
*Note: as of September 2026 the CISA page is marked "Archived Content". The model remains the most widely used maturity reference; check for a successor before citing it as current policy.*

### NSA Zero Trust Implementation Guidelines (ZIGs), January 2026
A Primer plus Discovery, Phase One and Phase Two guidelines covering 42 target-level capabilities and 91 activities, aligned to the Department of War (formerly DoD) CIO ZT Framework and NIST SP 800-207. The Discovery Phase is about establishing visibility of data, applications, assets and services and of access activity before implementing controls — the template for our Phase 2.
- Discovery Phase: https://media.defense.gov/2026/Jan/08/2003852321/-1/-1/0/CTR_ZIG_DISCOVERY_PHASE.PDF
- Phase One: https://media.defense.gov/2026/Jan/30/2003868308/-1/-1/0/CTR_ZIG_PHASE_ONE.PDF
- Primer and Phase Two: NSA Cybersecurity Advisories & Guidance — https://www.nsa.gov/Press-Room/Cybersecurity-Advisories-Guidance/

### DoD / Department of War CIO Zero Trust Strategy and Reference Architecture
The capability and activity catalogue that the NSA ZIGs implement. Useful for architects who want the full activity list; heavier than most enterprises need.
https://dodcio.defense.gov/Library/

## United Kingdom

### NCSC — Zero Trust Architecture collection
Eight design principles: know your architecture; know your user, service and device identities; assess user behaviour, device and service health; use policies to authorise requests; authenticate and authorise everywhere; focus monitoring on users, devices and services; don't trust any network, including your own; choose services designed for zero trust. Includes a board-level *Introduction to zero trust* — the recommended executive pre-read.
https://www.ncsc.gov.uk/collection/zero-trust-architecture

## Mainland China

### GB/T 43696-2024 — Cybersecurity technology: Zero trust reference architecture (网络安全技术 零信任参考体系架构)
China's first national standard for zero trust; published 25 April 2024, effective 1 November 2024, under TC260. It is a recommended (GB/T) standard, not a legal requirement. Use it as the reference for mainland operations, local suppliers and procurement language. Purchase via the national standards service.
- Standard record: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=C166002FE253A840E56BEBF13B4945E7
- National library entry: https://ndls.org.cn/standard/detail/1addd8501c44f04f9ab7eb255f218595

### Binding obligations that affect a ZT design
Adopting GB/T 43696 does not by itself meet any legal obligation. The obligations that bite in mainland China come from the Cybersecurity Law, the Multi-Level Protection Scheme (MLPS 2.0, GB/T 22239-2019), the Data Security Law and the Personal Information Protection Law (PIPL). ZT depends on central telemetry about users and devices; sending that data from the mainland to a global SIEM or policy engine may be a cross-border transfer of personal information. Take legal advice before designing where telemetry is processed and stored.

### Related standards to track
- 20250865-T-469 — Zero trust capability maturity model and evaluation method (national standard in development; the Chinese counterpart to a maturity model).
- YD/T 6853-2026 — Zero-trust-based security requirements for telecom network management plane (industry standard).
- Industry-standard index: https://std.samr.gov.cn/hb/search/stdHBDetailed?id=108B29E37A3FB367E06397BE0A0AAFC2

## Hong Kong

No dedicated Hong Kong zero trust standard was found. ZT is best positioned as the architecture that helps meet existing expectations:
- **HKMA Practice Guide on Cloud Adoption (January 2026)** — applies to authorised institutions; expanded from four to eight cloud domains, relevant to hybrid and multi-cloud access control. https://brdr.hkma.gov.hk/eng/doc-ldg/docId/getPdf/20260108-3-EN/20260108-3-EN.pdf
- **HKMA C-RAF 2.0** — cyber resilience assessment framework for banks (if the organisation or its clients are HKMA-regulated).
- **Protection of Critical Infrastructures (Computer Systems) Ordinance** — implementation from 2026; relevant if any entity is designated as a critical infrastructure operator.
- **Personal Data (Privacy) Ordinance (PDPO)** — access telemetry about staff is personal data; relevant to what is collected and where it is sent.

## United Kingdom — privacy

Access telemetry (sign-in behaviour, device data, location) is personal data under UK GDPR and the Data Protection Act 2018. Carry out a data protection impact assessment before pilots that add monitoring. ICO guidance: https://ico.org.uk/for-organisations/

## Secondary / vendor references

Useful for engineers; not authoritative for the briefing.
- Google BeyondCorp (origin of the modern ZT model): https://cloud.google.com/beyondcorp
- Microsoft Zero Trust guidance centre: https://learn.microsoft.com/security/zero-trust/
- Cloud Security Alliance, Zero Trust research: https://cloudsecurityalliance.org/research/topics/zero-trust

### Microsoft Zero Trust playbook and roadmap material

> **Proviso:** This is vendor guidance. It is a well-structured worked example of the NIST SP 800-207 decision/enforcement pattern, but its roadmap steps assume Microsoft products (Entra ID, Intune, Purview, Defender, Sentinel). Use it for structure, stakeholder material and sequencing ideas, not as the programme's framework spine and not as a product selection. Map any step taken from it back to the CISA ZTMM pillar and NSA ZIG activity it serves. Organisations that are mostly on another cloud or identity platform should read it alongside that vendor's equivalent (for example Google BeyondCorp) to keep the brief vendor-neutral.

| Resource | What it is | How we might use it |
|---|---|---|
| [Zero Trust adoption framework](https://learn.microsoft.com/en-us/security/zero-trust/adopt/zero-trust-adoption-overview) | Business-leader playbook: objectives, phased approach, progress tracking, ready-to-present slides | Borrow executive framing and the stakeholder slide for the briefing |
| [Rapid Modernization Plan (RaMP) checklists](https://learn.microsoft.com/en-us/security/zero-trust/user-access-productivity-validate-trust) | Prioritised deployment checklists with steps and project roles | Source of candidate quick wins when choosing pilots |
| [Zero Trust Workshop](https://learn.microsoft.com/en-us/security/zero-trust/workshop-zero-trust-overview) and [Assessment](https://microsoft.github.io/zerotrustassessment/) | Four-phase workshop (kickoff, optional assessment, roadmap, closeout) and a posture assessment tool | Optional input to discovery where the Microsoft stack is in scope |
| [Align adoption with Zero Trust frameworks](https://learn.microsoft.com/en-us/security/zero-trust/security-zero-trust-frameworks) | Microsoft's mapping of its adoption model to industry frameworks, including The Open Group Zero Trust Reference Model | Answers "how does the Microsoft approach relate to the standards?" |

## Maintenance

Re-check links and versions quarterly; links and 2026 publication details above were last checked in September 2026 and should be re-verified before external use. Watch for: a CISA ZTMM successor, NSA Phase Three/Four ZIGs, final publication of the Chinese ZT maturity model standard.
