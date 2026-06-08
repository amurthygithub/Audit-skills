# Data — nist-csf-2 skill

## Layout

```
data/
├── README.md            # this file
├── generators/
│   └── gen_profile.py   # deterministic seed generator
└── seeds/
    ├── uc-01-input.json
    ├── uc-02-input.json
    └── uc-03-input.json
```

## Seeds

The 3 seed JSONs are the canonical inputs to the 3 use cases. They are **fictional but representative** engagements:

- **uc-01-input.json** — DataRelay Inc. (50-FTE Series-A SaaS) first Organizational Profile
- **uc-02-input.json** — Pinecrest National Bank ($20B regional bank) board maturity report
- **uc-03-input.json** — Apex Manufacturing (240-FTE DoD supplier) CMMC L2 readiness

The seeds are committed so the test suite is reproducible without running the generator.

## Generator

`gen_profile.py` is a deterministic Python script that produces the 3 seed JSONs. It is invoked only when:

- Bootstrapping a new UC (UC-04, UC-05, etc.)
- Regenerating seeds after a schema change
- Adapting the seeds to a real engagement (modify the script to accept overrides)

Run from the repo root:

```bash
python3.11 skills/nist-csf-2/data/generators/gen_profile.py
```

## Crosswalks (Wave 3)

The `data/crosswalks/` directory (referenced in chunks/01, 05, 08) will be populated in Wave 3 with the full CSF 2.0 Informative References mappings:

- `csf-to-800-53-mod.json` — Subcategory → 800-53 Rev 5.1.1 control (49 rows verified in Wave 1 chunk/08)
- `csf-to-800-171-r3.json` — Subcategory → NIST 800-171 Rev 3 control
- `csf-to-iso27001-2022.json` — Subcategory → ISO 27001:2022 Annex A control
- `csf-to-hipaa.json` — Subcategory → HIPAA Security Rule §164.30X safeguard (Wave 3)
- `csf-2-0-subcategories.json` — canonical 106-Subcategory inventory

The chunks/ in Wave 1 already reference these by path with "(added in Wave 2)" disclaimers. The Wave 3 work creates the actual files.

## Schemas

Each seed is a JSON document. The structure is described in the corresponding use case file:

- `use-cases/uc-01-first-profile.md` for `uc-01-input.json` input schema
- `use-cases/uc-02-board-report.md` for `uc-02-input.json` input schema
- `use-cases/uc-03-c-t-to-800-53.md` for `uc-03-input.json` input schema

The stub (`tests/nist_csf_2_stub.py`) accepts any dict; the UC-specific input fields are optional with sensible defaults. The oracle tests (`tests/test_nist_csf_2_oracle.py`) assert specific output fields per UC.

## Anti-hallucination

- All org names (DataRelay Inc., Pinecrest National Bank, Apex Manufacturing) are fictional
- All FTE, asset, and dollar figures are illustrative
- All regulatory citations (OCC §III.C.3, NY DFS §500.11, FFIEC CAT Domain 4) are real citations to real regulations; the *application* of those citations to the specific scenarios is illustrative
- The 800-171 Rev 3 control IDs (3.x.x format) are real; the specific mapping to CSF 2.0 Subcategories in the crosswalk is illustrative and should be verified against the current NIST IR spreadsheet before use in a client deliverable
