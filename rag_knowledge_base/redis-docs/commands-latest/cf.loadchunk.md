# CF.LOADCHUNK

```json metadata
{
  "schema_version": 2,
  "title": "CF.LOADCHUNK",
  "description": "Restores a filter previously saved using SCANDUMP",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"key","type":"key"},{"name":"iterator","type":"integer"},{"name":"data","type":"string"}],
  "syntax_fmt": "CF.LOADCHUNK key iterator data",
  "complexity": "O(n), where n is the capacity",
  "group": "cf",
  "acl_categories": ["@cuckoo","@write","@slow"],
  "since": "1.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Restores a cuckoo filter previously saved using [`CF.SCANDUMP`](https://redis.io/docs/latest/commands/cf.scandump).

See the [`CF.SCANDUMP`](https://redis.io/docs/latest/commands/cf.scandump) command for example usage.

<note><b>Notes</b>

- This command overwrites the cuckoo filter stored under `key`.
- Make sure that the cuckoo filter is not changed between invocations.

</note>

## Required arguments

<details open><summary><code>key</code></summary>

is key name for a cuckoo filter to restore.
</details>

<details open><summary><code>iterator</code></summary>

Iterator value associated with `data` (returned by [`CF.SCANDUMP`](https://redis.io/docs/latest/commands/cf.scandump))
</details>

<details open><summary><code>data</code></summary>

Current data chunk (returned by [`CF.SCANDUMP`](https://redis.io/docs/latest/commands/cf.scandump))
</details>

## Examples

See [`CF.SCANDUMP`](https://redis.io/docs/latest/commands/cf.scandump) for an example.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, wrong key type, or when invalid data was passed.

**RESP3:**

One of the following:
* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings): `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: invalid arguments, wrong key type, or when invalid data was passed.



