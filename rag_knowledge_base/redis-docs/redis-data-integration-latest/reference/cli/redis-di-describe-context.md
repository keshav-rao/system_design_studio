# redis-di describe-context

```json metadata
{
  "schema_version": 2,
  "title": "redis-di describe-context",
  "description": "Describes a context",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Describes a single context from the `~/.redis-di` context file, showing its API connection details.
See the [CLI reference overview](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli#contexts)
for more about contexts.

## Usage

```
redis-di describe-context <name> [flags]
```

## Options

This command takes only the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
redis-di describe-context prod
```

