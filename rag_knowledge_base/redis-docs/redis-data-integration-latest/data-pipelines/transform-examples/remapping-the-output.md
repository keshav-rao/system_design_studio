# Remapping the fields in the output

```json metadata
{
  "schema_version": 2,
  "title": "Remapping the fields in the output",
  "description": "",
  "categories": ["docs","integrate","rs","rdi"],
  "group": "di",
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Sometimes, you may want to remap the fields in the output of a data pipeline. You can do this by defining a `mapping` section in the output configuration.

```yaml
name: Remap customer fields
source:
  table: Customer

output:
  - uses: redis.write
    with:
      data_type: hash
      mapping:
        - CustomerId: id
        - FirstName: first_name
        - LastName: last_name
```

The example above remaps the `CustomerId` field to `id`, `FirstName` to `first_name`, and `LastName` to `last_name` in the output. This allows you to customize the field names in the Redis data store according to your application's requirements.
You can also use `mapping` to include only the fields you need in the output and exclude the rest.

Mapping only allows you to rename fields and limit the output to specific fields and define a single level structure. To create nested structures and/or perform operations on the field values you can use the [map transformation](https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/transform-examples/map-example).

