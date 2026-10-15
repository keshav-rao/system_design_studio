```json
{
  "topic": "reference_architecture",
  "component": "messaging_platform",
  "decision_type": "reference_architecture",
  "content_type": "reference_architecture",
  "cloud_provider": "provider_neutral",
  "source_url": "https://engineering.fb.com/ | https://discord.com/blog",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# Reference Architecture: Real-Time Chat & Messaging Platform (WhatsApp / Discord Scale)

## 1. System Requirements
- **Scale**: 50 million concurrent active connections, 100,000 messages/sec peak.
- **Latency**: P99 message delivery latency < 150ms globally.
- **Features**: 1-on-1 private messaging, group chat (up to 1,000 members), online presence status, read receipts, offline message queuing.

---

## 2. Core Architecture & Topology

```
[Mobile / Web Clients]
          │ (WSS: WebSocket Secure)
          ▼
[Layer 4 Network Load Balancer (NLB)]
          │ (TCP passthrough)
          ▼
[Gateway Fleet: Erlang / Go / Rust WebSocket Servers]
   │ (Maintains 1M active TCP sockets per large node)
   ├── (Presence & Session Map) ──> [Redis Cluster (Session Registry)]
   ├── (Message Routing)        ──> [Internal gRPC Service Mesh]
   └── (Offline Queuing)        ──> [RabbitMQ / Kafka]
                                         │
                                         ▼
                             [Cassandra / ScyllaDB Cluster]
                              (Immutable Message History)
```

---

## 3. Key Design Decisions & Mechanics

### 3.1 Connection Termination and C10M Problem
- Operating systems hit memory limits when holding millions of open TCP sockets.
- **Tuning**:
  - Increase Linux file descriptor limits: `sysctl -w fs.file-max=2097152`.
  - Reduce TCP receive/transmit buffer memory: `sysctl -w net.ipv4.tcp_rmem="4096 87380 4194304"`.
  - Use lightweight runtime (Erlang/BEAM or Go/Rust epoll) where each socket connection costs < 4 KB of memory.

### 3.2 Session Registry (Where is User X connected?)
- When User A sends a message to User B:
  1. Gateway server receiving message checks Redis: `HGET user:sessions user_B`.
  2. Redis returns the IP address of the specific Gateway node holding User B's active WebSocket connection (e.g., `10.0.4.18`).
  3. Gateway forwards message over internal low-latency gRPC to `10.0.4.18`, which pushes it down the socket to User B.
  4. If User B is offline (no active session), message is written to Cassandra and an event is queued in RabbitMQ to trigger a push notification via APNs/FCM.

### 3.3 Message Ordering & Deduplication
- **Unique IDs**: Generated using Twitter Snowflake or UUIDv7 (64-bit integer: 41 bits timestamp + 10 bits machine ID + 12 bits sequence number).
- Guarantees k-sorted chronological ordering without cross-server clock sync coordination.
- Clients send client-side generated message ID (`client_msg_id`) as an idempotency key to prevent duplicate messages during transient mobile network reconnects.

### 3.4 Group Chat Fan-Out
- For small groups (< 50 members): Fan-out on write. The sender's message is replicated to each recipient's inbox.
- For massive groups (> 1,000 members): Shared message channel. Messages are written once to the group room log, and clients pull or receive pub/sub broadcasts via Redis/Kafka.
