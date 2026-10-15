# Managing Cassandra

## Overview
Managing an Apache Cassandra cluster involves monitoring node health, handling scaling operations, performing routine maintenance, and ensuring data consistency. 

## Key Operational Concepts

* **Nodetool:** The primary command-line utility used by administrators to manage a cluster. Common commands include `nodetool status` (check node health), `nodetool ring` (view token distribution), and `nodetool info`.
* **Compaction:** As data is continuously written to new SSTables, Cassandra periodically merges them in the background. This reclaims disk space by removing overwritten data and tombstones (deleted data markers) and improves read performance.
* **Repair:** Because Cassandra is a distributed system favoring high availability (AP in the CAP theorem), data can become out of sync between replicas (e.g., due to a node being down). Administrators must run anti-entropy repairs (`nodetool repair`) regularly to synchronize data across nodes.

## Scaling
Cassandra scales linearly. Adding capacity is as simple as bootstrapping new nodes into the cluster. The cluster automatically distributes the token ring and streams a portion of the existing data to the new nodes without downtime.

## Backup and Restore
* **Snapshots:** Administrators take point-in-time backups using `nodetool snapshot`, which creates hard links of the current SSTables on disk.
* **Commit Logs:** Incremental backups can be achieved by archiving commit logs alongside periodic snapshots.