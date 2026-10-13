# CQRS and Event Sourcing Pattern

## Command Query Responsibility Segregation (CQRS)
CQRS separates read and write operations into distinct specialized data models:
- **Command Model**: Optimized exclusively for high-throughput write validation, invariant enforcement, and state transitions. Rejects invalid business state.
- **Query Model**: Materialized views, read-replicas, or search indexes (Elasticsearch/OpenSearch) tailored precisely to specific UI screen access patterns.

### Why Separate Models?
Complex joins and full-text searches against normalized transactional tables choke write performance. By replicating write events into specialized read-optimized denormalized stores, reads execute in single-digit milliseconds without locking transaction tables.

## Event Sourcing
Instead of storing only the current snapshot of an entity, Event Sourcing records every state change as an immutable append-only event log (e.g. `OrderCreated`, `PaymentCaptured`, `ItemsDispatched`).
- Current state is reconstructed by replaying all historical events from genesis.
- **Snapshots**: Periodic materialized snapshots (every 100 or 1000 events) prevent linear replay latency as history grows.
- **Auditability**: Complete temporal audit trail. Can inspect exact state at any timestamp in the past.

## Integration Architecture
1. Client issues Command to write service.
2. Write service appends event to append-only Event Store (e.g., PostgreSQL with transactional outbox or Kafka).
3. Change Data Capture (CDC) or message consumers process events and update read projections asynchronously.
4. Read queries hit denormalized query projections with eventual consistency.
