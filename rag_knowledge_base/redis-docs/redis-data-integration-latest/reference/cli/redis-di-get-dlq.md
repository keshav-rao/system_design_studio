# redis-di get-dlq

```json metadata
{
  "schema_version": 2,
  "title": "redis-di get-dlq",
  "description": "Gets a dead-letter queue of a pipeline",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Gets a single dead-letter queue (DLQ) of a pipeline and prints it in the compact `list-dlqs` table
format.

The name is the DLQ's source-qualified table name, `<source>.<qualified_table_name>`, as
reported by [`list-dlqs`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di-list-dlqs).

## Usage

```
redis-di get-dlq <name> [flags]
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
redis-di get-dlq mysql.inventory.customers
```

