# CLUSTER BUMPEPOCH

```json metadata
{
  "schema_version": 2,
  "title": "CLUSTER BUMPEPOCH",
  "description": "Advances the cluster config epoch.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "CLUSTER BUMPEPOCH",
  "complexity": "O(1)",
  "group": "cluster",
  "command_flags": ["admin","stale","no_async_loading"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "3.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Advances the cluster config epoch.

The `CLUSTER BUMPEPOCH` command triggers an increment to the cluster's config epoch from the connected node. The epoch will be incremented if the node's config epoch is zero, or if it is less than the cluster's greatest epoch.

**Note:** config epoch management is performed internally by the cluster, and relies on obtaining a consensus of nodes. The `CLUSTER BUMPEPOCH` attempts to increment the config epoch **WITHOUT** getting the consensus, so using it may violate the "last failover wins" rule. Use it with caution.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): `BUMPED` if the epoch was incremented.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): `STILL` if the node already has the greatest configured epoch in the cluster.

**RESP3:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): `BUMPED` if the epoch was incremented.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): `STILL` if the node already has the greatest configured epoch in the cluster.



