# redis-di describe-secret

```json metadata
{
  "schema_version": 2,
  "title": "redis-di describe-secret",
  "description": "Describes a secret of a pipeline",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Describes a single secret of a pipeline. The API never returns secret values, so the output shows
only the key and whether it is set, not the stored value.

## Usage

```
redis-di describe-secret <key> [flags]
```

## Options

| Option             | Description                                                 |
| :----------------- | :---------------------------------------------------------- |
| `-p`, `--pipeline` | Pipeline to target (default `default`).                     |
| `--db`             | Database the secret belongs to: a source name, or `target`. |

This command also accepts the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
redis-di describe-secret PASSWORD --db target
```

