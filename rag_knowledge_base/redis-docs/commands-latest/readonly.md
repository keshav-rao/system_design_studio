# READONLY

```json metadata
{
  "schema_version": 2,
  "title": "READONLY",
  "description": "Enables read-only queries for a connection to a Redis Cluster replica node.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "READONLY",
  "complexity": "O(1)",
  "group": "cluster",
  "command_flags": ["loading","stale","fast"],
  "acl_categories": ["@fast","@connection"],
  "since": "3.0.0",
  "arity": 1,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Enables read queries for a connection to a Redis Cluster replica node. 

Normally replica nodes will redirect clients to the authoritative master for
the hash slot involved in a given command, however clients can use replicas
in order to scale reads using the `READONLY` command.

`READONLY` tells a Redis Cluster replica node that the client is willing to
read possibly stale data and is not interested in running write queries.

When the connection is in readonly mode, the cluster will send a redirection
to the client only if the operation involves keys not served by the replica's
master node. This may happen because:

1. The client sent a command about hash slots never served by the master of this replica.
2. The cluster was reconfigured (for example resharded) and the replica is no longer able to serve commands for a given hash slot.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



