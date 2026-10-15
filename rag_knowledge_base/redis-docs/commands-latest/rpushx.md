# RPUSHX

```json metadata
{
  "schema_version": 2,
  "title": "RPUSHX",
  "description": "Appends an element to a list only when the list exists.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"element","multiple":true,"name":"element","type":"string"}],
  "syntax_fmt": "RPUSHX key element [element ...]",
  "complexity": "O(1) for each element added, so O(N) to add N elements when the command is called with multiple arguments.",
  "group": "list",
  "command_flags": ["write","denyoom","fast"],
  "acl_categories": ["@write","@list","@fast"],
  "since": "2.2.0",
  "arity": -3,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"insert":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Inserts specified values at the tail of the list stored at `key`, only if `key`
already exists and holds a list.
In contrary to [`RPUSH`](https://redis.io/docs/latest/commands/rpush), no operation will be performed when `key` does not yet
exist.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key that holds the list.

</details>

<details open><summary><code>element [element ...]</code></summary>

One or more values to append to the list, only if it already exists.

</details>

## Examples


redis> RPUSH mylist "Hello"
(integer) 1
redis> RPUSHX mylist "World"
(integer) 2
redis> RPUSHX myotherlist "World"
(integer) 0
redis> LRANGE mylist 0 -1
1) "Hello"
2) "World"
redis> LRANGE myotherlist 0 -1
(empty array)


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Integer reply](../../develop/reference/protocol-spec#integers): the length of the list after the push operation.

**RESP3:**

[Integer reply](../../develop/reference/protocol-spec#integers): the length of the list after the push operation.



