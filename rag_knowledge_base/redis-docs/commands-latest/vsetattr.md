# VSETATTR

```json metadata
{
  "schema_version": 2,
  "title": "VSETATTR",
  "description": "Associate or remove the JSON attributes of elements.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "VSETATTR key element \"{ JSON obj }\"",
  "complexity": "O(1)",
  "group": "vector_set",
  "since": "8.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"},{"id":"related-topics","title":"Related topics"}]}

,
  "codeExamples": []
}
```


Associate a JSON object with an element in a vector set. Use this command to store attributes that can be used in filtered similarity searches with `VSIM`.

You can also update existing attributes or delete them by setting an empty string.

```shell
VSETATTR key element "{\"type\": \"fruit\", \"color\": \"red\"}"
```

To remove attributes, pass an empty JSON string:

```shell
VSETATTR key element ""
```

## Required arguments

<details open>
<summary><code>key</code></summary>

is the name of the key that holds the vector set.
</details>

<details open>
<summary><code>element</code></summary>

is the name of the element whose attributes you want to set or remove.
</details>

<details open>
<summary><code>json</code></summary>

is the JSON string with the attributes of the element. Use an empty string (`""`) to delete the attributes.
The string is stored as given, without validation. Elements whose attributes are not valid JSON are treated as not matching by the `FILTER` option of `VSIM`.
</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): 0 if either the key or element does not exist; 1 if the attributes were set or deleted.

**RESP3:**

[Boolean reply](../../develop/reference/protocol-spec#booleans): false if either the key or element does not exist; true if the attributes were set or deleted.



## Related topics

- [Vector sets](https://redis.io/docs/latest/develop/data-types/vector-sets)
- [Filtered search](https://redis.io/docs/latest/develop/data-types/vector-sets/filtered-search)

