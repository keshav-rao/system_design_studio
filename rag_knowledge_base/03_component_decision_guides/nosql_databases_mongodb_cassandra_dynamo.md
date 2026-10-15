```json
{
  "topic": "nosql_database_architecture",
  "component": "nosql_engines",
  "decision_type": "technology_selection",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://www.mongodb.com/docs/manual/ | https://cassandra.apache.org/doc/",
  "version": "7.0+ / 5.0+",
  "licence": "Open-Documentation",
  "last_verified": "2026-10-14"
}
```

# NoSQL Database Architecture: MongoDB vs. Cassandra vs. DynamoDB

## 1. Architectural Taxonomy

| Engine | Data Model | Primary Consistency | Scaling Mechanism | Query Capabilities |
| :--- | :--- | :--- | :--- | :--- |
| **MongoDB** | Document (BSON) | Strong (within single document / primary) | Horizontal sharding via `mongos` router + replica sets | Rich secondary indexes, aggregation pipeline, text & geospatial search |
| **Apache Cassandra** | Wide-Column (LSM-Tree) | Tunable / Eventual (AP default) | Masterless peer-to-peer ring (Consistent Hashing) | Primary key / Clustering key lookups only; No joins, no foreign keys |
| **Amazon DynamoDB** | Key-Value / Document | Eventual (default) or Strong | Fully managed partitions based on Partition Key (PK) | Key-value lookup, range queries on Sort Key (SK), Global Secondary Indexes |

---

## 2. In-Depth Engine Architectures

### 2.1 Apache Cassandra / ScyllaDB: The Write-Optimized Workhorse
- **Internal Write Path**:
  1. Incoming write appended sequentially to the on-disk **CommitLog** (for durability).
  2. Data written directly into RAM in an in-memory sorted structure called **Memtable**.
  3. Client receives write success immediately (< 2ms write latency).
  4. When Memtable fills up, it flushes sequentially to disk as an immutable **SSTable** (Sorted String Table).
  5. Background **Compaction** merges multiple SSTables and removes obsolete versions.
- **Tombstone Hazard**: Deletes do not erase data immediately; they insert a "tombstone" marker. Querying over many deleted rows scans millions of tombstones, causing query timeouts (`TombstoneOverwhelmingException`).
- **Ideal Workloads**: Time-series metrics, chat message history (partition by `conversation_id`, cluster by `message_timestamp ASC`), massive clickstream and swipe logs.

### 2.2 MongoDB: The Dynamic Document Store
- **Internal Model**: BSON documents stored in WiredTiger storage engine (B-Tree indexed).
- **Replica Sets**: Single primary node handles all writes, replicating to secondary nodes via an `oplog`. Automated failover elects a new primary in < 10 seconds via Raft-like consensus.
- **Ideal Workloads**: Polymorphic catalogs, content management, rich profile attributes with nested arrays and sub-documents, rapid iterative prototyping.

### 2.3 Amazon DynamoDB: The Predictable Cloud Key-Value Store
- **Key Schema**:
  - **Partition Key (Hash Key)**: Determines the physical storage partition using internal hash rings.
  - **Sort Key (Range Key)**: Orders items physically on disk within the partition.
- **Single-Table Design Pattern**: Adopting DynamoDB effectively requires modeling 1-to-many and many-to-many relationships within a single table using generic `PK` (e.g., `USER#123`) and `SK` (e.g., `ORDER#456` or `PROFILE`) values, eliminating cross-table joins.
- **Ideal Workloads**: High-scale shopping carts, user sessions, game leaderboards, key-value lookups requiring guaranteed single-digit millisecond response times regardless of dataset size (from 1 GB to 100 TB).

---

## 3. Database Selection for Real-World Workloads (e.g., Dating / Tinder-like App)

### Component-by-Component Mapping
1. **User Profiles, Auth, Subscription Status**:
   - **Recommendation**: **PostgreSQL**
   - *Rationale*: Requires strict schema validation, unique email/phone constraints, ACID transactions for payment status, and relational joins with user roles.
2. **Chat Messages Between Matches**:
   - **Recommendation**: **Cassandra / ScyllaDB** or **DynamoDB**
   - *Rationale*: Chat is append-only, high volume, and strictly scoped to two users. Partition key = `conversation_id`, Sort key = `message_id` (UUIDv7 or snowflake ID). Writes are distributed evenly across nodes and range scans retrieve the last 50 messages in 3ms.
3. **Swipe History Logs (Right/Left Swipes)**:
   - **Recommendation**: **Cassandra** or **DynamoDB**
   - *Rationale*: Millions of swipes per day. Relational databases hit write IOPS limits quickly. Cassandra absorbs high-throughput writes effortlessly.
4. **Instant Match Detection & Real-time Location**:
   - **Recommendation**: **Redis** (In-Memory) backed asynchronously by Cassandra/PostgreSQL.
