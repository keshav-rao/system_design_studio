# HOTKEYS HELP

```json metadata
{
  "schema_version": 2,
  "title": "HOTKEYS HELP",
  "description": "Returns helpful text about HOTKEYS commands and parameters.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "HOTKEYS HELP",
  "complexity": "O(1)",
  "group": "server",
  "command_flags": ["loading","stale"],
  "acl_categories": ["@admin"],
  "since": "8.6.1",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```


Returns helpful text about `HOTKEYS` commands and parameters.

## Return information

**RESP2:**

Returns an [array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) with the list of `HOTKEYS` subcommands and their descriptions.

**RESP3:**

Returns an [array reply](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays) with the list of `HOTKEYS` subcommands and their descriptions.



