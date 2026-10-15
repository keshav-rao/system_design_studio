# CLUSTER SAVECONFIG

```json metadata
{
  "schema_version": 2,
  "title": "CLUSTER SAVECONFIG",
  "description": "Forces a node to save the cluster configuration to disk.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "CLUSTER SAVECONFIG",
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

Forces a node to save the `nodes.conf` configuration on disk. Before to return
the command calls `fsync(2)` in order to make sure the configuration is
flushed on the computer disk.

This command is mainly used in the event a `nodes.conf` node state file
gets lost / deleted for some reason, and we want to generate it again from
scratch. It can also be useful in case of mundane alterations of a node cluster
configuration via the [`CLUSTER`](https://redis.io/docs/latest/commands/cluster) command in order to ensure the new configuration
is persisted on disk, however all the commands should normally be able to
auto schedule to persist the configuration on disk when it is important
to do so for the correctness of the system in the event of a restart.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the command was successful. Otherwise an error is returned.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the command was successful. Otherwise an error is returned.



