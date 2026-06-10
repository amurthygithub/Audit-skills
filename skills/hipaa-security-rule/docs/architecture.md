# Architecture — HIPAA Security Rule skill

## Shape

The skill is a router + chunk architecture. `SKILL.md` is the always-loaded router (≤300 lines); `chunks/` holds 8 on-demand deep-dives (≤200 lines each). Industry views (`industries/`) and use cases (`use-cases/`) provide sector-specific and engagement-specific framing. Tests, telemetry, and data complete the package.

```
skills/hipaa-security-rule/
├── SKILL.md                    # router, §1-§11 contract, §10 citation manifest, §11 routing table
├── README.md                   # consumer one-pager
├── chunks/                     # 8 deep-dive files (01-08), all ≤200 lines
│   ├── 01-scope-and-general-rules.md
│   ├── 02-risk-analysis-and-management.md
│   ├── 03-administrative-safeguards.md
│   ├── 04-physical-safeguards.md
│   ├── 05-technical-safeguards.md
│   ├── 06-organizational-and-documentation.md
│   ├── 07-addressable-decisions-and-evidence.md
│   └── 08-enforcement-audit-and-nprm.md
├── industries/                 # 4 sector views + _index.md
│   ├── _index.md
│   ├── healthcare.md
│   ├── saas-technology.md
│   ├── financial-services.md
│   └── public-sector.md
├── use-cases/                  # 3 worked examples + _index.md
│   ├── _index.md
│   ├── uc-01-ba-risk-analysis.md
│   ├── uc-02-ocr-readiness.md
│   └── uc-03-baa-and-checklist.md
├── data/
│   ├── generators/             # gen_addressable_register.py, gen_control_inventory.py
│   ├── seeds/                  # uc-01/02/03 inputs, sub-seeds, expected outputs
│   └── crosswalks/             # EMPTY in v1 — see "No crosswalk rows" below
├── tests/                      # test files + deterministic stub
│   ├── hipaa_security_rule_stub.py
│   ├── test_hipaa_security_rule_oracle.py
│   ├── test_hipaa_security_rule_grounding.py
│   ├── test_hipaa_security_rule_trace.py
│   ├── test_hipaa_security_rule_metamorphic.py
│   ├── test_hipaa_security_rule_adversarial.py
│   ├── test_hipaa_security_rule_telemetry.py
│   └── test_hipaa_security_rule_chunks.py
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

## Router vs. chunks: when each loads

- **SKILL.md** loads always (≤300 lines). It's the routing table — it answers "what does the user want?" and points to the right chunk(s).
- **chunks/** load on demand. Each chunk's `load_when` frontmatter field declares the triggers. The router's §11 table maps user intent → chunk path.
- **industries/** load on demand. The user (or the router) reads an industry file when the engagement sector is known.
- **use-cases/** load on demand. Each UC is a self-contained worked example with full input/procedure/oracle shape.

Chunk 08 deliberately isolates the volatile content (penalty amounts, the 2025 NPRM, OCR enforcement posture) so re-verification at each G4 pass touches one file.

## Derivability-oracle pattern (SOX-637)

Every oracle test in `tests/test_hipaa_security_rule_oracle.py` **recomputes the expected
answer independently from the seed files** and asserts the stub agrees — no expected number
is echoed from the stub's own code path, and footing invariants (summaries equal recounts)
are asserted on every output table. Concretely:

- UC-01: risk bands are recomputed from `uc-01-risks.json` with the labeled house convention
  (likelihood × impact; Low ≤2 / Medium 3-4 / High ≥6), and the §164.306(d)(3) disposition per
  addressable spec is re-derived from the register's documented assessment without calling the
  stub's helper.
- UC-02: the 22-row readiness matrix, status counts, stale-document flags (seed `as_of_date`,
  never the wall clock), and the gap-priority rollup are each recomputed from the seeds.
- UC-03: the missing-BAA-provision list is re-derived against the regulatory provision set
  (§164.314(a)(2)(i)(A)-(C) + §164.308(b)(3)), and every checklist cite is checked against the
  fact-sheet identifier list so no CFR cite can be fabricated.

The stub (`hipaa_security_rule_stub.py`) is a deterministic reference implementation — it
computes, it never echoes fixture numbers. The seed + oracle pair is the contract; the UC docs
were written TO the passing fixtures (process v3 rule 2).

## Standing fact-sheet inventory-diff test

`docs/hipaa-security-rule-fact-sheet.md` (repo root `docs/`) carries a machine-readable §0
YAML block: every Subpart C identifier with its exact (R)/(A) designation, plus every count
under both matrix counting conventions. `test_fact_sheet_inventory_diff` parses that block in
CI and asserts:

- the 22-spec addressable register equals exactly the Addressable identifiers in the sheet;
- the 22-row control inventory equals exactly the Standard identifiers in the sheet;
- the per-family Required/Addressable counts foot to the family totals (21/8/7 specs), and the
  Appendix A conventions hold (18 standards / 36 titled specs; 42-entry convention).

Because the fact sheet lives in-repo, this is a **standing Tier 1 gate**, not a one-time
check: any drift between chunk-stated inventory and the mechanically transcribed eCFR
inventory fails CI.

## No crosswalk rows in v1 (CPRT, SOX-638)

`data/crosswalks/` is intentionally empty. The authoritative Security Rule → CSF → SP 800-53r5
mapping was removed from NIST SP 800-66r2 and placed online in the NIST Cybersecurity and
Privacy Reference Tool (CPRT); the published mapping targets **CSF v1.1 only** and is
"intentionally broad" per the 800-66r2 PDF. Row-level encoding is deferred to **SOX-638**
(extract from CPRT/OLIR, verify per-row, encode in this skill and `nist-800-53-rmf` in the
same pass). Until then the chunks point to CPRT and the OLIR program without asserting any
row, and the skill never claims an 800-66r2 mapping to CSF 2.0.

## Cross-skill architecture

- `nist-csf-2` — healthcare industry view references INTO this skill's chunks (one-way; no
  restated facts)
- `nist-800-53-rmf` — crosswalk placeholder only until SOX-638
- `aicpa-soc-reporting` — SOC 2 evidence reuse for BAs (labeled overlap, not equivalence)
- `audit-workpapers` — evidence/documentation citation style

## Context budget

Always-loaded (router only): ~2,000-2,500 tokens
Per-chunk (loaded on demand): 800-1,500 tokens
Per-call typical: 2,500-4,000 tokens (router + 1-2 chunks)
Per-call max: 8,000-10,000 tokens (router + industry + 3-4 chunks)
