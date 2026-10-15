# cache

```json metadata
{
  "schema_version": 2,
  "title": "cache",
  "description": "Cache the result of an expression or lookup",
  "categories": ["docs","integrate","rs","rdi"],
  "group": "di",
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Cache the result of an expression or lookup. Caching avoids re-evaluating
the expression or re-querying Redis when the same input field values
appear repeatedly. Cache keys are derived from the values of the input
fields referenced by the expression, not from the full record.

The `cache:` block can be added to the following transformations and
output expressions:

- The expression in [`add_field`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/add_field) (single-field and per-item form).
- The expression in [`filter`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/filter).
- The expression in [`map`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/map).
- The argument expressions in [`redis.lookup`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/lookup). The same block accepts a `lookup_cache:` variant that caches the lookup result returned by Redis.
- The dynamic `key` and `expire` expressions of the `redis.write` output.

**Flink processor only.** The classic processor silently ignores `cache:` blocks.

**Properties**

| Name            | Type      | Description                                                    | Required | Default |
| --------------- | --------- | -------------------------------------------------------------- | -------- | ------- |
| **enabled**     | `boolean` | Set to `true` to enable caching.                               | no       | `false` |
| **max_size**    | `integer` | Maximum number of entries kept in the cache. Must be positive. | no       | `1000`  |
| **ttl_seconds** | `integer` | Time-to-live for each entry, in seconds. Must be positive.     | no       | `60`    |

**Additional Properties:** not allowed

**Example**

```yaml
source:
  schema: dbo
  table: customer
transform:
  - uses: add_field
    with:
      field: country
      language: sql
      expression: country_code || ' - ' || UPPER(country_name)
      cache:
        enabled: true
        max_size: 500
        ttl_seconds: 300
```

See
[Caching expression results](https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/transform-examples/caching-expression-results)
for additional examples.

