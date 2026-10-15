# redis-di stop

```json metadata
{
  "schema_version": 2,
  "title": "redis-di stop",
  "description": "Stops a pipeline",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Stops a pipeline. By default, the command waits for the pipeline to reach the `stopped` state before
returning.

## Usage

```
redis-di stop [pipeline] [flags]
```

The pipeline name is an optional argument that defaults to `default`.

## Options

| Option      | Description                                                                       |
| :---------- | :-------------------------------------------------------------------------------- |
| `--source`  | Target only this source instead of the whole pipeline.                            |
| `--wait`    | Wait for the pipeline to reach the expected state (default `true`).               |
| `--timeout` | Maximum time to wait for the pipeline to reach the expected state (default `2m`). |

This command also accepts the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
redis-di stop

# Stop only source mysql
redis-di stop --source mysql
```

