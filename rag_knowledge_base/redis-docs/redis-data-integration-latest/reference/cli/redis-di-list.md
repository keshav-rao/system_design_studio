# redis-di list

```json metadata
{
  "schema_version": 2,
  "title": "redis-di list",
  "description": "Lists all pipelines",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Lists all pipelines with their status in a compact table.

## Usage

```
redis-di list [flags]
```

## Options

| Option           | Description                                          |
| :--------------- | :--------------------------------------------------- |
| `-o`, `--output` | Output format: `table` (default), `json`, or `yaml`. |

This command also accepts the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
redis-di list
redis-di list -o json
```

