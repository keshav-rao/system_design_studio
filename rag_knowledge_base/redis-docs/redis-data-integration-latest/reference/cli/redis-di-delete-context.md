# redis-di delete-context

```json metadata
{
  "schema_version": 2,
  "title": "redis-di delete-context",
  "description": "Deletes a context",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Deletes a context from the `~/.redis-di` context file. Because this is destructive, the command asks
for confirmation unless you pass `--force`.

## Usage

```
redis-di delete-context <name> [flags]
```

## Options

| Option    | Description                   |
| :-------- | :---------------------------- |
| `--force` | Skip the confirmation prompt. |

This command also accepts the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
redis-di delete-context dev --force
```

