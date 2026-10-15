# JSON.NUMMULTBY

```json metadata
{
  "schema_version": 2,
  "title": "JSON.NUMMULTBY",
  "description": "Multiplies the numeric value at path by a value",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"path","type":"string"},{"name":"value","type":"double"}],
  "syntax_fmt": "JSON.NUMMULTBY key path value",
  "complexity": "O(1) when path is evaluated to a single value, O(N) when path is evaluated to multiple values, where N is the size of the key",
  "group": "json",
  "acl_categories": ["@json","@write","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Multiply the number value stored at `path` by `value`

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary> 

is key to modify.
</details>

<details open><summary><code>path</code></summary> 

is JSONPath to specify.
</details>

<details open><summary><code>value</code></summary> 

is number value to multiply. 
</details>

## Examples


redis> JSON.SET doc . '{"a":"b","b":[{"a":2}, {"a":5}, {"a":"c"}]}'
OK
redis> JSON.NUMMULTBY doc $.a 2
"[null]"
redis> JSON.NUMMULTBY doc $..a 2
"[null,4,10,null]"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

With `$`-based path argument: [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) containing a JSON array with one element per matching path: the new value, or `null` if the matching value is not a number. The array is empty if no path matches.

With `.`-based path argument: [Bulk string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) representing the stringified new value. If the path matches more than one number, the command updates all of them and returns the last new value. [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if no matching value is a number.

With either path argument: [simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if the key doesn't exist or the result is out of range.

**RESP3:**

The path syntax doesn't change the reply. [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) with one element per matching path: an [integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) or [double reply](https://redis.io/docs/latest/develop/reference/protocol-spec#doubles) containing the new value, or a [null reply](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls) if the matching value is not a number. The array is empty if no path matches.

[Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if the key doesn't exist or the result is out of range.



## See also

[`JSON.NUMINCRBY`](https://redis.io/docs/latest/commands/json.numincrby) | [`JSON.ARRINSERT`](https://redis.io/docs/latest/commands/json.arrinsert) 

## Related topics

* [RedisJSON](https://redis.io/docs/latest/develop/data-types/json)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)

