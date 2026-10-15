```json
{
  "topic": "reference_architecture",
  "component": "dating_swipe_platform",
  "decision_type": "reference_architecture",
  "content_type": "reference_architecture",
  "cloud_provider": "provider_neutral",
  "source_url": "https://netflixtechblog.com/ | https://eng.lyft.com/",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# Reference Architecture: High-Scale Dating Application (Tinder-Like System)

## 1. System Requirements & Functional Scope

### Functional Requirements
1. **User Profiles & Media**: Registration, photo gallery uploads, bio, preferences (gender, age range, distance radius).
2. **Recommendation Deck**: Generate and serve a continuous deck of potential candidate profiles within geographic proximity.
3. **Swipe Engine**: Record Right Swipe (Like), Left Swipe (Pass), and Super Like.
4. **Instant Match Detection**: Immediately detect when two users have mutually liked each other and notify both parties in real-time.
5. **Real-time 1-on-1 Chat**: Low-latency messaging between matched pairs.

### Non-Functional Requirements
- **Scale**: 10 million Daily Active Users (DAU), 1 billion swipes/day (~11,500 swipes/sec average, 50,000 swipes/sec peak).
- **Latency**:
  - Swipe acknowledgement: < 50ms.
  - Mutual match detection & notification: < 100ms.
  - Profile recommendation deck retrieval: < 150ms.
  - Chat message delivery: < 200ms end-to-end.
- **Availability**: 99.99% uptime.
- **Consistency**:
  - Mutual likes / Matches: Strong consistency (no duplicate match records, no missed matches).
  - Profile bio / photo updates: Eventual consistency (acceptable if profile updates propagate within a few seconds).
  - Transient location updates: Eventual consistency with high-frequency in-memory overwrites.

---

## 2. High-Level Architecture Diagram

```
                              [Mobile Clients (iOS / Android)]
                                       │
                    ┌──────────────────┴──────────────────┐
                    ▼                                     ▼
        [Cloudflare / CloudFront CDN]            [AWS Route 53 (Latency DNS)]
         (Photo Delivery & WebP Caching)                   │
                    │                                     ▼
                    │                       [Layer 4 Network LB (AWS NLB)]
                    │                                     │
                    │                       [Layer 7 Application LB (ALB)]
                    │                                     │
       ┌────────────┼─────────────────────────────────────┼────────────────────────────┐
       ▼            ▼                                     ▼                            ▼
[CDN Edge] [Presigned S3 Bucket]              [API Gateway / Envoy]         [WebSocket Gateway Fleet]
 (Photos)   (Raw Uploads)                                 │                    (Persistent Connections)
                                              ┌───────────┴──────────┐                 │
                                              ▼                      ▼                 ▼
                                       [Swipe Service]       [Profile Service]   [Chat Service]
                                              │                      │                 │
                                ┌─────────────┼──────────────┐       │                 │
                                ▼             ▼              ▼       ▼                 ▼
                        [Redis Cluster] [Kafka Cluster] [PostgreSQL] [PostgreSQL] [Cassandra / ScyllaDB]
                         (Sets, Geo,     (Swipe Events,  (Auth, KYC,  (Replicas)   (Message History)
                          Deck Cache)     Match Pipeline) Billing)
```

---

## 3. Deep-Dive Answers to Core Architectural Decisions

### 3.1 Why should this application use Redis, and when would it be unnecessary?
- **Why it MUST use Redis at Scale**:
  1. *Sub-millisecond Mutual Match Detection*: Uses Redis Sets (`SADD likes:user_A user_B`). When User B swipes on User A, an atomic check `SISMEMBER likes:user_B user_A` resolves in 0.2ms. If verified, the match is registered immediately.
  2. *Geospatial Proximity Filtering*: In-memory Geohash indexing via Redis Geospatial (`GEOSEARCH`) quickly identifies candidates within an $R$ kilometer radius.
  3. *Recommendation Deck Queue*: Precomputed candidate lists are pushed to Redis Lists (`LPUSH user:deck candidate_id`). Client fetches next 20 profiles via `RPOP` in < 2ms without querying disk databases.
  4. *Distributed Rate Limiting*: Prevents automated bot swiping using a Redis sliding window counter (`ZADD` / `ZREMRANGEBYSCORE`).
- **When Redis is UNNECESSARY**:
  - *At Early Stage (< 10,000 DAU)*: A single PostgreSQL instance with `PostGIS` extension and a `likes` table with a composite index `(user_id, target_id)` can easily handle 500–1,000 swipes/second. Introducing Redis introduces dual-write cache invalidation bugs and memory management overhead prematurely.
  - *For Long-term Chat History*: Inactive chat logs should be stored on NVMe SSDs (Cassandra/DynamoDB) rather than expensive RAM.

### 3.2 Should it use Kafka, RabbitMQ, or a simpler queue?
- **Swipe Ingestion & ML Pipeline**: **Apache Kafka** is mandatory.
  - A peak rate of 50,000 swipes/sec produces heavy event streams.
  - Kafka's partitioned log allows multiple decoupled consumer groups to read the same stream without message duplication overhead:
    - *Consumer Group 1 (Match Worker)*: Processes match celebrations.
    - *Consumer Group 2 (Recommendation Engine)*: Feeds collaborative filtering models and Elo rating updates.
    - *Consumer Group 3 (Anti-Abuse / Fraud)*: Detects spammers and bots.
- **Push Notifications & Asynchronous Tasks**: **RabbitMQ or AWS SQS**.
  - Sending push notifications via Apple APNs / Google FCM requires per-message retries, exponential backoffs, and dead-letter queues (DLQ), which RabbitMQ/SQS handles natively.

### 3.3 Which database suits its access patterns and consistency requirements?
- **User Accounts, Auth, Subscriptions (PostgreSQL)**:
  - Strong ACID guarantees, unique constraints (phone/email), relational mapping of payment invoices, and referential integrity.
- **Chat Messages (Apache Cassandra or ScyllaDB)**:
  - Access pattern: 100% write-heavy, append-only, partitioned strictly by `conversation_id`, sorted chronologically by `message_id`.
  - Cassandra's LSM-Tree storage engine writes sequentially to CommitLog and Memtable in < 2ms, providing linear write scalability.
- **Media Metadata & Photos (Amazon S3 + CloudFront CDN)**:
  - User photos are uploaded directly to S3 via presigned URLs and distributed globally through CDN edge nodes in WebP/AVIF formats.

### 3.4 What load balancer, replication strategy, and scaling approach should it use?
- **Load Balancing**:
  - Dual-tier: AWS Network Load Balancer (NLB) at Layer 4 for ultra-high throughput TCP connection termination, routing to an Application Load Balancer (ALB) / Envoy Gateway at Layer 7 for path routing and SSL offloading.
  - For WebSockets: ALB uses sticky cookie affinity and Least Connections routing to evenly distribute long-lived socket sessions across the gateway fleet.
- **Replication Strategy**:
  - PostgreSQL: Primary write leader with synchronous replication to a standby in AZ-2 (zero RPO failover) and 3 asynchronous read replicas in AZ-1, AZ-2, AZ-3.
  - Redis: Redis Cluster with 1 master and 1 replica per shard across 3 availability zones.
- **Scaling Approach**:
  - Horizontal scaling of stateless API containers on Kubernetes (EKS / GKE) using Horizontal Pod Autoscaler (HPA) triggered by CPU utilization and request count per target.

---

## 4. Deployment, Testing, and Pricing Strategy

### 4.1 Deployment Architecture
- Deployed on **Kubernetes (Amazon EKS / GKE)** using GitOps (ArgoCD).
- Blue/Green deployments for zero-downtime releases.
- Multi-AZ across 3 Availability Zones within the primary region, with cross-region cold disaster recovery in a secondary region.

### 4.2 Testing & Workload Verification (k6 / Locust)
- **k6 Load Script**: Simulates 10,000 virtual users (VUs) executing a realistic user journey:
  1. Login & fetch profile deck (`GET /deck` -> target < 150ms p95).
  2. Perform 10 swipes with 80% Left, 20% Right (`POST /swipe` -> target < 50ms p95).
  3. Mutual match celebration triggered on right swipe.
  4. Send 3 chat messages over WebSocket (`ws_send` -> target < 100ms p95).
- Chaos Engineering: Test network partition between Redis shards and DB primary failover using Chaos Mesh.

### 4.3 Estimated Monthly Cost Model (at 1M DAU Scale)

| Component | Specification / Sizing | Quantity | Monthly Cost (USD) |
| :--- | :--- | :--- | :--- |
| **Compute (EKS/EC2)** | `m6g.xlarge` (4 vCPU, 16 GB RAM) Graviton | 16 instances | ~$1,580 |
| **Relational DB (PostgreSQL)** | `db.r6g.2xlarge` Multi-AZ (8 vCPU, 64 GB RAM) | 1 Primary + 2 Replicas | ~$1,850 |
| **Cache (Redis Cluster)** | `cache.r6g.xlarge` (4 vCPU, 26 GB RAM) | 6 nodes (3 shards) | ~$1,320 |
| **Event Streaming (MSK)** | `kafka.m5.large` (2 vCPU, 8 GB RAM) | 3 brokers | ~$480 |
| **Chat DB (Cassandra/DynamoDB)** | DynamoDB On-Demand (~50M writes/day) | Pay-per-request | ~$650 |
| **Object Storage & CDN** | S3 (50 TB images) + CloudFront (200 TB egress) | Global CDN | ~$2,900 |
| **Networking & Load Balancers** | 2 ALB + 1 NLB + NAT Gateway data processing | High traffic | ~$1,100 |
| **Total Estimated Infrastructure Cost** | | | **~$9,880 / month** |
*(Unit cost per active user: ~$0.0098 / DAU / month).*
