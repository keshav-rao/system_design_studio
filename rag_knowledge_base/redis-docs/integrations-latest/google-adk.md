# Redis with Google Agent Development Kit (ADK)

```json metadata
{
  "schema_version": 2,
  "title": "Redis with Google Agent Development Kit (ADK)",
  "description": "Build AI agents with persistent memory, semantic search, and caching using Redis and Google ADK.",
  "categories": ["docs","integrate","oss","rs","rc"],
  "group": "ai",
  "tableOfContents": {"sections":[{"id":"architecture","title":"Architecture"},{"id":"prerequisites","title":"Prerequisites"},{"id":"installation","title":"Installation"},{"id":"quick-start","title":"Quick start"},{"id":"capabilities","title":"Capabilities"},{"id":"more-info","title":"More info"}]}

,
  "codeExamples": []
}
```


[Google Agent Development Kit (ADK)](https://google.github.io/adk-docs/) provides clean abstractions for building AI agents: interfaces for memory, sessions, tools, and callbacks. [adk-redis](https://github.com/redis-developer/adk-redis) implements these interfaces using Redis, giving agents persistent two-tier memory, semantic search for RAG, and response caching without requiring changes to agent logic.

## Architecture

adk-redis connects several backend systems to the ADK framework:

- **[Redis Agent Memory](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory)** handles working memory (sessions), long-term memory (extracted facts), auto-summarization, and memory search. Use the default `redis-agent-memory` for new work. It runs either on [Redis Cloud](https://redis.io/docs/latest/operate/rc/context-engine/agent-memory) or [self-managed](https://redis.io/docs/latest/operate/iris/agent-memory/self-managed) on your own Kubernetes cluster; both share one Data Plane API, so you pick a deployment by pointing `api_base_url` at the right endpoint.
- **[RedisVL](https://redis.io/docs/latest/develop/ai/redisvl)** (Redis Vector Library) powers the search tools and local semantic cache provider.
- **[LangCache](https://redis.io/langcache/)** provides managed semantic caching with server-side embeddings.

> [!NOTE]
> [Agent Memory Server](https://github.com/redis/agent-memory-server)
> (`opensource-agent-memory`) is now deprecated. If you have an existing
> deployment, see
> [Agent Memory Server (deprecated)](https://redis.io/docs/latest/integrate/google-adk/agent-memory-server),
> which also covers migrating to Redis Agent Memory.

## Prerequisites

- **Redis 8.4+** with vector search support, for the search tools and the local semantic cache
- **A [Redis Agent Memory](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory) store**, for the session and memory services, which gives you a Data Plane endpoint, an API key, and a store ID

Provision a store, then pass its Data Plane endpoint, API key, and store ID to the services.

- On **Redis Cloud**, there is nothing to run. See [Create an Agent Memory service](https://redis.io/docs/latest/operate/iris/agent-memory/create-service).
- To run it **yourself**, see [Self-managed Agent Memory](https://redis.io/docs/latest/operate/iris/agent-memory/self-managed) for deployment, configuration, and operations on your own Kubernetes cluster.

Both use `backend="redis-agent-memory"`. Only `api_base_url` differs.

## Installation

```bash
# Memory and session services (both backends)
pip install adk-redis[memory]

# Search tools via RedisVL
pip install adk-redis[search]

# SQL-style search tool (sql-redis)
pip install adk-redis[sql]

# Managed semantic caching via LangCache
pip install adk-redis[langcache]

# Everything
pip install adk-redis[all]

# For the RedisVL MCP server (used with ADK's native McpToolset)
pip install 'redisvl[mcp]>=0.18.2'
```

The `memory` extra requires `redis-agent-memory>=0.2.0`.

## Quick start

Wire up Redis Agent Memory in a few lines:

```python
from google.adk import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.runners import Runner
from adk_redis.sessions import (
    RedisSessionMemoryService,
    RedisSessionMemoryServiceConfig,
)
from adk_redis.memory import (
    RedisLongTermMemoryService,
    RedisLongTermMemoryServiceConfig,
)

session_service = RedisSessionMemoryService(
    config=RedisSessionMemoryServiceConfig(
        backend="redis-agent-memory",
        api_base_url="https://your-endpoint.redis.io",
        api_key="your-api-key",
        store_id="your-store-id",
        default_namespace="my_app",
    )
)
memory_service = RedisLongTermMemoryService(
    config=RedisLongTermMemoryServiceConfig(
        backend="redis-agent-memory",
        api_base_url="https://your-endpoint.redis.io",
        api_key="your-api-key",
        store_id="your-store-id",
        default_namespace="my_app",
    )
)

async def after_agent(callback_context: CallbackContext):
    await callback_context.add_session_to_memory()

agent = Agent(
    name="my_agent",
    model="gemini-2.5-flash",
    instruction="You are a helpful assistant with long-term memory.",
    after_agent_callback=after_agent,
)

runner = Runner(
    agent=agent,
    app_name="my_app",
    session_service=session_service,
    memory_service=memory_service,
)
```

## Capabilities

| Capability | Description | Page |
|------------|-------------|------|
| **Redis Agent Memory** | Session and long-term memory on Redis Cloud or self-managed, via framework services or REST tools | [Redis Agent Memory](https://redis.io/docs/latest/integrate/google-adk/redis-agent-memory) |
| **Integration patterns** | Framework-managed, LLM-controlled REST, and MCP tools | [Integration patterns](https://redis.io/docs/latest/integrate/google-adk/integration-patterns) |
| **Search tools** | Vector, hybrid, text, range, and SQL search via RedisVL, plus the `rvl mcp` server over `McpToolset` | [Search tools](https://redis.io/docs/latest/integrate/google-adk/search-tools) |
| **Semantic caching** | LLM response and tool result caching, with stable entry IDs and targeted invalidation | [Semantic caching](https://redis.io/docs/latest/integrate/google-adk/semantic-caching) |
| **Examples** | Complete examples covering all capabilities | [Examples](https://redis.io/docs/latest/integrate/google-adk/examples) |
| **Agent Memory Server** (deprecated) | Reference for the deprecated `opensource-agent-memory` backend, and how to migrate off it | [Agent Memory Server (deprecated)](https://redis.io/docs/latest/integrate/google-adk/agent-memory-server) |

## More info

- [adk-redis on GitHub](https://github.com/redis-developer/adk-redis)
- [adk-redis on PyPI](https://pypi.org/project/adk-redis/)
- [Car dealership tutorial](https://redis.io/tutorials/build-a-car-dealership-agent-with-google-adk-and-redis-agent-memory/)
- [RedisVL documentation](https://redis.io/docs/latest/develop/ai/redisvl)
- [Google ADK documentation](https://google.github.io/adk-docs/)

