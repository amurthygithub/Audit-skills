# Data — hipaa-security-rule

- `seeds/` — UC fixtures. The seed + oracle pair is the contract: UC documents are written
  to these fixtures, and `tests/test_hipaa_security_rule_oracle.py` recomputes every expected
  number independently (derivability oracles — nothing is echoed).
- `generators/` — deterministic CLIs (`--seed`) that emit the register/inventory seeds. The
  spec and standard tables they vendor are diffed against
  `docs/hipaa-security-rule-fact-sheet.md` §0 by
  `tests/test_hipaa_security_rule_oracle.py::test_fact_sheet_inventory_diff` — the standing
  inventory-diff gate.
- `crosswalks/` — the complete Security Rule -> SP 800-53 Rev 5.1.1 mapping, generated from
  the NIST CPRT extraction (SOX-638; see `crosswalks/README.md` for provenance). The CSF
  mapping in the same CPRT data targets CSF v1.1 only and is deliberately not encoded.

No file in this directory contains PHI/ePHI — org-level synthetic facts only. Dates used in
computations come from `as_of_date` seed fields, never the wall clock.

Packaging note: the test suite (including the fact-sheet inventory-diff) runs from the full
repo checkout; an installed copy of `skills/hipaa-security-rule/` alone cannot run it.
