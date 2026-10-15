# redis-di get-metric-collection

```json metadata
{
  "schema_version": 2,
  "title": "redis-di get-metric-collection",
  "description": "Gets a metric collection of a pipeline",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Gets a single metric collection of a pipeline, returning its raw metric data. This command is most
useful with `-o json` or `-o yaml` for scripting and for tools such as `jq`. Use
[`list-metric-collections`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di-list-metric-collections)
to see the available collections.

## Usage

```
redis-di get-metric-collection <name> [flags]
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
redis-di get-metric-collection processor_metrics -o json
redis-di get-metric-collection collector-mysql_metrics -o json
```

