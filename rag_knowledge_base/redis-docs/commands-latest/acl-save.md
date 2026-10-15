# ACL SAVE

```json metadata
{
  "schema_version": 2,
  "title": "ACL SAVE",
  "description": "Saves the effective ACL rules in the configured ACL file.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "ACL SAVE",
  "complexity": "O(N). Where N is the number of configured users.",
  "group": "server",
  "command_flags": ["admin","noscript","loading","stale"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "6.0.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

When Redis is configured to use an ACL file (with the `aclfile` configuration
option), this command will save the currently defined ACLs from the server memory to the ACL file.

## Examples

```
> ACL SAVE
+OK

> ACL SAVE
-ERR There was an error trying to save the ACLs. Please check the server logs for more information
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.
The command may fail with an error for several reasons: if the file cannot be written or if the server is not configured to use an external ACL file.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`.
The command may fail with an error for several reasons: if the file cannot be written or if the server is not configured to use an external ACL file.



