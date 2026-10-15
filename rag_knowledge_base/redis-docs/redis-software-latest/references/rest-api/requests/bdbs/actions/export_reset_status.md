# Export resets status database action requests

```json metadata
{
  "schema_version": 2,
  "title": "Export resets status database action requests",
  "description": "Reset database export status requests",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"permissions","title":"Permissions"},{"id":"put-request","title":"Request"},{"id":"put-response","title":"Response"}],"id":"put-bdbs-actions-export-reset-status","title":"Reset database export status"}]}

,
  "codeExamples": []
}
```


| Method | Path | Description |
|--------|------|-------------|
| [PUT](#put-bdbs-actions-export-reset-status) | `/v1/bdbs/{uid}/actions/export_reset_status` | Reset database export status |

## Reset database export status {#put-bdbs-actions-export-reset-status}

	PUT /v1/bdbs/{int: uid}/actions/export_reset_status

Resets the database's `export_status` to idle if an export is not in progress and clears the value of the `export_failure_reason` field.

### Permissions

| Permission name | Roles |
|-----------------|-------|
| [reset_bdb_current_export_status](https://redis.io/docs/latest/operate/rs/references/rest-api/permissions#reset_bdb_current_export_status) | admin<br />cluster_member<br />db_member |

### Request {#put-request}

#### Example HTTP request

```sh
PUT /v1/bdbs/1/actions/export_reset_status
```

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| uid | integer | The unique ID of the database |

### Response {#put-response}

Returns a status code.

#### Status codes {#put-status-codes}

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | The request is accepted and is being processed. |
| [404 Not Found](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) | Attempting to perform an action on a nonexistent database. |
| [406&nbsp;Not&nbsp;Acceptable](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.7) | Not all the modules loaded to the database support 'backup_restore' capability |
| [409 Conflict](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.10) | Database is currently busy with another action. In this context, this is a temporary condition and the request should be reattempted later. |

