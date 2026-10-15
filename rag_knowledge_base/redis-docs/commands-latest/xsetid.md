# XSETID

```json metadata
{
  "schema_version": 2,
  "title": "XSETID",
  "description": "An internal command for replicating stream values.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"display_text":"last-id","name":"last-id","type":"string"},{"display_text":"entries-added","name":"entries-added","optional":true,"since":"7.0.0","token":"ENTRIESADDED","type":"integer"},{"display_text":"max-deleted-id","name":"max-deleted-id","optional":true,"since":"7.0.0","token":"MAXDELETEDID","type":"string"}],
  "syntax_fmt": "XSETID key last-id [ENTRIESADDED entries-added]\n  [MAXDELETEDID max-deleted-id]",
  "complexity": "O(1)",
  "group": "stream",
  "command_flags": ["write","denyoom","fast"],
  "acl_categories": ["@write","@stream","@fast"],
  "since": "5.0.0",
  "arity": -3,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

 `XSETID` is an internal command. Users should not call it directly.
 
Redis primary shards use it to replicate the last delivered entry ID of the stream.

## Required arguments

<details open><summary><code>key</code></summary>

The stream key.

</details>

<details open><summary><code>last-id</code></summary>

The ID to set as the stream's last-generated ID.

</details>

## Optional arguments

<details open><summary><code>ENTRIESADDED entries-added</code></summary>

Set the stream's entries-added counter.

</details>

<details open><summary><code>MAXDELETEDID max-deleted-id</code></summary>

Set the stream's maximum deleted entry ID.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.



