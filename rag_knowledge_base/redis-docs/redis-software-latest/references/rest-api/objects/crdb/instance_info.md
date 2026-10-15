# CRDB instance info object

```json metadata
{
  "schema_version": 2,
  "title": "CRDB instance info object",
  "description": "An object that represents Active-Active instance info",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


An object that represents Active-Active instance info.

| Name | Type/Value | Description |
|------|------------|-------------|
| id | integer | Unique instance ID |
| cluster | [CRDB cluster_info](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/crdb/cluster_info) object | |
| compression | integer | Compression level when syncing from this source |
| db_config | [CRDB database_config](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/crdb/database_config) object | Database configuration for this specific instance. Use `db_config` only when you need to override or add configuration values that differ from the `default_db_config` in the main [CRDB object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/crdb). For a list of which settings must be identical across all instances and which to set per instance, see the [CRDB database config object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/crdb/database_config) reference. |
| db_uid | string | ID of local database instance. This field is likely to be empty for instances other than the local one. |

