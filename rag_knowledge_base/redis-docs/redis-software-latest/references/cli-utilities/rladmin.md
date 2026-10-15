# rladmin

```json metadata
{
  "schema_version": 2,
  "title": "rladmin",
  "description": "Manage Redis Software clusters and databases.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"rladmin-commands","title":"rladmin commands"},{"id":"use-the-rladmin-shell","title":"Use the rladmin shell"}]}

,
  "codeExamples": []
}
```


`rladmin` is a command-line utility that lets you perform administrative tasks such as failover, migration, and endpoint binding on a Redis Software cluster. You can also use `rladmin` to edit cluster and database configurations.

Although you can use the Cluster Manager UI for some of these tasks, others are unique to the `rladmin` command-line tool.

## `rladmin` commands


| Command | Description |
| --- | --- |
| [bind](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/bind/) | Manages the proxy policy for a specified database endpoint. |
| [cluster](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/) | Manage cluster. |
| [failover](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/failover/) | Fail over primary shards of a database to their replicas. |
| [help](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/help/) | Shows available commands or specific command usage. |
| [info](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/info/) | Shows the current configuration of a cluster, database, node, or proxy. |
| [metrics](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/metrics/) | Configures the metrics stream engine and manages local metrics storage. |
| [migrate](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/migrate/) | Moves Redis Software shards or endpoints to a new node in the same cluster. |
| [node](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/node/) | Manage nodes. |
| [placement](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/placement/) | Configures the shard placement policy for a database. |
| [recover](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/recover/) | Recovers databases in recovery mode. |
| [restart](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/restart/) | Restarts Redis Software processes for a specific database. |
| [status](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/status/) | Displays the current cluster status and topology information. |
| [suffix](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/suffix/) | Manages the DNS suffixes in the cluster. |
| [tune](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/tune/) | Configures parameters for databases, proxies, nodes, and clusters. |
| [upgrade](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/upgrade/) | Upgrades a database's Redis version and modules. |
| [verify](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/verify/) | Prints verification reports for the cluster. |


## Use the `rladmin` shell

To open the `rladmin` shell:

1. Sign in to a Redis Software node with an account that is a member of the **redislabs** group.

    The `rladmin` binary is located in `/opt/redislabs/bin`. If you don't have this directory in your `PATH`, you may want to add it. Otherwise, you can use `bash -l <username>` to sign in as a user with permissions for that directory.

1. Run: `rladmin`

    > [!NOTE]
    > If the CLI does not recognize the `rladmin` command,
    > run this command to load the necessary configuration first: <nobr>`bash -l`</nobr>

In the `rladmin` shell, you can:

- Run any `rladmin` command without prefacing it with `rladmin`.
- Enter `?` to view the full list of available commands.
- Enter [`help`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/help) followed by the name of a command for a detailed explanation of the command and its usage.
- Press the `Tab` key for command completion.
- Enter `exit` or press `Control+D` to exit the `rladmin` shell and return to the terminal prompt.

