# Install and upgrade modules

```json metadata
{
  "schema_version": 2,
  "title": "Install and upgrade modules",
  "description": "",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"automatically-enabled-capabilities-in-redis-8","title":"Automatically enabled capabilities in Redis 8"}]}

,
  "codeExamples": []
}
```


Several modules that provide additional Redis capabilities, such as Redis Search, JSON, time series, and probabilistic data structures, come packaged with [Redis Software](https://redis.io/docs/latest/operate/rs). As of version 8.0, Redis Software includes multiple feature sets, compatible with different Redis database versions.

However, if you want to use additional modules or upgrade a module to a more recent version, you need to:

1. [Install a module package](https://redis.io/docs/latest/operate/rs/installing-upgrading/modules/add-module-to-cluster) on the cluster.
1. [Enable a module](https://redis.io/docs/latest/operate/rs/installing-upgrading/modules/add-module-to-database) for a new database or [upgrade a module](https://redis.io/docs/latest/operate/rs/installing-upgrading/modules/upgrade-module) in an existing database.

## Automatically enabled capabilities in Redis 8

Databases created with or upgraded to Redis version 8 or later automatically enable the capabilities (modules) bundled with Redis Software as follows:

| Database type | Automatically enabled capabilities |
|---------------|------------------------------------|
| RAM-only | [Redis Search](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/search)<br />[JSON](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/json)<br />[Time series](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/timeseries)<br />[Probabilistic](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/bloom)  |
| Flash-enabled ([Redis Flex](https://redis.io/docs/latest/operate/rs/databases/flash)) | [JSON](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/json)<br />[Probabilistic](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/bloom) |
| [Active-Active](https://redis.io/docs/latest/operate/rs/databases/active-active)<sup>[1](#enabled-modules-table-note-1)</sup> | [Redis Search](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/search/search-active-active)<br />[JSON](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/json) |

1. <a name="enabled-modules-table-note-1"></a>Upgrading existing Active-Active databases to Redis version 8 does not automatically enable these capabilities. Only new Active-Active databases created with Redis version 8 enable these capabilities by default.

