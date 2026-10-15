# Redis Cloud compatibility with Redis Open Source

```json metadata
{
  "schema_version": 2,
  "title": "Redis Cloud compatibility with Redis Open Source",
  "description": "Redis Cloud compatibility with Redis Open Source.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"resp-compatibility","title":"RESP compatibility"},{"id":"client-side-caching-compatibility","title":"Client-side caching compatibility"},{"id":"compatibility-with-redis-cluster-api","title":"Compatibility with Redis Cluster API"}]}

,
  "codeExamples": []
}
```


Both [Redis Software](https://redis.io/docs/latest/operate/rs) and Redis Cloud are compatible with Redis Open Source.

Redis contributes extensively to the Redis project and uses it inside of Redis Software and Redis Cloud. As a rule, we adhere to the project's specifications and update both products with the latest version of Redis.

## Redis commands

See [Compatibility with Redis commands](https://redis.io/docs/latest/operate/rs/references/compatibility/commands) to learn which Redis commands are compatible with Redis Software and Redis Cloud.

## Configuration settings

[Compatibility with Redis configuration settings](https://redis.io/docs/latest/operate/rs/references/compatibility/config-settings) lists the Redis configuration settings supported by Redis Software and Redis Cloud.

## Redis clients

You can use any standard [Redis client](https://redis.io/docs/latest/develop/clients) with Redis Software and Redis Cloud.

## RESP compatibility

Redis Software and Redis Cloud support RESP2 and RESP3. In Redis Cloud, you can choose between RESP2 and RESP3 when you [create a database](https://redis.io/docs/latest/operate/rc/databases/create-database) and you can change it when you [edit a database](https://redis.io/docs/latest/operate/rc/databases/view-edit-database). For more information about the different RESP versions, see the [Redis serialization protocol specification](https://redis.io/docs/latest/develop/reference/protocol-spec#resp-versions).

## Client-side caching compatibility

Redis Software and Redis Cloud support [client-side caching](https://redis.io/docs/latest/develop/clients/client-side-caching) for databases with Redis versions 7.4 or later. See [Client-side caching compatibility with Redis Software and Redis Cloud](https://redis.io/docs/latest/operate/rs/references/compatibility/client-side-caching) for more information about compatibility.

## Compatibility with Redis Cluster API

Redis Cloud supports [Redis Cluster API](https://redis.io/docs/latest/operate/rc/databases/configuration/clustering#oss-cluster-api) on Redis Cloud Pro if it is enabled for a database. Review [Redis Cluster API architecture](https://redis.io/docs/latest/operate/rs/clusters/optimize/oss-cluster-api) to determine if you should enable this feature for your database.
