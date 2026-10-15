# redis-di delete-secret

```json metadata
{
  "schema_version": 2,
  "title": "redis-di delete-secret",
  "description": "Deletes a secret of a pipeline",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Deletes a secret of a pipeline. Because this is destructive, the command asks for confirmation unless
you pass `--force`.

## Usage

```
redis-di delete-secret <key> [flags]
```

## Options

| Option             | Description                                                                       |
| :----------------- | :-------------------------------------------------------------------------------- |
| `-p`, `--pipeline` | Pipeline to target (default `default`).                                           |
| `--db`             | Database the secret belongs to: a source name, or `target`.                       |
| `--force`          | Skip the confirmation prompt.                                                     |
| `--wait`           | Wait for the pipeline to reach the expected state (default `true`).               |
| `--timeout`        | Maximum time to wait for the pipeline to reach the expected state (default `2m`). |

This command also accepts the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
redis-di delete-secret CACERT --db mysql --force
```

