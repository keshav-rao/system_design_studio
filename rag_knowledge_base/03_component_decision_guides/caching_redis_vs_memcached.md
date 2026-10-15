```json
{
  "topic": "caching_and_in_memory_stores",
  "component": "redis",
  "decision_type": "technology_selection",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://redis.io/docs/latest/",
  "version": "7.2+",
  "licence": "Open-Documentation",
  "last_verified": "2026-10-14"
}
```

# Caching Decision Guide: Redis vs. Memcached

## 1. Executive Comparison

| Feature | Redis | Memcached |
| :--- | :--- | :--- |
| **Architecture** | Single-threaded event loop (I/O multiplexing with `epoll`), background threads for fsync and eviction | Multi-threaded with fine-grained slab locking |
| **Data Structures** | Strings, Hashes, Lists, Sets, Sorted Sets (ZSET), Bitmaps, HyperLogLogs, Geospatial (`GEOADD`), Streams | Plain Key-Value strings (byte arrays) only |
| **Persistence** | Snapshotting (RDB) and Append-Only File (AOF) with configurable fsync | None (purely volatile RAM; data vanishes on restart) |
| **Replication & HA** | Primary-Replica with Sentinel automatic failover or Redis Cluster | None natively (client-side hashing across independent servers) |
| **Clustering** | Redis Cluster (16,384 hash slots, distributed master-replica topology) | Client-side consistent hashing ring (e.g., Ketama) |
| **Max Value Size** | 512 MB per value | 1 MB per value (configurable up to 10MB) |
| **Transactions** | `MULTI` / `EXEC` blocks and Lua scripting for atomicity | Atomic increment / decrement (`INCR`/`DECR`) and CAS (Check-And-Set) |

---

## 2. In-Depth Redis Capabilities

### 2.1 Native Rich Data Structures
1. **Geospatial (`GEOADD`, `GEORADIUSBYMEMBER`, `GEOSEARCH`)**:
   - Stores coordinates using 52-bit Geohash integers embedded in a Sorted Set (ZSET).
   - Enables queries like: *"Find all active users within 10km of user X"* in $O(N + \log M)$ time.
2. **Sets (`SADD`, `SISMEMBER`, `SINTER`)**:
   - Stores mutual swipe tracking: User A's set of right swipes. When User B right-swipes User A, execute `SISMEMBER user:B:likes user:A:id`. If true, an instant match is confirmed without touching the relational database!
3. **Sorted Sets (ZSET)**:
   - Maintains real-time leaderboards, rate-limit sliding windows (`ZADD timestamp`), and priority message feeds ordered by score.
4. **Redis Streams**:
   - Log-like append-only data structure supporting consumer groups, at-least-once delivery, and pending entry lists (PEL) for lightweight event processing.

---

## 3. Deep-Dive: When to Use Redis in a Dating / Swipe Application (e.g., Tinder-like)

### Why Tinder-like Architectures Use Redis
1. **Instant Mutual Match Detection**:
   - Relational database queries for mutual likes require expensive bidirectional lookups:
     `SELECT 1 FROM likes WHERE user_id = B AND target_id = A;`
   - Under 50,000 swipes/second, this overwhelms Postgres connection pools and SSD IOPS.
   - In Redis: Storing `likes:<user_id>` as a Set allows sub-millisecond atomic verification:
     `SISMEMBER likes:target_id swiper_id` -> returns 1 in 0.2ms.
2. **Ephemeral Geolocation Tracking**:
   - Users continuously broadcast GPS coordinates while browsing. Persisting transient GPS updates to disk is an anti-pattern.
   - Redis Geospatial handles high-frequency location updates in memory and queries proximity bounding boxes effortlessly.
3. **Recommendation Deck Prefetching**:
   - A user's next 50 recommended profile candidates are precomputed by an offline ML pipeline and cached in a Redis List (`LPUSH` / `RPOP`). Swiping pops items off the list with zero DB latency.
4. **WebSocket Session Registry & Distributed Presence**:
   - Maps active socket connections to worker node IDs using Redis Hashes: `HSET user:presence:123 gateway_ip 10.0.1.42`.

### When Redis is UNNECESSARY (Avoid Over-Engineering)
1. **Early Stage / Small User Base (< 10,000 MAU)**:
   - When total concurrent users are under a few hundred, a single PostgreSQL instance with a `PostGIS` extension for geolocation and a well-indexed `likes` table (`CREATE UNIQUE INDEX ON likes (user_id, target_id)`) can handle all traffic easily. Adding Redis adds operational burden (backups, memory tuning, eviction risks, cache invalidation synchronization).
2. **Strict Financial Ledgers & Auditing**:
   - Redis is not an ACID database. Even with AOF `fsync everysec`, up to 1 second of transactions can be lost during an ungraceful crash. Billing and subscription transactions belong strictly in PostgreSQL or Spanner.
3. **Large Cold Datasets (> 1 TB)**:
   - RAM costs ~$3–5/GB/month on cloud providers vs. ~$0.08/GB for NVMe SSDs. Storing inactive user profiles or old chat histories in Redis wastes expensive RAM.

---

## 4. Configuration Limits and Failure Modes
- **Max Memory Policy**: In production, always set `maxmemory` explicitly (e.g., 75% of instance RAM) and configure `maxmemory-policy volatile-lru` or `allkeys-lru`. If memory reaches 100% without eviction, Redis returns OOM errors on all write operations.
- **Single-Threaded Head-of-Line Blocking**:
  - Running $O(N)$ commands like `KEYS *`, `SMEMBERS` on sets with 1,000,000 items, or `FLUSHALL` blocks the entire server event loop, stalling all client requests.
  - *Mitigation*: Always use cursor-based iteration: `SCAN`, `SSCAN`, `HSCAN`.
