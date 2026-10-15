# Durability and high availability

```json metadata
{
  "schema_version": 2,
  "title": "Durability and high availability",
  "description": "Overview of Redis Software durability features such as replication, clustering, and rack-zone awareness.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"replication","title":"Replication"},{"id":"clustering","title":"Clustering"},{"id":"database-persistence","title":"Database persistence"},{"id":"active-active-geo-distributed-replication","title":"Active-Active geo-distributed replication"},{"id":"rack-zone-awareness","title":"Rack-zone awareness"},{"id":"discovery-service","title":"Discovery service"}]}

,
  "codeExamples": []
}
```

Redis Software comes with several features that make your data more durable and accessible. The following features can help protect your data in cases of failures or outages and help keep your data available when you need it.

## Replication

When you [replicate your database](https://redis.io/docs/latest/operate/rs/databases/durability-ha/replication), each database instance (primary shard) is copied to a replica shard. When a primary shard fails, the cluster automatically promotes a replica shard to primary.

## Clustering

[Clustering](https://redis.io/docs/latest/operate/rs/databases/durability-ha/clustering) (or sharding) breaks your database into individual instances (shards) and spreads them across several nodes. Clustering lets you add resources to your cluster to scale your database and prevents node failures from causing availability loss.

## Database persistence

[Database persistence](https://redis.io/docs/latest/operate/rs/databases/configure/database-persistence) gives your database durability against process or server failures by saving data to disk at set intervals.

## Active-Active geo-distributed replication

[Active-Active Redis Software databases](https://redis.io/docs/latest/operate/rs/databases/active-active) allow reading and writing to the same dataset from multiple clusters in different geographic locations. This increases the durability of your database by reducing the likelihood of data or availability loss. It also reduces data access latency by serving requests from the nearest cluster.

## Rack-zone awareness

[Rack-zone awareness](https://redis.io/docs/latest/operate/rs/clusters/configure/rack-zone-awareness) maps each node in your Redis Software cluster to a physical rack or logical zone. The cluster uses this information to distribute primary shards and their replica shards in different racks or zones. This ensures data availability if a rack or zone fails.

## Discovery service

The [discovery service](https://redis.io/docs/latest/operate/rs/databases/durability-ha/discovery-service) provides an IP-based connection management service used when connecting to Redis Software databases. It lets your application discover which node hosts the database endpoint. The discovery service API complies with the [Redis Sentinel API](https://redis.io/docs/latest/operate/oss_and_stack/management/sentinel#sentinel-api).
