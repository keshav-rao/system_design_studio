```json
{
  "topic": "cloud_architecture_framework",
  "component": "aws_ecosystem",
  "decision_type": "technology_selection",
  "content_type": "official_documentation",
  "cloud_provider": "aws",
  "source_url": "https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html",
  "version": "2024-2026",
  "licence": "Open-Documentation",
  "last_verified": "2026-10-14"
}
```

# AWS Well-Architected Framework: Core Pillars and Architectural Heuristics

The AWS Well-Architected Framework defines six foundational pillars for building cloud-native, defensible architectures.

## 1. The Six Pillars of Architecture

### Pillar 1: Reliability
- **Core Principle**: Automatically recover from failure, test recovery procedures in production, and scale horizontally to increase overall workload availability.
- **Key AWS Services**: Multi-AZ deployments, Auto Scaling Groups (ASG), Route 53 DNS failover, AWS Backup, Amazon S3 cross-region replication (CRR).
- **Architectural Rules**:
  - Never run production databases in Single-AZ mode (Multi-AZ RDS / Aurora provides automated failover in < 30 seconds).
  - Decouple components using Amazon SQS queues to prevent backpressure collapses.

### Pillar 2: Performance Efficiency
- **Core Principle**: Democratize advanced technologies, go global in minutes, use serverless architectures, and experiment frequently.
- **Key AWS Services**: AWS Lambda, Amazon CloudFront (CDN), ElastiCache (Redis/Memcached), Amazon DynamoDB, AWS Global Accelerator.
- **Architectural Rules**:
  - Offload static assets and cacheable GET queries to CloudFront edge nodes (reduces origin server load by 70–95%).
  - Use read replicas for PostgreSQL/MySQL when read-to-write ratios exceed 4:1.

### Pillar 3: Cost Optimization
- **Core Principle**: Practice Cloud Financial Management (FinOps), measure overall efficiency, adopt consumption models, and avoid spending money on undifferentiated heavy lifting.
- **Key AWS Services**: AWS Cost Explorer, Savings Plans, Reserved Instances (RI), S3 Intelligent-Tiering, Graviton processors (arm64).
- **Architectural Rules**:
  - Migrate x86 EC2 / RDS instances to AWS Graviton (arm64) for ~20% lower cost and up to 40% better price-performance.
  - Apply S3 Lifecycle policies (transition objects to S3 Standard-IA at 30 days, Glacier at 90 days).

### Pillar 4: Security
- **Core Principle**: Apply security at all layers, implement least privilege access, automate security best practices, and protect data in transit and at rest.
- **Key AWS Services**: AWS IAM, AWS KMS, AWS WAF, Amazon GuardDuty, AWS Secrets Manager.
- **Architectural Rules**:
  - Never store database passwords or API keys in code or plaintext environment files; retrieve via IAM Role and Secrets Manager.
  - Enforce TLS 1.3 in transit and AES-256 (KMS CMK) at rest across all S3 buckets and EBS volumes.

### Pillar 5: Operational Excellence
- **Core Principle**: Perform operations as code, make frequent small reversible changes, anticipate failure, and learn from all operational events.
- **Key AWS Services**: AWS CloudFormation / Terraform, Amazon CloudWatch, AWS X-Ray (distributed tracing).
- **Architectural Rules**:
  - Instrument every microservice with structured JSON logs and distributed trace IDs (`x-amzn-trace-id`).

### Pillar 6: Sustainability
- **Core Principle**: Minimize environmental impact through efficient resource utilization, modern processor architectures, and aggressive scale-to-zero autoscaling.

---

## 2. AWS Service Mapping Cheat Sheet
| Category | Recommended AWS Service | Equivalent Open Source / Generic |
| :--- | :--- | :--- |
| **Object Storage** | Amazon S3 | MinIO / Ceph |
| **Relational Database** | Amazon Aurora PostgreSQL | Vanilla PostgreSQL + Patroni |
| **NoSQL Key-Value** | Amazon DynamoDB | Apache Cassandra / ScyllaDB |
| **In-Memory Cache** | Amazon ElastiCache for Redis | Standalone Redis Cluster |
| **Message Broker** | Amazon SQS / Amazon SNS | RabbitMQ |
| **Event Streaming** | Amazon Managed Streaming for Apache Kafka (MSK) | Apache Kafka |
| **API Gateway / L7 LB** | Application Load Balancer (ALB) / API Gateway | Envoy / NGINX / Traefik |
