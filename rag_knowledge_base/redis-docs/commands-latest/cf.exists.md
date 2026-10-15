# CF.EXISTS

```json metadata
{
  "schema_version": 2,
  "title": "CF.EXISTS",
  "description": "Checks whether one or more items exist in a Cuckoo Filter",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"item","type":"string"}],
  "syntax_fmt": "CF.EXISTS key item",
  "complexity": "O(k), where k is the number of sub-filters",
  "group": "cf",
  "acl_categories": ["@cuckoo","@read","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Determines whether a given item was added to a cuckoo filter.

This command is similar to [`CF.MEXISTS`](https://redis.io/docs/latest/commands/cf.mexists), except that only one item can be checked.

## Required arguments

<details open><summary><code>key</code></summary>

is key name for a cuckoo filter.

</details>

<details open><summary><code>item</code></summary>

is an item to check.
</details>

## Examples


redis> CF.ADD cf item1
(integer) 1
redis> CF.EXISTS cf item1
(integer) 1
redis> CF.EXISTS cf item2
(integer) 0


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers), where a value of `1` means the item was probably already added to the filter. A value of `0` means the item was definitely not added, `key` does not exist, or `key` contains a value of the wrong type.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if invalid arguments are passed.

**RESP3:**

One of the following:
* [Boolean reply](https://redis.io/docs/latest/develop/reference/protocol-spec#booleans), where a value of `true` means the item was probably already added to the filter. A value of `false` means the item was definitely not added, `key` does not exist, or `key` contains a value of the wrong type.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if invalid arguments are passed.


