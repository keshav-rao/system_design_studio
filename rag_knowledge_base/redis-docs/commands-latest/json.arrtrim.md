# JSON.ARRTRIM

```json metadata
{
  "schema_version": 2,
  "title": "JSON.ARRTRIM",
  "description": "Trims the array at path to contain only the specified inclusive range of indices from start to stop",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"path","type":"string"},{"name":"start","type":"integer"},{"name":"stop","type":"integer"}],
  "syntax_fmt": "JSON.ARRTRIM key path start stop",
  "complexity": "O(N) when path is evaluated to a single value where N is the size of the array, O(N) when path is evaluated to multiple values, where N is the size of the key",
  "group": "json",
  "acl_categories": ["@json","@write","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Trim an array so that it contains only the specified inclusive range of elements

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary> 

is key to modify.
</details>

## Optional arguments

<details open><summary><code>path</code></summary> 

is JSONPath to specify. Default is root `$`.
</details>

<details open><summary><code>start</code></summary> 

is index of the first element to keep (previous elements are trimmed). Default is 0. 
</details>

<details open><summary><code>stop</code></summary> 

is the index of the last element to keep (following elements are trimmed), including the last element. Default is 0. Negative values are interpreted as starting from the end.
</details>

> [!NOTE] About out-of-range indexes
> JSON.ARRTRIM is extremely forgiving, and using it with out-of-range indexes does not produce an error. Note a few differences between how RedisJSON v2.0 and legacy versions handle out-of-range indexes.
>
> Behavior as of RedisJSON v2.0:
>
> * If `start` is larger than the array's size or `start` > `stop`, returns 0 and an empty array. 
> * If `start` is < 0, then start from the end of the array.
> * If `stop` is larger than the end of the array, it is treated like the last element.

## Examples

<details open>
<summary><b>Trim an array to a specific set of values</b></summary>

Create two headphone products with maximum sound levels.


redis> JSON.SET key $
"[{\"name\":\"Healthy headphones\",\"description\":\"Wireless Bluetooth headphones with noise-cancelling technology\",\"connection\":{\"wireless\":true,\"type\":\"Bluetooth\"},\"price\":99.98,\"stock\":25,\"colors\":[\"black\",\"silver\"],\"max_level\":[60,70,80]},{\"name\":\"Noisy headphones\",\"description\":\"Wireless Bluetooth headphones with noise-cancelling technology\",\"connection\":{\"wireless\":true,\"type\":\"Bluetooth\"},\"price\":99.98,\"stock\":25,\"colors\":[\"black\",\"silver\"],\"max_level\":[85,90,100,120]}]"
OK


Add new sound level values to the second product.


redis> JSON.ARRAPPEND key $.[1].max_level 140 160 180 200 220 240 260 280
1) (integer) 12


Get the updated array.


redis> JSON.GET key $.[1].max_level
"[[85,90,100,120,140,160,180,200,220,240,260,280]]"


Keep only the values between the fifth and the ninth element, inclusive of that last element.


redis> JSON.ARRTRIM key $.[1].max_level 4 8
1) (integer) 5


Get the updated array.


redis> JSON.GET key $.[1].max_level
"[[140,160,180,200,220]]"

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

With `$`-based path argument: [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [integer replies](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) or [null replies](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls), where each element is the array's new size, or `null` if the matching value is not an array.

With `.`-based path argument: [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) representing the array's new size, or [null reply](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls) if the matching value is not an array.

**RESP3:**

With `$`-based path argument (default): [Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [integer replies](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) or [null replies](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls), where each element is the array's new size, or `null` if the matching value is not an array.

With `.`-based path argument: [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) representing the array's new size, or [null reply](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls) if the matching value is not an array.



## See also

[`JSON.ARRINDEX`](https://redis.io/docs/latest/commands/json.arrindex) | [`JSON.ARRINSERT`](https://redis.io/docs/latest/commands/json.arrinsert) 

## Related topics

* [RedisJSON](https://redis.io/docs/latest/develop/data-types/json)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)


