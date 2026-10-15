```json
{
  "topic": "container_orchestration",
  "component": "kubernetes",
  "decision_type": "technology_selection",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://kubernetes.io/docs/concepts/",
  "version": "1.30+",
  "licence": "Apache-2.0",
  "last_verified": "2026-10-14"
}
```

# Container Orchestration Decision Guide: Kubernetes Architecture and Resource Sizing

## 1. Kubernetes Fundamental Primitives

- **Pod**: The smallest deployable computing unit in Kubernetes. Represents a single instance of a running process in a cluster, encapsulating one or more tightly coupled containers, shared storage volumes, and a unique network IP.
- **Deployment**: Declarative controller that manages the desired state of Pods, enabling zero-downtime rolling updates, automated rollbacks, and replica scaling.
- **Service**: An abstract way to expose an application running on a set of Pods as a network service.
  - **ClusterIP**: Internal-only virtual IP reachable strictly within the k8s cluster.
  - **NodePort**: Exposes the service on a static port (30000–32767) on each worker node's external IP.
  - **LoadBalancer**: Provisions an external cloud load balancer (e.g., AWS NLB or GCP Network LB) directing traffic directly to Pods.
- **Ingress Controller (e.g., NGINX, Traefik, Envoy)**: Layer 7 reverse proxy managing external HTTP/S routing, SSL termination, and path-based routing across multiple internal Services.

---

## 2. Resource Management: Requests vs. Limits

Every container in a production pod must specify CPU and memory resources:

```yaml
resources:
  requests:
    cpu: "250m"       # 0.25 vCPU allocated for scheduling
    memory: "512Mi"   # 512 MB guaranteed RAM
  limits:
    cpu: "1000m"      # 1 vCPU max (throttled via CFS if exceeded)
    memory: "1Gi"     # 1 GB hard limit (OOMKilled if exceeded)
```

### Critical Production Rules
1. **CPU Throttling**: CPU is a compressible resource. When a container exceeds its CPU limit, Linux Completely Fair Scheduler (CFS) throttles CPU cycles. The process slows down, increasing request latency, but is not terminated.
2. **OOMKill (Out Of Memory)**: Memory is an incompressible resource. If a container allocates memory beyond its `limits.memory`, the Linux kernel immediately terminates the process with Exit Code 137 (`OOMKilled`).
3. **Overcommit Dangers**: Setting `requests` significantly lower than `limits` enables node overcommit. If all pods spike simultaneously, the worker node suffers memory pressure, evicting pods unexpectedly.

---

## 3. Health Probes: Liveness vs. Readiness vs. Startup

- **Liveness Probe**: Determines if the container needs to be restarted.
  - *Pitfall*: If liveness probe pings an external database that goes down, Kubernetes will blindly restart every single API container in the cluster, creating a restart storm. Liveness probes must only check internal container process liveness.
- **Readiness Probe**: Determines if the container is ready to accept incoming network traffic.
  - If readiness probe fails (e.g., while warming in-memory caches or loading ML weights), the Service temporarily removes the Pod's IP from the load balancer target pool until it recovers.
- **Startup Probe**: Disables liveness and readiness checks until the application has completed its initial slow bootup sequence.

---

## 4. Horizontal Pod Autoscaler (HPA) Strategy
- Default HPA scales on average CPU or Memory utilization (e.g., maintain 70% CPU).
- **Advanced Production Autoscaling**: Scale based on business metrics via KEDA (Kubernetes Event-driven Autoscaling):
  - Scale WebSocket gateway pods based on active concurrent TCP connections.
  - Scale background worker pods based on Kafka topic lag (`consumer_lag > 500`).
