# LINSERT

```json metadata
{
  "schema_version": 2,
  "title": "LINSERT",
  "description": "Inserts an element before or after another element in a list.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"arguments":[{"display_text":"before","name":"before","token":"BEFORE","type":"pure-token"},{"display_text":"after","name":"after","token":"AFTER","type":"pure-token"}],"name":"where","type":"oneof"},{"display_text":"pivot","name":"pivot","type":"string"},{"display_text":"element","name":"element","type":"string"}],
  "syntax_fmt": "LINSERT key \u003cBEFORE | AFTER\u003e pivot element",
  "complexity": "O(N) where N is the number of elements to traverse before seeing the value pivot. This means that inserting somewhere on the left end on the list (head) can be considered O(1) and inserting somewhere on the right end (tail) is O(N).",
  "group": "list",
  "command_flags": ["write","denyoom"],
  "acl_categories": ["@write","@list","@slow"],
  "since": "2.2.0",
  "arity": 5,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"insert":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Inserts `element` in the list stored at `key` either before or after the reference
value `pivot`.

When `key` does not exist, it is considered an empty list and no operation is
performed.

An error is returned when `key` exists but does not hold a list value.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the list.

</details>

<details open><summary><code>BEFORE | AFTER</code></summary>

Whether to insert `element` before or after `pivot`.

</details>

<details open><summary><code>pivot</code></summary>

The existing element to insert relative to.

</details>

<details open><summary><code>element</code></summary>

The value to insert.

</details>

## Examples


redis> RPUSH mylist "Hello"
(integer) 1
redis> RPUSH mylist "World"
(integer) 2
redis> LINSERT mylist BEFORE "World" "There"
(integer) 3
redis> LRANGE mylist 0 -1
1) "Hello"
2) "There"
3) "World"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): the list length after a successful insert operation.
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` when the key doesn't exist.
* [Integer reply](../../develop/reference/protocol-spec#integers): `-1` when the pivot wasn't found.

**RESP3:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): the list length after a successful insert operation.
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` when the key doesn't exist.
* [Integer reply](../../develop/reference/protocol-spec#integers): `-1` when the pivot wasn't found.



