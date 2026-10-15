# JSON.MERGE

```json metadata
{
  "schema_version": 2,
  "title": "JSON.MERGE",
  "description": "Merges a given JSON value into matching paths. Consequently, JSON values at matching paths are updated, deleted, or expanded with new children",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"path","type":"string"},{"name":"value","type":"string"}],
  "syntax_fmt": "JSON.MERGE key path value",
  "complexity": "O(M+N) when path is evaluated to a single value where M is the size of the original value (if it exists) and N is the size of the new value, O(M+N) when path is evaluated to multiple values where M is the size of the key and N is the size of the new value * the number of original values in the key",
  "group": "json",
  "acl_categories": ["@json","@write","@slow"],
  "since": "2.6.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"see-also","title":"See also"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```

Merge a given JSON value into matching paths. Consequently, JSON values at matching paths are updated, deleted, or expanded with new children.

This command complies with [RFC7396](https://datatracker.ietf.org/doc/html/rfc7396) Json Merge Patch

[Examples](#examples)

## Required arguments

<details open><summary><code>key</code></summary>

is the key to merge into.
</details>

<details open><summary><code>path</code></summary>

specifies the JSONPath. For non-existing keys the `path` must be `$`. For existing keys, for each matched `path`, the value that matches the `path` is merged with the JSON `value`. For existing keys, when the path exists, except for the last element, a new child is added with the JSON `value`.

</details>

<details open><summary><code>value</code></summary>

is the JSON value to merge with at the specified path. Merging is done according to the following rules per JSON value in the `value` argument while considering the corresponding original value if it exists:
*   merging an existing object key with a `null` value deletes the key
*   merging an existing object key with non-null value updates the value
*   merging a non-existing object key adds the key and value
*   merging an existing array with any merged value, replaces the entire array with the value
</details>

## Examples

JSON.MERGE provides four different behaviors to merge changes on a given key: create a non-existent path, update an existing path with a new value, delete an existing path, or replace an array with a new array

<details open>
<summary><b>Create a non-existent path-value</b></summary>


redis> JSON.SET doc $ '{"a":2}'
OK
redis> JSON.MERGE doc $.b '8'
OK
redis> JSON.GET doc $
"[{\"a\":2,\"b\":8}]"


</details>

<details open>
<summary><b>Replace an existing value</b></summary>


redis> JSON.SET doc $ '{"a":2}'
OK
redis> JSON.MERGE doc $.a '3'
OK
redis> JSON.GET doc $
"[{\"a\":3}]"


</details>

<details open>
<summary><b>Delete an existing value</b></summary>


redis> JSON.SET doc $ '{"a":2}'
OK
redis> JSON.MERGE doc $ '{"a":null}'
OK
redis> JSON.GET doc $
"[{}]"


</details>

<details open>
<summary><b>Replace an Array</b></summary>


redis> JSON.SET doc $ '{"a":[2,4,6,8]}'
OK
redis> JSON.MERGE doc $.a '[10,12]'
OK
redis> JSON.GET doc $
"[{\"a\":[10,12]}]"


</details>

<details open>
<summary><b>Merge changes in multi-paths</b></summary>


redis> JSON.SET doc $ '{"f1": {"a":1}, "f2":{"a":2}}'
OK
redis> JSON.GET doc
"{\"f1\":{\"a\":1},\"f2\":{\"a\":2}}"
redis> JSON.MERGE doc $ '{"f1": null, "f2":{"a":3, "b":4}, "f3":[2,4,6]}'
OK
redis> JSON.GET doc
"{\"f2\":{\"a\":3,\"b\":4},\"f3\":[2,4,6]}"


</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

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

[`JSON.GET`](https://redis.io/docs/latest/commands/json.get) | [`JSON.MGET`](https://redis.io/docs/latest/commands/json.mget) | [`JSON.SET`](https://redis.io/docs/latest/commands/json.set) | [`JSON.MSET`](https://redis.io/docs/latest/commands/json.mset)

## Related topics

* [RedisJSON](https://redis.io/docs/latest/develop/data-types/json)
* [Index and search JSON documents](https://redis.io/docs/latest/develop/ai/search-and-query/indexing)


