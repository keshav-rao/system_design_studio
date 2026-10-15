# Semantic caching with LangCache on Redis Cloud

```json metadata
{
  "schema_version": 2,
  "title": "Semantic caching with LangCache on Redis Cloud",
  "description": "Store LLM responses for AI applications in Redis Cloud.",
  "categories": ["docs","operate","iris"],
  "tableOfContents": {"sections":[{"id":"get-started-with-langcache-on-redis-cloud","title":"Get started with LangCache on Redis Cloud"},{"id":"get-started-with-self-managed-langcache","title":"Get started with self-managed LangCache"},{"id":"llm-cost-reduction-with-langcache","title":"LLM cost reduction with LangCache"}]}

,
  "codeExamples": []
}
```


LangCache is a semantic caching service available as a REST API that stores LLM responses for fast and cheaper retrieval, built on the Redis vector database. By using semantic caching, you can significantly reduce API costs and lower the average latency of your generative AI applications.

![The LangCache page in the Redis Cloud console, with Quick create and Create custom service options.](https://redis.io/docs/latest/images/rc/langcache-get-started.png)

For more information about how LangCache works, see the [LangCache overview](https://redis.io/docs/latest/develop/ai/context-engine/langcache).

## Get started with LangCache on Redis Cloud

To set up LangCache on Redis Cloud:

1. [Create a database](https://redis.io/docs/latest/operate/rc/databases/create-database) on Redis Cloud.
2. [Create a LangCache service](https://redis.io/docs/latest/operate/iris/langcache/create-service) for your database on Redis Cloud.
3. [Use the LangCache API](https://redis.io/docs/latest/operate/iris/langcache/use-langcache) from your client app.

After you set up LangCache, you can [view and edit the cache](https://redis.io/docs/latest/operate/iris/langcache/view-edit-cache) and [monitor the cache's performance](https://redis.io/docs/latest/operate/iris/langcache/monitor-cache).

See also our [Redis LangCache setup](https://www.youtube.com/watch?v=UOGhMZlZLko)
tutorial video for advice on how to get started.


## Get started with self-managed LangCache

To deploy LangCache on your own Kubernetes infrastructure instead of Redis Cloud, see [self-managed LangCache](https://redis.io/docs/latest/operate/iris/langcache/self-managed).

## LLM cost reduction with LangCache

LangCache reduces your LLM costs by caching responses and avoiding repeated API calls. When a response is served from cache, you don’t pay for output tokens. Input token costs are typically offset by embedding and storage costs.

For every cached response, you'll save the output token cost. To calculate your monthly savings with LangCache, you can use the following formula:

```bash
Est. monthly savings with LangCache = 
    (Monthly output token costs) × (Cache hit rate)
```

The more requests you serve from LangCache, the more you save, because you’re not paying to regenerate the output.

Here’s an example:
- Monthly LLM spend: $200
- Percentage of output tokens in your spend: 60%
- Cost of output tokens: $200 × 60% = $120
- Cache hit rate: 50%
- Estimated savings: $120 × 50% = $60/month

> [!NOTE]
> The formula and numbers above provide a rough estimate of your monthly savings. Actual savings will vary depending on your usage.

You can also use the [LangCache savings calculator](https://redis.io/calculator/langcache/) to estimate your annual savings with LangCache.

