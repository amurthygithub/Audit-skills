# Persona Review — isaca-audit-methodology (G4.5 consumer-ready gate)

Run 2026-06-10 per `prompts/persona-vetting.md` (process v2): 5 LLM persona agents + 3
clean-session smoke tests in parallel; every CRITICAL/HIGH verified BEFORE fixing — Tier 1
(on-disk greps, stub execution, math checks) or Tier 2 (live sources with verbatim quotes:
COBIT 2019 Governance and Management Objectives full text, ISACA CISA exam content outline +
2024 press release, ISACA COBIT/ITAF/CCP pages, ITAF 4th Edition full text, CSA CCM v4 page,
google/vsaq repo, sharedassessments.org, GDPR Art 83 (CELEX), eCFR 45 CFR 164.308/.312 and
16 CFR 314.1, GAO-24-106786). **LLM-vetted — a filter, not a certification.**

Resolution key: **FIXED** (PR `fix/SOX-636-vet-isaca`) · **TICKETED — SOX-644** · **ACCEPTED**.

> **Process v2 vindicated twice in one run:** two persona claims that all/most personas agreed
> on were REFUTED by Tier-2: (1) "ITAF 4th Edition is current; the 5th Edition is invented" —
> wrong: ISACA launched ITAF 5th Edition 2026-02-26 (the pre-existing SOX-630 ticket was right);
> (2) "ISACA is only a CMMC training partner; Cyber AB/CAICO confers CCP/CCA" — stale: ISACA
> was authorized as the CAICO in 2025. Findings are hypotheses; concurrence is not verification.

## CRITICAL

| persona | finding | verification | resolution |
|---|---|---|---|
| all 5 | **Fabricated COBIT 2019 structure**: "BAI12 Managed project portfolio" invented (BAI ends at BAI11); MEA truncated to 3 (MEA04 Managed Assurance — THE audit objective — erased); BAI02/03/05/06 names scrambled so the real change-management objective (BAI06 Managed IT Changes) vanished; "12 BAI + 3 MEA" arithmetic only reached 40 because the two errors offset | Tier 2 — full objective extraction from the GMO publication: 5/14/11/6/4, zero "BAI12" hits | **FIXED** — chunk 02 rebuilt from the verified catalog (all 40 official names); SKILL.md counts synced |
| all 5 | **"7 information criteria" taught as COBIT 2019** — they are COBIT 4.1, retired in COBIT 5/2019 (goals cascade replaced them); finding templates tagged outputs with the dead construct | Tier 2 — "information criteria" absent from COBIT 2019 texts; COBIT 4.1 PDF defines the seven | **FIXED** — goals-cascade section replaces it; `cobit_criteria_affected` relabeled an information-attribute house convention |
| Partner, 3PAO, CISO, State Dir | **Fabricated standard citations in golden outputs**: "ISACA Standard S17" (the skill's own fake numbering, defined as audit-risk, used as a recertification mandate) + "COBIT APO13.02" (actually "Define and manage an information security and privacy risk treatment plan" — wrong practice) baked into UC-02, chunk 06, README, stub — and ENFORCED by the oracle test; real ITAF numbers (1001-1402) appeared nowhere; limits doc told the agent to REFUSE if asked for them | Tier 2 — ITAF 4th Ed full text (1001-1008/1201-1207/1401-1402); APO13.02 + DSS05.04 verbatim | **FIXED** — fake S/G scheme retired skill-wide; real ITAF series tables in chunk 03; lifecycle re-keyed; criteria now cite auditee obligations (policy from seed + DSS05.04); oracle asserts S17 is ABSENT; "ITAF binds the auditor, not the auditee" rule added |
| SaaS, Partner, CISO (+ smokes) | **Skill contradicts its own oracle**: docs said severity "High" for the 3-of-5 scenario, stub/oracle hard-coded "Critical" via a raw exception count (≥3 → Critical = "Material Weakness" per chunk 05) — same finding flips SD↔MW depending on artifact; smoke UC-02 FAILED on this | Tier 1 — stub rule read; three doc locations grep'd | **FIXED** — stub/oracle aligned to "High"; count rule replaced with labeled deviation-rate demo heuristic that cannot emit Critical; MW/SD auto-mapping fenced (magnitude+likelihood judgment, ICFR-only) |
| SaaS (+ smoke UC-01 FAIL) | **Two competing output schemas**: chunk 03 template keys (`process_id`/`assessment_date`/`initiative`) vs oracle keys (`id`/`date`/`initiatives`/`classification` envelope) — a consumer following the only documented template fails the oracle | Tier 1 — keys diffed | **FIXED** — templates/UCs/README aligned to the tested contract incl. envelope keys (`maturity_assessment`, `observation`); broken SKILL.md §6 pointer corrected |
| 3PAO, Partner, SaaS | **Fabricated questionnaire mappings**: "CAIQ v4" table used codes GRM/AAC/CHM/SDE/RSK/IRM — none are v4 domains (real v4: 17 codes GRC, A&A, …, UEM); VSAQ "Section 1–9" invented (named questionnaires); "SIG's 18 domains" wrong (21) | Tier 2 — CSA CCM page (17 domains verbatim), google/vsaq repo, sharedassessments.org | **FIXED** — chunk 08 rebuilt with verified codes/names/counts; CSA-CCM-v4 added to citation registry + §10 manifest |

## HIGH

| persona | finding | resolution |
|---|---|---|
| all 5 | CISA weights self-contradiction: limits doc stamped 21/17/12/23/27 as "from CRM 28th Ed (2024)" while SKILL.md/chunk 01 said 18/18/12/26/26. Tier 2: 18/18/12/26/26 is the live outline (effective Aug 2024); 21/17/12/23/27 was the 2019 job practice | **FIXED** — one verified set everywhere, sourced to the exam content outline |
| all 5 | ITAF edition contradiction (manifest "5th Ed"/witaf5 vs README+limits "4th Ed"). Tier 2 REFUTED the persona majority: 5th Edition IS current (Feb 2026) | **FIXED** — 5th Edition consistently; registry/manifest URL corrected to the live isaca.org/resources/it-audit (HTTP 200); numbering verified against 4th-Ed text with a verify-titles caveat |
| Partner, State Dir | "Critical = Material Weakness, High = Significant Deficiency" as a decision rule in the always-loaded router | **FIXED** — router + chunk 05 now require magnitude/likelihood deficiency evaluation; GAGAS significance pointed for government audits |
| Partner, 3PAO | Invented attribute-sampling formula (proportion-CI with nonstandard precision) attributed to the methodology | **FIXED** — replaced with AICPA tables pointer (verified in audit-workpapers, e.g. n=59 @ 5/5/0); random-selection "cannot evaluate statistically" inversion corrected |
| Partner, 3PAO | L×I×CRF formula + bands attributed to "[CISA-CRM-28E] and [ITAF]"; heat-map cells (3,4 labeled M) contradicted the Low=1-4 band; CRF extends range to 0.5-50 | **FIXED** — labeled house methodology (attribution note + citations line); cells corrected; Low band "< 5"; range documented |
| Partner, State Dir | C-C-C-E-R attributed to "AS 1215/AU-C 230" (documentation standards); GAGAS four-elements-as-needed discipline absent | **FIXED** — lineage corrected to GAGAS 2024 8.116 (verified verbatim) / IIA; "no exceptions" rule scoped to ISACA engagements |
| CISO | healthcare.md fabricated crosswalk rows: BAI07→164.308(a)(2) "change management accountability" (it's the security-official standard; HIPAA has NO change-mgmt standard); break-glass→DSS05.02 (network security) omitting 164.312(a)(2)(ii) Required; "HIPAA requires logging of all ePHI access" (164.312(b) says record-and-examine activity, scope risk-based) + DSS05.04 mislabeled as monitoring (that's DSS05.07) | **FIXED** — all rows corrected per verified CFR + practice texts; post-hoc break-glass review added |
| CISO | Destructive ITAC test procedures (inject duplicates/invalid data) with no production/clinical safeguard; no patient-safety impact dimension in the risk model | **FIXED** — production-safety rule in chunk 04 + clinical-engineering sign-off; patient-safety impact note in healthcare.md; full clinical UC **TICKETED — SOX-644** |
| CISO, SaaS | Healthcare unreachable: frontmatter claimed it, §11 routed "other" (nonexistent) instead; UC-03 existed but was unrouted (smoke agent only found it by listing files) | **FIXED** — routing table now matches disk (4 industries incl. healthcare intents, 3 UCs) |
| Partner | GDPR effect wrong twice: Art 32 penalties quoted at "EUR 20M" (Art 83(4) tier is EUR 10M/2% — verified verbatim) and GDPR used as the effect for a US commercial bank | **FIXED** — bank scenario now cites GLBA Interagency Guidelines/FFIEC; chunk 06 example states the correct 83(4) tier with a verify-the-regime warning |
| Partner | financial-services.md cited 16 CFR 314 (FTC Safeguards) for banks — 314.1(b) scopes it to FTC-jurisdiction (non-bank) institutions; banks → Interagency Guidelines 12 CFR 30 App. B | **FIXED** — split by charter type (verified verbatim) |
| 3PAO, State Dir | Fabricated ISACA publication "COBIT 2019: Focus Area for Cybersecurity (NIST CSF 2.0 aligned)" in public-sector/fin-svcs references; "Focus Area for Cloud Computing" also unverifiable | **FIXED** — replaced with the verified focus-area titles (Information Security; I&T Risk; DevOps; SME) + *Implementing the NIST CSF Using COBIT 2019* (maps CSF v1.1) |
| SaaS, State Dir | README inventory false (SKILL.md.bak, conftest.py/test_lint.py, "7 chunks", "2 UCs", 198 lines, stale filename); acceptance-gate checkboxes false (7 chunks/3 industries/phantom tests checked as present); UC frontmatter test pointers broken; Path 1 quickstart silently delivers router-only context; no data-handling caveat | **FIXED** — README regenerated from disk; gate re-verified; pointers corrected; Path 1 now concatenates chunks + data-sensitivity warning |
| SaaS | Stub echoes seed answers as "analysis" (data/README even called `current_evidence` "evidence items"); UC-01 filename said "it-audit-plan" for a maturity assessment; README capability row promised a risk-register output no UC produces | **FIXED** — canned-output warnings (README Path 2 + limits doc), data dictionary honest, UC renamed `uc-01-saas-maturity-assessment.md`, capability row relabeled guidance-only. Real risk-plan UC **TICKETED — SOX-644** |
| State Dir | No GAGAS/Yellow Book layer anywhere; public-sector view federal-only ("state FISMA" invented); audit-committee-centric templates unusable for legislative offices; no small-shop path; no public-sector UC | Quick fixes **FIXED** (state/local row corrected, scope note added); GAGAS bridge + legislative reporting + small-shop scoping + public-sector UC **TICKETED — SOX-644** |

## MEDIUM/LOW (summary)

EDM05 "stakeholder transparency"→"Ensured Stakeholder Engagement", MEA03/BAI07 official names
in stub/UCs, COSO "Internal Environment"→"Control Environment", AT-C 100/200/300→AT-C 320,
MEA→Detect remapped (DSS05.07; MEA→Govern), ITIL table dual-labeled (ITIL 4 SVC / v3 legacy),
materiality-vs-audit-risk-model conflation, CMMC role updated (ISACA = CAICO, Tier-2), maturity
decision-rule vs fractional scores reconciled (house-convention note), roadmap "+0.5/quarter"
arithmetic relabeled illustrative, gen_risk_plan docstring seed-mapping corrected, saas
inheritance rewritten in COBIT terms (was pasted NIST control IDs) — all **FIXED**.
Board-deck localization, deeper FS subsector content — **TICKETED — SOX-644**.

## Smoke tests

Pre-fix: UC-01 **FAIL** (4/10 assertions — template-vs-oracle schema), UC-02 **FAIL** (5/22 —
severity contradiction, S17, undocumented fields), UC-03 PASS-WITH-NOTES. Post-fix re-runs in
clean sessions: UC-01 **PASS-WITH-NOTES** (11/11 assertions), UC-02 **PASS-WITH-NOTES** (all
assertions; the two residual notes — envelope key and ISP-003-not-in-seed — were then fixed:
envelope keys documented everywhere, policy reference moved into the seed so criteria are
input-derived). The recurring library pattern held: internally-coherent outputs over fabricated
framework facts, which structural tests green-light.

## Verdict

6 CRITICAL / 12 HIGH verified findings: all FIXED, TICKETED (SOX-644), or ACCEPTED. Headline:
**the COBIT 2019 objective catalog — the skill's central artifact — contained an invented
objective and erased the two objectives auditors cite most (BAI06 IT Changes, MEA04 Assurance),
and the test suite enforced citing a standard that does not exist.** The catalog is now
transcribed verbatim from the publication, the fake numbering is retired skill-wide, and the
oracle asserts its absence.
