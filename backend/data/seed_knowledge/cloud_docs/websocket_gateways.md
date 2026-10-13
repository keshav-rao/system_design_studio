# WebSocket Gateways and Real-Time Connection Scaling

## Protocol Characteristics
Unlike short-lived stateless HTTP request/response lifecycles, WebSockets establish a single bi-directional, full-duplex TCP connection that remains open indefinitely.
- Upgrades via HTTP handshake (`Upgrade: websocket`).
- Negligible frame overhead (2 to 10 bytes per packet) compared to verbose HTTP headers.

## Architectural Bottlenecks at Scale
1. **Operating System File Descriptors (Sockets)**:
   - Every active open connection holds a file descriptor.
   - Scale limits require tuning `sysctl`: `fs.file-max`, `net.core.somaxconn`, and `ulimit -n 1000000`.
2. **Memory Overhead**:
   - Each socket maintains read/write buffers. At 20 KB per connection, 1 million concurrent idle connections consume $\approx 20\text{ GB}$ of RAM.
3. **Cross-Server Routing and Fan-Out**:
   - Client A is connected to Server Node 1, while Client B is connected to Server Node 2.
   - When Client A sends a chat message to Client B, Server Node 1 has no direct memory reference to Client B.

## Decoupled Pub/Sub Backplane Pattern
- **Redis Pub/Sub / Apache Kafka / NATS**:
  - WebSocket gateway servers act as pure connection terminations.
  - When a message is sent, the gateway publishes an event to the shared message broker channel.
  - All gateway nodes subscribe to user/room channels and forward messages down to locally connected client sockets.
- **Heartbeats & Keep-Alive**:
  - Mandatory ping/pong frames every 30–60 seconds prevent intermediary NAT gateways, firewalls, and cloud load balancers (AWS ALB 60s idle timeout) from abruptly closing idle sockets.
