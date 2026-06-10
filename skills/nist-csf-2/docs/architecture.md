# Architecture — NIST CSF 2.0 skill

## Shape

The skill is a router + chunk architecture. `SKILL.md` is the always-loaded router (≤300 lines); `chunks/` holds 8 on-demand deep-dives (≤200 lines each). Industry views (`industries/`) and use cases (`use-cases/`) provide sector-specific and engagement-specific framing. Tests, telemetry, and data complete the package.

```
skills/nist-csf-2/
├── SKILL.md                    # router, 12 sections, §11 routing table
├── README.md                   # consumer one-pager
├── chunks/                     # 8 deep-dive files (01-08), all ≤200 lines
│   ├── 01-functions-categories.md
│   ├── 02-tiers-and-profiles.md
│   ├── 03-current-profile.md
│   ├── 04-target-profile-and-gap.md
│   ├── 05-govern-function.md
│   ├── 06-enterprise-reporting.md
│   ├── 07-implementation-playbook.md
│   └── 08-informative-references-crosswalk.md
├── industries/                 # 4 sector views + _index.md
│   ├── _index.md
│   ├── financial-services.md
│   ├── public-sector.md
│   ├── saas-technology.md
│   └── manufacturing.md
├── use-cases/                  # 3 worked examples + _index.md
│   ├── _index.md
│   ├── uc-01-first-organizational-profile.md
│   ├── uc-02-board-maturity-report.md
│   └── uc-03-csf-to-800-171-cmmc-l2.md
├── data/                       # generators + seeds (Wave 4)
│   ├── generators/
│   └── seeds/
├── tests/                      # 7 test files + stub
│   ├── nist_csf_2_stub.py
│   ├── test_nist_csf_2_oracle.py
│   ├── test_nist_csf_2_grounding.py
│   ├── test_nist_csf_2_trace.py
│   ├── test_nist_csf_2_metamorphic.py
│   ├── test_nist_csf_2_adversarial.py
│   ├── test_nist_csf_2_telemetry.py
│   └── test_nist_csf_2_chunks.py
├── telemetry/                  # 4 instrumentation files
│   ├── schema.json
│   ├── instrument.py
│   ├── redaction.md
│   └── baseline.md
├── docs/                       # 4 governance docs
│   ├── architecture.md         # this file
│   ├── limits-and-disclaimers.md
│   ├── changelog.md
│   └── acceptance-gate.md
└── assets/                     # (optional) radar/board templates if needed
```

## Router vs. chunks: when each loads

- **SKILL.md** loads always (≤300 lines, 239 currently). It's the routing table — it answers "what does the user want?" and points to the right chunk(s).
- **chunks/** load on demand. Each chunk's `load_when` frontmatter field declares the triggers. The router's §11 table maps user intent → chunk path.
- **industries/** load on demand. The user (or the router) reads an industry file when the engagement sector is known.
- **use-cases/** load on demand. Each UC is a self-contained worked example with full input/procedure/oracle shape.

## Cross-skill architecture

CSF 2.0 is a *bridge* skill — it's the framework most likely to be the *first* one a practitioner encounters (especially at executive level), and it hand-offs to:

- `nist-800-53-rmf` — when the engagement is federal/DoD/FedRAMP, or when the practitioner needs the control-by-control depth of 800-53
- `aicpa-soc-reporting` — when SOC 2 is in the picture (common for SaaS and financial services)
- `isaca-audit-methodology` — for the auditor-lens view (especially in financial services and manufacturing)
- `coso-internal-controls` — for SOX 404 work (financial services)
- `audit-workpapers` — for the 5-part C-C-C-E-R finding format and the workpaper structure

The 8 chunks' "Cross-references" sections and the industries' "Cross-references" sections make these hand-offs explicit. The `chunks/08-informative-references-crosswalk.md` chunk is the central artifact: it has the CSF↔800-53, CSF↔800-171, CSF↔ISO 27001, and CSF↔HIPAA mappings.

## Context budget

Always-loaded (router only): ~2,000-2,500 tokens
Per-chunk (loaded on demand): 800-1,500 tokens
Per-call typical: 2,500-4,000 tokens (router + 1-2 chunks)
Per-call max: 8,000-10,000 tokens (router + industry + 3-4 chunks)
