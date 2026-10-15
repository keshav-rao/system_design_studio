# ZSCAN

```json metadata
{
  "schema_version": 2,
  "title": "ZSCAN",
  "description": "Iterates over members and scores of a sorted set.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"cursor","name":"cursor","type":"integer"},{"display_text":"pattern","name":"pattern","optional":true,"token":"MATCH","type":"pattern"},{"display_text":"count","name":"count","optional":true,"token":"COUNT","type":"integer"}],
  "syntax_fmt": "ZSCAN key cursor [MATCH pattern] [COUNT count]",
  "complexity": "O(1) for every call. O(N) for a complete iteration, including enough command calls for the cursor to return back to 0. N is the number of elements inside the collection.",
  "group": "sorted-set",
  "command_flags": ["readonly"],
  "acl_categories": ["@read","@sortedset","@slow"],
  "since": "2.8.0",
  "arity": -3,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

See [`SCAN`](https://redis.io/docs/latest/commands/scan) for `ZSCAN` documentation.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the sorted set.

</details>

<details open><summary><code>cursor</code></summary>

The cursor value. Start an iteration with `0`, then use the cursor returned by each call as the argument to the next call.

</details>

## Optional arguments

<details open><summary><code>MATCH pattern</code></summary>

Only return members matching the given glob-style pattern.

</details>

<details open><summary><code>COUNT count</code></summary>

A hint for the number of members to return per iteration. The default is 10.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): cursor and scan response in array form.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): cursor and scan response in array form.



