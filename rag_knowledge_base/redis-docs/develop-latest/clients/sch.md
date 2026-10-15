# Smart client handoffs

```json metadata
{
  "schema_version": 2,
  "title": "Smart client handoffs",
  "description": "Learn how to avoid disruptions during Redis server maintenance.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "topics": ["smart-client-handoffs","resilience"],
  "relatedPages": ["/develop/clients/redis-py/connect#connect-using-smart-client-handoffs-sch","/develop/clients/nodejs/connect#connect-using-smart-client-handoffs-sch","/develop/clients/lettuce/connect#connect-using-smart-client-handoffs-sch","/develop/clients/go/connect#connect-using-smart-client-handoffs-sch","/develop/clients/dotnet/connect#connect-using-smart-client-handoffs-sch"],
  "scope": "overview",
  "tableOfContents": {"sections":[{"id":"sch-support-in-redis-client-libraries","title":"SCH support in Redis client libraries"},{"children":[{"id":"redis-cloud","title":"Redis Cloud"},{"id":"redis-software","title":"Redis Software"},{"id":"redis-enterprise-for-kubernetes","title":"Redis Enterprise for Kubernetes"},{"id":"redis-open-source","title":"Redis Open Source"}],"id":"sch-support-in-redis-server-products","title":"SCH support in Redis server products"}]}

,
  "codeExamples": []
}
```


*Smart client handoffs (SCH)* is a feature of Redis Cloud and
Redis Software servers that lets them actively notify clients
about planned server maintenance shortly before it happens. This
lets a client reconnect or otherwise respond gracefully without significant
interruptions in service.

SCH is primarily useful when server software or hardware upgrades
are required. It provides two main features to help the
client avoid disruptions in service during the maintenance period:

-   **Relaxed timeouts**: Upgrades tend to impact the general performance of the server.
    Advance notification of the upgrade lets a client adjust its command
    timeouts to take this into account and avoid aborting commands too soon.
-   **Pre-handoffs**: Upgrades also involve migrating
    Redis shards to new nodes, which inevitably disconnects clients from
    existing nodes. However, with some advance warning of the disconnection,
    a client can buffer commands, connect to a new node, and then resume
    the buffered commands without aborting any of them. As a result, users
    see no disruption in service. These transparent reconnections to new endpoints
    are known as *pre-handoffs*.

> [!NOTE]
> SCH does not work with blocking connections.
> These include connections used for blocking operations like
> [`BLPOP`](https://redis.io/docs/latest/commands/blpop) and also
> [pub/sub](https://redis.io/docs/latest/develop/pubsub) subscriptions.
> All non-blocking operations are safe to use with SCH.

## SCH support in Redis client libraries

SCH is enabled automatically on the client side during connection
if you select the [RESP3](https://redis.io/docs/latest/develop/reference/protocol-spec#resp-versions)
protocol, which is a requirement for SCH. However, you can
configure some parameters, such as the timeouts to use
during maintenance.

The following table lists the Redis client libraries that support SCH,
and the versions that added support for standard routing and for
[OSS Cluster API](https://redis.io/docs/latest/operate/rs/databases/configure/oss-cluster-api) connections.
Standard routing covers any connection that doesn't use the OSS Cluster API.

| Client | Standard routing | OSS Cluster API |
| :-- | :-- | :-- |
| [redis-py](https://redis.io/docs/latest/develop/clients/redis-py/connect#connect-using-smart-client-handoffs-sch) | v7.0.0 | v7.2.0 |
| [node-redis](https://redis.io/docs/latest/develop/clients/nodejs/connect#connect-using-smart-client-handoffs-sch) | v5.9.0 | v5.11.0 |
| [Lettuce](https://redis.io/docs/latest/develop/clients/lettuce/connect#connect-using-smart-client-handoffs-sch) | v7.0.0 | - |
| [go-redis](https://redis.io/docs/latest/develop/clients/go/connect#connect-using-smart-client-handoffs-sch) | v9.16.0 | v9.18.0 |
| [StackExchange.Redis](https://redis.io/docs/latest/develop/clients/dotnet/connect#connect-using-smart-client-handoffs-sch) | v3.3.0 | v3.3.0 |

> [!NOTE]
> SCH is currently disabled when a client is configured for
> [Client-side geographic failover](https://redis.io/docs/latest/develop/clients/failover).
> Integration of the two features is planned for a future release.

## SCH support in Redis server products

### Redis Cloud

SCH is fully supported and enabled by default on Redis Cloud, except when you
are using one of the following options:

- [AWS PrivateLink](https://redis.io/docs/latest/operate/rc/security/aws-privatelink)
- [Google Cloud Private Service Connect](https://redis.io/docs/latest/operate/rc/security/private-service-connect)

These services don't currently allow for pre-handoffs, but you still get the
benefit of relaxed timeouts during database version upgrades. All other
configurations have full support for both relaxed timeouts and pre-handoffs.

### Redis Software

You must enable SCH explicitly on self-managed Redis Software servers by using the
[v1/cluster](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/cluster)
REST API request to set the `client_maint_notifications` option to `true`.
The example below shows how to do this using the
[`curl`](https://curl.se/) command line utility:

```bash
curl -k -X PUT -H "accept: application/json" \
    -H "content-type: application/json" \
    -u "test@redis.com:test123" \
    -d '{ "client_maint_notifications": true }' \
    https://localhost:9443/v1/cluster
```

Redis Software uses relaxed timeouts to avoid command failures during
database version upgrades. SCH is supported for Redis Software from v8.0.2 on,
and OSS Cloud and OSS Cluster API from v8.0.16 on.

The degree of support for pre-handoffs depends on
the specific upgrade method you use, as detailed in the table below.

| Upgrade method | SCH support | Expected behavior |
| --- | --- | --- |
| [Rolling upgrade](https://redis.io/docs/latest/operate/rs/installing-upgrading/upgrading/upgrade-cluster#rolling-upgrade) | Full | New nodes and old ones removed sequentially. SCH pre-handoffs and relaxed timeouts greatly reduce disruptions during the upgrade. |
| [In-place upgrade](https://redis.io/docs/latest/operate/rs/installing-upgrading/upgrading/upgrade-cluster#in-place-upgrade) | Partial | Relaxed timeouts reduce errors but there are no pre-handoffs. Disconnections occur when processes are replaced during the upgrade, so clients should rely on auto-reconnect, which will cause brief lapses in service. |
| [Maintenance mode](https://redis.io/docs/latest/operate/rs/clusters/maintenance-mode) | Full | SCH is fully supported during hardware or OS patching operations. Pre-handoffs and relaxed timeouts minimize application impact. |


### Redis Enterprise for Kubernetes

SCH is not currently supported for [Kubernetes](https://redis.io/docs/latest/operate/kubernetes) clusters.

### Redis Open Source

SCH is not currently supported for [Redis Open Source](https://redis.io/docs/latest/operate/oss_and_stack).

