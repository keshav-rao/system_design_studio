# COPY

```json metadata
{
  "schema_version": 2,
  "title": "COPY",
  "description": "Copies the value of a key to a new key.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"source","key_spec_index":0,"name":"source","type":"key"},{"display_text":"destination","key_spec_index":1,"name":"destination","type":"key"},{"display_text":"destination-db","name":"destination-db","optional":true,"token":"DB","type":"integer"},{"display_text":"replace","name":"replace","optional":true,"token":"REPLACE","type":"pure-token"}],
  "syntax_fmt": "COPY source destination [DB destination-db] [REPLACE]",
  "complexity": "O(N) worst case for collections, where N is the number of nested items. O(1) for string values.",
  "group": "generic",
  "command_flags": ["write","denyoom"],
  "acl_categories": ["@keyspace","@write","@slow"],
  "since": "6.2.0",
  "arity": -3,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}},{"OW":true,"begin_search":{"spec":{"index":2},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


This command copies the value stored at the `source` key to the `destination`
key.

By default, the `destination` key is created in the logical database used by the
connection. The `DB` option allows specifying an alternative logical database
index for the destination key.

The command returns zero when the `destination` key already exists. The
`REPLACE` option removes the `destination` key before copying the value to it.

## Required arguments

<details open><summary><code>source</code></summary>

The key to copy from.

</details>

<details open><summary><code>destination</code></summary>

The key to copy to.

</details>

## Optional arguments

<details open><summary><code>DB destination-db</code></summary>

Copy the key to the given database index instead of the current one.

</details>

<details open><summary><code>REPLACE</code></summary>

Replace the destination key if it already exists.

</details>

## Examples

```
SET dolly "sheep"
COPY dolly clone
GET clone
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active\*</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active\*</nobr></span> | For Active-Active or clustered databases, the source and destination keys must be in the same hash slot.<br /><br />\*Not supported for stream consumer group info. |

## Return information

**RESP2:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `1` if _source_ was copied.
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` if _source_ was not copied.

**RESP3:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `1` if _source_ was copied.
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` if _source_ was not copied.



