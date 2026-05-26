# Example: SOX 404 ICFR Assessment

**Skill**: coso-internal-controls
**Scenario**: You are a SOX compliance manager performing the annual ICFR assessment for "ManufactureCo", a SEC-registered manufacturing company ($1.2B revenue, 3,000 employees, operations in 8 states and Mexico).

---

## Prompt

```
I need to perform the annual SOX 404 ICFR assessment for ManufactureCo.
Key facts:
- New ERP implementation (SAP S/4HANA) went live Oct 1 (Q3 of fiscal year)
- Mexico subsidiary has separate IT systems with limited controls
- Audit committee has 3 members; one joined in January with no financial expertise
- Prior year had 2 significant deficiencies (IT access controls, inventory count)
- CEO and CFO certified last year with no material weaknesses

Walk me through the full ICFR assessment end-to-end.
```

## Expected Agent Output Structure

### Phase 1: Scoping (§20, Phase 1)

- **Significant accounts**: Revenue, Inventory, PP&E, AP, Debt
- **Relevant assertions**: Revenue (existence, completeness, cutoff), Inventory (existence, valuation), AP (completeness, existence)
- **Entity-level controls to assess first**: P1-P5 (Control Environment), audit committee oversight
- **Multi-location**: Mexico subsidiary — assess as individually significant location per AS 2201.B1-.B38

### Phase 2: Entity-Level Assessment (§20, Phase 2)

**Critical finding — Audit Committee (P2)**:
- P2 requires board members with financial reporting and ICFR expertise
- New member lacks financial expertise → evaluate if committee as a whole meets expertise requirement
- **Assessment**: If other 2 members have sufficient expertise → P2 present and functioning (with concern noted)
- If committee lacks sufficient expertise overall → **Control deficiency** → proceed to decision tree

**SAP Go-Live Impact (P9)**:
- Major system change → must assess impact on ICFR
- Evaluate: data migration controls, new process controls, parallel run results, user training
- **Roll-forward procedures required** (AS 2201.48-.50): Test controls at go-live AND year-end

### Phase 3: Process-Level Assessment (§20, Phase 3)

**Inventory Walkthrough (§21.1 template)**:

| Step | Processing Point | Inquiry | Observation | Inspection | Re-performance | Control |
|------|------------------|---------|-------------|------------|----------------|---------|
| 1 | Raw materials received | Y - dock worker | Y - observed count | GRN, packing slip | Y - recount 5 items | 3-way match |
| 2 | Inventory entered in SAP | Y - clerk | Y - observed MM01 transaction | SAP screenshot | N/A | System validation |
| 3 | Physical count (annual) | Y - count supervisor | Y - observed count | Count sheets, tags | Y - recounted 10 items | Tag, double-count |
| 4 | SAP reconciliation | Y - accountant | N - after period | SAP MB52 report | Y - re-performed | Auto recon |

**Key risk**: Step 2 — new SAP system, limited user training, potential for entry errors

### Phase 4: Deficiency Evaluation (§8.2 decision tree)

**Prior Year SD #1 — IT Access Controls**:
- Was it remediated? → Test new access controls in SAP
- If remediation effective → Downgrade from SD to resolved
- If remediation not complete → **Consider aggregation with current-year findings**

**Prior Year SD #2 — Inventory Count**:
- Was it remediated? → Test revised count procedures
- If still issues → Walk through decision tree Step 2 again

**New Deficiency — SAP User Access (Mexico)**:
```
STEP 1: Design deficiency? YES — Mexico IT systems lack proper access controls
STEP 2: Reasonable possibility of material misstatement? 
  → Mexico inventory = $45M (3.8% of total assets, below materiality of $60M)
  → BUT aggregated with US IT access issues? → Assess per AS 2201.68
  → IF combined → reasonable possibility → YES
STEP 3: Magnitude material?
  → IF combined with US findings → could exceed materiality
  → CLASSIFY AS: SIGNIFICANT DEFICIENCY (pending compensating controls)
```

**Aggregation Rule (AS 2201.68)**: Mexico IT access + US SAP go-live issues → combined assessment → if reasonable possibility of material misstatement in combined account balances → upgrade to Material Weakness

### Phase 5: Reporting (§12-13 templates)

- Management's ICFR Report: Disclose significant deficiencies, confirm no material weaknesses (if compensating controls effective)
- Written representations (AS 2201.75-.76): Obtain from management

### Phase 6: Ongoing Monitoring (§20, Phase 6)

- Subsequent-year scaling: Reduce testing for controls tested effectively last year (except SAP — new, first-year level testing)
- Monitor SAP stabilization: Track error rates, user complaints data quality issues

---

## Key Agent Behaviors to Verify

1. **Decision tree followed exactly**: Each deficiency walks through Step 1→2→3
2. **Aggregation rule applied**: AS 2201.68 deficiency combination assessed
3. **Roll-forward procedures**: Interim testing at SAP go-live → roll forward to year-end
4. **Multi-location considerations**: Mexico subsidiary scoped per AS 2201.B1-.B38
5. **Written representations**: AS 2201.75-.76 requirements listed
6. **TSC mapping accuracy**: If asked about SOC 2 alignment, agent maps CC2→P13-15, CC3→P6-9 (NOT the old incorrect mapping)