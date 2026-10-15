# VISMEMBER

```json metadata
{
  "schema_version": 2,
  "title": "VISMEMBER",
  "description": "Check if an element exists in a vector set.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"element","type":"string"}],
  "syntax_fmt": "VISMEMBER key element",
  "complexity": "O(1)",
  "group": "vector_set",
  "command_flags": ["READONLY"],
  "since": "8.0.0",
  "arity": 3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Check if an element exists in a vector set.

## Required arguments

<details open>
<summary><code>key</code></summary>

is the name of the key that holds the vector set.
</details>

<details open>
<summary><code>element</code></summary>

is the name of the element you want to check for membership.
</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): `0` if the element does not exist in the vector set, or the key does not exist. `1` if the element exists in the vector set.

**RESP3:**

[Boolean reply](../../develop/reference/protocol-spec#booleans): `false` if the element does not exist in the vector set, or the key does not exist. `true` if the element exists in the vector set.



## Related topics

- [Vector sets](https://redis.io/docs/latest/develop/data-types/vector-sets)

