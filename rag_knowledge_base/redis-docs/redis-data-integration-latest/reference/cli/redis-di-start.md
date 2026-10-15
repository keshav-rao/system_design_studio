# redis-di start

```json metadata
{
  "schema_version": 2,
  "title": "redis-di start",
  "description": "Starts a pipeline",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Starts a pipeline. By default, the command waits for the pipeline to reach the `started` state before
returning.

## Usage

```
redis-di start [pipeline] [flags]
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
redis-di start
redis-di start my-pipeline --wait=false

# Start only source mysql. Does not start the pipeline if it's currently stopped.
redis-di start --source mysql
```

