# System Design Primer — Extracted Notes

Source: [donnemartin/system-design-primer](https://github.com/donnemartin/system-design-primer)

This file extracts the repository’s README structure, reusable system-design templates, and architecture-diagram references into a single Markdown study document.

## 1. Repository Overview

- **Purpose:** Learn how to design large-scale systems and prepare for system-design interviews.
- **Core idea:** System design is about trade-offs; the repository organizes principles, patterns, interview questions, solutions, and diagrams.
- **Main folders:**
  - `README.md` — primary study guide and topic index.
  - `solutions/` — exercise prompts, sample discussions, code, and architecture diagrams.
  - `images/` — diagram assets referenced by the README and solutions.
  - `resources/` — supplementary learning resources.
- **Extras:** Anki decks for system design, system-design exercises, and object-oriented design exercises.

## 2. What to Extract

| Asset | Location | Use |
|---|---|---|
| Main README | `README.md` | Core concepts, study guide, interview framework |
| System-design templates | `solutions/system_design/` | Reusable requirement, estimation, API, data-model, and scaling templates |
| Interview solutions | `solutions/system_design/pastebin/`, `twitter/`, `web_crawler/`, etc. | Worked examples with diagrams and code |
| OO-design templates | `solutions/object_oriented_design/` | Class-design and requirements templates |
| Architecture diagrams | `images/` and solution folders | Visual references for load balancing, caching, replication, sharding, and complete systems |

## 3. System Design Interview Template

Use this template for any open-ended design question.

### Step 1 — Clarify requirements

- Identify users and primary use cases.
- Define functional requirements.
- Define non-functional requirements: scale, latency, availability, consistency, security, and cost.
- State explicit assumptions.

Key questions:

- Who uses the system?
- What are the inputs and outputs?
- How many users and requests per second are expected?
- What is the read/write ratio?
- How much data must be stored?
- What latency and availability targets matter?

### Step 2 — Back-of-the-envelope estimates

Estimate before designing.

- Daily active users
- Requests per second
- Storage per record and total storage
- Bandwidth
- Cache memory
- Number of servers

Useful references in the repo:

- Powers-of-two table
- Latency numbers every programmer should know
- Back-of-the-envelope calculations

### Step 3 — High-level architecture

Sketch the main components and connections:

```text
Client
  -> DNS / CDN
  -> Load Balancer
  -> Web / API servers
  -> Application services
  -> Cache
  -> Database / object storage
  -> Queue and workers
```

Justify each component and explain how requests flow through the system.

### Step 4 — API design

Define the main endpoints, request/response shapes, authentication, pagination, and error handling.

Example:

```http
POST /urls
Request:  { "long_url": "https://example.com/very/long/path" }
Response: { "short_url": "https://short.io/abc123" }

GET /abc123
Response: 301 Redirect to the original URL
```

### Step 5 — Data model

Choose a storage model based on access patterns.

- **Relational database:** structured data, transactions, joins, strong consistency.
- **Key-value store:** simple lookups, caching, sessions.
- **Document store:** flexible schemas and nested objects.
- **Wide-column store:** very large write-heavy datasets.
- **Graph database:** relationships and traversals.
- **Object storage:** images, videos, backups, and large files.

Include:

- Entities and fields
- Primary keys
- Indexes
- Relationships
- Partition or shard key
- Retention and archival strategy

### Step 6 — Deep-dive core components

For a URL shortener, for example:

- Short-code generation: hashing, Base62 encoding, collision handling
- Redirect lookup: cache-first strategy, database fallback
- Analytics: asynchronous event ingestion
- Expiration and cleanup
- Abuse prevention and rate limiting

### Step 7 — Scale and address bottlenecks

Discuss trade-offs explicitly.

- Load balancing
- Horizontal scaling
- Stateless application servers
- Caching layers
- Database replication
- Sharding or federation
- Asynchronous processing
- Message queues
- Monitoring, alerting, and failure handling

## 4. Object-Oriented Design Template

Use this for low-level or object-oriented design prompts.

1. Clarify the problem and constraints.
2. Identify core entities.
3. Define relationships and ownership.
4. Define class responsibilities.
5. Choose design patterns where justified.
6. Handle concurrency, errors, and extensibility.
7. Present the class diagram and key code interfaces.

Repository examples include:

- Hash map
- LRU cache
- Call center
- Deck of cards
- Parking lot
- Chat server

## 5. Core Concepts to Include

### Scalability

- **Vertical scaling:** add more CPU, memory, or storage to one machine.
- **Horizontal scaling:** add more machines; usually requires stateless services and load balancing.
- A performance problem means the system is slow for one user; a scalability problem means it is fast for one user but degrades under load.

### Latency and throughput

- **Latency:** time to complete one operation.
- **Throughput:** operations completed per unit of time.
- Aim for high throughput while keeping latency acceptable.

### CAP theorem

In the presence of a network partition, choose between:

- **CP:** consistency and partition tolerance; may reject or time out requests.
- **AP:** availability and partition tolerance; may return stale data.

### Consistency patterns

| Pattern | Behavior | Typical use |
|---|---|---|
| Weak consistency | Reads may not see recent writes | Real-time chat, VoIP, gaming |
| Eventual consistency | Reads become consistent after a delay | DNS, email, highly available systems |
| Strong consistency | Reads always see the latest write | Financial transactions, RDBMSs |

### Availability

- Use fail-over and replication to improve availability.
- **Active-passive:** standby server takes over after failure.
- **Active-active:** multiple servers handle traffic simultaneously.
- Availability is often expressed in “nines,” e.g. 99.99% availability.

## 6. Architecture Building Blocks

### DNS

Translates domain names to IP addresses.

- `A` record: name to IP address
- `CNAME`: name to another name
- `MX` record: mail server
- `NS` record: authoritative name server
- Can route by weighted round robin, latency, or geography

### CDN

Serves content from edge locations near users.

- **Push CDN:** content is uploaded when created or changed.
- **Pull CDN:** content is fetched from origin on first request and cached according to TTL.
- Best for static assets; some CDNs also support dynamic content.

### Load balancer

Distributes traffic across healthy servers.

- Layer 4: routes using IP addresses and ports.
- Layer 7: routes using HTTP headers, URLs, cookies, and message content.
- Supports SSL termination, health checks, session persistence, and horizontal scaling.

### Reverse proxy

Centralizes access to backend services.

- Hides backend topology
- Terminates TLS
- Compresses responses
- Caches responses
- Serves static content
- Can also perform Layer 7 load balancing

### Application layer

Separates web serving from business logic.

- Enables independent scaling of web and application tiers.
- Microservices split functionality into independently deployable services.
- Service discovery tools such as Consul, etcd, and ZooKeeper help services locate each other.

### Caching

Common cache patterns:

- **Cache-aside:** application checks cache, then database; populates cache on miss.
- **Read-through:** cache loads data from the database automatically.
- **Write-through:** writes go to cache and database synchronously.
- **Write-behind:** writes go to cache first, then asynchronously to the database.
- **Refresh-ahead:** cache proactively refreshes likely-to-be-accessed data.

### Asynchronism

Use queues and workers for work that does not need an immediate response.

- Improves responsiveness under load.
- Enables retries and decouples services.
- Introduces eventual consistency and operational complexity.

### Databases

Relational databases provide ACID guarantees:

- Atomicity
- Consistency
- Isolation
- Durability

Scaling techniques:

- Master-slave replication
- Master-master replication
- Federation
- Sharding
- Denormalization
- SQL tuning

NoSQL families:

- Key-value stores
- Document stores
- Wide-column stores
- Graph databases

## 7. Key Architecture Diagrams to Preserve

When converting the repository into a local study pack, retain diagrams for:

- Client-server request flow
- DNS resolution
- CDN push versus pull models
- Layer 4 versus Layer 7 load balancing
- Active-passive and active-active fail-over
- Master-slave and master-master replication
- Database federation
- Database sharding
- Cache-aside, write-through, and write-behind caching
- Asynchronous workers and message queues
- Microservices and service discovery
- Complete solution diagrams for Pastebin, Twitter timeline/search, web crawler, Mint, social network, key-value store, sales ranking, and AWS-scale system

## 8. Practice Questions

### System design

- Design Pastebin or Bitly.
- Design the Twitter timeline and search, or Facebook feed and search.
- Design a web crawler.
- Design Mint.com.
- Design data structures for a social network.
- Design a key-value store for a search engine.
- Design Amazon’s sales ranking by category.
- Design a system that scales to millions of users on AWS.

### Object-oriented design

- Design a hash map.
- Design an LRU cache.
- Design a call center.
- Design a deck of cards.
- Design a parking lot.
- Design a chat server.

## 9. Study Plan

| Timeline | Focus | Practice |
|---|---|---|
| Short | Broad coverage of core topics | Solve some questions |
| Medium | Broad coverage plus selected depth | Solve many questions |
| Long | Broad coverage plus deeper mastery | Solve most questions |

## 10. Reusable Answer Checklist

- [ ] Clarified functional and non-functional requirements
- [ ] Stated assumptions
- [ ] Estimated users, QPS, storage, bandwidth, and cache size
- [ ] Drew a high-level architecture
- [ ] Defined APIs
- [ ] Designed the data model
- [ ] Selected database and cache strategy
- [ ] Addressed scaling, replication, and sharding
- [ ] Discussed failure modes and availability
- [ ] Identified bottlenecks and trade-offs
- [ ] Proposed monitoring and operational improvements
