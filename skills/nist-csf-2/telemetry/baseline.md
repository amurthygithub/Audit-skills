# Telemetry baseline — nist-csf-2

## Purpose

This document records the expected event volumes and latencies for the nist-csf-2 skill in production. The baseline is used to:

- Alert when event volume or latency drifts significantly (anomaly detection)
- Capacity-plan the telemetry pipeline
- Provide a benchmark for the stub executor

## Event volumes (per UC invocation)

| UC | Events emitted | Notes |
|---|---|---|
| UC-01 (first Organizational Profile) | 1 `skill_invocation` + 1 `profile_generated` + 1 `gap_analyzed` (if Target Profile provided) | 2-3 events per call |
| UC-02 (board maturity report) | 1 `skill_invocation` + 1 `profile_generated` | 2 events per call |
| UC-03 (Current/Target → 800-53 crosswalk) | 1 `skill_invocation` + 1 `crosswalk_computed` | 2 events per call |

## Expected volume (production estimates)

Assuming the skill is invoked 100 times/day across a small customer base (5 customers × 20 invocations/day):

- 200-300 events/day
- ~9,000 events/month
- ~110,000 events/year

For a mid-size deployment (50 customers × 50 invocations/day):

- 2,500-3,750 events/day
- ~75,000-110,000 events/month

The stub (this skill's reference executor) is fast enough that latency is dominated by JSON serialization (~1-5 ms per event). The real skill executor (LLM-based) will have higher latency, dominated by model inference.

## Latency baselines

| Operation | Stub latency (this skill) | Production latency (LLM-based, target) |
|---|---|---|
| `skill_invocation` event emission | <5 ms | 500-3000 ms |
| `profile_generated` event emission | <5 ms | 1000-5000 ms |
| `crosswalk_computed` event emission | <5 ms | 1000-5000 ms |

## Anomaly detection thresholds

Alert when (7-day rolling average):

- Event volume > 2x baseline (unexpected traffic spike)
- Event volume < 0.5x baseline (skill may be silently failing)
- P95 latency > 2x baseline (degradation)
- P99 latency > 5x baseline (outliers)

## SLOs (suggested)

- Availability: 99.5% monthly (the skill can be down for ~4 hours/month without breaching)
- Event delivery: 99.9% (events should never be dropped; better to buffer and retry than to fail)
- P95 invocation latency: <5s (LLM-based)
- P99 invocation latency: <15s (LLM-based)
