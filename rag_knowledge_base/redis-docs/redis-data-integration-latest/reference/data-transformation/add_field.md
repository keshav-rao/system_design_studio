# add_field

```json metadata
{
  "schema_version": 2,
  "title": "add_field",
  "description": "Add fields to a record",
  "categories": ["docs","integrate","rs","rdi"],
  "group": "di",
  "tableOfContents": {"sections":[{"id":"option-1-fields-array","title":"Option 1: fields[]: array"}]}

,
  "codeExamples": []
}
```


Add fields to a record

**Option 1 (alternative):**
Add multiple fields

**Properties**

| Name                         | Type       | Description | Required |
| ---------------------------- | ---------- | ----------- | -------- |
| [**fields**](#option1fields) | `object[]` | Fields<br/> | yes      |

**Additional Properties:** not allowed

**Example**

```yaml
source:
  schema: dbo
  table: emp
transform:
  - uses: add_field
    with:
      fields:
        - field: name.full_name
          language: jmespath
          expression: concat([name.fname, ' ', name.lname])
        - field: name.fname_upper
          language: jmespath
          expression: upper(name.fname)
```

**Option 2 (alternative):**
Add one field

**Properties**

| Name           | Type     | Description                                                                                                                                                                                           | Required |
| -------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| **field**      | `string` | Field<br/>                                                                                                                                                                                            | yes      |
| **expression** | `string` | Expression<br/>                                                                                                                                                                                       | yes      |
| **language**   | `string` | Language<br/>Enum: `"jmespath"`, `"sql"`<br/>                                                                                                                                                         | yes      |
| **cache**      | `object` | Cache the result of the field expression. See [`cache`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/cache) for the property list. **Flink processor only.**<br/> | no       |

**Additional Properties:** not allowed

**Example**

```yaml
source:
  schema: dbo
  table: emp
transform:
  - uses: add_field
    with:
      field: country
      language: sql
      expression: country_code || ' - ' || UPPER(country_name)
```

<a name="option1fields"></a>

## Option 1: fields\[\]: array

Fields

**Items**

**Item Properties**

| Name           | Type     | Description                                                                                                                                                                                           | Required |
| -------------- | -------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| **field**      | `string` | Field<br/>                                                                                                                                                                                            | yes      |
| **expression** | `string` | Expression<br/>                                                                                                                                                                                       | yes      |
| **language**   | `string` | Language<br/>Enum: `"jmespath"`, `"sql"`<br/>                                                                                                                                                         | yes      |
| **cache**      | `object` | Cache the result of the field expression. See [`cache`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/data-transformation/cache) for the property list. **Flink processor only.**<br/> | no       |

**Item Additional Properties:** not allowed

**Example**

```yaml
- {}
```

