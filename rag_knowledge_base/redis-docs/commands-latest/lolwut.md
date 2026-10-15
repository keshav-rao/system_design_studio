# LOLWUT

```json metadata
{
  "schema_version": 2,
  "title": "LOLWUT",
  "description": "Displays computer art and the Redis version",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"version","name":"version","optional":true,"token":"VERSION","type":"integer"}],
  "syntax_fmt": "LOLWUT [VERSION version]",
  "group": "server",
  "command_flags": ["readonly","fast"],
  "acl_categories": ["@read","@fast"],
  "since": "5.0.0",
  "arity": -1,
  "tableOfContents": {"sections":[{"id":"optional-arguments","title":"Optional arguments"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The LOLWUT command displays the Redis version: however as a side effect of
doing so, it also creates a piece of generative computer art that is different
with each version of Redis. The command was introduced in Redis 5 and announced
with this [blog post](http://antirez.com/news/123).

By default the `LOLWUT` command will display the piece corresponding to the
current Redis version, however it is possible to display a specific version
using the following form:

    LOLWUT VERSION 5 ... other optional arguments ...

Of course the "5" above is an example. Each LOLWUT version takes a different
set of arguments in order to change the output. The user is encouraged to
play with it to discover how the output changes adding more numerical
arguments.

LOLWUT wants to be a reminder that there is more in programming than just
putting some code together in order to create something useful. Every
LOLWUT version should have the following properties:

1. It should display some computer art. There are no limits as long as the output works well in a normal terminal display. However the output should not be limited to graphics (like LOLWUT 5 and 6 actually do), but can be generative poetry and other non graphical things.
2. LOLWUT output should be completely useless. Displaying some useful Redis internal metrics does not count as a valid LOLWUT.
3. LOLWUT output should be fast to generate so that the command can be called in production instances without issues. It should remain fast even when the user experiments with odd parameters.
4. LOLWUT implementations should be safe and carefully checked for security, and resist to untrusted inputs if they take arguments.
5. LOLWUT must always display the Redis version at the end.

## Optional arguments

<details open><summary><code>VERSION version</code></summary>

Request a specific version of the generated art.

</details>

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): a string containing generative computer art and the Redis version.

**RESP3:**

[Verbatim string reply](../../develop/reference/protocol-spec#verbatim-strings): a string containing generative computer art and the Redis version.



