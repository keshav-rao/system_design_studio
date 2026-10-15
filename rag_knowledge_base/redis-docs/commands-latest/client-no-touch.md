# CLIENT NO-TOUCH

```json metadata
{
  "schema_version": 2,
  "title": "CLIENT NO-TOUCH",
  "description": "Controls whether commands sent by the client affect the LRU/LFU of accessed keys.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"arguments":[{"display_text":"on","name":"on","token":"ON","type":"pure-token"},{"display_text":"off","name":"off","token":"OFF","type":"pure-token"}],"name":"enabled","type":"oneof"}],
  "syntax_fmt": "CLIENT NO-TOUCH \u003cON | OFF\u003e",
  "complexity": "O(1)",
  "group": "connection",
  "command_flags": ["noscript","loading","stale"],
  "acl_categories": ["@slow","@connection"],
  "since": "7.2.0",
  "arity": 3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `CLIENT NO-TOUCH` command controls whether commands sent by the client will alter the LRU/LFU of the keys they access.

When turned on, the current client will not change LFU/LRU stats, unless it sends the [`TOUCH`](https://redis.io/docs/latest/commands/touch) command.

When turned off, the client touches LFU/LRU stats just as a normal client.

## Required arguments

<details open><summary><code>ON | OFF</code></summary>

Turn off (`ON`) or on (`OFF`) updates to keys' last-access time and LFU counter for commands issued by this connection.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` if the command was successful.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: wrong number of or invalid arguments.

**RESP3:**

One of the following:

* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` if the command was successful.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: wrong number of or invalid arguments.



