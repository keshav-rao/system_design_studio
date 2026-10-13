# Idempotency Keys and Safe Retry Mechanisms

## The Duplicate Execution Problem
In network protocols, the network between client and server is unreliable. If a client sends a payment POST request and the network drops the HTTP response, the client cannot know whether the server executed the charge or failed before processing. Re-sending blindly causes double billing.

## Idempotency Key Architecture
An idempotency key is a client-generated unique identifier (UUID v4) sent in an HTTP request header (e.g. `Idempotency-Key: 7b31...`).

### Processing Protocol
1. **Acquire Key State**:
   - In a transaction or Redis atomic `SET NX EX`, check if the idempotency key exists:
   - If not found: insert key with status `IN_PROGRESS` and a TTL (e.g. 24 hours).
   - If found with status `IN_PROGRESS`: reject concurrent duplicate request with HTTP 409 Conflict.
   - If found with status `COMPLETED`: return the exact cached HTTP response and body from the previous run without executing the mutation again.
2. **Execute Business Transaction**:
   - Run business logic and database writes.
3. **Persist Result**:
   - Update key record to `COMPLETED` along with response status code and JSON payload.
   - Acknowledge success to the client.

## Critical Storage Requirements
- Store the SHA-256 hash of the request parameters alongside the idempotency key.
- If a client re-uses an existing key but sends a different request payload, immediately reject with HTTP 422 Unprocessable Entity (key collision error).
- Standard pattern adopted by Stripe, PayPal, and AWS APIs.
