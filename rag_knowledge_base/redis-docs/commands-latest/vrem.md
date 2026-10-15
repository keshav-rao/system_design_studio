# VREM

```json metadata
{
  "schema_version": 2,
  "title": "VREM",
  "description": "Remove an element from a vector set.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "VREM key element",
  "complexity": "O(log(N)) for each element removed, where N is the number of elements in the vector set.",
  "group": "vector_set",
  "since": "8.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Remove an element from a vector set.

```shell
VADD vset VALUES 3 1 0 1 bar
(integer) 1

VREM vset bar
(integer) 1

VREM vset bar
(integer) 0
```

`VREM` reclaims memory immediately. It does not use tombstones or logical deletions, making it safe to use in long-running applications that frequently update the same vector set.

## Required arguments

<details open>
<summary><code>key</code></summary>

is the name of the key that holds the vector set.
</details>

<details open>
<summary><code>element</code></summary>

is the name of the element to remove from the vector set.
</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): 0 if either element or key do not exist; 1 if the element was removed.

**RESP3:**

[Boolean reply](../../develop/reference/protocol-spec#booleans): false if either element or key do not exist; true if the element was removed.



## Related topics

- [Vector sets](https://redis.io/docs/latest/develop/data-types/vector-sets)

