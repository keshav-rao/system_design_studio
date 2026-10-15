# Smart client handoffs

```json metadata
{
  "schema_version": 2,
  "title": "Smart client handoffs",
  "description": "Enable Smart client handoffs for your Redis Software cluster.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"known-limitations","title":"Known limitations"}]}

,
  "codeExamples": []
}
```


Smart client handoffs (SCH) is a feature of Redis Cloud and Redis Software servers that lets them actively notify clients about planned server maintenance shortly before it happens. This lets a client reconnect or otherwise respond gracefully without significant interruptions in service.
See [Smart client handoffs](https://redis.io/docs/latest/develop/clients/sch) for more information about SCH.

SCH is supported for Redis Software from v8.0.2 on, and OSS Cluster API from v8.0.16 on.
The degree of support for SCH depends on the specific upgrade method you use, as detailed in the table below.

| Upgrade method | SCH support | Expected behavior |
| --- | --- | --- |
| [Rolling upgrade](https://redis.io/docs/latest/operate/rs/installing-upgrading/upgrading/upgrade-cluster#rolling-upgrade) | Full | New nodes and old ones removed sequentially. SCH pre-handoffs and relaxed timeouts greatly reduce disruptions during the upgrade. |
| [In-place upgrade](https://redis.io/docs/latest/operate/rs/installing-upgrading/upgrading/upgrade-cluster#in-place-upgrade) | Partial | Relaxed timeouts reduce errors but there are no pre-handoffs. Disconnections occur when processes are replaced during the upgrade, so clients should rely on auto-reconnect, which will cause brief lapses in service. |
| [Maintenance mode](https://redis.io/docs/latest/operate/rs/clusters/maintenance-mode) | Full | SCH is fully supported during hardware or OS patching operations. Pre-handoffs and relaxed timeouts minimize application impact. |


To enable SCH on a Redis Software server, you must use the
[/v1/cluster](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/cluster#put-cluster)
REST API request to set the `client_maint_notifications` option to `true`.
The example below shows how to do this using the
[`curl`](https://curl.se/) command line utility:

```bash
curl -k -X PUT -H "accept: application/json" \
    -H "content-type: application/json" \
    -u "<username>:<password>" \
    -d '{ "client_maint_notifications": true }' \
    https://<host>:<port>/v1/cluster
```

## Known limitations

During a rolling upgrade with SCH enabled, when some slot's shards have migrated to a different node but are still reachable from their original node, results of the `SCAN` command might be inconsistent: it might show some of the keys, it might show keys that are not reachable from that node, or it might show no keys. When the slot migration is done, this issue will fix itself.

