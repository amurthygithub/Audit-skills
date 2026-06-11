---
chunk_id: 05-section-302-vs-404
parent_skill: sox-302-disclosure-controls
topic: "§302 (quarterly officer cert, DC&P + ICFR) vs §404(a) (annual mgmt ICFR assessment, Item 308(a)) vs §404(b) (auditor attestation, accelerated/large only); newly-public + EGC exemptions for 404(b); §302 has no such exemption; the MW interplay"
load_when: "user asks the difference between Section 302 and Section 404, whether a newly-public filer or EGC owes 404(b), the auditor attestation, or which obligation applies"
---

# Chunk 05 — §302 vs §404 Boundary

The second most-confused distinction (after DC&P-vs-ICFR). **§302 is a certification; §404 is an assessment plus an attestation.** Stating the §404 exemptions imprecisely is the classic error. This chunk fixes the boundary; for §404/ICFR **assessment and attestation depth, use `coso-internal-controls`** — this skill does not re-teach §404.

## 1. The three obligations

| | §302 certification | §404(a) management assessment | §404(b) auditor attestation |
|---|---|---|---|
| What | Officer certification of the 6 elements, incl. DC&P + ICFR conclusions | Management's annual report on ICFR effectiveness | Auditor's attestation report on ICFR |
| Who acts | PEO + PFO (2 officers) sign personally | Management | Registered public accounting firm |
| Cadence | **Quarterly + annual** (each periodic report) | **Annual** (fiscal-year end) | **Annual** (with the annual report) |
| Where | Filed as a 601(b)(31) **exhibit** | **Item 308(a)** in the annual report | **Item 308(b)** in the annual report |
| Scope | DC&P (broad) + ICFR conclusion | ICFR only | ICFR only |
| Citation | 15 U.S.C. 7241; §240.13a-14 | Item 308(a) [Reg-S-K-Item-308 §a] | Item 308(b) [Reg-S-K-Item-308 §b] |

§404(a) and §404(b) are the **ICFR** workstream; their mechanics (COSO framework, scoping, walkthroughs, AS 2201 auditor testing) belong to `coso-internal-controls`. The §302 certification **incorporates** an ICFR conclusion (¶4–¶6, `chunks/03`) but is a separate, quarterly, officer-signed artifact.

## 2. The exemptions — precisely

- **§404(b) auditor attestation is required only for accelerated and large accelerated filers**, and is **exempt** for an **emerging growth company (EGC)**: the rule provides the attestation report is required "If the registrant, **other than a registrant that is an emerging growth company** … is an accelerated filer or a large accelerated filer" [Reg-S-K-Item-308 §b]. Non-accelerated filers and EGCs do not provide a §404(b) auditor attestation.
- **Newly-public companies** get a §404 **transition**: the first annual report need not include the Item 308(a) management ICFR report or the §404(b) attestation, and the issuer includes the SEC's prescribed transition-period statement instead [Reg-S-K-Item-308 §a]. A registrant "need not comply with paragraphs (a) and (b) of this Item until it … had been required to file an annual report … for the prior fiscal year" [Reg-S-K-Item-308 §a].
- **§302 has NO such exemption.** The §302 certification applies from the **first periodic report**. A newly-public issuer certifies §302 immediately; it may only omit the **ICFR** references in certification ¶4 until subject to the ICFR requirement [CFR-17-240.13a-14 §a] — the DC&P certification still applies in full from day one. **Never state the §404(b) (or §404 transition) exemption as also exempting §302.**

## 3. Decision logic — which obligation applies

```
Newly-public / first periodic report?
  -> §302 certification: YES (DC&P certification applies; ICFR refs in ¶4
     may be omitted until subject to the ICFR requirement)
  -> §404(a) mgmt ICFR report: NOT until required to file (transition)
  -> §404(b) auditor attestation: NO (transition; and exempt if EGC)

EGC (not newly-public)?
  -> §302: YES   §404(a): YES   §404(b): NO (EGC exemption)

Seasoned accelerated / large accelerated filer (not EGC)?
  -> §302: YES   §404(a): YES   §404(b): YES
```

This is the logic exercised by `use-cases/uc-02-newly-public-first-302.md` (newly-public EGC: §302 yes, §404(b) no).

## 4. The material-weakness interplay across the boundary

A material weakness identified in the §404 ICFR work does not stay on the §404 side. Because ICFR is the financial subset of DC&P (`chunks/02`):
- an **unremediated MW** over a disclosure-relevant area means the §302 **DC&P conclusion** is "not effective" for that area (disclosed under Item 307 — `chunks/04`);
- it triggers the §302 certification **¶5 disclosure** to the auditors and audit committee (`chunks/03`);
- management **cannot** report ICFR effective in the §404(a) Item 308(a) report with an MW present [Reg-S-K-Item-308 §a].

The full MW workflow is in `chunks/07-material-weakness-and-change.md`.

## 5. Anti-hallucination

- **§302 ≠ §404.** §302 = quarterly + annual officer **certification**; §404(a) = annual management ICFR **assessment** (Item 308(a)); §404(b) = auditor ICFR **attestation** (Item 308(b)). Do not merge them.
- **§404(b) is exempt for newly-public filers (transition) and EGCs** [Reg-S-K-Item-308 §a] [Reg-S-K-Item-308 §b]; **§302 is never exempt** — it applies from the first periodic report [CFR-17-240.13a-14 §a]. Do not state the §404(b) exemption as exempting §302.
- For §404/ICFR assessment and attestation **depth**, route to `coso-internal-controls`. This skill teaches the boundary, not §404.
