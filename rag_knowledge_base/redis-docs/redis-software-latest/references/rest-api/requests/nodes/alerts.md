# Node alerts requests

```json metadata
{
  "schema_version": 2,
  "title": "Node alerts requests",
  "description": "Node alert requests",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"get-all-request","title":"Request"},{"id":"get-all-response","title":"Response"},{"id":"get-all-status-codes","title":"Status codes"}],"id":"get-all-nodes-alerts","title":"Get all alert states"},{"children":[{"id":"get-request-all-alerts","title":"Request"},{"id":"get-response-all-alerts","title":"Response"},{"id":"get-status-codes-all-alerts","title":"Status codes"}],"id":"get-node-alerts","title":"Get node alert states"},{"children":[{"id":"get-request","title":"Request"},{"id":"get-response","title":"Response"},{"id":"get-status-codes","title":"Status codes"}],"id":"get-node-alert","title":"Get node alert state"}]}

,
  "codeExamples": []
}
```


| Method | Path | Description |
|--------|------|-------------|
| [GET](#get-all-nodes-alerts) | `/v1/nodes/alerts` | Get all alert states for all nodes |
| [GET](#get-node-alerts) | `/v1/nodes/alerts/{uid}` | Get all alert states for a node |
| [GET](#get-node-alert) | `/v1/nodes/alerts/{uid}/{alert}` | Get node alert state |

## Get all alert states {#get-all-nodes-alerts}

	GET /v1/nodes/alerts

Get all alert states for all nodes.

#### Required permissions

| Permission name |
|-----------------|
| [view_all_nodes_alerts](https://redis.io/docs/latest/operate/rs/references/rest-api/permissions#view_all_nodes_alerts) |

### Request {#get-all-request} 

#### Example HTTP request

	GET /v1/nodes/alerts 

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

#### Query parameters

| Field | Type | Description |
|-------|------|-------------|
| ignore_settings | boolean | Retrieve updated alert state regardless of the cluster's alert_settings. When not present, a disabled alert will always be retrieved as disabled with a false state. (optional) |

### Response {#get-all-response} 

Returns a hash of node UIDs and the [alert states](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/alert) for each node.

#### Example JSON body

```json
{
    "1": {
        "node_cpu_utilization": {
            "change_time": "2014-12-22T10:42:00Z",
            "change_value": {
                "cpu_util": 2.500000000145519,
                "global_threshold": "1",
                "state": true
            },
            "enabled": true,
            "state": true,
            "severity": "WARNING"
        },
        "..."
    },
    "..."
}
```

### Status codes {#get-all-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | No error |

## Get node alert states {#get-node-alerts}

	GET /v1/nodes/alerts/{int: uid}

Get all alert states for a node.

#### Required permissions

| Permission name |
|-----------------|
| [view_node_alerts](https://redis.io/docs/latest/operate/rs/references/rest-api/permissions#view_node_alerts) |

### Request {#get-request-all-alerts} 

#### Example HTTP request

	GET /v1/nodes/alerts/1 


#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |


#### Query parameters

| Field | Type | Description |
|-------|------|-------------|
| ignore_settings | boolean | Retrieve updated alert state regardless of the cluster's alert_settings. When not present, a disabled alert will always be retrieved as disabled with a false state. (optional) |

### Response {#get-response-all-alerts} 

Returns a hash of [alert objects](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/alert) and their states for a specific node.

#### Example JSON body

```json
{
   "node_cpu_utilization": {
        "change_time": "2014-12-22T10:42:00Z",
        "change_value": {
            "cpu_util": 2.500000000145519,
            "global_threshold": "1",
            "state": true
        },
        "enabled": true,
        "state": true,
        "severity": "WARNING",
    },
    "..."
}
```

### Status codes {#get-status-codes-all-alerts} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | No error |
| [404 Not Found](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) | Specified node does not exist |

## Get node alert state {#get-node-alert}

	GET /v1/nodes/alerts/{int: uid}/{alert}

Get a node alert state.

#### Required permissions

| Permission name |
|-----------------|
| [view_node_alerts](https://redis.io/docs/latest/operate/rs/references/rest-api/permissions#view_node_alerts) |

### Request {#get-request} 

#### Example HTTP request

	GET /v1/nodes/alerts/1/node_cpu_utilization 


#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |


#### Query parameters

| Field | Type | Description |
|-------|------|-------------|
| ignore_settings | boolean | Retrieve updated alert state regardless of the cluster's alert_settings. When not present, a disabled alert will always be retrieved as disabled with a false state. (optional) |

### Response {#get-response} 

Returns an [alert object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/alert).

#### Example JSON body

```json
{
    "change_time": "2014-12-22T10:42:00Z",
    "change_value": {
        "cpu_util": 2.500000000145519,
        "global_threshold": "1",
        "state": true
    },
    "enabled": true,
    "state": true,
    "severity": "WARNING",
}
```

### Status codes {#get-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | No error |
| [404 Not Found](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.5) | Specified alert or node does not exist |

