# Database shards requests

```json metadata
{
  "schema_version": 2,
  "title": "Database shards requests",
  "description": "REST API requests for database shards",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"get-request","title":"Request"},{"id":"get-response","title":"Response"},{"id":"get-status-codes","title":"Status codes"}],"id":"get-bdb-shards","title":"Get database shards"}]}

,
  "codeExamples": []
}
```


| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-bdb-shards) | `/v1/bdbs/{bdb_uid}/shards` | Get the status of a database's shards |

## Get database shards {#get-bdb-shards}

	GET /v1/bdbs/{int: bdb_uid}/shards

Gets the status for all shards that belong to the specified database.

### Request {#get-request} 

#### Example HTTP request

	GET /v1/bdbs/1/shards?extra_info_keys=used_memory_rss&extra_info_keys=connected_clients

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

#### URL parameters

| Field | Type | Description |
|-------|------|-------------|
| bdb_uid | integer | The unique ID of the database. |

### Response {#get-response} 

The response body contains a JSON array with all shards, represented as [shard objects](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/shard).

#### Example JSON body

```json
[
    {
        "uid": "1",
		"role": "master",
		"assigned_slots": "0-8191",
        "bdb_uid": 1,
        "detailed_status": "ok",
        "loading": {
            "status": "idle"
        },
        "node_uid": "1",
        "redis_info": {
			"connected_clients": 14,
            "used_memory_rss": 12460032
        },
        "report_timestamp": "2024-09-13T15:28:10Z",
        "status": "active"
    },
    {
        "uid": 2,
        "role": "slave",
        // additional fields...
    }
]
```

### Status codes {#get-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](https://www.rfc-editor.org/rfc/rfc9110.html#name-200-ok) | No error. |
| [404 Not Found](https://www.rfc-editor.org/rfc/rfc9110.html#name-404-not-found) | bdb uid does not exist. |

