# filter

```json metadata
{
  "schema_version": 2,
  "title": "filter",
  "description": "Filter records",
  "categories": ["docs","integrate","rs","rdi"],
  "group": "di",
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Filter records

**Properties**

| Name           | Type     | Description                                                                                                                                                                                            | Required |
| -------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------- |
| **expression** | `string` | Expression<br/>                                                                                                                                                                                        | yes      |
| **language**   | `string` | Language<br/>Enum: `"jmespath"`, `"sql"`<br/>                                                                                                                                                          | yes      |
| **cache**      | `object` | Cache the result of the filter expression. See [`cache`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/cache) for the property list. **Flink processor only.**<br/> | no       |

**Additional Properties:** not allowed

**Example**

```yaml
source:
  schema: dbo
  table: emp
transform:
  - uses: filter
    with:
      language: sql
      expression: age>20
```

