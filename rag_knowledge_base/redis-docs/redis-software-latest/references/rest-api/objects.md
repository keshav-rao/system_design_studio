# Redis Software REST API objects

```json metadata
{
  "schema_version": 2,
  "title": "Redis Software REST API objects",
  "description": "Documents the objects used with Redis Software REST API calls.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Certain [REST API requests](https://redis.io/docs/latest/operate/rs/references/rest-api/requests) require you to include specific objects in the request body. Many requests also return objects in the response body.

Both REST API requests and responses represent these objects as [JSON](https://www.json.org).


| Object | Description |
| --- | --- |
| [action](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/action/) | An object that represents cluster actions |
| [alert](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/alert/) | An object that contains alert info |
| [bdb](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/bdb/) | An object that represents a database |
| [bdb_group](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/bdb_group/) | An object that represents a group of databases with a shared memory pool |
| [bootstrap](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/bootstrap/) | An object for bootstrap configuration |
| [certificates](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/certificates/) | An object that represents a certificate |
| [check_result](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/check_result/) | An object that contains the results of a cluster check |
| [cluster](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/cluster/) | An object that represents a cluster |
| [cluster_settings](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/cluster_settings/) | An object for cluster resource management settings |
| [cm_settings](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/cm_settings/) | A REST API object that represents Cluster Manager UI settings |
| [crdb](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/crdb/) | An object that represents an Active-Active database |
| [crdb_task](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/crdb_task/) | An object that represents a CRDB task |
| [db_alerts_settings](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/db_alerts_settings/) | An object for database alerts configuration |
| [db_conns_auditing_config](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/db-conns-auditing-config/) | An object for database connection auditing settings |
| [job_scheduler](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/job_scheduler/) | An object for job scheduler settings |
| [jwt_authorize](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/jwt_authorize/) | An object for user authentication or a JW token refresh request |
| [ldap](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/ldap/) | An object that contains the cluster's LDAP configuration |
| [ldap_mapping](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/ldap_mapping/) | An object that represents a mapping between an LDAP group and roles |
| [metrics_config](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/metrics_config/) | An object that represents the cluster's v2 metrics stream engine configuration |
| [module](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/module/) | An object that represents a Redis module |
| [module_metadata](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/module_metadata/) | An object that represents Redis module metadata |
| [node](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/node/) | An object that represents a node in the cluster |
| [ocsp](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/ocsp/) | An object that represents the cluster's OCSP configuration |
| [ocsp_status](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/ocsp_status/) | An object that represents the cluster's OCSP status |
| [proxy](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/proxy/) | An object that represents a proxy in the cluster |
| [redis_acl](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/redis_acl/) | An object that represents a Redis access control list (ACL) |
| [role](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/role/) | An object that represents a role |
| [services_configuration](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration/) | An object for optional cluster services settings |
| [shard](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/shard/) | An object that represents a database shard |
| [sso](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/sso/) | An object for single sign-on (SSO) configuration |
| [state-machine](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/state-machine/) | An object that represents a state machine. |
| [statistics](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/statistics/) | An object that contains metrics for clusters, databases, nodes, or shards |
| [suffix](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/suffix/) | An object that represents a DNS suffix |
| [user](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/user/) | An API object that represents a Redis Software user |


