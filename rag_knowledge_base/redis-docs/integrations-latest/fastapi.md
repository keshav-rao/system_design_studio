# Redis with FastAPI

```json metadata
{
  "schema_version": 2,
  "title": "Redis with FastAPI",
  "description": "Add idiomatic Redis connection management and dependency-injection caching to FastAPI apps.",
  "categories": ["docs","integrate","oss","rs","rc"],
  "group": "framework",
  "tableOfContents": {"sections":[{"id":"requirements","title":"Requirements"},{"id":"install-and-import","title":"Install and import"},{"id":"quick-start","title":"Quick start"},{"id":"configuration","title":"Configuration"},{"children":[{"id":"dependency-injection-factories","title":"Dependency-injection factories"},{"id":"cachebackend-for-full-control","title":"CacheBackend for full control"}],"id":"caching","title":"Caching"},{"id":"http-caching","title":"HTTP caching"},{"id":"cluster-mode","title":"Cluster mode"},{"id":"observability","title":"Observability"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"fastapi_tutorial-stepcache_hit_miss","description":"Foundational: cache a GET response so the first request is a MISS and the next is served from Redis as a HIT","difficulty":"beginner","id":"cache_hit_miss","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_fastapi_tutorial-stepcache_hit_miss"}]},{"buildsUpon":["cache_hit_miss"],"codetabsId":"fastapi_tutorial-stepcache_evict","description":"Invalidate a cached entry so the next read recomputes the response","difficulty":"beginner","id":"cache_evict","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_fastapi_tutorial-stepcache_evict"}]},{"buildsUpon":["cache_hit_miss"],"codetabsId":"fastapi_tutorial-stephttp_caching","description":"Use ETag and Cache-Control headers so a revalidation request returns 304 Not Modified","difficulty":"intermediate","id":"http_caching","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_fastapi_tutorial-stephttp_caching"}]}]
}
```

## Code Examples Legend

The code examples below show how to perform the same operations in different programming languages and client libraries:

- **Redis CLI**: Command-line interface for Redis
- **C# (Synchronous)**: StackExchange.Redis synchronous client
- **C# (Asynchronous)**: StackExchange.Redis asynchronous client
- **Go**: go-redis client
- **Java (Synchronous - Jedis)**: Jedis synchronous client
- **Java (Asynchronous - Lettuce)**: Lettuce asynchronous client
- **Java (Reactive - Lettuce)**: Lettuce reactive/streaming client
- **JavaScript (Node.js)**: node-redis client
- **PHP**: Predis client
- **Python**: redis-py client
- **Rust (Synchronous)**: redis-rs synchronous client
- **Rust (Asynchronous)**: redis-rs asynchronous client

Each code example demonstrates the same basic operation across different languages. The specific syntax and patterns vary based on the language and client library, but the underlying Redis commands and behavior remain consistent.

---


[FastAPI](https://fastapi.tiangolo.com/) is a modern, high-performance web framework
for building APIs with Python. The official
[fastapi-redis-sdk](https://github.com/redis/fastapi-redis-sdk) integrates Redis with
FastAPI without any boilerplate. It manages connection pools through the application
lifespan and exposes caching as injectable dependencies, including HTTP-native
[`ETag`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/ETag),
[`304 Not Modified`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status/304),
and [`Cache-Control`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control)
support.

The SDK is built on the [redis-py](https://redis.io/docs/latest/develop/clients/redis-py) client,
so anything redis-py can do is still available to you alongside the caching helpers.

## Requirements

See [Requirements](https://github.com/redis/fastapi-redis-sdk#requirements) on the
GitHub repo for the full set of dependencies used by `fastapi-redis-sdk`.

You also need a running Redis server. You can run one locally with
[Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis),
use [Docker](https://hub.docker.com/_/redis), or connect to
[Redis Cloud](https://redis.io/cloud/).

## Install and import

Use the following command to install `fastapi-redis-sdk`:

```bash
pip install fastapi-redis-sdk
```

Note that although you install the package as `fastapi-redis-sdk`, you import it as
`redis_fastapi`:

```python
from redis_fastapi import FastAPIRedis
```

## Quick start

Attach Redis to your app with the [fluent builder](https://en.wikipedia.org/wiki/Fluent_interface). The `lifespan()` call hooks into
the [FastAPI lifespan events](https://fastapi.tiangolo.com/advanced/events/) to open a
connection pool at startup and close it cleanly on shutdown. Inject `AsyncRedisDep`
into your `async` endpoints to get a ready-to-use client:

```python
from fastapi import FastAPI
from redis_fastapi import FastAPIRedis, AsyncRedisDep

app = FastAPI()
FastAPIRedis(app).lifespan()

@app.get("/items")
async def get_items(redis: AsyncRedisDep):
    return {"items": await redis.get("items")}
```

The builder wraps any existing lifespan, so multiple libraries can register their own
startup and shutdown logic without conflicting.

## Configuration

All settings are read from environment variables prefixed with `REDIS_`, or from a
`.env` file in your project root. The simplest setup is a single connection URL:

```bash
export REDIS_URL=redis://user:pass@host:6379/0
```

Alternatively, you can configure individual fields:

```bash
export REDIS_HOST=redis.example.com
export REDIS_PORT=6380
export REDIS_PASSWORD=secret
```

When `REDIS_URL` is set, it takes precedence over the individual connection fields.
The most commonly used variables are described in the table below:

| Variable | Default | Description |
|----------|---------|-------------|
| `REDIS_URL` | - | Full Redis URL (takes precedence over the fields below) |
| `REDIS_HOST` | `localhost` | Redis host |
| `REDIS_PORT` | `6379` | Redis port |
| `REDIS_PASSWORD` | - | Redis password (stored securely as a Pydantic `SecretStr`) |
| `REDIS_SSL` | `false` | Enable TLS (or use a `rediss://` URL) |
| `REDIS_CLUSTER` | `false` | Enable [OSS Cluster mode](#cluster-mode) |
| `REDIS_PREFIX` | `redis:fastapi` | Global prefix applied to all keys |
| `REDIS_DEFAULT_TTL` | `0` | Default cache TTL in seconds (`0` = no expiry) |
| `REDIS_MAX_CONNECTIONS` | - | Maximum pooled connections |

Configuration is validated with [Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/),
so invalid values (for example, a port outside 1–65535) fail fast at startup. For the
full environment-variable reference, TLS options, and programmatic configuration, see
the [SDK configuration guide](https://redis.github.io/fastapi-redis-sdk/guide/configuration/).

## Caching

Enable caching by adding `.caching()` to the builder chain. The SDK then offers two
complementary approaches that share the same connection pool:

| Approach | Best for |
|----------|----------|
| `cache()`, `cache_evict()`, `cache_put()` | Most endpoints — read, invalidate, and write-through |
| `CacheBackend` | Complex invalidation, conditional or dynamic caching |

### Dependency-injection factories

`cache()`, `cache_evict()`, and `cache_put()` are
[dependency](https://fastapi.tiangolo.com/tutorial/dependencies/) factories you attach
to a route. Because all three share the same `key_builder`, a `GET`, `DELETE`, and
`PUT` on the same path target the exact same cache key:

```python
from fastapi import Depends, FastAPI
from redis_fastapi import FastAPIRedis, cache, cache_evict, cache_put, default_key_builder

app = FastAPI()
FastAPIRedis(app).lifespan().caching()

# READ - cache the GET response for 5 minutes
@app.get("/products/{product_id}", dependencies=[Depends(cache(ttl=300, eviction_group="products"))])
async def get_product(product_id: int):
    return await db.get_product(product_id)

# INVALIDATE - evict the cached entry when the product is deleted
@app.delete(
    "/products/{product_id}",
    dependencies=[Depends(cache_evict(eviction_group="products", key_builder=default_key_builder))],
)
async def delete_product(product_id: int):
    await db.delete(product_id)

# WRITE-THROUGH - refresh the cache so the next GET is a HIT
@app.put(
    "/products/{product_id}",
    dependencies=[Depends(cache_put(eviction_group="products", key_builder=default_key_builder, ttl=300))],
)
async def replace_product(product_id: int, body: Product):
    return await db.update(product_id, body)
```

Cached responses include an `X-Redis-Cache` header (`HIT` or `MISS`) along with
`Cache-Control` and `ETag` headers.

The example below drives a cached endpoint with FastAPI's
[`TestClient`](https://fastapi.tiangolo.com/reference/testclient/) so you can see the
`MISS` → `HIT` → eviction cycle, plus the HTTP caching headers, in action:

Foundational: cache a GET response so the first request is a MISS and the next is served from Redis as a HIT

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
# The first request is a MISS: the handler runs and the response is cached.
first = client.get("/cache-demo")
print(first.headers["X-Redis-Cache"])
# >>> MISS

# A second request within the TTL is a HIT, served from Redis without
# re-running the handler, so the cached body is returned unchanged.
second = client.get("/cache-demo")
print(second.headers["X-Redis-Cache"])
# >>> HIT

print(first.json() == second.json())
# >>> True
```



Evicting a resource clears its cached entry, so the following read is a `MISS` again:

Invalidate a cached entry so the next read recomputes the response

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
# Deleting the resource evicts its cache entry, so the next read is a MISS
# again and the handler recomputes a fresh response.
client.delete("/cache-demo")

third = client.get("/cache-demo")
print(third.headers["X-Redis-Cache"])
# >>> MISS

print(third.json() == first.json())
# >>> False
```



### CacheBackend for full control

For conditional caching, cascade invalidation, dynamic TTLs, or caching intermediate
results, inject `CacheBackendDep` and call its `get`/`set`/`delete`/`has`/`delete_group`
methods directly. Values are serialized to and from JSON automatically:

```python
from redis_fastapi import CacheBackendDep

@app.get("/dashboard/{user_id}")
async def dashboard(user_id: int, cache: CacheBackendDep):
    cached = await cache.get(f"stats:{user_id}", eviction_group="dashboard")
    if cached is not None:
        return cached
    result = await compute_dashboard(user_id)
    await cache.set(f"stats:{user_id}", result, ttl=300, eviction_group="dashboard")
    return result
```

See the [SDK caching guide](https://redis.github.io/fastapi-redis-sdk/guide/caching/)
for detailed patterns and best practices.

## HTTP caching

Responses cached with the DI factories carry standard HTTP caching headers, so clients
and proxies can revalidate cheaply. The SDK sets `Cache-Control` from the entry's TTL
and emits a weak `ETag`; when a client returns that tag in an `If-None-Match` header,
the server responds with `304 Not Modified` and no body:

Use ETag and Cache-Control headers so a revalidation request returns 304 Not Modified

**Difficulty:** Intermediate

**Available in:** Python

##### Python

```python
# Cached responses carry standard HTTP caching headers. Evict first so the next
# request is a fresh MISS whose Cache-Control reflects the full 30-second TTL.
client.delete("/cache-demo")
miss = client.get("/cache-demo")
print(miss.headers["Cache-Control"])
# >>> max-age=30

# The cached response also carries a weak ETag. Replaying it with If-None-Match
# lets the server answer 304 Not Modified with no body.
etag = miss.headers["ETag"]
not_modified = client.get("/cache-demo", headers={"If-None-Match": etag})
print(not_modified.status_code)
# >>> 304
```



## Cluster mode

To work with an [OSS Cluster](https://redis.io/docs/latest/operate/oss_and_stack/management/scaling),
set `REDIS_CLUSTER=true` and point `REDIS_URL` at the cluster nodes:

```bash
export REDIS_CLUSTER=true
export REDIS_URL=redis://node1:6379,node2:6379,node3:6379
```

In cluster mode, `AsyncRedisDep` yields an `AsyncRedisCluster` client.

## Observability

The SDK can emit [OpenTelemetry](https://opentelemetry.io/) spans and metrics for every
cache operation. Telemetry is opt-in and a zero-cost no-op when disabled. Install the
optional dependency and enable it on the builder:

```bash
pip install fastapi-redis-sdk[otel]
```

```python
FastAPIRedis(app).lifespan().caching().otel()
```

Calling `.otel()` on the builder is what activates the cache telemetry. To also emit
redis-py's low-level command spans and connection-pool metrics, set
`REDIS_OTEL_REDIS_ENABLED=true`. See the
[SDK configuration guide](https://redis.github.io/fastapi-redis-sdk/guide/configuration/#opentelemetry)
for the full list of spans and metrics that are emitted.

## More information

- [fastapi-redis-sdk on GitHub](https://github.com/redis/fastapi-redis-sdk)
- [fastapi-redis-sdk documentation](https://redis.github.io/fastapi-redis-sdk/)
- [fastapi-redis-sdk on PyPI](https://pypi.org/project/fastapi-redis-sdk/)
- [redis-py client documentation](https://redis.io/docs/latest/develop/clients/redis-py)
- [FastAPI documentation](https://fastapi.tiangolo.com/)

