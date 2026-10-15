# XINFO CONSUMERS

```json metadata
{
  "schema_version": 2,
  "title": "XINFO CONSUMERS",
  "description": "Returns a list of the consumers in a consumer group.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"group","name":"group","type":"string"}],
  "syntax_fmt": "XINFO CONSUMERS key group",
  "complexity": "O(1)",
  "group": "stream",
  "command_flags": ["readonly"],
  "acl_categories": ["@read","@stream","@slow"],
  "since": "5.0.0",
  "arity": 4,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":2},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

This command returns the list of consumers that belong to the `groupname` consumer group of the stream stored at `key`.

The following information is provided for each consumer in the group:

* **name**: the consumer's name
* **pending**: the number of entries in the PEL: pending messages for the consumer, which are messages that were delivered but are yet to be acknowledged
* **idle**: the number of milliseconds that have passed since the consumer's last attempted interaction (Examples: [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup), [`XCLAIM`](https://redis.io/docs/latest/commands/xclaim), [`XAUTOCLAIM`](https://redis.io/docs/latest/commands/xautoclaim))
* **inactive**: the number of milliseconds that have passed since the consumer's last successful interaction (Examples: [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) that actually read some entries into the PEL, [`XCLAIM`](https://redis.io/docs/latest/commands/xclaim)/[`XAUTOCLAIM`](https://redis.io/docs/latest/commands/xautoclaim) that actually claimed some entries)

Note that before Redis 7.2.0, **idle** used to denote the time passed since last successful interaction.
In 7.2.0, **inactive** was added and **idle** was changed to denote the time passed since last attempted interaction.

## Required arguments

<details open><summary><code>key</code></summary>

The stream key.

</details>

<details open><summary><code>group</code></summary>

The consumer group name.

</details>

## Examples

```
> XINFO CONSUMERS mystream mygroup
1) 1) name
   2) "Alice"
   3) pending
   4) (integer) 1
   5) idle
   6) (integer) 9104628
   7) inactive
   8) (integer) 18104698
2) 1) name
   2) "Bob"
   3) pending
   4) (integer) 1
   5) idle
   6) (integer) 83841983
   7) inactive
   8) (integer) 993841998
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of consumers and their attributes.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of consumers and their attributes.



