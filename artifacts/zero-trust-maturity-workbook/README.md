# Zero Trust Maturity Workbook

Self-assessment against the CISA Zero Trust Maturity Model v2.0, with a generated improvement roadmap. Plain Excel: no macros, no external links.

| File | Purpose |
|---|---|
| `Zero-Trust-Maturity-Workbook.xlsx` | Blank copy to fill in. Row ID-1 holds one example rating to show the expected format; replace it. |
| `Zero-Trust-Maturity-Workbook-example.xlsx` | Same workbook with **made-up, illustrative ratings** so the summary, chart and roadmap can be seen working. Not a real assessment of any organisation. |
| `source/ztdata.py` | Question bank: 40 CISA functions plus the 9-function payments appendix, stage descriptions, improvement actions and prerequisites. |
| `source/build_workbook.py` | Generates both workbooks from the question bank (`python3 build_workbook.py <output-dir>`, needs `openpyxl`). Open the result in Excel, or recalculate with LibreOffice, to populate formula values. |

## Tabs

| Tab | What it does |
|---|---|
| Start here | How to use the workbook, colour legend, how the roadmap is built, sources and caveats |
| Settings | Organisation, date, default target stage (Advanced), whether Appendix A joins the roadmap, low-priority delay, editable wave labels |
| Assessment | 40 functions across Identity, Devices, Networks, Applications and Workloads, Data and the cross-cutting capabilities. Inputs: current stage, target override, priority, applicable, owner, evidence. Calculated: scores, gap, status, next step and the wave it lands in |
| Appendix A Payments | Optional treasury and payments overlay (transaction step-up, beneficiary changes, systems of record, maker-checker, SWIFT CSCF 2.4A and 2.9, bank portals, limit changes, joined fraud detection). Scored separately and excluded from the core maturity figures |
| Summary | Overall and per-area maturity, gap to target, chart, roadmap steps per wave |
| Maturity map | Every function on one grid: stage reached today and stages planned up to target |
| Roadmap | Ordered improvement steps by wave, then priority, then framework order |
| Roadmap steps | Calculation sheet behind the roadmap |

## How the roadmap is built

- Every stage between a function's current stage and its target becomes one step, using the action written for that stage move.
- A function's first step goes in wave 1 (0–6 months), the next in wave 2 (6–12 months), and so on. Low-priority functions start one wave later; this is configurable.
- Steps wait for prerequisites. For example, device-based resource access (DV-3) waits until device compliance (DV-1) and authentication (ID-1) reach the same stage, or their own target if that is lower. The "Waiting on" column names the prerequisite that pushed a step later.
- Anything past four waves lands in the last wave. Waves are a sequencing aid, not a costed plan.

## Caveats

- Stage descriptions are paraphrased summaries written for this workbook; the improvement actions are design recommendations, not CISA text. Check the [CISA Zero Trust Maturity Model v2.0](https://www.cisa.gov/zero-trust-maturity-model) for the full criteria before reporting results externally.
- Keep filled-in copies out of this public repository; an organisation's real ratings, gaps and evidence belong in a private store.

## Status

Draft v0.1, October 2026.
