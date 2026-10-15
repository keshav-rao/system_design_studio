# Redis Software release notes 8.0.x

```json metadata
{
  "schema_version": 2,
  "title": "Redis Software release notes 8.0.x",
  "description": "Redis Software 8! The most performant, most secure, and richest version so far. Built for performance, scale, and reliability to power modern ML and AI applications.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"highlights","title":"Highlights"},{"id":"detailed-release-notes","title":"Detailed release notes"},{"children":[{"id":"breaking-changes","title":"Breaking changes"},{"id":"redis-8-breaking-changes","title":"Redis database version 8 breaking changes"},{"id":"openssl-version-on-rhel-9","title":"OpenSSL version on RHEL 9"},{"id":"reserved-ports","title":"Reserved ports"},{"id":"deprecations","title":"Deprecations"},{"id":"supported-platforms","title":"Supported platforms"}],"id":"version-changes","title":"Version changes"},{"id":"known-issues","title":"Known issues"},{"id":"known-limitations","title":"Known limitations"}]}

,
  "codeExamples": []
}
```


​[​Redis Software version 8.0](https://redis.io/downloads/#Redis_Software) is now available!

## Highlights

This version offers:

- Redis 8.0, 8.2, 8.4, and 8.6 feature set versions

- Performance improvements and memory reduction

- New vector set data structure

- Redis Flex revamped engine

- Redis Search upgrades

- Lag-aware availability API

- Metrics stream engine (General Availability)

- Simplified module management

- New REST API fields for database and cluster configuration

- Customer-managed certificates for internode encryption

- Smart client handoffs

## Detailed release notes

For more detailed release notes, select a build version from the following table:


| Version (Release date) | Major changes | Redis Open Source compatibility |
| --- | --- | --- |
| [8.0.20-108 (September 2026)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-20-108/) | Restored Active-Active database synchronization status indicators on the Cluster Manager overview page. Bug fixes for basic authentication when changing a user password through the REST API, database connectivity, and partial upgrades. Internal fixes and improvements. | Redis 8.6.2, 8.4.0, 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |
| [8.0.20-96 (August 2026)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-20-96/) | Bug fixes for Active-Active database upgrades and synchronization, internode encryption certificates, upgrades on RHEL 9 with an earlier OpenSSL version, and metrics exporter startup. Internal fixes and improvements. | Redis 8.6.2, 8.4.0, 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |
| [8.0.20-68 (July 2026)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-20-68/) | Bug fixes for `-MOVED` response metrics visibility, incomplete cleanup of stale Redis processes, internode encryption certificates, high CPU usage due to excessive heartbeat logging, and certificate-based authentication for LDAP blocking local user authentication. Internal fixes and improvements. | Redis 8.6.2, 8.4.0, 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |
| [8.0.20-44 (June 2026)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-20-44/) | Enabled `client_eviction` by default to fix an issue where a massive volume of traffic directed at a single hot key could cause high latency and out-of-memory errors. Bug fixes for Active-Active databases, LDAP, and ACLs. Internal fixes and improvements. | Redis 8.6.2, 8.4.0, 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |
| [8.0.20-19 (May 2026)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-20-19/) | Certificate-based authentication with LDAP group-based authorization. Amazon Linux 2023 support. API enhancements for Active-Active databases and identifying manually stopped database traffic. New search metrics. | Redis 8.6.2, 8.4.0, 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |
| [8.0.18-36 (May 2026)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-18-36/) | Bug fix for a cluster upgrade issue. Internal fixes and improvements. | Redis 8.6.2, 8.4.0, 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |
| [8.0.18-23 (April 2026)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-18-23/) | Redis 8.6 feature set and enhancements. Disk-based search indexing preview. Active-Active database upgrade API. JSON string reuse mechanism for Active-Active databases. Additional REST API enhancements. | Redis 8.6.2, 8.4.0, 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |
| [8.0.16-33 (March 2026)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-16-33/) | Bug fix for LDAP authentication failures after cluster upgrades. Bug fix for Active-Active database configuration update failures due to missing module featureset version errors after database upgrades. | Redis 8.4.0, 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |
| [8.0.16-29 (March 2026)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-16-29/) | Consolidated health report. Global Active-Active configuration in the Cluster Manager UI. | Redis 8.4.0, 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |
| [8.0.10-81 (February 2026)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-10-81/) | License information in usage reports. Bug fix for high disk usage due to excessive flash logs. | Redis 8.4.0, 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |
| [8.0.10-76 (February 2026)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-10-76/) | Bug fix for database failover error after node crashes and recovery. `filter_node_wd_health_metrics` policy, enabled by default to filter new node watchdog health metrics. Internal fixes and improvements. | Redis 8.4.0, 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |
| [8.0.10-64 (February 2026)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-10-64/) | Redis 8.4 feature set and enhancements. ARM support for RHEL 9 and Ubuntu 22.04. Redis Flex operational optimizations during maintenance, scaling, full sync, and shard migration. | Redis 8.4.0, 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |
| [8.0.6-54 (December 2025)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-6-54/) | Single sign-on for the Cluster Manager UI. Error reports for Replica Of migration status. Automatically download and install user-defined modules during bootstrapping. | Redis 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |
| [8.0.2-41 (November 2025)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-2-41/) | Bug fixes for cluster_wd configuration after restarts, internode encryption certificate storage and retrieval, database creation, Lua script migration issues, and database endpoint assignment after node removal. | Redis 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |
| [8.0.2-17 (October 2025)](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-2-17/) | Redis Software 8! The most performant, most secure, and richest version so far. Built for performance, scale, and reliability to power modern ML and AI applications. | Redis 8.2.1, 8.0.2, 7.4.3, 7.2.7, 6.2.13 |


## Version changes

- [`POST /v1/cluster/actions/change_master`](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/cluster/actions#post-cluster-action) REST API requests will no longer allow a node that exists but is not finished bootstrapping to become the primary node. Such requests will now return the status code `406 Not Acceptable`.

- Node status now returns the actual provisional RAM and flash values even when the maximum number of shards on the node (`max_redis_servers`) is reached. Previously, the API returned 0 for `provisional_ram_of_node` and `provisional_flash_of_node` when a node reached its shard limit. This change affects REST API node status requests and the `rladmin status nodes` command's output.

- `crdb_controller` is enabled by default as of Redis Software version 8.0.18.

### Breaking changes

- Upgrading to Redis Software version 8.0.10 through 8.0.16-29 can cause LDAP authentication to fail with "certificate signed by unknown authority" errors if your cluster currently uses LDAP authentication. This issue was fixed in [Redis Software version 8.0.16-33](https://redis.io/docs/latest/operate/rs/release-notes/rs-8-0-releases/rs-8-0-16-33).

- For Redis Software versions 8.0.2 through 8.0.10, LDAP filters for `user_dn_query` and `dn_group_query` strictly require parentheses to function correctly. Filters that previously worked without parentheses will no longer work after upgrading to these versions. For example, you must include the parentheses in `(sAMAccountName=%u)`. As of version 8.0.16, this breaking change no longer applies, and both `(sAMAccountName=%u)` and `sAMAccountName=%u` are valid filters.

- Redis Software installation script changes:

    - Changed the `--skip-updating-env-path` option to `--update-env-path` when running [`install.sh`](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/install-script).

    - Changed the `skip_updating_env_path` parameter to `update_env_path` in the [installation answers file](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/manage-installation-questions#configure-file-to-answer).

### Redis database version 8 breaking changes {#redis-8-breaking-changes}

When new major versions of Redis Open Source change existing commands, upgrading your database to a new version can potentially break some functionality. Before you upgrade, read the provided list of breaking changes that affect Redis Software and update any applications that connect to your database to handle these changes.

#### ACL behavior changes

Before Redis 8, the existing [ACL](https://redis.io/docs/latest/operate/rs/security/access-control/redis-acl-overview) categories `@read`, `@write`, `@dangerous`, `@admin`, `@slow`, and `@fast` did not include commands for Redis Search and the JSON, time series, and probabilistic data structures.

Starting with Redis 8, Redis includes all Query Engine, JSON, time series, Bloom filter, cuckoo filter, top-k, count-min sketch, and t-digest commands in these existing ACL categories.

As a result:

- Existing ACL rules such as `+@read +@write` will allow access to more commands than in previous versions of Redis. Here are some examples:

  - A user with `+@read` access will be able to execute `FT.SEARCH`.

  - A user with `+@write` access will be able to execute `JSON.SET`. 

- ACL rules such as `+@all -@write`  will allow access to fewer commands than previous versions of Redis.

  - For example, a user with `+@all -@write` will not be able to execute `JSON.SET`.

  - Explicit inclusion of new [command categories](https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl#command-categories) is required to maintain access. The new categories are: `@search`, `@json`, `@timeseries`, `@bloom`, `@cuckoo`, `@topk`, `@cms`, and `@tdigest`.

- ACL rules such as `+@read +JSON.GET` can now be simplified as `+@read` because `JSON.GET` is included in the `@read` category.

Note that the `@all` category did not change, as it always included all the commands.

#### Redis Search changes

The following changes affect behavior and validation in Redis Search:

- Enforces validation for `LIMIT` arguments (offset must be 0 if limit is 0).

- Enforces parsing rules for `FT.CURSOR READ` and `FT.ALIASADD`.

- Parentheses are now required for exponentiation precedence in `APPLY` expressions.

- Invalid input now returns errors instead of empty results.

- Default values revisited for reducers like `AVG`, `COUNT`, `SUM`, `STDDEV`, `QUANTILE`, and others.

- Updates to scoring (`BM25` is now the default instead of `TF-IDF`).

- Improved handling of expired records, memory constraints, and malformed fields.

### OpenSSL version on RHEL 9

On RHEL 9, Redis Software versions 8.0.16 through 8.0.20-68 require OpenSSL 3.3 or later. Version 8.0.20-96 and later are built against an earlier OpenSSL version, so the requirement no longer applies. Other supported platforms are unaffected.

The requirement exists because those versions are built against the OpenSSL 3.3 runtime included in recent RHEL 9 minor releases. Nodes on an earlier RHEL 9 minor release don't meet it. For example, RHEL 9.6 ships OpenSSL 3.2.2.

The pre-upgrade checks don't detect an incompatible OpenSSL version, so an upgrade can pass validation and then fail partway through. This can leave the management services on the node in a failed state.

Before you upgrade to a version between 8.0.16 and 8.0.20-68, check the OpenSSL version on each node:

```sh
openssl version
```

If the version is earlier than 3.3.0, either upgrade the `openssl` and `openssl-libs` packages first, or upgrade to Redis Software version 8.0.20-96 or later instead.

### Reserved ports

Make sure the following ports are open before upgrading Redis Software.

The following port was added as a reserved port in Redis Software version 8.0.18; however, it is optional instead of reserved in Redis Software version 8.0.20-44:

| Port | Process name | Usage |
|------|--------------|-------|
| 3357 | reconciliation_tree_grpc | Internal communication |

| Port | Process name | Usage | 
|------|--------------|-------|
| 3357 | reconciliation_tree_grpc | Internal communication |

Ports reserved as of Redis Software version 7.22.0:

| Port | Process name | Usage | 
|------|--------------|-------|
| 3346 | cluster_api_internal | Cluster API internal port |
| 3351 | cluster_watchdog_grpc_api | Cluster watchdog now supports gRPC |
| 3352 | grpc_service_mesh | gRPC communication between nodes |
| 3353 | local_grpc_service_mesh | Local gRPC services |
| 3354 | grpc_gossip_envoy | gRPC gossip protocol communication between nodes |
| 3355 | authentication_service | Authentication service internal port |

Ports reserved as of Redis Software version 7.8.2:

| Port | Process name | Usage | 
|------|--------------|-------|
| 3347 | cert_exporter | Reports cluster certificate metrics |
| 3348 | process_exporter | Reports process metrics for DMC and Redis processes |
| 3349 | cluster_wd_exporter | Reports cluster watchdog metrics |
| 3350 | db_controller | Internode communication |
| 9091 | node_exporter | Reports host node metrics related to CPU, memory, disk, and more |
| 9125 | statsd_exporter | Reports push metrics related to the DMC and syncer, and some cluster and node metrics |

See [Ports and port ranges used by Redis Software](https://redis.io/docs/latest/operate/rs/networking/port-configurations#ports-and-port-ranges-used-by-redis-software) for a complete list.

### Deprecations

#### API deprecations

- Deprecated the `policy` field for [bootstrap](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bootstrap) REST API requests. Use [`PUT /v1/cluster/policy`](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/cluster/policy#put-cluster-policy) to change cluster policies after cluster creation instead.

- Deprecated the `module_args` field for [database](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/bdbs) REST API requests. Use the new module configuration objects `search`, `timeseries`, and `probabilistic` instead.

- Deprecated `event_archive_cleanup_task_settings` for `job_scheduler` REST API requests.

#### Redis Search deprecations

- Deprecated commands: `FT.ADD`, `FT.SAFEADD`, `FT.DEL`, `FT.GET`, `FT.MGET`, `FT.SYNADD`, `FT.DROP`, `FT._DROPIFX`, and `FT.CONFIG`.

- Deprecated `FT.SEARCH` options: `GEOFILTER`, `FILTER`, and `NOSTOPWORDS`.

- Deprecated vector search options: `INITIAL_CAP` and `BLOCK_SIZE`.

- Deprecated configuration parameters: `WORKER_THREADS`, `MT_MODE`, `PRIVILEGED_THREADS_NUM`, and `GCSCANSIZE`.

- Deprecated dialects: `DIALECT 1`, `DIALECT 3`, and `DIALECT 4`.

#### Internal monitoring and v1 Prometheus metrics deprecation

The existing [internal monitoring engine](https://redis.io/docs/latest/operate/rs/monitoring/v1_monitoring) is deprecated. We recommend transitioning to the new [metrics stream engine](https://redis.io/docs/latest/operate/rs/monitoring/metrics_stream_engine) for improved performance, enhanced integration capabilities, and modernized metrics streaming.

V1 Prometheus metrics are deprecated but still available. To transition to the new metrics stream engine, either migrate your existing dashboards using [this guide](https://redis.io/docs/latest/operate/rs/references/metrics/prometheus-metrics-v1-to-v2) or use [new preconfigured dashboards](https://redis.io/docs/latest/integrate/prometheus-with-redis-enterprise#grafana-dashboards-for-redis-software).

As part of the transition to the metrics stream engine, some internal cluster manager alerts were deprecated in favor of external monitoring solutions. See the [alerts transition plan](https://redis.io/docs/latest/operate/rs/references/alerts/alerts-v1-to-v2) for guidance.

### Supported platforms

The following table provides a snapshot of supported platforms as of this Redis Software release. See the [supported platforms reference](https://redis.io/docs/latest/operate/rs/references/supported-platforms) for more details about operating system compatibility.

<span title="Check mark icon">&#x2705;</span> Supported – The platform is supported for this version of Redis Software and Redis Stack modules.

<span title="Warning icon" class="font-serif">:warning:</span> Deprecation warning – The platform is still supported for this version of Redis Software, but support will be removed in a future release.

| Redis Software<br />major versions | 8.0 | 7.22 | 7.8 | 7.4 | 7.2 | 6.4 | 6.2 |
|---------------------------------|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|:-----:|
| **Release date** | Oct 2025 | May 2025 | Nov 2024 | Feb 2024 | Aug 2023 | Feb 2023 | Aug 2021 |
| [**End-of-life date**](https://redis.io/docs/latest/operate/rs/installing-upgrading/product-lifecycle#endoflife-schedule) | Determined after<br />next major release | Oct 2027 | May 2027 | Nov 2026 | Feb 2026 | Aug 2025 | Feb 2025 |
| **Platforms** | | | | | | | |
| RHEL 9 &<br />compatible distros<sup>[1](#table-note-1)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | – | – | – |
| RHEL 9<br />FIPS mode<sup>[5](#table-note-5)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | – | – | – | – |
| RHEL 8 &<br />compatible distros<sup>[1](#table-note-1)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| RHEL 7 &<br />compatible distros<sup>[1](#table-note-1)</sup> | – | – | – | – | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> |
| Ubuntu 22.04<sup>[2](#table-note-2)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | – | – | – | – |
| Ubuntu 20.04<sup>[2](#table-note-2)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | – |
| Ubuntu 18.04<sup>[2](#table-note-2)</sup> | – | – | – | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> |
| Ubuntu 16.04<sup>[2](#table-note-2)</sup> | – | – | – | – | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> |
| Amazon Linux 2 | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | – |
| Amazon Linux 1 | – | – | – | – | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> | <span title="Deprecated" class="font-serif">:warning:</span> |
| Kubernetes<sup>[3](#table-note-3)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |
| Docker<sup>[4](#table-note-4)</sup> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> | <span title="Supported">&#x2705;</span> |

1. <a name="table-note-1"></a>The RHEL-compatible distributions CentOS, CentOS Stream, Alma, and Rocky are supported if they have full RHEL compatibility. Oracle Linux running the Red Hat Compatible Kernel (RHCK) is supported, but the Unbreakable Enterprise Kernel (UEK) is not supported.

2. <a name="table-note-2"></a>The server version of Ubuntu is recommended for production installations. The desktop version is only recommended for development deployments.

3. <a name="table-note-3"></a>See the [Redis Enterprise for Kubernetes documentation](https://redis.io/docs/latest/operate/kubernetes/reference/supported_k8s_distributions) for details about support per version and Kubernetes distribution.

4. <a name="table-note-4"></a>[Docker images](https://redis.io/docs/latest/operate/rs/installing-upgrading/quickstarts/docker-quickstart) of Redis Software are certified for development and testing only.

5. <a name="table-note-5"></a>Supported only if [FIPS was enabled during RHEL installation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening#proc_installing-the-system-with-fips-mode-enabled_switching-rhel-to-fips-mode) to ensure FIPS compliance.

## Known issues

- RS196225: After upgrading to Redis Software version 8.0.x, previously working LDAP filters that use an `OR` clause to match multiple attributes can fail to find a unique DN for some users.

    This issue is fixed in Redis Software version 8.0.20-68 and later.

- RS193156: Active Directory LDAP authentication can fail in the Cluster Manager UI after upgrading to Redis Software version 8.0.16-33 due to an issue with LDAP TLS client certificate handling. Users previously authenticated through Active Directory can no longer sign in to the Cluster Manager UI after the upgrade.

    As a workaround, configure an LDAP client certificate using an [update cluster certificates](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/cluster/certificates) REST API request:

    ```sh
    PUT https://<host>:<port>/v1/cluster/certificates
    {
      "certificates": [
        {
          "name": "ldap_client",
          "certificate": "<cert>",
          "key": "<key>"
        }
      ]
    }
    ```
    
    See [Create certificates](https://redis.io/docs/latest/operate/rs/security/certificates/create-certificates) and [Update certificates](https://redis.io/docs/latest/operate/rs/security/certificates/updating-certificates) for more detailed instructions.

    This issue was fixed in Redis Software version 8.0.18.

- RS180550: You cannot set up SSO when the Cluster Manager UI is exposed through an IPv6-based load balancer or gateway.

    As a workaround, use an IPv4-based address for the SSO service base address, or register a DNS name that resolves to the IPv6 address.

    This issue was fixed in Redis Software version 8.0.10.

- RS131972: Creating an ACL that contains a line break in the Cluster Manager UI can cause shard migration to fail due to ACL errors. This issue was fixed in Redis Software version 8.0.6.

- RS155734: Endpoint availability metrics do not work as expected due to a calculation error.

## Known limitations

#### Redis Search query failures during rolling upgrades across the 8.4 version boundary

Redis Search queries can fail during a rolling upgrade when a cluster contains shards running Redis versions earlier than 8.4 and shards running Redis version 8.4 or later, due to an internal protocol change introduced in version 8.4. This issue affects only clusters where `parallel_shards_upgrade` has been changed from its default value of `0`. If both conditions apply, expect Redis Search downtime until all nodes are upgraded.

#### Trim ACKED not supported for Active-Active 8.4 databases

For Active-Active databases running Redis database version 8.4, the `ACKED` option is not supported for trimming commands.

#### Rolling upgrade limitation for clusters with custom or deprecated modules

Due to module handling changes introduced in Redis Software version 8.0, upgrading a cluster that contains custom or deprecated modules, such as RedisGraph and RedisGears v2, can become stuck when adding a new node to the cluster during a rolling upgrade.

#### Module commands limitation during Active-Active database upgrades to Redis 8.0

When upgrading an Active-Active database to Redis version 8.0, you cannot use module commands until all Active-Active database instances have been upgraded. Currently, these commands are not blocked automatically.

#### Redis 8.0 database cannot be created with flash

You cannot create a Redis 8.0 database with flash storage enabled. Create a Redis 8.0 database with RAM-only storage instead, or use Redis 8.2 for flash-enabled (Redis Flex) databases.

#### New Cluster Manager UI limitations

The following legacy UI features are not yet available in the new Cluster Manager UI:

- Purge an Active-Active instance.

    Use [`crdb-cli crdb purge-instance`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/crdb-cli/crdb/purge-instance) instead.

- Search and export the log.

#### SCAN results can be inconsistent during a rolling upgrade in OSS Cluster API mode

During a rolling upgrade with Smart client handoffs (SCH) enabled, when some slot's shards have migrated to a different node but are still reachable from their original node, results of the `SCAN` command might be inconsistent: it might show some of the keys, it might show keys that are not reachable from that node, or it might show no keys. When the slot migration is done, this issue will fix itself.

