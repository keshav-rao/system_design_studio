# ASKING

```json metadata
{
  "schema_version": 2,
  "title": "ASKING",
  "description": "Signals that a cluster client is following an -ASK redirect.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "ASKING",
  "complexity": "O(1)",
  "group": "cluster",
  "command_flags": ["fast"],
  "acl_categories": ["@fast","@connection"],
  "since": "3.0.0",
  "arity": 1,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

When a cluster client receives an `-ASK` redirect, the `ASKING` command is sent to the target node followed by the command which was redirected.
This is normally done automatically by cluster clients.

If an `-ASK` redirect is received during a transaction, only one ASKING command needs to be sent to the target node before sending the complete transaction to the target node.

See [ASK redirection in the Redis Cluster Specification](https://redis.io/docs/latest/operate/oss_and_stack/reference/cluster-spec#ask-redirection) for details.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



