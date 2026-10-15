# Redis Context Retriever on Redis Cloud

```json metadata
{
  "schema_version": 2,
  "title": "Redis Context Retriever on Redis Cloud",
  "description": "Expose schema-first retrieval tools from your Redis Cloud data to AI agents.",
  "categories": ["docs","operate","iris"],
  "tableOfContents": {"sections":[{"id":"get-started-with-context-retriever-on-redis-cloud","title":"Get started with Context Retriever on Redis Cloud"},{"id":"get-started-with-self-managed-context-retriever","title":"Get started with self-managed Context Retriever"}]}

,
  "codeExamples": []
}
```


Redis Context Retriever helps teams expose operational context to AI agents through schema-first retrieval. It models the entities, fields, keys, and relationships that matter to an agent workflow, then presents that context through a governed tool surface the agent can call at runtime. Context Retriever helps an AI agent understand what business objects exist, how they connect, and which paths are safe to use.

![The Context Retriever page in the Redis Cloud console, with Create with CLI and Create custom service options.](https://redis.io/docs/latest/images/rc/context-retriever-get-started.png)

When you set up Redis Context Retriever, you model the objects that matter to your agent workflow and connect the relationships between them. You can do this through the UI, the [Context Surfaces Python Client](https://pypi.org/project/redis-context-retriever/), or the `ctxctl` CLI (available when you install the Python client). Context Retriever uses those relationships to automatically create and deploy retrieval tools from your entity model.

When an agent needs context during execution, it calls the MCP tools Context Retriever exposes. Instead of guessing which tool to use or generating SQL, the agent follows the defined entity paths and gets back structured, live, operational context.

For more details, see the [Redis Context Retriever overview](https://redis.io/docs/latest/develop/ai/context-engine/context-retriever).

## Get started with Context Retriever on Redis Cloud

To set up a Redis Context Retriever on Redis Cloud, you need a database on Redis Cloud that already has relevant data. If you use a relational database, use [Redis Data Integration (RDI)](https://redis.io/docs/latest/operate/rc/rdi) to ingest data into a Redis Cloud database.

When you have a database, [Create a context retriever service](https://redis.io/docs/latest/operate/iris/context-retriever/create-service) for your database on Redis Cloud.

After you set up Context Retriever, you can [view your service](https://redis.io/docs/latest/operate/iris/context-retriever/view-service). See the [Context Surfaces Python Client](https://pypi.org/project/redis-context-retriever/) for more information on how to call your tools.

## Get started with self-managed Context Retriever

To deploy Context Retriever on your own Kubernetes infrastructure instead of Redis Cloud, see [self-managed Context Retriever](https://redis.io/docs/latest/operate/iris/context-retriever/self-managed).

