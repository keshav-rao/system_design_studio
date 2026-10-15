# Redis Search commands

```json metadata
{
  "schema_version": 2,
  "title": "Redis Search commands",
  "description": "Lists Redis Search commands and provides links to the command reference pages.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


The following table lists Redis Search commands. See the command links for more information about each command's syntax, arguments, and examples.

| Command | Redis Software | Redis Cloud<br />Flexible & Annual | Redis Cloud<br />Free & Fixed | Description |
|:--------|:----------------------|:-----------------|:-----------------|:------|
| [FT.AGGREGATE](https://redis.io/docs/latest/commands/ft.aggregate) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Runs a search query on an index and groups, sorts, transforms, limits, and/or filters the results. |
| [FT.ALIASADD](https://redis.io/docs/latest/commands/ft.aliasadd) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Adds an alias to an index.  |
| [FT.ALIASDEL](https://redis.io/docs/latest/commands/ft.aliasdel) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Removes an alias from an index. |
| [FT.ALIASLIST](https://redis.io/docs/latest/commands/ft.aliaslist) | <span title="Not supported">&#x274c; Not supported</span> | <span title="Not supported">&#x274c; Not supported</span> | <span title="Not supported">&#x274c; Not supported</nobr></span> | List aliases for an index. |
| [FT.ALIASUPDATE](https://redis.io/docs/latest/commands/ft.aliasupdate) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Adds an alias to an index. If the alias already exists for a different index, it updates the alias to point to the specified index instead. |
| [FT.ALTER](https://redis.io/docs/latest/commands/ft.alter) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Adds a new field to an index. |
| [FT.CONFIG GET](https://redis.io/docs/latest/commands/ft.config-get) |  <span title="Not supported"><nobr>&#x274c; Not supported</span> | <span title="Not supported"><nobr>&#x26A0;&#xFE0F; Not supported</span><sup>[2](#table-note-2)</sup> | <span title="Not supported"><nobr>&#x274c; Not supported</nobr></span> | Displays configuration options. |
| [FT.CONFIG HELP](https://redis.io/docs/latest/commands/ft.config-help) |   <span title="Not supported"><nobr>&#x274c; Not supported</span> | <span title="Not supported"><nobr>&#x274c; Not supported</span> | <span title="Not supported"><nobr>&#x274c; Not supported</nobr></span> | Describes configuration options. |
| [FT.CONFIG SET](https://redis.io/docs/latest/commands/ft.config-set) | <span title="Not supported"><nobr>&#x26A0;&#xFE0F; Not supported</span><sup>[1](#table-note-1)</sup> | <span title="Not supported"><nobr>&#x26A0;&#xFE0F; Not supported</span><sup>[2](#table-note-2)</sup> | <span title="Not supported"><nobr>&#x274c; Not supported</nobr></span> | Sets configuration options. |
| [FT.CREATE](https://redis.io/docs/latest/commands/ft.create) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Creates an index. |
| [FT.CURSOR DEL](https://redis.io/docs/latest/commands/ft.cursor-del) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Deletes a cursor. |
| [FT.CURSOR&nbsp;READ](https://redis.io/docs/latest/commands/ft.cursor-read) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Reads the next results from an existing cursor. |
| [FT.DICTADD](https://redis.io/docs/latest/commands/ft.dictadd) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Adds terms to a dictionary. |
| [FT.DICTDEL](https://redis.io/docs/latest/commands/ft.dictdel) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Deletes terms from a dictionary. |
| [FT.DICTDUMP](https://redis.io/docs/latest/commands/ft.dictdump) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Returns all terms in the specified dictionary. |
| [FT.DROPINDEX](https://redis.io/docs/latest/commands/ft.dropindex) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Deletes an index. |
| [FT.EXPLAIN](https://redis.io/docs/latest/commands/ft.explain) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Returns the execution plan for a complex query as a string. |
| [FT.EXPLAINCLI](https://redis.io/docs/latest/commands/ft.explaincli) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Returns the execution plan for a complex query as an [array](https://redis.io/docs/latest/develop/reference/protocol-spec#arrays). |
| [FT.HYBRID](https://redis.io/docs/latest/commands/ft.hybrid) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Performs hybrid search combining text search and vector similarity with configurable fusion methods. |
| [FT.INFO](https://redis.io/docs/latest/commands/ft.info) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Returns index information and statistics.  |
| [FT._LIST](https://redis.io/docs/latest/commands/ft._list) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Lists all indexes. |
| [FT.PROFILE](https://redis.io/docs/latest/commands/ft.profile) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Runs [FT.SEARCH](https://redis.io/docs/latest/commands/ft.search) or [FT.AGGREGATE](https://redis.io/docs/latest/commands/ft.aggregate) and reports performance information. |
| [FT.SEARCH](https://redis.io/docs/latest/commands/ft.search) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Searches an index for a text query and returns matching documents or document IDs. |
| [FT.SPELLCHECK](https://redis.io/docs/latest/commands/ft.spellcheck) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Suggests spelling corrections for misspelled terms in a query. |
| [FT.SYNDUMP](https://redis.io/docs/latest/commands/ft.syndump) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Returns a list of synonym terms and their synonym group IDs. |
| [FT.SYNUPDATE](https://redis.io/docs/latest/commands/ft.synupdate) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Creates or updates a synonym group with additional terms. |
| [FT.TAGVALS](https://redis.io/docs/latest/commands/ft.tagvals) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</nobr></span> | Returns all distinct values indexed in a tag field. |

1. <a name="table-note-1" style="display: block; height: 80px; margin-top: -80px;"></a>Use [`rladmin`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin) or the [REST API](https://redis.io/docs/latest/operate/rs/references/rest-api) to change Redis Search configuration for Redis Software. See [Redis Search configuration compatibility with Redis Software](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/search/config) for more information and examples.

2. <a name="table-note-2" style="display: block; height: 80px; margin-top: -80px;"></a>[Contact support](https://redis.com/company/support/) to view the current configuration values or request configuration changes for Flexible or Annual Redis Cloud subscriptions.

