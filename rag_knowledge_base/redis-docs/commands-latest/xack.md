# XACK

```json metadata
{
  "schema_version": 2,
  "title": "XACK",
  "description": "Returns the number of messages that were successfully acknowledged by the consumer group member of a stream.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"group","name":"group","type":"string"},{"display_text":"id","multiple":true,"name":"id","type":"string"}],
  "syntax_fmt": "XACK key group id [id ...]",
  "complexity": "O(1) for each message ID processed.",
  "group": "stream",
  "command_flags": ["write","fast"],
  "acl_categories": ["@write","@stream","@fast"],
  "since": "5.0.0",
  "arity": -4,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The `XACK` command removes one or multiple messages from the
*Pending Entries List* (PEL) of a stream consumer group. A message is pending,
and as such stored inside the PEL, when it was delivered to some consumer,
normally as a side effect of calling [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup), or when a consumer took
ownership of a message calling [`XCLAIM`](https://redis.io/docs/latest/commands/xclaim). The pending message was delivered to
some consumer but the server is yet not sure it was processed at least once.
So new calls to [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) to grab the messages history for a consumer
(for instance using an ID of 0), will return such message.
Similarly the pending message will be listed by the [`XPENDING`](https://redis.io/docs/latest/commands/xpending) command,
that inspects the PEL.

Once a consumer *successfully* processes a message, it should call `XACK`
so that such message does not get processed again, and as a side effect,
the PEL entry about this message is also purged, releasing memory from the
Redis server.

## Required arguments

<details open><summary><code>key</code></summary>

The stream key.

</details>

<details open><summary><code>group</code></summary>

The consumer group name.

</details>

<details open><summary><code>id [id ...]</code></summary>

One or more message IDs to acknowledge.

</details>

## Examples

```
redis> XACK mystream mygroup 1526569495631-0
(integer) 1
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): The command returns the number of messages successfully acknowledged. Certain message IDs may no longer be part of the PEL (for example because they have already been acknowledged), and XACK will not count them as successfully acknowledged.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): The command returns the number of messages successfully acknowledged. Certain message IDs may no longer be part of the PEL (for example because they have already been acknowledged), and XACK will not count them as successfully acknowledged.



