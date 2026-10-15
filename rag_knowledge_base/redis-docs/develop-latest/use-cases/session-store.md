# Redis session store

```json metadata
{
  "schema_version": 2,
  "title": "Redis session store",
  "description": "Store web sessions in Redis.",
  "categories": ["docs","develop","stack","oss","rs","rc"],
  "tableOfContents": {"sections":[{"id":"when-to-use-a-session-store","title":"When to use a session store"},{"id":"why-the-problem-is-hard","title":"Why the problem is hard"},{"id":"what-you-can-expect-from-a-redis-solution","title":"What you can expect from a Redis solution"},{"id":"how-redis-supports-the-solution","title":"How Redis supports the solution"},{"id":"ecosystem","title":"Ecosystem"},{"id":"code-examples-to-build-your-own-redis-session-store","title":"Code examples to build your own Redis session store"}]}

,
  "codeExamples": []
}
```


## When to use a session store

Use a Redis session store when you need to share per-user session state (login context, shopping carts, preferences) across stateless application servers without sticky sessions or database round-trips.

## Why the problem is hard

HTTP is stateless, so you must rely on external state to recognize a returning user between requests.
Some of the obvious approaches have significant drawbacks:

-   **Storing sessions on individual app servers**: this requires
    [sticky routing](https://en.wikipedia.org/wiki/Load_balancing_(computing)#Persistence), which creates
    hot spots and precludes [failover](https://en.wikipedia.org/wiki/Failover).
-   **Moving session reads to a relational database**: this adds 5–20 ms per request. If you have
    thousands of concurrent users then session reads dominate connection pools. This turns every page load
    into a contention point that degrades the primary database for all other workloads.

Sessions need automatic cleanup without external sweep jobs. You will incur
direct business costs (abandoned carts, forced re-authentication, interrupted checkouts) if
you lose sessions, so durability matters more than it does with pure caching.

At operational scale, you also need to run queries against multiple sessions (for example, find all
carts containing a recalled product, count sessions per tenant), which is more complicated than just reading individual sessions.

## What you can expect from a Redis solution

You can:

-   Eliminate sticky sessions so any instance can serve any user behind a load balancer.
-   Expire inactive sessions automatically without cleanup jobs or database sweeps.
-   Update individual session fields without re-serializing the full session.
-   Track sessions across multiple devices per user, including logout-all.
-   Query across active sessions for operational and security tasks without key scanning.
-   Retain session data across deployments and node restarts with configurable durability.

## How Redis supports the solution

In practice, each session is stored as a Redis hash — one hash per session ID — and the key is set to expire automatically so inactive sessions are cleaned up without any external job.

Redis provides the following features that make it a good fit for session storage:

-   [Hashes](https://redis.io/docs/latest/develop/data-types/hashes) for field-level session access without 
    deserializing an entire session blob.
-   [`EXPIRE`](https://redis.io/docs/latest/commands/expire) with sliding TTL resets on each request so active 
    sessions stay alive while inactive ones are cleaned up automatically.
-   [Sets](https://redis.io/docs/latest/develop/data-types/sets) ([`SADD`](https://redis.io/docs/latest/commands/sadd), 
    [`SMEMBERS`](https://redis.io/docs/latest/commands/smembers)) to track all sessions per user for multi-device 
    management ([`DEL`](https://redis.io/docs/latest/commands/del) plus [`SREM`](https://redis.io/docs/latest/commands/srem) 
    handle explicit logout or logout-all).
-   AOF and RDB [persistence](https://redis.io/docs/latest/operate/oss_and_stack/management/persistence) to let 
    sessions survive process and node restarts within their expiration window. 
-   Secondary indexing (querying by field values rather than by key) via
    [Redis Search](https://redis.io/docs/latest/develop/ai/search-and-query) to support
    cross-session queries at runtime (finding affected carts, counting sessions by tenant)
    without key scanning.
-   Sub-millisecond latency on the request path, which is already on the same Redis instance
    in most stacks.

## Ecosystem

The following libraries and frameworks provide Redis session store integrations:

-   **Java**:
    [Spring Session Data Redis](https://docs.spring.io/spring-session/reference/configuration/redis.html)
-   **Node.js**: [`connect-redis`](https://www.npmjs.com/package/connect-redis)
    ([express-session](https://www.npmjs.com/package/express-session) store)
-   **Python**: [Flask-Session](https://flask-session.readthedocs.io/en/latest/),
    [django-redis](https://pypi.org/project/django-redis/)
-   **API gateways**: [Kong](https://docs.konghq.com/hub/kong-inc/session/),
    [Envoy](https://www.envoyproxy.io/docs/envoy/latest/start/quick-start/configuration-dynamic-control-plane)
    (Redis-backed session and token storage)

## Code examples to build your own Redis session store

The following guides show how to build a simple Redis-backed session store.
Each guide includes a runnable example to illustrate using the session store with a basic local
web server for each of the following client libraries:

* [redis-py (Python)](https://redis.io/docs/latest/develop/use-cases/session-store/redis-py)
* [node-redis (Node.js)](https://redis.io/docs/latest/develop/use-cases/session-store/nodejs)
* [go-redis (Go)](https://redis.io/docs/latest/develop/use-cases/session-store/go)
* [Jedis (Java)](https://redis.io/docs/latest/develop/use-cases/session-store/java-jedis)
* [Lettuce (Java)](https://redis.io/docs/latest/develop/use-cases/session-store/java-lettuce)
* [StackExchange.Redis (C#)](https://redis.io/docs/latest/develop/use-cases/session-store/dotnet)
* [Predis (PHP)](https://redis.io/docs/latest/develop/use-cases/session-store/php)
* [redis-rb (Ruby)](https://redis.io/docs/latest/develop/use-cases/session-store/ruby)
* [redis-rs (Rust)](https://redis.io/docs/latest/develop/use-cases/session-store/rust)

