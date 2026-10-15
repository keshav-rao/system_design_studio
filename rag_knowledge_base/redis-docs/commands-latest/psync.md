# PSYNC

```json metadata
{
  "schema_version": 2,
  "title": "PSYNC",
  "description": "An internal command used in replication.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"replicationid","name":"replicationid","type":"string"},{"display_text":"offset","name":"offset","type":"integer"}],
  "syntax_fmt": "PSYNC replicationid offset",
  "group": "server",
  "command_flags": ["admin","noscript","no_async_loading","no_multi"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "2.8.0",
  "arity": -3,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Initiates a replication stream from the master.

The `PSYNC` command is called by Redis replicas for initiating a replication
stream from the master.

For more information about replication in Redis please check the
[replication page](https://redis.io/docs/latest/operate/oss_and_stack/management/replication).

## Required arguments

<details open><summary><code>replicationid</code></summary>

The replication ID of the master.

</details>

<details open><summary><code>offset</code></summary>

The replication offset to resume from.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

**Non-standard return value**, a bulk transfer of the data followed by `PING` and write requests from the master.

**RESP3:**

**Non-standard return value**, a bulk transfer of the data followed by `PING` and write requests from the master.



