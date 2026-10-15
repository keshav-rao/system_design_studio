# Cluster identity object

```json metadata
{
  "schema_version": 2,
  "title": "Cluster identity object",
  "description": "Documents the cluster_identity object used with Redis Software REST API calls.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


| Name | Type/Value | Description |
|------|------------|-------------|
| name          | string                | Fully qualified cluster name. Limited to 64 characters and must comply with the IETF's RFC 952 standard and section 2.1 of the RFC 1123 standard. |
| nodes         | array of strings       | Array of IP addresses of existing cluster nodes |
| wait_command  | boolean (default:&nbsp;true) | Supports Redis wait command |

