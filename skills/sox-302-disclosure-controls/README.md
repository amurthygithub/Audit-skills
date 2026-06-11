# SOX §302 Disclosure Controls & Procedures — sox-302-disclosure-controls

The regulation skill for **SOX §302** (15 U.S.C. 7241) and its implementing rules — the **Disclosure Controls & Procedures (DC&P)** certification: who signs (the PEO and PFO), the six certification elements, the quarterly DC&P evaluation, and the Item 307 effectiveness conclusion. This is **distinct from §404/ICFR** (the COSO internal-controls work): §302 is the **quarterly officer certification** covering DC&P **and** ICFR conclusions; §404 is the **annual management ICFR assessment plus auditor attestation**. The skill exists to teach the two boundaries consumers get wrong — **DC&P ≠ ICFR** and **§302 ≠ §404** — and to build the certification process around them.

## What it does

- Produces the §302 **DC&P effectiveness conclusion** from the facts: a new unremediated ICFR material weakness in a disclosure-relevant area means DC&P is **not effective** [17 CFR 240.13a-15(e); Reg S-K Item 307].
- Determines the **obligation set** for any filer status — §302 applies from the first periodic report; §404(b) is exempt for a newly-public filer / EGC; §404(a) is the annual management assessment.
- Scopes DC&P vs ICFR: DC&P covers **all** disclosure items (financial **and** non-financial — risk factors, legal proceedings, MD&A, the cyber 8-K Item 1.05); ICFR covers only the financial-reporting subset.
- Designs the **sub-certification cascade** for a multi-entity group and computes the coverage and the FPI annual-vs-quarterly evaluation split.

## When to use

- An issuer needs its quarterly/annual **§302 certification** prepared, or the **DC&P effectiveness conclusion** reasoned from a material-weakness fact pattern.
- A newly-public company needs the precise **obligation determination** (what is owed, deferred, or exempt) for its first periodic report.
- A multi-entity group needs a **sub-certification cascade** with coverage control and the foreign-private-issuer evaluation-frequency split.

## When NOT to use

- The **§404 ICFR assessment or auditor attestation mechanics** — use `coso-internal-controls`; this skill references the §302-vs-§404 boundary and does not re-teach §404.
- **§906 criminal certification** (18 U.S.C. 1350) — named as the companion certification only.
- **HIPAA Breach Notification** behind a healthcare cyber 8-K — use `hipaa-security-rule`; this skill covers only the §302 DC&P / SEC 8-K side.
- Legal advice or a compliance certification — no template here is a safe harbor.

## Use cases (3)

- **UC-01 — Material-weakness interplay** (Crestline Financial Corp, accelerated filer, Q3 10-Q): an unremediated ITGC logical-access material weakness over the revenue system turns the DC&P conclusion **not effective** (`DCP_NOT_EFFECTIVE`); the cert ¶5 disclosure to auditors + audit committee fires; the 14-owner sub-cert cascade rolls up **1 exception / 13 clean** (IT/ITGC); the top-level cert is **not** clean; the same MW hits both the §302 cert now and the annual §404 assessment.
- **UC-02 — Newly-public first §302** (Nimbus Cloud Inc, newly-public EGC): §302 **required from the first periodic report** (no exemption); §404(b) auditor attestation **exempt**; §404(a) management assessment required (first annual report); DC&P scope **7** items / ICFR scope **3**; cyber 8-K Item 1.05 in DC&P scope (`FIRST_302_404B_EXEMPT`).
- **UC-03 — Multi-entity sub-cert cascade** (Meridian Group, 15 entities): **14 covered / 1 gap** (Entity-14, `CASCADE_GAPS_1`); the FPI evaluation split is **12 domestic (quarterly) / 3 foreign private issuers (annual)**; the cascade is labeled a house framework.

Every UC is seed-backed with **derivability oracles**: the tests recompute each expected number independently from `data/seeds/` (56 skill-local tests across oracle, metamorphic, adversarial, and structural suites, plus root-level lint/consistency/registry suites).

## 30-second quick start

```python
import sys, json

sys.path.insert(0, "skills/sox-302-disclosure-controls/tests")  # stub executor

from sox_302_disclosure_controls_stub import run_skill

payload = json.load(open("skills/sox-302-disclosure-controls/data/seeds/uc-01-input.json"))
out = run_skill("UC-01", payload)
print(out["classification"])            # -> "DCP_NOT_EFFECTIVE"
print(out["dcp_conclusion"])            # -> "not effective" (derived from the MW facts)
print(out["subcert_exceptions"],
      "/", out["subcert_clean"])        # -> 1 / 13  (the IT/ITGC owner)
print(out["par5_disclosure_required"])  # -> True  (an MW triggers the 7241(a)(5) disclosure)
```

The stub is a deterministic reference executor — it demonstrates output structure and the documented house conventions; it does not perform a legal certification.

## Caveats that govern everything here

1. **DC&P ≠ ICFR.** DC&P (17 CFR 240.13a-15(e)) covers **all** information required to be disclosed — financial **and** non-financial (risk factors, legal proceedings, MD&A, cyber 8-K Item 1.05). ICFR (17 CFR 240.13a-15(f)) is limited to the reliability of financial reporting. ICFR is a subset of DC&P for financial matters; DC&P adds the whole non-financial disclosure universe. A missed cyber-8-K is a DC&P failure that need not be an ICFR failure.
2. **§302 ≠ §404.** §302 is the **quarterly officer certification** (PEO + PFO, filed as the 601(b)(31) exhibit) covering DC&P and ICFR conclusions. §404 is the **annual** management ICFR assessment (Item 308(a)) plus, for accelerated/large accelerated filers, the auditor's ICFR attestation (§404(b)). The **§404(b) exemption never exempts §302** — §302 applies from the first periodic report regardless of newly-public / EGC status.
3. **The disclosure committee and the sub-certification cascade are practice, not rule.** The SEC *recommended* a disclosure committee in Release 33-8124; it did not mandate one, and no rule requires sub-certifications. The §302 certification is signed by exactly two officers (PEO + PFO); sub-certifications support, but never replace, their certification. Both are labeled house framework / recommended practice everywhere they appear.

## Industries covered (4)

- [financial-services](industries/financial-services.md) — bank/insurer accelerated filer: the MW §302/§404 interplay and the large sub-cert cascade (UC-01)
- [healthcare](industries/healthcare.md) — health-tech issuer: HIPAA/clinical matters as non-financial DC&P scope; privacy + cyber 8-K touchpoints
- [manufacturing](industries/manufacturing.md) — multi-entity / multi-segment group: the 15-entity cascade and the FPI annual-vs-quarterly nuance (UC-03)
- [saas-technology](industries/saas-technology.md) — newly-public / pre-IPO issuer: §302 from day one, §404(b) exempt, the disclosure committee, cyber scope (UC-02)

## Cross-references to other skills

- `coso-internal-controls` — authoritative for the §404 ICFR assessment and auditor attestation; this skill references the §302-vs-§404 boundary one-way
- `hipaa-security-rule` — HIPAA Breach Notification behind a healthcare cyber 8-K
- `nist-csf-2` — executive cyber-maturity overlay behind the cyber-8-K DC&P touchpoint (pointer only)
- `aicpa-soc-reporting` — SOC 2 report content as disclosure-process evidence for a SaaS issuer

## What this skill is NOT

- Not legal advice, and not a compliance certification — no template here is a safe harbor
- Not a §404/ICFR assessment skill (it references the boundary; `coso-internal-controls` owns §404)
- Not a §906 criminal-certification skill (named as the companion cert only)
- Not a substitute for the issuer's own certification — the §302 certification is the officers' obligation; this skill structures it

## Public-source note

Every fact in this skill is grounded in **public US federal text**: the SOX §302 statute (15 U.S.C. 7241, uscode.house.gov) and the SEC implementing rules and Reg S-K items on the eCFR (17 CFR 240.13a-14, 240.13a-15, 229.307, 229.308). All five citation labels resolve in the project citation registry. No EDGAR data and no MNPI: the seeded issuers (Crestline Financial Corp, Nimbus Cloud Inc, Meridian Group) are fictional and the seeds carry structural facts only.
