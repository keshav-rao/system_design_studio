# Role object

```json metadata
{
  "schema_version": 2,
  "title": "Role object",
  "description": "An object that represents a role",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


An API object that represents a role.

| Name | Type/Value | Description |
|------|------------|-------------|
| uid | integer | Role's unique ID |
| account_id | integer | SM account ID |
| action_uid | string | Action UID. If it exists, progress can be tracked by the GET /actions/{uid} API (read-only) |
| management | 'admin'<br />'db_member'<br />'db_viewer'<br />'cluster_member'<br />'cluster_viewer'<br />'user_manager'<br />'none' | [Management role](https://redis.io/docs/latest/operate/rs/references/rest-api/permissions#roles) |
| name | string | Role's name |
| resources | array of objects | Optional list of resource scopes that limit a `db_member` or `db_viewer` management role to specific databases. Each scope has a `type` (currently only `db`) and a `uids` array of database IDs the role applies to. If omitted or empty, the role applies to all databases. Example: `[{"type": "db", "uids": ["1", "2"]}]` |

