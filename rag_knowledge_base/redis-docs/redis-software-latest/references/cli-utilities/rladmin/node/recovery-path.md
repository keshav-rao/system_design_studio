# rladmin node recovery_path set

```json metadata
{
  "schema_version": 2,
  "title": "rladmin node recovery_path set",
  "description": "Sets a node's local recovery path.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Sets the node's local recovery path, which specifies the directory where [persistence files](https://redis.io/docs/latest/operate/rs/databases/configure/database-persistence) are stored. You can use these persistence files to [recover a failed database](https://redis.io/docs/latest/operate/rs/databases/recover).

```sh
rladmin node <ID> recovery_path set <path>
```

### Parameters

| Parameter | Type/Value                     | Description                                                                                   |
|-----------|--------------------------------|-----------------------------------------------------------------------------------------------|
| node      | integer                        | Sets the recovery path for the specified node                                            |
| path      | filepath                       | Path to the folder where persistence files are stored                                         |

### Returns

Returns `Updated successfully` if the recovery path was set. Otherwise, it returns an error.

### Example

```sh
$ rladmin node 2 recovery_path set /var/opt/redislabs/persist/redis
Updated successfully.
```

