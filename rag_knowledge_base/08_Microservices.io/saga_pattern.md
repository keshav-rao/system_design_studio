# Saga Pattern

## Context
You have applied the Database per Service pattern. Each service has its own database. However, some business transactions span multiple services, requiring data to be updated consistently across these independent databases.

## Problem
How do you implement transactions that span multiple services when each service has its own private database and two-phase commit (2PC) is not a viable option in modern distributed systems?

## Solution
Implement each business transaction that spans multiple services as a **Saga**. A saga is a sequence of local database transactions. Each local transaction updates the database and publishes a message or event to trigger the next local transaction in the saga.

If a local transaction fails because it violates a business rule, the saga executes a series of **compensating transactions** that undo the changes that were made by the preceding local transactions.

### Coordination Types
There are two primary ways to coordinate sagas:
1.  **Choreography:** Each local transaction publishes domain events that trigger local transactions in other services. There is no central coordinator.
2.  **Orchestration:** An orchestrator (an object/class) tells the participants what local transactions to execute.

## Consequences
*   **Benefits:** Enables distributed transactions without tight coupling or synchronous blocking (unlike 2PC).
*   **Drawbacks:** Increases complexity. Harder to debug and trace. Requires writing compensating logic for rollbacks.