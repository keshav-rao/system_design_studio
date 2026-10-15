```json
{
  "topic": "architecture_decision_record",
  "component": "in_memory_cache",
  "decision_type": "technology_selection",
  "content_type": "adr",
  "cloud_provider": "provider_neutral",
  "source_url": "https://martinfowler.com/bliki/ArchitectureDecisionRecord.html",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# ADR 003: Redis In-Memory Data Store & Distributed Caching Architecture

## Status
**Accepted**

## Context
High-traffic features (user authentication sessions, profile recommendation deck queues, mutual swipe checking, API rate limiting, and geospatial radius lookups) require response latencies under 5 milliseconds. Primary relational databases cannot sustain tens of thousands of read/write queries per second without connection exhaustion and high latency variance.

## Decision
Adopt **Redis (version 7.2+)** as the primary in-memory cache and volatile state engine, utilizing its specialized native data structures (Sets for mutual like verification, Geospatial indices for proximity search, Hashes for user presence, and Sorted Sets for rate limiting).

## Alternatives Considered
1. **Memcached**:
   - *Rejected*: While Memcached supports multi-threaded scaling for raw key-value caching, it completely lacks data structures (Sets, Hashes, Sorted Sets), persistence options (RDB/AOF), and native replication. Implementing mutual swipe matching on Memcached would require pulling large byte arrays into application memory, destroying performance.
2. **Local In-Process Memory Cache (e.g., Guava, LRU cache in Node/Go)**:
   - *Rejected for multi-node deployments*: In-process caches lead to severe cache inconsistency across autoscaled pods and memory bloat within container limits. Local caching is reserved only for near-static configuration dictionaries.

## Consequences & Trade-offs
### Positive Consequences
- Sub-millisecond reads and writes ($< 1\text{ms}$).
- Atomic operations (`SISMEMBER`, `ZADD`, `HINCRBY`) eliminate distributed race conditions without explicit application-level locking.
- Drastically reduces load on primary relational database (up to 80–90% query offloading).

### Negative Consequences & Risks
- **Cache Invalidation Complexity**: Applications must handle the Cache-Aside lifecycle carefully to avoid serving stale data.
- **Volatile Memory Cost**: RAM is expensive; cache entries must always carry explicit TTLs or use `allkeys-lru` eviction to avoid Out-Of-Memory (OOM) fatal crashes.
