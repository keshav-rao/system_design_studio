```json
{
  "topic": "cloud_pricing_models",
  "component": "pricing_engine",
  "decision_type": "cost_modeling",
  "content_type": "benchmark",
  "cloud_provider": "provider_neutral",
  "source_url": "https://calculator.aws/ | https://cloud.google.com/products/calculator",
  "version": "2024-2026",
  "licence": "Open-Documentation",
  "last_verified": "2026-10-14"
}
```

# Cloud Pricing Records and Deterministic Cost Calculation Models

## 1. Architectural Principle: Deterministic Pricing vs. RAG Inference

> **Critical Rule**: Never rely solely on an LLM or Vector RAG to hallucinate pricing math. 
> - **RAG Layer**: Retrieves architectural justification, service tier capabilities, and licensing limits.
> - **Deterministic Calculator**: Evaluates pricing formulas using concrete structured records (cost per vCPU hour, cost per GB storage, cost per million requests).

---

## 2. Standard Cloud Unit Pricing Reference Table (US-East Region, On-Demand)

| Service Category | Resource / Instance Tier | Specs (vCPU / RAM) | AWS Price (USD) | GCP Price (USD) | Azure Price (USD) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Compute (General)** | `m6g.large` / `e2-standard-2` / `D2as_v5` | 2 vCPU, 8 GB RAM | $0.077 / hr ($56/mo) | $0.067 / hr ($49/mo) | $0.076 / hr ($55/mo) |
| **Compute (App Server)**| `m6g.xlarge` / `e2-standard-4` / `D4as_v5` | 4 vCPU, 16 GB RAM | $0.154 / hr ($112/mo)| $0.134 / hr ($98/mo) | $0.152 / hr ($111/mo)|
| **Managed Postgres** | RDS `db.r6g.xlarge` (Multi-AZ) | 4 vCPU, 32 GB RAM | $0.52 / hr ($380/mo) | $0.48 / hr ($350/mo) | $0.50 / hr ($365/mo) |
| **Managed Redis** | ElastiCache `cache.r6g.large` | 2 vCPU, 13 GB RAM | $0.136 / hr ($99/mo) | $0.128 / hr ($93/mo) | $0.132 / hr ($96/mo) |
| **Managed Kafka** | AWS MSK `kafka.m5.large` | 2 vCPU, 8 GB RAM | $0.21 / hr / broker | Confluent Cloud tier | Event Hubs TU tier |
| **Object Storage** | S3 Standard / GCS Standard / Blob Hot | Per GB stored / month | $0.023 / GB | $0.020 / GB | $0.0208 / GB |
| **CDN Egress** | CloudFront / Cloud CDN / Azure CDN | First 10 TB egress | $0.085 / GB | $0.080 / GB | $0.087 / GB |
| **Internet Egress** | Direct from EC2/VM to public Internet | Per GB transferred | $0.090 / GB | $0.085 / GB | $0.087 / GB |
| **Application LB** | AWS ALB / GCP Regional HTTPS LB | Base hour + LCU/hr | $0.0225/hr + $0.008/LCU | $0.025/hr + rules | $0.025/hr + $0.008/capacity |

---

## 3. Deterministic Cost Estimation Formulas

### 3.1 Compute Cost Formula
$$\text{Cost}_{\text{compute}} = N_{\text{instances}} \times \text{Price}_{\text{hourly}} \times 730\text{ hours/month}$$

### 3.2 Relational Database Cost Formula
$$\text{Cost}_{\text{database}} = (\text{Price}_{\text{instance/hr}} \times 730) + (\text{Storage}_{\text{GB}} \times \text{Price}_{\text{storage/GB}}) + (\text{Provisioned IOPS} \times \text{Price}_{\text{IOPS}})$$

### 3.3 Storage & CDN Egress Cost Formula
$$\text{Cost}_{\text{media}} = (\text{Storage}_{\text{TB}} \times 1,000 \times \$0.023) + (\text{Egress}_{\text{TB}} \times 1,000 \times \text{CacheMissRatio} \times \$0.09) + (\text{Egress}_{\text{TB}} \times 1,000 \times \$0.085)$$

---

## 4. Cloud Free-Tier Quotas and Limitations (Do Not Infer Freely!)

1. **AWS Always-Free Limits**:
   - DynamoDB: 25 GB of storage, 25 provisioned Write Capacity Units (WCU), 25 Read Capacity Units (RCU).
   - AWS Lambda: 1,000,000 free requests/month and 3.2 million seconds of compute time.
   - CloudFront: 1 TB data transfer out per month, 10,000,000 HTTP/HTTPS requests.
2. **AWS 12-Month Free Tier**:
   - Amazon EC2: 750 hours/month of `t2.micro` or `t3.micro` (1 vCPU, 1 GB RAM).
   - Amazon RDS: 750 hours/month of `db.t3.micro` Single-AZ + 20 GB gp2 storage.
   - Amazon S3: 5 GB of standard storage, 20,000 GET requests, 2,000 PUT requests.
3. **Google Cloud Free Tier**:
   - 1 non-preemptible `e2-micro` VM instance per month (0.25 vCPU, 1 GB RAM) in selected US regions.
   - Cloud Run: 2 million requests/month, 360,000 GB-seconds memory.
   - BigQuery: 1 TB of queries/month and 10 GB storage.
