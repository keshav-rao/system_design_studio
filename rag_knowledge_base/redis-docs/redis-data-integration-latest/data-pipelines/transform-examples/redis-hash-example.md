# Write to a Redis hash

```json metadata
{
  "schema_version": 2,
  "title": "Write to a Redis hash",
  "description": "",
  "categories": ["docs","integrate","rs","rdi"],
  "group": "di",
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


In the following example, the data is captured from the source table named `invoice` and is written to the Redis database as hash keys. The `connection` is an optional parameter that refers to the corresponding connection name defined in `config.yaml`. 
When you specify the `data_type` parameter for the job, it overrides the system-wide setting `target_data_type` defined in `config.yaml`. 

In this case, the result will be Redis hashes with key names based on the key expression (for example, `invoice_id:1`) and with an expiration of 100 seconds.
If you don't supply an `expire` parameter, the keys will never expire. 

```yaml
name: Write invoice to hash
source:
  schema: public
  table: invoice
output:
  - uses: redis.write
    with:
      connection: target
      data_type: hash
      key:
        expression: concat(['invoice_id:', InvoiceId])
        language: jmespath
      expire: 100
```

