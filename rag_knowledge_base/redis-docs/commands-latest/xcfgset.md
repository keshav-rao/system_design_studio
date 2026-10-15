# XCFGSET

```json metadata
{
  "schema_version": 2,
  "title": "XCFGSET",
  "description": "Sets the IDMP configuration parameters for a stream.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"key_spec_index":0,"name":"key","type":"key"},{"name":"idmp-duration","optional":true,"token":"IDMP-DURATION","type":"integer"},{"name":"idmp-maxsize","optional":true,"token":"IDMP-MAXSIZE","type":"integer"}],
  "syntax_fmt": "XCFGSET key [IDMP-DURATION idmp-duration]\n  [IDMP-MAXSIZE idmp-maxsize]",
  "complexity": "O(1)",
  "group": "stream",
  "command_flags": ["write","fast"],
  "acl_categories": ["@write","@stream","@fast"],
  "since": "8.6.0",
  "arity": -2,
  "key_specs": [{"RW":true,"begin_search":{"spec":{"index":1},"type":"index"},"find_keys":{"spec":{"keystep":1,"lastkey":0,"limit":0},"type":"range"},"update":true}],
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"children":[{"id":"behavior","title":"Behavior"},{"id":"error-conditions","title":"Error conditions"}],"id":"details","title":"Details"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Sets the IDMP (Idempotent Message Processing) configuration parameters for a stream. This command configures how long idempotent IDs are retained and the maximum number of idempotent IDs tracked per producer.

For more details, see [Idempotent message processing](../../develop/data-types/streams/idempotency/).

## Required arguments

<details open><summary><code>key</code></summary>

The name of the stream key. The stream must already exist.

</details>

## Optional arguments

<details open><summary><code>IDMP-DURATION idmp-duration</code></summary>

Sets the duration, in seconds, for which each idempotent ID (iid) is retained in the stream's IDMP map. Valid range: 1-86,400 seconds. Default: 100 seconds.

When an idempotent ID expires, it can be reused for new messages. This provides an operational guarantee that Redis will not forget an idempotency ID before the duration elapses (unless capacity is reached).

</details>

<details open><summary><code>IDMP-MAXSIZE idmp-maxsize</code></summary>

Sets the maximum number of most recent idempotent IDs kept for each producer in the stream's IDMP map. Valid range: 1-10,000 entries. Default: 100 entries.

When the capacity is reached, the oldest idempotent IDs for that producer are evicted regardless of remaining duration. This prevents unbounded memory growth.

</details>

## Details

### Behavior

- Calling `XCFGSET` clears all existing producer IDMP maps for the stream.
- At least one of `IDMP-DURATION` or `IDMP-MAXSIZE` must be specified.
- The stream must exist before calling this command.
- Configuration changes apply immediately to all future IDMP operations.

### Error conditions

The command returns an error in the following cases:

- `WRONGTYPE`: The key exists but is not a stream.
- `ERR no such key`: The stream does not exist.
- `ERR syntax error`: Invalid command syntax or missing required arguments.
- `ERR invalid duration`: Duration value is outside the valid range (1-86,400).
- `ERR invalid maxsize`: Maxsize value is outside the valid range (1-10,000).

## Examples

```redis-cli
XADD mystream * field value
XCFGSET mystream IDMP-DURATION 300
XCFGSET mystream IDMP-MAXSIZE 1000
XCFGSET mystream IDMP-DURATION 600 IDMP-MAXSIZE 500
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the configuration was set successfully.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the configuration was set successfully.



