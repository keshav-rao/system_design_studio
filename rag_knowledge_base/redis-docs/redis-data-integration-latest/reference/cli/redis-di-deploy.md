# redis-di deploy

```json metadata
{
  "schema_version": 2,
  "title": "redis-di deploy",
  "description": "Deploys a pipeline with the specified configuration",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Deploys a pipeline, creating it or updating it from the configuration in the `--dir` directory. The
API validates the configuration and rejects an invalid one. By default, the command starts the
pipeline after deploying and waits for it to reach the expected state. `set` is an alias for this
command.

Pass `--empty` instead of `--dir` to deploy an empty configuration, which clears the pipeline. See
[Clear a pipeline](https://redis.io/docs/latest/integrate/redis-data-integration/data-pipelines/deploy#clear-a-pipeline) for
what clearing a pipeline removes and what it keeps.

## Usage

```
redis-di deploy [pipeline] [flags]
```

The pipeline name is an optional argument that defaults to `default`.

## Options

| Option              | Description                                                                          |
| :------------------ | :----------------------------------------------------------------------------------- |
| `--dir`             | Directory containing the pipeline configuration (default `.`).                       |
| `--empty`           | Deploy an empty configuration instead of loading one from a directory. Cannot be combined with `--dir`. |
| `--dry-run`         | Validate the configuration without deploying.                                        |
| `--validate-tables` | Validate the configuration against the source and target databases (default `true`). |
| `--validate-cdc`    | Validate the CDC configuration of the source databases.                              |
| `--start`           | Start the pipeline after deploying (default `true`, or `false` with `--empty`).      |
| `--wait`            | Wait for the pipeline to reach the expected state (default `true`).                  |
| `--timeout`         | Maximum time to wait for the pipeline to reach the expected state (default `2m`).    |

This command also accepts the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
# Deploy the configuration in the current directory
redis-di deploy

# Validate a configuration folder without deploying it
redis-di deploy --dir /opt/rdi/config --dry-run

# Clear the pipeline by deploying an empty configuration
redis-di deploy --empty
```

