# redis.lookup

```json metadata
{
  "schema_version": 2,
  "title": "redis.lookup",
  "description": "Lookup data from Redis using the given command and key",
  "categories": ["docs","integrate","rs","rdi"],
  "group": "di",
  "tableOfContents": {"sections":[{"id":"batch","title":"batch: object"},{"id":"args","title":"args[]: Redis command arguments"}]}

,
  "codeExamples": []
}
```


**Properties**

| Name                | Type       | Description                                                                                                                                                                                                                                                          | Required |
| ------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| **connection**      | `string`   | Connection name                                                                                                                                                                                                                                                      | yes      |
| **cmd**             | `string`   | The command to execute                                                                                                                                                                                                                                               | yes      |
| [**args**](#args)   | `string[]` | Redis command arguments                                                                                                                                                                                                                                              | yes      |
| **language**        | `string`   | Language<br/>Enum: `"jmespath"`, `"sql"`<br/>                                                                                                                                                                                                                        | yes      |
| **field**           | `string`   | The target field to write the result to<br/>                                                                                                                                                                                                                         | yes      |
| **cache**           | `object`   | Cache the result of the argument expressions. See [`cache`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/cache) for the property list. **Flink processor only.**<br/>                                                            | no       |
| **lookup_cache**    | `object`   | Cache the lookup results returned by Redis across batches, keyed by the resolved command arguments. Uses the same property list as [`cache`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/cache). **Flink processor only.**<br/> | no       |
| [**batch**](#batch) | `object`   | Override the default batching behavior for `redis.lookup` lookups. **Flink processor only.**<br/>                                                                                                                                                                    | no       |

**Additional Properties:** not allowed

**Items**

**Item Type:** `string`

## batch: object {#batch}

`redis.lookup` lookups are always batched and executed through a single Redis pipeline per batch. The processor flushes a batch when either the size or the timeout limit is reached. The defaults are sensible for most pipelines; add the `batch:` block only when you need to override them. **Flink processor only.**

**Properties**

| Name           | Type      | Description                                                                              | Required | Default |
| -------------- | --------- | ---------------------------------------------------------------------------------------- | -------- | ------- |
| **size**       | `integer` | Maximum number of lookups in a single batch. Must be positive.                           | no       | `200`   |
| **timeout_ms** | `integer` | Maximum time in milliseconds to wait before flushing a non-full batch. Must be positive. | no       | `100`   |

**Additional Properties:** not allowed
**Example**

Read a hash field:

```yaml
source:
  table: album
transform:
  - uses: redis.lookup
    with:
      connection: target
      cmd: HGET
      args:
        - concat(['artist:artistid:', artistid])
        - "`name`"
      language: jmespath
      field: artist
output:
  - uses: redis.write
    with:
      connection: target
      data_type: hash
      key:
        expression: concat(['album:albumid:', albumid])
        language: jmespath
```

## args\[\]: Redis command arguments {#args}

The list of expressions that produce arguments.

