# Redis Search

```json metadata
{
  "schema_version": 2,
  "title": "Redis Search",
  "description": "Searching and querying Redis data using Redis Search",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"enable-redis-search","title":"Enable Redis Search"},{"id":"license-and-source-code","title":"License and source code"}]}

,
  "codeExamples": []
}
```


Redis Search offers an enhanced Redis experience via the following search and query features:

- A rich query language
- Incremental indexing on JSON and hash documents
- Vector search
- Full-text search
- Geospatial queries
- Aggregations

You can find a complete list of features in the [reference documentation](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts).

Redis Search features allow you to use Redis as a:

- Document database
- Vector database
- Secondary index
- Search engine

Here are the next steps to get you started:

1. Follow our [quick start guide](https://redis.io/docs/latest/develop/get-started/search-tutorial) to get some initial hands-on experience.
1. Learn how to [create an index](https://redis.io/docs/latest/develop/ai/search-and-query/indexing).
1. Learn how to [query your data](https://redis.io/docs/latest/develop/ai/search-and-query/query).
1. [Install Redis Insight](https://redis.io/docs/latest/operate/redisinsight), connect it to your Redis database, and then use [Redis Copilot](https://redis.io/docs/latest/develop/tools/insight#redis-copilot) to help you learn how to execute complex queries against your own data using simple, plain language prompts.
1. Open the [AI agent builder](https://redis.io/docs/latest/develop/ai/agent-builder) and choose the **Knowledge Assistant** template to generate a working RAG agent built on Redis vector search.

> [!TIP]
> See Redis vector search in a real workflow: [Redis Repo Memory](https://github.com/marketplace/actions/redis-repo-memory) is a GitHub Action that surfaces related past PRs, issues, and commits on every pull request. Add it to any repository in a few minutes.

## Enable Redis Search

Redis Search is available in Redis Open Source, Redis Software, and Redis Cloud.
See
[Install Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack) or
[Install Redis Software](https://redis.io/docs/latest/operate/rs/installing-upgrading/install)
for full installation instructions.

> [!NOTE] Try it out
> Experiment with Redis Search interactively in the [Redis playground](https://redis.io/try/sandbox) — no installation required.

## License and source code

The Redis Search features of Redis are available under the Source Available License 2.0 (RSALv2), the Server Side Public License v1 (SSPLv1), or the GNU Affero General Public License version 3 (AGPLv3). Please read the [license file](https://raw.githubusercontent.com/RediSearch/RediSearch/master/LICENSE.txt) for further details. The source code and the [detailed release notes](https://github.com/RediSearch/RediSearch/releases) are available on [GitHub](https://github.com/RediSearch/RediSearch).

Do you have questions? Feel free to ask at the [RediSearch forum](https://forum.redis.com/c/modules/redisearch/).

<br/>

