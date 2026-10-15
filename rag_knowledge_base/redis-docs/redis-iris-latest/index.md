# Redis Iris context engine

```json metadata
{
  "schema_version": 2,
  "title": "Redis Iris context engine",
  "description": "Deploy and operate Redis Iris context engine services.",
  "categories": ["docs","operate","iris"],
  "tableOfContents": {"sections":[{"children":[{"id":"redis-cloud","title":"Redis Cloud"},{"id":"self-managed","title":"Self-managed"}],"id":"deployment-options","title":"Deployment options"}]}

,
  "codeExamples": []
}
```


Redis Iris context engine provides managed and self-managed services for building AI applications with persistent memory, semantic caching, and governed access to business data.

![The Redis Iris overview page in the Redis Cloud console, with cards for Data Pipelines, Context Retriever, Agent Memory, and LangCache.](https://redis.io/docs/latest/images/rc/iris-overview.png)

Use this section to deploy, configure, and operate Redis Iris services. Developer guides and API integration documentation remain under [Develop with Redis](https://redis.io/docs/latest/develop/ai/context-engine).

<div class="grid grid-cols-1 md:grid-cols-3 gap-6 my-8">
  
  
  
</div>

## Deployment options

Redis Iris services are available as managed services on Redis Cloud. All Redis Iris services are also available for self-managed deployment.

### Redis Cloud

Create and manage Redis Iris services through the Redis Cloud console without deploying the supporting infrastructure yourself.

- [Create a Redis Agent Memory service](https://redis.io/docs/latest/operate/iris/agent-memory/create-service)
- [Create a Redis Context Retriever service](https://redis.io/docs/latest/operate/iris/context-retriever/create-service)
- [Create a LangCache service](https://redis.io/docs/latest/operate/iris/langcache/create-service)

### Self-managed

Deploy Redis Iris services on Kubernetes when you need to operate them on your own infrastructure.

- [Self-managed Redis Agent Memory](https://redis.io/docs/latest/operate/iris/agent-memory/self-managed)
- [Self-managed Redis Context Retriever](https://redis.io/docs/latest/operate/iris/context-retriever/self-managed)
- [Self-managed LangCache](https://redis.io/docs/latest/operate/iris/langcache/self-managed)

