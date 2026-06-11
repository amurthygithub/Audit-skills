# Architecture — FedRAMP Cloud Authorization skill

## Shape

The skill is a router + chunk architecture. `SKILL.md` is the always-loaded router (≤300 lines); `chunks/` holds 8 on-demand deep-dives (≤200 lines each). Industry views (`industries/`) and use cases (`use-cases/`) provide sector-specific and engagement-specific framing. Tests, telemetry, and data complete the package.

```
skills/fedramp-authorization/
├── SKILL.md                    # router, §1-§11 contract, §10 citation manifest, §11 routing table
├── README.md                   # consumer one-pager
├── chunks/                     # 8 deep-dive files (01-08), all ≤200 lines
│   ├── 01-fedramp-and-governance.md
│   ├── 02-impact-levels-and-baselines.md
│   ├── 03-authorization-paths.md
│   ├── 04-the-authorization-package.md
│   ├── 05-assessment-and-inheritance.md
│   ├── 06-continuous-monitoring.md
│   ├── 07-poam-and-risk.md
│   └── 08-fedramp-20x-and-modernization.md
├── industries/                 # 4 sector views + _index.md
│   ├── _index.md
│   ├── saas-technology.md
│   ├── public-sector.md
│   ├── financial-services.md
│   └── healthcare.md
├── use-cases/                  # 3 worked examples + _index.md
│   ├── _index.md
│   ├── uc-01-moderate-agency-ato.md
│   ├── uc-02-li-saas-readiness.md
│   └── uc-03-third-party-assessment.md
├── data/
│   ├── seeds/                  # uc-01/02/03 self-contained inputs + expected outputs
│   ├── generators/             # deterministic --seed CLIs for the eval sampler
│   └── crosswalks/             # empty in v1 (baselines ARE 800-53 controls — identity, not a mapping)
├── tests/                      # test files + deterministic stub
│   ├── fedramp_authorization_stub.py
│   ├── test_fedramp_authorization_oracle.py
│   ├── test_fedramp_authorization_grounding.py
│   ├── test_fedramp_authorization_trace.py
│   ├── test_fedramp_authorization_metamorphic.py
│   ├── test_fedramp_authorization_adversarial.py
│   ├── test_fedramp_authorization_telemetry.py
│   └── test_fedramp_authorization_chunks.py
├── telemetry/                  # 4 instrumentation files
│   ├── schema.json
│   ├── instrument.py
│   ├── redaction.md
│   └── baseline.md
└── docs/                       # governance docs
    ├── architecture.md         # this file
    ├── limits-and-disclaimers.md
    ├── changelog.md
    └── acceptance-gate.md
```

## The 8 chunks: what each carries

| # | File | Role |
|---|------|------|
| 01 | `01-fedramp-and-governance.md` | What FedRAMP is; the 2022 Authorization Act (44 U.S.C. 3607-3616); the **statutory FedRAMP Board (§3610), NOT the JAB**; OMB M-24-15 (rescinds the 2011 memo); the program-layer-on-800-53 framing |
| 02 | `02-impact-levels-and-baselines.md` | **The spine + the boundary.** FIPS 199 categorization (CIA high-water mark → Low/Moderate/High); the 4 baselines with exact counts (156/323/410/156, base+enh); how FedRAMP tailors **up** from 800-53B (149/287/370); LI-SaaS Tailored (66 tested + 90 attested); the same 800-53 control IDs — boundary vs `nist-800-53-rmf` |
| 03 | `03-authorization-paths.md` | The **current** path: Agency Authorization (operative Rev 5); multi-agency; single-authorization + **presumption of adequacy** (M-24-15); **JAB P-ATO retired**; FedRAMP Ready → full assessment → ATO; the authorizing official |
| 04 | `04-the-authorization-package.md` | The package: **SSP** (the "security blueprint," CSP-authored), **SAP** (3PAO plan), **SAR** (3PAO results), **POA&M** (CSP corrective-action plan); who authors what; how they sequence; attachments |
| 05 | `05-assessment-and-inheritance.md` | The 3PAO: independent assessor; **A2LA** accreditation to **ISO/IEC 17020** (Type A or C; Type B prohibited); SAP → testing & sampling → SAR → risk + recommendation; **control inheritance / leveraging** (inherited controls not re-tested by the leveraging CSP) |
| 06 | `06-continuous-monitoring.md` | **ConMon** = monthly cadence; the three objectives (operational visibility / managed change control / incident response); monthly submission (updated POA&M, inventory, vuln scans); **remediation SLAs 30/90/180 days**; reassessment |
| 07 | `07-poam-and-risk.md` | **POA&M lifecycle**: SAR deficiency → POA&M item; severity → SLA; the three **deviation-request** types (False Positive / Risk Adjustment / Operational Requirement); how POA&M drives ConMon and re-authorization; the AO risk-acceptance role |
| 08 | `08-fedramp-20x-and-modernization.md` | **FedRAMP 20x (emerging — labeled):** automation-first, outcome-based; **Key Security Indicators (KSIs)**; **machine-readable packages**; OSCAL artifacts; what is settled (Rev 5) vs direction (20x) |

The two concepts consumers most often get wrong each get a dedicated chunk: the categorization → baseline-count logic and the 800-53 boundary live in **02**; the current-vs-retired-JAB governance lives in **01/03**. ConMon (06) and POA&M (07) are split because the deviation-request mechanics and severity SLAs are substantial enough to crowd the ConMon cadence content. 20x (08) is isolated so its "direction, not rule" caveat is unambiguous.

## Router vs. chunks: when each loads

- **SKILL.md** loads always (≤300 lines). It's the routing table — it answers "what does the user want?" and points to the right chunk(s) via §11.
- **chunks/** load on demand. The router's §11 table maps user intent → chunk path.
- **industries/** load on demand when the engagement sector is known.
- **use-cases/** load on demand. Each UC is a self-contained worked example with full input / procedure / expected output / derivability oracle.

## Contract-first / derivability-oracle design (SOX-637)

The seed + oracle pair is the **contract**, and the UC docs are written TO the passing fixtures (process v3 rule 2). Every oracle test in `tests/test_fedramp_authorization_oracle.py` **recomputes the expected answer independently from the seed files** and asserts the stub agrees — no expected number is echoed from the stub's own code path. Concretely:

- **UC-01:** the overall FIPS 199 impact is re-derived as `max(C, I, A)` over the high-water-mark ordering (Low < Moderate < High); the selected baseline's control count is looked up from the overall level (Low 156 / Moderate 323 / High 410 — **not** hardcoded to one value); each SAR finding's POA&M remediation due-date is recomputed as `identified_date + severity_SLA` (high/critical 30, moderate 90, low 180 days).
- **UC-02:** LI-SaaS eligibility is derived from `overall_impact == "Low" AND saas_delivery`; the 66-tested / 90-attested Tailored split is the fixed framework split (cited to the Tailored LI-SaaS baseline doc).
- **UC-03:** findings are recomputed as the controls the CSP **owns** (`tested AND not passed AND not inherited`); the POA&M item count = `len(findings)`; inherited-and-failed controls are excluded (they belong to the provider's package and POA&M); the severity roll-up and the residual-high risk note are recomputed from the finding set.

The stub (`fedramp_authorization_stub.py`) is a deterministic reference implementation — it computes, it never echoes fixture numbers. The baseline totals (156/323/410, 66/90) are framework **constants** taken from the PMO-authored OSCAL Rev 5 profiles; the *derivation* is the seed-driven selection/computation, not the constants.

## The 800-53 boundary

`data/crosswalks/` encodes **no crosswalk rows** in v1 (`crosswalks: []` in the fact sheet §0). FedRAMP does not maintain a separate control catalog: its Low/Moderate/High baselines ARE NIST SP 800-53 Rev 5 controls (the same IDs), tailored up from the 800-53B 149/287/370 baselines. The "mapping" is therefore identity + tailoring, not a framework-to-framework crosswalk. The natural cross-reference is one-way to **nist-800-53-rmf** (the control catalog + the general RMF), referenced from chunk 02; this skill cites the boundary and does not re-teach the catalog. A per-control baseline listing (300+ rows per baseline) is out of scope for v0.1.0.

## Metamorphic and adversarial coverage

- **Metamorphic** (`test_..._metamorphic.py`): raising any single FIPS 199 objective to High flips the overall impact to High and the baseline count to 410; marking a failed control `inherited` removes it from the CSP's POA&M; finding-order is invariant.
- **Adversarial** (`test_..._adversarial.py`): a missing FIPS 199 fact yields an `INSUFFICIENT_INPUT` refusal rather than a fabricated baseline; Moderate+SaaS is **not** LI-SaaS-eligible (it takes the full Moderate baseline); the JAB is never named as a current authorizer; 20x is labeled emerging; an inherited finding is excluded; the empty control set is handled.

## Cross-skill architecture

- `nist-800-53-rmf` — the 800-53 Rev 5 control catalog + general RMF; this skill references the "FedRAMP baselines are tailored 800-53 controls" boundary one-way from chunk 02, it does not re-teach the catalog (no restated catalog facts, no shared data)
- `hipaa-security-rule` — health-tech CSP: the FedRAMP + HIPAA control-family overlap (pointer in chunk 05 / `industries/healthcare.md`)
- `nist-csf-2` — general cyber posture feeding the SSP narrative (pointer in chunk 01)
- `aicpa-soc-reporting` — SOC 2 as the adjacent commercial assurance vs FedRAMP's federal authorization (one-line contrast in chunk 01)

## Context budget

All figures mirror the SKILL.md frontmatter `context_budget` block; the p90 is a pre-baseline estimate (no instrumented run yet — see `telemetry/baseline.md`):

- Always-loaded (router only): 3,800 tokens
- Per-call typical: 7,500 tokens — router + 1 chunk + 1 industry + 1 UC
- Per-call max: 17,000 tokens — router + all chunks + industry + UC
- Per-call p90: 9,500 tokens (estimate — no instrumented baseline yet)
