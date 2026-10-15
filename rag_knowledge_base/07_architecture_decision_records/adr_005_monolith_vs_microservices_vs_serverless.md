```json
{
  "topic": "architecture_decision_record",
  "component": "service_decomposition",
  "decision_type": "technology_selection",
  "content_type": "adr",
  "cloud_provider": "provider_neutral",
  "source_url": "https://martinfowler.com/bliki/ArchitectureDecisionRecord.html",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# ADR 005: Service Decomposition: Modular Monolith vs. Microservices vs. Serverless

## Status
**Accepted**

## Context
A major architectural choice in software design is determining service boundaries and deployment granularity. Teams frequently oscillate between monolithic architectures, fine-grained microservices, and serverless functions (AWS Lambda / Google Cloud Functions). 

Premature microservice decomposition introduces distributed transaction complexity, network serialization latency, and observability headaches. Conversely, an unwieldy monolith limits deployment velocity and independent autoscaling.

## Decision
We adopt a **Stage-Gated Architecture Evolution**:
1. **Phase 1 (MVP to Early Scale < 100k DAU)**: **Modular Monolith**.
   - Single deployable container codebase structured internally with strict domain boundaries (e.g., Auth, Profile, Matching, Billing as isolated modules with clear interfaces).
   - Single shared PostgreSQL database with schema-level domain separation.
2. **Phase 2 (High Concurrency / Scale > 100k DAU)**: **Domain-Driven Microservices**.
   - Extract only high-load, distinct scalability domains into independent services:
     - *Swipe Ingestion Service*: High write QPS, CPU-intensive.
     - *WebSocket Gateway Fleet*: Long-lived stateful TCP connections.
     - *Core Business Monolith / Services*: Low-frequency CRUD, auth, and billing.
3. **Serverless (Cloud Functions / Lambda)**:
   - Reserved strictly for sporadic, event-driven, or asynchronous batch tasks (e.g., image thumbnail generation on S3 upload, daily cron billing reports).

## Alternatives Considered
1. **Microservices from Day 1**:
   - *Rejected*: Incurs massive operational tax (distributed tracing, API gateways, independent CI/CD pipelines, network latency between services) before product-market fit.
2. **Pure Serverless (100% Lambda)**:
   - *Rejected for core API*: Suffers cold-start latency penalties (> 500ms), database connection exhaustion under concurrency spikes (without expensive RDS Proxy), and high cost at steady high throughput.

## Consequences & Trade-offs
### Positive Consequences
- Rapid development velocity during early stages.
- Straightforward migration path: internal modules can be detached into standalone microservices cleanly along predefined interface boundaries when required.
- Cost-efficient resource utilization without serverless cold starts.

### Negative Consequences & Risks
- Requires strict engineering discipline to prevent internal module code coupling within the monolith before extraction.
