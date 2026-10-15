```json
{
  "topic": "capacity_tier_sizing",
  "component": "infrastructure",
  "decision_type": "capacity_planning",
  "content_type": "benchmark",
  "cloud_provider": "provider_neutral",
  "source_url": "https://docs.aws.amazon.com/wellarchitected/latest/performance-efficiency-pillar/",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# Workload-to-Capacity Sizing Matrix: 1 to 1,000,000 Active Users

This matrix specifies how system components scale across discrete traffic tiers from local prototype up to massive production scale.

## 1. Capacity Tiers Overview

| User Scale | Peak QPS | Recommended Architecture Topology | Monthly Cost (Approx) |
| :--- | :--- | :--- | :--- |
| **Tier 1: Prototype (1 – 100 Users)** | 1 – 10 QPS | Single Monolith VM (Docker Compose) or Serverless (Cloud Run / Lambda). Shared SQLite or small Postgres container. Free-tier eligible. | $0 – $25 / month |
| **Tier 2: Early Traction (1k – 10k Users)**| 50 – 500 QPS | Scaled Monolith behind Application Load Balancer. Managed PostgreSQL (Single-AZ, 2 vCPU, 8 GB RAM) + Redis standalone instance for sessions/caching. | $150 – $400 / month |
| **Tier 3: Growth Stage (100k Users)** | 2,500 – 5,000 QPS | Microservices on Kubernetes (EKS / GKE). Multi-AZ PostgreSQL (4 vCPU, 16 GB RAM) with 2 Read Replicas + Redis Cluster (3 shards) + Kafka / RabbitMQ broker + CloudFront CDN. | $1,500 – $3,500 / month |
| **Tier 4: Enterprise Scale (1M+ Users)** | 25,000 – 50,000+ QPS | Globally distributed multi-region Kubernetes clusters. Sharded database / NoSQL (Cassandra/DynamoDB) + Multi-Broker Kafka cluster + Multi-node Redis Cluster + Anycast Edge CDN + dedicated PgBouncer fleets. | $8,000 – $25,000+ / month |

---

## 2. Resource Sizing by Component Across Tiers

### 2.1 Compute Tier (App / API Servers)
- **100 Users**: 1 container (`0.5 vCPU`, `512 MB RAM`).
- **1,000 Users**: 2 containers (`1 vCPU`, `1 GB RAM`) behind ALB for high availability.
- **10,000 Users**: 4–6 containers (`2 vCPU`, `4 GB RAM`) with CPU-based autoscaling (HPA).
- **100,000 Users**: 12–20 containers (`2 vCPU`, `4 GB RAM`) spread across 3 Availability Zones.
- **1,000,000 Users**: 50–100+ autoscaled worker pods with KEDA queue-based and concurrency-based autoscaling.

### 2.2 Relational Database Tier (PostgreSQL)
- **100 Users**: Shared host / `db.t3.micro` (1 vCPU, 1 GB RAM, 20 GB gp3).
- **1,000 Users**: `db.t3.small` (2 vCPU, 2 GB RAM, 50 GB gp3).
- **10,000 Users**: `db.m6g.large` (2 vCPU, 8 GB RAM, 100 GB gp3 with 3,000 IOPS).
- **100,000 Users**: `db.r6g.xlarge` Multi-AZ (4 vCPU, 32 GB RAM) + 2 Read Replicas + PgBouncer connection pooling.
- **1,000,000 Users**: `db.r6g.4xlarge` Multi-AZ (16 vCPU, 128 GB RAM) + 4 Read Replicas + table partitioning (sharding by user ID or tenant).

### 2.3 Caching Tier (Redis)
- **100 – 1,000 Users**: In-memory cache unnecessary or single local 512MB container.
- **10,000 Users**: `cache.t4g.medium` (2 vCPU, 3.09 GB RAM).
- **100,000 Users**: `cache.r6g.large` (2 vCPU, 13 GB RAM, Primary + Replica with Sentinel failover).
- **1,000,000 Users**: Redis Cluster with 6–12 shards (`cache.r6g.xlarge`, 26 GB RAM each = 150+ GB cluster RAM).
