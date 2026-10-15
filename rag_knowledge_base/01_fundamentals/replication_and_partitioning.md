```json
{
  "topic": "replication_and_sharding",
  "component": "database",
  "decision_type": "pattern_design",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://dataintensive.net/",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# Database Replication and Sharding Architecture

## 1. Replication Topologies

### 1.1 Single-Leader (Primary-Replica)
- **Data Flow**: All write requests are sent to the primary leader node. The leader records mutations in its Write-Ahead Log (WAL) and streams changes to read replicas.
- **Replication Modes**:
  - **Synchronous**: Leader waits for replica acknowledgement before committing. Guarantees zero data loss (RPO = 0), but increases write latency and stalls if replica fails.
  - **Asynchronous**: Leader acknowledges write immediately; streaming lag ($t_{lag}$) exists. Blazing fast, but uncommitted WAL entries are lost if primary crashes before sync.
  - **Semi-Synchronous**: (e.g., PostgreSQL with `synchronous_commit = on` and `num_sync = 1`) Waits for at least one replica, while streaming to remaining replicas asynchronously.

### 1.2 Multi-Leader (Active-Active)
- **Data Flow**: Multiple leader nodes accept writes simultaneously, often across separate geographic regions.
- **Benefits**: Local low-latency writes across continents; continues operating during datacenter outage.
- **Challenges**: Cross-datacenter conflict resolution. Techniques: Last-Write-Wins (risk of lost updates), CRDTs, or custom operational transformation.

### 1.3 Leaderless (Dynamo-Style)
- **Data Flow**: Client writes directly to multiple peer nodes.
- **Mechanisms**: Read Repair (detecting stale replica values during read) and Anti-Entropy background processes using Merkle trees.

---

## 2. Horizontal Partitioning (Sharding) Strategies

When dataset size exceeds single-node storage limits (> 2–4 TB) or write IOPS exceed drive bandwidth (> 40,000 IOPS), horizontal partitioning becomes mandatory.

### 2.1 Range-Based Sharding
- Keys divided into contiguous intervals (e.g., User IDs 1–1,000,000 on Shard 1, 1,000,001–2,000,000 on Shard 2).
- **Pro**: Efficient range scans (`WHERE created_at BETWEEN X AND Y`).
- **Con**: Severe write hotspots on the latest time interval.

### 2.2 Hash-Based Sharding
- Shard assigned via hash function: $Shard = \text{hash}(PartitionKey) \pmod N$.
- **Pro**: Uniform distribution of write load across disks.
- **Con**: Re-sharding when adding node $N+1$ forces migration of $\frac{N}{N+1} \approx 90\%$ of keys.

### 2.3 Consistent Hashing
- Hash space mapped to a virtual ring ($0 \dots 2^{32}-1$ or $2^{128}-1$).
- Both nodes and keys are hashed onto the ring. A key is stored on the first node encountered clockwise.
- **Virtual Nodes (vnodes)**: Each physical machine is mapped to 128–256 virtual tokens on the ring to prevent skew and smooth out rebalancing.
- **Cost of Rescaling**: When a node is added or removed, only $K/N$ keys move (where $K$ = total keys, $N$ = total nodes).
- **Production Examples**: Amazon Dynamo, Apache Cassandra, Couchbase, Discord gateway session distribution.

---

## 3. Sharding Anti-Patterns and Gotchas
1. **Cross-Shard Joins**: Queries requiring data across shards cause network fan-out and quadratic latency degradation.
   - *Fix*: Denormalize related entities into the same shard key (e.g., shard by `user_id`, placing both `users` and `user_posts` on the same shard).
2. **Celebrity / Hotspot Keys**: A single high-profile user (e.g., Elon Musk with 150M followers) causes a single partition to melt down.
   - *Fix*: Append random salt suffixes to hot partition keys (e.g., `user_id_salt_0` to `user_id_salt_9`) and fan-out reads.
