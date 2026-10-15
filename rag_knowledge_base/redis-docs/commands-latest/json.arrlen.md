# JSON.ARRLEN

```json metadata
{
  "schema_version": 2,
  "title": "JSON.ARRLEN",
  "description": "Returns the length of the array at path",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"path","optional":true,"type":"string"}],
  "syntax_fmt": "JSON.ARRLEN key [path]",
  "complexity": "O(1) where path is evaluated to a single value, O(N) where path is evaluated to multiple values, where N is the size of the key",
  "group": "json",
  "acl_categories": ["@json","@read","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Report the length of the JSON array at `path` in `key`

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary> 

is key to parse.
</details>

## Optional arguments

<details open><summary><code>path</code></summary> 

is JSONPath to specify. Default is root `$`, if not provided. Returns null if the `key` or `path` do not exist.
</details>

## Examples

<details open>
<summary><b>Get lengths of JSON arrays in a document</b></summary>

Create a document for wireless earbuds.


redis> JSON.SET item:2 $ '{"name":"Wireless earbuds","description":"Wireless Bluetooth in-ear headphones","connection":{"wireless":true,"type":"Bluetooth"},"price":64.99,"stock":17,"colors":["black","white"], "max_level":[80, 100, 120]}'
OK


Find lengths of arrays in all objects of the document.


redis> JSON.ARRLEN item:2 '$.[*]'
1) (nil)
2) (nil)
3) (nil)
4) (nil)
5) (nil)
6) (integer) 2
7) (integer) 3


Return the length of the `max_level` array.


redis> JSON.ARRLEN item:2 '$..max_level'
1) (integer) 3


Get all the maximum level values.


redis> JSON.GET item:2 '$..max_level'
"[[80,100,120]]"


</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

With `$`-based path argument: [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [integer replies](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) or [null replies](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls), where each element is the array length, or `null` if the matching value is not an array.

With `.`-based path argument: [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) representing the array length, or [null reply](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls) if the matching value is not an array.

**RESP3:**

With `$`-based path argument (default): [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [integer replies](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) or [null replies](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls), where each element is the array length, or `null` if the matching value is not an array.

With `.`-based path argument: [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) representing the array length, or [null reply](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls) if the matching value is not an array.



## See also

[`JSON.ARRINDEX`](https://redis.io/docs/latest/commands/json.arrindex) | [`JSON.ARRINSERT`](https://redis.io/docs/latest/commands/json.arrinsert) 

## Related topics

* [RedisJSON](https://redis.io/docs/latest/develop/data-types/json)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)

