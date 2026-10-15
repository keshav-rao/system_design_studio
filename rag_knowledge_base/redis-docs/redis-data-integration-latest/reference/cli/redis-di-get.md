# redis-di get

```json metadata
{
  "schema_version": 2,
  "title": "redis-di get",
  "description": "Gets a pipeline",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Gets a single pipeline and prints it in the compact `list` table format. Use
[`describe`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di-describe)
for the full pipeline view with its status and metrics.

## Usage

```
redis-di get [pipeline] [flags]
```

The pipeline name is an optional argument that defaults to `default`.

## Options

| Option           | Description                                          |
| :--------------- | :--------------------------------------------------- |
| `-o`, `--output` | Output format: `table` (default), `json`, or `yaml`. |

This command also accepts the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
redis-di get
redis-di get my-pipeline -o yaml
```

