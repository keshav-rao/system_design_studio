# Node identity object

```json metadata
{
  "schema_version": 2,
  "title": "Node identity object",
  "description": "Documents the node_identity object used with Redis Software REST API calls.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


| Name | Type/Value | Description |
|------|------------|-------------|
| bigstore_driver | 'rocksdb' | Bigstore driver name or none (deprecated, use the [cluster object](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/cluster)'s `bigstore_driver` instead) |
| bigstore_enabled | boolean (default: false) | If `true`, then flash storage is enabled on this node for [Redis Flex and Auto Tiering](https://redis.io/docs/latest/operate/rs/databases/flash) databases. Configurable during [bootstrapping](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bootstrap#post-bootstrap). After bootstrapping, it is read-only. |
| identity | [identity](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/bootstrap/identity) object | Node identity |
| limits | [limits](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/bootstrap/limits) object | Node limits |
| paths | [paths](https://redis.io/docs/latest/operate/rs/references/rest-api/objects/bootstrap/paths) object | Storage paths object |

