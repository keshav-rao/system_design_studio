# redis-di list-secrets

```json metadata
{
  "schema_version": 2,
  "title": "redis-di list-secrets",
  "description": "Lists the secrets of a pipeline",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Lists the secrets of a pipeline. The API never returns secret values, so the output shows only the
secret keys and whether each one is set, not the stored values.

## Usage

```
redis-di list-secrets [flags]
```

## Options

| Option             | Description                                                         |
| :----------------- | :------------------------------------------------------------------ |
| `-p`, `--pipeline` | Pipeline to target (default `default`).                             |
| `--db`             | List only the secrets of this database: a source name, or `target`. |
| `-o`, `--output`   | Output format: `table` (default), `json`, or `yaml`.                |

This command also accepts the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
redis-di list-secrets
redis-di list-secrets --db mysql
redis-di list-secrets -p my-pipeline
```

