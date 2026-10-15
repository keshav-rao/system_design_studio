# JSON.RESP

```json metadata
{
  "schema_version": 2,
  "title": "JSON.RESP",
  "description": "Returns the JSON value at path in Redis Serialization Protocol (RESP)",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"path","optional":true,"type":"string"}],
  "syntax_fmt": "JSON.RESP key [path]",
  "complexity": "O(N) when path is evaluated to a single value, where N is the size of the value, O(N) when path is evaluated to multiple values, where N is the size of the key",
  "group": "json",
  "acl_categories": ["@json","@read","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Return the JSON in `key` in [Redis serialization protocol specification](https://redis.io/docs/latest/develop/reference/protocol-spec) form 

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary> 

is key to parse.
</details>

## Optional arguments

<details open><summary><code>path</code></summary> 

is JSONPath to specify. Default is root `$`. This command uses the following mapping from JSON to RESP:

*   JSON `null` maps to the bulk string reply.
*   JSON `false` and `true` values map to the simple string reply.
*   JSON number maps to the integer reply or bulk string reply, depending on type.
*   JSON string maps to the bulk string reply.
*   JSON array is represented as an array reply in which the first element is the simple string reply `[`, followed by the array's elements.
*   JSON object is represented as an array reply in which the first element is the simple string reply `{`. Each successive entry represents a key-value pair as a two-entry array reply of the bulk string reply.

For more information about replies, see [Redis serialization protocol specification](https://redis.io/docs/latest/develop/reference/protocol-spec).
</details>

## Examples

<details open>
<summary><b>Return an array of RESP details about a document</b></summary>

Create a JSON document.


redis> JSON.SET item:2 $ '{"name":"Wireless earbuds","description":"Wireless Bluetooth in-ear headphones","connection":{"wireless":true,"type":"Bluetooth"},"price":64.99,"stock":17,"colors":["black","white"], "max_level":[80, 100, 120]}'
OK


Get all RESP details about the document.


redis> JSON.RESP item:2
 1) {
 2) "name"
 3) "Wireless earbuds"
 4) "description"
 5) "Wireless Bluetooth in-ear headphones"
 6) "connection"
 7) 1) {
    2) "wireless"
    3) true
    4) "type"
    5) "Bluetooth"
 8) "price"
 9) "64.989999999999995"
10) "stock"
11) (integer) 17
12) "colors"
13) 1) [
    2) "black"
    3) "white"
14) "max_level"
15) 1) [
    2) (integer) 80
    3) (integer) 100
    4) (integer) 120

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) representing the JSON value in RESP form, as detailed in the [Redis serialization protocol specification](https://redis.io/docs/latest/develop/reference/protocol-spec). The mapping from JSON to RESP follows the rules described in the command arguments.

**RESP3:**

[Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) representing the JSON value in RESP form, as detailed in the [Redis serialization protocol specification](https://redis.io/docs/latest/develop/reference/protocol-spec). The mapping from JSON to RESP follows the rules described in the command arguments.



## See also

[`JSON.SET`](https://redis.io/docs/latest/commands/json.set) | [`JSON.ARRLEN`](https://redis.io/docs/latest/commands/json.arrlen) 

## Related topics

* [RedisJSON](https://redis.io/docs/latest/develop/data-types/json)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)

