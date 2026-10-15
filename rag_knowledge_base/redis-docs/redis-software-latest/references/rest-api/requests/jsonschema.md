# JSON schema requests

```json metadata
{
  "schema_version": 2,
  "title": "JSON schema requests",
  "description": "API object JSON schema requests",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"get-request","title":"Request"},{"id":"get-response","title":"Response"},{"id":"get-status-codes","title":"Status codes"}],"id":"get-jsonschema","title":"Get object JSON schema"}]}

,
  "codeExamples": []
}
```


| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-jsonschema) | `/v1/jsonschema` | Get JSON schema of API objects |

## Get object JSON schema {#get-jsonschema}

	GET /v1/jsonschema

Get the JSON schema of various [Redis Software REST API objects](https://redis.io/docs/latest/operate/rs/references/rest-api/objects).

### Request {#get-request} 

#### Example HTTP request

	GET /v1/jsonschema?object=bdb 

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

#### Query parameters

| Field | Type | Description |
|-------|------|-------------|
| object | string | Optional. The API object name: 'cluster', 'node', 'bdb' etc. |

### Response {#get-response} 

Returns the JSON schema of the specified API object.

#### Example JSON body

```json
{
     "type": "object",
     "description": "An API object that represents a managed database in the cluster.",
     "properties": {
          "...."
     },
     "...."
}
```

### Status codes {#get-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | Success. |
| [406 Not Acceptable](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.7) | Invalid object. |

