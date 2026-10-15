# Redis Software compatibility with Redis Open Source

```json metadata
{
  "schema_version": 2,
  "title": "Redis Software compatibility with Redis Open Source",
  "description": "Redis Software compatibility with Redis Open Source.",
  "categories": ["docs","operate","rs","rc"],
  "tableOfContents": {"sections":[{"id":"resp-compatibility","title":"RESP compatibility"},{"id":"client-side-caching-compatibility","title":"Client-side caching compatibility"},{"id":"compatibility-with-open-source-redis-cluster-api","title":"Compatibility with open source Redis Cluster API"}]}

,
  "codeExamples": []
}
```

Both Redis Software and [Redis Cloud](https://redis.io/docs/latest/operate/rc) are compatible with Redis Open Source. 

If you're planning a move from a self-managed Redis Open Source deployment to Redis Software, see [Move from Redis Open Source to Redis Software](https://redis.io/docs/latest/operate/rs/installing-upgrading/move-from-open-source) for how configuration and deployment differ.

Redis contributes extensively to the Redis project and uses it inside of Redis Software and Redis Cloud. As a rule, we adhere to the project's specifications and update both products with the latest version of Redis.

## Redis commands

See [Compatibility with Redis commands](https://redis.io/docs/latest/operate/rs/references/compatibility/commands) to learn which Redis commands are compatible with Redis Software and Redis Cloud.

## Configuration settings

[Compatibility with Redis configuration settings](https://redis.io/docs/latest/operate/rs/references/compatibility/config-settings) lists the Redis configuration settings supported by Redis Software and Redis Cloud.

## Redis clients

You can use any standard [Redis client](https://redis.io/docs/latest/develop/clients) with Redis Software and Redis Cloud.

## RESP compatibility

Redis Software and Redis Cloud support RESP2 and RESP3. See [RESP compatibility with Redis Software](https://redis.io/docs/latest/operate/rs/references/compatibility/resp) for more information.

## Client-side caching compatibility

Redis Software and Redis Cloud support [client-side caching](https://redis.io/docs/latest/develop/clients/client-side-caching) for databases with Redis versions 7.4 or later. See [Client-side caching compatibility with Redis Software and Redis Cloud](https://redis.io/docs/latest/operate/rs/references/compatibility/client-side-caching) for more information about compatibility and configuration options.

## Compatibility with open source Redis Cluster API

Redis Software supports [Redis OSS Cluster API](https://redis.io/docs/latest/operate/rs/clusters/optimize/oss-cluster-api) if it is enabled for a database. For more information, see [Enable OSS Cluster API](https://redis.io/docs/latest/operate/rs/databases/configure/oss-cluster-api).

