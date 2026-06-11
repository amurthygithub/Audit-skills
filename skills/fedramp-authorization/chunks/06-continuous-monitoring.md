---
chunk_id: 06-continuous-monitoring
parent_skill: fedramp-authorization
topic: "Continuous Monitoring (ConMon) — the monthly cadence; the three objectives (operational visibility, managed change control, incident response); the monthly submission (updated POA&M, system inventory, vulnerability-scan results); scan frequencies; remediation SLAs 30/90/180 days (high-critical / moderate / low); significant-change requests; annual and triennial reassessment"
load_when: "user asks about Continuous Monitoring, ConMon, the monthly cadence, what is submitted monthly, scan frequency, remediation SLAs, significant changes, or annual / triennial reassessment"
---

# Chunk 06 — Continuous Monitoring (ConMon)

Authorization is not a one-time event. Once an agency grants the ATO, the CSP must keep proving the system stays secure through **Continuous Monitoring (ConMon)**. The single most load-bearing fact: **ConMon is monthly.** This chunk fixes the cadence, what is submitted, the scan and remediation rules, and the change / reassessment events that sit on top of the monthly cycle.

## 1. ConMon is monthly — the three objectives

The CSP submits ConMon evidence on a **monthly** cadence [FEDRAMP-CONMON §monthly]. ConMon exists to give the authorizing official ongoing assurance and serves **three objectives**:

1. **Operational visibility** — the AO can see the current security state of the authorized system.
2. **Managed change control** — changes to the system are tracked and assessed so they do not silently erode the authorized security posture.
3. **Incident response** — the CSP attends to its incident-response duties (detect, report, respond).

These three objectives are the reason the monthly package contains what it does.

## 2. What is submitted monthly

Each **monthly** ConMon submission delivers three things [FEDRAMP-CONMON §monthly]:

- An **updated POA&M** — the current state of every open corrective action (the POA&M lifecycle and deviation-request mechanics live in `chunks/07-poam-and-risk.md`).
- An **updated system inventory** — the components in the authorized boundary.
- **Vulnerability-scan results** — the latest scans of the system.

Together these let the AO confirm operational visibility, see what changed, and track remediation against the SLAs below.

## 3. Scan frequency

Vulnerability scanning feeds the monthly submission. Scans run at least on the monthly ConMon rhythm, and **internet-reachable resources are scanned more frequently** than internal-only components, because externally exposed surface carries higher exposure. The scan results are part of every monthly package.

## 4. Remediation SLAs — 30 / 90 / 180 days by severity

A finding's remediation deadline follows its **severity** [FEDRAMP-CONMON §monthly]:

| Severity | Remediation SLA |
|----------|-----------------|
| **High / Critical** | **30 days** |
| **Moderate** | **90 days** |
| **Low** | **180 days** |

These are the same severity-driven deadlines a POA&M item carries (`chunks/07-poam-and-risk.md`): a finding identified on a given date is due that date + {30 / 90 / 180} days by severity. Missing an SLA is itself something the monthly POA&M surfaces to the AO.

## 5. Change and reassessment events on top of the monthly cycle

The monthly cycle is the baseline; two kinds of events layer on top:

- **Significant-change requests.** A change that materially affects the security posture or the authorization boundary requires a **significant-change request** — the change is described and assessed before (or as) it is made, rather than just appearing in the next inventory. This is the "managed change control" objective in action.
- **Annual / triennial reassessment.** Beyond the monthly submissions, the system undergoes periodic reassessment by a 3PAO — an **annual** assessment of a subset of controls and a fuller **triennial** reassessment — to confirm the authorization still holds.

## 6. Procedure — the monthly ConMon cycle

1. **Scan.** Run vulnerability scans across the authorized boundary (internet-reachable resources more frequently).
2. **Triage to severity.** Classify each new finding as high/critical, moderate, or low.
3. **Set deadlines.** Assign each finding a remediation due-date = identified-date + {30 / 90 / 180} days by severity.
4. **Update the POA&M** with new, in-progress, and closed items (deviation requests per `chunks/07`).
5. **Refresh the inventory** to reflect the current components in the boundary.
6. **Submit** the updated POA&M + inventory + scan results for the month.
7. **Handle events:** raise a significant-change request for any material change; prepare for the annual / triennial reassessment when due.

## 7. Output template — monthly ConMon submission summary

```
System: <CSO name>          Reporting month: <YYYY-MM>          Baseline: <Low 156 | Moderate 323 | High 410>
Submitted this month:  [x] updated POA&M   [x] system inventory   [x] vulnerability-scan results
Open POA&M items by severity (with SLA):
  High/Critical: <n>  (SLA 30 days)
  Moderate:      <n>  (SLA 90 days)
  Low:           <n>  (SLA 180 days)
Items past SLA: <n>
Significant-change requests this period: <n>
Next reassessment: <annual: YYYY-MM | triennial: YYYY-MM>
```

## 8. Anti-hallucination

- **ConMon is monthly.** The CSP submits an updated POA&M, system inventory, and vulnerability-scan results every month [FEDRAMP-CONMON §monthly]. Do not state a quarterly or annual ConMon cadence — the monthly submission is the cadence; annual / triennial reassessment is a separate, additional event.
- **The three objectives are operational visibility, managed change control, and incident response** [FEDRAMP-CONMON §monthly].
- **Remediation SLAs are 30 / 90 / 180 days** for **high-critical / moderate / low** severity [FEDRAMP-CONMON §monthly]. Do not swap the day counts across severities.
- **Internet-reachable resources are scanned more frequently** than internal-only components.
- **POA&M deviation-request mechanics are not covered here** — see `chunks/07-poam-and-risk.md` (this chunk owns the monthly cadence; chunk 07 owns the POA&M lifecycle and deviation requests).
