# Zero Trust Building Blocks and Indicative Baseline

*Companion text for the two-page deck: [Zero Trust — Building Blocks Brief](https://claude.ai/artifact/TGfovH9dRaLXBWSBkZJZXM)*

## Page 1 — The building blocks

### The core model (NIST SP 800-207)

```
  Signals ─────────────► Policy Decision Point (PDP)
  identity, device,       policy engine + policy administrator
  threat intel, logs,              │ allow / deny / step-up
  data labels                      ▼
  Subject ─────────────► Policy Enforcement Point (PEP) ─────────► Resource
  user, device,           ZTNA / proxy, API gateway,               apps, APIs, data,
  workload                service mesh, host agent                 cloud workloads
```

Every request is evaluated; the network location of the subject grants no trust. Access is granted per session, with least privilege, and re-evaluated as signals change.

### Operating principles

1. Network location grants no trust.
2. Least privilege, granted per session.
3. Verify continuously, not once at login.
4. Assume breach; limit blast radius.

### Pillars and cross-cutting capabilities (CISA ZTMM v2.0)

| Pillar | What "good" looks like (Advanced/Optimal direction) |
|---|---|
| Identity | Phishing-resistant MFA; continuous identity risk evaluation; just-in-time privileged access |
| Devices | Complete asset inventory; device health checked at every access decision |
| Networks | Micro-segmentation; encrypted internal traffic; application-level access instead of network-level |
| Applications & workloads | Per-request authorisation at app and API; workload identity; secure software supply chain |
| Data | Continuous data inventory; automated classification; labels drive access and DLP |

Cross-cutting: **visibility & analytics**, **automation & orchestration**, **governance**.

### Mapping common products to ZT roles

| ZT role | Typical enterprise components |
|---|---|
| Policy decision point | IdP conditional access engine, ZTNA controller, authorisation service (e.g. OPA-style) |
| Policy enforcement point | ZTNA / identity-aware proxy, SASE/SSE gateway, API gateway, service mesh sidecar, host firewall/agent |
| Identity signals | IdP, PAM, identity governance, workload identity (SPIFFE-style) |
| Device signals | MDM/UEM, EDR, certificate-based device identity |
| Data signals | Classification/labelling, DLP, data security posture management |
| Analytics | SIEM, UEBA, SOAR |

## Page 2 — What we probably have vs. what ZT adds

*Indicative view of a typical enterprise. It is a hypothesis to test in discovery, not an assessment.*

| Building block | What we probably have | What zero trust adds | Status |
|---|---|---|---|
| Identity | SSO, MFA for most users | Phishing-resistant MFA, PAM, JIT | Partial |
| Devices | MDM and EDR on corporate endpoints | Posture checked at every access | Partial |
| Networks | Perimeter firewall, VPN, flat LAN | ZTNA instead of VPN; micro-segments | Gap |
| Apps & workloads | WAF, CI/CD scans, cloud guardrails | Per-request authZ; service identity | Partial |
| Data | Email DLP, partial data labels | Data inventory; labels drive access | Gap |
| Visibility & analytics | SIEM, central logs, SOC | Risk signals fed to policy engine | Partial |
| Automation & governance | Policies, annual access reviews | Policy-as-code, auto-response, owner | Gap |

**Ask:** sponsor a 6–8 week discovery to replace this indicative view with the real baseline, then choose two or three pilots.

## Discovery questions to validate the baseline

| Pillar | Questions |
|---|---|
| Identity | What share of users and admins use phishing-resistant MFA? How many service accounts, and who owns them? Is privileged access standing or just-in-time? |
| Devices | Is there one authoritative asset inventory? Can the IdP see device health at sign-in? How are unmanaged and third-party devices handled? |
| Networks | Which applications are reachable only via VPN or internal network? How flat are internal zones? Is east-west traffic encrypted and logged? |
| Apps & workloads | Which apps do their own authorisation, and which rely on the network? Do workloads have identities, or shared secrets? |
| Data | Where are the crown-jewel data sets? Are labels applied, and do any access decisions use them? |
| Visibility & analytics | Which signals reach the SIEM in near real time? Can any of them change an access decision automatically? |
| Automation & governance | Who owns ZT? Are access policies written down as code or as documents? How are exceptions tracked? |

## Sources

NIST SP 800-207; CISA ZTMM v2.0; NSA Zero Trust Implementation Guidelines (2026); NCSC Zero Trust Architecture design principles. Full list: [02-authoritative-resources.md](02-authoritative-resources.md).
