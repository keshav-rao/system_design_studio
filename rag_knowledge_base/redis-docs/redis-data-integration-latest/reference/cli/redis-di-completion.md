# redis-di completion

```json metadata
{
  "schema_version": 2,
  "title": "redis-di completion",
  "description": "Generates a shell autocompletion script",
  "categories": ["redis-di"],
  "tableOfContents": {"sections":[{"id":"usage","title":"Usage"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


Generates an autocompletion script for `redis-di` for the specified shell. Supported shells are
`bash`, `zsh`, `fish`, and `powershell`.

## Usage

```
redis-di completion [bash|zsh|fish|powershell]
```

Run `redis-di completion <shell> --help` for the per-shell installation instructions.

## Example

To load completions into the current `bash` session:

```bash
source <(redis-di completion bash)
```

