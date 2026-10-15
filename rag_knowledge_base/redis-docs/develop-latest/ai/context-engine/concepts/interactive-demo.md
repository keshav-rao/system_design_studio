# Redis Iris interactive demo

```json metadata
{
  "schema_version": 2,
  "title": "Redis Iris interactive demo",
  "description": "Step through one agent request across Data Integration, LangCache, Agent Memory, and Context Retriever, then take a service away to see what the agent loses.",
  "categories": ["docs","develop","ai"],
  "tableOfContents": {"sections":[{"id":"what-each-service-adds","title":"What each service adds"},{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": []
}
```


Redis Iris gives an AI agent governed access to live business data, memory, and cached answers. This tour follows one customer request through all four services, one step at a time. It starts where business data enters Iris, with Data Integration, and then follows the request through the other three services, in the order described in [How Redis Iris works](https://redis.io/docs/latest/develop/ai/context-engine/concepts). The last step takes one service away to show what the agent loses without it.

The tour runs in your browser and doesn't connect to any service. Each step links to that service's own interactive demo, which covers it in depth with the same customer and data. The agent's reasoning, the reply, and the timings are illustrative.



## What each service adds

| Service | What it does in this request | Without it |
|:--|:--|:--|
| [Data Integration](https://redis.io/docs/latest/develop/ai/context-engine/data-integration) | Syncs a change from PostgreSQL to Redis seconds after it happens | The agent reads last night's data and makes a promise it can't keep |
| [Context Retriever](https://redis.io/docs/latest/develop/ai/context-engine/context-retriever) | Looks up delivery times, alternatives, and past orders through governed tools | The agent can't check whether the food will arrive in time |
| [Agent Memory](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory) | Recalls last week's order and the customer's peanut allergy | The agent can find the order, but not the allergy |
| [LangCache](https://redis.io/docs/latest/develop/ai/context-engine/langcache) | Answers the general delivery fee question from the cache | The model answers it, which takes longer and costs output tokens |

## Next steps

- See [how a request flows through Redis Iris](https://redis.io/docs/latest/develop/ai/context-engine/concepts/request-flow), capability by capability.
- Get started with [Redis Iris on Redis Cloud](https://redis.io/docs/latest/operate/iris).

