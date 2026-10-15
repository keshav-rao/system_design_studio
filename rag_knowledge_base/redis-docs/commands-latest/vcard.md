# VCARD

```json metadata
{
  "schema_version": 2,
  "title": "VCARD",
  "description": "Return the number of elements in a vector set.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "VCARD key",
  "complexity": "O(1)",
  "group": "vector_set",
  "since": "8.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Return the number of elements in the specified vector set.

```shell
VCARD word_embeddings
(integer) 3000000
```

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

[Integer reply](../../develop/reference/protocol-spec#integers): 0 if the key doesn't exist or the number of elements contained in the vector set.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): 0 if the key doesn't exist or the number of elements contained in the vector set.



## Related topics

- [Vector sets](https://redis.io/docs/latest/develop/data-types/vector-sets)

