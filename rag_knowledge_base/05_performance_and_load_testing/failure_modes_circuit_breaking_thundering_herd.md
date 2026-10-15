```json
{
  "topic": "failure_modes_and_mitigations",
  "component": "reliability_engineering",
  "decision_type": "failure_mitigation",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems/",
  "version": "1.0",
  "licence": "Open-Documentation",
  "last_verified": "2026-10-14"
}
```

# Failure Modes in Distributed Systems: Cascades, Thundering Herds, and Circuit Breaking

## 1. Cascading Failures and Retry Storms

### The Failure Cascade Sequence
1. Microservice $B$ experiences a momentary transient slowdown (e.g., a 2-second garbage collection pause or slow database query).
2. Upstream Microservice $A$ times out after 1 second and immediately retries the request.
3. Every incoming client request now generates 3x or 4x requests against $B$.
4. Service $B$'s incoming request queue overflows; CPU utilization hits 100%.
5. Service $B$ crashes completely.
6. Service $A$ threads stall waiting for $B$, exhausting $A$'s connection pools and thread pools.
7. Service $A$ crashes. The entire microservice graph collapses like a row of dominoes.

### Antidote: Exponential Backoff with Full Jitter
Instead of fixed or immediate retries:
```python
import random
import time

def retry_with_jitter(attempt: int, base_delay: float = 0.1, max_delay: float = 5.0):
    # Calculate exponential backoff
    temp = min(max_delay, base_delay * (2 ** attempt))
    # Full jitter: random float uniformly distributed between 0 and temp
    sleep_duration = random.uniform(0, temp)
    time.sleep(sleep_duration)
```

---

## 2. The Thundering Herd (Dogpiling) Problem

### The Scenario
A high-traffic cached resource (e.g., the homepage hot-topics JSON, queried 20,000 times/sec) expires in Redis at $t = 0$.
Between $t = 0$ and $t = 50\text{ms}$ (while the first request queries the database to re-populate the cache):
- 1,000 concurrent application threads all observe a cache miss simultaneously.
- All 1,000 threads simultaneously issue the exact same heavy SQL query to PostgreSQL.
- The database connection pool is instantly exhausted, locking the entire platform.

### Solutions
1. **Singleflight / Mutex Locking (Distributed Mutex)**:
   - When a cache miss occurs, the worker attempts to acquire a short-lived Redis lock: `SET lock:hot_key uuid NX EX 5`.
   - Only the single worker that acquires the lock queries the database and populates Redis.
   - All other 999 workers sleep for 50ms and re-check Redis, receiving the refreshed cache value.
2. **Probabilistic Early Recomputation (XFetch Algorithm)**:
   - Workers recompute the cache before it actually expires based on read frequency and computation time:
     $$\Delta t \times \beta \times \ln(\text{random}()) > \text{TTL}_{\text{remaining}}$$

---

## 3. Circuit Breaker Implementation Details

```
       [Normal Traffic]
              │
              ▼
       ┌──────────────┐
       │    CLOSED    │ ──(Failure rate > 50% over 10s)──┐
       └──────────────┘                                  │
              ▲                                          ▼
   (Probe succeeds)                               ┌──────────────┐
              │                                   │     OPEN     │
              │                                   └──────────────┘
       ┌──────────────┐                                  │
       │  HALF-OPEN   │ ◄──(After sleep_window = 30s)────┘
       └──────────────┘
```

- **Metrics Window**: Track request success and failure using a sliding time window (e.g., 10 seconds with 10 buckets of 1 second).
- **Fallback Action**:
  - Return cached stale response.
  - Return default fallback payload (e.g., empty recommendation list, generic greeting).
  - Return HTTP 503 (Service Unavailable) immediately without making downstream network call.
