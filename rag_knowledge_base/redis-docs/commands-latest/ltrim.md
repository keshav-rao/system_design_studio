# LTRIM

```json metadata
{
  "schema_version": 2,
  "title": "LTRIM",
  "description": "Removes elements from both ends a list. Deletes the list if all elements were trimmed.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"start","name":"start","type":"integer"},{"display_text":"stop","name":"stop","type":"integer"}],
  "syntax_fmt": "LTRIM key start stop",
  "complexity": "O(N) where N is the number of elements to be removed by the operation.",
  "group": "list",
  "command_flags": ["write"],
  "acl_categories": ["@write","@list","@slow"],
  "since": "1.0.0",
  "arity": 4,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Trim an existing list so that it will contain only the specified range of
elements specified.
Both `start` and `stop` are zero-based indexes, where `0` is the first element
of the list (the head), `1` the next element, and so on.

For example: `LTRIM foobar 0 2` will modify the list stored at `foobar` so that
only the first three elements of the list will remain.

`start` and `stop` can also be negative numbers indicating offsets from the end
of the list, where `-1` is the last element of the list, `-2` the penultimate
element, and so on.

Out of range indexes will not produce an error: if `start` is larger than the
end of the list (`start > stop`), the result will be an empty list, which
causes `key` to be removed.
If `stop` is larger than the end of the list (`stop > start`), Redis will treat it like the last
element of the list.


## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the list.

</details>

<details open><summary><code>start</code></summary>

The zero-based start index. Negative indexes count from the tail.

</details>

<details open><summary><code>stop</code></summary>

The zero-based stop index (inclusive). Negative indexes count from the tail.

</details>

## Examples

A common use of `LTRIM` is to use it with [`LPUSH`](https://redis.io/docs/latest/commands/lpush) or [`RPUSH`](https://redis.io/docs/latest/commands/rpush).
For example:

```
LPUSH mylist someelement
LTRIM mylist 0 99
```

This pair of commands will push a new element on the list, while making sure
that the list will not grow larger than 100 elements.
This is very useful when using Redis to store logs for example.
It is important to note that when used in this way `LTRIM` is an O(1) operation
because in the average case just one element is removed from the tail of the
list.



redis> RPUSH mylist "one"
(integer) 1
redis> RPUSH mylist "two"
(integer) 2
redis> RPUSH mylist "three"
(integer) 3
redis> LTRIM mylist 1 -1
OK
redis> LRANGE mylist 0 -1
1) "two"
2) "three"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



