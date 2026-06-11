# Data — pci-dss-assessment

- `seeds/` — UC fixtures. The seed + oracle pair is the contract: the oracle test
  recomputes every expected value independently from the seed facts (derivability;
  nothing echoed).
- `generators/` — deterministic CLIs (`--seed`): `gen_system_inventory.py` (UC-02 CDE-tagged
  inventory) and `gen_saq_cases.py` (SAQ-selection boundary cases, oracle-labeled via the stub
  for the eval sampler).
- `crosswalks/` — **empty in v1.** The authoritative PCI↔CSF/800-53 mapping is the NIST OLIR
  reference (PCI-DSS-4.0.1-to-CSF-v2.0); row-level encoding is a later ticket (the OLIR
  extraction method is already proven). No rows asserted here.

No file contains real PAN/CHD/SAD — synthetic org-level facts only; full PAN is never shown
(a data-handling teaching point of the skill). Dates come from `as_of_date` seed fields.

Packaging note: the test suite (incl. the fact-sheet inventory-diff) runs from the full repo
checkout; an installed copy of `skills/pci-dss-assessment/` alone cannot run it.
