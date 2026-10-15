```json
{
  "topic": "load_testing_and_benchmarking",
  "component": "load_testing_tools",
  "decision_type": "benchmark",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://grafana.com/docs/k6/latest/ | https://docs.locust.io/",
  "version": "k6 v0.50+ / Locust v2.24+",
  "licence": "Open-Documentation",
  "last_verified": "2026-10-14"
}
```

# Load Testing and Benchmark Methodology: Grafana k6 vs. Locust

## 1. Tool Selection: k6 vs. Locust

| Dimension | Grafana k6 | Locust |
| :--- | :--- | :--- |
| **Language** | Test scripts in JavaScript (ES6), executed by high-performance Go runtime | Test scripts in pure Python, executed with gevent coroutines |
| **Resource Efficiency** | Extremely high: single machine can generate 30,000–50,000 Virtual Users (VUs) | Moderate: requires multi-process or distributed master-worker cluster for high concurrency |
| **CI/CD Integration** | First-class native CLI, returns non-zero exit codes on threshold failure | Good CLI and rich web UI dashboard with live graphs |
| **Protocol Support** | HTTP/1.1, HTTP/2, WebSockets, gRPC | HTTP/1.1, WebSockets, custom Python socket clients |

---

## 2. Realistic Workload Testing Profiles

A professional load test must never start with an instantaneous 100% traffic shock. It must model distinct phases:

### 2.1 Smoke Test
- **Purpose**: Verify scripts, authentication tokens, and backend routing without overloading.
- **Config**: 1 to 5 VUs for 1 minute.

### 2.2 Ramp-Up & Load Test (Baseline)
- **Purpose**: Measure normal peak capacity and confirm SLA/SLO compliance.
- **Stages**:
  1. Ramp up from 0 to 1,000 VUs over 5 minutes.
  2. Hold at 1,000 VUs steady-state for 15 minutes.
  3. Ramp down to 0 over 2 minutes.

### 2.3 Stress & Breaking-Point Test
- **Purpose**: Determine the exact concurrency where the system fails, verify autoscaling triggers, and confirm graceful degradation.
- **Method**: Step-ladder increment (e.g., +500 VUs every 2 minutes) until error rate exceeds 5% or P95 latency exceeds 2,000ms.

### 2.4 Spike Test
- **Purpose**: Simulate sudden viral shocks (e.g., flash sales, celebrity tweets, push notification blast).
- **Method**: Surge from 100 VUs to 10,000 VUs in 10 seconds. Monitor recovery time and circuit breaker trips.

### 2.5 Soak / Endurance Test
- **Purpose**: Uncover slow memory leaks, database connection pool exhaustion, file descriptor leaks, and disk log bloat over time.
- **Method**: Run at 60% capacity continuously for 12–24 hours.

---

## 3. Production k6 Example Script with Thresholds

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export const options = {
  stages: [
    { duration: '2m', target: 500 },   // Ramp-up
    { duration: '5m', target: 500 },   // Steady-state load
    { duration: '1m', target: 0 },     // Ramp-down
  ],
  thresholds: {
    // 95% of requests must complete below 150ms
    http_req_duration: ['p(95)<150', 'p(99)<300'],
    // Error rate must be strictly less than 1%
    http_req_failed: ['rate<0.01'],
  },
};

export default function () {
  const params = {
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer test-token',
    },
  };

  // 1. Fetch user deck
  const deckRes = http.get('https://api.example.com/api/v1/deck', params);
  check(deckRes, {
    'deck status is 200': (r) => r.status === 200,
  });

  sleep(1);

  // 2. Perform swipe
  const swipePayload = JSON.stringify({ target_id: 'user-789', action: 'right' });
  const swipeRes = http.post('https://api.example.com/api/v1/swipe', swipePayload, params);
  check(swipeRes, {
    'swipe status is 200': (r) => r.status === 200,
  });

  sleep(2);
}
```
