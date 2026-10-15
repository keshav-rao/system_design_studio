```json
{
  "topic": "architecture_decision_record",
  "component": "primary_data_storage",
  "decision_type": "technology_selection",
  "content_type": "adr",
  "cloud_provider": "provider_neutral",
  "source_url": "https://martinfowler.com/bliki/ArchitectureDecisionRecord.html",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# ADR 001: Selection of Primary Relational vs. NoSQL Storage Engine

## Status
**Accepted**

## Context
When designing application architectures (such as user accounts, authentication, e-commerce, and high-concurrency platforms), the engineering team must decide between a Relational SQL database (e.g., PostgreSQL) and a NoSQL database (e.g., MongoDB, DynamoDB, Cassandra). 

The requirements include:
1. Strong consistency and transactional ACID guarantees for billing, subscriptions, and identity records.
2. High-speed lookup and indexing on relational entities.
3. Long-term schema evolvability with safe migrations.
4. Scale-up potential to millions of active users.

## Decision
We select **PostgreSQL 16+** as the default primary database for structured domain entities, user accounts, and financial transactions, augmented by **NoSQL engines (Cassandra/DynamoDB)** only for specialized write-heavy, denormalized, or immutable time-series data streams (e.g., chat logs, swipe logs, telemetry).

## Alternatives Considered
1. **Pure NoSQL (MongoDB)**:
   - *Rejected for core domain*: Lacks strict schema enforcement out of the box; multi-document ACID transactions incur severe performance overhead compared to native relational engines; foreign key referential integrity is absent.
2. **Pure Distributed SQL (Google Spanner / CockroachDB)**:
   - *Rejected for general early-to-mid tier*: Prohibitive baseline cost (~$900–$2,000/mo minimum per cluster); introduces unnecessary latency and complexity before single-node relational boundaries are approached.
3. **MySQL / MariaDB**:
   - *Alternative viable*: PostgreSQL was chosen over MySQL due to advanced JSONB indexing, rich spatial query capabilities (PostGIS), superior MVCC execution, and broader ecosystem extensions.

## Consequences & Trade-offs
### Positive Consequences
- **Strict Data Integrity**: Foreign keys, check constraints, and ACID transactions prevent data corruption.
- **Rich Querying**: Complex joins, window functions, and JSONB document querying within a single engine.
- **Mature Tooling**: Robust migration frameworks (Alembic, Flyway), connection pooling (PgBouncer), and extensive cloud-managed offerings across AWS (RDS/Aurora), GCP (Cloud SQL), and Azure.

### Negative Consequences & Risks
- **Horizontal Scaling Ceiling**: Primary write leader can only scale vertically on a single host. Horizontal write sharding requires application-level partitioning or Citus extension.
- **Connection Overhead**: Process-per-connection architecture demands PgBouncer connection pooling when scaling past 100 concurrent clients.
