```json
{
  "topic": "caching_strategies",
  "component": "cache_layer",
  "decision_type": "pattern_design",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://redis.io/docs/latest/develop/use/caching/",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# Caching Principles, Access Patterns, and Invalidation Strategies

## 1. Caching Access Patterns

### 1.1 Cache-Aside (Lazy Loading)
- **Flow**:
  1. Application checks cache for `key`.
  2. Cache hit: returns data immediately.
  3. Cache miss: application queries database, stores result in cache with a TTL (Time-To-Live), and returns result.
- **Pros**: Only requested data is cached (memory efficient); cache failure does not halt application (falls back to DB).
- **Cons**: Three network trips on cache miss; initial request incurs latency penalty; potential stale data if DB is updated without invalidating cache.

### 1.2 Write-Through
- **Flow**: Application writes directly to the cache. The cache synchronously writes data to the primary database before acknowledging success to the client.
- **Pros**: Data in cache is never stale; guarantees immediate read consistency.
- **Cons**: High write latency (incurs two write hops); caches data that might never be read again (churn).

### 1.3 Write-Behind (Write-Back)
- **Flow**: Application writes to cache, which acknowledges immediately. Cache asynchronously batches and flushes writes to the backing database after a delay (e.g., every 5 seconds).
- **Pros**: Near-zero write latency; absorbs massive write spikes (e.g., video view counts, IoT telemetry, swipe logs).
- **Cons**: Severe risk of permanent data loss if cache node crashes before flushing dirty buffers to durable disk.

### 1.4 Refresh-Ahead
- **Flow**: Cache automatically reloads frequently accessed keys from database before their TTL expires.
- **Use Case**: Eliminates latency spikes on hot items (e.g., breaking news banner, homepage leaderboard).

---

## 2. Cache Eviction Policies

When cache memory fills up to `maxmemory`, eviction algorithms free memory:
1. **LRU (Least Recently Used)**: Discards keys that have not been read or written for the longest time. Standard general-purpose choice.
2. **LFU (Least Frequently Used)**: Tracks hit frequency counters; protects items with consistently high lifetime access even if briefly idle.
3. **FIFO (First In First Out)**: Evicts oldest stored item regardless of access frequency.
4. **Random**: Randomly drops keys to save tracking overhead.
5. **TTL-based (`volatile-lru` / `volatile-ttl`)**: Only evicts keys that have an explicit expiration timestamp set.

---

## 3. The Three Classic Cache Disasters and Solutions

### 3.1 Cache Penetration
- **Problem**: Malicious or buggy clients query millions of non-existent keys (e.g., `user_id = -999999`). Every query misses the cache and smashes the primary database.
- **Solution**:
  1. **Cache Null Values**: Store empty sentinel values with a short TTL (e.g., 60 seconds).
  2. **Bloom Filter**: Use a space-efficient probabilistic data structure at the API Gateway or Redis layer to reject definitely-non-existent keys before touching DB.

### 3.2 Cache Breakdown (Hotspot Invalidating)
- **Problem**: A super-hot key (e.g., viral product launch viewed by 50,000 req/sec) suddenly expires. Thousands of concurrent requests simultaneously miss the cache and overwhelm the database.
- **Solution**:
  1. **Mutex / Distributed Lock**: Only the first worker acquiring a Redis lock fetches from DB and populates cache; others wait and re-check cache.
  2. **Logical Expiration**: Key never expires physically in Redis; worker detects logical TTL is past and spawns background worker to refresh value.

### 3.3 Cache Avalanche
- **Problem**: Thousands of cached keys share the exact same TTL (e.g., 2 hours). At $t = 7200\text{s}$, all keys expire simultaneously, causing the entire database to crash.
- **Solution**: Add random jitter to all expiration times:
  $$\text{TTL}_{\text{effective}} = \text{TTL}_{\text{base}} + \text{random}(0, \Delta t)$$
