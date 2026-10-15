# BLMPOP

```json metadata
{
  "schema_version": 2,
  "title": "BLMPOP",
  "description": "Pops the first element from one of multiple lists. Blocks until an element is available otherwise. Deletes the list if the last element was popped.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"timeout","name":"timeout","type":"double"},{"display_text":"numkeys","name":"numkeys","type":"integer"},{"display_text":"key","key_spec_index":0,"multiple":true,"name":"key","type":"key"},{"arguments":[{"display_text":"left","name":"left","token":"LEFT","type":"pure-token"},{"display_text":"right","name":"right","token":"RIGHT","type":"pure-token"}],"name":"where","type":"oneof"},{"display_text":"count","name":"count","optional":true,"token":"COUNT","type":"integer"}],
  "syntax_fmt": "BLMPOP timeout numkeys key [key ...] \u003cLEFT | RIGHT\u003e [COUNT count]",
  "complexity": "O(N+M) where N is the number of provided keys and M is the number of elements returned.",
  "group": "list",
  "command_flags": ["write","blocking","movablekeys"],
  "acl_categories": ["@write","@list","@slow","@blocking"],
  "since": "7.0.0",
  "arity": -5,
  "key_specs": [{"RW":true,"access":true,"begin_search":{"spec":{"index":2},"type":"index"},"delete":true,"find_keys":{"spec":{"firstkey":1,"keynumidx":0,"keystep":1},"type":"keynum"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


`BLMPOP` is the blocking variant of [`LMPOP`](https://redis.io/docs/latest/commands/lmpop).

When any of the lists contains elements, this command behaves exactly like [`LMPOP`](https://redis.io/docs/latest/commands/lmpop).
When used inside a [`MULTI`](https://redis.io/docs/latest/commands/multi)/[`EXEC`](https://redis.io/docs/latest/commands/exec) block or a Lua script, this command behaves exactly like [`LMPOP`](https://redis.io/docs/latest/commands/lmpop).
When all lists are empty, Redis will block the connection until another client pushes to it or until the `timeout` (a double value specifying the maximum number of seconds to block) elapses.
A `timeout` of zero can be used to block indefinitely.

See [`LMPOP`](https://redis.io/docs/latest/commands/lmpop) for more information.

## Required arguments

<details open><summary><code>timeout</code></summary>

The maximum time to block, in seconds. A timeout of `0` blocks indefinitely.

</details>

<details open><summary><code>numkeys</code></summary>

The number of keys that follow.

</details>

<details open><summary><code>key [key ...]</code></summary>

One or more keys of lists to operate on.

</details>

<details open><summary><code>LEFT | RIGHT</code></summary>

The end of the list to pop elements from: `LEFT` (head) or `RIGHT` (tail).

</details>

## Optional arguments

<details open><summary><code>COUNT count</code></summary>

The number of elements to pop. Defaults to 1.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): when no element could be popped and the _timeout_ is reached.
* [Array reply](../../develop/reference/protocol-spec#arrays): a two-element array with the first element being the name of the key from which elements were popped, and the second element being an array of the popped elements.

**RESP3:**

One of the following:
* [Null reply](../../develop/reference/protocol-spec#nulls): when no element could be popped and the _timeout_ is reached.
* [Array reply](../../develop/reference/protocol-spec#arrays): a two-element array with the first element being the name of the key from which elements were popped, and the second element being an array of the popped elements.



