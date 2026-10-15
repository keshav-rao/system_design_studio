# LREM

```json metadata
{
  "schema_version": 2,
  "title": "LREM",
  "description": "Removes elements from a list. Deletes the list if the last element was removed.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"count","name":"count","type":"integer"},{"display_text":"element","name":"element","type":"string"}],
  "syntax_fmt": "LREM key count element",
  "complexity": "O(N+M) where N is the length of the list and M is the number of elements removed.",
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

Removes the first `count` occurrences of elements equal to `element` from the list
stored at `key`.
The `count` argument influences the operation in the following ways:

* `count > 0`: Remove elements equal to `element` moving from head to tail.
* `count < 0`: Remove elements equal to `element` moving from tail to head.
* `count = 0`: Remove all elements equal to `element`.

For example, `LREM list -2 "hello"` will remove the last two occurrences of
`"hello"` in the list stored at `key`.

Note that non-existing keys are treated like empty lists, so when `key` does not
exist, the command will always return `0`.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the list.

</details>

<details open><summary><code>count</code></summary>

The number of matching elements to remove and the direction: a positive value removes from the head, a negative value from the tail, and `0` removes all matches.

</details>

<details open><summary><code>element</code></summary>

The value to remove.

</details>

## Examples


redis> RPUSH mylist "hello"
(integer) 1
redis> RPUSH mylist "hello"
(integer) 2
redis> RPUSH mylist "foo"
(integer) 3
redis> RPUSH mylist "hello"
(integer) 4
redis> LREM mylist -2 "hello"
(integer) 2
redis> LRANGE mylist 0 -1
1) "hello"
2) "foo"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of removed elements.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the number of removed elements.



