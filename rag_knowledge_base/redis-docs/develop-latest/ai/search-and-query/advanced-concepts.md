# Search concepts

```json metadata
{
  "schema_version": 2,
  "title": "Search concepts",
  "description": "Details about query syntax, aggregation, scoring, and other search and query options",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"indexing-features","title":"Indexing features"},{"id":"query-features","title":"Query features"},{"id":"full-text-search-features","title":"Full-text search features"},{"id":"cluster-support","title":"Cluster support"},{"id":"supported-platforms","title":"Supported platforms"}]}

,
  "codeExamples": []
}
```


Redis Open Source supports the following Redis Search features. This article provides you an overview.

## Indexing features

* Secondary indexing
* Vector indexing
* Index on [JSON](https://redis.io/docs/latest/develop/data-types/json) documents
* Full-text indexing of multiple fields in a document
* Incremental indexing without performance loss
* Document deletion and updating with index garbage collection


## Query features

* Multi-field queries
* Query on [JSON](https://redis.io/docs/latest/develop/data-types/json) documents
* [Aggregation](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/aggregations)
* Boolean queries with AND, OR, and NOT operators between subqueries
* Optional query clauses
* Retrieval of full document contents or only their IDs
* Exact phrase search and slop-based search
* Numeric filters and ranges
* Geo-filtering using Redis [geo commands](/commands/?group=geo)
* [Vector search](https://redis.io/docs/latest/develop/ai/search-and-query/vectors)
* [Key and field expiration behavior](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/expiration)
* [Search commands in MULTI/EXEC transactions and Lua scripts](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/transactions)


## Full-text search features

* [Prefix-based searches](https://redis.io/docs/latest/develop/ai/search-and-query/query#prefix-matching)
* Field weights
* [Auto-complete](https://redis.io/docs/latest/develop/ai/search-and-query/administration/overview#auto-complete) and fuzzy prefix suggestions
* [Stemming](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/stemming)-based query expansion for [many languages](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/stemming#supported-languages) using [Snowball](http://snowballstem.org/)
* Support for custom functions for query expansion and scoring (see [Extensions](https://redis.io/docs/latest/develop/ai/search-and-query/administration/extensions))
* Unicode support (UTF-8 input required)
* Document ranking

## Cluster support

The Redis Search features of Redis Open Source are also available for distributed databases that can scale to billions of documents and hundreds of servers.

## Supported platforms
Redis Open Source is developed and tested on Linux and macOS on x86_64 CPUs.

Atom CPUs are not supported.

<br/>
