# Data — sox-302-disclosure-controls

- `seeds/` — UC fixtures. The seed + oracle pair is the contract: the oracle test recomputes
  every expected value independently from the seed facts (derivability; nothing echoed).
- `generators/` — deterministic CLIs (`--seed`): `gen_subcert_cascade.py` (multi-entity
  sub-cert / coverage cases for the eval sampler).
- `crosswalks/` — empty in v1 (the §404/ICFR boundary is a one-way prose reference to
  coso-internal-controls; no rows asserted).

No file contains MNPI or real EDGAR data — fictional issuers and structural facts only. Dates
come from `as_of_date` seed fields. Source text is US federal public-domain (statute + eCFR);
verbatim extracts are vendored at `docs/builds/sox-570/sec-source-extracts.json`.
