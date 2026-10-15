# VDIM

```json metadata
{
  "schema_version": 2,
  "title": "VDIM",
  "description": "Return the dimension of vectors in the vector set.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "VDIM key",
  "complexity": "O(1)",
  "group": "vector_set",
  "since": "8.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Return the number of dimensions of the vectors in the specified vector set.

```shell
VDIM word_embeddings
(integer) 300
```

If the vector set was created using the `REDUCE` option for dimensionality reduction, this command reports the reduced dimension. However, you must still use full-size vectors when performing queries with the `VSIM` command.

## Required arguments

<details open>
<summary><code>key</code></summary>

is the name of the key that holds the vector set.
</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): the number of vector set elements.
* [Simple error reply](../../develop/reference/protocol-spec#simple-errors): if the key does not exist.

**RESP3:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): the number of vector set elements.
* [Simple error reply](../../develop/reference/protocol-spec#simple-errors): if the key does not exist.



## Related topics

- [Vector sets](https://redis.io/docs/latest/develop/data-types/vector-sets)

