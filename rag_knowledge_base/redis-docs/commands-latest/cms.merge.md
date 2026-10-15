# CMS.MERGE

```json metadata
{
  "schema_version": 2,
  "title": "CMS.MERGE",
  "description": "Merges several sketches into one sketch",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"name":"destination","type":"key"},{"name":"numKeys","type":"integer"},{"multiple":true,"name":"source","type":"key"},{"arguments":[{"name":"weights","token":"WEIGHTS","type":"pure-token"},{"multiple":true,"name":"weight","type":"double"}],"name":"weight","optional":true,"type":"block"}],
  "syntax_fmt": "CMS.MERGE destination numKeys source [source ...] [WEIGHTS weight\n  [weight ...]]",
  "complexity": "O(n) where n is the number of sketches",
  "group": "cms",
  "acl_categories": ["@cms","@write"],
  "since": "2.0.0",
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

> [!NOTE]
> This command's behavior varies in clustered Redis environments. See the [multi-key operations](https://redis.io/docs/latest/develop/using-commands/multi-key-operations) page for more information.


Merges several sketches into one sketch. All sketches must have identical width and depth. Weights can be used to multiply certain sketches. Default weight is 1. 

## Required arguments

<details open><summary><code>destination</code></summary>

The name of the destination sketch. Must be initialized.

</details>

<details open><summary><code>numKeys</code></summary>

Number of sketches to be merged.

</details>

<details open><summary><code>source [source ...]</code></summary>

Names of source sketches to be merged.

</details>

## Optional arguments

<details open><summary><code>WEIGHTS weight [weight ...]</code></summary>

Multiple of each sketch. Default is 1.

</details>

## Examples

```
redis> CMS.MERGE dest 2 test1 test2 WEIGHTS 1 3
OK
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Supported</span><br /> | <span title="Supported">&#x2705; Flexible & Annual</span><br /><span title="Supported">&#x2705; Free & Fixed</nobr></span> |  |

## Return information

**RESP2:**

One of the following:

* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: non-existent key or destination key is not of the same width and/or depth.

**RESP3:**

One of the following:

* [Simple string reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-strings) `OK` if executed correctly.
* [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) in these cases: non-existent key or destination key is not of the same width and/or depth.


