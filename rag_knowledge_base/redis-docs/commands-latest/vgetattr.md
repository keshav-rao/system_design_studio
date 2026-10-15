# VGETATTR

```json metadata
{
  "schema_version": 2,
  "title": "VGETATTR",
  "description": "Retrieve the JSON attributes of elements.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "VGETATTR key element",
  "complexity": "O(1)",
  "group": "vector_set",
  "since": "8.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Return the JSON attributes associated with an element in a vector set.

```shell
VGETATTR key element
```

## Required arguments

<details open>
<summary><code>key</code></summary>

is the name of the key that holds the vector set.
</details>

<details open>
<summary><code>element</code></summary>

is the name of the element whose attributes you want to retrieve.
</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings) containing the JSON attribute(s).
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings) (null bulk string) for unknown key or element, or when no attributes exist for the given key/element pair.

**RESP3:**

One of the following:
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings) containing the JSON attribute(s).
* [Null reply](../../develop/reference/protocol-spec#nulls) for unknown key or element, or when no attributes exist for the given key/element pair.



## Related topics

- [Vector sets](https://redis.io/docs/latest/develop/data-types/vector-sets)
- [Filtered search](https://redis.io/docs/latest/develop/data-types/vector-sets/filtered-search)

