# BRPOPLPUSH

```json metadata
{
  "schema_version": 2,
  "title": "BRPOPLPUSH",
  "description": "Pops an element from a list, pushes it to another list and returns it. Block until an element is available otherwise. Deletes the list if the last element was popped.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"source","key_spec_index":0,"name":"source","type":"key"},{"display_text":"destination","key_spec_index":1,"name":"destination","type":"key"},{"display_text":"timeout","name":"timeout","type":"double"}],
  "syntax_fmt": "BRPOPLPUSH source destination timeout",
  "complexity": "O(1)",
  "group": "list",
  "command_flags": ["write","denyoom","blocking"],
  "acl_categories": ["@write","@list","@slow","@blocking"],
  "since": "2.2.0",
  "arity": 4,
  "key_specs": [{"RW":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}},{"RW":true,"begin_search":{"spec":{"index":2},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"insert":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"children":[{"id":"pattern-reliable-queue","title":"Pattern: reliable queue"},{"id":"pattern-circular-list","title":"Pattern: circular list"}],"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


`BRPOPLPUSH` is the blocking variant of [`RPOPLPUSH`](https://redis.io/docs/latest/commands/rpoplpush).
When `source` contains elements, this command behaves exactly like [`RPOPLPUSH`](https://redis.io/docs/latest/commands/rpoplpush).
When used inside a [`MULTI`](https://redis.io/docs/latest/commands/multi)/[`EXEC`](https://redis.io/docs/latest/commands/exec) block or a Lua script, this command behaves exactly like [`RPOPLPUSH`](https://redis.io/docs/latest/commands/rpoplpush).
When `source` is empty, Redis will block the connection until another client
pushes to it or until `timeout` is reached.
A `timeout` of zero can be used to block indefinitely.

See [`RPOPLPUSH`](https://redis.io/docs/latest/commands/rpoplpush) for more information.

## Required arguments

<details open><summary><code>source</code></summary>

The key of the source list.

</details>

<details open><summary><code>destination</code></summary>

The key of the destination list.

</details>

<details open><summary><code>timeout</code></summary>

The maximum time to block, in seconds. A timeout of `0` blocks indefinitely.

</details>

## Details

### Pattern: reliable queue

Please see the pattern description in the [`RPOPLPUSH`](https://redis.io/docs/latest/commands/rpoplpush) documentation.

### Pattern: circular list

Please see the pattern description in the [`RPOPLPUSH`](https://redis.io/docs/latest/commands/rpoplpush) documentation.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Deprecated as of Redis v6.2.0. |

## Return information

**RESP2:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the element being popped from _source_ and pushed to _destination_.
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): the timeout is reached.

**RESP3:**

One of the following:
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the element being popped from _source_ and pushed to _destination_.
* [Null reply](../../develop/reference/protocol-spec#nulls): the timeout is reached.



