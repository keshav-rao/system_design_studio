# redis-di describe-job

```json metadata
{
  "schema_version": 2,
  "title": "redis-di describe-job",
  "description": "Describes a job of a pipeline",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Describes a single job of a pipeline, printing its source properties followed by tables that
summarize its transformations and outputs.

## Usage

```
redis-di describe-job <name> [flags]
```

## Options

| Option             | Description                             |
| :----------------- | :-------------------------------------- |
| `-p`, `--pipeline` | Pipeline to target (default `default`). |

This command also accepts the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
redis-di describe-job customers_hash_job
```

