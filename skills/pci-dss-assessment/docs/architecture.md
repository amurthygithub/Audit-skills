# Architecture — PCI DSS assessment skill

## Shape

The skill is a router + chunk architecture. `SKILL.md` is the always-loaded router (≤300 lines); `chunks/` holds 8 on-demand deep-dives (≤200 lines each). Industry views (`industries/`) and use cases (`use-cases/`) provide sector-specific and engagement-specific framing. Tests, telemetry, and data complete the package.

```
skills/pci-dss-assessment/
├── SKILL.md                    # router, §1-§11 contract, §10 citation manifest, §11 routing table
├── README.md                   # consumer one-pager
├── chunks/                     # 8 deep-dive files (01-08), all ≤200 lines
│   ├── 01-scope-and-applicability.md
│   ├── 02-scoping-and-segmentation.md
│   ├── 03-saq-selection.md
│   ├── 04-requirements-1-6.md
│   ├── 05-requirements-7-12.md
│   ├── 06-validation-roc-aoc.md
│   ├── 07-approaches-and-compensating-controls.md
│   └── 08-currency-and-program-context.md
├── industries/                 # 4 sector views + _index.md
│   ├── _index.md
│   ├── saas-technology.md
│   ├── retail-ecommerce.md
│   ├── financial-services.md
│   └── healthcare.md
├── use-cases/                  # 3 worked examples + _index.md
│   ├── _index.md
│   ├── uc-01-saq-selection.md
│   ├── uc-02-roc-segmentation.md
│   └── uc-03-compensating-control.md
├── data/
│   ├── generators/             # deterministic seed builders
│   ├── seeds/                  # uc-01/02/03 inputs + expected outputs (self-contained)
│   └── crosswalks/             # EMPTY in v1 — see "No crosswalk rows" below
├── tests/                      # test files + deterministic stub
│   ├── pci_dss_assessment_stub.py
│   ├── test_pci_dss_assessment_oracle.py
│   ├── test_pci_dss_assessment_grounding.py
│   ├── test_pci_dss_assessment_trace.py
│   ├── test_pci_dss_assessment_metamorphic.py
│   ├── test_pci_dss_assessment_adversarial.py
│   ├── test_pci_dss_assessment_telemetry.py
│   └── test_pci_dss_assessment_chunks.py
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
- **industries/** load on demand. The user (or the router) reads an industry file when the engagement sector is known (saas-technology, retail-ecommerce, financial-services, healthcare).
- **use-cases/** load on demand. Each UC is a self-contained worked example with full input/procedure/oracle shape.

Chunk 08 deliberately isolates the volatile content (version currency, the future-dated-now-in-force status, the SAQ catalog versions, OLIR crosswalk status, and card-brand program context) so re-verification at each G4 pass touches one file.

Packaging note: the test suite (including the fact-sheet inventory-diff test) runs from the
full repo checkout — an installed copy of `skills/pci-dss-assessment/` alone cannot run it
(the fact sheet lives in repo-root `docs/pci-dss-assessment-fact-sheet.md`).

## Derivability-oracle pattern (SOX-637)

Every oracle test in `tests/test_pci_dss_assessment_oracle.py` **recomputes the expected
answer independently from the seed files** and asserts the stub agrees — no expected value is
echoed from the stub's own code path, and footing invariants (in-scope + out-of-scope = total)
are asserted on every output. Concretely:

- UC-01: the SAQ path is re-derived from the payment-page architecture facts with the labeled
  house convention (service provider → ROC/SAQ-D-SP; merchant servers touch PAN → ROC; fully
  outsourced redirect/iframe to a compliant TPSP with no merchant script → SAQ A; merchant
  controls page scripts but servers never receive PAN → SAQ A-EP), and the client-side-script
  requirements (6.4.3 / 11.6.1) are re-derived from that path — never echoed from the stub.
- UC-02: the in-scope count (CDE + connected/security-impacting), out-of-scope count, and the
  customized-approach accept/reject split (Appendix D requires a documented Targeted Risk
  Analysis) are each recomputed from the seed inventory, with the footing invariant asserted.
- UC-03: the four-element compensating-control worksheet completeness (Appendix B/C) and the
  compensating-control-vs-customized-approach control-type classification (constraint-driven vs
  TRA-driven) are re-derived from the seed, and `len(WORKSHEET_ELEMENTS) == 4` is asserted.

The stub (`pci_dss_assessment_stub.py`) is a deterministic reference implementation — it
computes, it never echoes fixture values. The seed + oracle pair is the contract; the UC docs
were written TO the passing fixtures (process v3 rule 2). PCI is machine-verifiable against the
local licensed copy of the standard, but the routing decision (which SAQ, in/out of scope,
compensating vs customized) is the skill's own labeled engagement logic, not verbatim standard
text.

## Standing fact-sheet inventory-diff test

`docs/pci-dss-assessment-fact-sheet.md` (repo root `docs/`) carries a machine-readable §0
YAML block: every principal-requirement and SAQ identifier, plus the mechanical structural
counts. `test_fact_sheet_inventory_diff` parses that block in CI and asserts:

- 6 goals and 12 principal requirements, with all twelve `Req N` identifiers present and the
  numbers forming exactly `1..12`;
- the depth-3 (205) + depth-4 (44) defined-requirement counts foot to the 249 main-body total;
- all 10 SAQ types are present in the identifier list (the ticket's original 6-type list was
  incomplete — corrected to 10 at Day 0).

Because the fact sheet lives in-repo, this is a **standing Tier 1 gate**, not a one-time check:
any drift between chunk-stated inventory and the mechanically transcribed PDF inventory fails
CI.

## No crosswalk rows in v1 (OLIR pointer)

`data/crosswalks/` is intentionally empty. The authoritative PCI DSS v4.0.1 → CSF v2.0 mapping
is the NIST OLIR final informative reference "PCI-DSS-4.0.1-to-CSF-v2.0" (PCI SSC-submitted,
US-gov hosted). Row-level encoding is deferred: until it lands, the chunks point to the OLIR
program and the NIST CSF informative-references catalog **without asserting any row**, and the
skill never claims a PCI → CSF mapping of its own. This mirrors the HIPAA skill's CPRT/OLIR
deferral and uses the same proven extraction method when rows are added.

## Cross-skill architecture

- `nist-csf-2` — when its informative-reference views ship, they reference INTO the OLIR PCI →
  CSF anchor rather than restate PCI requirements (one-way; no restated facts)
- `nist-800-53-rmf` — no PCI crosswalk encoded; OLIR pointer only
- `aicpa-soc-reporting` — SOC 2 evidence reuse for service providers (labeled overlap, not
  equivalence — a SOC 2 report is not an AOC)
- `audit-workpapers` — evidence/documentation citation style

## Context budget

All figures are pre-baseline estimates (no instrumented run yet — see `telemetry/baseline.md`);
they mirror the SKILL.md frontmatter `context_budget` block:

- Always-loaded (router only): 3,500 tokens (estimate)
- Per-call typical: 7,000 tokens — router + 1 chunk + 1 industry + 1 UC (estimate)
- Per-call max: 16,000 tokens — router + all chunks + industry + UC (estimate)
- Per-call p90: 9,000 tokens (estimate — no instrumented baseline yet)
