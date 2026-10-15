# CRDB updates requests

```json metadata
{
  "schema_version": 2,
  "title": "CRDB updates requests",
  "description": "Update Active-Active configuration requests",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"post-request","title":"Request"},{"id":"post-response","title":"Response"},{"id":"post-status-codes","title":"Status codes"}],"id":"post-crdbs-updates","title":"Modify Active-Active configuration"}]}

,
  "codeExamples": []
}
```


| Method | Path | Description |
|--------|------|-------------|
| [POST](#post-crdbs-updates) | `/v1/crdbs/{crdb_guid}/updates` | Modify Active-Active configuration |

## Modify Active-Active configuration {#post-crdbs-updates}

	POST /v1/crdbs/{crdb_guid}/updates

Modify Active-Active configuration.

> [!WARNING]
> This is a very powerful API request and can cause damage if used incorrectly.

To add or remove instances, you must use this API. For simple configuration updates, use [`PATCH /crdbs/{crdb_guid}`](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/crdbs#patch-crdbs) instead.

Updating `default_db_config` affects both existing and new instances.

When you update `db_config`, it changes the configuration of the specified database instance. This field overrides any corresponding fields in `default_db_config`.

For a list of which settings must be identical across all instances and which to set per instance, see the [CRDB database config object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/crdb/database_config) reference.

### Request {#post-request} 

#### Example HTTP request

    POST /v1/crdbs/1/updates

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| X-Task-ID | string | Specified task ID |
| X-Result-TTL | integer | Time (in seconds) to keep task result |

#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| crdb_guid | string | Globally unique Active-Active database ID (GUID) |

#### Query parameters

| Field | Type | Description |
|-------|------|-------------|
| dry_run | boolean | Validate the request without applying changes (optional) |

#### Request body

Include a [CRDB modify_request object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/crdb/modify_request) with updated fields in the request body.

### Response {#post-response} 

Returns a [CRDB task object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/crdb_task).

### Status codes {#post-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | The request has been accepted. |
| [400 Bad Request](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) | The posted Active-Active database contains invalid parameters. |
| [401 Unauthorized](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) | Unauthorized request. Invalid credentials |
| [404 Not Found](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) | Configuration, instance or Active-Active database not found. |
| [406&nbsp;Not&nbsp;Acceptable](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.7) | The posted Active-Active database cannot be accepted. |

