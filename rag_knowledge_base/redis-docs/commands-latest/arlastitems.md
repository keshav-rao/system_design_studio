# ARLASTITEMS

```json metadata
{
  "schema_version": 2,
  "title": "ARLASTITEMS",
  "description": "Returns the most recently inserted elements.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"key_spec_index":0,"name":"key","type":"key"},{"name":"count","type":"integer"},{"name":"rev","optional":true,"token":"REV","type":"pure-token"}],
  "syntax_fmt": "ARLASTITEMS key count [REV]",
  "complexity": "O(N) where N is the count",
  "group": "array",
  "command_flags": ["READONLY"],
  "acl_categories": ["@read","@array","@slow"],
  "since": "8.8.0",
  "arity": -3,
  "key_specs": [{"begin_search":{"index":{"pos":1}},"find_keys":{"range":{"lastkey":0,"limit":0,"step":1}},"flags":["RO","ACCESS"]}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the most recently inserted elements.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the array.

</details>

<details open><summary><code>count</code></summary>

The maximum number of most recently inserted elements to return. If the array contains fewer elements than `count`, all elements are returned.

</details>

## Optional arguments

<details open><summary><code>REV</code></summary>

When present, returns elements in reverse chronological order (most recent first) instead of the default oldest-first order.

</details>

## Examples


redis> ARINSERT log "first"
(integer) 0
redis> ARINSERT log "second"
(integer) 1
redis> ARINSERT log "third"
(integer) 2
redis> ARLASTITEMS log 2
1) "second"
2) "third"
redis> ARLASTITEMS log 2 REV
1) "third"
2) "second"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays)

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays)



