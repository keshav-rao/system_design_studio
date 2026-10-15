# rladmin placement

```json metadata
{
  "schema_version": 2,
  "title": "rladmin placement",
  "description": "Configures the shard placement policy for a database.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Configures the shard placement policy for a specified database.

``` sh
rladmin placement
        db { db:<id> | <name> }
        { dense | sparse }
```

> [!NOTE]
> `rladmin placement db` is deprecated and will be removed in a future version. Use [`rladmin tune db`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/tune#tune-db) with the `shards_placement` parameter instead.

### Parameters

| Parameter | Type/Value                     | Description                                                                                   |
|-----------|--------------------------------|-----------------------------------------------------------------------------------------------|
| db        | db:\<id\><br /> name           | Configures shard placement for the specified database                                         |
| dense     |                                | Places new shards on the same node as long as it has resources                                |
| sparse    |                                | Places new shards on the maximum number of available nodes within the cluster                 |

### Returns

Returns the new shard placement policy if the policy was changed successfully. Otherwise, it returns an error.

Use [`rladmin status databases`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/status#status-databases) to verify that the failover completed.

### Example

``` sh
$ rladmin status databases
DATABASES:
DB:ID  NAME       TYPE   STATUS   SHARDS   PLACEMENT    REPLICATION    PERSISTENCE    ENDPOINT                                
db:5   tr01       redis  active   1        dense        enabled        aof            redis-12000.cluster.local:12000         
$ rladmin placement db db:5 sparse
Shards placement policy is now sparse
$ rladmin status databases
DATABASES:
DB:ID  NAME       TYPE   STATUS   SHARDS   PLACEMENT    REPLICATION    PERSISTENCE    ENDPOINT                                
db:5   tr01       redis  active   1        sparse       enabled        aof            redis-12000.cluster.local:12000         
```

