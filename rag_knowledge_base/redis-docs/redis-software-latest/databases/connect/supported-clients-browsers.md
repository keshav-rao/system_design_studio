# Supported connection clients

```json metadata
{
  "schema_version": 2,
  "title": "Supported connection clients",
  "description": "Info about Redis client libraries and supported clients when using the discovery service.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"discovery-service","title":"Discovery service"}],"id":"redis-client-libraries","title":"Redis client libraries"}]}

,
  "codeExamples": []
}
```

You can connect to Redis Software databases programmatically using client libraries.

## Redis client libraries

To connect an application to a Redis database hosted by Redis Software, use a [client library](https://redis.io/docs/latest/develop/clients) appropriate for your programming language.

You can also use the `redis-cli` utility to connect to a database from the command line.

For examples of each approach, see the [Redis Software quickstart](https://redis.io/docs/latest/operate/rs/installing-upgrading/quickstarts/redis-enterprise-software-quickstart).

Note: You cannot use client libraries to configure Redis Software.  Instead, use:

- The Redis Software [Cluster Manager UI](https://redis.io/docs/latest/operate/rs/installing-upgrading/quickstarts/redis-enterprise-software-quickstart)
- The [REST API](https://redis.io/docs/latest/operate/rs/references/rest-api)
- Command-line utilities, such as [`rladmin`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin)

### Discovery service

All [recommended Redis client libraries](https://redis.io/docs/latest/develop/clients) support the Redis Sentinel API, so you can use any of them with the [discovery service](https://redis.io/docs/latest/operate/rs/databases/durability-ha/discovery-service).

If you need to use a client that doesn't support Sentinel, you can use [Sentinel Tunnel](https://github.com/RedisLabs/sentinel_tunnel) to discover the current primary Redis endpoint with Sentinel and create a TCP tunnel between a local port on the client and the primary endpoint.


