# Redis Software REST API requests

```json metadata
{
  "schema_version": 2,
  "title": "Redis Software REST API requests",
  "description": "Documents the requests supported by the Redis Software REST API calls.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


A REST API request requires the following components:
- [HTTP method](https://restfulapi.net/http-methods/) (`GET`, `PUT`, `PATCH`, `POST`, `DELETE`)
- Base URL
- Endpoint

Some requests may also require:
- URL parameters
- [Query parameters](https://en.wikipedia.org/wiki/Query_string)
- [JSON](http://www.json.org) request body
- [Permissions](https://redis.io/docs/latest/operate/rs/references/rest-api/permissions)


| Request | Description |
| --- | --- |
| [actions](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/actions/) | Actions requests |
| [bdbs](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs/) | Database requests |
| [bootstrap](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bootstrap/) | Bootstrap requests |
| [cluster](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/cluster/) | Cluster settings requests |
| [cm_settings](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/cm_settings/) | REST API requests for Cluster Manager UI settings |
| [crdb_tasks](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/crdb_tasks/) | Active-Active database task status requests |
| [crdbs](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/crdbs/) | Active-Active database requests |
| [debuginfo](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/debuginfo/) | Debug info requests |
| [diagnostics](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/diagnostics/) | REST API requests for the diagnostic logging service. |
| [endpoints/stats](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/endpoints-stats/) | Endpoint statistics requests |
| [job_scheduler](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/job_scheduler/) | REST API requests for the job scheduler |
| [jsonschema](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/jsonschema/) | API object JSON schema requests |
| [ldap_mappings](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/ldap_mappings/) | LDAP mappings requests |
| [license](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/license/) | License requests |
| [logs](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/logs/) | Cluster event logs requests |
| [metrics](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/metrics/) | Local metrics storage requests |
| [metrics_config](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/metrics_config/) | Metrics configuration requests |
| [migrations](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/migrations/) | REST API request to get the migration status of a database in the cluster when using Replica Of. |
| [modules](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/modules/) | Redis modules requests |
| [node/master_healthcheck](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/node_master_healthcheck/) | REST API requests to check a node's connection to the cluster's primary node. |
| [nodes](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/nodes/) | Node requests |
| [ocsp](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/ocsp/) | OCSP requests |
| [proxies](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/proxies/) | Proxy requests |
| [redis_acls](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/redis_acls/) | Redis access control list (ACL) requests |
| [roles](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/roles/) | Roles requests |
| [services](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/services/) | REST API requests to list or modify Redis Software services. |
| [shards](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/shards/) | REST API requests for database shards |
| [suffix](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/suffix/) | DNS suffix requests |
| [suffixes](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/suffixes/) | DNS suffixes requests |
| [usage_report](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/usage_report/) | REST API request to get the database usage report from the cluster. |
| [users](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/users/) | User requests |


