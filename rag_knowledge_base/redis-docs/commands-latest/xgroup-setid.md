# XGROUP SETID

```json metadata
{
  "schema_version": 2,
  "title": "XGROUP SETID",
  "description": "Sets the last-delivered ID of a consumer group.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"group","name":"group","type":"string"},{"arguments":[{"display_text":"id","name":"id","type":"string"},{"display_text":"new-id","name":"new-id","token":"$","type":"pure-token"}],"name":"id-selector","type":"oneof"},{"display_text":"entries-read","name":"entriesread","optional":true,"token":"ENTRIESREAD","type":"integer"}],
  "syntax_fmt": "XGROUP SETID key group \u003cid | $\u003e [ENTRIESREAD entries-read]",
  "complexity": "O(1)",
  "group": "stream",
  "command_flags": ["write"],
  "acl_categories": ["@write","@stream","@slow"],
  "since": "5.0.0",
  "arity": -5,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":2},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Set the last delivered ID for a consumer group.

Normally, a consumer group's last delivered ID is set when the group is created with [`XGROUP CREATE`](https://redis.io/docs/latest/commands/xgroup-create).
The `XGROUP SETID` command allows modifying the group's last delivered ID, without having to delete and recreate the group.
For instance if you want the consumers in a consumer group to re-process all the messages in a stream, you may want to set its next ID to 0:

    XGROUP SETID mystream mygroup 0

The optional `entries_read` argument can be specified to enable consumer group lag tracking for an arbitrary ID.
An arbitrary ID is any ID that isn't the ID of the stream's first entry, its last entry or the zero (`0-0`) ID.
This can be useful you know exactly how many entries are between the arbitrary ID (excluding it) and the stream's last entry.
In such cases, the `entries_read` can be set to the stream's `entries_added` subtracted with the number of entries.

## Required arguments

<details open><summary><code>key</code></summary>

The stream key.

</details>

<details open><summary><code>group</code></summary>

The consumer group name.

</details>

<details open><summary><code>id | $</code></summary>

The ID to set as the group's last-delivered ID. Use `$` for the last message currently in the stream, or `0` to reset to the start.

</details>

## Optional arguments

<details open><summary><code>ENTRIESREAD entries-read</code></summary>

Set the group's entries-read counter, used to compute its lag.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



