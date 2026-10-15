```json
{
  "topic": "consistency_and_transactions",
  "component": "database",
  "decision_type": "technology_selection",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://jepsen.io/consistency",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# Distributed Consistency Models and Transaction Isolation Levels

## 1. Spectrum of Consistency Models
Consistency in distributed systems exists on a spectrum between performance and correctness:

```
[Strict / Linearizable] --> [Sequential] --> [Causal] --> [Read-After-Write] --> [Eventual]
<-- Highest Latency, Lowest Availability                  Lowest Latency, Highest Availability -->
```

### 1.1 Linearizability (Strict Consistency)
- **Definition**: Every operation appears to take effect instantaneously at a discrete point in time between its invocation and completion. A global real-time clock ordering is preserved.
- **Implementations**: Google Cloud Spanner (TrueTime hardware with atomic clocks), CockroachDB (Hybrid Logical Clocks), etcd/Consul (Raft consensus).
- **Use Case**: Financial balance deduction, ticket seat locking, distributed leader election.

### 1.2 Sequential Consistency
- **Definition**: Operations can be reordered relative to real-time wall clocks, but all nodes observe the exact same sequence of operations, respecting single-process program order.
- **Implementations**: Apache ZooKeeper.

### 1.3 Causal Consistency
- **Definition**: Operations that are causally related (cause and effect) must be seen by every node in the same order. Concurrent operations with no causal relationship can be seen in different orders.
- **Implementations**: MongoDB (causal consistency sessions with Lamport timestamps).
- **Use Case**: Comment threads, chat replies (ensuring an answer does not appear before its question).

### 1.4 Eventual Consistency
- **Definition**: If no new updates are made, all replicas will eventually converge to identical values.
- **Implementations**: Amazon DynamoDB, Apache Cassandra, CouchDB, DNS caching.
- **Conflict Resolution Mechanisms**:
  - **Last-Write-Wins (LWW)**: Uses node timestamps; vulnerable to clock drift.
  - **Conflict-Free Replicated Data Types (CRDTs)**: Mathematically provable convergence for sets, counters, and maps without locks.
  - **Vector Clocks**: Tracks causal histories across nodes; surfaces conflicts to client application for resolution (e.g., Git merge style).

---

## 2. ACID Transaction Isolation Levels (ANSI SQL vs Actual Realities)

| Isolation Level | Dirty Read | Non-Repeatable Read | Phantom Read | Serialization Anomaly | Write Skew | Typical Engine Implementation |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Read Uncommitted** | Possible | Possible | Possible | Possible | Possible | Rarely used in production |
| **Read Committed** | Prevented | Possible | Possible | Possible | Possible | PostgreSQL default, Oracle |
| **Repeatable Read** | Prevented | Prevented | Prevented (MVCC) | Possible | Possible | MySQL InnoDB default |
| **Snapshot Isolation** | Prevented | Prevented | Prevented | Possible | Possible | PostgreSQL MVCC (RR mode) |
| **Serializable** | Prevented | Prevented | Prevented | Prevented | Prevented | Two-Phase Locking (2PL) or SSI |

### The Write Skew Trap
Snapshot Isolation avoids dirty, non-repeatable, and phantom reads, but is vulnerable to **Write Skew**:
- Two concurrent transactions read overlapping data, verify a shared constraint (e.g., "at least one doctor must be on call"), and both commit changes based on their stale local snapshots.
- *Mitigation in PostgreSQL*: Use `SERIALIZABLE` transaction isolation or explicit locking (`SELECT ... FOR UPDATE`).
