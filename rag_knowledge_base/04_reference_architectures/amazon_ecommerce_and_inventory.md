```json
{
  "topic": "reference_architecture",
  "component": "ecommerce_platform",
  "decision_type": "reference_architecture",
  "content_type": "reference_architecture",
  "cloud_provider": "provider_neutral",
  "source_url": "https://aws.amazon.com/architecture/patterns/",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# Reference Architecture: High-Scale E-Commerce & Flash-Sale Inventory Management

## 1. System Requirements & The Flash-Sale Problem
- **Problem**: 100,000 users attempt to purchase 1,000 limited-edition items simultaneously (Flash Sale / Black Friday).
- **Core Challenge**: Prevent inventory overselling while avoiding database connection pool exhaustion and deadlocks under massive concurrent transactions.

---

## 2. Flash-Sale Architecture Topology

```
[Clients (Browsers / Mobile Apps)]
                │
                ▼
[Cloudflare / CloudFront CDN & WAF (Virtual Waiting Room)]
                │
                ▼
    [API Gateway (Rate Limiter)]
                │
                ▼
[Order Service] ──(Atomic Lua Script)──> [Redis Cluster (Inventory Counter)]
        │                                  (Decrements quantity if > 0)
        │ (Success)
        ▼
[Kafka / SQS Order Queue]
        │
        ▼
[Payment & Fulfillment Worker Fleet]
        ├── 1. Process Stripe/Adyen Payment
        ├── 2. Saga Orchestrator (Compensating transaction if payment fails)
        └── 3. Persist Order to PostgreSQL Primary
```

---

## 3. Inventory Reservation Patterns

### 3.1 The Pessimistic Database Locking Trap (Anti-Pattern)
- `SELECT quantity FROM items WHERE id = 1 FOR UPDATE;`
- Under 50,000 concurrent requests, all transactions queue up waiting for row locks. Connection pools saturate, database CPU hits 100%, and API response times degrade to 30+ seconds.

### 3.2 Redis Atomic Lua Scripting (High-Throughput Solution)
```lua
-- Atomic check-and-decrement in Redis RAM
local current = redis.call('get', KEYS[1])
if not current or tonumber(current) <= 0 then
    return 0 -- Sold out
end
redis.call('decr', KEYS[1])
return 1 -- Successfully reserved
```
- Executes in memory in < 0.3ms without locks.
- If the script returns 1, the user is guaranteed an inventory reservation for 10 minutes. An asynchronous order message is published to Kafka for durable database persistence and payment processing.
- If payment fails or times out, a compensating message executes `INCR` in Redis to release the reservation back into the pool.

---

## 4. Distributed Saga Pattern for Order Fulfillment
Because microservices maintain private databases (Order DB, Payment DB, Inventory DB), distributed two-phase commit (2PC) is too fragile.
- **Orchestrated Saga**:
  1. `CreatePendingOrder` (Order Service)
  2. `ReserveInventory` (Inventory Service)
  3. `ChargeCreditCard` (Payment Service)
  4. `MarkOrderConfirmed` (Order Service)
- If step 3 fails (insufficient funds):
  - Orchestrator triggers compensating action: `CancelInventoryReservation` and `MarkOrderFailed`.
