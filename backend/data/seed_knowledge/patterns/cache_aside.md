# Cache-Aside, Write-Through, and Write-Behind Patterns

## Cache-Aside (Lazy Loading)
In Cache-Aside, the application code orchestrates interaction directly between the cache and the backing database:
1. Application queries the cache for key $K$.
2. **Cache Hit**: Value is returned immediately.
3. **Cache Miss**: Application queries the primary database, populates the cache with the retrieved value, and returns the result.
4. **Data Mutation**: Application updates the database first, then actively invalidates (deletes) the key from the cache.

### Why Delete Instead of Update on Write?
Updating the cache on write creates subtle race conditions when two concurrent writes occur. Deleting the cache key forces the next read to fetch the latest committed value from the database, preventing stale cached states.

## Write-Through Caching
The application writes exclusively to the cache system. The cache layer synchronously persists the update into the database before acknowledging success to the caller.
- *Advantage*: High read and write consistency; cache is always primed.
- *Disadvantage*: Higher write latency because every write does a round trip to both cache and disk.

## Write-Behind (Write-Back) Caching
The application writes to the cache, which acknowledges immediately. The cache queues updates and asynchronously batches writes into the database in the background.
- *Advantage*: Ultra-fast write throughput, database write-load smoothing, and reduced IOPS.
- *Disadvantage*: High risk of permanent data loss if the cache node crashes before flushing queued writes to durable storage.

## Mitigation of Common Cache Hazards
- **Cache Stampede (Thundering Herd)**: Occurs when a popular key expires and thousands of concurrent requests miss and query the database simultaneously. Fix with mutex locks (single-flight) or probabilistic early expiration (XFetch algorithm).
- **Cache Penetration**: Queries for non-existent keys bypass the cache and hit the database every time. Fix with Bloom filters or caching null objects with short TTLs.
- **Cache Avalanche**: Large number of keys expire at the exact same second. Fix by adding jitter (randomized offset) to TTLs.
