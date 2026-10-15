# Shard placement policy

```json metadata
{
  "schema_version": 2,
  "title": "Shard placement policy",
  "description": "Detailed info about the shard placement policy.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"dense-shard-placement-policy","title":"Dense shard placement policy"},{"id":"sparse-shard-placement-policy","title":"Sparse shard placement policy"}],"id":"shard-placement-policies","title":"Shard placement policies"},{"id":"related-articles","title":"Related articles"}]}

,
  "codeExamples": []
}
```

In Redis Software, the location of master and replica shards on the cluster nodes can impact the database and node performance.
Master shards and their corresponding replica shards are always placed on separate nodes for data resiliency.
The shard placement policy helps to maintain optimal performance and resiliency.

In addition to the shard placement policy, considerations that determine shard placement are:

- Separation of master and replica shards
- Available persistence and Auto Tiering storage
- [Rack-zone awareness](https://redis.io/docs/latest/operate/rs/clusters/configure/rack-zone-awareness)
- Memory available to host the database when fully populated

The shard placement policies are:

- `dense` - Place as many shards as possible on the smallest number of nodes to reduce the latency between the proxy and the database shards;
    Recommended for Redis on RAM databases to optimize memory resources
- `sparse` - Spread the shards across as many nodes in the cluster as possible to spread the traffic across cluster nodes;
    Recommended for databases with Auto Tiering enabled to optimize disk resources

When you create a Redis Software cluster, the default shard placement policy (`dense`) is assigned to all databases that you create on the cluster.

You can:

- Change the default shard placement policy for the cluster to `sparse` so that the cluster applies that policy to all databases that you create
- Change the shard placement policy for each database after the database is created

## Shard placement policies

### Dense shard placement policy

In the dense policy, the cluster places the database shards on as few nodes as possible.
When the node is not able to host all of the shards, some shards are moved to another node to maintain optimal node health.

For example, for a database with two master and two replica shards on a cluster with three nodes and a dense shard placement policy,
the two master shards are hosted on one node and the two replica shards are hosted on another node.

For Redis on RAM databases without the OSS cluster API enabled, use the dense policy to optimize performance.

![](https://redis.io/docs/latest/images/rs/dense_placement.png)

*Figure: Three nodes with two master shards (red) and two replica shards (white) with a dense placement policy*

### Sparse shard placement policy

In the sparse policy, the cluster places shards on as many nodes as possible to distribute the shards of a database across all available nodes.
When all nodes have database shards, the shards are distributed evenly across the nodes to maintain optimal node health.

For example, for a database with two master and two replica shards on a cluster with three nodes and a sparse shard placement policy:

- Node 1 hosts one of the master shards
- Node 2 hosts the replica for the first master shard
- Node 3 hosts the second master shard
- Node 1 hosts for the replica shard for master shard 2

For Redis on RAM databases with OSS cluster API enabled and for databases with Auto Tiering enabled, use the sparse policy to optimize performance.

![](https://redis.io/docs/latest/images/rs/sparse_placement.png)

*Figure: Three nodes with two master shards (red) and two replica shards (white) with a sparse placement policy*

## Related articles

You can [configure the shard placement policy](https://redis.io/docs/latest/operate/rs/databases/configure/shard-placement) for each database.

