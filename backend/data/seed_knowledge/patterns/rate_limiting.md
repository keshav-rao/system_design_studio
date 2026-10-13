# Distributed Rate Limiting Algorithms

## Purpose
Rate limiters protect API gateways and backend resources from traffic spikes, denial-of-service abuse, scraping, and noisy neighbors.

## Algorithms
1. **Token Bucket**:
   - A bucket has fixed capacity $C$ and refills at a constant rate $r$ tokens/second.
   - Each request attempts to draw $1$ token. If tokens remain, request proceeds; if empty, request is rejected (HTTP 429).
   - *Advantage*: Naturally accommodates bursts up to capacity $C$ while enforcing long-term average rate $r$.
2. **Leaky Bucket**:
   - Requests enter a FIFO queue of capacity $C$ and drain at a strictly constant rate.
   - If the queue overflows, incoming requests are dropped.
   - *Advantage*: Smooths out bursts, providing constant predictable downstream egress traffic.
3. **Fixed Window Counter**:
   - Counts requests within discrete clock intervals (e.g. 12:00:00 to 12:00:59).
   - *Flaw*: Boundary double-burst problem — a user can send max limit at 12:00:59 and another max limit at 12:01:00, allowing $2\times$ traffic in 2 seconds.
4. **Sliding Window Counter**:
   - Approximates rate by interpolating between the previous window and the current window:
     $\text{count} = \text{current\_window} + \text{prev\_window} \times (1 - \text{fraction\_elapsed})$.
   - Prevents boundary burst issues with minimal memory (requires only two integer counters per key in Redis).

## Distributed Coordination via Redis
In multi-node API gateways, rate limiter state must be centrally synchronized:
- Use Redis with Lua scripts or Redis Cell (`CL.THROTTLE`) to make the read-modify-write operation completely atomic.
- Avoid race conditions across API instances without needing distributed locks.
- Return standard headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, and `Retry-After`.
