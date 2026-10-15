# ACL DRYRUN

```json metadata
{
  "schema_version": 2,
  "title": "ACL DRYRUN",
  "description": "Simulates the execution of a command by a user, without executing the command.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"username","name":"username","type":"string"},{"display_text":"command","name":"command","type":"string"},{"display_text":"arg","multiple":true,"name":"arg","optional":true,"type":"string"}],
  "syntax_fmt": "ACL DRYRUN username command [arg [arg ...]]",
  "complexity": "O(1).",
  "group": "server",
  "command_flags": ["admin","noscript","loading","stale"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "7.0.0",
  "arity": -4,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

Simulate the execution of a given command by a given user.
This command can be used to test the permissions of a given user without having to enable the user or cause the side effects of running the command.

## Required arguments

<details open><summary><code>username</code></summary>

The user to run the simulated command as.

</details>

<details open><summary><code>command</code></summary>

The command to test.

</details>

## Optional arguments

<details open><summary><code>arg [arg ...]</code></summary>

The arguments to pass to the tested command.

</details>

## Examples

```
> ACL SETUSER VIRGINIA +SET ~*
"OK"
> ACL DRYRUN VIRGINIA SET foo bar
"OK"
> ACL DRYRUN VIRGINIA GET foo
"User VIRGINIA has no permissions to run the 'get' command"
```

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | Might reply with "unknown user" for LDAP users even if `AUTH` succeeds. |

## Return information

**RESP2:**

Any of the following:
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` on success.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): an error describing why the user can't execute the command.

**RESP3:**

Any of the following:
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` on success.
* [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings): an error describing why the user can't execute the command.



