# PFDEBUG

```json metadata
{
  "schema_version": 2,
  "title": "PFDEBUG",
  "description": "Internal commands for debugging HyperLogLog values.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"subcommand","name":"subcommand","type":"string"},{"display_text":"key","key_spec_index":0,"name":"key","type":"key"}],
  "syntax_fmt": "PFDEBUG subcommand key",
  "complexity": "N/A",
  "group": "hyperloglog",
  "command_flags": ["write","denyoom","admin"],
  "acl_categories": ["@write","@hyperloglog","@admin","@slow","@dangerous"],
  "since": "2.8.9",
  "arity": 3,
  "key_specs": [{"RW":true,"access":true,"begin_search":{"spec":{"index":2},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"}]}

,
  "codeExamples": []
}
```

The `PFDEBUG` command is an internal command.
It is meant to be used for developing and testing Redis.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

