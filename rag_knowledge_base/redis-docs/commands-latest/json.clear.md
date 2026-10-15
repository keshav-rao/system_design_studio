# JSON.CLEAR

```json metadata
{
  "schema_version": 2,
  "title": "JSON.CLEAR",
  "description": "Clears all values from an array or an object and sets numeric values to `0`",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"path","optional":true,"type":"string"}],
  "syntax_fmt": "JSON.CLEAR key [path]",
  "complexity": "O(N) when path is evaluated to a single value where N is the size of the values, O(N) when path is evaluated to multiple values, where N is the size of the key",
  "group": "json",
  "acl_categories": ["@json","@write","@slow"],
  "since": "2.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Clear container values (arrays/objects) and set numeric values to `0`

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary> 

is key to parse.
</details>

## Optional arguments

<details open><summary><code>path</code></summary> 

is JSONPath to specify. Default is root `$`. Nonexisting paths are ignored.
</details>

> [!NOTE]
>  
> Already cleared values are ignored for empty containers and zero numbers.

## Examples

<details open>
<summary><b>Clear container values and set numeric values to <code>0</code></b></summary>

Create a JSON document.


redis> JSON.SET doc $ '{"obj":{"a":1, "b":2}, "arr":[1,2,3], "str": "foo", "bool": true, "int": 42, "float": 3.14}'
OK


Clear all container values. This returns the number of objects with cleared values.


redis> JSON.CLEAR doc $.*
(integer) 4


Get the updated document. Note that numeric values have been set to `0`.


redis> JSON.GET doc $
"[{\"obj\":{},\"arr\":[],\"str\":\"foo\",\"bool\":true,\"int\":0,\"float\":0}]"

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the number of matching JSON arrays and objects cleared plus the number of matching JSON numerical values zeroed.

**RESP3:**

[Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): the number of matching JSON arrays and objects cleared plus the number of matching JSON numerical values zeroed.



## See also

[`JSON.ARRINDEX`](https://redis.io/docs/latest/commands/json.arrindex) | [`JSON.ARRINSERT`](https://redis.io/docs/latest/commands/json.arrinsert) 

## Related topics

* [RedisJSON](https://redis.io/docs/latest/develop/data-types/json)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)


