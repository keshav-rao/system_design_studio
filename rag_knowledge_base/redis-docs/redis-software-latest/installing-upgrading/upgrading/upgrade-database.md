# Upgrade a Redis Software database

```json metadata
{
  "schema_version": 2,
  "title": "Upgrade a Redis Software database",
  "description": "Upgrade a Redis Software database.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"default-db-versions","title":"Default Redis database versions"},{"id":"upgrade-prerequisites","title":"Upgrade prerequisites"},{"id":"upgrade-database","title":"Upgrade database"}]}

,
  "codeExamples": []
}
```


## Default Redis database versions {#default-db-versions}

When you upgrade an existing database, it uses the latest bundled Redis version unless you specify a different version with the `redis_version` option in the [REST API](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs) or [`rladmin upgrade db`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/upgrade#upgrade-db).

To view available Redis database versions:

- In the Cluster Manager UI, see **Redis database versions** on the **Cluster > Configuration** screen.

- Send a [`GET /nodes` REST API request](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/nodes) and see `supported_database_versions` in the response.

The default Redis database version differs between Redis Software releases as follows:

<a name="db-versions-table"></a>
| Redis Software<br />cluster version | Bundled Redis<br />DB versions | Default DB version<br />(upgraded/new databases) |
|-------|----------|-----|
| 8.2.0 | 6.2, 7.2, 7.4, 8.0, 8.2, 8.4, 8.6 | 8.6 |
| 8.0.20 | 6.2, 7.2, 7.4, 8.0, 8.2, 8.4, 8.6 | 8.6 |
| 8.0.18 | 6.2, 7.2, 7.4, 8.0, 8.2, 8.4, 8.6 | 8.6 |
| 8.0.16 | 6.2, 7.2, 7.4, 8.0, 8.2, 8.4 | 8.4 |
| 8.0.10 | 6.2, 7.2, 7.4, 8.0, 8.2, 8.4 | 8.4 |
| 8.0.6 | 6.2, 7.2, 7.4, 8.0, 8.2 | 8.2 |
| 8.0.2 | 6.2, 7.2, 7.4, 8.0, 8.2 | 8.2 |
| 7.22.x | 6.2, 7.2, 7.4 | 7.4 |
| 7.8.x | 6.2, 7.2, 7.4 | 7.4 |
| 7.4.x | 6.0, 6.2, 7.2 | 7.2 |
| 7.2.4 | 6.0, 6.2, 7.2 | 7.2 |
| 6.4.2 | 6.0, 6.2 | 6.2 |
| 6.2.x | 6.0, 6.2 | 6.0 |

## Upgrade prerequisites

Before upgrading a database:

- Review the relevant [release notes](https://redis.io/docs/latest/operate/rs/release-notes) for any preparation instructions.

- Verify that both the [current database version and the target database version are supported](#db-versions-table) by the cluster's Redis Software version.

    To determine the current database version:

    - Use the Cluster Manager UI to open the **Configuration** tab for the database and select ![The About database button](https://redis.io/docs/latest/images/rs/icons/info-icon.png#no-click) **About**.

    - _(Optional)_ Use the [`rladmin status extra all`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/status) command to display configuration details:

        ```sh
        rladmin status extra all
        ```
    
        When the database compatibility version is outdated, <nobr>`OLD REDIS VERSION`</nobr> appears in the command output.

- Verify the cluster is fully upgraded and operational.

    Use the Cluster Manager UI to display the **Configuration** tab for the cluster. The tab displays the cluster version information and the Redis database compatibility version.

- For [Replica Of databases](https://redis.io/docs/latest/operate/rs/databases/import-export/replica-of), upgrade the destination database before the source database.

- Check client compatibility with the database version.

    If you run Redis Stack commands with Go-Redis versions 9 and later or Lettuce versions 6 and later, set the client’s protocol version to RESP2 before upgrading your database to Redis version 7.2 to prevent potential application issues due to RESP3 breaking changes. See [Client prerequisites for Redis 7.2 upgrade](https://redis.io/docs/latest/operate/rs/references/compatibility/resp#client-prerequisites-for-redis-72-upgrade) for more details and examples.

- To avoid data loss during the upgrade, [back up your data](https://redis.io/docs/latest/operate/rs/databases/import-export/schedule-backups).  

    You can [export the data](https://redis.io/docs/latest/operate/rs/databases/import-export/export-data) to an external location, [enable replication](https://redis.io/docs/latest/operate/rs/databases/durability-ha/replication), or [enable persistence](https://redis.io/docs/latest/operate/rs/databases/configure/database-persistence).

    When choosing how to back up data, keep the following in mind:

    - To reduce downtime when replication is enabled, a failover is performed before restarting the primary (master) database.

    - When persistence is enabled without replication, the database is unavailable during restart because the data is restored from the persistence file. AOF persistence restoration is slower than snapshot restoration.

## Upgrade database

To upgrade a database:

**Cluster Manager UI:**

1. Complete all [prerequisites](#upgrade-prerequisites) before starting the upgrade.

1. Optionally, back up the database to minimize the risk of data loss.

1. Upgrade the database and its modules from the **Databases** screen or an individual database's **Configuration** screen in the Cluster Manager UI. During the upgrade process, the database will restart without losing any data.

    To upgrade a database from the **Databases** screen:

    1. Expand the database in the **Databases** list to show details.

        ![The database details are expanded, including an upgrade option.](https://redis.io/docs/latest/images/rs/screenshots/databases/expand-db-details.png)

    1. Click **Upgrade**.

    1. For **Select version**, choose the Redis version for the database upgrade from the list.

    1. Click **Upgrade**.

    1. After the upgrade process finishes, check the expanded database details to verify that the Redis version is set to the expected value.

    To upgrade a database from its **Configuration** screen:

    1. Select the database from the **Databases** list and go to its **Configuration** screen.

    1. Click the **More actions** button (**&vellip;**).

    1. Select **Upgrade version** from the list.

        ![The upgrade version option is selected in the more actions list.](https://redis.io/docs/latest/images/rs/screenshots/databases/db-more-actions-upgrade-version.png)

    1. For **Select version**, choose the Redis version for the database upgrade from the list.

    1. Click **Upgrade**.

    1. After the upgrade process finishes, click the **About** button (&#9432;) and verify that the Redis version is set to the expected value.

**rladmin:**

1. Complete all [prerequisites](#upgrade-prerequisites) before starting the upgrade.

1. Optionally, back up the database to minimize the risk of data loss.

1. Upgrade the database using [`rladmin upgrade db`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/upgrade). During the upgrade process, the database will restart without losing any data. Use the `preserve_roles` option to keep the database's current state, including primary shard placement, and prevent the cluster from becoming unbalanced.

    To upgrade a database and its modules:

    ```sh
    rladmin upgrade db <database name | database ID> preserve_roles
    ```

    Example of a successful upgrade:

    ```sh
    rladmin> upgrade db demo
    Monitoring d194c4a3-631c-4726-b799-331b399fc85c
    active - SMUpgradeBDB init
    active - SMUpgradeBDB wait_for_version
    active - SMUpgradeBDB configure_shards
    completed - SMUpgradeBDB
    Done
    ```

    To upgrade the database to a version other than the default version, use the `redis_version` parameter:

    ```sh
    rladmin upgrade db <database name | database ID> redis_version <version> preserve_roles
    ```

    For module upgrade options, see [Upgrade modules](https://redis.io/docs/latest/operate/rs/installing-upgrading/modules/upgrade-module).

1. Use [`rladmin status databases extra all`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/status#status-databases) to display a list of the databases in your cluster and their current Redis database compatibility version. Verify that the Redis version is set to the expected value.

    ```sh
    rladmin status databases extra all
    ```

**REST API:**

1. Complete all [prerequisites](#upgrade-prerequisites) before starting the upgrade.

1. Optionally, back up the database to minimize the risk of data loss.

1. Use an [upgrade database](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs/upgrade) REST API request. During the upgrade process, the database will restart without losing any data. Use the `preserve_roles` option to keep the database's current state, including primary shard placement, and prevent the cluster from becoming unbalanced.

    ```sh
    POST https://<host>:<port>/v1/bdbs/<database_id>/upgrade
    {
        "preserve_roles": true,
        // Additional fields
    }
    ```

    For additional database upgrade options, see the [request body](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs/upgrade#request-body) section of the database upgrade requests reference.



