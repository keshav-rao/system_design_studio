# Redis Enterprise Software release notes 6.2.18

```json metadata
{
  "schema_version": 2,
  "title": "Redis Enterprise Software release notes 6.2.18",
  "description": "Database auditing. Private key encryption. Active-Active database support for MEMORY USAGE command.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"detailed-release-notes","title":"Detailed release notes"},{"children":[{"id":"active-active-database-persistence","title":"Active-Active database persistence"},{"id":"tls-10-and-tls-11","title":"TLS 1.0 and TLS 1.1"},{"id":"3des-encryption-cipher","title":"3DES encryption cipher"}],"id":"deprecations","title":"Deprecations"},{"children":[{"id":"feature-limitations","title":"Feature limitations"},{"id":"installation-limitations","title":"Installation limitations"},{"id":"upgrade-limitations","title":"Upgrade limitations"}],"id":"known-limitations","title":"Known limitations"}]}

,
  "codeExamples": []
}
```


> [!WARNING]
> Redis Software 6.2 reached end of life on February 28, 2025. It no longer
> receives security patches, bug fixes, or maintenance releases.
> Support for 6.2-specific issues is limited per your subscription agreement,
> and you may be asked to upgrade before an issue can be investigated.
>
> Upgrade to a supported version. Reaching the latest version may require an
> intermediate upgrade first — see the
> [supported upgrade paths](https://redis.io/docs/latest/operate/rs/references/upgrade-paths)
> and the [Redis Software product lifecycle](https://redis.io/docs/latest/operate/rs/installing-upgrading/product-lifecycle#endoflife-schedule).

[Redis Enterprise Software version 6.2.18](https://redislabs.com/redis-enterprise-software/download-center/software/) is now available! 

This version of Redis Enterprise Software offers:

- RedisJSON on Active-Active General Availability 
- Database connection auditing
- Private key encryption
- Active-Active support for `memory usage` command
- `crdb-cli` improvements
- Compatibility with open source Redis v6.2.6
- Additional enhancements and fixes

## Detailed release notes

For more detailed release notes, select a build version from the following table:


| Version (Release date) | Major changes | OSS Redis compatibility |
| --- | --- | --- |
| [6.2.18-70 (January 2023)](https://redis.io/docs/latest/operate/rs/release-notes/rs-6-2-18-releases/rs-6-2-18-70/) | New script to generate new self-signed certificates for renewal. Improved logs. Deactivate alert_mgr using rladmin. | Redis 6.2.6, 6.0 |
| [6.2.18-65 (December 2022)](https://redis.io/docs/latest/operate/rs/release-notes/rs-6-2-18-releases/rs-6-2-18-65/) | Added To field to test email server alerts. New flag to skip cluster resource validation during imports. Improved error messages. | Redis 6.2.6, 6.0 |
| [6.2.18-58 (November 2022)](https://redis.io/docs/latest/operate/rs/release-notes/rs-6-2-18-releases/rs-6-2-18-58/) | UI support for custom REST API port. Added info level for troubleshooting redis_mgr. | Redis 6.2.6, 6.0 |
| [6.2.18-49 (October 2022)](https://redis.io/docs/latest/operate/rs/release-notes/rs-6-2-18-releases/rs-6-2-18-49/) | New REST API endpoint to check whether a node is a primary or a replica. Added metrics to track certificate expiration time. | Redis 6.2.6, 6.0 |
| [6.2.18-43 (September 2022)](https://redis.io/docs/latest/operate/rs/release-notes/rs-6-2-18-releases/rs-6-2-18-43/) | Database auditing. Private key encryption. Active-Active database support for MEMORY USAGE command. Improvements to crdb-cli. | Redis 6.2.6, 6.0 |


## Deprecations

### Active-Active database persistence

The snapshot option for [data persistence on Active-Active databases](https://redis.io/docs/latest/operate/rs/databases/active-active/manage#data-persistence) will be deprecated in a future version of Redis Enterprise Software. If you have an Active-Active database using snapshot persistence, switch to AOF persistence. Use `crdb-cli` to do so:
```text
crdb-cli crdb update --crdb-guid <CRDB_GUID> --default-db-config '{"data_persistence": "aof", "aof_policy":"appendfsync-every-sec"}'
```

### TLS 1.0 and TLS 1.1 

TLS 1.0 and TLS 1.1 connections are considered deprecated in favor of TLS 1.2 or later.  

Please verify that all clients, apps, and connections support TLS 1.2.  Support for the earlier protocols will be removed in a future release.

Certain operating systems, such as RHEL 8, have removed support for the earlier protocols. Redis Enterprise Software does not support connection protocols that are not supported by the underlying operating system.

### 3DES encryption cipher

The 3DES encryption cipher is considered deprecated in favor of stronger ciphers like AES.

Please verify that all clients, apps, and connections support the AES cipher. Support for 3DES will be removed in a future release.

Certain operating systems, such as RHEL 8, have already removed support for 3DES. Redis Enterprise Software cannot support cipher suites that are not supported by the underlying operating system.

## Known limitations
    
### Feature limitations

- RS54131 Running the `QUIT` command on a TLS connected database closes connection and does not return a `+OK` reply

- An intermittent issue can occur where a CRDB process becomes stuck in a restart loop. If this issue occurs while upgrading to Redis Enterprise Software version 6.2.18, please upgrade to the latest version [6.4.2-69](https://redis.io/docs/latest/operate/rs/release-notes/rs-6-4-2-releases/rs-6-4-2-69) or [contact support](https://redis.com/company/support/).

- RS40641 - API requests are redirected to an internal IP in case the request arrives from a node which is not the master. To avoid this issue, use [`rladmin cluster config`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/config) to configure `handle_redirects` or `handle_metrics_redirects`.

- RS51144, RS102128 - Active-Active: To start successfully, the syncer (`crdt-syncer`) must connect to all sources. In multi-cluster configurations (more than 2 A-A clusters participating), in some cases, if one or more of the clusters is not available, A-A replication will be down.

### Installation limitations

Several Redis Enterprise Software installation reference files are installed to the directory `/etc/opt/redislabs/` even if you use [custom installation directories](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/customize-install-directories).

As a workaround to install Redis Enterprise Software without using any root directories, do the following before installing Redis Enterprise Software:

1. Create all custom, non-root directories you want to use with Redis Enterprise Software.

1. Mount `/etc/opt/redislabs` to one of the custom, non-root directories.

### Upgrade limitations

Before you upgrade a cluster that hosts Active-Active databases with modules to v6.2.18, perform the following steps:

1. Use `crdb-cli` to verify that the modules (`modules`) and their versions (in `module_list`) are as they appear in the database configuration and in the default database configuration:

    ```sh
    crdb-cli crdb get --crdb-guid <crdb-guid>
    ```

1. From the admin console's **redis modules** tab, validate that these modules with their specific versions are loaded to the cluster.

1. If one or more of the modules/versions are missing or if you need help, [contact Redis support](https://redis.com/company/support/) before taking additional steps.

