# Use the LangCache API on Redis Cloud

```json metadata
{
  "schema_version": 2,
  "title": "Use the LangCache API on Redis Cloud",
  "description": "",
  "categories": ["docs","operate","iris"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


You can use the [LangCache API and SDK](https://redis.io/docs/latest/develop/ai/context-engine/langcache/api-examples) from your client app to store and retrieve LLM, RAG, or agent responses. 

To access the LangCache API, you need:

- LangCache API base URL
- LangCache service API key
- Cache ID

For LangCache on Redis Cloud, the base URL and cache ID are available in the LangCache service's **Configuration** page in the [**Connectivity** section](https://redis.io/docs/latest/operate/iris/langcache/view-edit-cache#connectivity).

The LangCache API key is only available immediately after you create the LangCache service. If you lost this value, you will need to [replace the service API key](https://redis.io/docs/latest/operate/iris/langcache/view-edit-cache#replace-service-api-key) to be able to use the LangCache API.

When you call the API, you need to pass the LangCache API key in the `Authorization` header as a Bearer token and the Cache ID as the `cacheId` path parameter. 

See the [LangCache API and SDK examples](https://redis.io/docs/latest/develop/ai/context-engine/langcache/api-examples) for more information on how to use the LangCache API.

