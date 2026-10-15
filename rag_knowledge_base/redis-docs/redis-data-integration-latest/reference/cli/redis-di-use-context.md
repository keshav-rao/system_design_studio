# redis-di use-context

```json metadata
{
  "schema_version": 2,
  "title": "redis-di use-context",
  "description": "Sets a context to be the active one",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Sets a context in the `~/.redis-di` context file to be the active one, so its connection details are
used by subsequent commands. Create or update a context with
[`set-context`](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di-set-context).

## Usage

```
redis-di use-context <name> [flags]
```

## Options

This command takes only the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
redis-di use-context prod
```

