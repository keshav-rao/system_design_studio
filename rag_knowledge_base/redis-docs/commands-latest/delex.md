# DELEX

```json metadata
{
  "schema_version": 2,
  "title": "DELEX",
  "description": "Conditionally removes the specified key based on value or hash digest comparison.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"key","key_spec_index":0,"name":"key","type":"key"},{"arguments":[{"display_text":"ifeq-value","name":"ifeq-value","token":"IFEQ","type":"string"},{"display_text":"ifne-value","name":"ifne-value","token":"IFNE","type":"string"},{"display_text":"ifdeq-digest","name":"ifdeq-digest","token":"IFDEQ","type":"string"},{"display_text":"ifdne-digest","name":"ifdne-digest","token":"IFDNE","type":"string"}],"name":"condition","optional":true,"type":"oneof"}],
  "syntax_fmt": "DELEX key [IFEQ ifeq-value | IFNE ifne-value | IFDEQ ifdeq-digest |\n  IFDNE ifdne-digest]",
  "complexity": "O(1) for IFEQ/IFNE, O(N) for IFDEQ/IFDNE where N is the length of the string value.",
  "group": "string",
  "command_flags": ["write","fast"],
  "acl_categories": ["@write","@string","@fast"],
  "since": "8.4.0",
  "arity": -2,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"delete":true,"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"}}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"children":[{"id":"hash-digest","title":"Hash Digest"}],"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Conditionally removes the specified key based on value or hash digest comparison.

## Required arguments

<details open><summary><code>key</code></summary>

The name of the key to delete.

</details>

## Optional arguments

The following options condition the deletion on the key's current value or [hash digest](#hash-digest). Only one may be specified.

<details open><summary><code>IFEQ ifeq-value</code></summary>

Delete the key only if its value is equal to `ifeq-value`.

</details>

<details open><summary><code>IFNE ifne-value</code></summary>

Delete the key only if its value is not equal to `ifne-value`.

</details>

<details open><summary><code>IFDEQ ifdeq-digest</code></summary>

Delete the key only if its hash digest is equal to `ifdeq-digest`.

</details>

<details open><summary><code>IFDNE ifdne-digest</code></summary>

Delete the key only if its hash digest is not equal to `ifdne-digest`.

</details>

In 8.4, keys must be of type string when using one of the options above. If no options are specified, the key is removed regardless of its type.

## Details

### Hash Digest {#hash-digest}

A hash digest is a fixed-size numerical representation of a string value, computed using the XXH3 hash algorithm. Redis uses this hash digest for efficient comparison operations without needing to compare the full string content. You can retrieve a key's hash digest using the [`DIGEST`](https://redis.io/docs/latest/commands/digest) command, which returns it as a hexadecimal string that you can use with the `IFDEQ` and `IFDNE` options, and also the [`SET`](https://redis.io/docs/latest/commands/set) command's `IFDEQ` and `IFDNE` options.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

One of the following:
- [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): 0 if not deleted (the key does not exist or a specified `IFEQ/IFNE/IFDEQ/IFDNE` condition is false), or 1 if deleted.
- [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if the key exists but holds a value that is not a string and one of `IFEQ, IFNE, IFDEQ,` or `IFDNE` is specified.

**RESP3:**

One of the following:
- [Integer reply](https://redis.io/docs/latest/develop/reference/protocol-spec#integers): 0 if not deleted (the key does not exist or a specified `IFEQ/IFNE/IFDEQ/IFDNE` condition is false), or 1 if deleted.
- [Simple error reply](https://redis.io/docs/latest/develop/reference/protocol-spec#simple-errors) if the key exists but holds a value that is not a string and one of `IFEQ, IFNE, IFDEQ,` or `IFDNE` is specified.



