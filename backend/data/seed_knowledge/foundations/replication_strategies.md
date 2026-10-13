# Database Replication Strategies

## Single-Leader (Primary-Replica) Replication
- All writes are processed exclusively by the leader node.
- The leader streams change events (WAL or binlog) to one or more read replicas.
- **Synchronous vs Asynchronous**:
  - *Synchronous*: Leader waits for confirmation from at least one replica before committing. Guarantees zero data loss (RPO = 0) at the expense of write latency.
  - *Asynchronous*: Leader commits immediately. High throughput, but risks replication lag and data loss during sudden primary failover.
- **Failover**: Requires consensus coordination (e.g. Raft, Patroni with etcd) to elect a new primary and reconfigure replicas.

## Multi-Leader Replication
- Multiple datacenters each maintain an active primary node that accepts local writes.
- Primaries asynchronously replicate changes across WAN links.
- *Conflict Resolution*: Writes to the same record in two datacenters produce concurrent conflicts. Handled via Last-Write-Wins (LWW), multi-version concurrency, or Conflict-Free Replicated Data Types (CRDTs).

## Leaderless Replication (Quorum-Based)
- Popularized by Amazon Dynamo, Apache Cassandra, and ScyllaDB.
- Clients send reads and writes concurrently to all $N$ replicas.
- **Quorum Equation**:
  - $W$: number of replicas that must acknowledge a write.
  - $R$: number of replicas queried for a read.
  - If $R + W > N$, the read set is guaranteed to overlap with the write set, ensuring strong consistency.
- **Self-Healing**: Utilizes read repair (client detects stale replica and pushes latest value) and anti-entropy background processes using Merkle trees.
