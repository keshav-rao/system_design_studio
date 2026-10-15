```json
{
  "topic": "asynchronous_messaging_and_streaming",
  "component": "message_broker",
  "decision_type": "technology_selection",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://kafka.apache.org/documentation/",
  "version": "3.7+",
  "licence": "Apache-2.0",
  "last_verified": "2026-10-14"
}
```

# Event Streaming and Message Queues: Kafka vs. RabbitMQ vs. SQS / Redis Streams

## 1. Architectural Philosophy: Smart Broker vs. Dumb Broker

### RabbitMQ: "Smart Broker, Dumb Consumer"
- **Model**: AMQP broker. Producers publish to **Exchanges** (Direct, Topic, Fanout, Headers). Exchanges route messages into **Queues** via routing keys.
- **Consumer Interaction**: Broker tracks message delivery and acknowledgement. When a consumer acknowledges (`ack`), the message is immediately purged from the queue.
- **State Management**: The broker maintains complex in-memory state tracking which message has been sent to which consumer.
- **Strengths**: Complex routing rules, per-message TTL, message priorities, Dead Letter Exchanges (DLX), immediate delivery guarantees.

### Apache Kafka: "Dumb Broker, Smart Consumer"
- **Model**: Distributed append-only partitioned commit log.
- **Consumer Interaction**: Messages are persisted to disk sequentially into topics and partitions. They are **not deleted** when read.
- **State Management**: The broker merely appends bytes to disk. Consumers maintain an `offset` (pointer) indicating their position in the log.
- **Strengths**: Extremely high write throughput (millions of msgs/sec via Zero-Copy OS pagecache transfers), durable history retention, event replayability, horizontal scaling by partition.

---

## 2. Comparison Matrix

| Feature | Apache Kafka | RabbitMQ | AWS SQS | Redis Streams |
| :--- | :--- | :--- | :--- | :--- |
| **Primary Pattern** | Event Streaming / Commit Log | Message Queue / AMQP | Managed Task Queue | Lightweight Stream |
| **Message Ordering** | Strict within single partition | FIFO within queue (single consumer) | Best-effort (or strict with SQS FIFO) | Strict per stream entry ID |
| **Retention** | Time/Size-based (hours, days, forever) | Transient (deleted upon ACK) | 1 to 14 days | Capped by length (`MAXLEN`) |
| **Replayability** | Yes (rewind consumer offset to any time) | No (once ACKed, data is lost) | No | Yes (via ID range queries) |
| **Throughput** | 100,000 to 1,000,000+ msgs/sec/node | 20,000 to 50,000 msgs/sec/node | Auto-scales (cloud managed) | 100,000+ ops/sec (in-memory) |
| **Routing Complexity** | Basic (Topic and Partition Key) | Very High (Topic wildcards, Headers) | Basic | Basic |
| **Operational Overhead**| High (KRaft consensus, JVM, disk tuning) | Medium (Erlang VM, Mnesia clustering) | Zero (Serverless fully managed) | Low (reuses existing Redis) |

---

## 3. Decision Tree: Which Queue / Stream Should You Choose?

```
Do you need to replay historical messages or have multiple decoupled systems read the same stream?
├── YES ──> Are you processing > 50,000 events/sec or building a real-time event-driven data pipeline?
│           ├── YES ──> APACHE KAFKA (or AWS MSK / Confluent)
│           └── NO  ──> REDIS STREAMS (if already using Redis) or KAFKA (if growth anticipated)
└── NO  ──> Do you need complex routing (e.g. wildcards, headers, priority queues)?
            ├── YES ──> RABBITMQ
            └── NO  ──> Do you want zero operational overhead in the cloud?
                        ├── YES ──> AWS SQS (Simple Queue Service)
                        └── NO  ──> RABBITMQ (Self-hosted or CloudAMQP)
```

---

## 4. Specific Workload Analysis (e.g., Tinder-like Swipe & Chat Application)

### Should it use Kafka, RabbitMQ, or a simpler queue?
1. **Swipe Events & Recommendation Feedback Loop (Use Apache Kafka)**:
   - User swipes generate massive event volume (100,000+ swipes/sec during peak evening hours).
   - Multiple independent consumer groups need the same swipe event:
     - Consumer Group 1: Match Evaluation Worker (checks for mutual like).
     - Consumer Group 2: Recommendation ML Pipeline (updates Elo/collaborative filtering scores).
     - Consumer Group 3: Analytics & Anti-Abuse (detects bot auto-swiping patterns).
   - In RabbitMQ, fan-out copying of 100,000 msgs/sec across three queues triples memory and disk usage. In Kafka, the single partition log is written once and read concurrently by all three groups with zero overhead.
2. **Chat Push Notifications (Use RabbitMQ or SQS)**:
   - When a match or new message occurs and a push notification must be sent via Apple APNs / Firebase FCM, this is a point-to-point task.
   - Requires retry policies with exponential backoff, priority flags (e.g., "new match" has higher priority than "read receipt"), and dead-letter queues for invalid tokens. RabbitMQ or AWS SQS is superior here.
3. **When to use Redis Streams instead**:
   - If the engineering team is small (< 5 engineers) and already operates a Redis cluster. Redis Streams can process 50,000 events/sec without the burden of running a Kafka cluster.

---

## 5. Failure Scenarios and Operational Pitfalls
- **Kafka Partition Hotspots**: If the partition key has low cardinality (e.g., partitioning by `gender`), all traffic floods into two partitions while other brokers remain idle.
  - *Fix*: Always use high-cardinality keys like `user_id` or composite keys `hash(user_id)`.
- **RabbitMQ Unacknowledged Message Memory Leak**: If consumers process messages without calling `basic_ack`, messages accumulate in RAM until RabbitMQ triggers memory alarm and blocks producers.
  - *Fix*: Always configure `prefetch_count` (e.g., 50–200) to limit outstanding in-flight unacked messages.
