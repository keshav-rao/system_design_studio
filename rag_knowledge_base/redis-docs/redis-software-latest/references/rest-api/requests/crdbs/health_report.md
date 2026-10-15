# CRDB health report requests

```json metadata
{
  "schema_version": 2,
  "title": "CRDB health report requests",
  "description": "Active-Active database health report requests",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"get-request","title":"Request"},{"id":"get-response","title":"Response"},{"id":"get-status-codes","title":"Status codes"}],"id":"get-crdbs-health","title":"Get health report"}]}

,
  "codeExamples": []
}
```


| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-crdbs-health) | `/v1/crdbs/{crdb_guid}/health_report` | Get a health report for an Active-Active database |

## Get health report {#get-crdbs-health}

	GET /v1/crdbs/{crdb_guid}/health_report

Get a health report for an Active-Active database.

### Request {#get-request} 

#### Example HTTP request

    GET /v1/crdbs/{crdb_guid}/health_report

#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| crdb_guid | string | Globally unique Active-Active database ID (GUID) |

#### Query parameters

| Field | Type | Description |
|-------|------|-------------|
| instance_id | integer | The request retrieves information from the specified Active-Active database instance. If this instance doesn’t exist, the request retrieves information from all instances. (optional) |

### Response {#get-response} 

Returns a JSON array of [CRDB health report objects](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/crdb/health_report).

### Status codes {#get-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | Action was successful. |
| [404 Not Found](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) | Configuration or Active-Active database not found. |

