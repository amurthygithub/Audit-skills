# Persona Review — hipaa-security-rule (G4.5 consumer-ready gate)

G4.5 born-vetted pass, run 2026-06-10 inside the build PR (SOX-572) per
`prompts/persona-vetting.md`. Wave 1 = persona vetting with 5 LLM persona agents (OCR
investigator, hospital CISO, health-tech SaaS compliance lead, solo consultant, Big 4
healthcare IT audit senior manager) + 3 clean-session consumer smoke tests (3/3 PASS or
PASS-WITH-NOTES) + the §5.11 live verification pass (CLEAN at CRITICAL/HIGH/MEDIUM; 5 LOW
notes, all resolved below). Every HIGH/MEDIUM finding was verified before fixing — Tier 1
(on-disk greps, seed/stub execution, identifier recounts) or Tier 2 (live sources with
verbatim quotes: eCFR 45 CFR 160.404 / Part 102 / Subpart C, Federal Register NPRM docket
RIN 0945-AA22 + the 2019 Notification of Enforcement Discretion, SP 800-66r2 PDF text on
disk). **LLM-vetted — a filter, not a certification.**

Resolution key: **FIXED** (this fix pass, branch `feat/SOX-572-hipaa-security-rule`) ·
**ACCEPTED** (with reason).

## Findings ledger

| # | sev | finding (abbreviated) | disposition |
|---|-----|----------------------|-------------|
| 1 | HIGH | Facility-disposition contradiction: chunk 04 said cloud BAs use the alternative-measure path for §164.310(a)(2)(i)–(iv) while UC-01/seeds disposition them not_reasonable_documented | FIXED — chunk 04 now states the distinguishing condition (operates-a-facility vs no organization-controlled facility); saas-technology.md aligned |
| 2 | HIGH | Phantom nist-csf-2 healthcare industry view claimed in 6 skill files + the design doc (no such file exists in skills/nist-csf-2/industries/) | FIXED — reframed everywhere: nist-csf-2 defers its healthcare view to its v1.0; when it ships it will reference into this skill |
| 3 | MED | UC-02 never said why §164.314(b) applies to Bellbrook | FIXED — self-funded group health plan sentence added in §1; mirrored in healthcare.md |
| 4 | MED | `alternative_considered` contract field (164.306(d)(3)(ii)(B)) missing from chunk 07 template and UC-01 §3 | FIXED — template field + one-sentence rule added; UC-01 §3/§5/oracle prose updated |
| 5 | MED | UC-03 item 8 wording implied MFA is a current Subpart C requirement | FIXED — row matches revised stub: own-identity authentication; MFA good practice, mandate NPRM-PROPOSED |
| 6 | MED | architecture.md token numbers contradicted SKILL.md frontmatter | FIXED — single set (3500/7000/16000/p90 9000), all labeled pre-baseline estimates |
| 7 | MED | Fact sheet §8 said "All 58 identifiers"; §0 contains 61 | FIXED — 61 with breakdown (22 standards + 36 matrix-titled specs + 3 §164.316(b)(2) documentation specs) |
| 8 | LOW | industries/_index.md "6,000-bed" (staff count, not beds) | FIXED — "6,000-staff" |
| 9 | LOW | README "26+ tests" stale | FIXED — 61 skill-local tests (plus root-level suites) |
| 10 | LOW | Penalty dollar amounts restated in limits-and-disclaimers.md | FIXED — single-sourced to chunk 08 (as-of 2026-06-10; 45 CFR 102.3 [CFR-45-102]) |
| 11 | LOW | data/crosswalks/ empty + untracked | FIXED — README added (intentionally empty in v1; CPRT; SOX-638) |
| 12 | LOW | §10 manifest: HIPAA-Security-Rule Title cell held an identifier; hhs.gov bot-wall undocumented in §10 | FIXED — proper title + bot-wall footnote |
| 13 | LOW | SRA Tool URL one 301 away from canonical | FIXED — registry + §10 now https://www.healthit.gov/privacy-security/security-risk-assessment-tool (200 direct, verified 2026-06-10) |
| 14 | LOW | SP 800-66r2 short title in registry/§10 | FIXED — official full title used |
| 15 | LOW | Quote hygiene: truncated sanction-policy quote (chunk 02); mid-quote capitalized "Terminate" (chunk 05) | FIXED — quote completed; logoff quote rephrased outside the quote |
| 16 | LOW | Chunk 07 "archive demonstrably reaches back 6 years" overstates for young entities | FIXED — full §164.316(b)(2)(i) retention window (back to entity inception if younger than 6 years) |
| 17 | LOW | Chunk 08 "document requests consistently lead with…" stated as fact | FIXED — labeled practitioner observation consistent with the OCR audit protocol's structure (protocol cited in prose; bot-walled) |
| 18 | LOW | Packaging: tests require full repo checkout, undocumented | FIXED — note added to architecture.md and data/README.md |

**ACCEPTED** (with reason):

- (i) `telemetry_contract: "telemetry/schema.json#/$defs/SkillInvocation"` pointer does not
  resolve (the root schema is itself titled SkillInvocation, with no `$defs`) — fleet-wide
  convention shared by all 7 skills; ticketed for the next structural sweep.
- (ii) UC-01 seed R-06 impact=1 looked low for an IdP MFA-fatigue risk — seed intent is a
  push-fatigue compromise of one account, contained by passwordless + session controls;
  band Medium preserved.
- (iii) UC-02 gap-register Low rows carry POL-x ids in the `standard_id` field — v1 stub
  convention, documented in the UC-02 doc; rename considered for v2.

## Tier-2 adjudications

- **Penalty-table currency CONFIRMED current:** live eCFR fetch — §102.3 Table 1 columns end
  at "2025 Maximum adjusted penalty ($)"; no 2026 adjustment exists as of 2026-06-10. The
  persona "there must be a 2026 column" currency instinct was refuted (5th
  persona-refutation library-wide). Gate row 38.
- **NPRM proposed-only CONFIRMED at the docket:** RIN 0945-AA22 returns exactly 1 document,
  type "Proposed Rule" — re-checked in the §5.11 pass. Gate rows 10/28.

## Smoke tests

3/3 consumer smokes PASS or PASS-WITH-NOTES; the notes were the facility-disposition
contradiction (finding 1) and the phantom nist-csf-2 healthcare view (finding 2), both fixed
in this pass (acceptance-gate rows 35–38 record the residual-risk closures).

## Verdict

Persona verdicts: 2 PASS, 3 CONDITIONAL PASS — all conditions resolved by this fix pass.
Overall: **G4.5 PASS pending re-verify.**
