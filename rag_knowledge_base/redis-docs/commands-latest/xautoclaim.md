# XAUTOCLAIM

```json metadata
{
  "schema_version": 2,
  "title": "XAUTOCLAIM",
  "description": "Changes, or acquires, ownership of messages in a consumer group, as if the messages were delivered to as consumer group member.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"group","name":"group","type":"string"},{"display_text":"consumer","name":"consumer","type":"string"},{"display_text":"min-idle-time","name":"min-idle-time","type":"string"},{"display_text":"start","name":"start","type":"string"},{"display_text":"count","name":"count","optional":true,"token":"COUNT","type":"integer"},{"display_text":"justid","name":"justid","optional":true,"token":"JUSTID","type":"pure-token"}],
  "syntax_fmt": "XAUTOCLAIM key group consumer min-idle-time start [COUNT count]\n  [JUSTID]",
  "complexity": "O(1) if COUNT is small.",
  "group": "stream",
  "command_flags": ["write","fast"],
  "acl_categories": ["@write","@stream","@fast"],
  "since": "6.2.0",
  "arity": -6,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

This command transfers ownership of pending stream entries that match the specified criteria. Conceptually, `XAUTOCLAIM`  is equivalent to calling [`XPENDING`](https://redis.io/docs/latest/commands/xpending) and then [`XCLAIM`](https://redis.io/docs/latest/commands/xclaim),
but provides a more straightforward way to deal with message delivery failures via [`SCAN`](https://redis.io/docs/latest/commands/scan)-like semantics.

Like [`XCLAIM`](https://redis.io/docs/latest/commands/xclaim), the command operates on the stream entries at `key` and in the context of the provided `group`.
It transfers ownership to `consumer` of messages pending for more than `min-idle-time` milliseconds and having an equal or greater ID than `start`.

The optional `count` argument, which defaults to 100, is the upper limit of the number of entries that the command attempts to claim.
Internally, the command begins scanning the consumer group's Pending Entries List (PEL) from `start` and filters out entries having an idle time less than or equal to `min-idle-time`.
The maximum number of pending entries that the command scans is the product of multiplying `count`'s value by 10 (hard-coded).
It is possible, therefore, that the number of entries claimed will be less than the specified value.

The optional `JUSTID` argument changes the reply to return just an array of IDs of messages successfully claimed, without returning the actual message.
Using this option means the retry counter is not incremented.

The command returns the claimed entries as an array. It also returns a stream ID intended for cursor-like use as the `start` argument for its subsequent call.
When there are no remaining PEL entries, the command returns the special `0-0` ID to signal completion.
However, note that you may want to continue calling `XAUTOCLAIM` even after the scan is complete with the `0-0` as `start` ID, because enough time passed, so older pending entries may now be eligible for claiming.

Note that only messages that are idle longer than `min-idle-time` are claimed, and claiming a message resets its idle time.
This ensures that only a single consumer can successfully claim a given pending message at a specific instant of time and trivially reduces the probability of processing the same message multiple times.

Messages that have been released back to the group using [`XNACK`](https://redis.io/docs/latest/commands/xnack) are immediately claimable since their delivery time is set to 0, satisfying any minimum idle time requirement.

While iterating the PEL, if `XAUTOCLAIM` stumbles upon a message which doesn't exist in the stream anymore (either trimmed or deleted by [`XDEL`](https://redis.io/docs/latest/commands/xdel)) it does not claim it, and deletes it from the PEL in which it was found. This feature was introduced in Redis 7.0.
These message IDs are returned to the caller as a part of `XAUTOCLAIM`s reply.

Lastly, claiming a message with `XAUTOCLAIM` also increments the attempted deliveries count for that message, unless the `JUSTID` option has been specified (which only delivers the message ID, not the message itself).
Messages that cannot be processed for some reason - for example, because consumers systematically crash when processing them - will exhibit high attempted delivery counts that can be detected by monitoring.

## Required arguments

<details open><summary><code>key</code></summary>

The stream key.

</details>

<details open><summary><code>group</code></summary>

The consumer group name.

</details>

<details open><summary><code>consumer</code></summary>

The name of the consumer that will own the claimed messages.

</details>

<details open><summary><code>min-idle-time</code></summary>

Claim only messages that have been idle for at least this long, in milliseconds.

</details>

<details open><summary><code>start</code></summary>

The message ID to start scanning from. Use `0` to start at the beginning of the PEL.

</details>

## Optional arguments

<details open><summary><code>COUNT count</code></summary>

The number of messages to attempt to claim per call. Defaults to 100.

</details>

<details open><summary><code>JUSTID</code></summary>

Return only the IDs of the claimed messages, without their fields, and do not increment their retry counters.

</details>

## Examples

```
> XAUTOCLAIM mystream mygroup Alice 3600000 0-0 COUNT 25
1) "0-0"
2) 1) 1) "1609338752495-0"
      2) 1) "field"
         2) "value"
3) (empty array)
```

In the previous example, you claim up to 25 pending entries that have been idle (having not been acknowledged or claimed) for at least one hour, starting from the beginning of the stream. The consumer Alice in the mygroup group takes ownership of these messages.

The returned stream ID is 0-0, which indicates that XAUTOCLAIM scanned the entire stream. The third reply element is an empty array, which means XAUTOCLAIM did not find any deleted messages.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays), specifically, an array with three elements:
1. A stream ID to be used as the _start_ argument for the next call to XAUTOCLAIM.
2. An [Array reply](../../develop/reference/protocol-spec#arrays) containing all the successfully claimed messages in the same format as `XRANGE`.
3. An [Array reply](../../develop/reference/protocol-spec#arrays) containing message IDs that no longer exist in the stream, and were deleted from the PEL in which they were found.

**RESP3:**

[Array reply](../../develop/reference/protocol-spec#arrays), specifically, an array with three elements:
1. A stream ID to be used as the _start_ argument for the next call to XAUTOCLAIM.
2. An [Array reply](../../develop/reference/protocol-spec#arrays) containing all the successfully claimed messages in the same format as `XRANGE`.
3. An [Array reply](../../develop/reference/protocol-spec#arrays) containing message IDs that no longer exist in the stream, and were deleted from the PEL in which they were found.



