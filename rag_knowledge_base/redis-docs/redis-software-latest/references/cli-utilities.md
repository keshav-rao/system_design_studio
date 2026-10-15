# Command-line utilities

```json metadata
{
  "schema_version": 2,
  "title": "Command-line utilities",
  "description": "Reference for Redis Software command-line utilities, including rladmin, redis-cli, crdb-cli, and rlcheck.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"public-utilities","title":"Public utilities"},{"id":"internal-utilities","title":"Internal utilities"}]}

,
  "codeExamples": []
}
```


Redis Software includes a set of utilities to help you manage and test your cluster. To use a utility, run it from the command line.

## Public utilities

Administrators can use these CLI tools to manage and test a Redis Software cluster. You can find the binaries in the `/opt/redislabs/bin/` directory.


| Utility | Description |
| --- | --- |
| [crdb-cli (manage Active-Active)](https://redis.io/docs/latest/operate/rs/references/cli-utilities/crdb-cli/) | Manage Active-Active databases. |
| [redis-cli (run Redis commands)](https://redis.io/docs/latest/operate/rs/references/cli-utilities/redis-cli/) | Run Redis commands. |
| [rladmin (manage cluster)](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/) | Manage Redis Software clusters and databases. |
| [rlcheck (verify nodes)](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rlcheck/) | Verify nodes. |


## Internal utilities

The `/opt/redislabs/bin/` directory also contains utilities used internally by Redis Software and for troubleshooting.

> [!WARNING]
> Do not use these tools for normal operations.

| Utility | Description |
|---------|-------------|
| bdb-cli | `redis-cli` connected to a database. |
| ccs-cli | Inspect Cluster Configuration Store. |
| cnm_ctl | Manages services for provisioning, migration, monitoring, <br />resharding, rebalancing, deprovisioning, and autoscaling. |
| consistency_checker | Checks the consistency of Redis instances. |
| crdbtop | Monitor Active-Active databases. |
| debug_mode | Enables debug mode. |
| debuginfo | Collects cluster information. |
| dmc-cli | Configure and monitor the DMC proxy. |
| pdns_control | Sends commands to a running PowerDNS nameserver. |
| [rdb-cli](https://github.com/redis/librdb) | Parse and convert RDB files. |
| redis_ctl | Stops or starts Redis instances. |
| rl_rdbloader | Load RDB backup files to a server. |
| rlutil | Maintenance utility. |
| shard-cli | `redis-cli` connected to a shard. |
| supervisorctl | Manages the lifecycles of Redis Software services. |

