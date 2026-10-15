```json
{
  "topic": "database_performance",
  "component": "connection_pooler",
  "decision_type": "capacity_planning",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://github.com/brettwooldridge/HikariCP/wiki/About-Pool-Sizing",
  "version": "1.0",
  "licence": "Apache-2.0",
  "last_verified": "2026-10-14"
}
```

# Database Limits, Connection Pooling Math, and Disk IOPS Bottlenecks

## 1. Connection Pool Sizing: The Counter-Intuitive Math

A common rookie mistake is assuming: *"I have 10,000 concurrent web users, so I should set `max_connections = 10,000` in PostgreSQL."*
Doing so will cause catastrophic CPU context switching and bring the server to a complete crawl.

### The HikariCP / PostgreSQL Formula
$$\text{Pool Size} = (2 \times \text{CPU Cores}) + \text{Disk Spindles / Concurrent NVMe Channels}$$

- On an 8-core database server with fast NVMe SSD storage:
  $$\text{Optimal Connections} = (2 \times 8) + 1 = 17 \text{ connections!}$$
- Even under 50,000 concurrent requests, a connection pool of **20–50 backend connections** will process transactions faster with lower median latency than a pool of 1,000 connections because the CPU is executing instructions rather than switching process memory context.

---

## 2. PgBouncer Modes in Production

When frontend microservices scale to hundreds of containers, they cannot each hold 10 direct database connections. **PgBouncer** is placed as a proxy:

| Mode | Behavior | Best Suited For | Caveats |
| :--- | :--- | :--- | :--- |
| **Session Pooling** | Connection assigned to client for the entire duration of its TCP connection | Applications using prepared statements or session-level advisory locks | Least efficient; holds connection during client idle time |
| **Transaction Pooling** | Connection assigned only for the duration of a single `BEGIN ... COMMIT` block | High-throughput web APIs (FastAPI, Express, Django) | Prepared statements must use named statement cache or generic execute |
| **Statement Pooling** | Connection returned immediately after every single SQL statement | Batch audit logging | Multi-statement transactions are strictly forbidden |

---

## 3. Storage Hardware Bottlenecks: Cloud Disk IOPS & Throughput

In cloud environments (AWS EBS gp3, Azure Managed Disks, GCP Persistent Disk), disk performance is throttled by two independent parameters:
1. **IOPS (Input/Output Operations Per Second)**:
   - AWS gp3 provides baseline 3,000 IOPS free, scalable to 16,000 IOPS.
   - If an index scan reads random 8 KB database pages, 3,000 IOPS allows at most:
     $$3,000 \times 8 \text{ KB} = 24 \text{ MB/sec of random I/O}.$$
   - Once IOPS limit is reached, disk queue length spikes from 0 to 50+, and query latency jumps from 1ms to 500ms.
2. **Burst Balance Depletion**:
   - Older burstable volume types (gp2) use burst bucket credits. When credits run dry during traffic spikes, IOPS plummet to baseline, crashing production. Always use **gp3** with provisioned IOPS or **io2** for primary databases.

---

## 4. Mandatory Database Guardrail Settings
```sql
-- Abort any statement executing longer than 3 seconds (prevents runaway rogue queries)
SET statement_timeout = '3000';

-- Abort any connection idle in transaction for longer than 10 seconds (prevents lock starvation)
SET idle_in_transaction_session_timeout = '10000';

-- Log any slow query taking longer than 250ms for performance tuning
SET log_min_duration_statement = 250;
```
