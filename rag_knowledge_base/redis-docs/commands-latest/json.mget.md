# JSON.MGET

```json metadata
{
  "schema_version": 2,
  "title": "JSON.MGET",
  "description": "Returns the values at a path from one or more keys",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"multiple":true,"name":"key","type":"key"},{"name":"path","type":"string"}],
  "syntax_fmt": "JSON.MGET key [key ...] path",
  "complexity": "O(M*N) when path is evaluated to a single value where M is the number of keys and N is the size of the value, O(N1+N2+...+Nm) when path is evaluated to multiple values where m is the number of keys and Ni is the size of the i-th key",
  "group": "json",
  "acl_categories": ["@json","@read","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


Return the values at `path` from multiple `key` arguments

> [!WARNING]
> When cluster mode is enabled, all specified keys must reside on the same [hash slot](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/#key-distribution-model).
>
> When the database has more than one shard, and the specified keys reside in different shards, Redis will not report a CROSSSLOT error (to avoid breaking changes) and the results may be partial.

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary> 

is key to parse. Returns `null` for nonexistent keys.
</details>

## Optional arguments

<details open><summary><code>path</code></summary> 

is JSONPath to specify. Returns `null` for nonexistent paths.

</details>

## Examples

<details open>
<summary><b>Return the values at <code>path</code> from multiple <code>key</code> arguments</b></summary>

Create two JSON documents.


redis> JSON.SET doc1 $ '{"a":1, "b": 2, "nested": {"a": 3}, "c": null}'
OK
redis> JSON.SET doc2 $ '{"a":4, "b": 5, "nested": {"a": 6}, "c": null}'
OK


Get values from all arguments in the documents.


redis> JSON.MGET doc1 doc2 $..a
1) "[1,3]"
2) "[4,6]"

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) or [null replies](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls), where each element is the JSON serialization of the value at the corresponding key's path, or `null` if the key or path doesn't exist.

**RESP3:**

[Array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) of [bulk string replies](https://redis.io/docs/latest/develop/reference/protocol-spec#bulk-strings) or [null replies](https://redis.io/docs/latest/develop/reference/protocol-spec#nulls), where each element is the JSON serialization of the value at the corresponding key's path, or `null` if the key or path doesn't exist.



## See also

[`JSON.SET`](https://redis.io/docs/latest/commands/json.set) | [`JSON.GET`](https://redis.io/docs/latest/commands/json.get) 

## Related topics

* [RedisJSON](https://redis.io/docs/latest/develop/data-types/json)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)

