# rladmin cluster

```json metadata
{
  "schema_version": 2,
  "title": "rladmin cluster",
  "description": "Manage cluster.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"commands-for-configured-clusters","title":"Commands for configured clusters"},{"id":"commands-for-non-configured-clusters","title":"Commands for non-configured clusters"}]}

,
  "codeExamples": []
}
```


Manages cluster configuration and administration. Most `rladmin cluster` commands are only for clusters that are already configured, while a few others are only for new clusters that have not been configured.

## Commands for configured clusters


| Command | Description |
| --- | --- |
| [certificate](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/certificate/) | Sets cluster certificates. |
| [change_password_hashing_algorithm](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/change_password_hashing_algorithm/) | Changes the password hashing algorithm. |
| [config](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/config/) | Updates the cluster's configuration. |
| [debug_info](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/debug_info/) | Creates a support package. |
| [master](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/master/) | Identifies or changes the cluster's master node. |
| [ocsp](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/ocsp/) | Manages OCSP. |
| [reset_password](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/reset_password/) | Changes the password for a given email. |
| [running_actions](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/running_actions/) | Lists all active tasks. |
| [stats_archiver](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/stats_archiver/) | Enables/deactivates the stats archiver. |


## Commands for non-configured clusters


| Command | Description |
| --- | --- |
| [create](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/create/) | Creates a new cluster. |
| [join](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/join/) | Adds a node to an existing cluster. |
| [recover](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/recover/) | Recovers a cluster from a backup file. |


