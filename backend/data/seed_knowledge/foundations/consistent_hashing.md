# Consistent Hashing and Virtual Nodes

## Problem Statement
In traditional modulo hashing (`node = hash(key) % N`), adding or removing a single node invalidates almost all cached keys (`(N - 1) / N` keys remapped). For large caching tiers, this causes a catastrophic cache stampede on the backing database.

## Mechanism
Consistent hashing maps both keys and server nodes to a circular hash ring (typically $0$ to $2^{32} - 1$):
1. **Hash the Servers**: Compute `hash(node_ip)` and place the server on the ring.
2. **Hash the Keys**: Compute `hash(object_key)` to locate a coordinate on the ring.
3. **Lookup Route**: Walk clockwise from the key's position until encountering the first server node.

When a node is added or removed, only $K/N$ keys need migration on average, where $K$ is the total key count and $N$ is the number of servers.

## Virtual Nodes (Vnodes)
A naive ring with few physical servers suffers from severe hot spots due to non-uniform key distribution.
- **Solution**: Assign each physical node multiple virtual coordinates (e.g. 100–256 virtual nodes per machine).
- **Benefits**:
  - Balanced load distribution across heterogeneous hardware (allocate more vnodes to larger servers).
  - Smooth rebalancing during node failure or cluster expansion.

## Production Implementations
- **Amazon DynamoDB & Apache Cassandra**: Token rings with consistent hashing for partition placement.
- **Discord & Akamai**: Load balancer consistent hashing for WebSocket session routing and CDN edge caching.
