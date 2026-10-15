"""Seed dataset for Phase 2 structured component catalog and compatibility matrix.

Contains 38 production-grade architectural components across all major categories
and layers, including limits, failure modes, cost units, and compatibility edges.
"""

from typing import Any

SEED_COMPONENTS: list[dict[str, Any]] = [
    # --- CDN / Edge ---
    {
        "slug": "cloudflare-cdn",
        "name": "Cloudflare Edge CDN",
        "category": "cdn",
        "layer": "edge",
        "description": "Global Anycast edge content delivery network providing edge caching, DDoS mitigation, WAF, and TLS termination.",
        "protocols": ["HTTPS", "HTTP/2", "HTTP/3", "WebSocket"],
        "limits": {
            "max_throughput_qps": 500000,
            "latency_p99_ms": 25,
            "max_payload_size_mb": 100,
            "cache_ttl_max_days": 365,
        },
        "failure_modes": [
            {
                "mode": "Cache stampede / Origin overload",
                "impact": "Origin server overwhelmed when hot keys expire simultaneously.",
                "mitigation": "Enable tiered caching and origin shield with stale-while-revalidate.",
            },
            {
                "mode": "SSL handshake exhaustion",
                "impact": "Increased TLS connection latency under traffic spikes.",
                "mitigation": "Enable session resumption, TLS 1.3 0-RTT, and origin keep-alive.",
            },
        ],
        "cost_units": {
            "model": "tier_bandwidth",
            "unit": "$/month + $/GB egress",
            "base_monthly_usd": 20.0,
            "free_tier": "Free plan includes basic CDN & shared SSL",
            "notes": "Enterprise plans custom; free/pro covers up to ~10TB traffic.",
        },
        "alternatives": ["aws-cloudfront", "fastly-cdn"],
    },
    {
        "slug": "aws-cloudfront",
        "name": "Amazon CloudFront",
        "category": "cdn",
        "layer": "edge",
        "description": "Low-latency content delivery network tightly integrated with AWS services like S3, API Gateway, and ALB.",
        "protocols": ["HTTPS", "HTTP/2", "HTTP/3", "WebSocket"],
        "limits": {
            "max_throughput_qps": 250000,
            "latency_p99_ms": 30,
            "max_payload_size_mb": 40,
            "cache_ttl_max_days": 365,
        },
        "failure_modes": [
            {
                "mode": "Origin timeout (504 Gateway Timeout)",
                "impact": "Users see HTTP 504 when upstream API takes >30s.",
                "mitigation": "Set aggressive read timeouts, enable CloudFront failover origins.",
            }
        ],
        "cost_units": {
            "model": "transfer",
            "unit": "$0.085/GB data transfer out",
            "base_monthly_usd": 0.0,
            "free_tier": "1TB free data transfer out per month permanently",
            "notes": "Cost scales with regional egress volume and HTTPS request counts.",
        },
        "alternatives": ["cloudflare-cdn", "fastly-cdn"],
    },
    # --- Gateways & Proxies ---
    {
        "slug": "nginx-reverse-proxy",
        "name": "NGINX Reverse Proxy & Load Balancer",
        "category": "gateway",
        "layer": "gateway",
        "description": "High-performance HTTP server, reverse proxy, load balancer, and SSL termination engine.",
        "protocols": ["HTTP", "HTTPS", "HTTP/2", "TCP", "UDP", "WebSocket"],
        "limits": {
            "max_throughput_qps": 75000,
            "connection_limit": 50000,
            "latency_p99_ms": 2,
            "max_payload_size_mb": 50,
        },
        "failure_modes": [
            {
                "mode": "Worker process connection saturation",
                "impact": "Dropped connections and HTTP 502/504 errors.",
                "mitigation": "Tune worker_rlimit_nofile and worker_connections in nginx.conf.",
            },
            {
                "mode": "Upstream health check flapping",
                "impact": "Traffic oscillation between failing backend nodes.",
                "mitigation": "Configure passive max_fails and fail_timeout parameters.",
            },
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/instance-month (compute host)",
            "base_monthly_usd": 20.0,
            "free_tier": "Open-source OSS; host on any cloud VPS",
            "notes": "Cost is purely the virtual machine or container running NGINX.",
        },
        "alternatives": ["envoy-proxy", "kong-api-gateway", "traefik"],
    },
    {
        "slug": "kong-api-gateway",
        "name": "Kong API Gateway",
        "category": "gateway",
        "layer": "gateway",
        "description": "Cloud-native API gateway providing authentication, rate limiting, logging, and plugin extensibility.",
        "protocols": ["HTTP", "HTTPS", "gRPC", "WebSocket"],
        "limits": {
            "max_throughput_qps": 40000,
            "connection_limit": 30000,
            "latency_p99_ms": 5,
        },
        "failure_modes": [
            {
                "mode": "Postgres/Redis config datastore latency spike",
                "impact": "Gateway delays routing requests during cache invalidation.",
                "mitigation": "Run Kong in DB-less declarative mode with in-memory caching.",
            }
        ],
        "cost_units": {
            "model": "provisioned_or_saas",
            "unit": "$/gateway-node-month",
            "base_monthly_usd": 40.0,
            "free_tier": "Kong Gateway Community OSS is free to self-host",
            "notes": "Kong Enterprise SaaS starts at ~$250/mo.",
        },
        "alternatives": ["nginx-reverse-proxy", "aws-api-gateway", "envoy-proxy"],
    },
    {
        "slug": "aws-api-gateway",
        "name": "Amazon API Gateway",
        "category": "gateway",
        "layer": "gateway",
        "description": "Fully managed API management service for creating, publishing, maintaining, and securing REST, HTTP, and WebSocket APIs.",
        "protocols": ["HTTPS", "WebSocket"],
        "limits": {
            "max_throughput_qps": 10000,
            "latency_p99_ms": 20,
            "max_payload_size_mb": 10,
            "timeout_seconds": 29,
        },
        "failure_modes": [
            {
                "mode": "Account-level burst throttle (HTTP 429)",
                "impact": "Requests rejected when exceeding 10k RPS burst quota.",
                "mitigation": "Request AWS service quota increases; enable usage plans with client keys.",
            }
        ],
        "cost_units": {
            "model": "serverless",
            "unit": "$1.00 per 1M HTTP API calls, $3.50 per 1M REST API calls",
            "base_monthly_usd": 0.0,
            "free_tier": "1M API calls per month for first 12 months",
            "notes": "Pay per million calls + data transfer out.",
        },
        "alternatives": ["kong-api-gateway", "nginx-reverse-proxy"],
    },
    {
        "slug": "envoy-proxy",
        "name": "Envoy Service Proxy",
        "category": "gateway",
        "layer": "gateway",
        "description": "High-performance C++ distributed proxy designed for cloud-native service meshes and ingress edge gateways.",
        "protocols": ["HTTP/1.1", "HTTP/2", "gRPC", "TCP"],
        "limits": {
            "max_throughput_qps": 80000,
            "connection_limit": 60000,
            "latency_p99_ms": 1,
        },
        "failure_modes": [
            {
                "mode": "Circuit breaker trip under downstream congestion",
                "impact": "Early request rejection via local 503 flags.",
                "mitigation": "Calibrate max_pending_requests and consecutive_5xx threshold.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/instance-month",
            "base_monthly_usd": 25.0,
            "free_tier": "Open-source OSS (Cloud Native Computing Foundation)",
            "notes": "Deploys as sidecar or ingress controller.",
        },
        "alternatives": ["nginx-reverse-proxy", "traefik"],
    },
    {
        "slug": "websocket-gateway",
        "name": "WebSocket Realtime Gateway",
        "category": "gateway",
        "layer": "gateway",
        "description": "Persistent connection termination gateway managing full-duplex bi-directional client channels with heartbeats and room presence.",
        "protocols": ["WebSocket", "WSS", "TCP"],
        "limits": {
            "max_throughput_qps": 30000,
            "connection_limit": 100000,
            "latency_p99_ms": 10,
        },
        "failure_modes": [
            {
                "mode": "File descriptor leak / OS socket exhaustion",
                "impact": "Gateway cannot accept new socket handshakes.",
                "mitigation": "Tune sysctl fs.file-max and ulimit -n to 1048576, implement heartbeat timeouts.",
            },
            {
                "mode": "Reconnection storm after node failure",
                "impact": "Mass reconnects DDOS auth service and redis presence store.",
                "mitigation": "Client jittered exponential backoff and connection rate limiting.",
            },
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/instance-month (memory-bound)",
            "base_monthly_usd": 35.0,
            "free_tier": "Self-host via Node.js ws or Go Gorilla",
            "notes": "Memory footprint ~2KB per idle TCP connection.",
        },
        "alternatives": ["aws-api-gateway", "pusher-channels"],
    },
    # --- Auth & Security ---
    {
        "slug": "jwt-auth-service",
        "name": "Stateless JWT Auth Service",
        "category": "auth",
        "layer": "application",
        "description": "Identity and access management service issuing cryptographically signed RS256/EdDSA JWT access and refresh tokens.",
        "protocols": ["HTTPS", "gRPC"],
        "limits": {
            "max_throughput_qps": 20000,
            "latency_p99_ms": 8,
            "token_ttl_access_minutes": 15,
            "token_ttl_refresh_days": 30,
        },
        "failure_modes": [
            {
                "mode": "Signing key compromise",
                "impact": "Attacker can forge valid authorization tokens.",
                "mitigation": "Automated asymmetric JWKS key rotation and token blacklist cache.",
            },
            {
                "mode": "Refresh token replay attack",
                "impact": "Compromised refresh tokens used repeatedly.",
                "mitigation": "One-time refresh token rotation with family revocation detection.",
            },
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/microservice-instance-month",
            "base_monthly_usd": 15.0,
            "free_tier": "Open source libraries (PyJWT, jose) free to host",
            "notes": "Or managed Auth0/Clerk with free tier up to 7,500-10,000 MAU.",
        },
        "alternatives": ["oauth2-provider", "clerk-auth", "auth0"],
    },
    {
        "slug": "oauth2-provider",
        "name": "OAuth2 / OIDC Identity Provider (Keycloak)",
        "category": "auth",
        "layer": "application",
        "description": "Federated identity provider supporting OAuth 2.1, OpenID Connect, social logins, SSO, and MFA.",
        "protocols": ["HTTPS", "OIDC"],
        "limits": {
            "max_throughput_qps": 8000,
            "connection_limit": 5000,
            "latency_p99_ms": 25,
        },
        "failure_modes": [
            {
                "mode": "User database contention during peak login hours",
                "impact": "Increased login latency and password verification queue buildup.",
                "mitigation": "Read replicas for user lookups, argon2id hashing worker thread pool.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/instance-month",
            "base_monthly_usd": 30.0,
            "free_tier": "Self-hosted Keycloak OSS is free",
            "notes": "Requires backing relational DB for user persistence.",
        },
        "alternatives": ["jwt-auth-service", "auth0", "firebase-auth"],
    },
    {
        "slug": "hashicorp-vault",
        "name": "HashiCorp Vault Secrets Manager",
        "category": "security",
        "layer": "infra",
        "description": "Centralized secret management, dynamic database credential generation, encryption-as-a-service, and transit keys.",
        "protocols": ["HTTPS", "gRPC"],
        "limits": {
            "max_throughput_qps": 15000,
            "latency_p99_ms": 5,
        },
        "failure_modes": [
            {
                "mode": "Sealed vault cluster upon unexpected reboot",
                "impact": "Services cannot read secrets or DB credentials.",
                "mitigation": "Cloud KMS auto-unseal (AWS KMS, GCP KMS) with HA raft storage.",
            }
        ],
        "cost_units": {
            "model": "provisioned_or_managed",
            "unit": "$/instance-month",
            "base_monthly_usd": 35.0,
            "free_tier": "Vault Community OSS is free to host",
            "notes": "HCP Vault managed starts at $0.03/hr.",
        },
        "alternatives": ["aws-secrets-manager", "doppler"],
    },
    # --- Compute & Workers ---
    {
        "slug": "fastapi-app-server",
        "name": "FastAPI Async Application Server",
        "category": "compute",
        "layer": "application",
        "description": "High-performance Python ASGI backend service powered by Starlette and Pydantic with native async I/O.",
        "protocols": ["HTTP", "HTTPS", "WebSocket"],
        "limits": {
            "max_throughput_qps": 12000,
            "connection_limit": 15000,
            "latency_p99_ms": 12,
            "concurrency_limit_per_worker": 2000,
        },
        "failure_modes": [
            {
                "mode": "Blocking CPU call inside async event loop",
                "impact": "Starves all concurrent async coroutines on worker process.",
                "mitigation": "Offload CPU-bound or blocking sync tasks to asyncio.to_thread or Celery.",
            },
            {
                "mode": "Memory leak in long-lived connection handlers",
                "impact": "Process crashes with OOM.",
                "mitigation": "Configure Uvicorn worker recycling (--max-requests) and monitor RSS memory.",
            },
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/container-instance-month",
            "base_monthly_usd": 20.0,
            "free_tier": "Deployable on standard free compute tier (e.g. Render, Fly.io)",
            "notes": "Cost scales with vCPU count and memory footprint.",
        },
        "alternatives": [
            "node-express-server",
            "go-microservice",
            "spring-boot-server",
        ],
    },
    {
        "slug": "node-express-server",
        "name": "Node.js / Express Application Server",
        "category": "compute",
        "layer": "application",
        "description": "Event-driven JavaScript/TypeScript backend server optimal for I/O multiplexing and JSON API services.",
        "protocols": ["HTTP", "HTTPS", "WebSocket"],
        "limits": {
            "max_throughput_qps": 15000,
            "connection_limit": 20000,
            "latency_p99_ms": 15,
        },
        "failure_modes": [
            {
                "mode": "Event loop lag from synchronous JSON parsing or regex evaluation",
                "impact": "High p99 latency spikes and connection timeouts.",
                "mitigation": "Use streaming parsers, avoid complex ReDoS regexes, use clustering.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/container-month",
            "base_monthly_usd": 20.0,
            "free_tier": "Free compute tier supported",
            "notes": "Scales horizontally across lightweight container replicas.",
        },
        "alternatives": ["fastapi-app-server", "go-microservice"],
    },
    {
        "slug": "go-microservice",
        "name": "Go High-Throughput Microservice",
        "category": "compute",
        "layer": "application",
        "description": "Compiled, statically typed Go service utilizing goroutines for minimal memory overhead and ultra-high concurrency.",
        "protocols": ["HTTP", "gRPC", "TCP"],
        "limits": {
            "max_throughput_qps": 45000,
            "connection_limit": 50000,
            "latency_p99_ms": 3,
            "memory_footprint_mb": 50,
        },
        "failure_modes": [
            {
                "mode": "Goroutine leak under unclosed channel or context",
                "impact": "Steady memory ramp leading to container OOM kill.",
                "mitigation": "Pass context.Context with timeout to all channels and network calls.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/container-month",
            "base_monthly_usd": 15.0,
            "free_tier": "Extremely low idle footprint (~15MB RAM)",
            "notes": "Ideal for cost reduction at scale due to compact memory usage.",
        },
        "alternatives": ["fastapi-app-server", "spring-boot-server"],
    },
    {
        "slug": "spring-boot-server",
        "name": "Spring Boot Enterprise Service",
        "category": "compute",
        "layer": "application",
        "description": "Enterprise Java backend framework offering strong type safety, mature ecosystem, and ORM abstractions.",
        "protocols": ["HTTP", "HTTPS", "gRPC"],
        "limits": {
            "max_throughput_qps": 20000,
            "connection_limit": 10000,
            "latency_p99_ms": 20,
            "memory_footprint_mb": 512,
        },
        "failure_modes": [
            {
                "mode": "JVM Garbage collection stop-the-world pauses",
                "impact": "Periodic 100ms-500ms latency spikes.",
                "mitigation": "Tune G1GC or ZGC collectors, calibrate heap bounds.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/instance-month (RAM-heavy)",
            "base_monthly_usd": 40.0,
            "free_tier": "None (demands at least 512MB-1GB RAM for JVM)",
            "notes": "Higher base cost than Go/Node due to JVM memory overhead.",
        },
        "alternatives": ["go-microservice", "fastapi-app-server"],
    },
    {
        "slug": "celery-worker",
        "name": "Celery Asynchronous Task Worker",
        "category": "compute",
        "layer": "async",
        "description": "Distributed task queue execution worker for background processing, email sending, batch computation, and image resizing.",
        "protocols": ["AMQP", "Redis Protocol"],
        "limits": {
            "max_throughput_qps": 5000,
            "concurrency_limit": 64,
            "task_timeout_seconds": 3600,
        },
        "failure_modes": [
            {
                "mode": "Task queue backup during downstream service outage",
                "impact": "Job backlog balloons, message memory fills broker.",
                "mitigation": "Configure task retries with exponential backoff and dead-letter queues (DLQ).",
            },
            {
                "mode": "Worker OOM on batch memory leak",
                "impact": "Worker abruptly terminates unfinished tasks.",
                "mitigation": "Set --max-tasks-per-child and --max-memory-per-child.",
            },
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/worker-month",
            "base_monthly_usd": 15.0,
            "free_tier": "Open source Python; runs on standard worker dyno",
            "notes": "Scales horizontally with backlog depth metric.",
        },
        "alternatives": ["aws-lambda", "temporal-orchestrator"],
    },
    {
        "slug": "aws-lambda",
        "name": "AWS Lambda Serverless Compute",
        "category": "compute",
        "layer": "application",
        "description": "Event-driven serverless computing platform executing code in response to API requests, SQS messages, or S3 uploads.",
        "protocols": ["HTTPS", "AWS EventBridge"],
        "limits": {
            "max_throughput_qps": 10000,
            "concurrency_limit": 1000,
            "max_payload_size_mb": 6,
            "timeout_seconds": 900,
            "latency_p99_ms": 70,
        },
        "failure_modes": [
            {
                "mode": "Cold start latency spike",
                "impact": "First invocation takes 300ms-2000ms to initialize runtime.",
                "mitigation": "Use lightweight runtimes (Node, Go, Python), provisioned concurrency for critical paths.",
            },
            {
                "mode": "Relational DB connection pool starvation",
                "impact": "Lambda instances spawn thousands of concurrent DB connections.",
                "mitigation": "Use RDS Proxy or PgBouncer between Lambda and PostgreSQL.",
            },
        ],
        "cost_units": {
            "model": "serverless",
            "unit": "$0.20 per 1M requests + $0.0000166667 for every GB-second",
            "base_monthly_usd": 0.0,
            "free_tier": "1M free requests and 400,000 GB-seconds of compute time per month",
            "notes": "Zero cost when idle; ideal for unpredictable or bursty workloads.",
        },
        "alternatives": ["fastapi-app-server", "celery-worker"],
    },
    # --- Caching ---
    {
        "slug": "redis-cache",
        "name": "Redis In-Memory Key-Value Cache",
        "category": "cache",
        "layer": "data",
        "description": "Ultra-low latency in-memory data store supporting strings, hashes, sorted sets, bitmaps, TTLs, and atomic transactions.",
        "protocols": ["RESP", "TCP"],
        "limits": {
            "max_throughput_qps": 100000,
            "connection_limit": 10000,
            "latency_p99_ms": 1,
            "max_key_size_mb": 512,
        },
        "failure_modes": [
            {
                "mode": "Maxmemory OOM eviction cascade",
                "impact": "Critical session or rate-limiting keys get dropped.",
                "mitigation": "Set volatile-lru eviction policy and configure 20% reserved memory buffer.",
            },
            {
                "mode": "Thundering herd on cache key expiration",
                "impact": "Thousands of requests hit database at once when key expires.",
                "mitigation": "Use probabilistic early expiration (XFetch) or distributed lock with mutex.",
            },
            {
                "mode": "Slow single-threaded command (e.g. KEYS *)",
                "impact": "Blocks all subsequent Redis operations.",
                "mitigation": "Rename/disable dangerous commands in config; use SCAN instead of KEYS.",
            },
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/GB-RAM-month",
            "base_monthly_usd": 15.0,
            "free_tier": "Upstash Redis offers 10,000 requests/day free; self-hostable OSS",
            "notes": "Cost scales with allocated RAM.",
        },
        "alternatives": ["memcached", "dragonfly-db"],
    },
    {
        "slug": "memcached",
        "name": "Memcached Distributed Cache",
        "category": "cache",
        "layer": "data",
        "description": "Multi-threaded in-memory key-value cache designed for simple high-throughput object caching without persistence overhead.",
        "protocols": ["TCP", "Binary Memcached Protocol"],
        "limits": {
            "max_throughput_qps": 150000,
            "connection_limit": 20000,
            "latency_p99_ms": 1,
            "max_payload_size_mb": 1,
        },
        "failure_modes": [
            {
                "mode": "Slab allocation imbalance",
                "impact": "Premature eviction even with free memory in other slabs.",
                "mitigation": "Enable modern slab automove and slab reassign runtime features.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/GB-RAM-month",
            "base_monthly_usd": 12.0,
            "free_tier": "Free open source",
            "notes": "Purely memory bound; lacks persistence or replication features.",
        },
        "alternatives": ["redis-cache"],
    },
    # --- Relational & Distributed Databases ---
    {
        "slug": "postgresql",
        "name": "PostgreSQL Relational Database",
        "category": "database",
        "layer": "data",
        "description": "Advanced ACID-compliant object-relational SQL database supporting complex joins, foreign keys, JSONB, and extensions.",
        "protocols": ["TCP", "SQL"],
        "limits": {
            "max_throughput_qps": 20000,
            "connection_limit": 500,
            "latency_p99_ms": 15,
            "storage_capacity_tb": 32,
            "max_row_size_mb": 32,
        },
        "failure_modes": [
            {
                "mode": "PostgreSQL connection exhaustion",
                "impact": "FATAL: remaining connection slots are reserved for non-replication superuser connections (500 errors).",
                "mitigation": "Place PgBouncer in front of Postgres to pool connections from app instances.",
            },
            {
                "mode": "Table bloat due to autovacuum starvation",
                "impact": "Degraded read performance, disk space exhaustion.",
                "mitigation": "Tune autovacuum_vacuum_scale_factor and autovacuum_cost_limit.",
            },
            {
                "mode": "Replication lag on read replicas",
                "impact": "Stale reads right after writes (read-your-own-writes hazard).",
                "mitigation": "Route read-after-write queries directly to primary or check replication LSN.",
            },
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/instance-month (vCPU + RAM + Storage)",
            "base_monthly_usd": 30.0,
            "free_tier": "Neon / Supabase provide 500MB free PostgreSQL tier",
            "notes": "Cost scales with instance size (db.t4g.small ~$30/mo up to multi-hundreds for HA).",
        },
        "alternatives": ["mysql", "cockroachdb"],
    },
    {
        "slug": "mysql",
        "name": "MySQL Relational Database",
        "category": "database",
        "layer": "data",
        "description": "Widely deployed open-source relational database powered by the InnoDB storage engine with row-level locking.",
        "protocols": ["TCP", "SQL"],
        "limits": {
            "max_throughput_qps": 22000,
            "connection_limit": 600,
            "latency_p99_ms": 15,
            "storage_capacity_tb": 16,
        },
        "failure_modes": [
            {
                "mode": "InnoDB Buffer Pool churn",
                "impact": "Frequent disk read I/O bottlenecks causing query stalls.",
                "mitigation": "Size innodb_buffer_pool_size to 70-80% of total system RAM.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/instance-month",
            "base_monthly_usd": 28.0,
            "free_tier": "PlanetScale / Aiven free tier",
            "notes": "Scales by CPU, RAM, and IOPS provisioned.",
        },
        "alternatives": ["postgresql", "cockroachdb"],
    },
    {
        "slug": "cockroachdb",
        "name": "CockroachDB Distributed SQL",
        "category": "database",
        "layer": "data",
        "description": "Cloud-native distributed SQL database providing serializable ACID transactions, automatic horizontal sharding, and multi-region resilience.",
        "protocols": ["TCP", "SQL (Postgres-compatible)"],
        "limits": {
            "max_throughput_qps": 80000,
            "connection_limit": 10000,
            "latency_p99_ms": 30,
            "storage_capacity_tb": 100,
        },
        "failure_modes": [
            {
                "mode": "Raft consensus round-trip latency in cross-region writes",
                "impact": "High p99 write latency (100ms+) when quorum spans continents.",
                "mitigation": "Configure regional tables or locality-aware routing rules.",
            },
            {
                "mode": "Transaction retry storms under hot-row contention",
                "impact": "Transaction rollback cascades due to serializable conflict detection.",
                "mitigation": "Avoid single-row counters; use batching or distributed counter patterns.",
            },
        ],
        "cost_units": {
            "model": "serverless_or_provisioned",
            "unit": "$/Request Unit (RU) + $/GB storage",
            "base_monthly_usd": 0.0,
            "free_tier": "50M Request Units (RUs) and 10GB storage free every month",
            "notes": "Serverless tier has excellent free quota.",
        },
        "alternatives": ["postgresql", "amazon-dynamodb"],
    },
    # --- NoSQL & Document & Graph Databases ---
    {
        "slug": "mongodb",
        "name": "MongoDB Document Database",
        "category": "database",
        "layer": "data",
        "description": "Document-oriented NoSQL database storing flexible BSON documents with rich indexing, aggregation, and replica sets.",
        "protocols": ["TCP", "MongoDB Wire Protocol"],
        "limits": {
            "max_throughput_qps": 30000,
            "connection_limit": 1500,
            "latency_p99_ms": 10,
            "max_document_size_mb": 16,
        },
        "failure_modes": [
            {
                "mode": "Unindexed query collection scans (COLLSCAN)",
                "impact": "CPU utilization spikes to 100%, starving normal operations.",
                "mitigation": "Mandate compound indexes, enable query profiler alerts.",
            },
            {
                "mode": "Primary failover election pause",
                "impact": "Writes rejected for 2-5 seconds during replica set election.",
                "mitigation": "Use retryable writes in client driver (retryWrites=true).",
            },
        ],
        "cost_units": {
            "model": "provisioned_or_cloud",
            "unit": "$/cluster-month",
            "base_monthly_usd": 25.0,
            "free_tier": "MongoDB Atlas M0 sandbox provides 512MB free forever",
            "notes": "Cost scales with Atlas cluster tier (M10, M20, M30).",
        },
        "alternatives": ["amazon-dynamodb", "postgresql"],
    },
    {
        "slug": "amazon-dynamodb",
        "name": "Amazon DynamoDB Key-Value & Document DB",
        "category": "database",
        "layer": "data",
        "description": "Serverless NoSQL database engineered for single-digit millisecond latency at any scale with automatic horizontal partitioning.",
        "protocols": ["HTTPS", "AWS SDK"],
        "limits": {
            "max_throughput_qps": 200000,
            "latency_p99_ms": 6,
            "max_item_size_kb": 400,
            "partition_key_rcu_limit": 3000,
            "partition_key_wcu_limit": 1000,
        },
        "failure_modes": [
            {
                "mode": "Hot partition throttling (HTTP 400 ProvisionedThroughputExceeded)",
                "impact": "Write requests for a specific key get rejected or queued.",
                "mitigation": "Design partition keys with high cardinality or add synthetic salt suffixes.",
            },
            {
                "mode": "Item size limit exceeded (>400KB)",
                "impact": "Write fails outright.",
                "mitigation": "Store heavy payloads in S3 and store the S3 object key in DynamoDB.",
            },
        ],
        "cost_units": {
            "model": "serverless_pay_per_request",
            "unit": "$1.25 per 1M write units, $0.25 per 1M read units",
            "base_monthly_usd": 0.0,
            "free_tier": "25GB storage + 25 provisioned WCU and 25 RCU free forever",
            "notes": "Generous free tier covers low-to-medium volume systems.",
        },
        "alternatives": ["cassandra", "mongodb", "redis-cache"],
    },
    {
        "slug": "apache-cassandra",
        "name": "Apache Cassandra Distributed Wide-Column Store",
        "category": "database",
        "layer": "data",
        "description": "Masterless distributed database offering linear scalability, high write throughput, and zero single point of failure.",
        "protocols": ["CQL", "TCP"],
        "limits": {
            "max_throughput_qps": 150000,
            "connection_limit": 5000,
            "latency_p99_ms": 10,
            "storage_capacity_tb": 200,
        },
        "failure_modes": [
            {
                "mode": "Tombstone saturation leading to ReadTimeoutException",
                "impact": "Queries scanning deleted rows exceed 100,000 tombstone threshold and crash.",
                "mitigation": "Avoid anti-pattern deletes; tune gc_grace_seconds.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/node-month",
            "base_monthly_usd": 60.0,
            "free_tier": "Astra DB provides $25/mo free credit",
            "notes": "Demands multi-node cluster (at least 3 nodes) for quorum replication.",
        },
        "alternatives": ["amazon-dynamodb", "scylladb"],
    },
    {
        "slug": "neo4j",
        "name": "Neo4j Graph Database",
        "category": "database",
        "layer": "data",
        "description": "Native graph database designed for traversing deep relationship networks, friend recommendations, and fraud rings.",
        "protocols": ["Bolt", "HTTPS"],
        "limits": {
            "max_throughput_qps": 15000,
            "latency_p99_ms": 20,
            "storage_capacity_tb": 10,
        },
        "failure_modes": [
            {
                "mode": "Graph supernode traversal blowup",
                "impact": "Traversing nodes with millions of edges exhausts memory and hangs query.",
                "mitigation": "Edge filtering by relationship type, index lookups, limiting hop depth.",
            }
        ],
        "cost_units": {
            "model": "provisioned_or_cloud",
            "unit": "$/instance-month",
            "base_monthly_usd": 65.0,
            "free_tier": "Neo4j AuraDB Free tier (up to 200k nodes & 400k relationships)",
            "notes": "RAM-intensive for caching graph topology in memory.",
        },
        "alternatives": ["amazon-neptune", "postgresql"],
    },
    # --- Search ---
    {
        "slug": "elasticsearch",
        "name": "Elasticsearch Full-Text Search & Analytics",
        "category": "search",
        "layer": "data",
        "description": "Distributed RESTful search engine built on Apache Lucene for inverted index search, geo-distance queries, and aggregations.",
        "protocols": ["HTTP", "REST"],
        "limits": {
            "max_throughput_qps": 25000,
            "latency_p99_ms": 25,
            "max_docs_per_shard": 2147483647,
            "storage_capacity_tb": 50,
        },
        "failure_modes": [
            {
                "mode": "Heap pressure & GC freeze during heavy aggregations",
                "impact": "Cluster nodes disconnect causing unassigned shards and red cluster status.",
                "mitigation": "Cap JVM heap at 31GB, use circuit breakers, offload heavy filters.",
            },
            {
                "mode": "Split-brain cluster partition",
                "impact": "Conflicting data states across network partitions.",
                "mitigation": "Maintain odd number of dedicated master nodes (cluster.initial_master_nodes).",
            },
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/node-month",
            "base_monthly_usd": 45.0,
            "free_tier": "Self-hosted OSS or OpenSearch",
            "notes": "RAM and SSD storage intensive; minimum 2-3 nodes for high availability.",
        },
        "alternatives": ["meilisearch", "opensearch", "typesense"],
    },
    {
        "slug": "meilisearch",
        "name": "Meilisearch Fast Typo-Tolerant Search",
        "category": "search",
        "layer": "data",
        "description": "Lightweight, lightning-fast typo-tolerant search engine optimized for interactive frontend search-as-you-type bars.",
        "protocols": ["HTTP", "REST"],
        "limits": {
            "max_throughput_qps": 12000,
            "latency_p99_ms": 10,
            "max_database_size_gb": 100,
        },
        "failure_modes": [
            {
                "mode": "LMDB virtual memory space exhaustion",
                "impact": "Indexer fails to commit document additions.",
                "mitigation": "Configure max_indexing_memory and index in manageable batches.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/instance-month",
            "base_monthly_usd": 20.0,
            "free_tier": "Free open-source binary; Meilisearch Cloud free trial",
            "notes": "Significantly easier to operate and lower RAM consumption than Elasticsearch.",
        },
        "alternatives": ["elasticsearch", "typesense"],
    },
    # --- Streaming & Queues ---
    {
        "slug": "apache-kafka",
        "name": "Apache Kafka Event Streaming Platform",
        "category": "streaming",
        "layer": "async",
        "description": "High-throughput distributed append-only commit log for event sourcing, stream processing, and real-time pub/sub.",
        "protocols": ["Kafka Protocol", "TCP"],
        "limits": {
            "max_throughput_qps": 200000,
            "latency_p99_ms": 8,
            "max_message_size_mb": 10,
            "retention_period_days": 30,
        },
        "failure_modes": [
            {
                "mode": "Consumer group rebalance storm",
                "impact": "Message consumption freezes during rebalancing when consumers lag or crash.",
                "mitigation": "Tune max.poll.interval.ms and enable static group membership.",
            },
            {
                "mode": "Disk saturation from unpruned topic retention",
                "impact": "Brokers halt writes to avoid log corruption.",
                "mitigation": "Configure retention.bytes and retention.ms with disk space alerting.",
            },
        ],
        "cost_units": {
            "model": "provisioned_or_cloud",
            "unit": "$/broker-month + $/GB ingress",
            "base_monthly_usd": 50.0,
            "free_tier": "Confluent Cloud provides $400 free credit or Upstash Kafka free tier",
            "notes": "KRaft mode simplifies deployment by eliminating ZooKeeper.",
        },
        "alternatives": ["rabbitmq", "aws-sqs", "apache-pulsar"],
    },
    {
        "slug": "rabbitmq",
        "name": "RabbitMQ Message Broker",
        "category": "queue",
        "layer": "async",
        "description": "Flexible, AMQP-compliant message broker offering complex routing keys, fanout exchanges, topic subscriptions, and dead-lettering.",
        "protocols": ["AMQP 0-9-1", "MQTT", "STOMP"],
        "limits": {
            "max_throughput_qps": 50000,
            "connection_limit": 20000,
            "latency_p99_ms": 5,
        },
        "failure_modes": [
            {
                "mode": "Queue memory alarm (broker throttling)",
                "impact": "RabbitMQ blocks all publisher connections when RAM reaches 40% threshold.",
                "mitigation": "Use Quorum Queues, configure Lazy Queues to page messages to disk.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/instance-month",
            "base_monthly_usd": 25.0,
            "free_tier": "CloudAMQP Little Lemur plan is free (1M messages/month)",
            "notes": "Low latency message delivery for transactional tasks.",
        },
        "alternatives": ["aws-sqs", "apache-kafka"],
    },
    {
        "slug": "aws-sqs",
        "name": "Amazon Simple Queue Service (SQS)",
        "category": "queue",
        "layer": "async",
        "description": "Fully managed distributed message queuing service providing standard (at-least-once) and FIFO (exactly-once) queues.",
        "protocols": ["HTTPS", "AWS SDK"],
        "limits": {
            "max_throughput_qps": 100000,
            "max_message_size_kb": 256,
            "retention_period_days": 14,
            "visibility_timeout_seconds": 43200,
            "latency_p99_ms": 25,
        },
        "failure_modes": [
            {
                "mode": "Poison pill message loop",
                "impact": "Corrupt payload causes worker crash repeatedly, stalling processing.",
                "mitigation": "Configure Dead Letter Queue (DLQ) with maxReceiveCount=3.",
            }
        ],
        "cost_units": {
            "model": "serverless",
            "unit": "$0.40 per 1M requests",
            "base_monthly_usd": 0.0,
            "free_tier": "1M requests free per month permanently",
            "notes": "Extremely cost-effective for asynchronous decoupling with zero maintenance.",
        },
        "alternatives": ["rabbitmq", "redis-pubsub"],
    },
    # --- Messaging & Notifications ---
    {
        "slug": "redis-pubsub",
        "name": "Redis Pub/Sub & Stream Dispatcher",
        "category": "notification",
        "layer": "async",
        "description": "Ultra-fast fire-and-forget message publication and channel distribution mechanism across backend processes.",
        "protocols": ["RESP", "TCP"],
        "limits": {
            "max_throughput_qps": 100000,
            "connection_limit": 10000,
            "latency_p99_ms": 1,
        },
        "failure_modes": [
            {
                "mode": "Slow subscriber client output buffer overflow",
                "impact": "Redis forcibly disconnects slow consumers, causing dropped messages.",
                "mitigation": "Tune client-output-buffer-limit pubsub, or use Redis Streams with consumer groups.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "Included in Redis Cache instance cost",
            "base_monthly_usd": 0.0,
            "free_tier": "Included with Redis cache",
            "notes": "Shares compute with Redis instance.",
        },
        "alternatives": ["aws-sns", "rabbitmq"],
    },
    {
        "slug": "aws-sns",
        "name": "Amazon Simple Notification Service (SNS)",
        "category": "notification",
        "layer": "async",
        "description": "High-throughput managed pub/sub messaging service for fanout message delivery to SQS queues, Lambda functions, and webhooks.",
        "protocols": ["HTTPS", "AWS SDK"],
        "limits": {
            "max_throughput_qps": 100000,
            "max_message_size_kb": 256,
            "latency_p99_ms": 30,
        },
        "failure_modes": [
            {
                "mode": "HTTP endpoint endpoint delivery backpressure",
                "impact": "Webhook subscriber failure causes delivery retry queue backlog.",
                "mitigation": "Fan out SNS topics to SQS queues rather than hitting HTTP endpoints directly.",
            }
        ],
        "cost_units": {
            "model": "serverless",
            "unit": "$0.50 per 1M publish requests",
            "base_monthly_usd": 0.0,
            "free_tier": "1M publishes and 100,000 HTTP/S notifications free each month",
            "notes": "Cost-effective for high-fanout architecture.",
        },
        "alternatives": ["redis-pubsub", "firebase-fcm"],
    },
    {
        "slug": "firebase-fcm",
        "name": "Firebase Cloud Messaging (FCM)",
        "category": "notification",
        "layer": "edge",
        "description": "Cross-platform messaging solution to reliably send push notifications to iOS, Android, and Web clients.",
        "protocols": ["HTTPS", "HTTP/2"],
        "limits": {
            "max_throughput_qps": 20000,
            "latency_p99_ms": 150,
            "max_payload_size_kb": 4,
        },
        "failure_modes": [
            {
                "mode": "Invalid / Expired registration tokens",
                "impact": "Failed notification deliveries and HTTP 404/410 errors.",
                "mitigation": "Prune unregistered device tokens from database upon receiving canonical errors.",
            }
        ],
        "cost_units": {
            "model": "serverless",
            "unit": "Free unlimited push notifications",
            "base_monthly_usd": 0.0,
            "free_tier": "Completely free for push message delivery",
            "notes": "Google provides FCM at zero direct cost.",
        },
        "alternatives": ["onesignal", "aws-sns"],
    },
    # --- Object & File Storage ---
    {
        "slug": "aws-s3",
        "name": "Amazon Simple Storage Service (S3)",
        "category": "storage",
        "layer": "data",
        "description": "Industry-standard scalable object storage offering 99.999999999% (11 9s) data durability, versioning, and presigned URLs.",
        "protocols": ["HTTPS", "S3 REST API"],
        "limits": {
            "max_throughput_qps": 3500,
            "max_object_size_tb": 5,
            "latency_p99_ms": 30,
        },
        "failure_modes": [
            {
                "mode": "Prefix write throttling (HTTP 503 Slow Down)",
                "impact": "Uploads fail when hitting >3,500 PUT or 5,500 GET requests per second per prefix.",
                "mitigation": "Partition object keys using hash prefixes or UUIDs.",
            },
            {
                "mode": "Unexpected egress cost shock",
                "impact": "Viral asset downloads generate huge bandwidth bills.",
                "mitigation": "Serve public S3 objects exclusively through CloudFront or Cloudflare CDN.",
            },
        ],
        "cost_units": {
            "model": "usage_storage_and_transfer",
            "unit": "$0.023/GB-month storage + $0.09/GB egress",
            "base_monthly_usd": 0.0,
            "free_tier": "5GB standard storage + 20,000 GET requests free for 12 months",
            "notes": "Primary cost driver is data egress; mitigate with CDN.",
        },
        "alternatives": ["cloudflare-r2", "minio"],
    },
    {
        "slug": "cloudflare-r2",
        "name": "Cloudflare R2 Object Storage",
        "category": "storage",
        "layer": "data",
        "description": "S3-compatible object storage featuring zero egress bandwidth fees and native Cloudflare edge caching integration.",
        "protocols": ["HTTPS", "S3 REST API"],
        "limits": {
            "max_throughput_qps": 5000,
            "max_object_size_tb": 5,
            "latency_p99_ms": 25,
        },
        "failure_modes": [
            {
                "mode": "Eventual consistency edge replication lag",
                "impact": "Immediate read after overwrite may return old metadata for ~seconds.",
                "mitigation": "Use immutable key generation (e.g. UUIDs or content hashes) rather than in-place overwrites.",
            }
        ],
        "cost_units": {
            "model": "usage_storage",
            "unit": "$0.015/GB-month storage + $0.00 egress",
            "base_monthly_usd": 0.0,
            "free_tier": "10GB storage + 1M Class A operations free per month",
            "notes": "Zero egress fees make it ideal for user avatars and image uploads.",
        },
        "alternatives": ["aws-s3", "minio"],
    },
    {
        "slug": "minio",
        "name": "MinIO High-Performance Object Storage",
        "category": "storage",
        "layer": "data",
        "description": "Open-source S3-compatible self-hosted object store built for on-premise, edge, and private cloud deployments.",
        "protocols": ["HTTPS", "S3 REST API"],
        "limits": {
            "max_throughput_qps": 10000,
            "latency_p99_ms": 15,
            "storage_capacity_tb": 50,
        },
        "failure_modes": [
            {
                "mode": "Drive drive corruption / bit rot",
                "impact": "Potential data loss if redundancy threshold breached.",
                "mitigation": "Enable erasure coding across minimum 4 drives per pool.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/instance-month (hardware bound)",
            "base_monthly_usd": 20.0,
            "free_tier": "AGPLv3 open-source binary free to self-host",
            "notes": "Zero vendor lock-in S3 API alternative.",
        },
        "alternatives": ["aws-s3", "cloudflare-r2"],
    },
    # --- Observability ---
    {
        "slug": "prometheus-grafana",
        "name": "Prometheus & Grafana Observability",
        "category": "observability",
        "layer": "observability",
        "description": "Time-series monitoring, scrape metrics collector, alerting engine, and customizable visualization dashboards.",
        "protocols": ["HTTP", "PromQL"],
        "limits": {
            "max_samples_per_second": 1000000,
            "retention_period_days": 15,
            "latency_p99_ms": 10,
        },
        "failure_modes": [
            {
                "mode": "High cardinality metric explosion",
                "impact": "Prometheus runs out of RAM and crashes (OOM loop).",
                "mitigation": "Avoid raw user IDs or UUIDs in metric label dimensions.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/instance-month",
            "base_monthly_usd": 25.0,
            "free_tier": "Grafana Cloud free tier provides 10k metrics & 50GB logs",
            "notes": "Self-hosted OSS on small VPS is cost effective.",
        },
        "alternatives": ["datadog", "newrelic"],
    },
    {
        "slug": "opentelemetry-collector",
        "name": "OpenTelemetry Collector",
        "category": "observability",
        "layer": "observability",
        "description": "Vendor-agnostic proxy that receives, processes, filters, batches, and exports telemetry data (traces, metrics, logs).",
        "protocols": ["OTLP/gRPC", "OTLP/HTTP"],
        "limits": {
            "max_throughput_qps": 50000,
            "latency_p99_ms": 2,
        },
        "failure_modes": [
            {
                "mode": "Memory queue overflow on downstream exporter outage",
                "impact": "Telemetry spans dropped when memory buffer reaches memory_limiter threshold.",
                "mitigation": "Configure memory_limiter processor and batch processor with retry_on_failure.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/container-month",
            "base_monthly_usd": 15.0,
            "free_tier": "CNCF open source",
            "notes": "Lightweight sidecar or daemonset.",
        },
        "alternatives": ["prometheus-grafana", "jaeger"],
    },
    # --- Middleware & Workflow & Analytics ---
    {
        "slug": "pgbouncer",
        "name": "PgBouncer PostgreSQL Connection Pooler",
        "category": "middleware",
        "layer": "data",
        "description": "Lightweight connection pooler for PostgreSQL reducing backend connection overhead from thousands of app threads to a tight pool.",
        "protocols": ["TCP", "PostgreSQL Wire Protocol"],
        "limits": {
            "max_client_connections": 10000,
            "max_server_connections": 200,
            "latency_p99_ms": 1,
        },
        "failure_modes": [
            {
                "mode": "Session-level pinning conflict under transaction pooling mode",
                "impact": "Prepared statements or advisory locks leak across pooled sessions.",
                "mitigation": "Use transaction pooling mode and configure client drivers to discard session-level state.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/container-month",
            "base_monthly_usd": 10.0,
            "free_tier": "Open source; negligible RAM (~20MB)",
            "notes": "Essential companion to PostgreSQL under microservice traffic.",
        },
        "alternatives": ["aws-rds-proxy", "odyssey"],
    },
    {
        "slug": "temporal-orchestrator",
        "name": "Temporal Durable Workflow Orchestrator",
        "category": "workflow",
        "layer": "async",
        "description": "Durable execution platform executing long-running distributed stateful workflows, compensation sagas, and retries safely.",
        "protocols": ["gRPC", "HTTPS"],
        "limits": {
            "max_throughput_qps": 10000,
            "latency_p99_ms": 20,
            "history_size_limit_mb": 50,
        },
        "failure_modes": [
            {
                "mode": "Workflow history event limit exceeded (>50k events)",
                "impact": "Workflow performance degrades and terminates with history size error.",
                "mitigation": "Implement continue-as-new pattern to reset workflow execution history.",
            }
        ],
        "cost_units": {
            "model": "provisioned_or_cloud",
            "unit": "$/instance-month",
            "base_monthly_usd": 40.0,
            "free_tier": "Temporal OSS is free; Temporal Cloud offers trial",
            "notes": "Eliminates complex distributed saga code in application layer.",
        },
        "alternatives": ["celery-worker", "aws-step-functions"],
    },
    {
        "slug": "clickhouse-olap",
        "name": "ClickHouse Analytical Columnar DB",
        "category": "analytics",
        "layer": "data",
        "description": "Blazing-fast columnar database management system for real-time analytical reporting, user activity logs, and clickstreams.",
        "protocols": ["TCP", "HTTP", "SQL"],
        "limits": {
            "max_throughput_qps": 50000,
            "insert_throughput_rows_sec": 1000000,
            "latency_p99_ms": 25,
            "storage_capacity_tb": 100,
        },
        "failure_modes": [
            {
                "mode": "Too many parts exception on high-frequency single row inserts",
                "impact": "Server rejects inserts when background part merges cannot keep up.",
                "mitigation": "Batch inserts into chunks of at least 1,000-10,000 rows or buffer via Kafka/Vector.",
            }
        ],
        "cost_units": {
            "model": "provisioned",
            "unit": "$/instance-month",
            "base_monthly_usd": 45.0,
            "free_tier": "Open source OSS; ClickHouse Cloud trial",
            "notes": "100x faster than traditional row DBs for aggregation queries.",
        },
        "alternatives": ["snowflake", "google-bigquery"],
    },
]

# Key architectural compatibility edges (both valid connections and flagged antipatterns)
SEED_COMPATIBILITIES: list[dict[str, Any]] = [
    # --- Edge to Gateways ---
    {
        "source_slug": "cloudflare-cdn",
        "target_slug": "nginx-reverse-proxy",
        "is_compatible": True,
        "protocol": "HTTPS",
        "recommended_pattern": "Origin Shielding & Strict TLS",
        "constraints": {"max_payload_size_mb": 100},
        "reason": "Edge CDN efficiently terminates global TLS and forwards cached misses to origin NGINX proxy.",
    },
    {
        "source_slug": "cloudflare-cdn",
        "target_slug": "kong-api-gateway",
        "is_compatible": True,
        "protocol": "HTTPS",
        "recommended_pattern": "WAF to API Gateway",
        "constraints": {"max_payload_size_mb": 40},
        "reason": "Cloudflare absorbs edge traffic and routes authenticated API calls to Kong Gateway.",
    },
    {
        "source_slug": "cloudflare-cdn",
        "target_slug": "aws-api-gateway",
        "is_compatible": True,
        "protocol": "HTTPS",
        "recommended_pattern": "Custom Domain TLS Proxy",
        "constraints": {"timeout_seconds": 29},
        "reason": "Cloudflare CDN fronts AWS API Gateway with custom edge rules and DDoS filtering.",
    },
    {
        "source_slug": "aws-cloudfront",
        "target_slug": "aws-api-gateway",
        "is_compatible": True,
        "protocol": "HTTPS",
        "recommended_pattern": "Native Regional API Origin",
        "constraints": {"timeout_seconds": 29},
        "reason": "Direct native AWS backbone integration between CloudFront and API Gateway.",
    },
    {
        "source_slug": "aws-cloudfront",
        "target_slug": "aws-s3",
        "is_compatible": True,
        "protocol": "HTTPS",
        "recommended_pattern": "Origin Access Control (OAC)",
        "constraints": {"enforce_private_bucket": True},
        "reason": "CloudFront serves S3 assets securely without public bucket access, slashing egress bandwidth costs.",
    },
    {
        "source_slug": "cloudflare-cdn",
        "target_slug": "cloudflare-r2",
        "is_compatible": True,
        "protocol": "HTTPS",
        "recommended_pattern": "Direct Cloudflare Edge Binding",
        "constraints": {"zero_egress": True},
        "reason": "Zero egress bandwidth cost caching pipeline between Cloudflare CDN and R2 object storage.",
    },
    # --- Antipattern: Edge directly to Database / Cache ---
    {
        "source_slug": "cloudflare-cdn",
        "target_slug": "postgresql",
        "is_compatible": False,
        "protocol": "None",
        "recommended_pattern": "Application API Layer Required",
        "constraints": {},
        "reason": "CRITICAL ANTIPATTERN: Public edge CDNs must never terminate directly against internal relational databases. Lacks authentication, connection pooling, and business validation.",
    },
    {
        "source_slug": "aws-cloudfront",
        "target_slug": "postgresql",
        "is_compatible": False,
        "protocol": "None",
        "recommended_pattern": "Application API Layer Required",
        "constraints": {},
        "reason": "CRITICAL ANTIPATTERN: Edge CDNs cannot query relational databases directly without an intermediate application layer.",
    },
    {
        "source_slug": "cloudflare-cdn",
        "target_slug": "redis-cache",
        "is_compatible": False,
        "protocol": "None",
        "recommended_pattern": "Application / API Gateway Required",
        "constraints": {},
        "reason": "ANTIPATTERN: In-memory cache must not be directly exposed to public CDN traffic without auth middleware.",
    },
    # --- Gateways to Compute ---
    {
        "source_slug": "nginx-reverse-proxy",
        "target_slug": "fastapi-app-server",
        "is_compatible": True,
        "protocol": "HTTP/1.1",
        "recommended_pattern": "Unix Domain Socket or Keep-Alive Reverse Proxy",
        "constraints": {"client_max_body_size_mb": 32},
        "reason": "Standard production deployment: NGINX buffers requests, manages slow clients, and proxies to Uvicorn/FastAPI.",
    },
    {
        "source_slug": "nginx-reverse-proxy",
        "target_slug": "node-express-server",
        "is_compatible": True,
        "protocol": "HTTP/1.1",
        "recommended_pattern": "Round-Robin Cluster Proxy",
        "constraints": {},
        "reason": "NGINX load-balances HTTP requests across multiple Node.js process instances.",
    },
    {
        "source_slug": "kong-api-gateway",
        "target_slug": "fastapi-app-server",
        "is_compatible": True,
        "protocol": "HTTP/REST",
        "recommended_pattern": "Authenticated Downstream Upstream",
        "constraints": {},
        "reason": "Kong verifies JWT and rate limits before routing clean requests to FastAPI.",
    },
    {
        "source_slug": "kong-api-gateway",
        "target_slug": "jwt-auth-service",
        "is_compatible": True,
        "protocol": "HTTP/REST",
        "recommended_pattern": "Forward Auth / Token Verification",
        "constraints": {"cache_jwks": True},
        "reason": "Kong queries Auth service for token validation or caches JWKS public keys.",
    },
    {
        "source_slug": "websocket-gateway",
        "target_slug": "redis-pubsub",
        "is_compatible": True,
        "protocol": "RESP",
        "recommended_pattern": "Horizontal WebSocket Pub/Sub Fanout",
        "constraints": {"buffer_size_mb": 64},
        "reason": "WebSocket gateway nodes subscribe to Redis channels to deliver messages to clients connected to any node.",
    },
    # --- Compute to Data & Storage ---
    {
        "source_slug": "fastapi-app-server",
        "target_slug": "postgresql",
        "is_compatible": True,
        "protocol": "TCP/SQL",
        "recommended_pattern": "Connection Pooler (PgBouncer) Recommended",
        "constraints": {"max_connections": 20, "pool_size": 10},
        "reason": "Async SQLAlchemy connects over TCP to PostgreSQL. High instance counts should place PgBouncer in between.",
    },
    {
        "source_slug": "fastapi-app-server",
        "target_slug": "pgbouncer",
        "is_compatible": True,
        "protocol": "TCP/SQL",
        "recommended_pattern": "Transaction-Level Connection Pooling",
        "constraints": {"pool_mode": "transaction"},
        "reason": "FastAPI connects to PgBouncer to eliminate connection limits on PostgreSQL primary.",
    },
    {
        "source_slug": "pgbouncer",
        "target_slug": "postgresql",
        "is_compatible": True,
        "protocol": "TCP/SQL",
        "recommended_pattern": "Multiplexed Server Connection Pool",
        "constraints": {"max_server_connections": 100},
        "reason": "PgBouncer maintains small, healthy long-lived connection pool to PostgreSQL server.",
    },
    {
        "source_slug": "fastapi-app-server",
        "target_slug": "redis-cache",
        "is_compatible": True,
        "protocol": "RESP",
        "recommended_pattern": "Cache-Aside / Read-Through",
        "constraints": {"default_ttl_seconds": 3600},
        "reason": "FastAPI checks Redis before querying DB, storing serialized JSON or msgpack with TTL.",
    },
    {
        "source_slug": "fastapi-app-server",
        "target_slug": "aws-s3",
        "is_compatible": True,
        "protocol": "HTTPS (S3 SDK)",
        "recommended_pattern": "Presigned Upload & Download URLs",
        "constraints": {"presigned_url_expiry_seconds": 900},
        "reason": "FastAPI generates temporary presigned S3 URLs so clients upload avatars/media directly to S3 without bottlenecking backend memory.",
    },
    {
        "source_slug": "fastapi-app-server",
        "target_slug": "rabbitmq",
        "is_compatible": True,
        "protocol": "AMQP 0-9-1",
        "recommended_pattern": "Transactional Outbox / Publisher Confirmations",
        "constraints": {"publisher_confirms": True},
        "reason": "FastAPI pushes background job messages to RabbitMQ with publisher confirms.",
    },
    {
        "source_slug": "fastapi-app-server",
        "target_slug": "apache-kafka",
        "is_compatible": True,
        "protocol": "Kafka Protocol",
        "recommended_pattern": "Transactional Event Producer",
        "constraints": {"acks": "all", "idempotence": True},
        "reason": "FastAPI publishes domain events (e.g. UserSwiped, MatchCreated) to Kafka topic partitions.",
    },
    {
        "source_slug": "fastapi-app-server",
        "target_slug": "elasticsearch",
        "is_compatible": True,
        "protocol": "HTTP/REST",
        "recommended_pattern": "Search-Only Index Querying",
        "constraints": {"read_timeout_seconds": 3},
        "reason": "FastAPI queries Elasticsearch for complex full-text search, filtering, and geolocation queries.",
    },
    {
        "source_slug": "fastapi-app-server",
        "target_slug": "amazon-dynamodb",
        "is_compatible": True,
        "protocol": "HTTPS",
        "recommended_pattern": "Single-Table Design Key-Value Lookups",
        "constraints": {"max_item_size_kb": 400},
        "reason": "FastAPI queries DynamoDB for ultra-low latency key-value lookups (e.g. user session or swiped status).",
    },
    # --- Async Workers & Pipelines ---
    {
        "source_slug": "celery-worker",
        "target_slug": "rabbitmq",
        "is_compatible": True,
        "protocol": "AMQP 0-9-1",
        "recommended_pattern": "Prefetch-Optimized Task Consumer",
        "constraints": {"worker_prefetch_multiplier": 1},
        "reason": "Celery worker processes consume tasks from RabbitMQ queues.",
    },
    {
        "source_slug": "celery-worker",
        "target_slug": "redis-cache",
        "is_compatible": True,
        "protocol": "RESP",
        "recommended_pattern": "Task Result Backend & Lock Coordinator",
        "constraints": {"result_expires_seconds": 86400},
        "reason": "Celery stores task status/results in Redis and coordinates distributed locks.",
    },
    {
        "source_slug": "celery-worker",
        "target_slug": "postgresql",
        "is_compatible": True,
        "protocol": "TCP/SQL",
        "recommended_pattern": "Batch Write Upserts",
        "constraints": {"batch_size": 500},
        "reason": "Worker updates user states and records transactional completions in PostgreSQL.",
    },
    {
        "source_slug": "celery-worker",
        "target_slug": "firebase-fcm",
        "is_compatible": True,
        "protocol": "HTTPS",
        "recommended_pattern": "Batch Push Notification Dispatcher",
        "constraints": {"batch_limit": 500},
        "reason": "Celery workers send push notifications to user devices via Firebase Cloud Messaging upon events (e.g. new match).",
    },
    # --- Antipattern: Database directly to Queue without Outbox/CDC ---
    {
        "source_slug": "postgresql",
        "target_slug": "apache-kafka",
        "is_compatible": False,
        "protocol": "None",
        "recommended_pattern": "Debezium / CDC Outbox Connector Required",
        "constraints": {},
        "reason": "ANTIPATTERN: Relational databases cannot push directly to Kafka topics without a Change Data Capture (CDC) agent like Debezium or application-level transactional outbox.",
    },
    {
        "source_slug": "postgresql",
        "target_slug": "rabbitmq",
        "is_compatible": False,
        "protocol": "None",
        "recommended_pattern": "Transactional Outbox Pattern Required",
        "constraints": {},
        "reason": "ANTIPATTERN: Database engines do not push directly to message queues. Dual writes without transactional outbox cause data inconsistency.",
    },
    # --- Observability Integrations ---
    {
        "source_slug": "fastapi-app-server",
        "target_slug": "opentelemetry-collector",
        "is_compatible": True,
        "protocol": "OTLP/gRPC",
        "recommended_pattern": "Asynchronous Batch Trace Export",
        "constraints": {"batch_timeout_ms": 5000},
        "reason": "FastAPI instruments requests and exports distributed traces and latency metrics to OTel collector.",
    },
    {
        "source_slug": "opentelemetry-collector",
        "target_slug": "prometheus-grafana",
        "is_compatible": True,
        "protocol": "PromQL / Prometheus Remote Write",
        "recommended_pattern": "Metrics Pipeline Forwarder",
        "constraints": {},
        "reason": "OTel collector aggregates and converts spans/metrics into Prometheus scrape targets.",
    },
]
