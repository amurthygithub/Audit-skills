---
chunk_id: 07-monitor
parent_skill: nist-800-53-rmf
topic: "Continuous Monitoring (RMF Step 7) — ISCM Strategy"
load_when: "user asks about ISCM, annual assessment, POA&M management, ConMon"
---

# Chunk 06 — Monitor (RMF Step 7 / ISCM)

## Procedure

Per NIST SP 800-137, the ISCM strategy defines the frequency, scope, and triggers for continuous monitoring.

1. Maintain the **ISCM strategy** in SSP §13 — frequency per control family, triggers (significant change, incident, threshold breach).
2. Annual control assessment (or triggered assessment).
3. POA&M management — track remediation, risk level, scheduled completion.
4. Configuration change management — significant-change assessment.
5. Vulnerability scanning (Nessus, Qualys, etc.) and patch SLA per FIPS 199 category.
6. Incident-driven reassessment — major incidents may trigger re-authorization.

## ISCM strategy — frequency and triggers

| Trigger | Action | Frequency |
|---------|--------|-----------|
| Scheduled control assessment | Re-assess all controls in scope | Annually (or per agency policy) |
| Significant change | Re-assess affected controls | On change |
| Major incident (catastrophic, severe) | Re-assess and possibly re-authorize | On incident |
| Threshold breach (vuln, config drift) | Investigate and remediate | Continuous |
| POA&M milestone reached | Verify closure or escalate | On milestone |

## FedRAMP ConMon (continuous monitoring) requirements

CSPs operating under a FedRAMP authorization must operate a continuous monitoring program that includes:

- **Monthly vulnerability scans** (OS, web app, database) — internal + external.
- **Annual assessment** by a 3PAO (or self-assessment for some baselines).
- **POA&M management** — submit monthly, track risk, remediate by date.
- **Significant-change notifications** to the AO and the FedRAMP PMO.
- **Incident reporting** to US-CERT and the AO per US-CERT incident categories.

## Patch SLAs by FIPS 199 category

| Severity | Low baseline | Moderate baseline | High baseline |
|----------|--------------|-------------------|---------------|
| Critical | 30 days | 15 days | 7 days |
| High | 60 days | 30 days | 14 days |
| Medium | 90 days | 60 days | 30 days |
| Low | 180 days | 90 days | 60 days |

(Verify against current FedRAMP ConMon Strategy Guide.)

## SSP §13 (Continuous Monitoring Strategy) template

```yaml
iscm_strategy:
  assessment_frequency: annual
  triggers:
    - significant_change
    - major_incident
    - threshold_breach
  vulnerability_scanning:
    cadence: monthly
    tools: [Nessus, Qualys]
  poam_management:
    cadence: monthly
    owner: ISSO
  significant_change_review: true
  incident_reporting: US-CERT
  patch_sla: ref("above table")
```

## Citations in this chunk

- `[NIST-SP-800-37-Rev2 Step 7]` — monitor
- `[NIST-SP-800-137]` — ISCM
- `[FedRAMP-Rev5 ConMon Strategy]` — continuous monitoring

See `## 10. References & Citation Manifest` in SKILL.md.
