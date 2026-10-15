# JSON.MSET

```json metadata
{
  "schema_version": 2,
  "title": "JSON.MSET",
  "description": "Sets or updates the JSON value of one or more keys",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"arguments":[{"name":"key","type":"key"},{"name":"path","type":"string"},{"name":"value","type":"string"}],"multiple":true,"name":"triplet","type":"block"}],
  "syntax_fmt": "JSON.MSET key path value [key path value ...]",
  "complexity": "O(K*(M+N)) where k is the number of keys in the command, when path is evaluated to a single value where M is the size of the original value (if it exists) and N is the size of the new value, or O(K*(M+N)) when path is evaluated to multiple values where M is the size of the key and N is the size of the new value * the number of original values in the key",
  "group": "json",
  "acl_categories": ["@json","@write","@slow"],
  "since": "2.6.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


Set or update one or more JSON values according to the specified `key`-`path`-`value` triplets

`JSON.MSET` is atomic, hence, all given additions or updates are either applied or not. It is not possible for clients to see that some of the keys were updated while others are unchanged.

A JSON value is a hierarchical structure. If you change a value in a specific path - nested values are affected.

> [!WARNING]
> When cluster mode is enabled, all specified keys must reside on the same [hash slot](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec/#key-distribution-model).

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary>

is key to modify.
</details>

<details open><summary><code>path</code></summary>

is JSONPath to specify. For new Redis keys the `path` must be the root. For existing keys, when the entire `path` exists, the value that it contains is replaced with the `json` value. For existing keys, when the `path` exists, except for the last element, a new child is added with the `json` value.

</details>

<details open><summary><code>value</code></summary>

is value to set at the specified path
</details>

## Examples

<details open>
<summary><b>Add a new values in multiple keys</b></summary>


redis> JSON.MSET doc1 $ '{"a":1}' doc2 $ '{"f":{"a":2}}' doc3 $ '{"f1":{"a":0},"f2":{"a":0}}'
OK
redis> JSON.MSET doc1 $ '{"a":2}' doc2 $.f.a '3' doc3 $ '{"f1":{"a":1},"f2":{"a":2}}'
OK
redis> JSON.GET doc1 $
"[{\"a\":2}]"
redis> JSON.GET doc2 $
"[{\"f\":{\"a\":3}}]"
redis> JSON.GET doc3
"{\"f1\":{\"a\":1},\"f2\":{\"a\":2}}"

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors): if the operation fails to set the new values.

**RESP3:**

One of the following:
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors): if the operation fails to set the new values.



## See also

[`JSON.SET`](https://redis.io/docs/latest/commands/json.set) | [`JSON.MGET`](https://redis.io/docs/latest/commands/json.mget) | [`JSON.GET`](https://redis.io/docs/latest/commands/json.get) 

## Related topics

* [RedisJSON](https://redis.io/docs/latest/develop/data-types/json)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)

