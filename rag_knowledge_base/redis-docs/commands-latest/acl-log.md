# ACL LOG

```json metadata
{
  "schema_version": 2,
  "title": "ACL LOG",
  "description": "Lists recent security events generated due to ACL rules.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"arguments":[{"display_text":"count","name":"count","type":"integer"},{"display_text":"reset","name":"reset","token":"RESET","type":"pure-token"}],"name":"operation","optional":true,"type":"oneof"}],
  "syntax_fmt": "ACL LOG [count | RESET]",
  "complexity": "O(N) with N being the number of entries shown.",
  "group": "server",
  "command_flags": ["admin","noscript","loading","stale"],
  "acl_categories": ["@admin","@slow","@dangerous"],
  "since": "6.0.0",
  "arity": -2,
  "tableOfContents": {"sections":[{"id":"optional-arguments","title":"Optional arguments"},{"id":"examples","title":"Examples"},{"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The command shows a list of recent ACL security events:

1. Failed authentications with [`AUTH`](https://redis.io/docs/latest/commands/auth) or [`HELLO`](https://redis.io/docs/latest/commands/hello) (reason = auth)
2. Commands violating the current ACL rules
   - Disallowed commands (reason = command).
   - Disallowed keys (reason = key).
   - Disallowed pub/sub channel (reason = channel).

The optional argument specifies how many entries to show. By default
up to ten failures are returned. The special [`RESET`](https://redis.io/docs/latest/commands/reset) argument clears the log.
Entries are displayed starting from the most recent.

## Optional arguments

<details open><summary><code>count | RESET</code></summary>

The number of recent entries to return, or `RESET` to clear the log.

</details>

## Examples

```
> AUTH someuser wrongpassword
(error) WRONGPASS invalid username-password pair
> ACL LOG 1
1)  1) "count"
    2) (integer) 1
    3) "reason"
    4) "auth"
    5) "context"
    6) "toplevel"
    7) "object"
    8) "AUTH"
    9) "username"
   10) "someuser"
   11) "age-seconds"
   12) "8.038"
   13) "client-info"
   14) "id=3 addr=127.0.0.1:57275 laddr=127.0.0.1:6379 fd=8 name= age=16 idle=0 flags=N db=0 sub=0 psub=0 ssub=0 multi=-1 qbuf=48 qbuf-free=16842 argv-mem=25 multi-mem=0 rbs=1024 rbp=0 obl=0 oll=0 omem=0 tot-mem=18737 events=r cmd=auth user=default redir=-1 resp=2"
   15) "entry-id"
   16) (integer) 0
   17) "timestamp-created"
   18) (integer) 1675361492408
   19) "timestamp-last-updated"
   20) (integer) 1675361492408
```

## Details

Each log entry is composed of the following fields:

1. `count`: The number of security events detected within a 60 second period that are represented by this entry.
2. `reason`: The reason that the security events were logged. Either `command`, `key`, `channel`, or `auth`.
3. `context`: The context that the security events were detected in. Either `toplevel`, `multi`, `lua`, or `module`.
4. `object`: The resource that the user had insufficient permissions to access. `auth` when the reason is `auth`.
5. `username`: The username that executed the command that caused the security events or the username that had a failed authentication attempt.
6. `age-seconds`: Age of the log entry in seconds.
7. `client-info`: Displays the client info of a client which caused one of the security events.
8. `entry-id`: The sequence number of the entry (starting at 0) since the server process started. Can also be used to check if items were "lost", if they fell between periods.
9. `timestamp-created`: A UNIX timestamp in `milliseconds` at the time the entry was first created.
10. `timestamp-last-updated`: A UNIX timestamp in `milliseconds` at the time the entry was last updated.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> | <span title="Not supported">&#x274c; Standard</span><br /><span title="Not supported"><nobr>&#x274c; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

When called to show security events:
* [Array reply](../../develop/reference/protocol-spec#arrays): an array of [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings) elements representing ACL security events.
When called with `RESET`:
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the security log was cleared.

**RESP3:**

When called to show security events:
* [Array reply](../../develop/reference/protocol-spec#arrays): an array of [Bulk string reply](../../develop/reference/protocol-spec#bulk-strings) elements representing ACL security events.
When called with `RESET`:
* [Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK` if the security log was cleared.



