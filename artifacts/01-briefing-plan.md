# Zero Trust Adoption — Enterprise Briefing Plan

*Draft v0.1 · September 2026*

## 1. Purpose

Give the enterprise a shared, standards-based understanding of zero trust (ZT) and secure a decision to start: an executive sponsor, a funded discovery phase, and agreement on how pilots will be chosen.

The briefing deliberately frames ZT as an **architecture and operating model**, not a product. Most of the building blocks are things the enterprise already buys; the change is making them feed one policy decision for every access request (NIST SP 800-207).

## 2. Outcomes we want from the briefing

1. Leadership can explain ZT in one sentence and recognises the core model (subject → enforcement point → decision point → resource).
2. Agreement that our starting point is **partial**: good point products, weak integration.
3. A named executive sponsor and a ZT programme owner.
4. Approval for a 6–8 week discovery phase aligned to the NSA Zero Trust Implementation Guideline *Discovery Phase*.
5. Agreed criteria for choosing two or three pilots after discovery.

## 3. Audiences and formats

| Audience | Format | Length | Material |
|---|---|---|---|
| Board / ExCo | Executive brief | 15 min | Two-page deck, one decision |
| CIO, CISO, heads of infrastructure, apps, data | Working session | 60–90 min | Deck + [03-building-blocks-and-baseline.md](03-building-blocks-and-baseline.md) + discovery scope |
| Architects and engineers | Technical deep dives (per pillar) | 2 × 90 min | NIST SP 1800-35 example builds, CISA ZTMM functions, NSA ZIG activities |
| Risk, compliance, legal | Alignment session | 45 min | Jurisdiction mapping (US/UK/CN/HK) from [02-authoritative-resources.md](02-authoritative-resources.md) |

## 4. Plan

### Phase 0 — Prepare (weeks 1–2)

- Confirm sponsor candidate and the one decision the executive brief will ask for.
- Select the reference framework spine: **NIST SP 800-207** for concepts, **CISA ZTMM v2.0** for maturity scoring, **NSA ZIGs** for phased activities. Add **NCSC principles** (UK operations) and **GB/T 43696-2024** (mainland China operations and suppliers) as regional overlays.
- Pre-read for leadership: NCSC *Introduction to zero trust* (short, board-friendly).
- Tailor slide 2 (baseline) with whatever is already known — in a private copy.

### Phase 1 — Brief (week 3)

- Executive brief (15 min) using the two-page deck.
- Working session with technology leadership (agenda below).

### Phase 2 — Discovery (weeks 4–10)

Aligned to the NSA ZIG Discovery Phase, which focuses on visibility of data, applications, assets and services (DAAS) and of access activity. Work items:

- Inventory crown-jewel data, applications and services; map who and what accesses them, from where.
- Identity inventory: workforce, privileged, third-party, service accounts and workload identities.
- Device inventory and posture coverage (managed, unmanaged, BYOD, OT/IoT if in scope).
- Network flows between zones; remote access paths (VPN, jump hosts, vendor access).
- Telemetry available to a policy engine today (IdP risk, EDR, SIEM, DLP).
- Score each pillar against CISA ZTMM v2.0 stages (Traditional → Initial → Advanced → Optimal).

### Phase 3 — Target state and roadmap (weeks 10–14)

- Target maturity per pillar for 12 and 36 months (pillars may progress at different speeds).
- Choose two or three pilots using the criteria in section 7.
- Cost, dependencies, and integration points (the PDP/PEP pattern for each pilot).

### Phase 4 — Decision (week 15)

- Return to ExCo with baseline, target, pilots and funding request.

## 5. Working-session agenda (90 min)

| Time | Topic |
|---|---|
| 0:00 | Why now — threat drivers, cloud and remote work, regulatory expectations |
| 0:10 | The model — NIST 800-207 logical components (slide 1) |
| 0:25 | Five pillars and three cross-cutting capabilities (CISA ZTMM v2.0) |
| 0:40 | Indicative baseline — what we probably have vs. what ZT adds (slide 2); challenge and correct it live |
| 1:00 | How others implemented it — NIST SP 1800-35 example builds |
| 1:10 | Discovery scope, owners, data needed |
| 1:25 | Decisions and next steps |

## 6. Key messages

1. ZT is a strategy for making access decisions per request, not a product you buy.
2. We are not starting from zero — identity, endpoint, SIEM and cloud controls are foundations to connect.
3. Discovery comes first: you cannot write policy for assets and flows you have not inventoried.
4. Progress pillar by pillar; small, measurable pilots beat a big-bang programme.
5. One framework spine, regional overlays — so the same programme satisfies Western and Chinese expectations.

## 7. Pilot selection criteria

A good first pilot is high-value, contained, and visible: it touches a real risk, needs no more than two pillars, and has an owner willing to change. Typical candidates to test against these criteria: replacing VPN with ZTNA for one user group or third-party access; phishing-resistant MFA plus just-in-time access for administrators; isolating one crown-jewel application behind an identity-aware proxy with device posture checks.

## 8. Risks and pitfalls to raise in the briefing

| Pitfall | Mitigation |
|---|---|
| Vendor-led "ZT in a box" | Anchor on NIST/CISA; map products to PDP/PEP roles, not the reverse |
| Boiling the ocean | Pillar-by-pillar maturity targets; two or three pilots |
| Identity debt (stale accounts, shared service accounts) | Clean-up is part of discovery, not a later project |
| Legacy and OT that cannot authenticate | Enclave them behind an enforcement point; document exceptions |
| Cross-border differences (HK / UK / mainland) | Regional overlay in the resource map; legal review of telemetry and logging |
| User friction | Measure login friction and helpdesk tickets in pilots |

## 9. Decisions to request

1. Executive sponsor and programme owner named.
2. Discovery phase approved (scope, 6–8 weeks, named contributors from infra, apps, data, IAM).
3. Framework spine agreed (NIST 800-207 + CISA ZTMM + NSA ZIG, with NCSC and GB/T overlays).

## 10. Deliverables

| Deliverable | Where |
|---|---|
| Two-page executive deck | [Deck link](https://claude.ai/artifact/TGfovH9dRaLXBWSBkZJZXM) (export to `/deck`) |
| Resource map | [02-authoritative-resources.md](02-authoritative-resources.md) |
| Building blocks and baseline | [03-building-blocks-and-baseline.md](03-building-blocks-and-baseline.md) |
| Discovery templates | `/discovery` (to create) |
| Organisation-specific baseline and roadmap | **Private** repository only |
