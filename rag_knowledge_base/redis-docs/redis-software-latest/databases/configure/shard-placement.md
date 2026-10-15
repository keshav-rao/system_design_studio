# Configure shard placement

```json metadata
{
  "schema_version": 2,
  "title": "Configure shard placement",
  "description": "Configure shard placement to improve performance.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"default-shard-placement-policy","title":"Default shard placement policy"},{"id":"shard-placement-policy-for-a-database","title":"Shard placement policy for a database"}]}

,
  "codeExamples": []
}
```

In Redis Software, the location of master and replica shards on the cluster nodes can impact the database and node performance.
Master shards and their corresponding replica shards are always placed on separate nodes for data resiliency.
The [shard placement policy](https://redis.io/docs/latest/operate/rs/databases/memory-performance/shard-placement-policy) helps to maintain optimal performance and resiliency.

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

## Default shard placement policy

When you create a new cluster, the cluster configuration has a `dense` default shard placement policy.
When you create a database, this default policy is applied to the new database.

To see the current default shard placement policy, run `rladmin info cluster`:

![](https://redis.io/docs/latest/images/rs/shard_placement_info_cluster.png)

To change the default shard placement policy so that new databases are created with the `sparse` shard placement policy, run:

```sh
rladmin tune cluster default_shards_placement [ dense | sparse ]
```

## Shard placement policy for a database

To see the shard placement policy for a database in `rladmin status`.

![](https://redis.io/docs/latest/images/rs/shard_placement_rladmin_status.png)

To change the shard placement policy for a database, run:

```sh
rladmin tune db { db:<ID> | <database-name> } shards_placement { dense | sparse }
```

