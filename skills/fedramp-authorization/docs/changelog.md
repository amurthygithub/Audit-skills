# Changelog — FedRAMP Cloud Authorization skill

All notable changes to this skill are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [0.1.0] — 2026-06-11 — Initial release (SOX-574, born-vetted build, M5 cycle 4)

First FedRAMP skill built end-to-end under process v3: the Day 0 fact sheet
(`docs/fedramp-authorization-fact-sheet.md`, repo root — transcribed from public US-government text
and with the Rev 5 baseline counts counted directly from the PMO-authored OSCAL Rev 5 profiles)
preceded every content file; seed + derivability-oracle contracts were written before the UC docs;
G4.5 persona vetting and §5.11 live-source verification run inside the build PR (born-vetted, not
retrofitted). Two load-bearing facts are pinned everywhere: **FedRAMP baselines ARE tailored 800-53
Rev 5 controls** (not a separate catalog — `nist-800-53-rmf` owns it), and **the current authorizer
is the statutory FedRAMP Board, NOT the retired JAB**.

### Added

- `SKILL.md` router (§1-§11 contract, §10 citation manifest, §11 routing table) + `README.md`
- **8 chunks** (`chunks/01-08`): FedRAMP & governance (the 2022 Act / FedRAMP Board / M-24-15),
  impact levels & baselines (FIPS 199 high-water mark + the 4 baselines + the 800-53 boundary),
  authorization paths (Agency Authorization / presumption of adequacy / JAB retired), the
  authorization package (SSP/SAP/SAR/POA&M), 3PAO assessment & inheritance (A2LA / ISO 17020 /
  leveraging), continuous monitoring (monthly cadence / SLAs 30-90-180), POA&M & risk (lifecycle +
  the three deviation-request types), and FedRAMP 20x & modernization (labeled emerging direction)
- **4 industry views** (`industries/`): saas-technology (Moderate via Agency Authorization),
  public-sector (the sponsoring-agency / AO side), financial-services (the High baseline), healthcare
  (FedRAMP + HIPAA overlap)
- **3 use cases** (`use-cases/`): UC-01 SaaS FedRAMP Moderate via Agency Authorization (Acme Cloud
  Suite — categorization → 323 controls → POA&M deadlines by severity), UC-02 cloud-vendor LI-SaaS
  readiness (Beacon Forms — Low + SaaS → 156 controls, method-designated), UC-03 Big-4 3PAO assessment
  of a Moderate CSP (Example 3PAO — inheritance-aware finding roll-up → POA&M)
- `data/seeds/` (UC-01/02/03 self-contained inputs + expected outputs; no real package data; dates on
  POA&M-deadline computations) + `data/generators/` (`gen_fips199.py`, `gen_control_results.py` —
  deterministic `--seed` CLIs for the eval sampler); **no crosswalk rows** in v1 (baselines ARE
  800-53 controls — identity, not a mapping)
- Test suite + `fedramp_authorization_stub.py`: **contract-first** derivability oracles (SOX-637
  pattern — the stub computes from seed facts, never echoes), plus grounding, trace, metamorphic,
  adversarial, telemetry, and chunk smoke suites
- 4 telemetry files: `schema.json`, `instrument.py`, `redaction.md`, `baseline.md`
- 4 docs files: `architecture.md`, `limits-and-disclaimers.md`, `changelog.md`, `acceptance-gate.md`
  (seeded from the fact sheet's verified rows)
- Eval lane: `evals/fedramp-authorization/cases/` — the 3 UC substance cases + a categorization
  idempotence/invariant case, oracle-labeled, CI-enforced
- Registry citations: `FEDRAMP-ACT-2022`, `OMB-M-24-15`, `FEDRAMP-REV5-BASELINES`, `FEDRAMP-CONMON`,
  `FEDRAMP-PLAYBOOK`, `A2LA-3PAO`, `NIST-800-53R5`, `FIPS-199`

### Known deferrals

- Per-control baseline enumeration (300+ rows per baseline): out of scope in v1 — the counts
  (156/323/410/156, OSCAL-verified) and the tailoring relationship are encoded, not the full listing;
  the catalog itself is `nist-800-53-rmf`
- Crosswalk rows: none in v1 (the baselines ARE 800-53 controls — identity, not a mapping)
- DoD Impact Levels (IL2/4/5/6) / DISA SRG, GovRAMP (formerly StateRAMP), CMMC: named as adjacent regimes; not detailed
- Authoring a full SSP/SAR document: the skill explains the package + process; document drafting is a
  downstream use case, not a deliverable
- Currency: the Rev 5 baseline counts, the M-24-15 governance model, and the FedRAMP 20x track must
  be re-verified at every G4 pass — a later 800-53 maintenance release or a 20x RFC may have landed
  (NIST SP 800-53 is still Rev 5 — no Rev 6 — as of 2026-06)

## Sign-off

Built 2026-06-11 from the Day 0 fact sheet (gate PASS; licence class: public — machine-verifiable,
full vendoring permitted). The skill ships `status: draft` v0.1.0 pending Epic 6 reliability
measurement; the LLM-backed executor replaces the deterministic stub in a later slice.
