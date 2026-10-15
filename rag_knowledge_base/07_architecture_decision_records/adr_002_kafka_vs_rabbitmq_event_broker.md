```json
{
  "topic": "architecture_decision_record",
  "component": "message_broker",
  "decision_type": "technology_selection",
  "content_type": "adr",
  "cloud_provider": "provider_neutral",
  "source_url": "https://martinfowler.com/bliki/ArchitectureDecisionRecord.html",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# ADR 002: Message Queue vs. Distributed Event Streaming Broker Selection

## Status
**Accepted**

## Context
Applications require asynchronous decoupling between high-throughput client ingestion (e.g., user swipes, clickstreams, order submissions) and downstream consumers (notification pushers, machine learning recommendation pipelines, analytics, audit loggers). 

We must decide when to adopt **Apache Kafka** (distributed event log) versus **RabbitMQ / AWS SQS** (traditional message queue).

## Decision
1. Adopt **Apache Kafka (or AWS MSK / Confluent Cloud)** as the event backbone for:
   - High-throughput event streams (> 10,000 events/sec).
   - Multi-consumer broadcast scenarios where multiple independent services consume the exact same events at varying speeds.
   - Workloads requiring event replayability (e.g., ML retraining, debugging, event sourcing).
2. Adopt **RabbitMQ (or AWS SQS)** for:
   - Point-to-point task offloading (e.g., PDF generation, resizing photos, transcode tasks).
   - Complex message routing (wildcard topics, header-based exchange routing).
   - Tasks requiring individual message acknowledgements, dead-letter retries, and priority queues.

## Alternatives Considered
1. **Single Universal Broker for Everything**:
   - *Using Kafka for simple background tasks*: Overkill; Kafka lacks native individual task delayed execution and priority queues without complex application-level workarounds.
   - *Using RabbitMQ for massive analytics event streaming*: Fails under 100,000+ msgs/sec because message replication across multiple fanout queues exhausts RAM and CPU.
2. **Redis Pub/Sub or Redis Streams**:
   - Viable for lightweight prototypes, but Redis Pub/Sub has no durability (messages lost if subscriber is down) and Redis Streams consumes expensive RAM rather than cheap disk.

## Consequences & Trade-offs
### Positive Consequences
- Kafka provides near-zero consumer lag at high scale with immutable, re-playable log retention.
- RabbitMQ/SQS handles task retry storms with automatic exponential backoff and dead-letter queues.

### Negative Consequences & Risks
- Operating both Kafka and a message queue increases infrastructure and observability overhead.
- Requires team expertise in Kafka partition sizing, consumer group rebalancing, and KRaft consensus.
