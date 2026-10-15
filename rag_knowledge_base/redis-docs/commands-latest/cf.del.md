# CF.DEL

```json metadata
{
  "schema_version": 2,
  "title": "CF.DEL",
  "description": "Deletes an item from a Cuckoo Filter",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"item","type":"string"}],
  "syntax_fmt": "CF.DEL key item",
  "complexity": "O(k), where k is the number of sub-filters",
  "group": "cf",
  "acl_categories": ["@cuckoo","@write","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"complexity","title":"Complexity"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Deletes an item once from the filter.

If the item exists only once, it will be removed from the filter. If the item was added multiple times, it will still be present.

> [!NOTE]
> Never use this command to delete an item unless you are certain you've added the item to the filter. Deleting an item you didn't previously add may corrupt the filter and cause false negatives.

## Required arguments

<details open><summary><code>key</code></summary>

is key name for a cuckoo filter.
</details>

<details open><summary><code>item</code></summary>

is an item to delete.
</details>

## Complexity

O(n), where n is the number of `sub-filters`. Both alternative locations are
checked on all `sub-filters`.

## Examples


redis> CF.INSERT cf ITEMS item1 item2 item2
1) (integer) 1
2) (integer) 1
3) (integer) 1
redis> CF.DEL cf item1
(integer) 1
redis> CF.DEL cf item1
(integer) 0
redis> CF.DEL cf item2
(integer) 1
redis> CF.DEL cf item2
(integer) 1
redis> CF.DEL cf item2
(integer) 0


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers) `1` for successfully deleting an item, or `0` if no such item was found in the filter.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments or wrong key type.

**RESP3:**

One of the following:
* [Boolean reply](https://redis.io/docs/latest/develop/reference/protocol-spec#booleans) `true` for successfully deleting an item, or `false` if no such item was found in the filter.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments or wrong key type.



