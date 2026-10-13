# Redis Topologies, Hash Slots, and Eviction Policies

## Deployment Topologies
1. **Standalone**: Single process. Simple, zero cluster overhead, but a single point of failure (SPOF) with zero high availability.
2. **Sentinel (High Availability)**:
   - Primary-replica topology monitored by at least 3 Redis Sentinel daemon processes.
   - Sentinel achieves quorum to automatically failover and promote a replica if the primary becomes unreachable.
   - Capacity is limited to the RAM of a single primary instance (typically $< 128\text{ GB}$).
3. **Redis Cluster (Sharded Horizontal Scaling)**:
   - Distributes key storage across multiple masters without a proxy.
   - Space is partitioned into $16,384$ fixed hash slots:
     $\text{slot} = \text{CRC16}(\text{key}) \pmod{16384}$.
   - **Hash Tags**: Forcing related keys into the identical hash slot using `{...}` syntax (e.g. `{user_123}.profile` and `{user_123}.cart`) allows atomic multi-key operations (transactions, pipelines, Lua scripts) across cluster nodes.

## Memory Management and Eviction Policies
When `maxmemory` threshold is reached:
- `allkeys-lru`: Evicts least recently used keys regardless of TTL. Recommended for general caching tiers.
- `volatile-lru`: Evicts LRU keys among those configured with an expiration TTL.
- `allkeys-lfu`: Evicts least frequently used keys, ideal when hot items should stay cached even if not queried for a brief moment.
- `noeviction`: Returns errors on write operations when memory is full. Mandatory when Redis is used as a session store or broker rather than an expendable cache.
