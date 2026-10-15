# XPENDING

```json metadata
{
  "schema_version": 2,
  "title": "XPENDING",
  "description": "Returns the information and entries from a stream consumer group's pending entries list.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"group","name":"group","type":"string"},{"arguments":[{"display_text":"min-idle-time","name":"min-idle-time","optional":true,"since":"6.2.0","token":"IDLE","type":"integer"},{"display_text":"start","name":"start","type":"string"},{"display_text":"end","name":"end","type":"string"},{"display_text":"count","name":"count","type":"integer"},{"display_text":"consumer","name":"consumer","optional":true,"type":"string"}],"name":"filters","optional":true,"type":"block"}],
  "syntax_fmt": "XPENDING key group [[IDLE min-idle-time] start end count [consumer]]",
  "complexity": "O(N) with N being the number of elements returned, so asking for a small fixed number of entries per call is O(1). O(M), where M is the total number of entries scanned when used with the IDLE filter. When the command returns just the summary and the list of consumers is small, it runs in O(1) time; otherwise, an additional O(N) time for iterating every consumer.",
  "group": "stream",
  "command_flags": ["readonly"],
  "acl_categories": ["@read","@stream","@slow"],
  "since": "5.0.0",
  "arity": -3,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"children":[{"id":"summary-form-of-xpending","title":"Summary form of XPENDING"},{"id":"extended-form-of-xpending","title":"Extended form of XPENDING"},{"id":"idle-time-filter","title":"Idle time filter"},{"id":"exclusive-ranges-and-iterating-the-pel","title":"Exclusive ranges and iterating the PEL"}],"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Fetching data from a stream via a consumer group, and not acknowledging
such data, has the effect of creating *pending entries*. This is
well explained in the [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) command, and even better in our
[introduction to Redis Streams](https://redis.io/docs/latest/develop/data-types/streams). The [`XACK`](https://redis.io/docs/latest/commands/xack) command
will immediately remove the pending entry from the Pending Entries List (PEL)
since once a message is successfully processed, there is no longer need
for the consumer group to track it and to remember the current owner
of the message.

The `XPENDING` command is the interface to inspect the list of pending
messages, and is as thus a very important command in order to observe
and understand what is happening with a streams consumer groups: what
clients are active, what messages are pending to be consumed, or to see
if there are idle messages. Moreover this command, together with [`XCLAIM`](https://redis.io/docs/latest/commands/xclaim)
is used in order to implement recovering of consumers that are failing
for a long time, and as a result certain messages are not processed: a
different consumer can claim the message and continue. This is better
explained in the [streams intro](https://redis.io/docs/latest/develop/data-types/streams) and in the
[`XCLAIM`](https://redis.io/docs/latest/commands/xclaim) command page, and is not covered here.

## Required arguments

<details open><summary><code>key</code></summary>

The stream key.

</details>

<details open><summary><code>group</code></summary>

The consumer group name.

</details>

## Optional arguments

With no optional arguments, `XPENDING` returns a summary. Providing `start`, `end`, and `count` returns the extended (detailed) form.

<details open><summary><code>IDLE min-idle-time</code></summary>

Filter to messages that have been idle for at least this long, in milliseconds.

</details>

<details open><summary><code>start</code></summary>

The start of the ID range to inspect, inclusive. Use `-` for the smallest ID.

</details>

<details open><summary><code>end</code></summary>

The end of the ID range to inspect, inclusive. Use `+` for the greatest ID.

</details>

<details open><summary><code>count</code></summary>

The maximum number of messages to return.

</details>

<details open><summary><code>consumer</code></summary>

Filter to messages owned by the given consumer.

</details>

## Details

### Summary form of XPENDING

When `XPENDING` is called with just a key name and a consumer group
name, it just outputs a summary about the pending messages in a given
consumer group. In the following example, we create a consumer group and
immediately create a pending message by reading from the group with
[`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup).

```
> XGROUP CREATE mystream group55 0-0
OK

> XREADGROUP GROUP group55 consumer-123 COUNT 1 STREAMS mystream >
1) 1) "mystream"
   2) 1) 1) 1526984818136-0
         2) 1) "duration"
            2) "1532"
            3) "event-id"
            4) "5"
            5) "user-id"
            6) "7782813"
```

We expect the pending entries list for the consumer group `group55` to
have a message right now: consumer named `consumer-123` fetched the
message without acknowledging its processing. The simple `XPENDING`
form will give us this information:

```
> XPENDING mystream group55
1) (integer) 1
2) 1526984818136-0
3) 1526984818136-0
4) 1) 1) "consumer-123"
      2) "1"
```

In this form, the command outputs the total number of pending messages for this
consumer group, which is one, followed by the smallest and greatest ID among the
pending messages, and then list every consumer in the consumer group with
at least one pending message, and the number of pending messages it has.

### Extended form of XPENDING

The summary provides a good overview, but sometimes we are interested in the
details. In order to see all the pending messages with more associated
information we need to also pass a range of IDs, in a similar way we do it with
[`XRANGE`](https://redis.io/docs/latest/commands/xrange), and a non optional *count* argument, to limit the number
of messages returned per call:

```
> XPENDING mystream group55 - + 10
1) 1) 1526984818136-0
   2) "consumer-123"
   3) (integer) 196415
   4) (integer) 1
```

In the extended form we no longer see the summary information, instead there
is detailed information for each message in the pending entries list. For
each message four attributes are returned:

1. The ID of the message.
2. The name of the consumer that fetched the message and has still to acknowledge it. We call it the current *owner* of the message. For messages that have been released back to the group using [`XNACK`](https://redis.io/docs/latest/commands/xnack), this field will be an empty string.
3. The number of milliseconds that elapsed since the last time this message was delivered to this consumer.
4. The number of times this message was delivered.

The deliveries counter, that is the fourth element in the array, is incremented
when some other consumer *claims* the message with [`XCLAIM`](https://redis.io/docs/latest/commands/xclaim), or when the
message is delivered again via [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup), when accessing the history
of a consumer in a consumer group (see the [`XREADGROUP`](https://redis.io/docs/latest/commands/xreadgroup) page for more info).

It is possible to pass an additional argument to the command, in order
to see the messages having a specific owner:

```
> XPENDING mystream group55 - + 10 consumer-123
```

But in the above case the output would be the same, since we have pending
messages only for a single consumer. However what is important to keep in
mind is that this operation, filtering by a specific consumer, is not
inefficient even when there are many pending messages from many consumers:
we have a pending entries list data structure both globally, and for
every consumer, so we can very efficiently show just messages pending for
a single consumer.

### Idle time filter

It is also possible to filter pending stream entries by their idle-time,
given in milliseconds (useful for [`XCLAIM`](https://redis.io/docs/latest/commands/xclaim)ing entries that have not been
processed for some time):

```
> XPENDING mystream group55 IDLE 9000 - + 10
> XPENDING mystream group55 IDLE 9000 - + 10 consumer-123
```

The first case will return the first 10 (or less) PEL entries of the entire group
that are idle for over 9 seconds, whereas in the second case only those of
`consumer-123`.

### Exclusive ranges and iterating the PEL

The `XPENDING` command allows iterating over the pending entries just like
[`XRANGE`](https://redis.io/docs/latest/commands/xrange) and [`XREVRANGE`](https://redis.io/docs/latest/commands/xrevrange) allow for the stream's entries. You can do this by
prefixing the ID of the last-read pending entry with the `(` character that
denotes an open (exclusive) range, and proving it to the subsequent call to the
command.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

* [Array reply](../../develop/reference/protocol-spec#arrays): different data depending on the way XPENDING is called, as explained on this page.

**RESP3:**

* [Array reply](../../develop/reference/protocol-spec#arrays): different data depending on the way XPENDING is called, as explained on this page.



