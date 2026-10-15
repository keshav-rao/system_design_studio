# Logrotate settings object

```json metadata
{
  "schema_version": 2,
  "title": "Logrotate settings object",
  "description": "Documents the logrotate_settings object used with Redis Software REST API calls.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


| Name | Type/Value | Description |
|------|------------|-------------|
| maxage | integer (default: 7) | Remove rotated logs older than the specified number of days |
| maxsize | string (default: 200M) | The log will rotate after it reaches the specified size |
| rotate | integer (default: 10) | Determines how many times the log will be rotated. If set to 0, old versions are removed rather than rotated. |
