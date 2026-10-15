# SLAVEOF

```json metadata
{
  "schema_version": 2,
  "title": "SLAVEOF",
  "description": "Sets a Redis server as a replica of another, or promotes it to being a master.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"arguments":[{"arguments":[{"display_text":"host","name":"host","type":"string"},{"display_text":"port","name":"port","type":"integer"}],"name":"host-port","type":"block"},{"arguments":[{"display_text":"no","name":"no","token":"NO","type":"pure-token"},{"display_text":"one","name":"one","token":"ONE","type":"pure-token"}],"name":"no-one","type":"block"}],"name":"args","type":"oneof"}],
  "syntax_fmt": "SLAVEOF \u003chost port | NO ONE\u003e",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["admin","noscript","stale","no_async_loading"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "1.0.0",
  "arity": 3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

**A note about the word slave used in this man page and command name**: starting with Redis version 5, if not for backward compatibility, the Redis project no longer uses the word slave. Please use the new command [`REPLICAOF`](https://redis.io/docs/latest/commands/replicaof). The command `SLAVEOF` will continue to work for backward compatibility.

The `SLAVEOF` command can change the replication settings of a replica on the fly.
If a Redis server is already acting as replica, the command `SLAVEOF` NO ONE will
turn off the replication, turning the Redis server into a MASTER.
In the proper form `SLAVEOF` hostname port will make the server a replica of
another server listening at the specified hostname and port.

If a server is already a replica of some master, `SLAVEOF` hostname port will stop
the replication against the old server and start the synchronization against the
new one, discarding the old dataset.

The form `SLAVEOF` NO ONE will stop replication, turning the server into a
MASTER, but will not discard the replication.
So, if the old master stops working, it is possible to turn the replica into a
master and set the application to use this new master in read/write.
Later when the other Redis server is fixed, it can be reconfigured to work as a
replica.

## Required arguments

<details open><summary><code>host port | NO ONE</code></summary>

The host and port of the master to replicate from, or `NO ONE` to stop replicating. `SLAVEOF` is deprecated; use `REPLICAOF` instead.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | Deprecated as of Redis v5.0.0. |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



