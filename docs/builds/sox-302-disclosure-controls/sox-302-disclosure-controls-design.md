# Design — sox-302-disclosure-controls (SOX-570)

> 15-section design per `docs/skill-design-template.md`. Built on the Day-0 fact sheet
> (`docs/sox-302-disclosure-controls-fact-sheet.md`, gate PASS) and the vendored public SEC
> extracts (`docs/builds/sox-570/sec-source-extracts.json`). Born-vetted (process v3/v3.1):
> G4.5 + the eval lane ship inside the build PR. Licence class = public (US federal text —
> machine-verifiable, full vendoring permitted).

## 0. Why this design doc exists

M5 cycle 2's new skill. Focused (effort S): SOX §302 Disclosure Controls & Procedures (DC&P)
certification, distinct from the §404/ICFR work in coso-internal-controls (the named
dependency). The design pins the chunk map, the three UC contracts (ticket B25/B26/B27), the
§5.11 plan, and the non-goals (no re-teaching §404; no §906 detail).

## 1. Scope & dependencies

### 1.1 Primary source citation

SOX §302 (15 U.S.C. 7241); SEC Rules 17 CFR 240.13a-14, 240.13a-15(b)/(c)/(e)/(f); Reg S-K
Items 307, 308, 601(b)(31). All public, fetched 2026-06-11. The verbatim DC&P/ICFR definitions
are the load-bearing facts.

### 1.2 Structural inventory (counts)

From the fact sheet §0: 6-element certification (15 U.S.C. 7241(a)(1)-(6)); 6 numbered cert
paragraphs in the 601(b)(31) exhibit; 4 core implementing rules; 3 Reg S-K items; 2 signing
officers (PEO + PFO); quarterly DC&P evaluation (FPI: annual).

### 1.3 Persona

**FIN** (per ticket): SOX/SEC reporting professionals — controllers, SEC-reporting managers,
disclosure-committee members, Big-4 advisors. Auditee-side (the issuer's certification process),
not the external auditor.

### 1.4 Effort estimate

**S** (per ticket). 7 chunks, 4 industries, 3 UCs, ~32 tests + eval cases. One build PR.

### 1.5 Dependencies

- Day-0 fact sheet (done).
- **coso-internal-controls** (the §404/ICFR skill) — one-way cross-reference for the 302-vs-404
  boundary; no shared data.
- nist-csf-2 / hipaa — referenced for the cyber-8-K DC&P touchpoint (B26); pointer only.
- Registry: 5 SEC citations added at G1.

### 1.6 Out-of-scope (explicit non-goals)

- **§404 ICFR assessment/attestation mechanics** — coso-internal-controls owns it; this skill
  cites the boundary, does not re-teach §404.
- §906 criminal certification (18 U.S.C. 1350) — named as the companion cert, not detailed.
- Auditor attestation standards (AS 2201) — pointer only.
- The disclosure committee and sub-cert cascade are **recommended practice / house framework**,
  labeled everywhere — never asserted as a rule mandate.
- No crosswalk rows in v1.

## 2. Chunk architecture (7 chunks)

| # | File | Contents (all from fact sheet / public extracts) | Est. lines |
|---|------|--------------------------------------------------|-----------|
| 01 | 01-section-302-overview.md | What §302 requires; 15 U.S.C. 7241; who signs (PEO + PFO, 13a-14); quarterly + annual; the 601(b)(31) exhibit; relationship to §906 (pointer) | 160 |
| 02 | 02-dcp-vs-icfr.md | The spine: verbatim DC&P (13a-15(e)) and ICFR (13a-15(f)) definitions; DC&P ⊃ ICFR for financial matters + the non-financial universe (risk factors, legal, MD&A, cyber 8-K); the Venn relationship; why a DC&P failure need not be an ICFR failure and vice versa | 175 |
| 03 | 03-the-six-certifications.md | The 6 numbered cert paragraphs verbatim-grounded: ¶1 reviewed, ¶2 no untrue statement, ¶3 fair presentation, ¶4 DC&P/ICFR responsibility + design + evaluation, ¶5 disclosure to auditors + audit committee (SD/MW + fraud), ¶6 ICFR-change note | 180 |
| 04 | 04-evaluation-and-disclosure.md | 13a-15(b) quarterly DC&P evaluation; Item 307 (disclose DC&P conclusion); Item 308(a)/(c) (ICFR report + changes); evidence the evaluation rests on; effectiveness conclusion language | 170 |
| 05 | 05-302-vs-404-boundary.md | §302 (quarterly officer cert, DC&P + ICFR) vs §404(a) (annual mgmt ICFR assessment) vs §404(b) (auditor attestation, accelerated/large only); newly-public + EGC exemptions for 404(b) (the 302 obligation has NO such exemption — it applies from the first periodic report); the MW interplay | 175 |
| 06 | 06-disclosure-committee-subcert.md | The disclosure committee (recommended, 33-8124 — labeled) and the sub-certification cascade (house framework): how entities/process owners sub-certify up to the PEO/PFO; coverage and exception roll-up; multi-entity groups | 175 |
| 07 | 07-material-weakness-and-change.md | A new MW or significant deficiency and its effect on the 302 DC&P conclusion; material-change disclosure; ¶5 disclosure to auditors/audit committee; the cyber-8-K timeliness DC&P touchpoint (Item 1.05, 4 business days); remediation-period certification language | 170 |

### 2.8 Why 7 chunks

The DC&P-vs-ICFR boundary and the 302-vs-404 boundary are the two concepts consumers get wrong
— each gets its own chunk (02, 05). The 6 certifications are the operative artifact (03). The
disclosure committee + sub-cert cascade is the process consumers build (06, the B27 anchor). MW
interplay + cyber scope is the volatile/edge content (07). 6 would merge the two boundaries;
8 would split the evaluation thinly.

## 3. Industry angles (4)

| Industry | Angle |
|----------|-------|
| saas-technology.md | Newly-public / pre-IPO tech issuer (B26): first 302, disclosure-committee charter, non-financial scope incl. cyber 8-K; 404(b) exemption year 1 but 302 applies immediately |
| financial-services.md | Bank/insurer accelerated filer (B25): mature DC&P, MW interplay, regulatory-disclosure overlap, large sub-cert cascade |
| healthcare.md | Health-tech issuer: HIPAA/clinical disclosure as non-financial DC&P scope; cyber + privacy 8-K touchpoints |
| manufacturing.md | Multi-entity / multi-segment group (B27): the 15-entity sub-cert framework, foreign-subsidiary annual-vs-quarterly nuance |

`_index.md` mirrors SKILL.md routing.

## 4. Use cases (3 — ticket B25/B26/B27)

UC seed + oracle contracts; docs written to the tested fixtures. Oracles are derivability-based.

### 4.1 UC-01 — Accelerated filer Q3 10-Q with a new MW (B25)

Seed: a Q3 disclosure with a newly-identified ICFR material weakness, plus a 14-owner sub-cert
cascade (each sub-cert flags clean/exception). Output: the 302 DC&P effectiveness conclusion
(a material weakness in ICFR over a financially significant area means DC&P is **not effective**
for that area → officers must conclude DC&P not effective and disclose under Item 307); the ¶5
disclosure obligation (to auditors + audit committee); the sub-cert roll-up (exception count,
whether the top-level cert is clean). Oracle: the DC&P conclusion is derived from the MW facts
(an unremediated MW affecting a disclosure-relevant area → DC&P not effective); the cascade
roll-up counts are recomputed from the sub-cert list.

### 4.2 UC-02 — Newly-public SaaS first 302 (B26)

Seed: a first-time filer's obligation set (first 10-Q post-IPO) + a disclosure inventory tagged
financial vs non-financial (revenue, risk factors, cyber-incident, legal). Output: the
obligation determination (302 certification **required from the first periodic report**; 404(a)
management assessment timing; **404(b) auditor attestation exempt** in the transition / for an
EGC) and the DC&P scope (financial AND non-financial items in scope; cyber 8-K Item 1.05 is a
DC&P item). Oracle: obligation flags derived from filer-status facts (newly-public → 404(b)
exempt, 302 applies); scope set = financial ∪ non-financial disclosure items.

### 4.3 UC-03 — 302 sub-cert framework for a 15-entity group (B27)

Seed: 15 entities (some foreign private issuers with annual eval), each with a coverage tag.
Output: the sub-certification cascade design — every entity mapped to a sub-certifier rolling up
to the group PEO/PFO; coverage check (all 15 covered, gaps flagged); the FPI annual-vs-quarterly
evaluation-frequency split. Oracle: coverage count and gap list recomputed from the entity list;
the quarterly/annual split derived from the FPI tags.

### 4.4 UC selection rationale

Ticket-specified (B25/B26/B27); covers the MW-interplay path, the newly-public obligation/scope
path, and the multi-entity cascade path — the three things FIN consumers build. Both the
boundary concepts and the process artifact are exercised.

## 5. Test architecture

| File | Cases | Count |
|------|-------|-------|
| test_sox_302_disclosure_controls_lint.py | linter exit 0 | 1 |
| test_sox_302_disclosure_controls_oracle.py | UC-01/02/03 derivability + expected-seed agreement | 5 |
| test_sox_302_disclosure_controls_grounding.py | citations resolve; manifest bidirectional; registry sync | 4 |
| test_sox_302_disclosure_controls_trace.py | UC procedures cite real SKILL.md sections; chunks exist | 3 |
| test_sox_302_disclosure_controls_metamorphic.py | sub-cert order invariance; MW-removed flips DC&P conclusion; entity-list order invariance | 3 |
| test_sox_302_disclosure_controls_adversarial.py | missing filer-status fact → refuse; unremediated MW forces not-effective; 404(b) never required for newly-public; disclosure-committee labeled non-mandatory; empty entity list | 5 |
| test_sox_302_disclosure_controls_telemetry.py | schema; instrument; enums | 5 |
| test_sox_302_disclosure_controls_consistency.py | routing ↔ chunks; industry/UC index sync; fact-sheet counts == chunk counts (inventory-diff) | 5 |
| test_sox_302_disclosure_controls_chunks.py | per-chunk frontmatter, ≤200 lines, in routing | 7 |
| **Total target** | | **38** |

Eval lane: `evals/sox-302-disclosure-controls/cases/` with the 3 UC substance cases + 1
idempotence invariant + the refusal/obligation perturbation set, oracle-labeled, CI-enforced.

### 5.11 Source-of-truth verification plan

| Fact | Source | Verified by |
|------|--------|-------------|
| DC&P definition verbatim (broader than ICFR) | 17 CFR 240.13a-15(e) | dispatcher; G4 re-fetch |
| ICFR definition verbatim | 17 CFR 240.13a-15(f) | dispatcher |
| 6-element certification | 15 U.S.C. 7241(a)(1)-(6) + 601(b)(31) exhibit | dispatcher |
| PEO + PFO sign; filed as exhibit | 17 CFR 240.13a-14 | dispatcher |
| Quarterly DC&P eval (FPI annual) | 17 CFR 240.13a-15(b) | dispatcher |
| Item 307 DC&P disclosure / Item 308 ICFR | 17 CFR 229.307 / 229.308 | dispatcher |
| 404(b) newly-public/EGC exemption; 302 has none | SEC releases / JOBS Act §103; statute | dispatcher (verify quotes) |
| Disclosure committee recommended not mandated | SEC Release 33-8124 | dispatcher (label as practice) |
| Cyber 8-K Item 1.05 = 4 business days | Form 8-K (library-verified) | dispatcher |

Public, machine-verifiable; §5.11 agent diffs against eCFR/statute. Anti-hallucination/limits
sections verified FIRST. Key risk: presenting the disclosure committee / sub-cert cascade as a
rule (it is practice) — explicit gate.

## 6. PoV analyses — 5 lenses

- **Framework fidelity:** DC&P≠ICFR and 302≠404 are the two fidelity risks; the disclosure
  committee/sub-cert-as-rule is the third → all three get inventory-diff/grep gates.
- **Completeness:** all 6 cert elements; both boundaries; the cascade; both personas of the FIN
  audience (process-builder + certifier).
- **Usability:** the disclosure-committee charter and sub-cert template are copy-paste; the
  302-vs-404 table is the reference consumers want.
- **Spine conventions:** ≤300-line router, ≤200-line chunks, §1-§11, telemetry, house-style §6.
- **Cross-skill:** coso-internal-controls boundary is one-way; cyber-8-K references nist/hipaa.

## 7. PoV analyses — 5 personas

- **SEC-reporting manager:** wants the cert mechanics and the evaluation evidence exactly right.
- **Disclosure-committee chair (newly-public, B26):** the charter + non-financial scope + cyber.
- **Big-4 SOX advisor (B27):** the multi-entity sub-cert framework, FPI nuance.
- **Controller (B25):** the MW→DC&P-conclusion logic and ¶5 disclosure.
- **Securities lawyer:** will check that the disclosure committee/sub-cert is labeled practice,
  not rule, and that 302-vs-404 exemptions are stated precisely.

## 8. Cross-skill alignment table

| Other skill | Touchpoint | Shape |
|-------------|-----------|-------|
| coso-internal-controls | §404/ICFR boundary | one-way reference from chunk 05 |
| nist-csf-2 / hipaa-security-rule | cyber/privacy 8-K as non-financial DC&P scope | pointer in chunk 07 / healthcare.md |
| aicpa-soc-reporting | SOC report as disclosure-process evidence | reference in saas-technology.md |

## 9. Data & synthetic content

- `data/seeds/`: uc-01-input/expected (Q3 MW + 14 sub-certs), uc-02-input/expected (newly-public
  obligation/scope), uc-03-input/expected (15-entity cascade). Fictional issuers; no real EDGAR
  data; `as_of_date` where dates matter.
- `data/generators/`: `gen_subcert_cascade.py --seed` (entity/sub-cert lists for the eval sampler).
- `data/crosswalks/`: empty v1.
- Redaction: no MNPI/financial data; seeds are structural facts only.

## 10. Telemetry & docs

Standard Spine set. Docs: architecture.md, limits-and-disclaimers.md (DC&P≠ICFR; 302≠404;
disclosure-committee/sub-cert = practice not rule; not legal advice; currency re-verify),
changelog.md, acceptance-gate.md (≥20 rows from the fact sheet's verified facts).
persona-review.md by G4.5.

## 11. Risk register (top per category)

1. **Fidelity:** DC&P conflated with ICFR → chunk 02 + inventory-diff + adversarial test.
2. **Fidelity:** disclosure committee / sub-cert cascade presented as a rule → grep gate + label.
3. **Fidelity:** 404(b) exemption stated as also exempting 302 → adversarial test (302 always applies).
4. **Completeness:** a cert element dropped → consistency test asserts all 6.
5. **Usability:** the MW→DC&P-conclusion logic too abstract → UC-01 walks it; oracle derives it.
6. **Cross-skill:** §404 re-taught here (scope creep) → chunk 05 references coso, does not re-teach.

## 12. Build sequence

- Day 1: scaffold + SKILL.md + chunk 01-02.
- Day 2: chunks 03-07.
- Day 3: industries; seeds + generator + stub + oracle/metamorphic/adversarial (contract first);
  UC docs to fixtures; eval cases.
- Day 4: remaining tests; lint; consistency; calibration sweep.
- Day 4.5 (§5.11): verification vs eCFR/statute + fix + re-verify.
- Day 5: 5-lens + persona vetting (G4.5) in-PR; smokes; acceptance-gate.
- Day 6: PR, CI, merge; Linear; plan.

## 13. File-by-file plan

`skills/sox-302-disclosure-controls/`: SKILL.md, README.md; chunks/01-07; industries/_index + 4;
use-cases/_index + uc-01-mw-interplay.md, uc-02-newly-public-first-302.md,
uc-03-multientity-subcert.md; data/ per §9; tests/ 9 files + stub + conftest; telemetry/ 4;
docs/ 4 + persona-review.md (G4.5); evals/sox-302-disclosure-controls/cases/.

## 14. Open questions for review

1. Reproduce the full cert exhibit text verbatim, or paraphrase with cites? **Decision:
   verbatim is fine** — it is public federal text (601(b)(31)); reproduce the 6-paragraph exhibit
   as the operative artifact in chunk 03.
2. Industries — is "manufacturing" the right 4th, or "multi-entity group"? **Decision: keep
   sector names** (manufacturing carries the multi-entity-group angle); the cascade is a UC, not
   an industry.
3. Sub-cert cascade size in UC-01 (14) vs UC-03 (15)? **Decision: keep both** — ticket-specified
   (B25 = 14 owners; B27 = 15 entities); different constructs (process owners vs legal entities).

## 15. Requirements parameters checklist

- [x] §1 scope/deps/out-of-scope; [x] §2 7 chunks ≤200 rationale; [x] §3 4 industries;
- [x] §4 3 UCs with seed+oracle contracts; [x] §5 test arch (38 target) + §5.11 plan;
- [x] §6 5 lenses; [x] §7 5 personas; [x] §8 cross-skill; [x] §9 data (no MNPI);
- [x] §10 telemetry/docs; [x] §11 risk register; [x] §12 day plan; [x] §13 file plan;
- [x] §14 open questions resolved; [x] §15 this checklist.

## 16. Sign-off

- Designer: Claude (Fable 5) dispatcher, 2026-06-11.
- Fact-sheet gate: PASS. Licence class: public (machine-verifiable, full vendoring permitted).
- Ready for G3: **yes** — build agents receive the fact sheet + public extracts + this design;
  the UC seed/oracle contracts in §4 are binding.
