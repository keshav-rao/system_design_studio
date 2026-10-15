# redis-di get-secret

```json metadata
{
  "schema_version": 2,
  "title": "redis-di get-secret",
  "description": "Gets a secret of a pipeline",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Gets a single secret of a pipeline and prints it in the compact `list-secrets` table format. The API
never returns secret values, so the output shows only the key and whether it is set, not the stored
value.

## Usage

```
redis-di get-secret <key> [flags]
```

## Options

| Option             | Description                                                 |
| :----------------- | :---------------------------------------------------------- |
| `-p`, `--pipeline` | Pipeline to target (default `default`).                     |
| `--db`             | Database the secret belongs to: a source name, or `target`. |
| `-o`, `--output`   | Output format: `table` (default), `json`, or `yaml`.        |

This command also accepts the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
redis-di get-secret USERNAME --db mysql
```

