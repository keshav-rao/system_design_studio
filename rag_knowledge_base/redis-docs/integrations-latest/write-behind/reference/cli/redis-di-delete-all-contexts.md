# redis-di delete-all-contexts

```json metadata
{
  "schema_version": 2,
  "title": "redis-di delete-all-contexts",
  "description": "Deletes all contexts",
  "categories": ["docs","integrate","rs","rdi"],
  "group": "di",
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"options","title":"Options"},{"id":"cli-help","title":"CLI help"}]}

,
  "codeExamples": []
}
```


## Usage

```
Usage: redis-di delete-all-contexts [OPTIONS]
```

## Options

- `loglevel`:

  - Type: Choice(['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'])
  - Default: `info`
  - Usage: `--loglevel
-log-level`

- `force`:

  - Type: BOOL
  - Default: `false`
  - Usage: `--force
-f`

  Force operation. skips verification prompts

- `help`:

  - Type: BOOL
  - Default: `false`
  - Usage: `--help`

  Show this message and exit.

## CLI help

```
Usage: redis-di delete-all-contexts [OPTIONS]

  Deletes all contexts

Options:
  -log-level, --loglevel [DEBUG|INFO|WARN|ERROR|CRITICAL]
                                  [default: INFO]
  -f, --force                     Force operation. skips verification prompts
  --help                          Show this message and exit.
```

