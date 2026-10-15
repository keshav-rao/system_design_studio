# JSON.DEBUG MEMORY

```json metadata
{
  "schema_version": 2,
  "title": "JSON.DEBUG MEMORY",
  "description": "Reports the size in bytes of a key",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"path","optional":true,"type":"string"}],
  "syntax_fmt": "JSON.DEBUG MEMORY key [path]",
  "complexity": "O(N) when path is evaluated to a single value, where N is the size of the value, O(N) when path is evaluated to multiple values, where N is the size of the key",
  "group": "json",
  "acl_categories": ["@json","@read"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Report a value's memory usage in bytes 

> [!WARNING]
> The actual total memory consumption by a key could be much lower than the value reported by this command because of an internal JSON string reuse mechanism. For more information, see the [JSON memory usage page](https://redis.io/docs/latest/develop/data-types/json/ram#json-string-reuse-mechanism).

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary> 

is key to parse.
</details>

## Optional arguments

<details open><summary><code>path</code></summary> 

is JSONPath to specify. Default is root `$`. 
</details>

## Examples

<details open>
<summary><b>Report a value's memory usage in bytes</b></summary>

Create a JSON document.


redis> JSON.SET item:2 $ '{"name":"Wireless earbuds","description":"Wireless Bluetooth in-ear headphones","connection":{"wireless":true,"type":"Bluetooth"},"price":64.99,"stock":17,"colors":["black","white"], "max_level":[80, 100, 120]}'
OK


Get the values' memory usage in bytes.


redis> JSON.DEBUG MEMORY item:2
(integer) 573

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the value size in bytes.

**RESP3:**

[Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the value size in bytes.



## See also

[`JSON.SET`](https://redis.io/docs/latest/commands/json.set) | [`JSON.ARRLEN`](https://redis.io/docs/latest/commands/json.arrlen) 

## Related topics

* [RedisJSON](https://redis.io/docs/latest/develop/data-types/json)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)

