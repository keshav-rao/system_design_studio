# redis-di get-job

```json metadata
{
  "schema_version": 2,
  "title": "redis-di get-job",
  "description": "Gets a job of a pipeline",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Gets a single job of a pipeline and prints it in the compact `list-jobs` table format. Use
[`describe-job`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di-describe-job)
for the full job view with its transformations and outputs.

## Usage

```
redis-di get-job <name> [flags]
```

## Options

| Option             | Description                                          |
| :----------------- | :--------------------------------------------------- |
| `-p`, `--pipeline` | Pipeline to target (default `default`).              |
| `-o`, `--output`   | Output format: `table` (default), `json`, or `yaml`. |

This command also accepts the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
redis-di get-job customers_hash_job
```

