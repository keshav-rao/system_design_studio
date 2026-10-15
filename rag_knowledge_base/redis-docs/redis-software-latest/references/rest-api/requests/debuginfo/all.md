# All nodes debug info requests

```json metadata
{
  "schema_version": 2,
  "title": "All nodes debug info requests",
  "description": "Documents the Redis Software REST API debuginfo/all requests.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"get-all-request","title":"Request"},{"id":"get-all-response","title":"Response"},{"id":"get-all-status-codes","title":"Status codes"}],"id":"get-all-debuginfo","title":"Get debug info for all nodes"}]}

,
  "codeExamples": []
}
```



This REST API path is deprecated as of Redis Software version 7.4.2. Use the new path [`/v1/cluster/debuginfo`](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/cluster/debuginfo) instead.


| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-all-debuginfo) | `/v1/debuginfo/all` | Get debug info for all nodes |

## Get debug info for all nodes {#get-all-debuginfo}

	GET /v1/debuginfo/all

Downloads a tar file that contains debug info from all nodes.

#### Required permissions

| Permission name |
|-----------------|
| [view_debugging_info](https://redis.io/docs/latest/operate/rs/references/rest-api/permissions#view_debugging_info) |

### Request {#get-all-request} 

#### Example HTTP request

	GET /v1/debuginfo/all 

### Response {#get-all-response} 

Downloads the debug info in a tar file called `filename.tar.gz`. Extract the files from the tar file to access the debug info for all nodes.

#### Response headers

| Key | Value | Description |
|-----|-------|-------------|
| Content-Type | application/x-gzip | Media type of request/response body |
| Content-Length | 653350 | Length of the response body in octets |
| Content-Disposition | attachment; filename=debuginfo.tar.gz | Display response in browser or download as attachment |

### Status codes {#get-all-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | Success. |
| [500 Internal Server Error](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.5.1) | Failed to get debug info. |

