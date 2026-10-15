# Redis Enterprise Software Release Notes 6.0.8 (September 2020)

```json metadata
{
  "schema_version": 2,
  "title": "Redis Enterprise Software Release Notes 6.0.8 (September 2020)",
  "description": "RediSearch 2.0 support. Improved rladmin support for module upgrades.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"upgrade-instructions","title":"Upgrade instructions"},{"id":"end-of-life","title":"End of life"}],"id":"version-information","title":"Version information"},{"children":[{"id":"open-source-redis-6","title":"Open source Redis 6"},{"id":"upgrading-redis-modules-via-rladmin","title":"Upgrading Redis modules via rladmin"}],"id":"new-features","title":"New features"},{"id":"redis-modules","title":"Redis modules"},{"id":"additional-capabilities","title":"Additional capabilities"},{"id":"important-fixes","title":"Important fixes"},{"children":[{"id":"active-active-databases","title":"Active-Active databases"},{"id":"installation-limitations","title":"Installation limitations"},{"id":"upgrade","title":"Upgrade"},{"id":"redis-commands","title":"Redis commands"}],"id":"known-limitations","title":"Known limitations"}]}

,
  "codeExamples": []
}
```

[Redis Enterprise Software (RS) 6.0.8](https://redislabs.com/download-center/#downloads) is now available!
This version includes the new RediSearch 2.0 module, open source Redis 6.0.5, changes the rladmin tool for upgrading modules, and includes bug fixes.

## Version information

### Upgrade instructions

Follow [these instructions](https://redis.io/docs/latest/operate/rs/installing-upgrading/upgrading) for upgrading to RS 6.0.8 from RS 5.4.0 and above.
For Active-Active deployments, this release requires that you [upgrade the CRDB featureset version](https://redis.io/docs/latest/operate/rs/installing-upgrading/upgrading/upgrade-active-active).

### End of life

End of Life (EOL) for Redis Enterprise Software 6.0 and previous RS versions, can be found [here](https://redis.io/docs/latest/operate/rs/installing-upgrading/product-lifecycle).
EOL for Redis Modules can be found [here](https://redis.io/docs/latest/operate/rs/installing-upgrading/product-lifecycle).

- Support for Red Hat Enterprise Linux 6 and Oracle Linux 6 [operating systems platforms](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/supported-platforms) will end on November 30, 2020.
- Support for Ubuntu 14.04 (Trusty Tahr) [operating systems platforms](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/supported-platforms) will end on November 30, 2020.

## New features

### Open source Redis 6

RS 6.0 includes open source Redis 6.0.5.
For more information about Redis 6.0.5, check out the [release notes](https://raw.githubusercontent.com/redis/redis/6.0.5/00-RELEASENOTES).

### Upgrading Redis modules via rladmin

The [`rladmin` CLI](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin) introduces several updates to the commands for upgrading modules.
It is now easier to upgrade your modules to the latest module version.
Find out more [here](https://redis.io/docs/latest/operate/rs/installing-upgrading/modules/upgrade-module).

## Redis modules

The following GA releases of Redis Modules are bundled in RS 6.0:

- [RediSearch](https://redislabs.com/redis-enterprise/redis-search/), version [2.0](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisearch) (updated)
- [RedisJSON](https://redislabs.com/redis-enterprise/redis-json/), version [1.0.4](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisjson/redisjson-1.0-release-notes)
- [RedisGraph](https://redislabs.com/redis-enterprise/redis-graph/), version [2.0.19](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisgraph/redisgraph-2.0-release-notes) (updated)
- [RedisTimeSeries](https://redislabs.com/redis-enterprise/redis-time-series/), version [1.2.7](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redistimeseries/redistimeseries-1.2-release-notes) (updated)
- [RedisBloom](https://redislabs.com/redis-enterprise/redis-bloom/), version [2.2.4](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/release-notes/redisbloom/redisbloom-2.2-release-notes) (updated)

To use the updated modules with a database, you must [upgrade the module on the database](https://redis.io/docs/latest/operate/rs/installing-upgrading/modules/upgrade-module).

## Additional capabilities

- [Shard level metrics](https://redis.io/docs/latest/integrate/prometheus-with-redis-enterprise/prometheus-metrics-definitions#shard-metrics) have been added to the metrics_exporter and are now available from Prometheus. You can find all of the metrics [here](https://redis.io/docs/latest/integrate/prometheus-with-redis-enterprise/prometheus-metrics-definitions).

- RS DEB packages (for Ubuntu) and RPM packages (for RHEL) are now signed with a GPG key so customers can verify that the package is authentic and has not been tampered with. You can access the GPG on the [installaion page](https://redis.io/docs/latest/operate/rs/installing-upgrading#installing-rs-on-linux).

- The [`crdb-cli`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/crdb-cli) history log is now being added to support packages.

## Important fixes

- RS33193 - Improved log files handling in the proxy for large files.
- RS43572 - Fixed a bug causing the UI to fail when enabling SMTP STARTLS.
- RS46062 - Fixed missing metrics of Active-Active databases in Grafana.
- RS44758 - Fixed non responding button for saving a new user via the UI.
With build 6.0.8-32:
- RS45627, RS47382 - Fixed bugs causing clients to disconnect when using XREAD and XREADGROUP commands in blocking mode on other clients’ connections.

## Known limitations

-RS81463 - A shard may crash when resharding an Active-Active database with Auto Tiering . Specifically, the shard will crash when volatile keys or Active-Active tombstone keys reside in Flash memory.

### Active-Active databases
- RS44656 - A bug causing TLS mode for clients connections to toggle between ‘all communication’ to ‘for crdb communication only’ when performing a global configuration change.
- RS51359 - Active-Active databases, using replication and Append Only File (AOF) for [Database persistence](https://redis.io/docs/latest/operate/rs/databases/configure/database-persistence), are suffering from memory leaks on replica shards, causing them to grow bigger than the master shards. Customers are advised to upgrade to RS 6.0.12. Meanwhile you can use snapshots for database persistence or restart the replica shards.

### Installation limitations

Several Redis Enterprise Software installation reference files are installed to the directory `/etc/opt/redislabs/` even if you use [custom installation directories](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/customize-install-directories).

As a workaround to install Redis Enterprise Software without using any root directories, do the following before installing Redis Enterprise Software:

1. Create all custom, non-root directories you want to use with Redis Enterprise Software.

1. Mount `/etc/opt/redislabs` to one of the custom, non-root directories.

### Upgrade

- [RS 5.4.2](https://redis.io/docs/latest/operate/rs/release-notes/legacy-release-notes/rs-5-4-2-april-2019) introduced new Active-Active Redis Database capabilities that improve its compatibility with open source Redis. Now the string data-type in Active-Active Redis Database is implicitly and dynamically typed, just like open source Redis. To use the new capabilities on nodes that are upgraded from version RS 5.4.2 or lower, you must [upgrade the Active-Active Redis Database protocol](https://redis.io/docs/latest/operate/rs/installing-upgrading/upgrading#upgrading-crdbs).
- When you upgrade an Active-Active Redis with active AOF from version [RS 5.4.2](https://redis.io/docs/latest/operate/rs/release-notes/legacy-release-notes/rs-5-4-2-april-2019) or lower to version [RS 5.4.2](https://redis.io/docs/latest/operate/rs/release-notes/legacy-release-notes/rs-5-4-4-june-2019) or higher:
    - If replication is enabled, you must run the BGREWRITEAOF command on all replica shards after the upgrade.
    - If replication is not enabled, you must run the BGREWRITEAOF command on all shards after the upgrade.
- Node upgrade fails if the SSL certificates were configured in version 5.0.2 or above by manually updating the certificates on the disk instead of [updating them through the API](https://redis.io/docs/latest/operate/rs/security/certificates/updating-certificates).
    For assistance with this issue, contact [Support](https://redislabs.com/support).
- Starting from [RS 5.4.2](https://redis.io/docs/latest/operate/rs/release-notes/legacy-release-notes/rs-5-4-2-april-2019), to preserve the current Redis major.minor version during database upgrade you must use the keep_redis_version option instead of keep_current_version.

### Redis commands

- The capability of disabling specific Redis commands does not work on commands specific to Redis Modules.
- Starting from RS 5.4.2 and after you upgrade an Active-Active database, TYPE commands for string data-type in Active-Active databases return "string" (OSS Redis standard).

