```json
{
  "topic": "performance_metrics",
  "component": "observability",
  "decision_type": "benchmark",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://sre.google/sre-book/service-level-objectives/",
  "version": "1.0",
  "licence": "Open-Documentation",
  "last_verified": "2026-10-14"
}
```

# Latency Percentiles, SLA/SLO/SLI, and Latency Numbers Every Architect Must Know

## 1. Why "Average Latency" is a Dangerous Lie

Consider a web service where 99 users experience 10ms latency, but 1 user experiences a 10,000ms (10-second) database lock timeout.
- $\text{Arithmetic Mean (Average)} = \frac{(99 \times 10) + 10,000}{100} = 109.9\text{ ms}$.
- An engineer inspecting the average would report: *"System is healthy at ~110ms"*, completely masking the fact that 1% of users suffered an intolerable 10-second outage!
- In modern distributed microservices where a single user page render fans out to 50 backend RPC calls, if each call has a 99th percentile latency of 200ms, the probability of the user encountering that slow call across 50 requests is:
  $$P(\text{Slow}) = 1 - (0.99)^{50} \approx 39.5\%!$$
- More than 1 out of 3 users will experience the 99th percentile tail latency!

---

## 2. Percentile Definitions
- **P50 (Median)**: 50% of requests are faster than this number. Represents the typical user experience.
- **P95**: 95% of requests are faster than this threshold. Represents slightly congested conditions.
- **P99**: Only 1 in 100 requests is slower. The standard metric for high-scale enterprise service guarantees.
- **P99.9 (Three Nines)**: Only 1 in 1,000 requests is slower. Critical for high-frequency financial and trading systems.

---

## 3. SLA vs. SLO vs. SLI Framework (Google SRE)

1. **SLI (Service Level Indicator)**: The quantifiable metric measured in real-time.
   - *Example*: The proportion of successful HTTP requests with latency < 200ms measured at the API Gateway over a rolling 30-day window:
     $$\text{SLI} = \frac{\text{Count}(\text{status} = 200 \land \text{duration} < 200\text{ms})}{\text{Total Requests}}$$
2. **SLO (Service Level Objective)**: The internal engineering target agreed upon by product and development teams.
   - *Example*: The SLI must be $\ge 99.9\%$ over any 30-day period.
3. **SLA (Service Level Agreement)**: The external contractual commitment with customers, carrying financial penalties or credits if breached.
   - *Example*: If availability drops below $99.5\%$ in a billing month, customer receives a 20% billing credit.
4. **Error Budget**: The inverse of the SLO ($100\% - \text{SLO}$).
   - For a 99.9% SLO, the error budget is 0.1% of requests (or ~43 minutes of downtime per month).
   - If the error budget is depleted, feature deployments are frozen and all engineering effort pivots to reliability and performance hardening.

---

## 4. Latency Numbers Every Architect Must Know

| Operation | Latency | Scaled Comparison (1 CPU cycle = 1 sec) |
| :--- | :--- | :--- |
| **L1 CPU Cache reference** | 0.5 ns | 1 second |
| **L2 CPU Cache reference** | 7 ns | 14 seconds |
| **RAM main memory reference** | 100 ns | 3.3 minutes |
| **Read 1 MB sequentially from RAM** | 250,000 ns (250 µs) | 2.9 days |
| **Read 1 MB sequentially from NVMe SSD**| 1,000,000 ns (1 ms) | 11.6 days |
| **Intra-datacenter network round trip** | 500,000 ns (0.5 ms) | 5.8 days |
| **Read 1 MB sequentially from Spinning HDD** | 20,000,000 ns (20 ms) | 7.7 months |
| **Send packet CA to Netherlands & back** | 150,000,000 ns (150 ms) | 4.8 years! |

**Key Takeaways**:
- RAM is ~1,000x faster than disk access.
- Cross-continent network round trips dominate all algorithmic micro-optimizations. Always place caches and edge termination close to users!
