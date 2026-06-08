# Data — nist-800-53-rmf

Synthetic datasets and generators that drive the use cases and tests. Every dataset is **deterministic** (seeded) so test runs are reproducible.

## Layout

```
data/
  README.md                 # this file
  generators/               # Python CLI generators; --seed for reproducibility
    gen_fips199.py
    gen_sar_findings.py
    gen_crosswalk_gap.py
    gen_control_inventory.py
  seeds/                    # canonical fixtures (small/medium/large/edge)
    uc-01-input.json
    uc-01-crm.json
    uc-01-expected.json
    uc-02-input.json
    uc-02-findings.json
    uc-02-expected.json
    uc-03-input.json
    uc-03-gap-list.json
    uc-03-remediation.json
    uc-03-expected.json
  crosswalks/               # cross-framework mappings
    soc2-to-800-53-mod.json
    iso27001-2022-to-800-53.json
    hipaa-to-800-53.json
    pci-to-800-53.json
  controls/                 # raw control catalog (Rev 5) — small curated subset
    nist_800_53_mod_reduced.json
    nist_800_53_mod_325_count.json
```

## Data Dictionary

### `seeds/uc-01-input.json` — UC-01 FedRAMP SaaS input

| Field | Type | Description |
|-------|------|-------------|
| `system_name` | string | System identifier (kebab-case or human-readable) |
| `system_description` | string | Free-form description; redacted before telemetry |
| `information_types[]` | array | Each: `name`, `sp_800_60_info_type_code`, `description`, `cia_baseline` (c/i/a each ∈ LOW/MODERATE/HIGH), `rationale` |
| `downstream_consumers[]` | array of strings | Who consumes the system's data |
| `cloud_provider` | string | IaaS provider (AWS, Azure, GCP) + region/sovereignty |
| `cloud_fedramp_id` | string | Hyperscaler's FedRAMP package ID |
| `customer_responsibility_matrix` | string | Path to CRM fixture |

### `seeds/uc-01-crm.json` — UC-01 Customer Responsibility Matrix

| Field | Type | Description |
|-------|------|-------------|
| `controls[]` | array | Each: `control_id`, `status` (inherited / system-specific / hybrid), `source`, `narrative` |
| `inherited_provider` | string | Hyperscaler provider name |
| `inherited_fedramp_id` | string | Hyperscaler's FedRAMP package ID |

### `seeds/uc-01-expected.json` — UC-01 oracle target

The expected skill output. The oracle test compares the actual output to this.

### `seeds/uc-02-findings.json` — UC-02 SAR findings

22 finding objects, each: `finding_id`, `control_id`, `severity`, `determination`, `description`, `cause`, `effect`, `recommendation`, `compensating_control`, `remediation_plan`, `risk_acceptance_required`.

### `seeds/uc-03-gap-list.json` — UC-03 gap controls

94 gap controls, each: `control_id`, `gap_type`, `priority`, `owner`, `target_date`, `remediation_action`, `evidence_refs`.

### `crosswalks/soc2-to-800-53-mod.json` — SOC 2 ↔ 800-53

A bidirectional map. Each row: `soc2_id` (e.g., `CC6.1`), `nist_800_53_id` (e.g., `AC-2`), `mapping_strength` (exact / partial / contextual), `note`.

## Generation

All generators are deterministic. Example:

```bash
python data/generators/gen_fips199.py --seed 42 --system caseflow > data/seeds/uc-01-input.json
python data/generators/gen_sar_findings.py --seed 42 --n 22 --out data/seeds/uc-02-findings.json
python data/generators/gen_crosswalk_gap.py --seed 42 --out data/seeds/uc-03-gap-list.json
```

The seeds shipped in `seeds/` are the canonical fixtures; re-running the generator with the same seed produces byte-identical output.

## PII / NPI / PHI Redaction

Per `telemetry/redaction.md` and the Spine (skills/TEMPLATE):

- All generators strip free-form PII before persisting; no SSNs, no real names, no real account numbers.
- Free-form description fields use synthetic placeholders (e.g., "John Doe", "123-45-6789", "john.doe@example.com") that the redaction patterns catch deterministically.
- Structured IDs (control_id, finding_id, uc_id) are kept.

## How tests use the data

- `tests/test_oracle.py` — loads the `*-input.json`, runs the skill entrypoint (when implemented), compares to `*-expected.json` per the UC's `oracle` field.
- `tests/test_trace.py` — verifies that the skill's output cites the right `§X` of `SKILL.md` for each decision.
- `tests/test_metamorphic.py` — mutates the input in known ways and asserts the output mutates accordingly.
- `tests/test_adversarial.py` — feeds edge-case inputs and asserts the skill refuses or handles correctly.
- `tests/test_grounding.py` — verifies the in-body citations resolve to `## 10. References` of `SKILL.md`.
