# redis-di delete

```json metadata
{
  "schema_version": 2,
  "title": "redis-di delete",
  "description": "Deleting a pipeline is not supported",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Deleting a pipeline is currently not supported, and the `redis-di delete` command is no longer
available.

To stop a pipeline and discard its configuration, deploy an empty configuration instead:

```bash
redis-di deploy --empty
```

See [Clear a pipeline](https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/deploy#clear-a-pipeline)
for what this removes and what it keeps, and
[`redis-di deploy`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di-deploy)
for the command's options.

