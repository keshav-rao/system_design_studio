# CRDB purge requests

```json metadata
{
  "schema_version": 2,
  "title": "CRDB purge requests",
  "description": "Purge removed Active-Active database requests",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"put-request","title":"Request"},{"id":"put-response","title":"Response"},{"id":"put-status-codes","title":"Status codes"}],"id":"put-crdbs-purge","title":"Purge data from removed instance"}]}

,
  "codeExamples": []
}
```


| Method | Path | Description |
|--------|------|-------------|
| [PUT](#put-crdbs-purge) | `/v1/crdbs/{crdb_guid}/purge` | Purge data from an instance that was forcibly removed from the Active-Active database |

## Purge data from removed instance {#put-crdbs-purge}

	PUT /v1/crdbs/{crdb_guid}/purge

Purge the data from an instance that was removed from the
Active-Active database by force.

When you force the removal of an instance from an Active-Active
database, the removed instance keeps the data and configuration
according to the last successful synchronization.

To delete the data and configuration from the forcefully removed
instance you must use this API (Must be executed locally on the
removed instance).

### Request {#put-request} 

#### Example HTTP request

    PUT /v1/crdbs/1/purge

#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| crdb_guid | string | Globally unique Active-Active database ID (GUID) |

#### Request body

| Field | Type | Description |
|-------|------|-------------|
| instances | array of integers | Array of unique instance IDs |

### Response {#put-response} 

Returns a [CRDB task object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/crdb_task).

### Status codes {#put-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | Action was successful. |
| [400 Bad Request](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) | The request is invalid or malformed. |
| [401 Unauthorized](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2) | Unauthorized request. Invalid credentials |
| [404 Not Found](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) | Configuration, instance, or Active-Active database not found. |

