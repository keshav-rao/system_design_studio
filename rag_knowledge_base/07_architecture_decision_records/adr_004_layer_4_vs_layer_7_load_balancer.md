```json
{
  "topic": "architecture_decision_record",
  "component": "load_balancing_tier",
  "decision_type": "technology_selection",
  "content_type": "adr",
  "cloud_provider": "provider_neutral",
  "source_url": "https://martinfowler.com/bliki/ArchitectureDecisionRecord.html",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# ADR 004: Ingress Load Balancing Architecture: Layer 4 vs. Layer 7 Tiering

## Status
**Accepted**

## Context
The platform must handle high-concurrency external traffic consisting of:
1. Short-lived REST / GraphQL API requests (`/api/v1/*`).
2. Long-lived persistent WebSocket connections for real-time messaging and notifications (`/ws/chat`).
3. Static media downloads and direct presigned S3 uploads.

We must define the ingress topology to balance extreme connection throughput with application-level routing flexibility.

## Decision
Adopt a **Two-Tier Ingress Architecture**:
1. **Tier 1 (Layer 4 Network Load Balancer - NLB)**:
   - Terminates edge IP traffic with static Anycast IP addresses.
   - Handles multi-million concurrent TCP connections with ultra-low latency and zero packet inspection overhead.
   - Forwards raw TCP traffic to the Layer 7 tier.
2. **Tier 2 (Layer 7 Application Load Balancer - ALB / Envoy Ingress)**:
   - Terminates TLS (SSL certificates).
   - Performs HTTP/2 and WebSocket protocol negotiation.
   - Inspects URL paths and routes traffic to specialized service clusters:
     - `/api/v1/auth` -> Auth Service.
     - `/api/v1/swipe` -> Swipe Engine.
     - `/ws/*` -> WebSocket Gateway Fleet (with Least Connections routing).

## Alternatives Considered
1. **Single-Tier Layer 7 ALB Only**:
   - Viable for lower traffic (< 50,000 concurrent sockets), but ALB auto-scaling during sudden traffic surges is slower than an NLB.
2. **Single-Tier Layer 4 NLB Only**:
   - Lacks URL path routing, HTTP header inspection, cookie-based session stickiness, and gzip/brotli compression support. Every microservice would have to implement independent TLS termination.

## Consequences & Trade-offs
### Positive Consequences
- Maximum scalability: NLB easily absorbs volumetric traffic spikes and DDoS surges.
- Maximum flexibility: ALB / Envoy provides dynamic canary routing, path rewriting, and rate limiting.

### Negative Consequences & Risks
- Incurs two load-balancing hops (minor latency addition of ~1–2ms).
- Slightly higher cloud infrastructure cost compared to a single load balancer.
