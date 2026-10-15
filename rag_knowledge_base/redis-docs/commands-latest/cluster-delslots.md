# CLUSTER DELSLOTS

```json metadata
{
  "schema_version": 2,
  "title": "CLUSTER DELSLOTS",
  "description": "Sets hash slots as unbound for a node.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"slot","multiple":true,"name":"slot","type":"integer"}],
  "syntax_fmt": "CLUSTER DELSLOTS slot [slot ...]",
  "complexity": "O(N) where N is the total number of hash slot arguments",
  "group": "cluster",
  "command_flags": ["admin","stale","no_async_loading"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "3.0.0",
  "arity": -3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"children":[{"id":"usage-in-redis-cluster","title":"Usage in Redis Cluster"},{"id":"other-details","title":"Other details"}],"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

In Redis Cluster, each node keeps track of which master is serving
a particular hash slot.

The `CLUSTER DELSLOTS` command asks a particular Redis Cluster node to
forget which master is serving the hash slots specified as arguments.


## Required arguments

<details open><summary><code>slot [slot ...]</code></summary>

One or more hash slots to unassign from the current node.

</details>

## Examples

The following command removes the association for slots 5000 and
5001 from the node receiving the command:

    > CLUSTER DELSLOTS 5000 5001
    OK

## Details

### Usage in Redis Cluster

This command only works in cluster mode and may be useful for
debugging and in order to manually orchestrate a cluster configuration
when a new cluster is created. It is currently not used by `redis-cli`,
and mainly exists for API completeness.

### Other details

In the context of a node that has received a `CLUSTER DELSLOTS` command and
has consequently removed the associations for the passed hash slots,
we say those hash slots are *unbound*. Note that the existence of
unbound hash slots occurs naturally when a node has not been
configured to handle them (something that can be done with the
[`CLUSTER ADDSLOTS`](https://redis.io/docs/latest/commands/cluster-addslots) command) and if it has not received any information about
who owns those hash slots (something that it can learn from heartbeat
or update messages).

If a node with unbound hash slots receives a heartbeat packet from
another node that claims to be the owner of some of those hash
slots, the association is established instantly. Moreover, if a
heartbeat or update message is received with a configuration epoch
greater than the node's own, the association is re-established.

However, note that:

1. The command only works if all the specified slots are already
associated with some node.
2. The command fails if the same slot is specified multiple times.
3. As a side effect of the command execution, the node may go into
down state because not all hash slots are covered.


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the command was successful. Otherwise an error is returned.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the command was successful. Otherwise an error is returned.



