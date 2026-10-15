# Sync object

```json metadata
{
  "schema_version": 2,
  "title": "Sync object",
  "description": "Documents the sync object used with Redis Software REST API calls.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


| Name | Type/Value | Description |
|------|------------|-------------|
| progress  | integer        | Number of bytes remaining in current sync |
| status    | 'in_progress'<br />'idle'<br />'link_down' | Indication of the shard's current sync status |

