```json
{
  "topic": "traffic_management_and_networking",
  "component": "load_balancer",
  "decision_type": "technology_selection",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://roadmap.sh/system-design",
  "version": "1.0",
  "licence": "Open-Documentation",
  "last_verified": "2026-10-14"
}
```

# Traffic Management Decision Guide: DNS, CDNs, and Load Balancers (L4 vs. L7)

## 1. Global Traffic Ingress: DNS and CDN

### 1.1 DNS Routing Strategies (e.g., Route 53 / Cloudflare DNS)
- **Geolocation Routing**: Resolves client DNS requests to the IP address of the datacenter closest to the client's geographic country or state.
- **Latency-Based Routing**: Cloud provider periodically measures round-trip time between network regions and routes client to the lowest-latency endpoint.
- **Health Checks & Failover Routing**: Automated DNS health checks ping primary region endpoints. If probes fail consecutively, DNS updates within 60 seconds (low TTL) to redirect traffic to the secondary standby region.

### 1.2 Content Delivery Networks (CDNs)
- **Architecture**: Distributed edge Points of Presence (PoPs) deployed globally (e.g., Cloudflare, CloudFront, Fastly).
- **Edge Offloading**:
  - Terminates TLS handshakes at the edge node closest to the client, shaving 100–300ms off TCP/TLS connection setup times.
  - Caches static assets (images, video segments, CSS, JS, fonts) with `Cache-Control: public, max-age=31536000, immutable`.
  - Compresses responses using Brotli/Gzip and converts images to WebP/AVIF dynamically.
  - Mitigates volumetric DDoS attacks (SYN floods, UDP reflection) at the edge before traffic hits origin servers.

---

## 2. Layer 4 vs. Layer 7 Load Balancing

```
[Client]
   │
   ▼
[Layer 4 Load Balancer (NLB / IPVS)]   <-- Operates on IP/TCP/UDP packets (Millions req/s, ultra-low latency)
   │
   ▼
[Layer 7 Load Balancer (ALB / Envoy)]  <-- Inspects HTTP headers, cookies, paths, SSL termination
   ├── Path: /api/v1/auth    ──> [Auth Service Cluster]
   ├── Path: /api/v1/chat    ──> [WebSocket Gateway Cluster]
   └── Path: /api/v1/search  ──> [Search Service Cluster]
```

### Detailed Comparison Matrix
| Dimension | Layer 4 Load Balancer (NLB) | Layer 7 Load Balancer (ALB / Reverse Proxy) |
| :--- | :--- | :--- |
| **OSI Layer** | Transport Layer (TCP, UDP, TLS) | Application Layer (HTTP/1.1, HTTP/2, HTTP/3, WebSockets, gRPC) |
| **Packet Inspection** | Source IP, Source Port, Dest IP, Dest Port only | Full HTTP payload: URL path, query params, cookies, headers |
| **SSL/TLS Handling** | Pass-through or high-speed hardware termination | Full SSL termination, certificate management, SNI routing |
| **Throughput & Latency**| Ultra-high throughput (millions of connections/sec), sub-millisecond latency | High throughput, adds ~2–5ms processing latency per request |
| **Routing Intelligence**| Cannot route by URL or HTTP verb; routes whole TCP streams | Path-based routing (`/users` vs `/orders`), host headers, cookie stickiness |
| **Sticky Sessions** | IP-hash based (problematic if users share corporate NAT IP) | Cookie-based (`AWSALB` session cookie injection) |
| **Typical Tools** | AWS NLB, Linux IPVS, HAProxy (TCP mode) | AWS ALB, NGINX, Envoy Proxy, Traefik |

---

## 3. Load Balancing Algorithms

1. **Round Robin**: Distributes requests sequentially across backend instances. Ideal when all servers have identical hardware and requests have uniform processing cost.
2. **Weighted Round Robin**: Routes a higher proportion of requests to instances with larger CPU/RAM capacity.
3. **Least Connections**: Routes incoming request to the server currently handling the fewest active connections. Ideal for long-lived connections (e.g., database queries, WebSocket chat, video streaming).
4. **IP Hash**: Hashes client IP to ensure the same client consistently routes to the same backend server (useful for caching session state locally in memory).
5. **Consistent Hashing**: Used in distributed caching and storage tiers to minimize key redistribution during node scale-up or scale-down.

---

## 4. Production Load Balancer Configuration Best Practices
- **Connection Draining (Deregistration Delay)**: When terminating an instance during deployment or autoscaling down, keep the socket open for 30–60 seconds to allow existing in-flight HTTP requests and database writes to complete gracefully before severing connections.
- **Cross-Zone Load Balancing**: Ensure the load balancer evenly distributes traffic across target instances in all availability zones, preventing unbalanced loads when clients concentrate in one subnet.
- **Proper Health Checks**: Health check endpoint (e.g., `/healthz`) must verify core internal connectivity (DB, Redis) without triggering expensive database queries on every ping (which can cause health checks to DOS the database).
