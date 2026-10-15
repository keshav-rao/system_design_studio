# JSON.ARRAPPEND

```json metadata
{
  "schema_version": 2,
  "title": "JSON.ARRAPPEND",
  "description": "Append one or more JSON values into the array at path after the last element in it.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"path","type":"string"},{"multiple":true,"name":"value","type":"string"}],
  "syntax_fmt": "JSON.ARRAPPEND key path value [value ...]",
  "complexity": "O(1) when path is evaluated to a single value, O(N) when path is evaluated to multiple values, where N is the size of the key",
  "group": "json",
  "acl_categories": ["@json","@write","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Append the JSON values into the array at `path` after the last element in it.

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary> 

is the key to modify.
</details>

<details open><summary><code>path</code></summary>

is the JSONPath to match.
</details>

<details open><summary><code>value</code></summary> 

is one or more values to append to one or more arrays. 

> [!NOTE] About using strings with JSON commands
> To specify a string as an array value to append, wrap the quoted string with an additional set of single quotes. Example: `'"silver"'`. For more detailed use, see [Examples](#examples).
</details>

## Examples

<details open>
<summary><b>Add a new color to a list of product colors</b></summary>

Create a document for noise-cancelling headphones in black and silver colors.


redis> JSON.SET item:1 $ '{"name":"Noise-cancelling Bluetooth headphones","description":"Wireless Bluetooth headphones with noise-cancelling technology","connection":{"wireless":true,"type":"Bluetooth"},"price":99.98,"stock":25,"colors":["black","silver"]}'
OK


Add `blue` to the end of the `colors` array. `JSON.ARRAPPEND` returns the new length of the `colors` array.


redis> JSON.ARRAPPEND item:1 $.colors '"blue"'
1) (integer) 3


Get the updated value of the `colors` array.


redis> JSON.GET item:1 $.colors
"[[\"black\",\"silver\",\"blue\"]]"


</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported"><nobr>&#x2705; Flexible & Annual</nobr></span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

With `$`-based path argument: [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [integer replies](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) or [null replies](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls), where each element is the array's new length, or `null` if the matching value is not an array.

With `.`-based path argument: [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) representing the array's new length, or [null reply](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls) if the matching value is not an array.

**RESP3:**

With `$`-based path argument (default): [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [integer replies](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) or [null replies](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls), where each element is the array's new length, or `null` if the matching value is not an array.

With `.`-based path argument: [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) representing the array's new length, or [null reply](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls) if the matching value is not an array.



## See also

[`JSON.ARRINDEX`](https://redis.io/docs/latest/commands/json.arrindex) | [`JSON.ARRINSERT`](https://redis.io/docs/latest/commands/json.arrinsert) 

## Related topics

* [RedisJSON](https://redis.io/docs/latest/develop/data-types/json)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)

