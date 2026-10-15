# Backup object

```json metadata
{
  "schema_version": 2,
  "title": "Backup object",
  "description": "Documents the backup object used with Redis Software REST API calls.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


| Name | Type/Value | Description |
|------|------------|-------------|
| progress  | number, (range: 0-100) | Shard backup progress (percentage) |
| status    | 'exporting'<br />'succeeded'<br />'failed' | Status of scheduled periodic backup process |

