# Best practices for scalable Redis Search

```json metadata
{
  "schema_version": 2,
  "title": "Best practices for scalable Redis Search",
  "description": "Best practices for scalable Redis Search in Redis Software and Redis Cloud.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"best-candidates-for-query-performance-factor-improvements","title":"Best candidates for query performance factor improvements"},{"children":[{"id":"improve-indexing","title":"Improve indexing"},{"id":"improve-queries","title":"Improve queries"}],"id":"best-practices","title":"Best practices"},{"children":[{"id":"anti-pattern-index-schema","title":"Anti-pattern index schema"},{"id":"anti-pattern-query","title":"Anti-pattern query"},{"id":"improved-index-schema","title":"Improved index schema"},{"id":"improved-query","title":"Improved query"}],"id":"index-and-query-examples","title":"Index and query examples"},{"children":[{"id":"vector-schema-type","title":"Vector schema type"},{"id":"tag-schema-type","title":"Tag schema type"},{"id":"text-schema-type","title":"Text schema type"},{"id":"numeric-schema-type","title":"Numeric schema type"},{"id":"geo-schema-type","title":"Geo schema type"}],"id":"performance-results","title":"Performance results"}]}

,
  "codeExamples": []
}
```


[Vertical scaling of Redis Search](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/search/query-performance-factor) requires configuring query performance factors. With careful crafting of search indexes and queries, query performance factors allow throughput scaling up to 16X. The following recommendations can help optimize your indexes and queries to maximize the performance benefits from additional CPUs allocated by query performance factors.

## Best candidates for query performance factor improvements

- Query types:

    - [Full-text](https://redis.io/docs/latest/develop/ai/search-and-query/query/full-text)

    - [Tag](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/tags)

    - [Vector](https://redis.io/docs/latest/develop/ai/search-and-query/query/vector-search)

    - [Numeric](https://redis.io/docs/latest/develop/ai/search-and-query/query/range)

    - [Geo](https://redis.io/docs/latest/develop/ai/search-and-query/query/geo-spatial)

- Result set types:

    - Small result sets

    - Document subsets that are indexed in their [non-normalized](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/sorting#normalization-unf-option) form

## Best practices

If query performance factors have not boosted the performance of your queries as much as expected:

1. Verify your index includes all queried and returned fields.

1. Identify and avoid query [anti-patterns](https://redis.io/docs/latest/develop/ai/search-and-query/best-practices/scalable-query-best-practices#anti-patterns) that limit scalability.

1. Follow best practices to [improve indexing](#improve-indexing).

1. Follow best practices to [improve queries](#improve-queries).

### Improve indexing

Follow these best practices for [indexing](https://redis.io/docs/latest/develop/ai/search-and-query/indexing):

- Include fields in the index definition that are used in the query or the required result sets (projections).

- Use `SORTABLE` for all fields returned in result sets.

- Use the `UNF` option for `TAG` and `GEO` fields.

- Use the `NOSTEM` option for `TEXT` fields.

### Improve queries

Follow these best practices to optimize [queries](https://redis.io/docs/latest/develop/ai/search-and-query/query):

- Specify the result set fields in the `RETURN` or `LOAD` clauses and include them in the index definition. Don’t just return the default result set from [`FT.SEARCH`](https://redis.io/docs/latest/commands/ft.search)  or `LOAD *` from [`FT.AGGREGATE`](https://redis.io/docs/latest/commands/ft.aggregate).

- Use `LIMIT` to reduce the result set size.

- Use [`DIALECT 3`](https://redis.io/docs/latest/develop/ai/search-and-query/advanced-concepts/dialects#dialect-3) or higher for any queries against JSON.

## Index and query examples

The following examples depict an anti-pattern index schema and query, followed by a corrected schema and query, which allows for scalability with Redis Search.

### Anti-pattern index schema

The following index schema is not optimized for vertical scaling:

```sh
FT.CREATE jsonidx:profiles ON JSON PREFIX 1 profiles: 
          SCHEMA $.tags.* as t NUMERIC SORTABLE 
                 $.firstName as name TEXT 
                 $.location as loc GEO
```

### Anti-pattern query

The following query is not optimized for vertical scaling:

```sh
FT.AGGREGATE jsonidx:profiles '@t:[1299 1299]' LOAD * LIMIT 0 10
```

### Improved index schema

Here's an improved index schema that follows best practices for vertical scaling:

```sh
FT.CREATE jsonidx:profiles ON JSON PREFIX 1 profiles: 
          SCHEMA $.tags.* as t NUMERIC SORTABLE 
                 $.firstName as name TEXT NOSTEM SORTABLE 
                 $.lastName as lastname TEXT NOSTEM SORTABLE 
                 $.location as loc GEO SORTABLE 
                 $.id as id TAG SORTABLE UNF 
                 $.ver as ver TAG SORTABLE UNF
```

### Improved query

Here's an improved query that follows best practices for vertical scaling:

```sh
FT.AGGREGATE jsonidx:profiles '@t:[1299 1299]' 
                LOAD 6 id t name lastname loc ver
                LIMIT 0 10
                DIALECT 3
```

## Performance results

The following benchmarks show the performance improvements for different query types achieved with query performance factors. Vector, tag, and text queries strongly benefit, while numeric and geographic queries show more limited improvements.

### Vector schema type

#### Vector ingest

| Shards | Threads per shard | CPUs | Speedup factor |
|--------|-------------------|------|----------------|
| 1      | 0                 | 1    | 0              |
| 6      | 0                 | 6    | 6.6            |
| 1      | 6                 | 6    | 2.5            |
| 2      | 6                 | 12   | 6.1            |
| 4      | 6                 | 24   | 24.3           |

#### Vector query

| Shards | Threads per shard | CPUs | Speedup factor |
|--------|-------------------|------|----------------|
| 1      | 0                 | 1    | 0              |
| 6      | 0                 | 6    | 0.8            |
| 1      | 6                 | 6    | 4.7            |
| 2      | 6                 | 12   | 5.1            |
| 4      | 6                 | 24   | 5.6            |

### Tag schema type

| Worker threads | % change |
|----------------|----------|
| 0              | 0        |
| 6              | 135.88   |

### Text schema type

#### Two-word union queries

| Worker threads | Queries per second | % change |
|----------------|--------------------|----------|
| 0              | 188                | 0        |
| 6              | 1,072              | 470      |
| 12             | 1,995              | 961      |
| 18             | 2,834              | 1,407    |

#### Two-word intersection queries

| Worker threads | Queries per second | % change |
|----------------|--------------------|----------|
| 0              | 2,373              | 0        |
| 6              | 12,396             | 422      |
| 12             | 17,506             | 638      |
| 18             | 19,764             | 733      |

#### Simple one-word match

| Worker threads | Queries per second | % change |
|----------------|--------------------|----------|
| 0              | 476                | 0        |
| 6              | 2,837              | 496      |
| 12             | 5,292              | 1,012    |
| 18             | 7,512              | 1,478    |

### Numeric schema type

| Worker threads | Queries per second | % change |
|----------------|--------------------|----------|
| 0              | 33,584             | 0        |
| 1              | 36,993             | 10.15    |
| 3              | 36,504             | 8.69     |
| 6              | 36,897             | 9.86     |

### Geo schema type

#### Geo queries without UNF

| Worker threads | Queries per second | % change |
|----------------|--------------------|----------|
| 0              | 48                 | 0        |
| 6              | 96                 | 100      |
| 12             | 96                 | 100      |
| 18             | 98                 | 104      |

#### Geo queries with UNF

| Worker threads | Queries per second | % change |
|----------------|--------------------|----------|
| 0              | 61                 | 0        |
| 6              | 227                | 272      |
| 12             | 217                | 256      |
| 18             | 217                | 256      |

