# Rotate cluster certificates requests

```json metadata
{
  "schema_version": 2,
  "title": "Rotate cluster certificates requests",
  "description": "Rotate cluster certificates requests",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"post-request","title":"Request"},{"id":"post-response","title":"Response"},{"id":"post-status-codes","title":"Status codes"}],"id":"post-cluster-certificates-rotate","title":"Rotate cluster certificates"}]}

,
  "codeExamples": []
}
```


| Method | Path | Description |
|--------|------|-------------|
| [POST](#post-cluster-certificates-rotate) | `/v1/cluster/certificates/rotate` | Regenerate all internal cluster certificates |

## Rotate cluster certificates {#post-cluster-certificates-rotate}

	POST /v1/cluster/certificates/rotate

Regenerates all _internal_ cluster certificates.

The certificate rotation will be performed on all nodes within the cluster. If
"name" is provided, only rotate the specified certificate on all nodes within the cluster.

### Request {#post-request} 

#### Example HTTP request

	POST /v1/cluster/certificates/rotate

#### Request headers

| Key | Value | Description |
|-----|-------|-------------|
| Host | cnm.cluster.fqdn | Domain name |
| Accept | application/json | Accepted media type |

### Response {#post-response} 

Responds with a `200 OK` status code if the internal certificates successfully rotate across the entire cluster.

### Status codes {#post-status-codes} 

| Code | Description |
|------|-------------|
| [200 OK](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.2.1) | No error |
| [400 Bad Request](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.1) | Failed, not all nodes have been updated. |
| [403 Forbidden](http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.4) | Unsupported internal certificate rotation. |

