```json
{
  "topic": "distributed_systems_theory",
  "component": "storage_layer",
  "decision_type": "technology_selection",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://en.wikipedia.org/wiki/CAP_theorem",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# CAP and PACELC Theorems in Distributed Architecture

## 1. CAP Theorem (Brewer's Theorem)
In a distributed asynchronous network, a data store can guarantee at most two of the following three properties:

- **Consistency (C)**: Every read request receives the most recent write or returns an error. All nodes see the exact same data simultaneously (Linearizability).
- **Availability (A)**: Every non-failing node returns a non-error response for every incoming request, though it cannot guarantee it is the latest write.
- **Partition Tolerance (P)**: The system continues to operate despite arbitrary communication loss, delayed packets, or dropped network links between cluster nodes.

### The Inevitability of Partition Tolerance
In distributed cloud infrastructure, network partitions (cables cut, switch failures, cross-region timeouts, GC pauses) are physical certainties. Thus, the system architect cannot "choose C and A and reject P". 
When a network partition occurs, the architecture MUST choose between:
1. **CP (Consistency / Partition Tolerance)**: Reject writes or delay reads to prevent stale or conflicting data (e.g., Google Spanner, CockroachDB, etcd, Apache HBase).
2. **AP (Availability / Partition Tolerance)**: Allow writes and reads on isolated partitions, resolving discrepancies asynchronously using conflict resolution (e.g., Apache Cassandra, Amazon DynamoDB, CouchDB).

---

## 2. PACELC Theorem (Abadi's Extension)
The CAP theorem only applies **when there is a network partition**. Daniel Abadi introduced PACELC to govern regular operation:

> **If there is a Partition (P):**
> Choose between **Availability (A)** and **Consistency (C)**.
> **Else (E) (during normal operation):**
> Choose between **Latency (L)** and **Consistency (C)**.

### Classification Matrix
| System | Partition Guarantee | Normal Operation Trade-off | Classification | Use Cases |
| :--- | :--- | :--- | :--- | :--- |
| **Apache Cassandra** | Availability (A) | Latency (L) | **PA/EL** | Metrics, clickstreams, chat inbox sync, swipe queues |
| **Amazon DynamoDB** | Availability (A) | Latency (L) *(default)* | **PA/EL** | High-throughput cart, session tracking, social reactions |
| **MongoDB** | Consistency (C) | Consistency (C) *(default)* | **PC/EC** | Catalogs, order processing, document records |
| **Google Spanner** | Consistency (C) | Consistency (C) | **PC/EC** | Global financial ledgers, strict ACID across regions |
| **PostgreSQL (Sync Rep)** | Consistency (C) | Consistency (C) | **PC/EC** | Core banking, billing, inventory reservation |

---

## 3. Tunable Quorums ($R + W > N$)
Distributed stores like Cassandra and DynamoDB avoid hard binary choices via configurable quorums:
- $N$ = Number of replicas across the cluster.
- $W$ = Number of replicas that must acknowledge a write before returning success.
- $R$ = Number of replicas that must respond to a read query.

### Strong Consistency Quorum
When $R + W > N$, the read set and write set must overlap by at least one node, guaranteeing that the reader observes the latest committed version.
- **Typical setup**: $N=3, W=2, R=2$.
- **High write throughput (AP)**: $N=3, W=1, R=1$ (Eventual consistency, potential read skew).
- **Fast read, slow write**: $N=3, W=3, R=1$.

---

## 4. Failure Scenarios and Mitigations
1. **Split-Brain Syndrome**: Two partitioned sub-clusters accept concurrent writes, believing the other died.
   - *Mitigation*: Raft/Paxos consensus requiring majority quorum ($\lfloor N/2 \rfloor + 1$) to elect a leader or commit writes.
2. **Stale Reads in AP Mode**: Client updates profile, immediately reloads, and sees outdated data.
   - *Mitigation*: Read-your-own-writes session consistency using client version vectors or routing user reads to primary for 5 seconds post-write.
