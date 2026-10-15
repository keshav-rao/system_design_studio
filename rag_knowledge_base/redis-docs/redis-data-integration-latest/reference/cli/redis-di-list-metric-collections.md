# redis-di list-metric-collections

```json metadata
{
  "schema_version": 2,
  "title": "redis-di list-metric-collections",
  "description": "Lists the metric collections of a pipeline",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Lists the metric collections of a pipeline. Metric collections hold the raw component metrics that
the [`describe`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di-describe)
command summarizes in its Statistics and Performance sections. This command is most useful with
`-o json` or `-o yaml` for scripting and for tools such as `jq`.

## Usage

```
redis-di list-metric-collections [flags]
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
redis-di list-metric-collections
```

