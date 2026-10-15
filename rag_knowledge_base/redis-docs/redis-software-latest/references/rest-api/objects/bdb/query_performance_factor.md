# Query performance factor object

```json metadata
{
  "schema_version": 2,
  "title": "Query performance factor object",
  "description": "Configuration object for query performance factor",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Configures [query performance factor](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/search/query-performance-factor) and related fields.

| Field | Type/Value | Description |
|-------|------------|-------------|
| active | boolean (default: false) | If true, enables query performance factor for the database |
| scaling_factor | integer (range: 0-16) (default: 0) | Scales the magnitude of the query performance factor |


