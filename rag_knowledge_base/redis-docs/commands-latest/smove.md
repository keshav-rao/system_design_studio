# SMOVE

```json metadata
{
  "schema_version": 2,
  "title": "SMOVE",
  "description": "Moves a member from one set to another.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"source","key_spec_index":0,"name":"source","type":"key"},{"display_text":"destination","key_spec_index":1,"name":"destination","type":"key"},{"display_text":"member","name":"member","type":"string"}],
  "syntax_fmt": "SMOVE source destination member",
  "complexity": "O(1)",
  "group": "set",
  "command_flags": ["write","fast"],
  "acl_categories": ["@write","@set","@fast"],
  "since": "1.0.0",
  "arity": 4,
  "key_specs": [{"RW":true,"access":true,"begin_search":{"spec":{"index":1},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}},{"RW":true,"begin_search":{"spec":{"index":2},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"insert":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


Move `member` from the set at `source` to the set at `destination`.
This operation is atomic.
In every given moment the element will appear to be a member of `source` **or**
`destination` for other clients.

If the source set does not exist or does not contain the specified element, no
operation is performed and `0` is returned.
Otherwise, the element is removed from the source set and added to the
destination set.
When the specified element already exists in the destination set, it is only
removed from the source set.

## Required arguments

<details open><summary><code>source</code></summary>

The key of the source set.

</details>

<details open><summary><code>destination</code></summary>

The key of the destination set.

</details>

<details open><summary><code>member</code></summary>

The member to move from the source set to the destination set.

</details>

## Examples


redis> SADD myset "one"
(integer) 1
redis> SADD myset "two"
(integer) 1
redis> SADD myotherset "three"
(integer) 1
redis> SMOVE myset myotherset "two"
(integer) 1
redis> SMEMBERS myset
1) "one"
redis> SMEMBERS myotherset
1) "three"
2) "two"


## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `1` if the element is moved.
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` if the element is not a member of _source_ and no operation was performed.

**RESP3:**

One of the following:
* [Integer reply](../../develop/reference/protocol-spec#integers): `1` if the element is moved.
* [Integer reply](../../develop/reference/protocol-spec#integers): `0` if the element is not a member of _source_ and no operation was performed.



