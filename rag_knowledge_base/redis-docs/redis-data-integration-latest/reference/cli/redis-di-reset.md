# redis-di reset

```json metadata
{
  "schema_version": 2,
  "title": "redis-di reset",
  "description": "Resets a pipeline",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Resets a pipeline into initial full-sync mode, so it reloads a snapshot of the source data before
resuming change data capture. By default, the command waits for the pipeline to reach a terminal
state before returning.

With `--source`, only the specified source is reset. See
[Start, stop, and reset a single source](https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/multiple-sources#start-stop-and-reset-a-single-source) for more information.

## Usage

```
redis-di reset [pipeline] [flags]
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
redis-di reset

# Reset only source mysql
redis-di reset --source mysql
```

