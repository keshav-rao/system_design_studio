# CLUSTER COUNTKEYSINSLOT

```json metadata
{
  "schema_version": 2,
  "title": "CLUSTER COUNTKEYSINSLOT",
  "description": "Returns the number of keys in a hash slot.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"slot","name":"slot","type":"integer"}],
  "syntax_fmt": "CLUSTER COUNTKEYSINSLOT slot",
  "complexity": "O(1)",
  "group": "cluster",
  "command_flags": ["stale"],
  "acl_categories": ["@slow"],
  "since": "3.0.0",
  "arity": 3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the number of keys in the specified Redis Cluster hash slot. The
command only queries the local data set, so contacting a node
that is not serving the specified hash slot will always result in a count of
zero being returned.

> [!NOTE]
> During atomic slot migration operations (available since Redis 8.4.0), keys being imported or trimmed will be filtered out from the results.


## Required arguments

<details open><summary><code>slot</code></summary>

The hash slot to count the keys in.

</details>

## Examples

```
> CLUSTER COUNTKEYSINSLOT 7000
(integer) 50341
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): The number of keys in the specified hash slot, or an error if the hash slot is invalid.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): The number of keys in the specified hash slot, or an error if the hash slot is invalid.



