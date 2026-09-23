# Zero Trust Building Blocks and Indicative Baseline

*Companion text for the five-slide deck: [Zero Trust — Building Blocks Brief](zero-trust-building-blocks-brief/) (open `deck.html`; live copy on claude.ai). This file covers slides 2 and 3 in full; slides 1, 4 and 5 are summarised at the end.*

## Slide 1 — Why now (summary)

Attackers log in rather than break in, and a trusted internal network lets them spread. Four drivers: stolen credentials and phishing; lateral movement and ransomware; work has left the perimeter (SaaS, cloud, remote staff, suppliers); regulators and insurers ask for evidence. Before presenting, add the organisation's own exposure: incidents or near misses, open audit findings, cyber insurance conditions, cost of one day of outage.

## Slide 2 — The building blocks

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

The decision point becomes a critical dependency and a prime target. Design in break-glass access, a fail-open/fail-closed rule per resource class, and hardening of the identity provider from the start.

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
| Identity signals | IdP, PAM, identity governance, workload identity (SPIFFE-style), inventory of automated agents with delegated access |
| Device signals | MDM/UEM, EDR, certificate-based device identity |
| Data signals | Classification/labelling, DLP, data security posture management |
| Analytics | SIEM, UEBA, SOAR |

## Slide 3 — What we probably have vs. what ZT adds

*Indicative view of a typical enterprise. It is a hypothesis to test in discovery, not an assessment. "Likely stage" uses the CISA ZTMM scale (Traditional → Initial → Advanced → Optimal) so it carries straight into discovery scoring.*

| Building block | What we probably have | What zero trust adds | Likely stage |
|---|---|---|---|
| Identity | SSO, MFA for most users | Phishing-resistant MFA, PAM, JIT | Initial |
| Devices | MDM and EDR on corporate endpoints | Posture checked at every access | Initial |
| Networks | Perimeter firewall, VPN, flat LAN | ZTNA instead of VPN; micro-segments | Traditional |
| Apps & workloads | SaaS behind SSO, WAF, cloud guardrails | Per-request authZ; SaaS session controls | Initial |
| Data | Email DLP, partial data labels | Data inventory; labels drive access | Traditional |
| Non-human & supplier access | Shared service accounts; supplier VPN | Workload identity; brokered, time-bound access | Traditional |
| Visibility & analytics | SIEM, central logs, SOC | Risk signals fed to policy engine | Initial |
| Automation & governance | Policies, annual access reviews | Policy-as-code, auto-response, owner | Traditional |

We ask leadership to accept this view as plausible enough to justify discovery, not to agree the scores.

## Discovery questions to validate the baseline

| Pillar | Questions |
|---|---|
| Identity | What share of users and admins use phishing-resistant MFA? How many service accounts, and who owns them? Is privileged access standing or just-in-time? |
| Devices | Is there one authoritative asset inventory? Can the IdP see device health at sign-in? How are unmanaged and third-party devices handled? |
| Networks | Which applications are reachable only via VPN or internal network? How flat are internal zones? Is east-west traffic encrypted and logged? |
| Apps & workloads | Which apps do their own authorisation, and which rely on the network? Do workloads have identities, or shared secrets? Which SaaS apps hold crown-jewel data, and can we control sessions in them? |
| Data | Where are the crown-jewel data sets? Are labels applied, and do any access decisions use them? |
| Non-human & supplier access | How many service accounts, API keys and automated agents exist, and who owns each? How do suppliers connect today, and is their access time-bound? |
| Visibility & analytics | Which signals reach the SIEM in near real time? Can any of them change an access decision automatically? |
| Automation & governance | Who owns ZT? Where are access decisions made today (IdP, VPN, firewalls, cloud IAM, apps), and who owns each? Are access policies written down as code or as documents? How are exceptions tracked? |
| Resilience & privacy | What happens to access if the IdP is unavailable? Is there tested break-glass access? Which access telemetry is personal data, and where is it stored by jurisdiction? |

## Slide 4 — The ask (summary)

Three decisions today: (1) name a sponsor and one accountable programme owner; (2) approve a 6–8 week discovery scoped to crown-jewel data and services, with effort and budget stated; (3) adopt one framework backbone — NIST SP 800-207 for the model and CISA ZTMM for scoring, with regional standards as references. In parallel, one no-regret step: phishing-resistant MFA and just-in-time access for administrators.

## Slide 5 — How we will know it is working (summary)

- **Discovery is done when** crown jewels are inventoried with who and what can reach them; each pillar is scored with evidence; a target design names which system makes the access decision; two or three pilots are chosen with success measures.
- **A pilot succeeds when** [__]% of the pilot group reach the resource only through the new decision point; standing admin rights in scope fall to [__]; sign-in friction and helpdesk tickets stay flat or fall; it ships in about 90 days with one user group and one resource set.
- **Designed in from day one:** break-glass access and IdP resilience; a hardened IdP; privacy and cross-border review of access telemetry (PIPL, UK GDPR, HK PDPO).

## Sources

NIST SP 800-207; CISA ZTMM v2.0; NSA Zero Trust Implementation Guidelines (2026); NCSC Zero Trust Architecture design principles. Full list: [02-authoritative-resources.md](02-authoritative-resources.md).
