---
name: audit-workpapers
version: 1.0
description: >
  Create, organize, evaluate, and review audit workpapers per PCAOB AS 1215, AS 2315, AS 1105, AS 3105,
  AICPA AU-C 230, ISA 230, and ISACA ITAF. Use this skill when asked to draft workpapers, design sampling
  plans, document audit evidence, write findings, compute sample sizes or upper limits on misstatement,
  structure tickmark systems, perform risk model calculations (AR = IR × CR × AP × TD), determine audit
  opinions, build cross-reference tables, or ensure compliance with audit documentation standards.
  Triggers: workpaper, audit documentation, sampling plan, MUS, attribute sampling, tickmark, sign-off,
  finding, cross-reference, audit risk model, tolerable misstatement, engagement completion document.
category: audit
risk: high
source: PCAOB AS 1215/2315/1105/3105/1220; AICPA AU-C 230; ISA 230; ISACA ITAF; COSO ICIF-2013; arXiv:2604.06116; arXiv:2403.14069
date_added: "2026-05-25"
tags:
  - audit
  - workpapers
  - pcaob
  - aicpa
  - sampling
  - mus
  - attribute-sampling
  - audit-evidence
  - audit-risk
  - internal-control
  - coso
  - isaca
  - findings
  - quality-control
  - documentation
  - isa
---

# Audit Workpapers Skill

## 1. When to Use This Skill

**USE this skill when:**
- Creating, organizing, indexing, or reviewing any audit workpaper
- Designing sampling plans (attribute, MUS/PPS, variables, non-statistical, dual-purpose)
- Documenting audit evidence, re-performance, or re-computation
- Writing audit findings in the 5-part format
- Computing sample sizes, upper limits on misstatement, or projected misstatements
- Building tickmark legends, cross-reference tables, or lead schedules
- Performing audit risk model calculations (AR = IR × CR × AP × TD)
- Determining audit opinions (unqualified, qualified, adverse, disclaimer)
- Preparing engagement completion documents (per AS 1215.13)
- Ensuring compliance with PCAOB, AICPA, ISA, or ISACA documentation standards
- Evaluating electronic workpaper controls, retention, or sign-off protocols
- Integrating data analytics or ML-enhanced sampling into audit documentation

**DO NOT use this skill when:**
- The task is purely tax preparation (different standards apply)
- The task is a forensic investigation outside an audit engagement
- The task involves advisory/consulting services with no audit documentation requirements
- The task is a SOC 1/SOC 2 examination (use SOC-specific skills instead, unless workpaper structure is needed)
- The user is asking about financial statement preparation (not an audit task)

---

## 2. Applicable Standards

| Standard | Body | Scope | Key Focus | Effective/Updated |
|----------|------|-------|-----------|-------------------|
| AS 1215 | PCAOB | Audit Documentation | Documentation requirements, retention, review, completion | Amended .09/.11 eff. Dec 15, 2026 |
| AS 2315 | PCAOB | Audit Sampling | Statistical/nonstatistical sampling, risk types | Amended .11 eff. Dec 15, 2026 |
| AS 1105 | PCAOB | Audit Evidence | Evidence types, relevance, reliability, assertions | Current |
| AS 3105 | PCAOB | Departures from Unqualified Opinions | Qualified, adverse, disclaimer opinions | Current |
| AS 1101 | PCAOB | Audit Risk | Risk model: AR = IR × CR × AP × TD | Current |
| AS 2105 | PCAOB | Materiality | Tolerable misstatement planning | Current |
| AS 2110 | PCAOB | Identifying/Assessing Risks | Risk assessment procedures | Current |
| AS 2301 | PCAOB | Responses to Risks of Misstatement | Nature, timing, extent of procedures | Current |
| AS 1220 | PCAOB | Engagement Quality Review | EQR requirements | Current |
| AS 1201 | PCAOB | Supervision | Supervisory review requirements | Current |
| AS 3101 | PCAOB | Auditor's Report | Report format, CAMs | Current |
| AS 2201 | PCAOB | IC over Financial Reporting | Material weakness, significant deficiency | Current |
| AS 1305 | PCAOB | Communications about IC Deficiencies | Significant deficiency reporting | Current |
| AU-C 230 | AICPA | Audit Documentation | Clarity standards for private co. audits | Current |
| AU-C 500 | AICPA | Audit Evidence | Private-co evidence standards | Current |
| AU-C 530 | AICPA | Audit Sampling | Private-co sampling guidance | Current |
| ISA 230 | IAASB | Audit Documentation | International documentation standards | Current (ISA is principle-based) |
| ISA 500 | IAASB | Audit Evidence | International evidence standards | Current |
| ISA 530 | IAASB | Audit Sampling | International sampling guidance; includes PPS | Current |
| ITAF | ISACA | IT Audit Framework | IT-specific workpaper standards, CAATs | Current |
| ICIF-2013 | COSO | Internal Control — Integrated Framework | 5 components, 17 principles | 2013; 2026 GenAI guidance |
| QC 1000 | PCAOB | Firm Quality Control | QC framework replacing prior standards | Eff. Dec 15, 2025 |
| AS 1000 | PCAOB | General Responsibilities | Replaces prior general standards | Eff. Dec 15, 2024 (large firms) |

### 2.1 Regulatory Updates (2024–2026)

| Update | Effective Date | Impact on Workpapers |
|--------|---------------|---------------------|
| QC 1000 (amended firm QC) | Dec 15, 2025 (small firms); Dec 15, 2024 (firms >100 issuers) | New quality control framework; documentation of firm-level QC procedures |
| AS 1000 (general responsibilities) | Dec 15, 2024 (large firms) | Replaces prior general standards; updates professional requirements |
| AS 1215 amendments (.09 and .11) | Dec 15, 2026 | New documentation completion and quality review requirements per PCAOB Release No. 2024-005 |
| AS 2315 amendment (.11) | Dec 15, 2026 | Updated nonsampling risk language |
| COSO 2026 GenAI guidance | 2026 | "Achieving Effective Internal Control Over Generative AI" — new controls for AI-generated outputs |

**Agent behavior:** When the engagement date falls on or after an effective date, APPLY the updated standard. When referencing a standard that has been amended, NOTE the amendment and effective date.

---

## 3. Workpaper Structure and Indexing

### 3.1 Hierarchical Index Scheme (A–N)

Every workpaper receives a unique alphanumeric index. Letter = major section; Number = workpaper within section; Sub-number = sub-workpaper.

| Index | Section | Typical Contents |
|-------|---------|-----------------|
| **A** | Permanent File / Entity Information | Org structure, articles, bylaws, agreements, business description, related parties, continuing significance items |
| **B** | Audit Planning & Risk Assessment | Engagement letter, planning memo, risk assessment summary, materiality, strategy, timelines |
| **C** | Internal Control Evaluation | COSO 5 components, walkthrough documentation, control matrix, IT general/application controls, control risk assessments |
| **D** | Substantive Testing — Revenue | Revenue recognition, AR confirmations, revenue cutoff, allowances |
| **E** | Substantive Testing — Expenditures | AP testing, purchase cutoff, expense analysis, payroll |
| **F** | Substantive Testing — Assets | Cash, investments, inventory, fixed assets, intangibles |
| **G** | Substantive Testing — Liabilities | Debt, accruals, contingencies, leases |
| **H** | Substantive Testing — Equity | Capital stock, retained earnings, dividends, stock-based compensation |
| **I** | Audit Sampling Documentation | Sampling plans, selection lists, evaluation worksheets |
| **J** | Analytical Procedures | Ratio analysis, trend analysis, budget-to-actual, reasonableness tests |
| **K** | Completion & Reporting | Engagement completion document, uncorrected misstatements, opinion determination, subsequent events |
| **L** | Communications & Representations | Management representation letter, audit committee communications, fraud inquiries |
| **M** | Quality Review | Supervisory review notes, partner review notes, EQR notes and resolutions |
| **N** | Specialty Areas | IT audit, fair value estimates, related parties, going concern, segment reporting |

**Index format examples:**
- `D-1` = First workpaper in the Revenue section
- `D-3.1` = Sub-workpaper 1 of the third Revenue workpaper
- `I-2` = Second workpaper in the Sampling section
- `B-1.3` = Sub-workpaper 3 of the first Planning workpaper

### 3.2 Cross-Referencing System

**Every workpaper must cross-reference:**

1. **Source documents** — Where did the data originate? (e.g., "Source: Client GL trial balance as of 12/31/25")
2. **Lead schedules** — Tie workpaper detail to financial statement line items (e.g., "See lead schedule K-1")
3. **Risk-to-response linkage** — Per AS 2110 and AS 2301, link identified risks to the procedures that address them
4. **Tickmark-to-workpaper** — Each tickmark explained in a tickmark legend workpaper
5. **Conclusion linkage** — Where does the conclusion flow? (e.g., "Conclusion carried to K-2")

**Cross-reference format:**
```
[Source WP Index] → [This WP Index] → [Conclusion WP Index]
```

**Example:** `B-2 (Risk Assessment) → D-1 (Revenue Testing) → K-1 (Completion Summary)`

**Agent behavior:** When creating any workpaper, ALWAYS include cross-references in both directions: where data came from AND where conclusions flow to.

### 3.3 Tickmark System

**8 Standard Tickmarks:**

| Symbol | Meaning | Documentation Requirement |
|--------|---------|--------------------------|
| ✓ | Verified to source document | Identify source (e.g., "✓ = traced to bank statement") |
| ∧ | Agrees to prior year | Identify prior-year WP (e.g., "∧ = agrees to WP D-1 PY") |
| ∨ | Footed / cross-footed | Specify computation (e.g., "∨ = column footed and agreed to total") |
| ○ | Tested via sampling | Reference sampling WP (e.g., "○ = selected per sampling plan I-1") |
| □ | Confirmed with third party | Identify confirment and date (e.g., "□ = bank confirmation received 2/15/26") |
| △ | Recomputed / recalculated | Show computation (e.g., "△ = depreciation recomputed per client policy") |
| ※ | Exception noted | Describe exception (e.g., "※ = invoices missing for 3 items; see Exception 1") |
| ◆ | Re-performed | Describe procedure re-performed (e.g., "◆ = bank rec re-performed independently") |

**Custom tickmark rules:**
- Custom tickmarks ARE permitted but MUST be defined in a tickmark legend workpaper (typically `B-5` or similar)
- Every custom tickmark must be explained at least once in the file where it first appears
- Do not reuse a standard tickmark symbol with a different meaning
- If a workpaper uses any tickmark, that tickmark MUST appear in the tickmark legend

**Agent behavior:** When generating a workpaper, create a tickmark legend section at the bottom listing every tickmark used on that workpaper with its explanation.

### 3.4 Sign-off Protocol

Per AS 1215.06: Documentation must demonstrate WHO performed the work and WHO reviewed it, with DATES.

| Role | Sign-off Required | Standard Reference | Timing |
|------|-------------------|-------------------|--------|
| **Preparer** | Initials + date work performed | AS 1215.06 | At time work is performed |
| **Reviewer (Supervisory)** | Initials + date review completed | AS 1201 | Before report release |
| **Engagement Partner** | Sign-off on significant matters | AS 1215.15 | Before report release — all necessary procedures complete AND partner/supervisory review complete |
| **EQR Partner** | Sign-off per AS 1220 | AS 1220 | Before report release for applicable engagements |

**Sign-off format:**
```
Prepared by: [Initials]  [MM/DD/YY]
Reviewed by: [Initials]  [MM/DD/YY]
Partner:     [Initials]  [MM/DD/YY]
EQR:        [Initials]  [MM/DD/YY]
```

**Agent behavior:** Every workpaper output MUST include preparer and reviewer sign-off placeholders with date fields. If the engagement meets EQR thresholds, include EQR sign-off placeholder.

### 3.5 Header/Footer Requirements

**Every page must contain:**
- Client name
- Engagement period (FY ending date)
- Workpaper index
- Preparer initials/date
- Reviewer initials/date
- Page number (Page X of Y)

---

## 4. Workpaper Content Requirements (Per AS 1215.04–.07)

### 4.1 Three Mandatory Elements (AS 1215.04)

Every workpaper MUST satisfy:

1. **Clear understanding of PURPOSE** — Why was this workpaper created? What objective does it serve?
2. **Clear identification of SOURCE** — Where did the data come from? What documents, systems, or personnel provided the information?
3. **Clear CONCLUSIONS reached** — What was the auditor's conclusion? Must be explicit, not implied.

### 4.2 Experienced Auditor Standard (AS 1215.06A)

Documentation must be sufficient to enable an **experienced auditor** (having no previous connection with the engagement) to:

1. Understand the **nature, timing, extent, and results** of procedures performed
2. Understand the **evidence obtained** and **conclusions reached**
3. Determine **who performed** the work and **date** completed
4. Determine **who reviewed** the work and **date** of review

### 4.3 The 5W1H Framework

| Question | Required Content | Standard |
|----------|-----------------|---------|
| **Who** | Preparer, reviewer, person performing work | AS 1215.06, .06A |
| **What** | Procedures performed, evidence obtained, conclusions reached | AS 1215.06 |
| **When** | Date work performed, date of review, timing relative to balance sheet date | AS 1215.06, .15 |
| **Where** | Source of data, location of records, location of physical assets | AS 1215.10 |
| **Why** | Purpose/objective of procedure, audit assertion addressed | AS 1215.04, .07 |
| **How** | Methodology used, sampling approach, specific techniques | AS 1215.04, .10 |

**Agent behavior:** When generating any workpaper, verify that ALL six 5W1H elements are present. If any element is missing, ADD it before finalizing.

---

## 5. Audit Evidence Types and Hierarchy (Per AS 1105)

### 5.1 Evidence Categories

**A. Risk Assessment Procedures** — Required for every engagement (AS 1105.03)
***(See also AS 2110 for risk assessment procedures and identification of risks of material misstatement.)***

**B. Further Audit Procedures:**
- Tests of Controls (when relying on operating effectiveness of controls)
- Substantive Procedures:
  - Tests of Details of Classes of Transactions, Account Balances, and Disclosures
  - Substantive Analytical Procedures

### 5.2 Audit Evidence Types (AS 1105.15–.21)

| # | Type | Standard | Description | Documentation Requirements |
|---|------|----------|-------------|--------------------------|
| 1 | **Inspection** | AS 1105.15 | Examining internal/external documents and records, AND physical examination of tangible assets | Identify specific items inspected (check #s, invoice #s, dates) or physical items examined (identification, location, condition). If sampling, document selection method per AS 1215.10 |
| 2 | **Observation** | AS 1105.16 | Looking at process/procedure performed by others | Document what was observed, when, and who performed it. Note: observation provides evidence only at point in time |
| 3 | **Inquiry** | AS 1105.17 | Seeking info from knowledgeable persons | Document who was asked, what was asked, what was said. **CRITICAL: Inquiry alone does NOT provide sufficient evidence per AS 1105.17** |
| 4 | **Confirmation** | AS 1105.18 | Direct written communication from third party | Document confirment, information confirmed, response received (or non-response and alternative procedures). External confirmation > internal |
| 5 | **Recalculation** | AS 1105.19 | Checking mathematical accuracy | Document original computation source, independent recalculation result, agreement/disagreement |
| 6 | **Reperformance** | AS 1105.20 | Independent execution of procedures/controls originally performed by entity | Document procedure re-performed, inputs used with sources, result, comparison to original |
| 7 | **Analytical Procedures** | AS 1105.21 | Evaluation of plausible relationships among financial/nonfinancial data | Document expectation development, comparison, investigation of significant differences |

### 5.3 Evidence Reliability Hierarchy (AS 1105.08)

**Priority order — higher = more reliable:**

1. **External evidence** obtained directly by auditor > Internal evidence
2. From **independent source** > From company source
3. **Directly obtained** by auditor > Indirectly obtained
4. **Original documents** > Photocopies/facsimiles
5. Evidence from **effective IT controls** over data > Evidence from systems without controls
6. **Written evidence** > Oral evidence (AS 1215.06: oral evidence alone does not provide sufficient documentation for an experienced auditor)
### 5.4 IPE Risk Assessment and Evaluation

When relying on information produced by the company (IPE) as audit evidence, the engagement team must assess risks that could compromise the relevance and reliability of the data. In accordance with PCAOB AS 1105.10, risks must be evaluated across the following dimensions:

*   **Extraction and Parameters Risk:** The risk that the report parameters, filters, or logic used to query the system are incorrect, leading to an incomplete or inaccurate data extraction (Nonsampling Risk per AS 2315.11).
*   **Data Integrity and ITGC Risk:** The risk that unauthorized changes were made to the underlying data or application logic due to deficient Information Technology General Controls (ITGCs).
*   **End-User Computing (EUC) Risk:** The risk of manual manipulation, broken links, or formula errors in user-defined spreadsheets (e.g., Excel, Access) provided by the client.

#### IPE Input Gating: What the Agent Needs Before It Can Work

**Agent behavior: DO NOT proceed with IPE procedures until you have verified you have the minimum evidence bundle.** If any required item is missing, STOP and ask the auditor for it. Do not guess, assume, or skip.

**STEP 1: Classify the IPE by source and purpose.**

```
Classify the IPE on two dimensions:

DIMENSION A — Source:
  SYSTEM-GENERATED: Extracted directly from an ERP/database
    (e.g., SAP aging report, Oracle GL extract, Workday payroll file)
  END-USER COMPUTING (EUC): Built or manipulated by a person
    (e.g., Excel accrual schedule, Access database maintained by a controller)

DIMENSION B — Purpose:
  POPULATION: The IPE is the set of items you will test
    (e.g., AR aging used to select confirmations, inventory list used for counts)
  ANALYTICAL INPUT: The IPE feeds a calculation or expectation
    (e.g., depreciation schedule plugged into analytics, FX rate table)
  SUPPORTING EVIDENCE: The IPE backs a single assertion or disclosure
    (e.g., board minutes, lease schedule, legal letter)
```

**STEP 2: Derive the minimum evidence bundle from the classification.**

For each classification, the mandatory minimum items are:

| Classification | Minimum Evidence Required |
|---|---|
| **System-generated + Population** | (a) The IPE report itself (full extract, not summary), (b) GL trial balance or sub-ledger to reconcile totals, (c) ITGC workpapers for the source system (or confirmation ITGCs were tested), (d) System documentation or query parameters used to generate the report |
| **System-generated + Analytical Input** | (a) The IPE report, (b) The formula/methodology the auditor is applying to it, (c) ITGC workpapers for the source system, (d) GL tie-out for any balance-based inputs |
| **System-generated + Supporting Evidence** | (a) The IPE document, (b) Confirmation of source (system name, report name, date generated), (c) ITGC reference or basis for relying on system controls |
| **EUC + Population** | (a) The EUC file in native format (Excel, Access — not PDF), (b) GL trial balance or sub-ledger for reconciliation, (c) Description of who built/maintains the EUC and how, (d) If the EUC sources from a system: the source report used as input |
| **EUC + Analytical Input** | (a) The EUC file in native format, (b) The formula/methodology applied to it, (c) Documentation of EUC logic (who built it, what it calculates, when last updated), (d) Source data feeding the EUC |
| **EUC + Supporting Evidence** | (a) The EUC document, (b) Description of authorship and update cycle, (c) Any source inputs feeding the EUC |

**STEP 3: Run the gap check.**

```
FOR each item in the minimum evidence bundle:
  Item provided? → YES: note what was provided and its format
                  → NO:  FLAG AS MISSING

IF any items are flagged MISSING → STOP.
Respond: "Before I can validate this IPE, I need: [list missing items].
Here's why each is required: [one-line reason per item].
What I have so far: [list what was provided]."

IF all items are provided → PROCEED to Mandatory Procedures below.
```

**Important:** The minimum evidence bundle adapts to what the auditor gives you. A $50M manufacturer running SAP needs different evidence than a $2M startup running QuickBooks with Excel workpapers. The classification above covers both — the auditor provides what their environment produces, and the agent verifies it's enough to proceed.

### Mandatory Procedures for Testing the Accuracy and Completeness of IPE

Before using IPE as a population or audit evidence for substantive procedures, the auditor must obtain audit evidence about the accuracy and completeness of the information. Perform and document the following procedures:

1.  **Establish Population Completeness:**
    *   **Reconciliation:** Reconcile the total balance or record count of the IPE report directly to the General Ledger (GL) trial balance or appropriate sub-ledger.
    *   **Sequence Testing:** For document populations (e.g., invoices, checks, shipping logs), test the numerical sequence to ensure no gaps or omissions exist in the provided data.
2.  **Verify Data Accuracy:**
    *   **Source Document Vouching:** Select a representative sample of line items from the IPE report and vouch them back to original, independent source documents (e.g., third-party bank statements, executed contracts, physical shipping notes).
    *   **Logic and Formula Recalculation:** Independently re-perform any system or user-defined calculations within the report (e.g., aging buckets, mathematical totals, complex Excel formulas).
3.  **Evaluate System Reliability:**
    *   Verify if the report is "System-Generated." If so, cross-reference and document the testing of ITGCs and Automated Application Controls (refer to C-series workpapers) that restrict unauthorized access to the report writer or database.

**Decision rules:**
- If evidence conflicts, DO NOT disregard either piece. Document the conflict, perform additional procedures, and reach a conclusion (AS 1215.08; additional procedures per AS 1105.29)
- If an assertion is addressed only by inquiry, OBTAIN additional corroborating evidence
- When using company-produced information, test its accuracy and completeness (AS 1105.10)
- When using electronic information from external sources, verify its source and reliability (AS 1105.10A)

### 5.5 Handling Contradictory Evidence (AS 1105.29)

When the auditor obtains audit evidence that contradicts other evidence obtained:

1. **Investigate the inconsistency** — Determine the cause of the contradiction by performing additional procedures
2. **Obtain further corroborating evidence** — Seek additional audit evidence to resolve the inconsistency
3. **Evaluate reliability** — Reassess the reliability of both the contradictory evidence and the other available evidence
4. **Consider implications** — Evaluate whether the inconsistency affects other areas of the audit or indicates a risk of material misstatement
5. **Document resolution** — Document the inconsistency, the additional procedures performed, the evidence obtained, and the conclusion reached
6. **Do not disregard** — The auditor must not simply disregard contradictory evidence without investigation (AS 1105.29)

> **Distinction:** AS 1105.29 specifically addresses *contradictory evidence* — situations where audit evidence directly conflicts with other evidence obtained. "Doubtful" evidence — where the auditor questions reliability absent a direct conflict — extends beyond .29 and is a matter of professional judgment under AS 1101 (due professional care). Both situations require additional procedures, but contradictory evidence triggers the specific requirements of AS 1105.29, while doubtful evidence is resolved under general professional judgment standards.

**Agent behavior:** When encountering contradictory or doubtful evidence, ALWAYS document the inconsistency, the additional procedures performed to resolve it, and the conclusion. Never ignore contradictory evidence.

### 5.6 Using Company's Specialist Work (AS 1105 Appendix A)

When the auditor uses the work of a company's specialist (e.g., actuary, appraiser, environmental consultant) as audit evidence:

1. **Evaluate the specialist's competence and abilities** — Assess the specialist's professional certification, license, reputation, and experience in the relevant field
2. **Evaluate the specialist's objectivity** — Consider whether the specialist is employed by the company or is an independent party; evaluate potential bias
3. **Understand the specialist's work** — Understand the nature, assumptions, methods, and data used by the specialist
4. **Evaluate the reasonableness of assumptions and methods** — Determine whether the specialist's assumptions and methods are reasonable and consistent with the auditor's understanding of the business and industry
5. **Evaluate the relevance and reliability of the specialist's work** — Determine whether the specialist's work provides sufficient appropriate audit evidence for the assertion being tested
6. **Test the data** — When relying on company-provided data used by the specialist, test the accuracy and completeness of that data (AS 1105.10)
7. **Document the evaluation** — Document the specialist's identity, qualifications, objectivity assessment, the nature of work performed, the assumptions and methods used, and the auditor's conclusion on the reliability of the specialist's work

**Agent behavior:** When relying on a company's specialist, document the evaluation of competence, objectivity, and the reasonableness of assumptions and methods. Do not accept specialist work without evaluation.

### 5.6 Financial Statement Assertions (AS 1105.11)

| # | Assertion | Definition | Typical Procedures |
|---|----------|-----------|-------------------|
| 1 | **Existence or Occurrence** | Assets/liabilities exist at B/S date; transactions occurred during period | Physical observation, confirmation, inspection of source documents |
| 2 | **Completeness** | All transactions/accounts that should be presented ARE included | Tracing from source documents to records, completeness checks, cutoff testing |
| 3 | **Valuation or Allocation** | Amounts are appropriate; allocations are reasonable | Recalculation, fair value testing, aging analysis, impairment testing |
| 4 | **Rights and Obligations** | Entity holds rights to assets; liabilities are obligations of entity | Contract review, confirmation, title documents |
| 5 | **Presentation and Disclosure** | Components properly classified, described, and disclosed per GAAP | Disclosure checklist, classification testing, presentation review |

**Assertion-to-procedure mapping:** When documenting any test, EXPLICITLY state which assertion(s) the procedure addresses. A single procedure may address multiple assertions; document ALL assertions addressed.

---

## 6. Complete Sampling Methodology

### 6.1 Sampling Decision Framework

**Use this decision sequence:**

1. Is the population suitable for 100% examination? (Small population of large items, significant risks, automatable population) → If YES, test 100% (AS 1105.22)
2. Are specific items the appropriate approach? (Key items, high-value, specific characteristics) → If YES, select specific items. NOTE: Results CANNOT be projected to population (AS 1105.27)
3. Is audit sampling appropriate? → If YES, proceed to statistical vs. non-statistical decision

**Statistical vs. Non-Statistical Decision:**

| Factor | Statistical | Non-Statistical |
|--------|-------------|-----------------|
| Population size | Large (>500 items) | Small (<500 items) |
| Need for quantified sampling risk | Yes | No (but must still consider sampling risk per AS 2315.09) |
| Special knowledge of specific items | No | Yes |
| Cost vs. benefit | Benefit exceeds cost | Cost exceeds benefit |
| Projection of results to population | Required and quantified | Required but not quantified |
| Auditor's professional judgment | Complemented by statistics | Primary basis |

**Attribute vs. MUS vs. Variables Decision:**

| Objective | Method | When to Use |
|-----------|--------|-------------|
| Test control operating effectiveness (deviation rate) | **Attribute Sampling** | Tests of controls; binary yes/no for each item |
| Test for monetary overstatement of balances | **MUS/PPS** | Substantive testing; population with positive balances; testing for overstatement |
| Test for overstatement AND understatement | **Variables Sampling** (Difference/Ratio) | When both directions of misstatement are a concern |
| Estimate population value directly | **Variables Sampling** (MPU) | When book values are unavailable or unreliable |

### 6.2 Attribute Sampling (Tests of Controls)

**Purpose:** Estimate deviation rate from prescribed controls.

**Parameters:**

| Parameter | Description | Standard |
|-----------|-------------|----------|
| Tolerable Rate | Maximum deviation rate supporting planned assessed control risk | AS 2315.34 |
| Expected Deviation Rate | Auditor's estimate of true deviation rate | Professional judgment + prior-year results |
| Risk of Assessing Control Risk Too Low | Risk that assessed control risk < true operating effectiveness | Affects EFFECTIVENESS — more serious |
| Risk of Assessing Control Risk Too High | Risk that assessed control risk > true operating effectiveness | Affects EFFICIENCY — less serious |

**Sample size relationships (AS 2315.38):**
- As tolerable rate ↓, sample size ↑
- As expected deviation rate ↑, sample size ↑
- As risk of assessing control risk too low ↓, sample size ↑

**Attribute Sampling Sample Size Table (95% Confidence / 5% Risk of Assessing CR Too Low):**

| Tolerable Rate | Expected Deviation Rate | Approximate Sample Size |
|---------------|------------------------|------------------------|
| 2% | 0% | 150 |
| 3% | 0% | 100 |
| 5% | 0% | 60 |
| 5% | 1% | 90 |
| 5% | 2% | 140 |
| 7% | 0% | 45 |
| 7% | 1% | 60 |
| 7% | 2% | 80 |
| 10% | 0% | 30 |
| 10% | 1% | 40 |
| 10% | 2% | 55 |
| 15% | 0% | 20 |
| 20% | 0% | 15 |

**Attribute Sampling Procedure:**

1. **Define the objective:** What control is being tested? What constitutes a deviation?
2. **Define the population:** All items subject to the control during the period
3. **Set parameters:** Tolerable rate, expected deviation rate, risk level
4. **Determine sample size:** Use table above or statistical formula
5. **Select sample:** Random, systematic (random start + fixed interval), or haphazard
6. **Perform tests:** Apply control test to each selected item; document each result
7. **Evaluate results:**
   - Calculate sample deviation rate = (# deviations / sample size) × 100
   - Compare sample deviation rate to tolerable rate
   - Consider whether sample deviation rate + sampling risk exceeds tolerable rate
   - If deviations found, consider nature, cause, and effect on control risk assessment
8. **Document conclusion:** Control is/is not operating effectively at the assessed level; impact on control risk assessment per AS 2315.28

### 6.3 Monetary Unit Sampling (MUS) / PPS

**Purpose:** Substantive test of details for overstatement in monetary balances. Each dollar in the population is a potential selection unit.

**Parameters:**

| Parameter | Description | Standard |
|-----------|-------------|----------|
| Tolerable Misstatement (TM) | Maximum monetary misstatement for account/class | AS 2315.18 |
| Risk of Incorrect Acceptance (RIA) | Risk sample supports "not misstated" when it IS | AS 2315.12 |
| Risk of Incorrect Rejection (RIR) | Risk sample supports "IS misstated" when it is NOT | AS 2315.12 |
| Expected Misstatement (E[M]) | Auditor's estimate of actual misstatement | Professional judgment |
| Sampling Interval (SI) | = TM / Reliability Factor | Formula below |
| Population Book Value (BV) | Total recorded value of population | Client records |
| Reliability Factor (RF) | Factor based on RIA and expected # overstatements | See table below |

**Reliability Factors for MUS (Risk of Incorrect Acceptance):**

| Number of Overstatements | 1% Risk | 5% Risk | 10% Risk | 15% Risk | 20% Risk |
|--------------------------|---------|---------|----------|----------|----------|
| 0 | 4.61 | 3.00 | 2.31 | 1.90 | 1.61 |
| 1 | 6.64 | 4.75 | 3.89 | 3.38 | 2.95 |
| 2 | 8.41 | 6.30 | 5.33 | 4.72 | 4.17 |
| 3 | 10.05 | 7.76 | 6.69 | 5.98 | 5.32 |
| 4 | 11.63 | 9.16 | 7.99 | 7.18 | 6.40 |

**Formulas:**

```
Sampling Interval (SI) = Tolerable Misstatement / Reliability Factor

Sample Size (n) = (BV × RF) / TM    [basic formula]

Sample Size (n) = (BV × RF) / (TM - E[M])    [when considering expected misstatement]
where E[M] = Expected Error Rate × BV

Equivalently:
n = (BV × RF) / (TM - (EA × BV))
where EA = Expected Misstatement / Book Value (error rate)
```

**MUS Selection Method:**
1. Calculate sampling interval
2. Select a random start between $0.01 and the sampling interval
3. Select items where cumulative dollar amount crosses an interval boundary
4. **All items > sampling interval are automatically selected (100% examination)**

**MUS Evaluation — Computing Upper Limit on Misstatement (ULM):**

```
Step 1: Calculate Basic Precision (BP)
        BP = Reliability Factor × Sampling Interval

Step 2: For each misstatement found, calculate the Tainting Percentage
        Tainting = (Misstatement Amount / Book Value of Item) × 100%

Step 3: For each misstatement, calculate the Incremental Allowance (IA)
        IA = (Additional RF for this overstatement count - Previous RF) × SI

Step 4: Calculate Upper Limit on Misstatement (ULM)
        ULM = BP + Sum of all Incremental Allowances

Step 5: Compare ULM to Tolerable Misstatement
        If ULM ≤ TM → Balance is NOT materially misstated (at the specified risk level)
        If ULM > TM → Balance MAY BE materially misstated; consider additional procedures
```

**MUS Worked Example:**

Given:
- Population Book Value (BV) = $5,000,000
- Tolerable Misstatement (TM) = $200,000
- Risk of Incorrect Acceptance = 5%
- Expected 0 overstatements (RF = 3.00)
- Expected error rate = 0 (no adjustment)

Step 1: Sampling Interval
```
SI = TM / RF = $200,000 / 3.00 = $66,667
```

Step 2: Sample Size
```
n = (BV × RF) / TM = ($5,000,000 × 3.00) / $200,000 = 75 items
```

Step 3: Selection
- Random start = $23,417
- Select items at cumulative amounts: $23,417; $90,084; $156,751; ... (adding SI each time)
- Any item with BV > $66,667 is automatically selected (100%)

Step 4: Testing — Assume 1 misstatement found:
- Item with BV = $50,000, audit value = $47,000 → Misstatement = $3,000
- Tainting = $3,000 / $50,000 = 6.0%

Step 5: Evaluation
```
BP = RF for 0 overstatements at 5% risk × SI = 3.00 × $66,667 = $200,001

Incremental Allowance for 1st misstatement:
  IA = (RF for 1 overstatement at 5% - RF for 0 overstatements at 5%) × SI
  IA = (4.75 - 3.00) × $66,667 = 1.75 × $66,667 = $116,667

ULM = BP + IA = $200,001 + $116,667 = $316,668

Compare: ULM ($316,668) > TM ($200,000)
CONCLUSION: Upper limit exceeds tolerable misstatement → Consider additional procedures or modify risk assessment
```

† Rounding differences ≤$1 are immaterial.

### 6.4 Variables Sampling

**Three Methods:**

| Method | Description | When to Use |
|--------|-------------|-------------|
| **Mean-per-Unit (MPU)** | Estimates population value using average audited value × population size | When book values unavailable or unreliable |
| **Difference Estimation** | Estimates average difference between book and audited values; applies to population | When many differences expected; population size known |
| **Ratio Estimation** | Estimates ratio of audited-to-book values; applies ratio to total book value | When differences are proportional to book values |

**Variables Sampling Sample Size Formula:**
```
n = (Z × σ / A)²

where:
  Z = Z-value for desired confidence level
      90% confidence: Z = 1.64
      95% confidence: Z = 1.96
      99% confidence: Z = 2.58
  σ = Estimated standard deviation of population
  A = Desired precision = TM - Expected Misstatement

Adjusted for finite population:
  n_adj = n / (1 + n/N)
  where N = population size
```

**For difference and ratio estimation, precision must be expressed per item:**

```
n = (Z × σ / A_per_item)²

where:
  A_per_item = A / N   (desired aggregate precision divided by population size)

Note: When using difference/ratio estimation, precision must be expressed per
item (A/N), not in aggregate, because the projection multiplies the per-item
estimate by N. Using aggregate precision directly in the formula produces an
artificially tiny sample size that understates the required n.
```

**Estimating σ (Population Standard Deviation):**

Since σ is typically unknown before testing, estimate it using one of the following methods:

1. **Pilot sample:** Select a small preliminary sample (≥30 items), compute the sample standard deviation (s), and use it as the estimate of σ. The pilot sample items can be included in the final sample.
2. **Prior-year data:** Use the standard deviation from the prior year's audit sample as the estimate, adjusting for known changes in the population. Document the basis for assuming prior-year variability is representative.
3. **Range rule (quick approximation):** σ ≈ Range / 4 (for approximately normal distributions). Use the range of a small sample or the expected range of the population. This is less precise and should be replaced with pilot sample data when available.

**Document the method used to estimate σ and any assumptions made.** If σ is underestimated, the sample will be too small and precision will be less than desired; if overestimated, the sample will be larger than needed but precision will exceed requirements.

**Projection Formulas:**

```
MPU:    Estimated Population Value = x̄ × N
        where x̄ = sample mean of audited values, N = population size

Difference:  Projected Misstatement = d̄ × N
            where d̄ = sample mean difference (audit value - book value)

Ratio:      Estimated Population Value = (Σ audit values / Σ book values) × Total Book Value
            Projected Misstatement = Estimated Population Value - Total Book Value
```

### 6.5 Non-Statistical Sampling (AS 2315.03, .45)

Nonstatistical sampling, when properly applied, CAN provide sufficient evidence. Sample size should be comparable to or larger than an efficient statistical sample (AS 2315.23A, .38).

**When to use:**
- Populations too small for statistical significance
- Auditor has special knowledge of specific items
- Professional judgment sufficient given risk assessment
- Cost of statistical design exceeds benefit
- Haphazard selection is appropriate (all items have opportunity for selection)

**Required documentation for non-statistical sampling:**
1. Rationale for non-statistical approach
2. How sample size was determined (factors considered: risk level, population size, variability, prior experience)
3. How items were selected (haphazard, key items, etc.)
4. Evaluation methodology (comparison to tolerable misstatement/deviation rate)
5. Consideration of sampling risk even though not quantified
6. Qualitative evaluation of misstatements

**Agent behavior:** When documenting non-statistical sampling, ALWAYS state the rationale for the approach and how sampling risk was considered even though not quantified.

### 6.6 Sequential Sampling (Emerging — per arXiv:2604.06116)

Recent research (Kato & Nakagawa, 2026) formulates audit sampling with sequentially collected items as a sequential testing problem.

**Key principles:**
- Defines null hypothesis (deviation rate ≤ tolerable) and alternative (deviation rate > tolerable)
- Specifies stopping and decision rules with exact sequential boundary conditions
- Calibrates boundaries via Monte Carlo simulation at least-favorable deviation rates
- Provides ex ante control of decision error probabilities
- Most suited to attribute auditing and deviation-rate auditing (tests of controls)
- Extensible to one-sided, two-stage, and truncated designs

**When to consider:** Large control-testing populations where early stopping saves effort; continuous monitoring environments.

**Documentation:** If using sequential sampling, document the stopping rule, boundary conditions, error probabilities, and the point at which testing was terminated.

### 6.7 ML-Enhanced Sampling (Emerging — per arXiv:2403.14069)

Research (Sheu & Liu, 2024) demonstrates integration of Naive Bayes classifier with sampling.

**Three approaches:**
1. **User-based:** Samples symmetric around median of classified group (≈ monetary + variable sampling)
2. **Item-based:** Asymmetric sampling based on posterior probabilities for riskier items (≈ nonstatistical + monetary sampling)
3. **Hybrid:** Balances representativeness and riskiness

**Representativeness Index:** Primary metric — how well samples represent population characteristics.

**Benefits:** Unbiased samples, handles complex patterns and correlations, improves efficiency for big data.

**Limitations:** Classification accuracy dependence, prior probability range constraints, requires validation of ML model.

**Documentation requirements:** If using ML-enhanced sampling, document the ML model used, training data, feature selection, classification approach, posterior probability thresholds, and how sampling risk was assessed.

### 6.8 Dual-Purpose Sampling (AS 2315.44)

- Samples designed for BOTH test of controls AND substantive test
- Sample size = **larger** of the two separate required samples
- Evaluate deviations and misstatements **SEPARATELY** using respective risk levels
- Requires preliminary assessment of acceptably low risk of control deviation
- Document that the sample was designed for dual purposes and explain the rationale

### 6.9 Sample Selection Methods

| Method | Procedure | Appropriate For | Documentation |
|--------|-----------|-----------------|---------------|
| **Random** | Every item has equal probability; use random number generator | Statistical sampling | Document random number seed, range, items selected |
| **Systematic** | Select every nth item after random start | Statistical and nonstatistical | Document random start, interval, items selected |
| **PPS (Probability-Proportional-to-Size)** | Selection probability proportional to dollar amount | MUS | Document sampling interval, random start, items selected |
| **Haphazard** | Select without conscious bias; all items have opportunity | Nonstatistical | Document selection rationale; no pattern should exist |
| **Stratified** | Divide population into subgroups (strata); sample from each | All methods when population has significant variability | Document strata definition, sample per stratum, basis for stratification |
| **Key Items / Judgmental** | Select specific items based on risk, size, characteristics | Nonstatistical; specific-item testing | Document basis for each item selected; results NOT projected |

---

## 7. Audit Risk Model

### 7.1 Model: AR = IR × CR × AP × TD

```
AR = Allowable Audit Risk (typically 5% or 10%)
IR = Inherent Risk
CR = Control Risk
AP = Risk that analytical procedures fail to detect misstatement
TD = Allowable risk of incorrect acceptance for substantive test of details
```

**Per AS 2315 Appendix:**
- Audit risk is the risk that the auditor may unknowingly fail to appropriately modify the opinion on financial statements that are materially misstated
- AR is set by the auditor (typically 5% for public companies, 10% may be used)
- IR and CR are assessed by the auditor based on risk assessment procedures (AS 2110)
- AP depends on the nature and precision of analytical procedures
- TD is the risk component that the auditor controls through the nature, timing, and extent of substantive tests of details

**Cross-reference:** For risk assessment procedures and identification of risks of material misstatement, see AS 2110 (Identifying and Assessing Risks of Material Misstatement). Risk assessment drives the IR and CR assessments that feed into the audit risk model.

### 7.2 Computing TD (Detection Risk for Substantive Tests of Details)

```
TD = AR / (IR × CR × AP)
```

**Worked Example:**

```
Given:
  AR = 5%  (0.05) — allowable audit risk
  IR = 80% (0.80) — high inherent risk (complex revenue recognition)
  CR = 60% (0.60) — moderate control risk (some controls ineffective)
  AP = 50% (0.50) — moderate risk AP doesn't detect (analytical procedures limited)

Calculate:
  TD = AR / (IR × CR × AP)
  TD = 0.05 / (0.80 × 0.60 × 0.50)
  TD = 0.05 / 0.24
  TD = 0.2083 ≈ 20.8%

Interpretation:
  The auditor must design substantive tests of details such that the risk of
  incorrect acceptance does not exceed approximately 21%. This means a RIGOROUS
  substantive testing program is needed — larger sample sizes, more precise procedures.
```

### 7.3 Risk Types Summary

| Risk Type | Direction | Effect | Impact | Standard |
|-----------|-----------|--------|--------|----------|
| Risk of Incorrect Acceptance (substantive) | Concluding balance is NOT misstated when it IS | Affects EFFECTIVENESS | **More serious** — auditor misses material misstatement | AS 2315.12 |
| Risk of Incorrect Rejection (substantive) | Concluding balance IS misstated when it is NOT | Affects EFFICIENCY | Less serious — additional work but correct conclusion | AS 2315.12 |
| Risk of Assessing CR Too Low (controls) | Assessing CR < true effectiveness | Affects EFFECTIVENESS | **More serious** — auditor relies on ineffective controls | AS 2315.12 |
| Risk of Assessing CR Too High (controls) | Assessing CR > true effectiveness | Affects EFFICIENCY | Less serious — auditor does more substantive work than needed | AS 2315.12 |

> **Note on statistical terminology:** In some audit literature, effectiveness risks (incorrect acceptance, assessing CR too low) are associated with Type I / alpha risk, and efficiency risks (incorrect rejection, assessing CR too high) are associated with Type II / beta risk. However, AS 2315 does not use these statistical labels. Use the official AS 2315 terminology in workpapers, and if statistical labels are needed for reference, include them as clearly labeled footnotes or a separate column.

**Agent behavior:** ALWAYS distinguish between effectiveness risks and efficiency risks in sampling documentation. Effectiveness risks are more serious and require more conservative sample sizes.

### 7.4 AS 2315 Appendix — Risk Assessment Matrix (Table 2)

This matrix shows how combinations of assessed IR, CR, and AP risk levels determine the required TD (and thus the extent of substantive tests of details), assuming AR = 5%.

| IR Assessment | CR Assessment | AP Assessment | Combined Risk (IR × CR × AP) | Required TD (AR / Combined) | Extent of Substantive Detail Testing |
|---------------|---------------|---------------|----------------------------|----------------------------|------------------------------------|
| Maximum (100%) | Maximum (100%) | High (100%) | 1.00 | 5% | Maximum — very large sample; year-end testing required |
| High (80%) | High (80%) | High (80%) | 0.512 | ~10% | Very extensive — large sample required |
| High (80%) | High (80%) | Moderate (50%) | 0.32 | ~15.6% | Extensive — large sample required |
| High (80%) | Moderate (50%) | Moderate (50%) | 0.20 | 25% | Moderate-large sample required |
| Moderate (50%) | Moderate (50%) | Moderate (50%) | 0.125 | 40% | Moderate sample adequate |
| Moderate (50%) | Low (30%) | Low (20%) | 0.03 | >100%¹ | Minimal detail testing; AP may be primary substantive evidence |
| Low (20%) | Low (20%) | Low (10%) | 0.004 | >100%¹ | Minimal to no detail testing; rely on AP and controls |

¹ When computed TD exceeds 100% (or 1.0), the combined risk of IR, CR, and AP is so low that any substantive test of details will provide sufficient assurance. The auditor may rely primarily on analytical procedures and tests of controls.

**Required TD → Sample Size Relationship (MUS):**

| Required TD Level | Approximate RIA for MUS | Reliability Factor (0 overstatements) | Sample Size Implication |
|-------------------|------------------------|--------------------------------------|------------------------|
| Very Low (≤5%) | 1% RIA or lower | ≥4.61 | Very large sample |
| Low (5–10%) | 1–5% RIA | 3.00–4.61 | Large sample |
| Moderate (10–30%) | 5–10% RIA | 2.31–3.00 | Moderate sample |
| High (30–50%) | 10–15% RIA | 1.90–2.31 | Small sample |
| Very High (>50%) | 15–20% RIA | 1.61–1.90 | Minimal sample |

---

## 8. Five-Part Finding Format

Every audit finding MUST be documented using all five mandatory elements:

**Mandatory 5 Parts (C-C-C-E-R):** Condition, Criteria, Cause, Effect, Recommendation. These are required for every finding and are the minimum acceptable documentation format.

**Recommended Additions:** Management Response and Follow-Up are strongly recommended additions that enhance the completeness and actionability of findings but are not mandatory elements of the finding itself.

### 8.1 Condition (What Is)

- Factual description of the current state observed during the audit
- What was found — specific, measurable, objective
- Reference supporting workpapers
- Avoid opinions or judgments in this section
- Include quantitative data where measurable

### 8.2 Criteria (What Should Be)

- Standard, law, regulation, policy, or expectation against which condition is measured
- Reference the specific standard (e.g., "Per PCAOB AS 2201...", "Per company policy XYZ-001...")
- This is the "yardstick" for evaluation
- Must be authoritative and relevant

### 8.3 Cause (Why the Difference Exists)

- Root cause analysis of why condition differs from criteria
- Contributing factors: people, process, technology, or environment
- Go beyond surface-level explanation — use "5 Whys" or similar technique when appropriate
- May involve multiple causes; prioritize by significance

### 8.4 Effect (So What / Impact)

- Actual or potential impact of the condition
- **Quantify where possible** — financial, operational, compliance impact
- Distinguish **actual effect** (known, measurable) from **potential effect** (reasonably possible)
- Consider both direct and indirect effects

### 8.5 Recommendation (What to Do)

- Specific, actionable corrective actions
- Prioritize by risk/impact (highest first)
- Identify responsible party and target timeline
- May include multiple options with pros/cons
- Should be practical and proportionate to the finding

### 8.6 Severity Classification

| Severity | Criteria | Reporting |
|----------|----------|-----------|
| **Material Weakness** | Deficiency or combination resulting in reasonable possibility material misstatement won't be prevented/detected | Report to audit committee; report in auditor's report on ICFR (AS 2201; AS 1305) |
| **Significant Deficiency** | Deficiency less severe than material weakness but important enough to merit attention | Report to audit committee (AS 1305) |
| **Other Finding (Control Deficiency)** | Control deficiency or observation not meeting significant deficiency threshold | Communicate to management; document in workpapers |

### 8.7 Finding Example

```
FINDING #3
WP INDEX: C-4.2
SEVERITY: Significant Deficiency
ASSERTION: Completeness (Accounts Payable)

CONDITION:
During testing of the accounts payable cutoff process (WP C-4.2), we identified
12 of 75 selected invoices (16%) that were recorded in the incorrect period.
Specifically, 8 invoices totaling $342,500 were recorded in January 2025 for
goods received in December 2024, and 4 invoices totaling $128,750 were recorded
in December 2024 for goods received in January 2025.

CRITERIA:
Per ASC 606 and ASC 330, expenses should be recorded in the period in which the
related goods or services are received (matching principle). Per company AP Policy
AP-200, invoices must be matched to receiving reports and recorded within the
period of receipt.

CAUSE:
The receiving department does not notify accounts payable of goods received on
the last 3 business days of each month. The three-way match process relies on
the supplier invoice date rather than the receiving report date for cutoff
determination. Additionally, there is no automated cutoff procedure in the ERP
system to flag late-recorded receipts.

EFFECT:
ACTUAL: $342,500 of expenses were understated in 2024 and overstated in 2025;
$128,750 of expenses were overstated in 2024 and understated in 2025. Net effect
on 2024 pre-tax income is an understatement of $213,750.
POTENTIAL: If this condition exists throughout the year, the cumulative effect on
financial statements could be material. The absence of cutoff controls creates
risk of material misstatement in accounts payable and accrued expenses.

RECOMMENDATION:
1. Implement automated cutoff procedures in the ERP system to flag goods
   received within 3 days of period-end that have not been invoiced (Responsible:
   IT Director; Target: Q2 2026)
2. Require receiving department to generate daily receiving reports through the
   last business day of each month and transmit to AP (Responsible: Warehouse
   Manager; Target: Q1 2026)
3. Perform monthly cutoff testing by internal audit for 6 months to validate
   remediation (Responsible: Internal Audit Director; Target: Q3 2026)
```

---

## 9. Re-Performance and Re-Computation Documentation (AS 1105.19–.20)

### 9.1 Definitions

- **Recalculation (AS 1105.19):** Checking mathematical accuracy of information or computations performed by the company.
- **Reperformance (AS 1105.20):** Independent execution of procedures or controls that were originally performed as part of the entity's internal control.

### 9.2 Required Documentation

For every re-performance or re-computation, document:

1. **Source of original computation/procedure** — What document, system, or person provided the original?
2. **Procedure independently re-performed** — What exactly did the auditor do?
3. **Inputs used** — What data was used, with source identification for each input
4. **Method/formula applied** — What computation or procedure was re-executed?
5. **Result of independent re-performance** — What did the auditor calculate/observe?
6. **Comparison to original result** — Does the independent result agree with the original?
7. **Conclusion** — Agrees / Does not agree
8. **If not in agreement:** Investigation of difference, root cause determination, implications for other assertions

### 9.3 Re-Performance Template

```
RE-PERFORMANCE DOCUMENTATION
═════════════════════════════
WP INDEX: [Reference]
OBJECTIVE: [What is being re-performed]

ORIGINAL:
  Source:           [Document/system/person]
  Method/Formula:   [Description]
  Inputs:           [List with sources]
  Result:           [Original computed value]

INDEPENDENT RE-PERFORMANCE:
  Procedure:        [Description of what auditor did]
  Inputs:           [List with sources — may differ from original]
  Method/Formula:   [Description]
  Result:           [Auditor's computed value]

COMPARISON:
  Agrees:           [Yes / No]
  Difference:        [Amount, if any]
  Investigation:     [If difference, what was found]
  Root Cause:        [If difference, why did it occur]
  Implications:      [If difference, what other areas may be affected]

CONCLUSION: [Statement of conclusion]
TICKMARK: △ [Recomputed; see above]
```

---

## 10. Workpaper Creation Workflow (7 Steps)

### Step 1: Planning Documentation

**Actions:**
- Create permanent file (A-series): entity info, organizational structure, business description
- Document engagement acceptance/continuance (per QC 1000 requirements as applicable)
- Prepare audit strategy/planning memorandum (B-series)
- Document risk assessment procedures and results (B-series per AS 2110)
- Create risk assessment summary linking risks → responses (per AS 2110 and AS 2301)
- Establish materiality and tolerable misstatement (per AS 2105)
- Document understanding of internal control (C-series; COSO 5 components)
- Create tickmark legend workpaper (B-5 or similar)
- Create cross-reference index (B-6 or similar)

**Quality checkpoint:** Planning documentation complete → preparer signs off → reviewer confirms all required elements present

### Step 2: Internal Control Documentation

**Actions:**
- Document flow of transactions (walkthrough procedures per AS 2301)
- Identify key controls and assess their operating effectiveness
- Document COSO components:
  - Control Environment (Principles 1–5): Tone at top, org structure, competence, accountability
  - Risk Assessment (Principles 6–9): Entity-level & activity-level risks, fraud risk, change management
  - Control Activities (Principles 10–12): Policies/procedures, IT controls, segregation of duties, authorization
  - Information & Communication (Principles 13–15): Financial reporting info, internal/external communication
  - Monitoring (Principles 16–17): Ongoing/periodic monitoring, deficiency evaluation & communication
- Evaluate IT general controls and application controls (N-series)
- Document assessment of control risk for each relevant assertion

**Quality checkpoint:** IC documentation complete → preparer signs off → reviewer confirms risk-to-control mapping

### Step 3: Sampling Documentation

**Actions:**
- For each area requiring sampling, create sampling workpaper (I-series)
- Document sampling plan per Section 6 above
- Include all required elements: objective, population, method, parameters, sample size, selection, evaluation, conclusion
- Record all exceptions and misstatements found
- Perform qualitative evaluation

**Quality checkpoint:** Sampling workpaper complete → preparer signs off → reviewer confirms sample size is adequate and evaluation is appropriate

### Step 4: Substantive Testing Documentation

**Actions:**
- Document each test: objective, procedure, sample, results, conclusion (D–H series)
- Create lead schedules tying to financial statements (K-series)
- Document re-performance and re-computation per Section 9
- Document analytical procedures and investigation of differences (J-series)
- For each procedure, explicitly state the assertion(s) addressed

**Quality checkpoint:** Substantive testing complete → preparer signs off → reviewer confirms all assertions are addressed and conclusions are supported

### Step 5: Findings Documentation

**Actions:**
- Document ALL findings using the 5-part format per Section 8
- Track accumulated misstatements (quantitative AND qualitative)
- Identify and document significant findings per AS 1215.12 (all 8 categories)
- Evaluate findings for severity (material weakness, significant deficiency, other)
- Obtain and document management responses

**Quality checkpoint:** All findings documented → preparer signs off → reviewer confirms 5-part format and severity classification

### Step 6: Completion Procedures

**Actions:**
- Prepare engagement completion document per AS 1215.13 (K-series)
- Obtain management representation letter (L-series)
- Evaluate subsequent events
- Summarize uncorrected misstatements (quantitative + qualitative evaluation)
- Determine overall conclusion and opinion per Section 13
- Document all significant findings/issues in the engagement completion document

**Quality checkpoint:** Completion procedures done → preparer signs off → engagement partner review → EQR review

### Step 7: Review and Sign-off

**Actions:**
- Supervisory review per AS 1201 — document all review notes and their resolution
- Engagement partner review per AS 1215.15 — must be complete before report release
- Engagement quality review (EQR) per AS 1220 — for applicable engagements
- Document all review notes and their resolution in M-series
- Confirm documentation completion within 14 days of report release per AS 1215.14

**Quality checkpoint:** All reviews complete → all review notes resolved → documentation completion date recorded (≤14 days after report release)

---

## 11. Output Templates

### 11.1 Standard Workpaper Template

```
┌─────────────────────────────────────────────────────────────┐
│ CLIENT: [Name]           PERIOD: [FY ending date]          │
│ WORKPAPER INDEX: [A-1]   PREPARED BY: [Initials/Date]      │
│ SUBJECT: [Title]         REVIEWED BY: [Initials/Date]      │
├─────────────────────────────────────────────────────────────┤
│ OBJECTIVE: [Purpose of this workpaper]                      │
│ SOURCE: [Where data came from]                             │
│ ASSERTION(S): [Existence/Completeness/Valuation/etc.]       │
├─────────────────────────────────────────────────────────────┤
│ PROCEDURE:                                                 │
│ [Step-by-step description of what was done]             │
│                                                             │
│ DATA / ANALYSIS:                                            │
│ [Tables, computations, comparisons]                        │
│                                                             │
│ TICKMARK LEGEND:                                            │
│ Tickmark  Description                                       │
│ ✓         [Explanation]                                     │
│ ∧         [Explanation]                                     │
│                                                             │
│ CONCLUSION: [Clear statement of conclusion reached]         │
│ EXCEPTIONS: [None / Description if any]                     │
│ CROSS-REFS: [Related workpaper indices]                     │
├─────────────────────────────────────────────────────────────┤
│ REVIEW NOTES:                                               │
│ [Date] [Reviewer] [Note] [Resolution]                      │
└─────────────────────────────────────────────────────────────┘
```

### 11.2 Sampling Workpaper Template

```
SAMPLING PLAN AND EVALUATION
════════════════════════════
CLIENT:                  PERIOD:
WP INDEX:                PREPARED BY:           REVIEWED BY:

SECTION A: PLANNING
────────────────────
Objective:              [What the sample is testing]
Population:             [Description and size (N =)]
Sampling Unit:          [Individual item / Monetary unit]
Sampling Approach:      [Statistical / Nonstatistical]
Method:                 [Attribute / MUS / Variables / etc.]
Tolerable Misstatement/Rate:  [Amount or %]
Expected Misstatement/Rate:   [Amount or %]
Risk Level:             [Risk of incorrect acceptance/assessing CR too low %]
Confidence Level:       [e.g., 95%, 90%]
Required Sample Size:   [Calculation shown with formula and inputs]

SECTION B: SELECTION
────────────────────
Selection Method:       [Random / Systematic / PPS / Haphazard]
Random Start:           [If systematic or PPS]
Sampling Interval:      [If MUS/systematic]
Items Selected:         [Identified by: check #s, invoice #s, dates]

SECTION C: PERFORMANCE
────────────────────
Procedure Applied:      [Description of audit procedure per item]
Exceptions/Misstatements Found:
  Item ID | Description | Amount | Cause | Type (Error/Fraud)

SECTION D: EVALUATION
────────────────────
Sample Deviation Rate / Misstatement: [Rate or amount]
Projection Method:       [Ratio / Difference / Mean-per-unit]
Projected Misstatement/Rate: [Amount or rate calculated]
Upper Limit on Misstatement: [For MUS — Basic Precision + Increments]
Comparison to Tolerable: [ULM or projected vs TM or tolerable rate; state whether ≤ or >]
Sampling Risk Assessment: [Acceptable / Unacceptable]

SECTION E: QUALITATIVE EVALUATION
────────────────────
Nature of Misstatements: [Error vs. fraud, pattern analysis]
Cause Analysis:          [Understanding vs. carelessness, etc.]
Relationship to Other Work: [Implications for other assertions]

SECTION F: CONCLUSION
────────────────────
Conclusion:              [Population is/is not materially misstated]
Impact on Risk Assessment: [Whether reassessment needed per AS 2315.28]
Cross-References:        [Related WP indices]
```

### 11.3 Finding Documentation Template

```
AUDIT FINDING
═══════════════
FINDING #: [Sequential number]
WP INDEX:  [Reference]
SEVERITY:  [High / Medium / Low — or Material Weakness / Significant Deficiency / Other]
ASSERTION: [Relevant financial statement assertion]

NOTE: The 5 mandatory parts of every audit finding are Condition-Criteria-Cause-Effect-
Recommendation (C-C-C-E-R). Management Response and Follow-Up are recommended additions
that enhance actionability but are not mandatory elements.

CONDITION:
[Description of what was found — factual, objective, specific]

CRITERIA:
[Standard, policy, regulation, or expectation that applies]

CAUSE:
[Root cause analysis — why the condition exists]

EFFECT:
[Actual and/or potential impact — quantify where possible]

RECOMMENDATION:
[Specific corrective action, responsible party, timeline]

MANAGEMENT RESPONSE:  [Recommended addition]
[Agreement/disagreement, planned action, target date]

FOLLOW-UP:  [Recommended addition]
[Status, remaining actions, target completion]
```

### 11.4 Engagement Completion Document Template (Per AS 1215.13)

```
ENGAGEMENT COMPLETION DOCUMENT
══════════════════════════════
CLIENT:                      PERIOD:
ENGAGEMENT PARTNER:          EQR PARTNER:

1. SIGNIFICANT FINDINGS/ISSUES (per AS 1215.12):
   a. Accounting principles matters                    [WP Ref: ___]
   b. Misstatements/deficiencies identified           [WP Ref: ___]
   c. Accumulated misstatements summary               [WP Ref: ___]
   d. Disagreements within engagement team             [WP Ref: ___]
   e. Difficulties in applying procedures              [WP Ref: ___]
   f. Changes in risk assessments                      [WP Ref: ___]
   g. Significant risks and responses                  [WP Ref: ___]
   h. Report modification matters                      [WP Ref: ___]

2. EVALUATION OF UNCORRECTED MISSTATEMENTS:
   [Quantitative summary + Qualitative factors per AS 2810]

3. OVERALL CONCLUSION:
   [Opinion determination: Unqualified/Qualified/Adverse/Disclaimer]

4. INDEPENDENCE COMPLIANCE:
   [Confirmation of firm and engagement team independence]

5. REVIEW COMPLETION:
   Partner review completion date: ___
   EQR completion date: ___
   Documentation completion date: ___ (not >14 days after report release)
```

### 11.5 Tickmark Legend Template

```
TICKMARK LEGEND
═══════════════
CLIENT:                  PERIOD:
WP INDEX: B-5            PREPARED BY:           REVIEWED BY:

STANDARD TICKMARKS (per Section 3.3):
─────────────────────────────────────
Symbol  Meaning                              Documentation Reference
✓       Verified to source document          [Identify source]
∧       Agrees to prior year                 [Identify prior-year WP]
∨       Footed / cross-footed                [Specify computation]
○       Tested via sampling                  [Reference sampling WP]
□       Confirmed with third party           [Identify confirment and date]
△       Recomputed / recalculated            [Show computation]
※       Exception noted                      [Describe exception]
◆       Re-performed                         [Describe procedure re-performed]

CUSTOM TICKMARKS (engagement-specific):
────────────────────────────────────────
Symbol  Meaning                              First Used (WP Index)   Date Defined
[α]     [Custom meaning 1]                   [WP index]              [Date]
[β]     [Custom meaning 2]                   [WP index]              [Date]
[γ]     [Custom meaning 3]                   [WP index]              [Date]

RULES:
1. Every tickmark used in any workpaper MUST appear in this legend with explanation.
2. Standard tickmark symbols must NOT be reused with different meanings.
3. Custom tickmarks must be explained at least once where first used AND in this legend.
4. Add new custom tickmarks to this legend as they are defined during the engagement.
```

### 11.6 Cross-Reference Index Template

```
CROSS-REFERENCE INDEX
═════════════════════
CLIENT:                  PERIOD:
WP INDEX: B-6            PREPARED BY:           REVIEWED BY:

SOURCE → WORKPAPER → CONCLUSION
────────────────────────────────
From WP  This WP  To WP  Description                      Assertion
──────── ──────── ────── ─────────────────────────────── ──────────
B-2      D-1      K-1    Revenue testing — existence       Existence
B-2      D-2      K-1    Revenue testing — cutoff          Cutoff/Completeness
B-3      E-1      K-2    AP testing — completeness         Completeness
C-3      F-1      K-1    Inventory observation              Existence/Valuation
I-1      D-1      K-3    MUS sampling — AR valuation       Valuation
A-1      B-1      —      Entity info — permanent file      N/A

RISK-TO-RESPONSE LINKAGE (per AS 2110 and AS 2301):
───────────────────────────────────────────────────
Risk ID  Risk Description                    Response WP   Procedure Type
───────  ──────────────────────────────────  ────────────  ──────────────
R-01     Revenue recognition complexity      D-1, D-2      Substantive
R-02     AP cutoff weakness                  E-1, C-4.2    Control + Substantive
R-03     Inventory obsolescence              F-2, J-2      Analytical + Substantive

NOTES:
1. Cross-references must be bidirectional — if D-1 references B-2, then B-2 must also reference D-1.
2. Update this index whenever a new workpaper is created or a cross-reference is added.
3. Risk-to-response linkage must trace every identified risk to the procedure(s) that address it.
```

### 11.7 Risk Assessment Summary Template

```
RISK ASSESSMENT SUMMARY
═══════════════════════
CLIENT:                  PERIOD:
WP INDEX: B-2            PREPARED BY:           REVIEWED BY:

RISK ASSESSMENT PROCEDURES (per AS 2110):
─────────────────────────────────────────
Procedure                      WP Ref   Date Completed  Performed By
Inquiries of management        B-2.1    [Date]          [Initials]
Analytical procedures (planning) B-2.2  [Date]          [Initials]
Observation/inspection          B-2.3    [Date]          [Initials]
Prior-year review               B-2.4    [Date]          [Initials]

SIGNIFICANT RISKS IDENTIFIED:
──────────────────────────────
Risk   Description               FS Area    Assertion(s)   IR   CR   Likelihood   Magnitude   Significant?
────── ────────────────────────── ────────── ───────────── ──── ──── ──────────── ─────────── ─────────────
R-01   [Risk description 1]      Revenue    Existence/Val  High High  Probable     Material    Yes
R-02   [Risk description 2]      AP        Completeness   Mod  Mod   Reasonable   Material    No
R-03   [Risk description 3]      Inventory Valuation       High Low   Probable     Moderate    Yes

FRAUD RISK ASSESSMENT (per AS 2110):
────────────────────────────────────
Fraud Risk Factor         Present?   Description                        WP Ref
Incentive/Pressure       [Y/N]      [Description]                      B-2.5
Opportunity              [Y/N]      [Description]                      B-2.5
Attitude/Rationalization [Y/N]      [Description]                      B-2.5
Management Override       [Y/N]      [Description]                      B-2.5

RISK RESPONSE SUMMARY:
─────────────────────
Risk   Planned Response           Procedure Type    Timing      WP Ref
────── ────────────────────────── ────────────────── ─────────── ───────
R-01   Expanded substantive       Detail testing     Year-end   D-1, D-2
R-02   Test controls + cutoff     Control + Subst.   Year-end   C-4.2, E-1
R-03   Specialist + observation   Detail testing     Physical   F-2

RISK MODEL CALCULATIONS:
─────────────────────────
FS Area     IR     CR     AP     TD     AR
Revenue     80%    60%    50%    20.8%  5%  (calculated)
AP          50%    50%    40%    50%    5%  (calculated)
Inventory   60%    30%    50%    55.6%  5%  (calculated)

CROSS-REFERENCES:
Planning Memo: B-1
Materiality Memo: B-3
Internal Control Evaluation: C-1 through C-5
Significant Risks: AS 2110, AS 2301
```
## 11.8 IPE Reliability and Validation Log Template

| IPE Validation Field | Auditor Documentation / Testing Results |
| :--- | :--- |
| Workpaper Index Reference | [e.g., C-4.3] |
| Description of IPE | [e.g., FY25 Inventory Ageing Report as of 12/31/25] |
| Source System & Report Name | [e.g., SAP ECC 6.0 - ZINV_AGE_RPT] |
| Purpose of Use | [e.g., Used as the base population for substantive testing in WP F-2] |
| Completeness Procedures | `[ ]` Tied report total ($X,XXX,XXX) to GL Account #### (See WP F-1 for roll-forward reconciliation).<br>`[ ]` Verified sequential parameters from invoice #XXXX to #YYYY. |
| Accuracy Procedures | `[ ]` Selected a sample of [XX] items and vouched to original supplier invoices.<br>`[ ]` Independently recalculated the client's Excel aging logic/formulas with zero variances noted. |
| ITGC Reference | `[ ]` Confirmed ITGCs over report parameters are operating effectively (Refer to IT Audit WP IT-3.2). |
| Standard Tickmarks Used | **✓** = Agreed report balance to General Ledger trial balance.<br>**Δ** = Independently re-performed spreadsheet formulas for accuracy. |
| Conclusion | Based on the procedures performed above, the information produced by the entity is sufficient, accurate, and complete, and is deemed reliable for use as audit evidence. |

---

## 12. Opinion Determination Guide (Per AS 3105)

### 12.1 Decision Flow

```
Is the audit scope limited?
├── YES: Is the scope limitation so material and pervasive
│   that a qualified opinion is insufficient?
│   ├── YES → DISCLAIMER OF OPINION (AS 3105.07)
│   └── NO  → QUALIFIED OPINION — scope limitation (AS 3105.04–.05)
│
└── NO: Are there departures from GAAP/APB opinions?
    ├── YES: Is the GAAP departure so material and pervasive
    │   that a qualified opinion is insufficient?
    │   ├── YES → ADVERSE OPINION (AS 3105.06)
    │   └── NO  → QUALIFIED OPINION — GAAP departure (AS 3105.03)
    │
    └── NO → UNQUALIFIED OPINION (AS 3101)
```

### 12.2 Opinion Types — Conditions and Language

| Opinion | When Required | Report Language | Standard |
|---------|--------------|----------------|---------|
| **Unqualified** | Financial statements present fairly in all material respects | "In our opinion, the financial statements present fairly..." | AS 3101 |
| **Qualified ("Except For")** — Scope limitation | Unable to obtain sufficient appropriate evidence; limitation not so material as to require disclaimer | "Except for the effects of the adjustments, if any, as might have been determined had we been able to..." | AS 3105.04–.05 |
| **Qualified ("Except For")** — GAAP departure | Financial statements not in conformity with GAAP; departure not so material as to require adverse opinion | "Except for the effects of the matter discussed in Note X, the financial statements present fairly..." | AS 3105.03 |
| **Adverse** | GAAP departure so material and pervasive that qualification is insufficient | "In our opinion, because of the effects of the matters discussed in Note X, the financial statements do not present fairly..." | AS 3105.06 |
| **Disclaimer** | Scope limitation so material and pervasive that qualified opinion is insufficient; or independence impaired | "We do not express an opinion on the financial statements..." | AS 3105.07 |

### 12.3 Critical Audit Matters (AS 3101)

A **Critical Audit Matter (CAM)** is any matter arising from the current period audit that was communicated or required to be communicated to the audit committee, that involves:
- Accounts or disclosures that are material to the financial statements
- Especially challenging, subjective, or complex auditor judgment

**CAM documentation requirements:**
- Identify each CAM
- Explain why the matter is a CAM
- Describe how the CAM was addressed in the audit

### 12.4 Required Report Elements (Per AS 3101)

All audit reports must include:
1. Title: "Report of Independent Registered Public Accounting Firm"
2. Addressee
3. Opinion section
4. Basis for Opinion section
5. Critical Audit Matters (if applicable)
6. Signature, firm name, city/state
7. Date
8. Auditor tenure disclosure

---

## 13. Electronic Workpaper Requirements

### 13.1 Access Controls

- **Password protection** on all electronic workpaper files
- **Access logs** recording who accessed, modified, or printed each workpaper
- **Role-based access** — preparers, reviewers, and partners have appropriate access levels
- **Unauthorized access prevention** — controls consistent with AS 1215.16 (no unauthorized modification after completion)

### 13.2 Version Control and Audit Trail

- **Version control** must prevent unauthorized modification after documentation completion date
- **Audit trail** of ALL modifications (per AS 1215.16: date, person, reason for each change)
- **No deletion or discard** after documentation completion date (AS 1215.17)
- **Post-completion additions** must indicate: date, preparer name, and reason (AS 1215.16)

### 13.3 Digital Signatures

- Electronic sign-off capabilities must use **digital signatures** with authentication
- Sign-off must be attributable to the specific individual
- Timestamps must be automatically recorded and tamper-resistant
- Must meet the same requirements as physical sign-offs (per AS 1215.06)

### 13.4 Retention Compliance

- **7-year retention** from report release date (AS 1215.14)
- Must maintain **readability** throughout retention period
- **Format migration** plans for technology changes (e.g., software version upgrades)
- **Backup and disaster recovery** procedures
- Office issuing the report retains responsibility for all documentation (AS 1215.18)
- **PDF/A archival format** — For long-term electronic retention, use PDF/A (ISO 19005) format to ensure documents remain readable and self-contained throughout the 7-year retention period. PDF/A embeds fonts, prohibits external dependencies, and ensures rendering consistency across platforms. Document the archival format chosen and any format migration plans.

### 13.5 Long-Term Readability

- Use widely supported file formats when possible
- Document software versions used to create workpapers
- Maintain capability to produce readable copies throughout 7-year retention period
- Consider format conversion when software is deprecated
- **PDF/A** (ISO 19005) is the recommended archival format for electronic workpapers to ensure long-term readability without dependency on specific software versions

---

## 14. Review Standards

### 14.1 Supervisory Review (AS 1201)

- **Objective:** Ensure work performed meets quality standards and supports conclusions
- **Scope:** All workpapers should be reviewed by a supervisory team member
- **Timing:** Before report release
- **Documentation:** Review notes must be documented, tracked, and resolved
- **Requirements:** Reviewer must have appropriate competence and authority

### 14.2 Engagement Partner Review (AS 1215.15)

- Partner review must be **complete before report release**
- All necessary procedures must be complete before partner sign-off
- Partner must review significant judgments, risk assessments, and conclusions
- Partner review is not a sampling exercise — all significant matters must be reviewed

### 14.3 Engagement Quality Review — EQR (AS 1220)

**When required:**
- Listed issuer audits (public companies subject to PCAOB oversight)
- Other engagements as required by firm policy per QC 1000

**EQR requirements:**
- EQR reviewer must be a qualified partner or equivalent NOT on the engagement team
- EQR must evaluate significant judgments and conclusions
- EQR must be completed before report release
- EQR reviewer must not be overridden by the engagement team

**EQR documentation:**
- Date EQR completed
- EQR reviewer identification
- Matters reviewed
- Conclusions reached by EQR reviewer
- Any objections raised and their resolution

### 14.4 Review Notes Documentation

Every review note must include:
1. **Date** of the review note
2. **Reviewer** identification
3. **Workpaper referenced** (WP index)
4. **Description** of the review note (question, concern, request for additional work)
5. **Resolution** — How was the note resolved? (additional work performed, explanation provided, revision made)
6. **Clearance** — Reviewer initials/date acknowledging resolution

**Agent behavior:** Track all review notes in M-series workpapers. Ensure every review note has a corresponding resolution and clearance.

### 14.5 Reviewer Guidance for IPE Documentation
When reviewing workpapers that utilize client-prepared reports or data extracts, the reviewer must verify that:
*   [ ] The specific report name, system of origin, and file format are clearly documented.
*   [ ] There is clear, visual evidence (tickmarks and cross-references) showing how the population was verified for completeness against the general ledger.
*   [ ] The workpaper clearly concludes on the *reliability* of the data before drawing a conclusion on the primary audit objective.

## 15. Data Analytics in Audit (2024–2026 Trends)

### 15.1 Full-Population Testing

- **Purpose:** Test 100% of transactions as complement or alternative to sampling
- **When appropriate:** When data is electronic, population is accessible, and automated testing is cost-effective
- **Documentation:** Document the data analytics procedure, population scope, criteria, and all exceptions identified
- **Impact on sampling:** Reduces or eliminates sampling risk for the tested population; sampling may still be needed for items that cannot be tested via data analytics

### 15.2 ML-Based Risk Scoring

- Use ML models to score transaction risk for **targeted sampling**
- High-risk items selected for detailed testing; low-risk items may use reduced testing
- **Documentation:** Document ML model, risk factors, scoring methodology, and how results influence sample selection
- **Limitation:** ML-based selection is a form of judgmental sampling — results CANNOT be statistically projected to the population unless combined with random selection

### 15.3 Continuous Auditing / Continuous Monitoring

- Automated procedures running at regular intervals (daily, weekly, monthly)
- **Documentation:** Document the continuous procedures, frequency, parameters, and how exceptions are escalated
- Combine with periodic full-scope audit procedures

### 15.4 Automated Anomaly Detection

- **Autoencoder-based** approaches (per Schreyer et al.) detect unusual journal entries or transactions
- NLP for contract/transaction analysis
- **Documentation:** Document the anomaly detection methodology, model architecture, training data, threshold calibration, and findings

### 15.5 RPA for Evidence Gathering

- Robotic Process Automation for routine evidence collection (download statements, extract data)
- **Documentation:** Document the RPA procedure, source systems, validation of extracted data accuracy and completeness

### 15.6 COSO 2026 — Generative AI Controls

- New COSO guidance: "Achieving Effective Internal Control Over Generative AI" (2026)
- Requires documentation of controls over AI-generated outputs used in financial reporting
- **Key areas:** Data input controls, model validation, output verification, segregation of duties between AI and human reviewers

### 15.7 How Data Analytics Affects Sampling Risk

- If full-population testing is performed via data analytics, **sampling risk is zero** for the tested population
- However, **nonsampling risk remains** (AS 2315.11): inappropriate procedures, failure to recognize misstatements
- Data analytics results should be evaluated for both sampling and nonsampling risk
- Document the relationship between data analytics results and sampling conclusions

---

## 16. Quality Checklist

### 16.1 Pre-Engagement

- [ ] Engagement acceptance/continuance evaluated per QC 1000
- [ ] Independence confirmed (firm and engagement team)
- [ ] Engagement letter obtained and signed
- [ ] Prior-year workpapers reviewed (if continuing engagement)
- [ ] Planning team assembled with appropriate competence

### 16.2 During Engagement

- [ ] All workpapers have: purpose, source, conclusion (AS 1215.04)
- [ ] All workpapers satisfy experienced auditor standard (AS 1215.06A)
- [ ] All workpapers include 5W1H elements
- [ ] All workpapers have preparer and reviewer sign-off placeholders
- [ ] Evidence sufficiency and appropriateness evaluated (AS 1105.05–.08)
- [ ] Sampling adequacy verified (sample size, selection, evaluation)
- [ ] All tickmarks defined and explained
- [ ] Cross-referencing complete and bidirectional
- [ ] Risk-to-response linkage documented (per AS 2110 and AS 2301)
- [ ] All assertions addressed with appropriate procedures
- [ ] Inconsistent/contradictory information documented (AS 1215.08)

### 16.3 Completion

- [ ] All findings documented in 5-part format
- [ ] Uncorrected misstatements evaluated (quantitative + qualitative)
- [ ] Engagement completion document prepared (AS 1215.13)
- [ ] All 8 categories of significant findings addressed (AS 1215.12)
- [ ] Management representation letter obtained
- [ ] Subsequent events evaluated
- [ ] Opinion determination documented with rationale
- [ ] CAMs identified and documented (if applicable)

### 16.4 Post-Engagement

- [ ] Documentation completion within 14 days of report release (AS 1215.14–.15)
- [ ] 7-year retention plan established (AS 1215.14)
- [ ] No documentation deleted or discarded after completion date (AS 1215.17)
- [ ] All review notes resolved and cleared
- [ ] All post-completion additions documented: date, person, reason (AS 1215.16)

---

## 17. Compliance Validation Rules

The following rules are MANDATORY. Violation of any rule requires immediate correction.

1. **All workpapers must have:** purpose, source, conclusion, preparer, reviewer, dates — no exceptions
2. **All sampling workpapers must have:** objective, population description, sampling method, sample size rationale, selection method, results, evaluation, conclusion
3. **All findings must use the 5-part format:** Condition, Criteria, Cause, Effect, Recommendation
4. **All evidence must be assessed for relevance AND reliability** before reliance (AS 1105.05–.08)
5. **No documentation may be deleted after the documentation completion date** (AS 1215.17)
6. **All post-completion additions must identify: date, person, reason** (AS 1215.16)
7. **Oral evidence alone does not provide sufficient audit documentation for an experienced auditor** per AS 1215.06
8. **Inquiry alone is never sufficient** for audit evidence (AS 1105.17)
9. **All uncorrected misstatements must be evaluated** against tolerable misstatement (AS 2810)
10. **Documentation completion must occur within 14 days** of report release (AS 1215.14–.15)
11. **All significant findings must be documented** per AS 1215.12 (8 categories)
12. **Engagement partner review must be complete** before report release (AS 1215.15)
13. **Cross-referencing must be bidirectional** — from source to workpaper and from workpaper to conclusion

---

## 18. Cross-Reference Tables

### 18.1 AICPA ↔ PCAOB Crosswalk

| AICPA (AU-C) | PCAOB (AS) | Topic | Notes |
|--------------|-----------|-------|-------|
| AU-C 230 | AS 1215 | Audit Documentation | |
| AU-C 500 | AS 1105 | Audit Evidence | |
| AU-C 530 | AS 2315 | Audit Sampling | |
| AU-C 450 | AS 2810 | Evaluating Audit Results | AS 2810 is broader in scope; AU-C 450 focuses specifically on misstatement evaluation |
| AU-C 220 | QC 1000 | Quality Control | |
| AU-C 315 | AS 2110 | Risk Assessment | |
| AU-C 330 | AS 2301 | Responses to Risks | |
| AU-C 700 | AS 3101 | Opinion Reporting | |
| AU-C 705 | AS 3105 | Modified Opinions | |
| AU-C 260 | AS 1301 | Communications with Audit Committee | |

### 18.2 ISACA ↔ AICPA/PCAOB Crosswalk

| ISACA (ITAF) | AICPA/PCAOB | Key Differences |
|--------------|------------|-----------------|
| ITAF 2.2: Planning | AU-C 315 / AS 2110 | ITAF adds IT-specific risk factors (system complexity, data integrity, access controls) |
| ITAF 2.3: Execution | AU-C 330 / AS 2301 | ITAF includes CAAT/IT test procedures (CISA, CAATT approaches) |
| ITAF 2.4: Reporting | AU-C 700 / AS 3101 | ITAF includes IT-specific findings format |
| ITAF 3.0: Mgt Guidelines | N/A | ITAF-specific: governance and management guidelines |
| IS Audit Evidence | AS 1105 | ITAF: system-generated evidence reliability considerations |
| IS Sampling | AS 2315 | ITAF: CAATT-based sampling approaches |

### 18.3 COSO ↔ Workpaper Integration

| COSO Component | Principles | Workpaper Documentation |
|----------------|-----------|------------------------|
| **Control Environment** | 1–5 | Tone at top, organizational structure, competence, accountability (C-1 series) |
| **Risk Assessment** | 6–9 | Entity-level & activity-level risks, fraud risk, change management (C-2 series) |
| **Control Activities** | 10–12 | Policies/procedures, IT controls, segregation of duties, authorization (C-3 series) |
| **Information & Communication** | 13–15 | Financial reporting information, internal/external communication (C-4 series) |
| **Monitoring** | 16–17 | Ongoing/periodic monitoring, evaluation & communication of deficiencies (C-5 series) |

### 18.4 ISA ↔ PCAOB Crosswalk

| ISA | PCAOB AS | Notes |
|-----|---------|-------|
| ISA 230 | AS 1215 | Conceptually aligned; ISA is more principle-based, PCAOB is more prescriptive |
| ISA 500 | AS 1105 | Similar evidence hierarchy; ISA includes specific guidance on external confirmations |
| ISA 530 | AS 2315 | Aligned on risk types; ISA adds guidance on PPS sampling |
| ISA 700 | AS 3101 | Different report format requirements; ISA has "Key Audit Matters" vs. PCAOB "Critical Audit Matters" |
| ISA 705 | AS 3105 | Aligned on opinion types |
| ISA 220 | QC 1000 | ISA: ISQM 1/2 replacing ISQC 1/2; QC 1000 is new PCAOB framework |
| ISA 315 | AS 2110 | Similar risk assessment approach; ISA includes more guidance on IT risks |
| ISA 330 | AS 2301 | Similar responsive procedures framework |

---

## 19. Key Terminology Glossary

| # | Term | Definition | Source |
|---|------|-----------|--------|
| 1 | **Audit Documentation** | Written record of basis for auditor's conclusions; provides support for representations | AS 1215.02 |
| 2 | **Work Papers / Working Papers** | Alternative terms for audit documentation | AS 1215.02 |
| 3 | **Experienced Auditor** | Auditor with reasonable understanding of audit activities, studied company's industry and relevant issues | AS 1215.06A |
| 4 | **Documentation Completion Date** | Date not more than 14 days after report release date when final documentation is assembled | AS 1215.15 |
| 5 | **Report Release Date** | Date auditor grants permission to use auditor's report | AS 1215.14 |
| 6 | **Engagement Completion Document** | Document identifying all significant findings or issues with cross-references as needed | AS 1215.13 |
| 7 | **Significant Findings/Issues** | Substantive matters important to procedures, evidence, or conclusions | AS 1215.12 |
| 8 | **Audit Sampling** | Application of audit procedure to <100% of items to evaluate some characteristic of the population | AS 2315.01 |
| 9 | **Sampling Risk** | Risk auditor's conclusion differs from conclusion if entire population subjected to same procedure | AS 2315.10 |
| 10 | **Nonsampling Risk** | All audit risk not due to sampling (e.g., inappropriate procedures, failure to recognize misstatements) | AS 2315.11 |
| 11 | **Risk of Incorrect Acceptance** | Sample supports conclusion balance is NOT misstated when it IS (substantive test) | AS 2315.12 |
| 12 | **Risk of Incorrect Rejection** | Sample supports conclusion balance IS misstated when it is NOT (substantive test) | AS 2315.12 |
| 13 | **Risk of Assessing Control Risk Too Low** | Assessed control risk < true operating effectiveness (controls test) | AS 2315.12 |
| 14 | **Risk of Assessing Control Risk Too High** | Assessed control risk > true operating effectiveness (controls test) | AS 2315.12 |
| 15 | **Tolerable Misstatement** | Maximum monetary misstatement in account/class that would not cause material misstatement of FS | AS 2315.18 |
| 16 | **Tolerable Rate** | Maximum rate of deviations from prescribed control supporting planned assessed control risk | AS 2315.34 |
| 17 | **Projected Misstatement** | Misstatement estimated from sample results extended to the entire population | AS 2315.26 |
| 18 | **Monetary Unit Sampling (MUS)** | Statistical sampling where each dollar is a sampling unit; tests for overstatement | AICPA Audit Guide |
| 19 | **Probability-Proportional-to-Size (PPS)** | Same concept as MUS — larger items have proportionately higher selection probability | AS 2315 fn.4 |
| 20 | **Attribute Sampling** | Statistical sampling for testing controls; estimates deviation rate from prescribed controls | AS 2315.31–.43 |
| 21 | **Variables Sampling** | Statistical sampling for substantive testing of monetary amounts (MPU, difference, ratio) | Audit methodology |
| 22 | **Dual-Purpose Sample** | Sample used for both test of controls AND substantive test | AS 2315.44 |
| 23 | **Haphazard Selection** | Nonrandom selection without conscious bias; all items have opportunity for selection | AS 2315.24 |
| 24 | **Systematic Selection** | Selecting every nth item after a random start | AS 2315.10 Note 3 |
| 25 | **Stratification** | Process of dividing a population into relatively homogeneous groups (strata) | AS 2315.22 |
| 26 | **Audit Risk (AR)** | Risk auditor fails to detect material misstatement; AR = IR × CR × AP × TD | AS 2315 Appendix |
| 27 | **Inherent Risk (IR)** | Susceptibility of an assertion to material misstatement before consideration of controls | AS 2315 Appendix |
| 28 | **Control Risk (CR)** | Risk that material misstatement will not be prevented or detected by entity's internal control | AS 2315 Appendix |
| 29 | **Detection Risk (DR)** | Risk auditor's procedures will not detect a material misstatement that exists. In the audit risk model, DR = AP × TD, where AP is the risk that analytical procedures fail to detect misstatement and TD is the risk of incorrect acceptance for substantive tests of details. Note: TD alone is sometimes loosely called "detection risk" but DR properly encompasses both AP and TD. | AS 1101; AS 2315 Appendix |
| 30 | **TD (Test of Details Risk)** | The allowable risk of incorrect acceptance for substantive tests of details. TD = AR / (IR × CR × AP). TD is a COMPONENT of detection risk, not synonymous with it: DR = AP × TD. | AS 2315 Appendix |
| 31 | **Audit Evidence** | All information used by the auditor in arriving at conclusions on which the audit opinion is based | AS 1105.02 |
| 32 | **Sufficiency** | Measure of the quantity of audit evidence needed | AS 1105.05 |
| 33 | **Appropriateness** | Measure of quality of audit evidence (relevance + reliability) | AS 1105.06 |
| 34 | **Relevance** | Evidence's relationship to the assertion or control objective being tested | AS 1105.07 |
| 35 | **Reliability** | Dependability of evidence based on its nature, source, and circumstances | AS 1105.08 |
| 36 | **Inspection** | Examining records/documents or physical examination of tangible assets | AS 1105.15 |
| 37 | **Observation** | Looking at a process or procedure being performed by others | AS 1105.16 |
| 38 | **Inquiry** | Seeking information from knowledgeable persons inside or outside the entity | AS 1105.17 |
| 39 | **Confirmation** | Direct written communication from a third party confirming information | AS 1105.18 |
| 40 | **Recalculation** | Checking mathematical accuracy of computations or documents | AS 1105.19 |
| 41 | **Reperformance** | Independent execution of procedures or controls originally performed by entity personnel | AS 1105.20 |
| 42 | **Analytical Procedures** | Evaluations of plausible relationships among financial and nonfinancial data | AS 1105.21 |
| 43 | **Existence/Occurrence** | Assertion that assets/liabilities exist at B/S date and transactions occurred during period | AS 1105.11 |
| 44 | **Completeness** | Assertion that all transactions and accounts that should be presented are included | AS 1105.11 |
| 45 | **Valuation/Allocation** | Assertion that financial statement amounts are appropriate and allocations are reasonable | AS 1105.11 |
| 46 | **Rights and Obligations** | Assertion that entity holds or controls rights to assets and liabilities are its obligations | AS 1105.11 |
| 47 | **Presentation and Disclosure** | Assertion that FS components are properly classified, described, and disclosed per applicable framework | AS 1105.11 |
| 48 | **Material Weakness** | Deficiency or combination of deficiencies resulting in reasonable possibility that material misstatement won't be prevented/detected | AS 2201 |
| 49 | **Significant Deficiency** | Deficiency less severe than material weakness but important enough to merit attention by those charged with governance | AS 1305 |
| 50 | **Critical Audit Matter (CAM)** | Matter arising from current period audit communicated in auditor's report involving especially challenging, subjective, or complex auditor judgment | AS 3101 |
| 51 | **Engagement Quality Review (EQR)** | Quality review of engagement by qualified reviewer not on engagement team, evaluating significant judgments and conclusions | AS 1220 |
| 52 | **Tickmark** | Symbol placed on workpaper indicating a specific audit procedure was performed on the marked item | Practice |
| 53 | **Lead Schedule** | Summary schedule tying workpaper detail amounts to financial statement line items | Practice |
| 54 | **Permanent File** | Workpapers of continuing audit relevance retained across periods (org docs, agreements, bylaws) | Practice |
| 55 | **Walkthrough** | Tracing a single transaction through the entire process from initiation to financial statement reporting to understand controls | AS 2301 |
| 56 | **COSO ICIF-2013** | Committee of Sponsoring Organizations Internal Control — Integrated Framework (5 components, 17 principles) | COSO 2013 |
| 57 | **Three Lines of Defense** | Model for assigning risk management and control duties across organization (operational management, risk functions, internal audit) | IIA/COSO |
| 58 | **Representativeness Index** | Metric measuring how well a sample represents the population's characteristics; primary metric in ML-enhanced sampling | Sheu & Liu 2024 |
| 59 | **Basic Precision (MUS)** | Reliability factor for zero overstatements × sampling interval; floor of the upper limit on misstatement | AICPA Audit Guide |
| 60 | **Incremental Allowance (MUS)** | Additional precision required for each misstatement found above the basic precision | AICPA Audit Guide |
| 61 | **Upper Limit on Misstatement (ULM)** | BP + sum of incremental allowances; maximum misstatement likely in population at given confidence level | AICPA Audit Guide |
| 62 | **Tainting Percentage** | Percentage by which an item is misstated relative to its book value; used in MUS evaluation | AICPA Audit Guide |
| 63 | **Reliability Factor** | Multiplier from Poisson distribution used in MUS to calculate sampling interval and basic precision | AICPA Audit Guide |
| 64 | **Sampling Interval** | Dollar amount used in MUS = Tolerable Misstatement / Reliability Factor; items crossing interval boundaries are selected | AICPA Audit Guide |

---

## 20. Behavioral Requirements (14 Agent Behaviors)

### 20.1 Standards Compliance

When acting as the audit-workpapers skill agent, you MUST:

1. **Always identify the applicable standard** before providing guidance. State whether the guidance is per PCAOB AS, AICPA AU-C, ISA, or ISACA ITAF, and provide the paragraph reference.
2. **Flag 2024–2026 standard changes** when applicable. Note QC 1000 (eff. Dec 2025), AS 1000 (eff. Dec 2024), AS 1215 amendments (eff. Dec 2026), AS 2315 amendments (eff. Dec 2026), and COSO 2026 GenAI guidance.
3. **Cite specific paragraph references** when providing standard-based guidance. Example: "Per AS 1215.06, documentation must demonstrate who performed the work..." not "Per auditing standards, documentation should show who did the work..."

### 20.2 Evidence Sufficiency

4. **Never recommend inquiry alone** as sufficient evidence. Cite AS 1105.17 and recommend corroborating procedures.
5. **Never recommend oral evidence alone** to support procedures performed. Cite AS 1215.06 (oral evidence alone does not meet the experienced auditor standard for sufficient documentation).
6. **Always flag when uncorrected misstatements approach tolerable misstatement.** Provide quantitative comparison and note whether additional evaluation is needed per AS 2810.
7. **Always document inconsistent/contradictory information.** Per AS 1215.08 and AS 1105.29, document the inconsistency, procedures performed in response, and resolution.

### 20.3 Documentation Standards

8. **Always require the 5-part finding format** (Condition, Criteria, Cause, Effect, Recommendation) when documenting audit findings. Do not accept abbreviated formats. Management Response and Follow-Up are recommended additions.
9. **Always specify who/when for sign-offs.** Every workpaper output must include preparer, reviewer, and (where applicable) partner and EQR sign-off placeholders with date fields.
10. **Always verify cross-referencing completeness.** Check that every workpaper references its data source, related workpapers, and the conclusion destination. Cross-references must be bidirectional.
11. **Always require documentation completion within 14 days** of report release. Cite AS 1215.14–.15.

### 20.4 Sampling Rigor

12. **Always include sampling risk assessment** in any sampling documentation. State the type of risk (effectiveness vs. efficiency), the risk level selected, and its impact on sample size.
13. **Distinguish between effectiveness risks and efficiency risks** in sampling. Effectiveness risks (incorrect acceptance, assessing CR too low) are more serious and require more conservative approaches.

### 20.5 Professional Judgment

14. **Use professional judgment language when standards require judgment.** When a standard says the auditor "should consider" or "may," do NOT prescribe a single approach. Present the factors the auditor should evaluate.

---

## 21. Examples

### 21.1 Worked MUS Calculation

**Scenario:** Audit of accounts receivable for XYZ Corp. as of 12/31/2025.

```
GIVEN:
  Population (Accounts Receivable): BV = $12,500,000
  Tolerable Misstatement: TM = $500,000
  Risk of Incorrect Acceptance: 5%
  Expected Overstatements: 0
  Reliability Factor (0 overstatements, 5% risk): RF = 3.00

CALCULATION:
  Sampling Interval = TM / RF = $500,000 / 3.00 = $166,667
  Sample Size = (BV × RF) / TM = ($12,500,000 × 3.00) / $500,000 = 75 items

SELECTION:
  Random start: $87,234 (selected from random number table)
  Items selected where cumulative amount crosses interval boundary:
    $87,234; $253,901; $420,568; $587,235; ... (adding $166,667 each time)
  All items with book value > $166,667 automatically selected (100%)

TESTING RESULTS:
  3 misstatements found:
    Item 1: BV = $200,000, Audit Value = $185,000, Misstatement = $15,000, Tainting = 7.5%
    Item 2: BV = $45,000, Audit Value = $42,000, Misstatement = $3,000, Tainting = 6.7%
    Item 3: BV = $120,000, Audit Value = $115,500, Misstatement = $4,500, Tainting = 3.75%

EVALUATION:
  Basic Precision = 3.00 × $166,667 = $500,001

  Incremental Allowance #1: (4.75 - 3.00) × $166,667 = 1.75 × $166,667 = $291,667
  Incremental Allowance #2: (6.30 - 4.75) × $166,667 = 1.55 × $166,667 = $258,334
  Incremental Allowance #3: (7.76 - 6.30) × $166,667 = 1.46 × $166,667 = $243,334

  Upper Limit on Misstatement = $500,001 + $291,667 + $258,334 + $243,334 = $1,293,336

  Comparison: ULM ($1,293,336) > TM ($500,000)

CONCLUSION:
  The upper limit on misstatement exceeds tolerable misstatement. The accounts
  receivable balance MAY be materially misstated. Additional procedures are needed:
  (1) expand sample, (2) request management adjustments, or (3) modify audit report.

  Per AS 2315.28, consider whether risk assessment should be revised.
```

† Rounding differences ≤$1 are immaterial.

### 21.2 Worked Attribute Sampling Example

**Scenario:** Test of controls — Three-way match approval for purchases at XYZ Corp.

```
GIVEN:
  Control being tested: All purchase orders > $5,000 require three-way match
  (PO + receiving report + invoice) approved by procurement manager before payment.
  Population: All purchase orders > $5,000 issued during FY 2025 (N = 2,400)
  Tolerable Rate: 5% (maximum deviation rate supporting planned CR assessment)
  Expected Deviation Rate: 1% (based on prior-year testing)
  Risk of Assessing CR Too Low: 5% (95% confidence)

SAMPLE SIZE DETERMINATION:
  From Attribute Sampling Table (95% confidence):
  Tolerable Rate 5%, Expected Deviation Rate 1% → n = 90

SELECTION:
  Method: Systematic selection
  Interval: 2,400 / 90 = 26.67 ≈ 27
  Random start: 14 (from random number table)
  Select POs at positions: 14, 41, 68, 95, ... (adding 27 each time)

TESTING RESULTS:
  90 purchase orders selected and tested.
  Deviations found: 2
    Deviation 1: PO #4521 ($7,200) — Receiving report dated 4 days after
                 payment was processed; match not performed prior to payment.
    Deviation 2: PO #8103 ($11,500) — Invoice approved by department head
                 instead of procurement manager (wrong approver).

EVALUATION:
  Sample Deviation Rate = 2/90 = 2.2%
  Tolerable Rate = 5%
  Sample deviation rate (2.2%) < Tolerable rate (5%)

  However, consider sampling risk: At 95% confidence with 2 deviations in
  a sample of 90, the upper limit on the deviation rate must be considered.
  Using Poisson approximation, upper limit ≈ 6.2% (at 95% confidence, 2 errors).

  Upper limit (6.2%) > Tolerable rate (5%)

CONCLUSION:
  The upper limit on the deviation rate exceeds the tolerable rate. The control
  is NOT operating effectively at the level required to support the planned
  assessed control risk. Pending additional procedures, the auditor should
  consider:
  (1) Raising the assessed control risk,
  (2) Expanding the sample to gain more precision, or
  (3) Modifying the nature, timing, or extent of substantive procedures.
  
  Per AS 2315.28, reassessment of the control risk assessment is needed.
  Impact: Increased assessed CR → reduced TD → larger substantive samples required.
```

### 21.3 Worked Variables Sampling Example (Difference Estimation)

**Scenario:** Substantive test of accounts payable at XYZ Corp. as of 12/31/2025.

```
GIVEN:
  Population: Accounts payable ledger (N = 4,000 vendor line items)
  Total book value: BV = $8,200,000
  Tolerable Misstatement: TM = $300,000
  Expected Misstatement: E[M] = $40,000
  Desired aggregate precision: A = TM - E[M] = $300,000 - $40,000 = $260,000
  Confidence level: 95% (Z = 1.96)

σ ESTIMATION:
  Using prior-year data: Prior-year sample standard deviation of differences
  (audit value - book value) was $420. Adjusting for 10% increase in transaction
  complexity, estimated σ = $460.
  (Alternatively, a pilot sample of 35 items yielded s = $475; we use $475 as
  a more current estimate.)

SAMPLE SIZE DETERMINATION:
  For difference estimation, precision must be expressed per item (A/N), not
  in aggregate, because the projection multiplies the per-item estimate by N.

  Precision per item = A / N = $260,000 / 4,000 = $65

  n = (Z × σ / Precision_per_item)²
  n = (1.96 × $475 / $65)²
  n = ($931 / $65)²
  n = (14.32)²
  n = 205

  Adjusted for finite population:
  n_adj = 205 / (1 + 205/4,000) = 205 / 1.05125 = 195

  Final sample size: 195 items

SELECTION:
  Method: Stratified random sampling (3 strata by dollar size)
  High-value stratum (> $50,000): 40 items — 100% examined
  Medium stratum ($5,000–$50,000): 100 items selected randomly from 1,560 items
  Low stratum (< $5,000): 55 items selected randomly from 2,400 items

TESTING RESULTS (for 100 medium + 55 low stratum items = 155):
  Audit values compared to book values for each item.
  
  Sample statistics (155 items):
    Sum of book values:        $1,875,000
    Sum of audit values:       $1,859,250
    Sum of differences (audit - book): -$15,750 (understatement)
    Mean difference (d̄):      -$15,750 / 155 = -$101.61 per item
    Sample standard deviation: $485

EVALUATION — PROJECTION:
  Projected Misstatement = d̄ × N = -$101.61 × 4,000 = -$406,440

  The negative sign indicates the AP balance is understated by $406,440.

  Precision (sampling risk adjustment):
  Adjusted precision = (Z × s_d × N / √n) × √(1 - n/N)
  = (1.96 × $485 × 4,000 / 13.964) × √(1 - 195/4,000)
  = (1.96 × $485 × 4,000 / 13.964) × 0.9753
  = $272,410 × 0.9753
  ≈ $265,700

  Note: The finite population correction √(1-n/N) is a multiplier applied
  to the precision, not a divisor in the denominator. s_d denotes the
  sample standard deviation of differences (estimated from the sample).

  Confidence interval for misstatement:
  Lower limit = -$406,440 - $265,700 = -$672,140
  Upper limit = -$406,440 + $265,700 = -$140,740

COMPARISON TO TOLERABLE:
  The projected understatement of $406,440 exceeds tolerable misstatement
  of $300,000 in absolute terms. Even the most favorable bound of the
  confidence interval (-$140,740 understatement) does not indicate
  material overstatement, but the worst case (-$672,140) far exceeds TM.

CONCLUSION:
  The accounts payable balance is likely materially understated. Pending
  additional procedures, the auditor should:
  (1) Investigate the nature and cause of the understatements,
  (2) Request management adjust the AP balance,
  (3) Expand the sample, or
  (4) Consider the impact on the financial statements and audit opinion.

  Per AS 2315.28, reassessment of risk levels may be needed.
```

### 21.4 Complete Finding Example

*(See Section 8.7 above for the full 5-part finding example on AP cutoff.)*

### 21.5 Complete Mock Workpaper

```
┌─────────────────────────────────────────────────────────────┐
│ CLIENT: XYZ Corporation  PERIOD: Year ending 12/31/2025    │
│ WP INDEX: D-1            PREPARED BY: JDW  03/15/26         │
│ SUBJECT: Accounts          REVIEWED BY: MRS  03/22/26       │
│          Receivable Confirmation                             │
├─────────────────────────────────────────────────────────────┤
│ OBJECTIVE: To test the existence and valuation of accounts   │
│ receivable balances as of 12/31/2025 through third-party    │
│ confirmation.                                               │
│ SOURCE: Client A/R aging as of 12/31/2025; bank/customer   │
│         confirmation responses                              │
│ ASSERTION(S): Existence, Valuation                         │
├─────────────────────────────────────────────────────────────┤
│ PROCEDURE:                                                  │
│ 1. Selected 75 items from A/R aging using MUS sampling plan │
│    (see WP I-1)                                             │
│ 2. Sent positive confirmation requests to 75 customers      │
│ 3. Followed up on non-responses with second request after   │
│    14 days                                                  │
│ 4. For non-responses after second request, applied           │
│    alternative procedures: traced to subsequent cash         │
│    receipts, sales invoices, and shipping documents         │
│                                                             │
│ DATA / ANALYSIS:                                            │
│ Total A/R per aging:         $12,500,000                    │
│ Sample size:                 75 items                        │
│ Confirmations sent:          75                              │
│ Responses received:          62 (82.7%)                     │
│ Non-responses:              13 (alternative procedures OK)   │
│ Exceptions:                 3 (see below)                    │
│                                                             │
│ Summary of Exceptions:                                      │
│ Customer  A/R Balance  Confirmed  Difference   Type          │
│ ABC Co    $200,000     $185,000   $15,000     Pricing       │
│ DEF Inc    $45,000     $42,000    $3,000      Qty dispute   │
│ GHI Ltd   $120,000     $115,500   $4,500      Credit memo   │
│ TOTAL     $365,000     $342,500   $22,500                    │
│                                                             │
│ TICKMARK LEGEND:                                            │
│ ✓  Traced to customer confirmation response                  │
│ □  Bank/external confirmation received                      │
│ ∧  Agrees to A/R aging per client records                   │
│ ∨  Footed and cross-footed; agrees to total                  │
│ ○  Selected per MUS sampling plan (WP I-1)                  │
│ ※  Exception noted — see exception detail above             │
│ ◆  Alternative procedures performed for non-response         │
│                                                             │
│ CONCLUSION: The upper limit on misstatement per MUS         │
│ evaluation (WP I-1) exceeds tolerable misstatement.          │
│ Accordingly, a conclusion that accounts receivable is not    │
│ materially misstated cannot be reached at this time.         │
│ Pending additional procedures — see WP I-1 for expanded     │
│ sample evaluation and WP K-3 for uncorrected misstatement    │
│ summary.                                                    │
│ EXCEPTIONS: 3 pricing/quantity exceptions totaling $22,500   │
│ CROSS-REFS: I-1 (MUS evaluation), K-3 (uncorrected misstmt), │
│            D-2 (AR aging analysis), J-1 (analytical procedures)│
├─────────────────────────────────────────────────────────────┤
│ REVIEW NOTES:                                               │
│ 03/22/26 MRS: Consider expanding sample given the 3        │
│ exceptions. Resolution: Sample expanded by 25 items per       │
│ I-1 supplement. Results consistent with original sample.    │
│ MRS 03/28/26 cleared.                                       │
│                                                             │
│ Partner Review: EPK 04/02/26                                │
│ EQR: JLR 04/05/26                                          │
└─────────────────────────────────────────────────────────────┘
```

---

*End of Audit Workpapers Skill*
