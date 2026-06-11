---
chunk_id: 02-impact-levels-and-baselines
parent_skill: fedramp-authorization
topic: "FIPS 199 high-water-mark categorization; the 4 FedRAMP Rev 5 baselines (Low 156 / Moderate 323 / High 410 / LI-SaaS 156) and how they are tailored from the NIST SP 800-53B baselines (149 / 287 / 370); the boundary vs nist-800-53-rmf"
load_when: "user asks which baseline applies, how to categorize a system, FIPS 199, impact levels, how many controls are in a baseline, LI-SaaS, or how FedRAMP relates to 800-53 control counts"
---

# Chunk 02 — Impact levels and baselines (the spine and the boundary)

Two facts drive every FedRAMP scoping decision: **how a system's impact level is set** (FIPS 199, high-water mark) and **how many controls each baseline carries**. Both are the most-misquoted numbers in this domain — pin them to the counts below, which were taken directly from the **PMO-authored OSCAL Rev 5 baseline profiles**.

## 1. FIPS 199 categorization — the high-water mark

A system is categorized against the **CIA triad** — Confidentiality, Integrity, Availability — each rated **Low**, **Moderate**, or **High** by the potential impact of a breach (limited / serious / severe-or-catastrophic) [FIPS-199 §categorization]. The **overall** impact level is the **high-water mark**: the **maximum** of the three objective ratings.

```
overall_impact = max(confidentiality, integrity, availability)   # Low < Moderate < High
```

- A system rated (C = Moderate, I = Low, A = Low) is an **overall Moderate** system.
- Raising **any single** objective to High makes the **whole system High**.
- **Do not average.** One High objective makes the system High; the high-water mark never rounds down.

The overall impact level then selects the FedRAMP **baseline**.

## 2. The four Rev 5 baselines (OSCAL-verified counts)

| Baseline | Controls (base + enhancements) | When it applies |
|----------|--------------------------------|-----------------|
| **Low** | **156** (135 base + 21 enh) | overall impact = Low |
| **Moderate** | **323** (181 base + 142 enh) | overall impact = Moderate (the most common SaaS authorization) |
| **High** | **410** (191 base + 219 enh) | overall impact = High |
| **LI-SaaS** (Low-Impact SaaS, "Tailored") | **156** (= Low's set; **66** 3PAO-tested + **90** CSP-attested) | a **Low-impact** offering delivered as **SaaS** |

[FEDRAMP-REV5-BASELINES §counts]

**Counting convention:** each total counts **base controls plus selected control enhancements** together (one entry each). 156 = 135 + 21; 323 = 181 + 142; 410 = 191 + 219.

> **Currency note:** **325** is the **Rev 4** Moderate count. Rev 5 Moderate is **323**. If you see 325 quoted as current, it is stale.

## 3. LI-SaaS (Tailored) — eligibility and the test/attest split

LI-SaaS is **not** a separate impact level — it is a **tailoring of the Low baseline** for low-impact Software-as-a-Service. Eligibility is two conditions, both required:

```
li_saas_eligible = (overall_impact == Low) AND (delivered as SaaS)
```

- The LI-SaaS baseline is the same **156** controls as Low, but the assessment burden is lighter: some controls are independently **3PAO-assessed** and the rest are satisfied by **CSP attestation** [FEDRAMP-REV5-BASELINES §li-saas]. The Rev 5 Tailored OSCAL profile assigns each control a **method designation** — `ASSESS` (3PAO-assessed), `ATTEST` (CSP-attested), `NSO`, `FED` — rather than a single flat split. **Correction (G4.5 §5.11):** the widely-quoted **"66 tested / 90 attested" flat split is a Rev 4 figure** (`REV_4_FedRAMP-Tailored-LI-SaaS-Requirements.docx`) and is **not** reproducible from the Rev 5 profile — so state the 156 total and the method-designation structure, not a fixed 66/90.
- **The trap:** a **Moderate** (or High) impact system is **not** LI-SaaS-eligible **even if** it is SaaS-delivered — it takes the full Moderate (323) or High (410) baseline. SaaS delivery alone does not make a system LI-SaaS; the impact must be **Low**.

## 4. The boundary: FedRAMP baselines ARE tailored 800-53 controls

FedRAMP does **not** define a separate control catalog. Each baseline is the corresponding **NIST SP 800-53B** baseline, tailored **up**:

| Overall impact | NIST SP 800-53B baseline | FedRAMP Rev 5 baseline | FedRAMP adds |
|----------------|--------------------------|------------------------|--------------|
| Low | 149 | **156** | +7 (net) controls/enhancements + FedRAMP parameter values |
| Moderate | 287 | **323** | +36 (net) |
| High | 370 | **410** | +40 (net) |

[NIST-800-53R5 §baselines]

- The control **IDs are the same 800-53 Rev 5 catalog** (AC-2, AU-6, SC-7, …). FedRAMP adds specific controls/enhancements and **sets parameter values** (the "[FedRAMP Assignment: …]" values) that 800-53 leaves to the organization.
- **For the catalog itself** — the control families, the text of a control, the general RMF 7-step process, or control-selection mechanics — use **`nist-800-53-rmf`**. This skill states the counts and the tailoring relationship; it does not enumerate or re-teach the catalog. A control-by-control baseline listing (300+ rows) is out of scope for v1.

## 5. Procedure — categorize and select a baseline

1. **Rate each objective.** Assign Low/Moderate/High to Confidentiality, Integrity, Availability based on the data and the impact of a breach (FIPS 199; the system's information types per NIST SP 800-60 inform this).
2. **Take the high-water mark.** Overall = max of the three.
3. **Check LI-SaaS.** If overall = Low **and** the offering is SaaS, LI-SaaS (156 controls, method-designated) is available; otherwise use the full baseline for the level.
4. **Select the baseline** — Low 156 / Moderate 323 / High 410.
5. **Record** the categorization rationale in the SSP (`chunks/04-the-authorization-package.md`).

## 6. Output template — categorization + baseline summary

```
System: <name>
FIPS 199: C=<level>  I=<level>  A=<level>   ->  Overall impact = <max> (high-water mark)
LI-SaaS eligible: <yes/no>  (Low AND SaaS)
Selected baseline: <Low 156 | Moderate 323 | High 410 | LI-SaaS 156 (method-designated)>
Catalog basis: NIST SP 800-53 Rev 5 (tailored from 800-53B <149|287|370>)
```

## 7. Anti-hallucination

- **Overall impact is the high-water mark (max of C/I/A), never an average** [FIPS-199 §categorization].
- **The Rev 5 counts are 156 / 323 / 410 / 156** (LI-SaaS = Low's 156) [FEDRAMP-REV5-BASELINES §counts]. **325 is the Rev 4 Moderate count** — do not state it as current. The LI-SaaS **"66 tested / 90 attested" split is also Rev 4** and is not reproducible from the Rev 5 profile — do not assert it.
- **LI-SaaS requires Low impact AND SaaS delivery.** Moderate/High + SaaS is not LI-SaaS — use the full baseline [FEDRAMP-REV5-BASELINES §li-saas].
- **FedRAMP baselines are tailored NIST SP 800-53 Rev 5 controls** (800-53B 149/287/370 tailored up), same catalog IDs — not a separate catalog [NIST-800-53R5 §baselines]. For the catalog/RMF, use `nist-800-53-rmf`.
