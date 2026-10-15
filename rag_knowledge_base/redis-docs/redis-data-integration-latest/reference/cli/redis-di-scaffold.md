# redis-di scaffold

```json metadata
{
  "schema_version": 2,
  "title": "redis-di scaffold",
  "description": "Generates pipeline configuration files",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Generates a starter pipeline configuration for the given source database type. With `--dir`, the
command writes a `config.yaml` file and a `jobs/job.yaml` file into that directory, prompting
before overwriting existing files unless `--force` is set. Without `--dir`, it prints the
configuration to standard output.

## Usage

```
redis-di scaffold [flags]
```

## Options

| Option          | Description                                                                                                                     |
| :-------------- | :------------------------------------------------------------------------------------------------------------------------------ |
| `--db-type`     | Source database type (required): `mariadb`, `mongodb`, `mysql`, `oracle`, `postgresql`, `snowflake`, `sqlserver`, or `spanner`. |
| `--db-flavor`   | Source database flavor: `mongodb-atlas`, `mongodb-replica-set`, or `mongodb-sharded-cluster`.                                   |
| `--source-name` | Name of the generated source; defaults to the database type.                                                                    |
| `--dir`         | Directory to write the configuration and job files to; prints the configuration to standard output when omitted.                |
| `--force`       | Skip the confirmation prompt when overwriting an existing file.                                                                 |

This command also accepts the
[global options](https://redis.io/docs/latest/integrate/redis-data-integration/reference/cli/redis-di#global-options).

## Example

```bash
# Print a PostgreSQL configuration to stdout
redis-di scaffold --db-type postgresql

# Write a MySQL configuration into a directory
redis-di scaffold --db-type mysql --dir /opt/rdi/config

# Name the generated source 'inventory' instead of 'mysql'
redis-di scaffold --db-type mysql --source-name inventory --dir /opt/rdi/config
```

