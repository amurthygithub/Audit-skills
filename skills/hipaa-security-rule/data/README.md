# Data — hipaa-security-rule

- `seeds/` — UC fixtures. The seed + oracle pair is the contract: UC documents are written
  to these fixtures, and `tests/test_hipaa_security_rule_oracle.py` recomputes every expected
  number independently (derivability oracles — nothing is echoed).
- `generators/` — deterministic CLIs (`--seed`) that emit the register/inventory seeds. The
  spec and standard tables they vendor are diffed against
  `docs/hipaa-security-rule-fact-sheet.md` §0 by
  `tests/test_hipaa_security_rule_oracle.py::test_fact_sheet_inventory_diff` — the standing
  inventory-diff gate.
- `crosswalks/` — **intentionally empty in v1.** The authoritative Security Rule ↔ NIST CSF /
  SP 800-53 mapping was moved out of SP 800-66r2 into the NIST CPRT (and maps to CSF v1.1,
  intentionally broad). Row-level encoding is tracked as SOX-638: extract from CPRT, verify
  per row, then encode in this skill and nist-800-53-rmf in the same pass.

No file in this directory contains PHI/ePHI — org-level synthetic facts only. Dates used in
computations come from `as_of_date` seed fields, never the wall clock.

Packaging note: the test suite (including the fact-sheet inventory-diff) runs from the full
repo checkout; an installed copy of `skills/hipaa-security-rule/` alone cannot run it.
