# Architecture — SOX §302 Disclosure Controls skill

## Shape

The skill is a router + chunk architecture. `SKILL.md` is the always-loaded router (≤300 lines); `chunks/` holds 7 on-demand deep-dives (≤200 lines each). Industry views (`industries/`) and use cases (`use-cases/`) provide sector-specific and engagement-specific framing. Tests, telemetry, and data complete the package.

```
skills/sox-302-disclosure-controls/
├── SKILL.md                    # router, §1-§11 contract, §10 citation manifest, §11 routing table
├── README.md                   # consumer one-pager
├── chunks/                     # 7 deep-dive files (01-07), all ≤200 lines
│   ├── 01-section-302-overview.md
│   ├── 02-dcp-vs-icfr.md
│   ├── 03-the-six-certifications.md
│   ├── 04-evaluation-and-disclosure.md
│   ├── 05-section-302-vs-404.md
│   ├── 06-disclosure-committee-subcert.md
│   └── 07-material-weakness-and-change.md
├── industries/                 # 4 sector views + _index.md
│   ├── _index.md
│   ├── saas-technology.md
│   ├── financial-services.md
│   ├── healthcare.md
│   └── manufacturing.md
├── use-cases/                  # 3 worked examples + _index.md
│   ├── _index.md
│   ├── uc-01-mw-interplay.md
│   ├── uc-02-newly-public-first-302.md
│   └── uc-03-multientity-subcert.md
├── data/
│   ├── seeds/                  # uc-01/02/03 self-contained inputs + expected outputs
│   └── registry/              # citations.json — the §10 manifest labels
├── tests/                      # test files + deterministic stub
│   ├── sox_302_disclosure_controls_stub.py
│   ├── test_sox_302_disclosure_controls_oracle.py
│   ├── test_sox_302_disclosure_controls_grounding.py
│   ├── test_sox_302_disclosure_controls_trace.py
│   ├── test_sox_302_disclosure_controls_metamorphic.py
│   ├── test_sox_302_disclosure_controls_adversarial.py
│   ├── test_sox_302_disclosure_controls_telemetry.py
│   └── test_sox_302_disclosure_controls_chunks.py
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

Chunk 02 (DC&P vs. ICFR) and chunk 05 (§302 vs. §404 boundary) carry the two definitional distinctions the skill exists to teach; chunk 06 isolates the disclosure committee and sub-certification cascade — labeled recommended practice / house framework everywhere — so any reader can see the rule/practice line in one place.

Packaging note: the test suite (including the fact-sheet inventory-diff test) runs from the
full repo checkout — an installed copy of `skills/sox-302-disclosure-controls/` alone cannot
run it (the fact sheet lives in repo-root `docs/`).

## Derivability-oracle pattern (SOX-637)

Every oracle test in `tests/test_sox_302_disclosure_controls_oracle.py` **recomputes the
expected answer independently from the seed files** and asserts the stub agrees — no expected
number is echoed from the stub's own code path, and footing invariants (summaries equal
recounts) are asserted on every output table. Concretely:

- UC-01: the §302 DC&P effectiveness conclusion is re-derived from the seed material-weakness
  facts (13a-15(e) / Item 307: an unremediated MW in a disclosure-relevant area ⇒ "not
  effective"); the ¶5 disclosure-to-auditors trigger (15 U.S.C. 7241(a)(5)) and the
  sub-certification cascade roll-up (clean + exceptions = total) are recomputed from the seed,
  not read from the stub.
- UC-02: the newly-public obligations are re-derived from the seed filer status — §302 always
  applies (no newly-public/EGC exemption); §404(b) auditor attestation is exempt for a
  newly-public filer / EGC; the DC&P scope (all disclosure items) is recomputed strictly
  broader than the ICFR scope (financial subset) directly from the disclosure inventory.
- UC-03: the multi-entity cascade coverage and gap list are re-derived from the entity roster,
  and the FPI annual-vs-domestic-quarterly DC&P-evaluation split (13a-15(b)) is recomputed and
  footed against the entity total.

The stub (`sox_302_disclosure_controls_stub.py`) is a deterministic reference implementation —
it computes, it never echoes fixture numbers. The seed + oracle pair is the contract; the UC
docs were written TO the passing fixtures (process v3 rule 2).

## Standing fact-sheet inventory-diff test

`docs/sox-302-disclosure-controls-fact-sheet.md` (repo root `docs/`) carries a machine-readable
§0 YAML block: the structural counts (6 certification elements, 6 numbered cert paragraphs, 2
signing officers, 4 core implementing rules, 3 Reg S-K items) plus the identifier list with
exact section refs. `test_fact_sheet_inventory_diff` parses that block in CI and asserts:

- the stated counts (`certification_elements_302a`, `cert_paragraphs_in_exhibit`,
  `signing_officers`, `implementing_rules_core`, `reg_sk_items`) match the skill's spine; and
- the core identifiers (17 CFR 240.13a-15(e), 240.13a-15(f), 15 U.S.C. 7241, Reg S-K Item 307)
  are all present in the sheet's identifier list.

Because the fact sheet lives in-repo, this is a **standing Tier 1 gate**, not a one-time
check: any drift between chunk-stated structure and the mechanically transcribed statute/eCFR
inventory fails CI.

## No crosswalk rows in v1

`data/` encodes **no crosswalk rows** in v1 (`crosswalks: []` in the fact sheet §0). The
natural cross-references are to **coso-internal-controls** (the §404/ICFR skill — the §302↔§404
boundary) and to **nist-csf-2 / hipaa** for the cyber-8-K Item 1.05 DC&P touchpoint. These are
one-way prose references only; the skill asserts no mapping row. Row-level encoding (if any) is
deferred to a later pass.

## Cross-skill architecture

- `coso-internal-controls` — the §404/ICFR assessment + auditor-attestation mechanics; this
  skill references the §302↔§404 boundary and the DC&P⊃ICFR relationship, it does not re-teach
  §404 (one-way; no restated §404 facts)
- `nist-csf-2` / `hipaa-security-rule` — the cyber 8-K Item 1.05 DC&P timeliness touchpoint
  (non-financial timely disclosure), labeled overlap, not equivalence
- `audit-workpapers` — evidence/documentation citation style

## Context budget

All figures are pre-baseline estimates (no instrumented run yet — see `telemetry/baseline.md`);
they mirror the SKILL.md frontmatter `context_budget` block:

- Always-loaded (router only): 3,500 tokens (estimate)
- Per-call typical: 7,000 tokens — router + 1 chunk + 1 industry + 1 UC (estimate)
- Per-call max: 15,000 tokens — router + all chunks + industry + UC (estimate)
- Per-call p90: 9,000 tokens (estimate — no instrumented baseline yet)
