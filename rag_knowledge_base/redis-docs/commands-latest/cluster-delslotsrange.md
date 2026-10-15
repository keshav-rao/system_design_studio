# CLUSTER DELSLOTSRANGE

```json metadata
{
  "schema_version": 2,
  "title": "CLUSTER DELSLOTSRANGE",
  "description": "Sets hash slot ranges as unbound for a node.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"arguments":[{"display_text":"start-slot","name":"start-slot","type":"integer"},{"display_text":"end-slot","name":"end-slot","type":"integer"}],"multiple":true,"name":"range","type":"block"}],
  "syntax_fmt": "CLUSTER DELSLOTSRANGE start-slot end-slot [start-slot end-slot ...]",
  "complexity": "O(N) where N is the total number of the slots between the start slot and end slot arguments.",
  "group": "cluster",
  "command_flags": ["admin","stale","no_async_loading"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "7.0.0",
  "arity": -4,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"children":[{"id":"usage-in-redis-cluster","title":"Usage in Redis Cluster"}],"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `CLUSTER DELSLOTSRANGE` command is similar to the [`CLUSTER DELSLOTS`](https://redis.io/docs/latest/commands/cluster-delslots) command in that they both remove hash slots from the node.
The difference is that [`CLUSTER DELSLOTS`](https://redis.io/docs/latest/commands/cluster-delslots) takes a list of hash slots to remove from the node, while `CLUSTER DELSLOTSRANGE` takes a list of slot ranges (specified by start and end slots) to remove from the node.

## Required arguments

<details open><summary><code>start-slot end-slot [start-slot end-slot ...]</code></summary>

One or more inclusive ranges of hash slots to unassign from the current node.

</details>

## Examples

To remove slots 1 2 3 4 5 from the node, the [`CLUSTER DELSLOTS`](https://redis.io/docs/latest/commands/cluster-delslots) command is:

    > CLUSTER DELSLOTS 1 2 3 4 5
    OK

The same operation can be completed with the following `CLUSTER DELSLOTSRANGE` command:

    > CLUSTER DELSLOTSRANGE 1 5
    OK

However, note that:

1. The command only works if all the specified slots are already associated with the node.
2. The command fails if the same slot is specified multiple times.
3. As a side effect of the command execution, the node may go into *down* state because not all hash slots are covered.

## Details

### Usage in Redis Cluster

This command only works in cluster mode and may be useful for
debugging and in order to manually orchestrate a cluster configuration
when a new cluster is created. It is currently not used by `redis-cli`,
and mainly exists for API completeness.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the command was successful. Otherwise an error is returned.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the command was successful. Otherwise an error is returned.



