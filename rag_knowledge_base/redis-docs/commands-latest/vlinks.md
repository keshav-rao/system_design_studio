# VLINKS

```json metadata
{
  "schema_version": 2,
  "title": "VLINKS",
  "description": "Return the neighbors of an element at each layer in the HNSW graph.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "VLINKS key element [WITHSCORES]",
  "complexity": "O(1)",
  "group": "vector_set",
  "since": "8.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Return the neighbors of a specified element in a vector set. The command shows the connections for each layer of the HNSW graph.

```shell
VLINKS key element
```

Use the `WITHSCORES` option to include similarity scores for each neighbor.

```shell
VLINKS key element WITHSCORES
```

## Required arguments

<details open>
<summary><code>key</code></summary>

is the name of the key that holds the vector set.
</details>

<details open>
<summary><code>element</code></summary>

is the name of the element whose HNSW neighbors you want to inspect.
</details>

## Optional arguments

<details open>
<summary><code>WITHSCORES</code></summary>

includes similarity scores for each neighbor.
</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* An [array](../../develop/reference/protocol-spec#arrays) of [array replies](../../develop/reference/protocol-spec#arrays) containing the names of adjacent elements as [bulk strings](../../develop/reference/protocol-spec#bulk-strings); interleaved with scores as [bulk strings](../../develop/reference/protocol-spec#bulk-strings) when used with the `WITHSCORES` option.
* [Simple error reply](../../develop/reference/protocol-spec/#simple-errors) for incorrect syntax.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings) (null bulk string) for unknown keys and/or elements.

**RESP3:**

One of the following:
* An [array](../../develop/reference/protocol-spec#arrays) of [array replies](../../develop/reference/protocol-spec#arrays) containing the names of adjacent elements as [bulk strings](../../develop/reference/protocol-spec#bulk-strings) when used without the `WITHSCORES` option.
* An [array](../../develop/reference/protocol-spec#arrays) of [map replies](../../develop/reference/protocol-spec#maps) containing the names of adjecent elements as [bulk strings](../../develop/reference/protocol-spec#bulk-strings), together with their scores as [doubles](../../develop/reference/protocol-spec#doubles) when used with the `WITHSCORES` option.
* [Simple error reply](../../develop/reference/protocol-spec/#simple-errors) for incorrect syntax.
* [Null reply](../../develop/reference/protocol-spec#nulls) for unknown keys and/or elements.



## Related topics

- [Vector sets](https://redis.io/docs/latest/develop/data-types/vector-sets)

