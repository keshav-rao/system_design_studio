# Asynchronous operations with redis-py

```json metadata
{
  "schema_version": 2,
  "title": "Asynchronous operations with redis-py",
  "description": "Use redis-py with asyncio for non-blocking Redis access",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"basic-connection","title":"Basic connection"},{"id":"connection-pools","title":"Connection pools"},{"id":"awaiting-commands","title":"Awaiting commands"},{"id":"pipelines-and-transactions","title":"Pipelines and transactions"},{"id":"pubsub","title":"Pub/Sub"},{"id":"cluster-connections","title":"Cluster connections"},{"id":"cleanup-and-lifecycle","title":"Cleanup and lifecycle"},{"id":"cancellation-and-timeouts","title":"Cancellation and timeouts"},{"id":"translating-sync-examples","title":"Translating sync examples"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"async_intro-stepconnect","description":"Foundational: Connect to Redis with the async client and run a basic SET/GET","difficulty":"beginner","id":"connect","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_async_intro-stepconnect"}]},{"codetabsId":"async_intro-stepcontext_manager","description":"Foundational: Use the async client as a context manager for automatic cleanup","difficulty":"beginner","id":"context_manager","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_async_intro-stepcontext_manager"}]},{"codetabsId":"async_intro-steppool","description":"Foundational: Create and share a single async client across the app","difficulty":"beginner","id":"pool","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_async_intro-steppool"}]},{"codetabsId":"async_intro-stepgather","description":"Run several Redis commands concurrently with asyncio.gather","difficulty":"intermediate","id":"gather","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_async_intro-stepgather"}]},{"codetabsId":"async_intro-steppipeline","description":"Foundational: Execute commands in an async pipeline","difficulty":"beginner","id":"pipeline","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_async_intro-steppipeline"}]},{"codetabsId":"async_intro-stepwatch","description":"Optimistic locking with an async pipeline and WATCH","difficulty":"intermediate","id":"watch","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_async_intro-stepwatch"}]},{"codetabsId":"async_intro-steppubsub","description":"Subscribe and receive messages with the async pub/sub API","difficulty":"intermediate","id":"pubsub","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_async_intro-steppubsub"}]},{"codetabsId":"async_intro-stepcluster","description":"Foundational: Connect to a Redis cluster with the async client","difficulty":"beginner","id":"cluster","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_async_intro-stepcluster"}]},{"codetabsId":"async_intro-steptimeout","description":"Apply an asyncio timeout to a Redis command","difficulty":"intermediate","id":"timeout","languages":[{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_async_intro-steptimeout"}]}]
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


`redis-py` provides an asyncio-compatible API under the
[`redis.asyncio`](https://redis.readthedocs.io/en/stable/examples/asyncio_examples.html)
namespace. It mirrors the synchronous client API, so most code patterns
translate directly — you `await` commands instead of calling them.

Use the async client for I/O-bound workloads, for integration with async web
frameworks (such as [FastAPI](https://redis.io/docs/latest/integrate/fastapi), [Starlette](https://www.starlette.io/), [aiohttp](https://docs.aiohttp.org/en/stable/), or [Sanic](https://sanic.dev/en/), or when you need
to run many concurrent Redis operations from a single process. For simple
scripts, CPU-bound work, or codebases without an existing event loop, the
synchronous client is usually a better choice.

The examples on the other pages in this section use the synchronous client,
but you can translate any of them to async by following the rules in
[Translating sync examples](#translating-sync-examples) below.

## Basic connection

Import the async client from `redis.asyncio` and `await` each command.
Construction is synchronous and doesn't open a connection — the pool
establishes one lazily the first time you issue a command. Call `aclose()`
when you're done to release the underlying socket.

Foundational: Connect to Redis with the async client and run a basic SET/GET

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
import redis.asyncio as redis

async def basic_example():
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    await r.set('foo', 'bar')
    value = await r.get('foo')
    print(value)
    # bar
    await r.aclose()

asyncio.run(basic_example())
```



The recommended pattern is to use the client as an async context manager,
which ensures `aclose()` runs even if an exception is raised:

Foundational: Use the async client as a context manager for automatic cleanup

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
async def context_example():
    async with redis.Redis(
        host='localhost', port=6379, decode_responses=True
    ) as r:
        await r.set('foo', 'bar')
        value = await r.get('foo')
        print(value)
        # bar

asyncio.run(context_example())
```



## Connection pools

For production usage, you should manage connections with a connection pool
rather than opening and closing them individually.
See [Connection pools and multiplexing](https://redis.io/docs/latest/develop/clients/pools-and-muxing)
for more information about how this works.

A `Redis` client instance already creates and manages its own connection
pool internally, so in a long-running async application the recommended
pattern is to create a single client at startup, share it across requests
and tasks, and close it at shutdown. Avoid creating a new `Redis()` per
request — it defeats pooling and pays the connection cost on every call.

Foundational: Create and share a single async client across the app

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
async def shared_client_example():
    # Create one client at startup. It owns its own internal pool,
    # which is sized by max_connections.
    r = redis.Redis(
        host='localhost', port=6379, decode_responses=True,
        max_connections=10,
    )
    try:
        # Share `r` across every request and task for the app's lifetime.
        await r.set('foo', 'bar')
        value = await r.get('foo')
        print(value)
        # bar
    finally:
        # Close the client at shutdown to release pooled connections.
        await r.aclose()

asyncio.run(shared_client_example())
```



Tune `max_connections` to the maximum number of concurrent Redis operations
you expect from the process. If you'd rather block on pool exhaustion than
raise an error, construct the client with a `BlockingConnectionPool`.

> [!NOTE]
> Don't share a single `ConnectionPool` across multiple `Redis(connection_pool=...)`
> instances. Closing any one of those clients also closes the shared pool,
> which silently invalidates the connections held by every other client using
> it. Share the `Redis` client object instead.

## Awaiting commands

Every command method on the async client returns a coroutine — each call
must be `await`ed. Forgetting `await` returns a coroutine object instead of
a result, which is the most common async mistake to watch for.

Because each command is a coroutine, you can run several concurrently with
`asyncio.gather()`:

Run several Redis commands concurrently with asyncio.gather

**Difficulty:** Intermediate

**Available in:** Python

##### Python

```python
async def gather_example():
    async with redis.Redis(
        host='localhost', port=6379, decode_responses=True
    ) as r:
        await r.mset({'a': '1', 'b': '2', 'c': '3'})
        a, b, c = await asyncio.gather(
            r.get('a'),
            r.get('b'),
            r.get('c'),
        )
        print(a, b, c)
        # 1 2 3

asyncio.run(gather_example())
```



Each in-flight command consumes one pooled connection while it's executing,
so size `max_connections` to match your peak concurrency. (If you instantiate
the client with `single_connection_client=True`, all commands serialize
through a single connection instead.)

## Pipelines and transactions

Pipelines and transactions work the same way as in the synchronous client
(see [Pipelines and transactions](https://redis.io/docs/latest/develop/clients/redis-py/transpipe)
for the conceptual background). The only difference is that you create the
pipeline inside an `async with` block and `await pipe.execute()`.

Foundational: Execute commands in an async pipeline

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
async def pipeline_example():
    async with redis.Redis(
        host='localhost', port=6379, decode_responses=True
    ) as r:
        async with r.pipeline(transaction=True) as pipe:
            pipe.set('a', '1')
            pipe.set('b', '2')
            pipe.get('a')
            pipe.get('b')
            results = await pipe.execute()
            print(results)
            # [True, True, '1', '2']

asyncio.run(pipeline_example())
```



`WATCH`/`MULTI`/`EXEC` for optimistic locking also has an async form.
`watch()` and `execute()` are coroutines; `multi()` remains synchronous
because it only toggles internal pipeline state.

Optimistic locking with an async pipeline and WATCH

**Difficulty:** Intermediate

**Available in:** Python

##### Python

```python
from redis.exceptions import WatchError

async def watch_example():
    async with redis.Redis(
        host='localhost', port=6379, decode_responses=True
    ) as r:
        await r.set('counter', '0')
        async with r.pipeline(transaction=True) as pipe:
            while True:
                try:
                    await pipe.watch('counter')
                    current = int(await pipe.get('counter'))
                    pipe.multi()
                    pipe.set('counter', str(current + 1))
                    await pipe.execute()
                    break
                except WatchError:
                    continue
        print(await r.get('counter'))
        # 1

asyncio.run(watch_example())
```



## Pub/Sub

The async pub/sub object follows the same shape as the sync version. Call
`await pubsub.subscribe(...)` to register channels, then iterate messages
with `async for message in pubsub.listen():`. Use the `PubSub` object as an
async context manager (`async with r.pubsub() as pubsub:`) or call
`await pubsub.aclose()` explicitly to release the connection.

Subscribe and receive messages with the async pub/sub API

**Difficulty:** Intermediate

**Available in:** Python

##### Python

```python
async def pubsub_example():
    async with redis.Redis(
        host='localhost', port=6379, decode_responses=True
    ) as r:
        async with r.pubsub() as pubsub:
            await pubsub.subscribe('channel-1')

            async def reader():
                async for message in pubsub.listen():
                    if message['type'] == 'message':
                        print(message['data'])
                        # hello
                        break

            reader_task = asyncio.create_task(reader())
            await asyncio.sleep(0.1)
            await r.publish('channel-1', 'hello')
            await reader_task

asyncio.run(pubsub_example())
```



A single `PubSub` object isn't safe to share across tasks — give each
consuming task its own subscription.

## Cluster connections

To connect to a Redis cluster asynchronously, import `RedisCluster` from
`redis.asyncio.cluster`. The API matches the synchronous cluster client
(see [Connect to a Redis cluster](https://redis.io/docs/latest/develop/clients/redis-py/connect#connect-to-a-redis-cluster)),
with `await` in front of each command.

Foundational: Connect to a Redis cluster with the async client

**Difficulty:** Beginner

**Available in:** Python

##### Python

```python
from redis.asyncio.cluster import RedisCluster

async def cluster_example():
    rc = RedisCluster(host='localhost', port=16379, decode_responses=True)
    await rc.set('foo', 'bar')
    value = await rc.get('foo')
    print(value)
    # bar
    await rc.aclose()

asyncio.run(cluster_example())
```



## Cleanup and lifecycle

Always close clients and pools when you're done:

- Use `async with Redis(...) as r:` whenever the client's lifetime fits a
  single scope.
- For longer-lived clients, call `await r.aclose()` explicitly. (The older
  `close()` method is deprecated.)
- For frameworks with startup/shutdown hooks — for example [FastAPI](https://redis.io/docs/latest/integrate/fastapi)'s
  `lifespan` — create the client or pool at startup and close it at
  shutdown so connections aren't leaked between process restarts.

## Cancellation and timeouts

You can cancel an in-flight command by wrapping it in `asyncio.wait_for()`
(or `asyncio.timeout()` on Python 3.11+). If the command is canceled
mid-flight, `redis-py` disconnects the underlying connection to avoid
response/request misalignment on subsequent reads. The next command
transparently picks up a new connection from the pool.

Apply an asyncio timeout to a Redis command

**Difficulty:** Intermediate

**Available in:** Python

##### Python

```python
async def timeout_example():
    async with redis.Redis(
        host='localhost', port=6379, decode_responses=True
    ) as r:
        try:
            # BLPOP blocks waiting for a value, so the timeout reliably fires.
            await asyncio.wait_for(r.blpop('empty-queue'), timeout=0.1)
        except asyncio.TimeoutError:
            print('command canceled')

asyncio.run(timeout_example())
```



A `Redis` client instance is safe to share across tasks (the pool handles
concurrency), but stateful objects derived from it — pipelines and pub/sub
subscriptions — are not. Give each task its own pipeline or `PubSub`.

## Translating sync examples

To adapt any synchronous example elsewhere in this guide to the async
client, apply these rules:

- Replace `import redis` with `import redis.asyncio as redis`.
- Wrap the example in an `async def` function and call it with
  `asyncio.run(...)`.
- Add `await` in front of every command call. (Exception: buffered pipeline
  commands such as `pipe.set(...)` stay un-awaited; only `pipe.watch(...)`,
  any reads issued before `pipe.multi()`, and `pipe.execute()` are awaited.)
- Replace `with r.pipeline(...) as pipe:` with
  `async with r.pipeline(...) as pipe:`, and `await pipe.execute()`.
- Replace `r.close()` with `await r.aclose()`, or use
  `async with redis.Redis(...) as r:` as a context manager.

## More information

- The [`redis-py` asyncio examples](https://redis.readthedocs.io/en/stable/examples/asyncio_examples.html)
  on Read the Docs cover further patterns.
- See [Error handling](https://redis.io/docs/latest/develop/clients/redis-py/error-handling) and
  [Client-side geographic failover](https://redis.io/docs/latest/develop/clients/redis-py/failover) for
  resiliency patterns that apply to both sync and async clients.

