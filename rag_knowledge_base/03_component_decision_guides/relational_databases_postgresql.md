```json
{
  "topic": "relational_database_architecture",
  "component": "postgresql",
  "decision_type": "technology_selection",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://www.postgresql.org/docs/current/",
  "version": "16+",
  "licence": "PostgreSQL-Licence",
  "last_verified": "2026-10-14"
}
```

# Relational Databases Decision Guide: PostgreSQL Architecture and Scaling Limits

## 1. PostgreSQL Core Architecture

### 1.1 Process Model and Connection Memory Cost
- Unlike MySQL or multithreaded databases, PostgreSQL allocates a separate OS process per incoming client connection (`fork()` model).
- Each connection consumes ~5 MB to 10 MB of RAM (in addition to `work_mem` allocated per query sort/hash operation).
- **Rule of Thumb**: Connecting 1,000 application threads directly to PostgreSQL consumes ~10 GB of RAM in overhead alone and causes catastrophic context-switching CPU thrashing.
- **Mandatory Component**: Always place a connection pooler like **PgBouncer** (in transaction pooling mode) between application servers and PostgreSQL. PgBouncer multiplexes 10,000 application client connections into 50–100 persistent database backend connections.

### 1.2 Multi-Version Concurrency Control (MVCC) and Vacuuming
- In PostgreSQL, updates and deletes do not overwrite data in place.
  - `UPDATE` = Write new row version (tuple) with `xmin` + mark old tuple as dead with `xmax`.
  - `DELETE` = Mark tuple dead with `xmax`.
- Readers never block writers, and writers never block readers.
- **Autovacuum**: Background daemon that scans pages, reclaims disk space occupied by dead tuples, and updates data statistics for the query planner.
- *Failure Mode*: If autovacuum cannot keep up with high-frequency update tables (e.g., continuous GPS location updates), "table bloat" causes query latencies to explode. High-frequency transient updates must be routed to Redis or unlogged tables.

---

## 2. Advanced Indexing Strategies

| Index Type | Algorithmic Structure | Best Suited For | Query Example |
| :--- | :--- | :--- | :--- |
| **B-Tree** | Balanced Multi-way Tree | Equality and range queries on scalar data | `WHERE user_id = 42`, `WHERE age BETWEEN 21 AND 35` |
| **GiST (Generalized Search Tree)** | R-Tree / Spatial Tree | Geospatial 2D/3D polygons, bounding boxes, distance | `ST_DWithin(location, ST_Point(lon, lat), 5000)` (PostGIS) |
| **GIN (Generalized Inverted Index)** | Inverted Index (term-to-row mapping) | JSONB document keys, arrays, full-text search tokens | `WHERE attributes @> '{"interests": ["hiking"]}'` |
| **BRIN (Block Range Index)** | Min/Max values per physical disk block range | Massive append-only chronological time-series data | `WHERE created_at >= '2026-01-01'` on 1-billion row log table |

---

## 3. Scaling PostgreSQL: Read Replicas & Connection Pooling

### 3.1 Streaming Replication Architecture
```
[Application Clients] 
         │ (10,000 conns)
         ▼
    [PgBouncer] 
         │ (50 persistent conns)
         ▼
[PostgreSQL Primary (Write Leader)] 
         │
         ├── (WAL Streaming Asynchronous) ──> [Read Replica 1] (Read Queries)
         └── (WAL Streaming Asynchronous) ──> [Read Replica 2] (Analytics / Search)
```

- **Replication Lag**: Replicas apply WAL asynchronously. During heavy write bursts, replica lag can increase to 100ms – 5s.
- **Read-After-Write Consistency**: If a user updates their profile and immediately navigates to their profile page, a query routed to a lagging read replica will show the old data.
- **Architectural Solution**: Route all writes and subsequent reads from the same user for 5 seconds to the Primary node; route general search/catalog browsing queries to Read Replicas.

---

## 4. When PostgreSQL is the Ideal Choice
1. **Core User Account & Authentication**: Strict ACID compliance, unique email/phone constraints, foreign key referential integrity between users, roles, and permissions.
2. **Billing and Subscriptions**: Invoicing, payment ledger, credit transactions where financial correctness is non-negotiable.
3. **Structured Entity Relationships**: E.g., Matches, block lists, chat conversation memberships.
4. **Moderate Geospatial Proximity**: With the `PostGIS` extension, PostgreSQL is an enterprise-grade spatial database capable of handling complex polygon queries.
