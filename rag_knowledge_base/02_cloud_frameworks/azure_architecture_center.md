```json
{
  "topic": "cloud_architecture_framework",
  "component": "azure_ecosystem",
  "decision_type": "technology_selection",
  "content_type": "official_documentation",
  "cloud_provider": "azure",
  "source_url": "https://learn.microsoft.com/en-us/azure/well-architected/",
  "version": "2024-2026",
  "licence": "Open-Documentation",
  "last_verified": "2026-10-14"
}
```

# Microsoft Azure Well-Architected Framework: Service Patterns & Cross-Cloud Comparison

The Azure Well-Architected Framework guides architects in designing robust, scalable, and secure cloud applications on Microsoft Azure.

## 1. Core Architectural Patterns in Azure

### 1.1 Azure Front Door vs. Application Gateway
- **Azure Front Door**: Global Layer 7 reverse proxy, Anycast CDN, and WAF operating at the edge. Terminate SSL/TLS closest to the user and accelerate traffic to backend origin pools across multiple Azure regions.
- **Application Gateway**: Regional Layer 7 load balancer with integrated WAF, URL path-based routing, and SSL offloading inside a virtual network (VNet).

### 1.2 Azure Cosmos DB: The Five Consistency Levels
Unlike systems offering only a binary choice between Strong and Eventual consistency, Azure Cosmos DB provides five well-defined consistency levels:
1. **Strong**: Linearizability; guarantees reads always return the latest committed write. Highest latency, lowest availability (confined to single-region or limited replication distance).
2. **Bounded Staleness**: Reads lag behind writes by at most $K$ versions or $T$ time intervals (e.g., 5 seconds). Ideal for near-real-time dashboards.
3. **Session**: Default level. Guarantees read-your-own-writes and monotonic reads within a single user session token.
4. **Consistent Prefix**: Guarantees updates are never seen out of order, though reads may be stale.
5. **Eventual**: Out-of-order, stale reads possible during convergence. Lowest latency, highest write throughput.

---

## 2. Cross-Cloud Equivalence Matrix

When designing cloud-agnostic architectures or mapping multi-cloud solutions, use this reference table:

| Architectural Component | AWS | Google Cloud (GCP) | Microsoft Azure | Open Source Native |
| :--- | :--- | :--- | :--- | :--- |
| **Edge CDN & Anycast LB** | CloudFront + Route 53 | Cloud CDN + Global HTTPS LB | Azure Front Door | Cloudflare / Fastly |
| **Regional L7 Load Balancer** | Application Load Balancer (ALB) | Regional External HTTPS LB | Application Gateway | Envoy Proxy / NGINX |
| **Layer 4 Network LB** | Network Load Balancer (NLB) | Network Load Balancer | Azure Load Balancer | HAProxy / IPVS |
| **Container Orchestration** | EKS (Elastic Kubernetes) | GKE (Google Kubernetes Engine)| AKS (Azure Kubernetes Service) | Kubernetes (k8s) |
| **Serverless Containers** | AWS Fargate | Cloud Run | Azure Container Apps | Knative |
| **Relational DB** | RDS / Aurora PostgreSQL | Cloud SQL / AlloyDB | Azure Database for PostgreSQL | PostgreSQL |
| **Distributed Multi-Model** | DynamoDB | Spanner / Firestore | Cosmos DB | Cassandra / ScyllaDB |
| **In-Memory Cache** | ElastiCache Redis | Memorystore for Redis | Azure Cache for Redis | Redis / Dragonfly |
| **Event Streaming** | Amazon MSK | Confluent Cloud / Pub/Sub | Azure Event Hubs | Apache Kafka |
| **Message Queue** | Amazon SQS | Cloud Pub/Sub | Azure Service Bus | RabbitMQ |
| **Object Storage** | Amazon S3 | Cloud Storage (GCS) | Azure Blob Storage | MinIO |
| **Secrets Management** | AWS Secrets Manager | Secret Manager | Azure Key Vault | HashiCorp Vault |
