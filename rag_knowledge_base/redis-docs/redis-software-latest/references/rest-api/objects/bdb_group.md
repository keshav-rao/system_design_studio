# BDB group object

```json metadata
{
  "schema_version": 2,
  "title": "BDB group object",
  "description": "An object that represents a group of databases with a shared memory pool",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


An API object that represents a group of databases that share a memory pool.

| Name | Type/Value | Description |
|------|------------|-------------|
| uid          | integer          | Cluster unique ID of the database group |
| members      | array of strings | A list of UIDs of member databases (read-only) |
| memory_size  | integer          | The common memory pool size limit for all databases in the group, expressed in bytes |

