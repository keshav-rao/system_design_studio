# Product Context

## Problem
Designers and developers struggle to formulate defensible, production-ready system architectures. Chatbots often hallucinate connections or suggest ungrounded patterns without explaining trade-offs.

## Solution
An interactive AI System Design Studio:
1. **Interactive Requirements Interview**: Gathers in-and-out details (target scale, geographical distribution, read/write ratio, latency tolerances, storage types, caching, load balancers, messaging queues).
2. **Infinite Canvas Visualization**: Automatically constructs layered high-level system diagrams (React Flow) with full component rationale (e.g. why Kafka was selected).
3. **Component Alternatives & Tool Swapping**: Allows users to select alternatives directly on canvas (e.g., Redis vs AWS ElastiCache vs Memcached; Nginx vs AWS ALB vs Envoy).
4. **Load Testing Simulation**: Simulates architectural behaviour under 1, 100, 1k, and 100k concurrent users to surface bottlenecks and latency impact.
5. **Tiered Cost & Setup Breakdown**: Generates cost estimates comparing free-tier capabilities (1–10k users) to pro managed cloud infrastructure (10k–100k users).
