# JSON.TYPE

```json metadata
{
  "schema_version": 2,
  "title": "JSON.TYPE",
  "description": "Returns the type of the JSON value at path",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"path","optional":true,"type":"string"}],
  "syntax_fmt": "JSON.TYPE key [path]",
  "complexity": "O(1) when path is evaluated to a single value, O(N) when path is evaluated to multiple values, where N is the size of the key",
  "group": "json",
  "acl_categories": ["@json","@read","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Report the type of JSON value at `path`

The returned type is one of the following strings:

| Type | Description |
|:-----|:------------|
| `null` | A JSON null value. |
| `boolean` | A JSON `true` or `false` value. |
| `integer` | A number with no fractional part. |
| `number` | A number with a fractional part (a floating-point value). <sup>[1](#table-note-1)</sup>|
| `string` | A JSON string value. |
| `object` | A JSON object (a collection of key-value pairs). |
| `array` | A JSON array (an ordered list of values). |

1. <a name="table-note-1"></a>
A floating-point homogeneous array (FPHA) stored with the [`JSON.SET`](https://redis.io/docs/latest/commands/json.set) `FPHA` argument still reports as `array`, and its elements report as `number`. The FP type (`FP16`, `BF16`, `FP32`, or `FP64`) is an internal storage representation and is not exposed by `JSON.TYPE`.

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary> 

is key to parse.
</details>

## Optional arguments

<details open><summary><code>path</code></summary> 

is JSONPath to specify. Default is root `$`. Returns null if the `key` or `path` do not exist.

</details>

## Examples


redis> JSON.SET doc $ '{"a":2, "nested": {"a": true}, "foo": "bar"}'
OK
redis> JSON.TYPE doc $..foo
1) "string"
redis> JSON.TYPE doc $..a
1) "integer"
2) "boolean"
redis> JSON.TYPE doc $..dummy
(empty array)


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

With `$`-based path argument: [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings), where each element is the type of the matching value.

With `.`-based path argument: [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) representing the type of the matching value.

**RESP3:**

With `$`-based path argument (default): [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [array replies](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings), where each nested array contains the type of the matching value.

With `.`-based path argument: [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) representing the type of the matching value.



## See also

[`JSON.SET`](https://redis.io/docs/latest/commands/json.set) | [`JSON.ARRLEN`](https://redis.io/docs/latest/commands/json.arrlen) 

## Related topics

* [RedisJSON](https://redis.io/docs/latest/develop/data-types/json)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)

