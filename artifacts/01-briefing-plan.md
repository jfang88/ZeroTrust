# Zero Trust Adoption — Enterprise Briefing Plan

*Draft v0.2 · September 2026*

## 1. Purpose

Give the enterprise a shared, standards-based understanding of zero trust (ZT) and secure a decision to start: an executive sponsor, a funded discovery phase, and an agreed framework backbone.

The briefing deliberately frames ZT as an **architecture and operating model**, not a product. Most of the building blocks are things the enterprise already buys; the change is making them feed one policy decision for every access request (NIST SP 800-207).

The briefing leads with **risk, not architecture**: why the current perimeter model fails the way attacks now happen, and what that exposure means for this organisation.

## 2. Outcomes we want from the briefing

1. Leadership can explain ZT in one sentence and recognises the core model (a subject's request passes through an enforcement point, which asks a decision point, before reaching a resource).
2. Leadership accepts the indicative baseline as **plausible enough to justify discovery**. We are not asking them to agree the scores; discovery produces those.
3. The three decisions in section 9 are taken.
4. One no-regret improvement starts in parallel with discovery (section 9).

## 3. Audiences and formats

| Audience | Format | Length | Material |
|---|---|---|---|
| Board / ExCo | Executive brief | 15 min | Five-slide deck; the three decisions in section 9 |
| CIO, CISO, heads of infrastructure, apps, data | Working session | 60–90 min | Deck + [03-building-blocks-and-baseline.md](03-building-blocks-and-baseline.md) + discovery scope |
| Architects and engineers | Technical deep dives (per pillar) | 2 × 90 min | NIST SP 1800-35 example builds, CISA ZTMM functions, NSA ZIG activities |
| Risk, compliance, legal | Alignment session | 45 min | Jurisdiction mapping (US/UK/CN/HK) from [02-authoritative-resources.md](02-authoritative-resources.md) |
| Privacy, HR and (where relevant) works councils | Alignment session | 45 min | What telemetry ZT collects about staff, where it is stored, cross-border transfer |
| Application and business-unit owners | Briefing | 30 min | What changes for their apps and users; pilot candidates |
| Finance | Briefing | 30 min | Discovery cost; how the week-15 funding request will be built |

End users are not briefed at this stage; pilot communications are planned with each pilot.

## 4. Plan

### Phase 0 — Prepare (weeks 1–2)

- Confirm the sponsor candidate and the three decisions the executive brief will ask for.
- Propose the framework backbone: **NIST SP 800-207** for the model and vocabulary, **CISA ZTMM v2.0** for maturity scoring. Use the **NSA ZIGs** as an activity checklist (not a second backbone; they are written for defence and are heavier than most enterprises need), **NCSC principles** for UK operations and **GB/T 43696-2024** for mainland China operations and suppliers. Where sources differ, NIST and CISA decide. Note that the CISA ZTMM page is marked "Archived"; check for a successor before the brief.
- Gather the organisation's own "why now" evidence for slide 1: incidents and near misses, open audit findings, cyber insurance conditions, rough cost of an outage of a critical service.
- Estimate discovery effort (person-weeks, any external support) and cost for slide 4.
- Pre-read for leadership: NCSC *Introduction to zero trust* (short, board-friendly).
- Tailor slide 3 (baseline) with whatever is already known — in a private copy.

### Phase 1 — Brief (week 3)

- Executive brief (15 min) using the five-slide deck.
- Working session with technology leadership (agenda below), and the alignment sessions in section 3.
- Start the no-regret step: phishing-resistant MFA and just-in-time access for administrators.

### Phase 2 — Discovery (weeks 4–10, 7 weeks)

Aligned to the NSA ZIG Discovery Phase, which focuses on visibility of data, applications, assets and services (DAAS) and of access activity. **Scoped to crown-jewel data and services**, not the whole estate, so that the timebox is realistic; the rest of the estate is inventoried later, pillar by pillar. Work items:

- Inventory crown-jewel data, applications and services, including SaaS; map who and what accesses them, from where.
- Identity inventory: workforce, privileged, third-party, service accounts, workload identities and automated agents with delegated access.
- Device inventory and posture coverage (managed, unmanaged, BYOD; OT/IoT where it touches crown jewels).
- Network flows between zones; remote access paths (VPN, jump hosts, supplier access).
- Telemetry available to a policy engine today (IdP risk, EDR, SIEM, DLP), and where that telemetry is stored by jurisdiction.
- Today's decision points: list every place an access policy is enforced (IdP conditional access, VPN, firewalls, cloud IAM, app-level roles) and who owns each.
- Score each pillar against CISA ZTMM v2.0 stages (Traditional → Initial → Advanced → Optimal) using a written rubric; every score cites evidence.

**Exit criteria.** Discovery is done when:
1. Crown-jewel data, apps and services are inventoried, with who and what can reach them.
2. Each pillar is scored, with evidence behind every score.
3. The inputs for the target decision-point design (Phase 3) are complete.
4. A long list of pilot candidates is tested against the criteria in section 7.

### Phase 3 — Target state and roadmap (weeks 11–14)

In this order:

1. **Target decision-point design.** Decide which system is authoritative for access decisions (typically the IdP's conditional access engine, extended by ZTNA and API-level policy), how today's separate enforcement points will consult it, who owns policy, and how exceptions are governed. Pilots must plug into this design; this is what stops them becoming new silos.
2. **Resilience and privacy by design.** Break-glass access if the IdP or decision point fails; the fail-open/fail-closed rule per resource class; IdP hardening; where telemetry is processed and stored per jurisdiction (section 8).
3. Target maturity per pillar for 12 and 36 months (pillars may progress at different speeds).
4. Choose two or three pilots using the criteria in section 7, each with success measures.
5. Cost, dependencies and integration points for each pilot.

### Phase 4 — Decision (week 15)

- Return to ExCo with baseline, target design, pilots, success measures and funding request.

## 5. Working-session agenda (90 min)

| Time | Topic |
|---|---|
| 0:00 | Why now — our own exposure and the threat drivers (slide 1) |
| 0:10 | The model — NIST 800-207 logical components (slide 2) |
| 0:25 | Five pillars and three cross-cutting capabilities (CISA ZTMM v2.0) |
| 0:35 | Indicative baseline (slide 3); challenge and correct it live |
| 0:50 | Where access decisions are made today, and who owns them |
| 1:00 | How others implemented it — NIST SP 1800-35 example builds |
| 1:10 | Discovery scope, owners, data needed, exit criteria (slide 5) |
| 1:25 | Decisions and next steps (slide 4) |

## 6. Key messages

1. ZT is a strategy for making access decisions per request, not a product you buy.
2. Attackers now log in rather than break in; a trusted internal network lets one stolen login become a company-wide incident.
3. We are not starting from zero — identity, endpoint, SIEM and cloud controls are foundations to connect into one decision point.
4. Discovery comes first: you cannot write policy for assets and flows you have not inventoried. One no-regret step (admin MFA and just-in-time access) does not need to wait.
5. Progress pillar by pillar; small, measurable pilots beat a big-bang programme.
6. One framework backbone with regional references, so the programme *aligns with* expectations in the US, UK, Hong Kong and mainland China. ZT supports compliance; it does not by itself satisfy any regulation.

## 7. Pilot selection criteria

A good first pilot is **high-value, contained, visible and measurable**:

- It reduces a real, named risk.
- It covers **one user group and one resource set**. (Pilots will usually touch several pillars — identity, devices and network together is normal — so scope is limited by users and resources, not by pillar count.)
- It plugs into the target decision-point design rather than adding a new, separate policy engine.
- It can ship in about 90 days, has an owner willing to change, and has success measures agreed before it starts.

Typical candidates to test against these criteria: replacing VPN with ZTNA for one user group or for third-party access; isolating one crown-jewel application behind an identity-aware proxy with device posture checks; brokered, time-bound supplier access to one system.

## 8. Risks and pitfalls to raise in the briefing

| Pitfall | Mitigation |
|---|---|
| Vendor-led "ZT in a box" | Anchor on NIST/CISA; map products to PDP/PEP roles, not the reverse |
| Boiling the ocean | Crown-jewel discovery scope; pillar-by-pillar targets; two or three pilots |
| Pilots become new silos | Target decision-point design comes before pilot selection (Phase 3) |
| IdP / decision point becomes a single point of failure and the top target | Break-glass accounts, fail-open/fail-closed rule per resource class, IdP hardening and monitoring |
| Identity debt (stale accounts, shared service accounts, unmanaged automated agents) | Clean-up is part of discovery, not a later project |
| Legacy and OT that cannot authenticate | Enclave them behind an enforcement point; document exceptions |
| Access telemetry is personal data and may cross borders (mainland China, Hong Kong, UK) | Privacy and legal review in Phase 3; regional processing or storage where required (PIPL, UK GDPR, HK PDPO) |
| Ownership conflict between IAM, network, apps and data teams | One accountable programme owner; RACI agreed in Phase 3 |
| User friction | Measure sign-in friction and helpdesk tickets in pilots |
| Momentum lost during 15 weeks of analysis | Start the no-regret admin step in week 3 |

## 9. Decisions to request

From the executive brief (slide 4):

1. **Executive sponsor and programme owner named.** One owner accountable across IAM, network, apps and data.
2. **Discovery phase approved.** Crown-jewel scope, 6–8 weeks, named contributors from infra, apps, data and IAM; effort [__ person-weeks] and budget [__].
3. **Framework backbone agreed.** NIST SP 800-207 for the model and CISA ZTMM for scoring; NSA ZIG, NCSC and GB/T 43696 as references.

In parallel (no decision beyond normal change approval): phishing-resistant MFA and just-in-time access for administrators.

## 10. Success measures

| Stage | Measure |
|---|---|
| Discovery | Exit criteria in Phase 2 met by week 10 |
| No-regret step | Share of admin accounts on phishing-resistant MFA; standing admin rights removed |
| Each pilot | [__]% of the pilot group reach the resource only through the new decision point; standing admin rights in scope fall to [__]; sign-in friction and helpdesk tickets flat or better; shipped in ~90 days |
| Programme | Pillar scores against the 12- and 36-month targets, re-scored every six months with evidence |

Bracketed targets are set during discovery.

## 11. Deliverables

| Deliverable | Where |
|---|---|
| Five-slide executive deck | [artifacts/zero-trust-building-blocks-brief](zero-trust-building-blocks-brief/) (open `deck.html`); live copy on claude.ai |
| Resource map | [02-authoritative-resources.md](02-authoritative-resources.md) |
| Building blocks and baseline | [03-building-blocks-and-baseline.md](03-building-blocks-and-baseline.md) |
| Discovery templates and scoring rubric | `/discovery` (to create) |
| Organisation-specific baseline, target design and roadmap | **Private** repository only |
