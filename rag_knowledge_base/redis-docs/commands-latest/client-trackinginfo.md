# CLIENT TRACKINGINFO

```json metadata
{
  "schema_version": 2,
  "title": "CLIENT TRACKINGINFO",
  "description": "Returns information about server-assisted client-side caching for the connection.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "syntax_fmt": "CLIENT TRACKINGINFO",
  "complexity": "O(1)",
  "group": "connection",
  "command_flags": ["noscript","loading","stale"],
  "acl_categories": ["@slow","@connection"],
  "since": "6.2.0",
  "arity": 2,
  "tableOfContents": {"sections":[{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": []
}
```

The command returns information about the current client connection's use of the [server assisted client side caching](https://redis.io/docs/latest/develop/clients/client-side-caching) feature.

Here's the list of tracking information sections and their respective values:

* **flags**: A list of tracking flags used by the connection. The flags and their meanings are as follows:
  * `off`: The connection isn't using server assisted client side caching.
  * `on`: Server assisted client side caching is enabled for the connection.
  * `bcast`: The client uses broadcasting mode.
  * `optin`: The client does not cache keys by default.
  * `optout`: The client caches keys by default.
  * `caching-yes`: The next command will cache keys (exists only together with `optin`).
  * `caching-no`: The next command won't cache keys (exists only together with `optout`).
  * `noloop`: The client isn't notified about keys modified by itself.
  * `broken_redirect`: The client ID used for redirection isn't valid anymore.
* **redirect**: The client ID used for notifications redirection, 0 for self-redirection, or -1 when none.
* **prefixes**: A list of key prefixes for which notifications are sent to the client.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Array reply](../../develop/reference/protocol-spec#arrays): a list of tracking information sections and their respective values.

**RESP3:**

[Map reply](../../develop/reference/protocol-spec#maps): a list of tracking information sections and their respective values.



