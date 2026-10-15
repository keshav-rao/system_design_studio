# Use the LangCache API and SDK

```json metadata
{
  "schema_version": 2,
  "title": "Use the LangCache API and SDK",
  "description": "Learn to use the Redis LangCache API for semantic caching.",
  "categories": ["docs","develop","ai"],
  "tableOfContents": {"sections":[{"id":"authentication","title":"Authentication"},{"children":[{"id":"search-langcache-for-similar-responses","title":"Search LangCache for similar responses"},{"id":"store-a-new-response-in-langcache","title":"Store a new response in LangCache"},{"id":"delete-cached-responses","title":"Delete cached responses"},{"id":"flush-the-cache","title":"Flush the cache"}],"id":"examples","title":"Examples"}]}

,
  "codeExamples": [{"codetabsId":"langcache_sdk-stepimports_setup","description":"Foundational: Authenticate with the LangCache API using Bearer token authorization in the request header","difficulty":"beginner","id":"imports_setup","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_langcache_sdk-stepimports_setup"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_langcache_sdk-stepimports_setup"},{"id":"Node-js","panelId":"panel_Nodejs_langcache_sdk-stepimports_setup"}]},{"codetabsId":"langcache_sdk-stepsearch_basic","description":"Foundational: Search the cache for semantically similar responses to a user prompt","difficulty":"beginner","id":"search_basic","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_langcache_sdk-stepsearch_basic"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_langcache_sdk-stepsearch_basic"},{"id":"Node-js","panelId":"panel_Nodejs_langcache_sdk-stepsearch_basic"}]},{"codetabsId":"langcache_sdk-stepsearch_attributes","description":"Filter responses: Filter cached responses by custom attributes to scope search results to specific contexts or metadata","difficulty":"intermediate","id":"search_attributes","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_langcache_sdk-stepsearch_attributes"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_langcache_sdk-stepsearch_attributes"},{"id":"Node-js","panelId":"panel_Nodejs_langcache_sdk-stepsearch_attributes"}]},{"codetabsId":"langcache_sdk-stepsearch_strategies","description":"Hybrid search: Combine exact and semantic search strategies to find both identical and semantically similar cached responses","difficulty":"intermediate","id":"search_strategies","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_langcache_sdk-stepsearch_strategies"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_langcache_sdk-stepsearch_strategies"},{"id":"Node-js","panelId":"panel_Nodejs_langcache_sdk-stepsearch_strategies"}]},{"codetabsId":"langcache_sdk-stepstore_basic","description":"Foundational: Store a new LLM response in the cache with its corresponding prompt for future retrieval","difficulty":"beginner","id":"store_basic","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_langcache_sdk-stepstore_basic"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_langcache_sdk-stepstore_basic"},{"id":"Node-js","panelId":"panel_Nodejs_langcache_sdk-stepstore_basic"}]},{"codetabsId":"langcache_sdk-stepstore_attributes","description":"Custom attributes: Store cached responses with custom attributes to enable filtering and scoping of future searches","difficulty":"intermediate","id":"store_attributes","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_langcache_sdk-stepstore_attributes"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_langcache_sdk-stepstore_attributes"},{"id":"Node-js","panelId":"panel_Nodejs_langcache_sdk-stepstore_attributes"}]},{"codetabsId":"langcache_sdk-stepdelete_entry","description":"Foundational: Delete a specific cached response by its entry ID when you need to remove outdated or incorrect cache entries","difficulty":"beginner","id":"delete_entry","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_langcache_sdk-stepdelete_entry"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_langcache_sdk-stepdelete_entry"},{"id":"Node-js","panelId":"panel_Nodejs_langcache_sdk-stepdelete_entry"}]},{"codetabsId":"langcache_sdk-stepdelete_query","description":"Delete by attribute: Delete multiple cached responses based on attribute filters when you need to remove entries matching specific criteria","difficulty":"intermediate","id":"delete_query","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_langcache_sdk-stepdelete_query"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_langcache_sdk-stepdelete_query"},{"id":"Node-js","panelId":"panel_Nodejs_langcache_sdk-stepdelete_query"}]},{"codetabsId":"langcache_sdk-stepflush","description":"Flush cache: Clear all cached responses from the cache in a single operation (use with caution as this cannot be undone)","difficulty":"advanced","id":"flush","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_langcache_sdk-stepflush"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_langcache_sdk-stepflush"},{"id":"Node-js","panelId":"panel_Nodejs_langcache_sdk-stepflush"}]}]
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


Use the [LangCache API](https://redis.io/docs/latest/develop/ai/context-engine/langcache/api-reference) from your client app to store and retrieve LLM, RAG, or agent responses.

You can use any standard REST client or library to access the API. If your app is written in Python or Javascript, you can also use the LangCache Software Development Kits (SDKs) to access the API:

- [LangCache SDK for Python](https://pypi.org/project/langcache/)
- [LangCache SDK for Javascript](https://www.npmjs.com/package/@redis-ai/langcache)

## Authentication

To access the LangCache API, you need:

- LangCache API base URL
- LangCache service API key
- Cache ID

When you call the API, you need to pass the LangCache API key in the `Authorization` header as a Bearer token and the Cache ID as the `cacheId` path parameter.

For example:

Foundational: Authenticate with the LangCache API using Bearer token authorization in the request header

**Difficulty:** Beginner

**Available in:** Redis CLI, JavaScript (Node.js), Python

##### Redis CLI

```
curl -s -X POST "https://$HOST/v1/caches/$CACHE_ID/entries/search" \
    -H "accept: application/json" \
    -H "Authorization: Bearer $API_KEY" \
    -d '{ "prompt": "What is semantic caching" }'
```

##### JavaScript (Node.js)

```javascript
import { LangCache } from "@redis-ai/langcache";

const langCache = new LangCache({
    serverURL: "https://" + process.env.HOST,
    cacheId: process.env.CACHE_ID,
    apiKey: process.env.API_KEY,
  });
```

##### Python

```python
from langcache import LangCache
import os

lang_cache = LangCache(
    server_url=f"https://{os.getenv('HOST', '')}",
    cache_id=os.getenv("CACHE_ID", ""),
    api_key=os.getenv("API_KEY", "")
)
```



This example expects several variables to be set in the shell:

- **$HOST** - the LangCache API base URL
- **$CACHE_ID** - the Cache ID of your cache
- **$API_KEY** - The LangCache API token

## Examples

### Search LangCache for similar responses

Use [`POST /v1/caches/{cacheId}/entries/search`](https://redis.io/docs/latest/develop/ai/context-engine/langcache/api-reference#tag/Cache-Entries/operation/search) to search the cache for matching responses to a user prompt.

Foundational: Search the cache for semantically similar responses to a user prompt

**Difficulty:** Beginner

**Available in:** Redis CLI, JavaScript (Node.js), Python

##### Redis CLI

```
POST https://[host]/v1/caches/{cacheId}/entries/search
{
    "prompt": "User prompt text"
}
```

##### JavaScript (Node.js)

```javascript
async function searchBasic() {
    const result = await langCache.search({
      prompt: "User prompt text",
      similarityThreshold: 0.9,
    });

    console.log(result);
}

searchBasic();
```

##### Python

```python
res = lang_cache.search(
    prompt="User prompt text",
    similarity_threshold=0.9
)

print(res)
```



Place this call in your client app right before you call your LLM's REST API. If LangCache returns a response, you can send that response back to the user instead of calling the LLM.

If LangCache does not return a response, you should call your LLM's REST API to generate a new response. After you get a response from the LLM, you can [store it in LangCache](#store-a-new-response-in-langcache) for future use.

#### Attributes
You can also scope the responses returned from LangCache by adding an `attributes` object to the request. LangCache will only return responses that match the attributes you specify.

Filter responses: Filter cached responses by custom attributes to scope search results to specific contexts or metadata

**Difficulty:** Intermediate

**Available in:** Redis CLI, JavaScript (Node.js), Python

##### Redis CLI

```
POST https://[host]/v1/caches/{cacheId}/entries/search
{
    "prompt": "User prompt text",
    "attributes": {
        "customAttributeName": "customAttributeValue"
    }
}
```

##### JavaScript (Node.js)

```javascript
async function searchAttributes() {
    const result = await langCache.search({
      prompt: "User prompt text",
      attributes: {
        "customAttributeName": "customAttributeValue",
      },
      similarityThreshold: 0.9,
    });

    console.log(result);
}

searchAttributes();
```

##### Python

```python
res = lang_cache.search(
    prompt="User prompt text",
    attributes={"customAttributeName": "customAttributeValue"},
    similarity_threshold=0.9,
)

print(res)
```



#### Search strategies
LangCache supports two search strategies when looking for a cached response:

- **`exact`**: Returns a result only when the stored prompt matches the query exactly (case insensitive).
- `**semantic**`: Uses vector similarity to find semantically similar prompts and responses.

By default, LangCache uses `semantic` search only. You can specify one or more search strategies in the request body.

Hybrid search: Combine exact and semantic search strategies to find both identical and semantically similar cached responses

**Difficulty:** Intermediate

**Available in:** Redis CLI, JavaScript (Node.js), Python

##### Redis CLI

```
POST https://[host]/v1/caches/{cacheId}/entries/search
{
    "prompt": "User prompt text",
    "searchStrategies": ["exact", "semantic"]
}
```

##### JavaScript (Node.js)

```javascript
import { SearchStrategy } from '@redis-ai/langcache/models/searchstrategy.js';

async function searchStrategies() {
    const result = await langCache.search({
      prompt: "User prompt text",
      searchStrategies: [SearchStrategy.Exact, SearchStrategy.Semantic],
      similarityThreshold: 0.9,
    });

    console.log(result);
}

searchStrategies();
```

##### Python

```python
from langcache.models import SearchStrategy

res = lang_cache.search(
    prompt="User prompt text",
    search_strategies=[SearchStrategy.EXACT, SearchStrategy.SEMANTIC],
    similarity_threshold=0.9,
)

print(res)
```



### Store a new response in LangCache

Use [`POST /v1/caches/{cacheId}/entries`](https://redis.io/docs/latest/develop/ai/context-engine/langcache/api-reference#tag/Cache-Entries/operation/set) to store a new response in the cache.

Foundational: Store a new LLM response in the cache with its corresponding prompt for future retrieval

**Difficulty:** Beginner

**Available in:** Redis CLI, JavaScript (Node.js), Python

##### Redis CLI

```
POST https://[host]/v1/caches/{cacheId}/entries
{
    "prompt": "User prompt text",
    "response": "LLM response text"
}
```

##### JavaScript (Node.js)

```javascript
async function storeBasic() {
    const result = await langCache.set({
      prompt: "User prompt text",
      response: "LLM response text",
    });

    console.log(result);
}

storeBasic();
```

##### Python

```python
res = lang_cache.set(
    prompt="User prompt text",
    response="LLM response text",
)

print(res)
```



Place this call in your client app after you get a response from the LLM. This will store the response in the cache for future use.

You can also store the responses with custom attributes by adding an `attributes` object to the request.

Custom attributes: Store cached responses with custom attributes to enable filtering and scoping of future searches

**Difficulty:** Intermediate

**Available in:** Redis CLI, JavaScript (Node.js), Python

##### Redis CLI

```
POST https://[host]/v1/caches/{cacheId}/entries
{
    "prompt": "User prompt text",
    "response": "LLM response text",
    "attributes": {
        "customAttributeName": "customAttributeValue"
    }
}
```

##### JavaScript (Node.js)

```javascript
async function storeAttributes() {
    const result = await langCache.set({
      prompt: "User prompt text",
      response: "LLM response text",
      attributes: {
        "customAttributeName": "customAttributeValue",
      },
    });

    console.log(result);
}

storeAttributes();
```

##### Python

```python
res = lang_cache.set(
    prompt="User prompt text",
    response="LLM response text",
    attributes={"customAttributeName": "customAttributeValue"},
)

print(res)
```



### Delete cached responses

Use [`DELETE /v1/caches/{cacheId}/entries/{entryId}`](https://redis.io/docs/latest/develop/ai/context-engine/langcache/api-reference#tag/Cache-Entries/operation/delete) to delete a cached response from the cache.

Foundational: Delete a specific cached response by its entry ID when you need to remove outdated or incorrect cache entries

**Difficulty:** Beginner

**Available in:** Redis CLI, JavaScript (Node.js), Python

##### Redis CLI

```
DELETE https://[host]/v1/caches/{cacheId}/entries/{entryId}
```

##### JavaScript (Node.js)

```javascript
async function deleteEntry() {
    const result = await langCache.deleteById({
      entryId: "<entryId>",
    });

    console.log(result);
}

deleteEntry();
```

##### Python

```python
res = lang_cache.delete_by_id(entry_id="<entryId>")

print(res)
```



You can also use [`DELETE /v1/caches/{cacheId}/entries`](https://redis.io/docs/latest/develop/ai/context-engine/langcache/api-reference#tag/Cache-Entries/operation/deleteQuery) to delete multiple cached responses based on the `attributes` you specify. If you specify multiple `attributes`, LangCache will delete entries that contain all given attributes.

> [!WARNING]
> If you do not specify any `attributes`, all responses in the cache will be deleted. This cannot be undone.

<br/>

Delete by attribute: Delete multiple cached responses based on attribute filters when you need to remove entries matching specific criteria

**Difficulty:** Intermediate

**Available in:** Redis CLI, JavaScript (Node.js), Python

##### Redis CLI

```
DELETE https://[host]/v1/caches/{cacheId}/entries
{
    "attributes": {
        "customAttributeName": "customAttributeValue"
    }
}
```

##### JavaScript (Node.js)

```javascript
async function deleteQuery() {
    const result = await langCache.deleteQuery({
      attributes: {
        "customAttributeName": "customAttributeValue",
      },
    });

    console.log(result);
}

deleteQuery();
```

##### Python

```python
res = lang_cache.delete_query(
    attributes={"customAttributeName": "customAttributeValue"},
)

print(res)
```



### Flush the cache

Use
[POST /v1/caches/{cacheId}/flush](https://redis.io/docs/latest/develop/ai/context-engine/langcache/api-reference/#tag/Cache-Entries/operation/flush)
to flush all entries from the cache.

Flush cache: Clear all cached responses from the cache in a single operation (use with caution as this cannot be undone)

**Difficulty:** Advanced

**Available in:** Redis CLI, JavaScript (Node.js), Python

##### Redis CLI

```
POST https://[host]/v1/caches/{cacheId}/flush
```

##### JavaScript (Node.js)

```javascript
async function flush() {
    await langCache.flush();
}

flush();
```

##### Python

```python
lang_cache.flush()
```



