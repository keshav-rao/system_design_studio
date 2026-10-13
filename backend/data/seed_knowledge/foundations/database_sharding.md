# Database Sharding and Horizontal Partitioning

## Motivation
When a single database instance exhausts vertical scaling limits (CPU bottlenecks, IOPS saturation, storage volume limits > 16 TB), horizontal sharding distributes distinct rows across multiple independent database nodes.

## Partitioning Strategies
1. **Range-Based Sharding**:
   - Routes rows based on key ranges (e.g., User IDs 1–1M on Node 1, 1M–2M on Node 2).
   - *Risk*: Severe write hot spots if monotonically increasing IDs are used.
2. **Hash-Based Sharding**:
   - Computes `hash(shard_key) % num_shards`.
   - *Benefit*: Uniform distribution of writes and reads across all shards.
   - *Challenge*: Re-sharding when adding new nodes requires cluster-wide data redistribution unless paired with consistent hashing.
3. **Directory / Lookup-Based Sharding**:
   - A central lookup service tracks which shard holds each entity ID.
   - *Benefit*: Maximum flexibility and easy split of huge tenants.
   - *Risk*: Lookup service becomes a single point of failure and read latency bottleneck.

## Critical Challenges & Anti-Patterns
- **Cross-Shard Joins**: Joining tables across distinct physical nodes requires distributed query coordination or two-phase commits, causing severe latency degradation.
- **Celebrity / Hot Key Problem**: A high-profile user with millions of followers will overwhelm a single shard. Mitigate by salt-hashing or caching fan-out data.
- **Distributed Transactions**: Two-Phase Commit (2PC) blocks during coordinator partition. Avoid cross-shard transactions whenever possible using saga patterns.
