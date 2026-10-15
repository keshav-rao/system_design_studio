# Check result object

```json metadata
{
  "schema_version": 2,
  "title": "Check result object",
  "description": "An object that contains the results of a cluster check",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Cluster check result

| Name | Type/Value | Description |
|------|------------|-------------|
| cluster_test_result | boolean | Indication if any of the tests failed |
| nodes | 
[{
  "node_uid": integer,
  "result": boolean,
  "error": string
}, ...]
 | Nodes results |

