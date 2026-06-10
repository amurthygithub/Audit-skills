# Persona Review — coso-internal-controls (G4.5 consumer-ready gate)

Run 2026-06-09 per `prompts/persona-vetting.md` (process v2): 5 LLM persona agents in
parallel; every CRITICAL/HIGH verified BEFORE fixing — Tier 1 (on-disk: grep, table
inspection, stub execution) or Tier 2 (live sources with verbatim quotes: PCAOB AS 2201
full text, SEC 33-8810 / 33-9142 / 34-88365 / Item 308, OMB M-16-17, GAO Green Book,
NIST 800-53A/FIPS 199/FedRAMP POA&M). **LLM-vetted — a filter, not a certification.**

Resolution key: **FIXED** (PR `fix/SOX-636-vet-coso`) · **TICKETED** · **ACCEPTED**.

## CRITICAL

| persona | finding | verification | resolution |
|---|---|---|---|
| Partner, SaaS | Management ICFR conclusion "Effective, subject to remediation" — SEC 33-8810 expressly prohibits qualified ICFR conclusions; the oracle test hard-coded the non-compliant language, so every consumer reproduced it | Tier 2 — 33-8810 verbatim ("should not qualify its assessment...") | **FIXED** — UC-01, stub, and oracle now conclude "Effective" with the SD communicated to the audit committee in writing |
| 3PAO | UC-02's compensating-control conclusion is security-unsound: reconciliations rated "precision: sufficient" against terminated-user access risk, but recs only catch unrecorded/mismatched items — fraudulent-but-recorded transactions reconcile cleanly; ITGC pervasiveness (reliance on app controls/IPE) never assessed; magnitude caps unsupported | Tier 1 (reads) + domain analysis; the Partner persona independently put MW on the table | **TICKETED — SOX-641** (UC-02 re-work: lookback, authority-limit magnitude analysis, occurrence-assertion precision test, ITGC-pervasiveness step; cascades into seed+stub+tests) |
| 3PAO, CISO | Fabricated AS 2201 Appendix B ITGC citations (.B4-.B10 access / .B11-.B16 change / .B17-.B21 IT ops) — App B actually covers audit integration, multiple locations, service organizations, benchmarking | Tier 2 — App B headings fetched | **FIXED** — re-cited to AS 2201.36 (ITGC context) + explicit note on App B's real contents |
| State Dir | Green Book absent skill-wide and A-123 row claims "COSO 2013 explicitly referenced" — A-123 (per M-16-17) mandates GAO's Green Book, which adapts COSO for government | Tier 2 — M-16-17 verbatim | **FIXED** (A-123 row corrected); full Green Book layer + government UC-03 variant **TICKETED — SOX-641** |
| State Dir | UC-03 (17-principle assessment) tagged financial-services/SEC-filer-only while README/_index advertise it as the public-sector UC; UC-03 missing from §8/§11 routing | Tier 1 (reads) | **TICKETED — SOX-641** (routing row + government variant); UC frontmatter test refs **FIXED** |

## HIGH

| persona | finding | resolution |
|---|---|---|
| Partner | "Reasonable possibility = neither remote nor certain; more than insignificant" — resurrects AS 2's rescinded threshold; AS 2201's note ties it to FAS 5 "reasonably possible or probable" (more than remote) | **FIXED** (Tier-2 verbatim note) |
| Partner, 3PAO, CISO | AS 2201.69 items recast as "per se indicators that a MW EXISTS"/"compensating analysis IRRELEVANT" — the standard says *indicators*; AS 5 retired per-se treatment | **FIXED** — rebuttable-presumption framing in chunks 05 + 07 (conservative default kept: departing from MW requires documented evaluation) |
| Partner, 3PAO, CISO | Mechanical "severity MAY be reduced by one level" demotion rule — not in AS 2201; compensating controls feed the likelihood/magnitude re-assessment | **FIXED** — re-run-Steps-2-3 framing, tested-control requirement noted |
| Partner, SaaS | "SRCs exempt from 404(b)" false (only if also non-accelerated); non-accelerated exemption is Dodd-Frank §989G, not the JOBS Act; EGC early-exit triggers absent | **FIXED** (Tier-2: 33-9142 + 34-88365 quotes) — exemptions split by statute with the SRC nuance and EGC loss triggers |
| SaaS | Item 308 attestation statement listed as an unconditional MUST — it applies only where 404(b) applies (Item 308(a)(4) filer-status wording); EGC-relying issuers must NOT state it | **FIXED** in chunks 03 + 06 (Tier-2: Item 308 verbatim) |
| 3PAO | Fabricated "NIST CSF/RMF (4-Tier)" severity scale — 800-53A produces S/OTS; FIPS 199 has 3 levels; the L/M/H(+Critical) scale is FedRAMP's POA&M layer | **FIXED** — column re-attributed + explicit this-is-our-construct note (FedRAMP "Critical" original-rating nuance included) |
| 3PAO, Partner | chunk 07's COSO↔TSC table severed mid-table by the spliced-in override section (3 orphaned rows) | **FIXED** — table re-merged, orphan rows removed |
| Partner | COSO PoF misattribution (P7 lists fraud-risk and change-assessment PoF that belong to P8/P9) and per-principle counts diverging from the publication | **TICKETED — SOX-641** — requires the COSO 2013 publication (paywalled): a Day-0 fact-sheet job, not an inline edit from recall |
| Partner | UC-01 scoping omits the period-end financial reporting process and ITGCs for a $12B bank | **TICKETED — SOX-641** |
| SaaS | No 404(a)-readiness path: routing dead-ends a pre-IPO SaaS into a $12B-bank UC; IPO-year timing omits the newly-public transition exemption; SEC 33-8810 management-assessment path absent from manifest | **TICKETED — SOX-641** |
| CISO | Non-issuer branch absent (AU-C 265, voluntary COSO, Single Audit, bond-covenant reporting); healthcare invisible in README; no COSO/ICFR board deck | **TICKETED — SOX-641**; README healthcare/industry inventory **FIXED** |
| Partner | COSO-GenAI-2026 / COSO-RPA-2024 manifest entries unverifiable as real COSO publications | **TICKETED — SOX-641** (verify-or-remove; registry cascade) |
| all | README inventory false: "7 chunks" (8), 214-line claim, phantom SKILL.md.bak / conftest.py / test_lint.py, "2 worked examples" (3), fictitious UC test refs | **FIXED** — regenerated from disk |

## Verdict

5 CRITICAL / 14 HIGH verified findings: all FIXED, TICKETED (SOX-641), or ACCEPTED.
The headline: **the most-copied artifact in the skill — the management ICFR report
conclusion — was SEC-prohibited language, enforced by the test suite.** Smoke tests
passed 3/3 because the skill is internally consistent; persona vetting + live-source
verification is what caught the places where it is consistently wrong.
