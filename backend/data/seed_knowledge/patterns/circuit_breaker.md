# Circuit Breaker and Graceful Degradation Pattern

## Motivation
In distributed microservice architectures, cascading failures occur when a downstream dependency slows down or becomes unresponsive. Calling services exhaust their worker thread pools waiting for HTTP timeouts, causing the entire upstream application stack to collapse.

## State Transitions
A Circuit Breaker wraps external calls and manages three distinct states:
1. **CLOSED**:
   - Operations execute normally.
   - Monitors failure rates over a sliding window (e.g. last 100 requests).
   - If failure rate or slow request percentage exceeds a threshold (e.g. 50% errors), the breaker trips to **OPEN**.
2. **OPEN**:
   - All subsequent incoming calls fail fast immediately without attempting the network request.
   - Fallback response (cached stale data, default value, or 503 Service Unavailable) is returned instantly.
   - Worker threads and connection pools remain unblocked.
   - A reset timer begins (e.g., 30 seconds).
3. **HALF-OPEN**:
   - Once reset timeout expires, the breaker permits a limited trial number of probe requests (e.g. 5 requests).
   - If all probe requests succeed, the breaker resets to **CLOSED**.
   - If any probe fails, the breaker immediately returns to **OPEN** and resets the backoff timer.

## Best Practices
- Combine circuit breakers with aggressive client timeouts (e.g., 500ms max timeout for external calls).
- Provide meaningful fallbacks (e.g. recommendation service fallback: return static top 10 popular items).
- Use exponential backoff with full jitter on retries to prevent retry stampedes.
