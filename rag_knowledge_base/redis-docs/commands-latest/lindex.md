# LINDEX

```json metadata
{
  "schema_version": 2,
  "title": "LINDEX",
  "description": "Returns an element from a list by its index.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"index","name":"index","type":"integer"}],
  "syntax_fmt": "LINDEX key index",
  "complexity": "O(N) where N is the number of elements to traverse to get to the element at index. This makes asking for the first or the last element of the list O(1).",
  "group": "list",
  "command_flags": ["readonly"],
  "acl_categories": ["@read","@list","@slow"],
  "since": "1.0.0",
  "arity": 3,
  "key_specs": [{"RO":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Returns the element at index `index` in the list stored at `key`.
The index is zero-based, so `0` means the first element, `1` the second element
and so on.
Negative indices can be used to designate elements starting at the tail of the
list.
Here, `-1` means the last element, `-2` means the penultimate and so forth.

When the value at `key` is not a list, an error is returned.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the list.

</details>

<details open><summary><code>index</code></summary>

The zero-based index of the element to return. Negative indexes count from the tail (`-1` is the last element).

</details>

## Examples


redis> LPUSH mylist "World"
(integer) 1
redis> LPUSH mylist "Hello"
(integer) 2
redis> LINDEX mylist 0
"Hello"
redis> LINDEX mylist -1
"World"
redis> LINDEX mylist 3
(nil)


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Nil reply](../../develop/reference/protocol-spec#bulk-strings): when _index_ is out of range.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the requested element.

**RESP3:**

One of the following:
* [Null reply](../../develop/reference/protocol-spec#nulls): when _index_ is out of range.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): the requested element.



