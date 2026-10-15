```json
{
  "topic": "system_design_primer",
  "component": "distributed_systems",
  "decision_type": "pattern_design",
  "content_type": "reference_architecture",
  "cloud_provider": "provider_neutral",
  "source_url": "https://github.com/donnemartin/system-design-primer",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# System Design Primer: Core Architectural Building Blocks and Patterns

This reference summarizes the fundamental concepts, patterns, and trade-offs codified by the open-source System Design Primer.

## 1. High-Level Design (HLD) vs. Low-Level Design (LLD)

### High-Level Design (HLD)
- **Scope**: Macro-architecture of the distributed system.
- **Artifacts**: Service topology diagrams, network boundaries, data pipelines, load balancer placement, CDN edge distribution, database replication topologies, and async queue boundaries.
- **Key Questions**: How do independent microservices communicate? Where are the single points of failure? What is the failover strategy?

### Low-Level Design (LLD)
- **Scope**: Micro-level implementation within an individual service or process.
- **Artifacts**: Class and sequence diagrams, internal data structures (e.g., Trie for autocomplete, Min-Heap for priority task scheduling), concurrency locks, API schema definitions, and SQL table indexes.
- **Key Questions**: Which in-memory data structure minimizes cache line misses? How are database connections pooled?

---

## 2. Asynchronous Processing & Decoupling

### 2.1 Message Queues vs. Event Streams
- **Message Queues (e.g., RabbitMQ, SQS)**:
  - Point-to-point / worker queue pattern.
  - Messages are acknowledged and immediately deleted from the broker.
  - Excellent for task offloading (e.g., thumbnail generation, sending emails, generating billing PDFs).
- **Event Streams (e.g., Apache Kafka, Amazon Kinesis)**:
  - Append-only partitioned distributed commit log.
  - Messages are persisted according to retention policies (e.g., 7 days) and not deleted upon consumer read.
  - Multiple consumer groups read from arbitrary offsets independently.
  - Excellent for real-time analytics, event sourcing, user activity feeds, and data pipelines.

---

## 3. Communication Protocols

| Protocol | Transport | Latency | Overhead | Best Suited For |
| :--- | :--- | :--- | :--- | :--- |
| **HTTP/1.1** | TCP | Moderate | High (text headers, head-of-line blocking per connection) | Legacy public REST APIs |
| **HTTP/2** | TCP | Low | Medium (binary framing, multiplexing on single TCP connection) | Modern web browsers, frontend-to-backend APIs |
| **HTTP/3 (QUIC)**| UDP | Ultra-low | Low (0-RTT connection resumption, immune to TCP packet drop head-of-line blocking) | Mobile apps on lossy cellular networks, video streaming |
| **WebSockets** | TCP | Ultra-low | Minimal (2-byte frame header after initial HTTP handshake) | Full-duplex persistent connections: chat apps, live collaborative whiteboards, trading tickers |
| **gRPC** | HTTP/2 (Protobuf) | Ultra-low | Very low (compact binary serialization, code generation) | East-West internal microservice-to-microservice communication |
