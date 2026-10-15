# Services configuration object

```json metadata
{
  "schema_version": 2,
  "title": "Services configuration object",
  "description": "An object for optional cluster services settings",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Optional cluster services settings

| Name | Type/Value | Description |
|------|------------|-------------|
| alert_mgr | [alert_mgr](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration/alert_mgr) object | Whether to enable/disable the alert manager processes |
| call_home_agent | [call_home_agent](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration/call_home_agent) object | Whether to enable/disable the call_home_agent process, which sends daily usage statistics to Redis |
| cm_server | [cm_server](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration/cm_server) object | Whether to enable/disable the CM server |
| crdb_coordinator | [crdb_coordinator](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration/crdb_coordinator) object | Whether to enable/disable the CRDB coordinator process |
| crdb_worker | [crdb_worker](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration/crdb_worker) object | Whether to enable/disable the CRDB worker processes |
| entraid_agent_mgr | [entraid_agent_mgr](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration/entraid_agent_mgr) object | Whether to enable/disable the Entra ID agent manager process |
| ldap_agent_mgr | [ldap_agent_mgr](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration/ldap_agent_mgr) object | Whether to enable/disable the LDAP agent manager processes |
| mdns_server | [mdns_server](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration/mdns_server) object | Whether to enable/disable the multicast DNS server |
| metrics_local_storage_service | [metrics_local_storage_service](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration/metrics_local_storage_service) object | Whether to enable/disable local metrics storage |
| pdns_server | [pdns_server](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration/pdns_server) object | Whether to enable/disable the PDNS server |
| sentinel_service | [sentinel_service](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration/sentinel_service) object | Whether to enable/disable the Sentinel service process |
| stats_archiver | [stats_archiver](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/services_configuration/stats_archiver) object | Whether to enable/disable the stats archiver service |

