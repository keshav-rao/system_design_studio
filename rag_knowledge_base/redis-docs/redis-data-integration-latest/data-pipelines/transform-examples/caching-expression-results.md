# Caching expression results

```json metadata
{
  "schema_version": 2,
  "title": "Caching expression results",
  "description": "",
  "categories": ["docs","integrate","rs","rdi"],
  "group": "di",
  "tableOfContents": {"sections":[{"id":"the-cache-block","title":"The cache: block"},{"id":"caching-an-add_field-expression","title":"Caching an add_field expression"},{"id":"caching-a-map-expression","title":"Caching a map expression"},{"id":"caching-redislookup-arguments-and-results","title":"Caching redis.lookup arguments and results"},{"id":"caching-key-and-expire-output-expressions","title":"Caching key and expire output expressions"}]}

,
  "codeExamples": []
}
```


The Flink processor can cache the result of any expression that
produces a value (for example, an
[`add_field`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/add_field)
expression, a [`map`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/map)
expression, the arguments to a
[`redis.lookup`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/lookup),
or a custom output `key`/`expire` expression). Caching is useful when
the same expression is evaluated repeatedly with the same input field
values, for example when many incoming records share a common foreign
key.

> [!NOTE]
> Caching is supported only by the **Flink processor**. The
> classic processor silently ignores `cache:` blocks.

## The `cache:` block

You enable caching by adding a `cache:` block next to the expression
you want to cache. Cache keys are derived from the values of the input
fields referenced by the expression, not from the full record. See
[`cache`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/cache)
for the full property list.

| Property      | Type      | Description                                                    | Default |
| ------------- | --------- | -------------------------------------------------------------- | ------- |
| `enabled`     | `boolean` | Set to `true` to enable caching.                               | `false` |
| `max_size`    | `integer` | Maximum number of entries kept in the cache. Must be positive. | `1000`  |
| `ttl_seconds` | `integer` | Time-to-live for each entry, in seconds. Must be positive.     | `60`    |

## Caching an `add_field` expression

The example below adds a `country` field whose value is derived from
`country_code` and `country_name`. When the same combination of input
values appears repeatedly (for example, many customers from the same
country), caching the result avoids re-evaluating the expression.

```yaml
name: Cached country field
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

## Caching a `map` expression

```yaml
name: Cached map expression
source:
  table: customer
transform:
  - uses: map
    with:
      language: jmespath
      expression: |
        {
          "CustomerId": customer_id,
          "Country": country_code
        }
      cache:
        enabled: true
```

## Caching `redis.lookup` arguments and results

`redis.lookup` supports two independent caches. The `cache:` block
caches the *argument* expressions (the JMESPath or SQL expressions
that produce the Redis command arguments). The `lookup_cache:` block
caches the *result* of the Redis command itself, keyed by the
resolved arguments. Both blocks accept the same properties as the
`cache:` block above.

```yaml
name: Cached lookup
source:
  table: order
transform:
  - uses: redis.lookup
    with:
      connection: target
      cmd: HGETALL
      args:
        - concat(['customer:', customer_id])
      language: jmespath
      field: customer
      cache:
        enabled: true
        ttl_seconds: 60
      lookup_cache:
        enabled: true
        max_size: 10000
        ttl_seconds: 300
```

## Caching `key` and `expire` output expressions

A `cache:` block can also be added to the
[output `key` and `expire` expressions](https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/transform-examples)
when those are dynamic. The properties are the same as above.

```yaml
name: Cached key expression
source:
  table: order
output:
  - uses: redis.write
    with:
      data_type: hash
      key:
        expression: concat(['order:', order_id])
        language: jmespath
        cache:
          enabled: true
```

