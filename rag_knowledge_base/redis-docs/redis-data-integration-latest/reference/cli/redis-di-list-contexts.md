# redis-di list-contexts

```json metadata
{
  "schema_version": 2,
  "title": "redis-di list-contexts",
  "description": "Lists all contexts",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Lists all contexts from the `~/.redis-di` context file and indicates which one is active. See the
[CLI reference overview](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli#contexts)
for more about contexts.

## Usage

```
redis-di list-contexts [flags]
```

## Options

This command takes only the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
redis-di list-contexts
```

