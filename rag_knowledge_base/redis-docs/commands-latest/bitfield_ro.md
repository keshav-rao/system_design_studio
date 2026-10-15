# BITFIELD_RO

```json metadata
{
  "schema_version": 2,
  "title": "BITFIELD_RO",
  "description": "Performs arbitrary read-only bitfield integer operations on strings.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"arguments":[{"display_text":"encoding","name":"encoding","type":"string"},{"display_text":"offset","name":"offset","type":"integer"}],"multiple":true,"multiple_token":true,"name":"get-block","optional":true,"token":"GET","type":"block"}],
  "syntax_fmt": "BITFIELD_RO key [GET encoding offset [GET encoding offset ...]]",
  "complexity": "O(1) for each subcommand specified",
  "group": "bitmap",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@bitmap","@fast"],
  "since": "6.0.0",
  "arity": -2,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Read-only variant of the [`BITFIELD`](https://redis.io/docs/latest/commands/bitfield) command.
It is like the original [`BITFIELD`](https://redis.io/docs/latest/commands/bitfield) but only accepts `GET` subcommand and can safely be used in read-only replicas.

Since the original [`BITFIELD`](https://redis.io/docs/latest/commands/bitfield) has `SET` and `INCRBY` options it is technically flagged as a writing command in the Redis command table.
For this reason read-only replicas in a Redis Cluster will redirect it to the master instance even if the connection is in read-only mode (see the [`READONLY`](https://redis.io/docs/latest/commands/readonly) command of Redis Cluster).

Since Redis 6.2, the `BITFIELD_RO` variant was introduced in order to allow [`BITFIELD`](https://redis.io/docs/latest/commands/bitfield) behavior in read-only replicas without breaking compatibility on command flags.

See original [`BITFIELD`](https://redis.io/docs/latest/commands/bitfield) for more details.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the string.

</details>

## Optional arguments

<details open><summary><code>GET encoding offset</code></summary>

Return the value at `offset`, interpreted with `encoding` (for example `u8` or `i16`). May be given multiple times.

</details>

## Examples

```
BITFIELD_RO hello GET i8 16
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): each entry being the corresponding result of the sub-command given at the same position.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): each entry being the corresponding result of the sub-command given at the same position.



