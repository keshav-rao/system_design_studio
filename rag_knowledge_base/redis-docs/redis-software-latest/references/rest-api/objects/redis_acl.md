# Redis ACL object

```json metadata
{
  "schema_version": 2,
  "title": "Redis ACL object",
  "description": "An object that represents a Redis access control list (ACL)",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


An API object that represents a Redis [access control list (ACL)](https://redis.io/docs/latest/operate/rs/security/access-control/create-db-roles)

| Name | Type/Value | Description |
|------|------------|-------------|
| uid | integer | Object's unique ID |
| account_id | integer | SM account ID |
| acl | string | Redis ACL's string |
| action_uid | string | Action UID. If it exists, progress can be tracked by the `GET`&nbsp;`/actions/{uid}` API (read-only) |
| name | string | Redis ACL's name |
| min_version | string | Minimum database version that supports this ACL. Read only |
| max_version | string | Maximum database version that supports this ACL. Read only |


