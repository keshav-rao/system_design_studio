# ARINFO

```json metadata
{
  "schema_version": 2,
  "title": "ARINFO",
  "description": "Returns metadata about an array.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"key_spec_index":0,"name":"key","type":"key"},{"name":"full","optional":true,"token":"FULL","type":"pure-token"}],
  "syntax_fmt": "ARINFO key [FULL]",
  "complexity": "O(1), or O(N) with FULL option where N is the number of slices.",
  "group": "array",
  "command_flags": ["READONLY"],
  "acl_categories": ["@read","@array","@slow"],
  "since": "8.8.0",
  "arity": -2,
  "key_specs": [{"begin_search":{"index":{"pos":1}},"find_keys":{"range":{"lastkey":0,"limit":0,"step":1}},"flags":["RO","ACCESS"]}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns metadata about an array.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the array.

</details>

## Optional arguments

<details open><summary><code>FULL</code></summary>

When present, includes per-slice statistics in the reply: the number of dense and sparse slices and their average sizes and fill rates. Raises the complexity from O(1) to O(N) where N is the number of slices.

</details>

## Examples


redis> ARMSET myarray 0 "a" 1 "b" 100 "c"
(integer) 3
redis> ARINSERT myarray "d"
(integer) 0
redis> ARINFO myarray
 1) "count"
 2) (integer) 3
 3) "len"
 4) (integer) 101
 5) "next-insert-index"
 6) (integer) 1
 7) "slices"
 8) (integer) 1
 9) "directory-size"
10) (integer) 1
11) "super-dir-entries"
12) (integer) 0
13) "slice-size"
14) (integer) 4096


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays)

**RESP3:**

[Map reply](../../develop/reference/protocol-spec#maps)



