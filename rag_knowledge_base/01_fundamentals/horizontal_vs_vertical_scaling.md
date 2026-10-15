```json
{
  "topic": "scaling_strategies",
  "component": "compute_and_storage",
  "decision_type": "capacity_planning",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# Horizontal vs. Vertical Scaling: Architectural Trade-Offs

## 1. Core Definitions
- **Vertical Scaling (Scale-Up)**: Increasing the capacity of an existing individual machine by adding more CPU cores, RAM, high-speed NVMe storage, or network bandwidth.
- **Horizontal Scaling (Scale-Out)**: Adding more independent commodity machine instances into a pool and distributing requests across them via load balancers, reverse proxies, or distributed hashing.

---

## 2. Detailed Comparison Matrix

| Dimension | Vertical Scaling (Scale-Up) | Horizontal Scaling (Scale-Out) |
| :--- | :--- | :--- |
| **Hardware Ceiling** | Hard ceiling: Max AWS EC2 instance (e.g., `u-24tb1.112xlarge` = 448 vCPUs, 24 TB RAM) | Theoretically near-infinite by adding thousands of smaller nodes |
| **Cost Curve** | Exponential: High-end enterprise hardware and mammoth cloud instances have steep non-linear cost multipliers | Linear: Small-to-medium spot/on-demand instances scale predictably with demand |
| **Application Complexity** | Minimal: Code remains monolithic; no network partitions, distributed locks, or RPC serialization | Significant: Requires stateless application servers, distributed caches, session affinity, or JWTs |
| **Downtime / Upgrades** | Often requires planned maintenance downtime or complex active-passive failover | Zero-downtime rolling deployments, blue/green updates, canary releases |
| **Fault Tolerance & SPOF** | High risk: The single host remains a Single Point of Failure (SPOF) | High resilience: Individual node failure simply shifts traffic to healthy peers |
| **Data Consistency** | Simple ACID transactions locally in-memory or on local NVMe disk | Requires distributed transactions (2PC/Sagas), Paxos/Raft consensus, or eventual consistency |

---

## 3. Decision Heuristics for the Engineering Architect

### When to Scale Up (Vertical)
1. **Early Stage / MVP (< 10,000 DAU)**: Fast time-to-market. A single $80/mo Postgres instance can easily handle 5,000 queries/sec with proper indexes and connection pooling.
2. **Relational Database Primary**: Scaling the write leader of PostgreSQL or MySQL vertically to 32–64 vCPU and 256GB RAM is 10x cheaper in engineering hours than sharding across multiple clusters.
3. **Complex In-Memory Graph Algorithms**: Fraud detection or route optimization graph traversal that cannot easily tolerate network latency hops across cluster nodes.

### When to Scale Out (Horizontal)
1. **Stateless Web/API Tier**: REST / GraphQL / gRPC gateways must always scale horizontally behind Layer 7 Application Load Balancers.
2. **Unpredictable Traffic Spikes**: E-commerce Black Friday or viral dating app launches where auto-scaling groups can spin up 100 extra containers in seconds.
3. **Global Multi-Region Latency**: Serving users in Tokyo, Frankfurt, and Virginia with sub-50ms local responses.
4. **Data Size > 3 TB**: When dataset exceeds physical SSD capacities or backups become prohibitively slow.
