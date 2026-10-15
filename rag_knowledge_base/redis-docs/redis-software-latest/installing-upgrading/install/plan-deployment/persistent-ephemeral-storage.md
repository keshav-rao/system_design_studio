# Persistent and ephemeral node storage

```json metadata
{
  "schema_version": 2,
  "title": "Persistent and ephemeral node storage",
  "description": "Configure paths for persistent storage and ephemeral storage.",
  "categories": ["docs","operate","rs","kubernetes"],
  "tableOfContents": {"sections":[{"id":"persistent-storage","title":"Persistent storage"},{"id":"ephemeral-storage","title":"Ephemeral storage"},{"id":"disk-size-requirements","title":"Disk size requirements"}]}

,
  "codeExamples": []
}
```

For each node in the cluster, you can configure paths for both persistent
storage and ephemeral storage. To do so, the volume must have full permissions for user and group `redislabs` or users:group `redislabs:redislabs`. See the [Customize system user and group](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/customize-user-and-group) page for instructions.

> [!NOTE]
> The persistent storage and ephemeral storage discussed in this document are not related
> to Redis persistence or AWS ephemeral drives.

## Persistent storage

Persistent storage is mandatory. The cluster uses persistent storage to store
information that needs to persist if a shard or a node fails,
such as server logs, configurations, and files.

To set the frequency of syncs, you can configure [persistence](https://redis.io/docs/latest/operate/rs/databases/configure/database-persistence)
options for a database.
    
The persistent volume must be a storage area network (SAN)
using an EXT4 or XFS file system and be connected as an external storage volume.
NFS, NFS-like, and multi-read-write/shared storage options are not supported. These types of storage are often slow and can cause locking behaviors that are incompatible with the requirements of database storage.

When using append-only file (AOF) persistence, use flash-based storage
for the persistent volume.

## Ephemeral storage

Ephemeral storage is optional. If configured, temporary information that does not need to be persisted is stored by the cluster in the ephemeral storage.
This improves performance and helps reduce the load on the persistent storage.

Ephemeral storage must be a locally attached volume on each node.

## Disk size requirements

For disk size requirements, see:

- [Hardware
    requirements](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/hardware-requirements)
    for general guidelines regarding the ideal disk size for each type of
    storage.
- [Disk size requirements for extreme write
    scenarios](https://redis.io/docs/latest/operate/rs/clusters/optimize/disk-sizing-heavy-write-scenarios)
    for special considerations when dealing with a high rate of write
    commands.

