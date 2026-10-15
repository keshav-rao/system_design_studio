# COMMAND GETKEYSANDFLAGS

```json metadata
{
  "schema_version": 2,
  "title": "COMMAND GETKEYSANDFLAGS",
  "description": "Extracts the key names and access flags for an arbitrary command.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"command","name":"command","type":"string"},{"display_text":"arg","multiple":true,"name":"arg","optional":true,"type":"string"}],
  "syntax_fmt": "COMMAND GETKEYSANDFLAGS command [arg [arg ...]]",
  "complexity": "O(N) where N is the number of arguments to the command",
  "group": "server",
  "command_flags": ["loading","stale"],
  "acl_categories": ["@slow","@connection"],
  "since": "7.0.0",
  "arity": -3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```


`COMMAND GETKEYSANDFLAGS` is a helper command to let you find the keys from a full Redis `command`, together with flags that indicate what each key is used for.

[COMMAND](https://redis.io/docs/latest/commands/command) describes how Redis identifies key names for each command, including `firstkey`, [key specifications](https://redis.io/docs/latest/develop/reference/key-specs#logical-operation-flags), and `movablekeys`. For some commands, Redis can identify the keys only by parsing the full command. Use [COMMAND GETKEYS](https://redis.io/docs/latest/commands/command-getkeys) or COMMAND GETKEYSANDFLAGS to get key names directly from the Redis command parser.

Refer to [key specifications](https://redis.io/docs/latest/develop/reference/key-specs#logical-operation-flags) for information about the meaning of the key flags.

## Required arguments

<details open><summary><code>command</code></summary>

The name of the command to analyze.

</details>

## Optional arguments

<details open><summary><code>arg [arg ...]</code></summary>

The arguments that would be passed to the command.

</details>

## Examples


redis> COMMAND GETKEYS MSET a b c d e f
1) "a"
2) "c"
3) "e"
redis> COMMAND GETKEYS EVAL "not consulted" 3 key1 key2 key3 arg1 arg2 arg3 argN
1) "key1"
2) "key2"
3) "key3"
redis> COMMAND GETKEYSANDFLAGS LMOVE mylist1 mylist2 left left
1) 1) "mylist1"
   2) 1) RW
      2) access
      3) delete
2) 1) "mylist2"
   2) 1) RW
      2) insert


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of keys from the given command and their usage flags.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of keys from the given command and their usage flags.



