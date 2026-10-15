```json
{
  "topic": "high_availability",
  "component": "infrastructure",
  "decision_type": "reliability_engineering",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# High Availability, Fault Tolerance, and Resilience Patterns

## 1. Measuring Availability: "The Nines"

Availability is calculated as:
$$\text{Availability} = \frac{\text{Uptime}}{\text{Uptime} + \text{Downtime}} \times 100\%$$

| Availability Level | Downtime per Year | Downtime per Month | Downtime per Week | Example Workloads |
| :--- | :--- | :--- | :--- | :--- |
| **99% (Two Nines)** | 3.65 days | 7.31 hours | 1.68 hours | Internal dev/staging tools, batch analytics |
| **99.9% (Three Nines)** | 8.77 hours | 43.8 minutes | 10.1 minutes | Typical SaaS applications, blogs, content sites |
| **99.99% (Four Nines)** | 52.6 minutes | 4.38 minutes | 1.01 minutes | Production e-commerce, banking APIs, authentication |
| **99.999% (Five Nines)** | 5.26 minutes | 26.3 seconds | 6.05 seconds | Telco core switches, cloud DNS, hospital systems |

---

## 2. Recovery Metrics: RPO and RTO

- **RPO (Recovery Point Objective)**: The maximum acceptable data loss measured in time backward from disaster.
  - *Example*: 1-hour RPO means backup snapshots must be taken every hour; up to 59 minutes of recent data may be lost upon failure.
- **RTO (Recovery Time Objective)**: The maximum acceptable duration of system downtime before restoration.
  - *Example*: 15-minute RTO means automated failovers must detect the crash, promote a replica, update DNS/service mesh, and resume traffic within 15 minutes.

---

## 3. Resilience and Fault Tolerance Patterns

### 3.1 Circuit Breaker Pattern
Prevents a cascading failure when a downstream microservice experiences degradation.
- **Closed**: Requests flow normally. Failures are tracked.
- **Open**: When failure rate exceeds threshold (e.g., 50% errors in 10s window), all subsequent requests immediately fail fast without hitting the downstream service.
- **Half-Open**: After a sleep timeout (e.g., 30s), a small sample of probe requests are allowed through. If successful, breaker closes; if errors persist, breaker resets to open.

### 3.2 Bulkhead Pattern
Isolates resources (such as thread pools, connection pools, CPU quotas, or worker processes) into distinct compartments.
- *Example*: In an e-commerce platform, checkout requests use a dedicated database connection pool of 50 connections, while product browsing uses an independent pool of 100 connections. A slow search query can never starve checkout transactions.

### 3.3 Retry with Exponential Backoff and Jitter
Naive immediate retries cause "thundering herd" amplification during momentary outages.
- **Backoff Formula**:
  $$t_{\text{wait}} = \min(t_{\text{max}}, t_{\text{base}} \times 2^{\text{attempt}}) + \text{jitter}$$
- **Full Jitter**: Adding random noise uniformly distributed between 0 and $t_{\text{wait}}$ decorrelates requests across millions of retrying client devices.

### 3.4 Graceful Degradation & Fallbacks
When non-critical sub-components fail, the system serves degraded responses rather than HTTP 500:
- If recommendation engine is down, render static top-10 trending items.
- If user avatar microservice is offline, render default SVG placeholders.
