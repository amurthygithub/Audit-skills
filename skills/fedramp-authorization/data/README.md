# Data — fedramp-authorization

- `seeds/` — UC fixtures (UC-01/02/03 self-contained inputs + expected outputs). The seed + oracle
  pair is the contract: the oracle test recomputes every expected value independently from the seed
  facts (derivability; nothing echoed). UC-01 carries per-objective FIPS 199 + SAR findings with
  identified dates (POA&M deadlines); UC-02 a low-impact SaaS offering + the `saas_delivery` flag;
  UC-03 a control-test set with passed / inherited / severity tags.
- `generators/` — deterministic CLIs (`--seed`) that emit cases for the eval sampler:
  - `gen_fips199.py` — CIA-objective triples (per-objective Low/Moderate/High) for the
    categorization → high-water-mark → baseline metamorphic cases.
  - `gen_control_results.py` — control-test sets (passed / inherited / severity) for the UC-03-style
    SAR finding roll-up cases.
  Content is fixed; `--seed` is a marker (the oracle recomputes the answer either way). No external
  dependencies.
- `crosswalks/` — empty in v1. FedRAMP baselines ARE NIST SP 800-53 Rev 5 controls (the same IDs),
  tailored — the relationship is identity + tailoring, not a framework-to-framework mapping, so there
  are no crosswalk rows to assert. The 800-53 boundary is a one-way prose reference to
  `nist-800-53-rmf`.

The Rev 5 baseline totals the stub uses (Low **156** / Moderate **323** / High **410** / LI-SaaS
**156** = 66 tested + 90 attested) are framework constants counted directly from the PMO-authored
OSCAL Rev 5 baseline profiles (fact sheet §0); the *derivation* the oracles check is the seed-driven
selection / computation (the high-water-mark categorization, the baseline lookup, each POA&M
due-date, the inheritance-aware finding roll-up), not the constants.

No file contains real FedRAMP package data — fictional CSPs/systems (Acme Cloud Suite, Beacon Forms,
Example 3PAO) and structural facts only; no real system names, IP addresses, or vulnerability data.
Dates (POA&M deadlines) come from the seed `identified_date` / `as_of_date` fields — there is no
wall-clock dependence. Source text is US-government public-domain (the FedRAMP Authorization Act, OMB
M-24-15, fedramp.gov, NIST SP 800-53 Rev 5); the baseline counts are anchored to the OSCAL Rev 5
profiles on the OSCAL-Foundation/fedramp-resources mirror.
