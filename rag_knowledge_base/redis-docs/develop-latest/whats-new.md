# What's new?

```json metadata
{
  "schema_version": 2,
  "title": "What's new?",
  "description": "High-level description of important updates to the Develop section",
  "categories": ["docs","operate","rs","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"redis-version-updates","title":"Redis Version Updates"},{"id":"redis-iris-context-engine","title":"Redis Iris (Context Engine)"}],"id":"q3-2026-july---september-updates","title":"Q3 2026 (July - September) Updates"},{"children":[{"id":"redis-version-updates-1","title":"Redis Version Updates"}],"id":"q2-2026-april---june-updates","title":"Q2 2026 (April - June) Updates"},{"children":[{"id":"tools","title":"Tools"},{"id":"redis-ai--vectors","title":"Redis AI \u0026 Vectors"},{"id":"data-types","title":"Data Types"},{"id":"client-libraries","title":"Client Libraries"},{"id":"documentation-updates","title":"Documentation Updates"},{"id":"redis-version-updates-2","title":"Redis Version Updates"}],"id":"q1-2026-january---march-updates","title":"Q1 2026 (January - March) Updates"},{"children":[{"id":"tools-1","title":"Tools"},{"id":"redis-ai--vectors-1","title":"Redis AI \u0026 Vectors"},{"id":"client-libraries-1","title":"Client Libraries"},{"id":"documentation-updates-1","title":"Documentation Updates"}],"id":"q4-2025-october---december-updates","title":"Q4 2025 (October - December) Updates"},{"children":[{"id":"tools-2","title":"Tools"},{"id":"redis-ai--vectors-2","title":"Redis AI \u0026 Vectors"},{"id":"data-types-1","title":"Data Types"},{"id":"client-libraries-2","title":"Client Libraries"},{"id":"documentation-updates-2","title":"Documentation Updates"}],"id":"q3-2025-july---september-updates","title":"Q3 2025 (July - September) Updates"},{"children":[{"id":"tools-3","title":"Tools"},{"id":"redis-ai--vectors-3","title":"Redis AI \u0026 Vectors"},{"id":"redis-80--82-features","title":"Redis 8.0 \u0026 8.2 Features"},{"id":"data-types-2","title":"Data Types"},{"id":"client-libraries-3","title":"Client Libraries"},{"id":"documentation-structure--navigation","title":"Documentation Structure \u0026 Navigation"},{"id":"protocol--technical-updates","title":"Protocol \u0026 Technical Updates"}],"id":"q2-2025-april---june-updates","title":"Q2 2025 (April - June) Updates"},{"children":[{"id":"tools-4","title":"Tools"},{"id":"redis-ai--vectors-4","title":"Redis AI \u0026 Vectors"},{"id":"data-types-3","title":"Data Types"},{"id":"commands--api-docs","title":"Commands \u0026 API Docs"},{"id":"search--query","title":"Search \u0026 Query"},{"id":"client-libraries-4","title":"Client Libraries"}],"id":"q1-2025-january---march-updates","title":"Q1 2025 (January - March) Updates"},{"id":"q4-2024-october---december-updates","title":"Q4 2024 (October - December) Updates"},{"id":"q3-2024-july---september-updates","title":"Q3 2024 (July - September) Updates"}]}

,
  "codeExamples": []
}
```


## Q3 2026 (July - September) Updates

### Redis Version Updates

- [Redis 8.10](https://redis.io/docs/latest/develop/whats-new/8-10) - Compact Hashes for lower memory usage and higher throughput; incremental backup and restore; extensive JSONPath extensions; new commands for Lists, Sets, Search, and Time Series, including `LMOVEM/BLMOVEM`, `SUNIONCARD/SDIFFCARD`, `FT.ALIASLIST`, `TS.NRANGE/TS.NREVRANGE`, and `TS.READ`; a new `FT.AGGREGATE COLLECT` reducer; stricter query timeout enforcement; and performance improvements across Redis core and Streams.

---

### Redis Iris (Context Engine)

- Added self-managed deployment documentation for all four Redis Iris services: [LangCache](https://redis.io/docs/latest/operate/iris/langcache/self-managed), [Agent Memory](https://redis.io/docs/latest/operate/iris/agent-memory/self-managed), [Context Retriever](https://redis.io/docs/latest/develop/ai/context-engine/context-retriever/install), and [Data Integration](https://redis.io/docs/latest/integrate/redis-data-integration)
- Updated [LangCache](https://redis.io/docs/latest/develop/ai/context-engine/langcache), [Agent Memory](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory), [Context Retriever](https://redis.io/docs/latest/develop/ai/context-engine/context-retriever), and [Data Integration](https://redis.io/docs/latest/develop/ai/context-engine/data-integration) quickstarts with fully managed and self-managed deployment paths
- Added [Redis Iris concepts](https://redis.io/docs/latest/develop/ai/context-engine/concepts) explaining how agents get context from Redis Iris
- Added new [AI agent builder](https://redis.io/docs/latest/develop/ai/agent-builder) templates for knowledge assistants (RAG) and Redis Iris conversational assistants

## Q2 2026 (April - June) Updates

### Redis Version Updates

- [Redis 8.8](https://redis.io/docs/latest/develop/whats-new/8-8) - New Array data structure, `INCREX` rate limiter, in-group sorting reducer for `FT.AGGREGATE`, Rust iterators and devirtualized vector hot paths in Search, HyperLogLog and `MGET`/`MSET`/`HGETALL` performance improvements.

## Q1 2026 (January - March) Updates

### Tools

- Redis Insight [v3.2.0 release notes](https://redis.io/docs/latest/develop/tools/insight/release-notes/v.3.2.0)
- Redis Insight [v3.0.3 release notes](https://redis.io/docs/latest/develop/tools/insight/release-notes/v.3.0.3)
- Redis Insight [v2.68.0 release notes](https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.68.0)
- Redis Insight [v2.66.0 release notes](https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.66.0)

---

### Redis AI & Vectors

- Added [n8n vector store integration](https://redis.io/docs/latest/integrate/n8n-vector-store)
- Updated [RedisVL 0.7.0 documentation](https://redis.io/docs/latest/develop/ai/redisvl/0.7.0)
- Updated [RedisVL 0.9.1 documentation](https://redis.io/docs/latest/develop/ai/redisvl/0.9.1)
- Updated [RedisVL 0.12.1 documentation](https://redis.io/docs/latest/develop/ai/redisvl/0.12.1) (28 pages)

---

### Data Types

- Enhanced [example progression](https://redis.io/docs/latest/develop/data-types) with metadata for:
  - [Strings](https://redis.io/docs/latest/develop/data-types/strings)
  - [Hashes](https://redis.io/docs/latest/develop/data-types/hashes)
  - [Lists](https://redis.io/docs/latest/develop/data-types/lists)
  - [Sets](https://redis.io/docs/latest/develop/data-types/sets)
  - [Sorted sets](https://redis.io/docs/latest/develop/data-types/sorted-sets)
  - [Bitmaps](https://redis.io/docs/latest/develop/data-types/strings/bitmaps)
  - [Geospatial](https://redis.io/docs/latest/develop/data-types/geospatial)
  - [JSON](https://redis.io/docs/latest/develop/data-types/json)
  - [Time series](https://redis.io/docs/latest/develop/data-types/timeseries)
  - [Vector sets](https://redis.io/docs/latest/develop/data-types/vector-sets)

---

### Client Libraries

#### Ruby (NEW)
- Added [Ruby client documentation](https://redis.io/docs/latest/develop/clients/ruby)
- Landing page code examples for redis-rb

#### ioredis (NEW)
- Added [ioredis connect page](https://redis.io/docs/latest/develop/clients/ioredis/connect)

#### node-redis (JavaScript)
- Added Smart client handoffs section in the Connect page

#### Rust
- Added [Rust AMR/EntraID connection page](https://redis.io/docs/latest/develop/clients/rust/amr)
- Added Rust error handling documentation
- Added Rust transactions and pipelines documentation

#### Python (redis-py)
- Updated failover documentation with initial health checks
- Added failback configuration details
- Added observability page
- Added Smart client handoffs section in the Connect page

#### Java (Jedis)
- Added failback configuration section
- Updated failover behavior documentation

#### Java (Lettuce)
- Added failover documentation
- Added `LagAwareStrategy` dependencies
- Added Smart client handoffs section in the Connect page

#### .NET (NRedisStack)
- Added [FusionCache integration page](https://redis.io/docs/latest/integrate/fusioncache)

#### Go
- Added observability page
- Added Smart client handoffs section in the Connect page

---

### Documentation Updates

- Added BinderHub support for "Run in browser" functionality with Python examples
- Added Jupyter notebook support with pre-configured environments
- Enhanced example progression metadata across all data types
- Added testable code example shortcodes with language-specific markers
- Fixed fuzzy search documentation with specific attribute examples
- Updated client library description differences across all major clients
- Added observability overview with OpenTelemetry metrics
- Added Smart client handoffs overview
- Docs for n8n Redis vector store integration
- Added railroad diagrams and API methods to all command pages

---

### Redis Version Updates

- [Redis 8.6](https://redis.io/docs/latest/develop/whats-new/8-6) - Stream idempotency, least recently modified eviction policies, hot key detection, TLS certificate-based authentication, enhanced time series with NaN support, memory optimizations
- [Redis 8.4](https://redis.io/docs/latest/develop/whats-new/8-4) - Updated documentation (removed RC1 designation)

## Q4 2025 (October - December) Updates

### Tools

- Enhanced Redis Insight documentation with autocomplete features

---

### Redis AI & Vectors

- Launched [AI Agent Builder](https://redis.io/docs/latest/develop/ai/agent-builder) - interactive code generator for production-ready AI agents
- Documented [RedisVL 0.9.0](https://redis.io/docs/latest/develop/ai/redisvl) (28 pages):
  - Vector search and indexing
  - Semantic caching
  - Message history management
  - Rerankers and routers
  - Vectorizers
- Added [AI video tutorials](https://redis.io/docs/latest/develop/ai/ai-videos) with YouTube content
- Added [AI notebook collection](https://redis.io/docs/latest/develop/ai/notebook-collection) with notebook links
- Added [LangCache documentation](https://redis.io/docs/latest/develop/ai/context-engine/langcache) with API examples

---

### Client Libraries

#### Rust (NEW)
- Added [Rust client documentation](https://redis.io/docs/latest/develop/clients/rust)
- Enabled Rust-Sync and Rust-Async client variants
- Landing page code examples for Rust

#### Java (Jedis)
- Added [vector set embedding examples](https://redis.io/docs/latest/develop/clients/jedis/vecsets)

#### .NET (NRedisStack)
- Added [vector set embedding examples](https://redis.io/docs/latest/develop/clients/dotnet/vecsets)
- Enabled C#-Sync and C#-Async client variants with async examples

---

### Documentation Updates

- Integrated BinderHub for "Run in browser" functionality with Python examples
- Launched Testable Code Examples (TCE) framework for hands-on learning
- Added new integration guides (cloud platforms, monitoring tools, AI/ML frameworks)

---

## Q3 2025 (July - September) Updates

### Tools

- Added [redis-cli installation instructions](https://redis.io/docs/latest/develop/tools/cli)

---

### Redis AI & Vectors

- Updated [vector types documentation](https://redis.io/docs/latest/develop/ai/search-and-query/vectors) for INT8 and UINT8
- Added [GEO search precision information](https://redis.io/docs/latest/develop/ai/search-and-query/indexing/geoindex)
- Enhanced [LangCache SDK](https://redis.io/docs/latest/develop/ai/context-engine/langcache) with savings calculator and improved API documentation

---

### Data Types

- [Bitmaps](https://redis.io/docs/latest/develop/data-types/strings/bitmaps):
  - Added BITOP documentation with Python testable code examples
  - Added bit operation diagrams

---

### Client Libraries

#### Java (Jedis)
- Added [vector set embedding examples](https://redis.io/docs/latest/develop/clients/jedis/vecsets)

#### .NET (NRedisStack)
- Added [vector set embedding examples](https://redis.io/docs/latest/develop/clients/dotnet/vecsets)
- Enabled C#-Sync and C#-Async client variants with async examples on the landing page

#### Rust (NEW)
- Added initial [Rust client documentation](https://redis.io/docs/latest/develop/clients/rust)
- Enabled Rust-Sync and Rust-Async client variants
- Landing page code examples for Rust

---

### Documentation Updates

- Added [close/quit details](https://redis.io/docs/latest/develop/clients) to client landing pages
- Added [redlock-universal](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks) to Redlock implementations list
- Fixed [keyspace notifications](https://redis.io/docs/latest/develop/pubsub/keyspace-notifications) typo
- Updated Unicode quotes to ASCII throughout documentation
- Fixed broken links and improved cross-references

## Q2 2025 (April - June) Updates

### Tools

- Redis Insight [v2.70.1 release notes](https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.70.1)
- Redis Insight [v1.4.0 release notes](https://redis.io/docs/latest/develop/tools/insight/release-notes/v1.4.0)
- Updated [Redis Insight pages](https://redis.io/docs/latest/develop/tools/insight) with consistent image-card layout
- Added Redis Insight SVG icons and download links across [tools documentation](https://redis.io/docs/latest/develop/tools)

---

### Redis AI & Vectors

- Reorganized [search and query documentation](https://redis.io/docs/latest/develop/ai/search-and-query) under AI section
- Added [AI video tutorials](https://redis.io/docs/latest/develop/ai/ai-videos) with YouTube content
- Added [AI notebook collection](https://redis.io/docs/latest/develop/ai/notebook-collection) with 8 new notebook links
- Expanded vector examples across multiple clients:
  - [Python vector sets](https://redis.io/docs/latest/develop/clients/redis-py/vecsets)
  - [Go vector sets](https://redis.io/docs/latest/develop/clients/go/vecsets)
  - [JavaScript vector sets](https://redis.io/docs/latest/develop/clients/nodejs/vecsets)
  - [Lettuce vector queries](https://redis.io/docs/latest/develop/clients/lettuce/vecsearch)
  - [Lettuce vector sets](https://redis.io/docs/latest/develop/clients/lettuce/vecsets)
- Updated [redisvl documentation](https://redis.io/docs/latest/develop/ai/redisvl) for versions 0.6.0-0.8.2
- Added [LangCache SDK](https://redis.io/docs/latest/develop/ai/context-engine/langcache) documentation with [API reference](https://redis.io/docs/latest/develop/ai/context-engine/langcache/api-examples)

---

### Redis 8.0 & 8.2 Features

- [Redis Open Source 8.2 documentation](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.2-release-notes)
- Updated [Redis 8.0 release notes](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce/redisos-8.0-release-notes)
- [Redis Search expiration capabilities](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/expiration) in Redis 8
- Enhanced [TAG documentation](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/tags) per GitHub issues
- [Vector quantization and compression](https://redis.io/docs/latest/develop/ai/search-and-query/vectors/svs-compression) moved to dedicated page

---

### Data Types

- TimeSeries:
  - [Enhanced time series examples](https://redis.io/docs/latest/develop/data-types/timeseries) with query and aggregation info
  - Added testable code examples (TCE) support
- Probabilistic:
  - Added testable examples for [Python](https://redis.io/docs/latest/develop/clients/redis-py/prob), [C#](https://redis.io/docs/latest/develop/clients/dotnet/nredisstack/prob), [Java](https://redis.io/docs/latest/develop/clients/jedis/prob), and [Go](https://redis.io/docs/latest/develop/clients/go/prob)
  - Updated [Cuckoo filter documentation](https://redis.io/docs/latest/develop/data-types/probabilistic/cuckoo-filter)

---

### Client Libraries

#### Python (redis-py)
- Added [reconnection examples](https://redis.io/docs/latest/develop/clients/redis-py/connect#retrying-connections)
- Enhanced [timeout and retry details](https://redis.io/docs/latest/develop/clients/redis-py/produsage#timeouts)
- Fixed [pip install command](https://redis.io/docs/latest/develop/clients/redis-py/amr) for redis-py entraid extension
- Added [Binder environment links](https://redis.io/docs/latest/develop/clients/redis-py#connect-and-test) for Python examples

#### Java (Jedis)
- Updated to [latest Jedis version](https://redis.io/docs/latest/develop/clients/jedis#install)
- Added [reconnection examples](https://redis.io/docs/latest/develop/clients/jedis/connect#retrying-a-command-after-a-connection-failure)
- Enhanced [probabilistic data type examples](https://redis.io/docs/latest/develop/clients/jedis/prob)

#### Node.js
- Added [command reliability information](https://redis.io/docs/latest/develop/clients/nodejs/produsage#command-execution-reliability)
- Fixed [reconnection details](https://redis.io/docs/latest/develop/clients/nodejs/connect#reconnect-after-disconnection)

#### .NET (StackExchange.Redis/NRedisStack)
- Added [retries and timeouts](https://redis.io/docs/latest/develop/clients/dotnet/produsage) to production usage advice
- Enhanced [dialect 2 notes](https://redis.io/docs/latest/develop/clients/dotnet/nredisstack/queryjson)

#### Go (go-redis)
- Added [retries and timeouts](https://redis.io/docs/latest/develop/clients/go/produsage) to production usage
- Enhanced [dialect 2 notes](https://redis.io/docs/latest/develop/clients/go/queryjson)
- Added [Connect with AMR](https://redis.io/docs/latest/develop/clients/go/amr) page.

#### Lettuce
- Updated to [latest Lettuce version](https://redis.io/docs/latest/develop/clients/lettuce#install)
- Added [command reliability information](https://redis.io/docs/latest/develop/clients/lettuce/produsage#connection-and-execution-reliability)
- Added [JSON query examples](https://redis.io/docs/latest/develop/clients/lettuce/queryjson)

#### PHP (Predis)
- Enhanced [dialect 2 notes](https://redis.io/docs/latest/develop/clients/php/queryjson)

---

### Documentation Structure & Navigation

- Reorganized [develop section navigation](https://redis.io/docs/latest/develop) with improved sidebar structure
- Moved [programmability section](https://redis.io/docs/latest/develop/programmability) into develop area
- Relocated [patterns folder](https://redis.io/docs/latest/develop/clients/patterns) to clients section
- Added [Using commands section](https://redis.io/docs/latest/develop/using-commands) to develop area
- Enhanced [keyspace notifications](https://redis.io/docs/latest/develop/pubsub/keyspace-notifications) and [pub/sub](https://redis.io/docs/latest/develop/pubsub) documentation
- Updated [transactions](https://redis.io/docs/latest/develop/using-commands/transactions) and [pipeline](https://redis.io/docs/latest/develop/using-commands/pipelining) pages
- Added comprehensive aliases for backward compatibility

---

### Protocol & Technical Updates

- Fixed [RESP protocol specification](https://redis.io/docs/latest/develop/reference/protocol-spec) attribute byte documentation
- Enhanced [FT.AGGREGATE expression precedence](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/aggregations-syntax) documentation
- Updated [distributed locks](https://redis.io/docs/latest/develop/clients/patterns/distributed-locks) documentation
- Fixed [FP32 vectorsets endianness](https://redis.io/docs/latest/develop/data-types/vector-sets#endianness-considerations-for-fp32-format) documentation

## Q1 2025 (January - March) Updates

### Tools

- Redis Insight [v2.66 release notes](https://redis.io/docs/latest/develop/tools/insight/release-notes/v.2.66.0)
- Updated CLI output samples for [`bigkeys`, `memkeys`, `keystats`](https://redis.io/docs/latest/develop/tools/cli)

---

### Redis AI & Vectors

- Expanded vector examples:
  - [Python](https://redis.io/docs/latest/develop/clients/redis-py/vecsearch)
  - [Node.js](https://redis.io/docs/latest/develop/clients/nodejs/vecsearch)
  - [Java (Jedis)](https://redis.io/docs/latest/develop/clients/jedis/vecsearch)
  - [Go](https://redis.io/docs/latest/develop/clients/go/vecsearch)
  - [.NET](https://redis.io/docs/latest/develop/clients/dotnet/nredisstack/vecsearch)
- Updated AI integrations:
  - [AI overview](https://redis.io/docs/latest/develop/ai)
  - [RAG intro](https://redis.io/docs/latest/develop/get-started/rag)
  - [Redis in AI](https://redis.io/docs/latest/develop/get-started/redis-in-ai)

---

### Data Types

- TimeSeries:
  - [`COMPACTION_POLICY`](https://redis.io/docs/latest/develop/data-types/timeseries/configuration)
  - [Client-side caching update](https://redis.io/docs/latest/develop/clients/client-side-caching)
- JSON:
  - [Active memory defragmentation](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/json/commands)
- Probabilistic:
  - [Bloom filter](https://redis.io/docs/latest/develop/data-types/probabilistic/bloom-filter)
  - [Count-min sketch](https://redis.io/docs/latest/develop/data-types/probabilistic/count-min-sketch)
  - [Top-K](https://redis.io/docs/latest/develop/data-types/probabilistic/top-k)
  - [Cuckoo filter](https://redis.io/docs/latest/develop/data-types/probabilistic/cuckoo-filter)

---

### Commands & API Docs

- Pages updated for format and accuracy:
  - [ACL SETUSER](https://redis.io/docs/latest/commands/acl-setuser)
  - [JSON.GET](https://redis.io/docs/latest/commands/json.get)
  - [TS.ADD](https://redis.io/docs/latest/commands/ts.add)
  - [SCAN](https://redis.io/docs/latest/commands/scan)
  - [SORT](https://redis.io/docs/latest/commands/sort)
- RESP3 reply types documented in [Hiredis command page](https://redis.io/docs/latest/develop/clients/hiredis/issue-commands)
- [CSC behavior clarified](https://redis.io/docs/latest/develop/clients/client-side-caching)

---

### Search & Query

- Best practices:
  - [Dev-to-prod guide](https://redis.io/docs/latest/develop/ai/search-and-query/best-practices/dev-to-prod-best-practices)
  - [Scalable queries](https://redis.io/docs/latest/develop/ai/search-and-query/best-practices/scalable-query-best-practices)
  - [Index lifecycle](https://redis.io/docs/latest/develop/ai/search-and-query/best-practices/index-mgmt-best-practices)
- New/updated topics:
  - [Autocomplete](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/autocomplete)
  - [Escaping & tokenization](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/escaping)
  - [Geo indexing](https://redis.io/docs/latest/develop/ai/search-and-query/indexing/geoindex)
  - [Sorting, scoring, stemming](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/sorting)

---

### Client Libraries

#### Go
- [Trans/pipe examples](https://redis.io/docs/latest/develop/clients/go/transpipe)
- [JSON queries](https://redis.io/docs/latest/develop/clients/go/queryjson)

#### .NET
- [Vector search](https://redis.io/docs/latest/develop/clients/dotnet/nredisstack/vecsearch)
- [Trans/pipe usage](https://redis.io/docs/latest/develop/clients/dotnet/transpipe)
- [JSON queries](https://redis.io/docs/latest/develop/clients/dotnet/nredisstack/queryjson)

#### Java (Jedis)
- [Vector search](https://redis.io/docs/latest/develop/clients/jedis/vecsearch)
- [Trans/pipe usage](https://redis.io/docs/latest/develop/clients/jedis/transpipe)

#### Node.js
- [Vector queries](https://redis.io/docs/latest/develop/clients/nodejs/vecsearch)
- [Trans/pipe examples](https://redis.io/docs/latest/develop/clients/nodejs/transpipe)
- [JSON queries](https://redis.io/docs/latest/develop/clients/nodejs/queryjson)

#### Redis-py
- [ScanIter usage](https://redis.io/docs/latest/develop/clients/redis-py/scaniter)
- [Vector search](https://redis.io/docs/latest/develop/clients/redis-py/vecsearch)
- [Trans/pipe usage](https://redis.io/docs/latest/develop/clients/redis-py/transpipe)
- [JSON queries](https://redis.io/docs/latest/develop/clients/redis-py/queryjson)

#### Lettuce
- [Cluster connection](https://redis.io/docs/latest/develop/clients/lettuce/connect)
- [Production usage](https://redis.io/docs/latest/develop/clients/lettuce/produsage)

#### Hiredis
- Full client guide:
  - [Overview](https://redis.io/docs/latest/develop/clients/hiredis)
  - [Connect](https://redis.io/docs/latest/develop/clients/hiredis/connect)
  - [Issue commands](https://redis.io/docs/latest/develop/clients/hiredis/issue-commands)
  - [Handle replies](https://redis.io/docs/latest/develop/clients/hiredis/handle-replies)
  - [Transactions and pipelines](https://redis.io/docs/latest/develop/clients/hiredis/transpipe)



## Q4 2024 (October - December) Updates

* Updated the RESP3 specification document to include the [attribute type](https://redis.io/docs/latest/develop/reference/protocol-spec#attributes).
* Updates to the [key eviction](https://redis.io/docs/latest/develop/reference/eviction) page.
* Updates to the Redis Insight page related to its new Redis Search auto-completion [feature](https://redis.io/docs/latest/develop/tools/insight#workbench).
* Restructured and added testable connection examples to the [client pages](https://redis.io/docs/latest/develop/clients).
* Added [Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce) and [Redis Stack](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisstack) release notes.
* Added new [Redis for AI](https://redis.io/docs/latest/develop/ai) page.
* Added new [Predis (PHP client library)](https://redis.io/docs/latest/develop/clients/php) page.

## Q3 2024 (July - September) Updates

* Updated the [RAG with Redis quick start guide](https://redis.io/docs/latest/develop/get-started/rag).
* Updates for [Redis Open Source version 7.4](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisce).
* Added new [Redis Insight debugging](https://redis.io/docs/latest/develop/tools/insight/debugging) page.
* Completed a major re-write/restructuring of the [vector indexing page](https://redis.io/docs/latest/develop/ai/search-and-query/vectors).
* Added new [client-side caching page](https://redis.io/docs/latest/develop/clients/client-side-caching).
* Added new documentation for the [RDI in Redis Insight feature](https://redis.io/docs/latest/develop/tools/insight/rdi-connector).
* Added new documentation for the [Redis for VS Code feature](https://redis.io/docs/latest/develop/tools/redis-for-vscode).
* Added multi-language code examples to Redis Search [query](https://redis.io/docs/latest/develop/ai/search-and-query/query) pages.
* Added client-side caching information to the [supported clients](https://redis.io/docs/latest/develop/clients/client-side-caching#which-client-libraries-support-client-side-caching) pages.
* Numerous changes to the [Redis client content](https://redis.io/docs/latest/develop/clients).

