# Cluster services configuration requests

```json metadata
{
  "schema_version": 2,
  "title": "Cluster services configuration requests",
  "description": "Cluster services configuration requests",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"get-request","title":"Request"},{"id":"get-response","title":"Response"},{"id":"get-status-codes","title":"Status codes"}],"id":"get-cluster-services_config","title":"Get cluster services configuration"},{"children":[{"id":"put-request","title":"Request"},{"id":"put-response","title":"Response"},{"id":"put-status-codes","title":"Status codes"}],"id":"put-cluster-services_config","title":"Update cluster services configuration"}]}

,
  "codeExamples": []
}
```


| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-cluster-services_config) | `/v1/cluster/services_configuration` | Get cluster services settings |
| [PUT](#put-cluster-services_config) | `/v1/cluster/services_configuration` | Update cluster services settings |

## Get cluster services configuration {#get-cluster-services_config}

	GET /v1/cluster/services_configuration

Get cluster services settings.

#### Required permissions

| Permission name |
|-----------------|
| [view_cluster_info](https://redis.io/docs/latest/operate/rs/references/rest-api/permissions#view_cluster_info) |

### Request {#get-request} 

#### Example HTTP request

	GET /v1/cluster/services_configuration 

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

### Response {#get-response} 

Returns a [services configuration object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration).

#### Example JSON body

```json
{
     "cm_server": {
         "operating_mode": "disabled"
     },
     "mdns_server": {
         "operating_mode": "enabled"
     },
     "// additional services..."
}
```

### Status codes {#get-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | No error |

## Update cluster services configuration {#put-cluster-services_config}

	PUT /v1/cluster/services_configuration

Update the cluster services settings.

#### Required permissions

| Permission name |
|-----------------|
| [update_cluster](https://redis.io/docs/latest/operate/rs/references/rest-api/permissions#update_cluster) |

### Request {#put-request} 

#### Example HTTP request

	PUT /v1/cluster/services_configuration 

#### Example JSON body

```json
{
     "cm_server": {
         "operating_mode": "disabled"
     },
     "// additional services..."
}
```

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

#### Request body

Include a [services configuration object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration) with updated fields in the request body.

### Response {#put-response} 

Returns the updated [services configuration object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration).

#### Example JSON body

```json
{
     "cm_server": {
         "operating_mode": "disabled"
     },
     "mdns_server": {
         "operating_mode": "enabled"
     },
     "// additional services..."
}
```

### Status codes {#put-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | No error |

