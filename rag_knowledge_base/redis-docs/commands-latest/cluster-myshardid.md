# CLUSTER MYSHARDID

```json metadata
{
  "schema_version": 2,
  "title": "CLUSTER MYSHARDID",
  "description": "Returns the shard ID of a node.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "CLUSTER MYSHARDID",
  "complexity": "O(1)",
  "group": "cluster",
  "command_flags": ["stale"],
  "acl_categories": ["@slow"],
  "since": "7.2.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the node's shard id.

The `CLUSTER MYSHARDID` command returns the unique, auto-generated identifier that is associated with the shard to which the connected cluster node belongs.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the node's shard ID.

**RESP3:**

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the node's shard ID.



