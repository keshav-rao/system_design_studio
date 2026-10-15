# REPLICAOF

```json metadata
{
  "schema_version": 2,
  "title": "REPLICAOF",
  "description": "Configures a server as replica of another, or promotes it to a master.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"arguments":[{"arguments":[{"display_text":"host","name":"host","type":"string"},{"display_text":"port","name":"port","type":"integer"}],"name":"host-port","type":"block"},{"arguments":[{"display_text":"no","name":"no","token":"NO","type":"pure-token"},{"display_text":"one","name":"one","token":"ONE","type":"pure-token"}],"name":"no-one","type":"block"}],"name":"args","type":"oneof"}],
  "syntax_fmt": "REPLICAOF \u003chost port | NO ONE\u003e",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["admin","noscript","stale","no_async_loading"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "5.0.0",
  "arity": 3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `REPLICAOF` command can change the replication settings of a replica on the fly.

If a Redis server is already acting as replica, the command `REPLICAOF` NO ONE will turn off the replication, turning the Redis server into a MASTER.  In the proper form `REPLICAOF` hostname port will make the server a replica of another server listening at the specified hostname and port.

If a server is already a replica of some master, `REPLICAOF` hostname port will stop the replication against the old server and start the synchronization against the new one, discarding the old dataset.

The form `REPLICAOF` NO ONE will stop replication, turning the server into a MASTER, but will not discard the already replicated data. So, if the old master stops working, it is possible to turn the replica into a master and set the application to use this new master in read/write. Later when the other Redis server is fixed, it can be reconfigured to work as a replica.

## Required arguments

<details open><summary><code>host port | NO ONE</code></summary>

The host and port of the master to replicate from, or `NO ONE` to stop replicating and turn the server back into a master.

</details>

## Examples

```
> REPLICAOF NO ONE
"OK"

> REPLICAOF 127.0.0.1 6799
"OK"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



