# redis-di list-jobs

```json metadata
{
  "schema_version": 2,
  "title": "redis-di list-jobs",
  "description": "Lists the jobs of a pipeline",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Lists the jobs of a pipeline, one row per job with its source, its transformation and output counts,
and the target connections of its outputs. Use
[`describe-job`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di-describe-job)
for the full view of a single job.

## Usage

```
redis-di list-jobs [flags]
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
redis-di list-jobs
```

