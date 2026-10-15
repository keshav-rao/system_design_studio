# Apache Cassandra Architecture

## Overview
Apache Cassandra is a highly scalable, high-performance distributed database designed to handle large amounts of data across many commodity servers, providing high availability with no single point of failure.

## Core Concepts
* **Peer-to-Peer Architecture:** Unlike master-slave systems, all nodes in a Cassandra cluster are peers. There is no central coordinator, which eliminates single points of failure.
* **Gossip Protocol:** Nodes communicate with each other using a peer-to-peer gossip protocol to exchange information about the cluster state and node availability.
* **Partitioner:** Determines which node receives which data by using a hash of the partition key.
* **Replication Factor (RF):** Determines how many copies of the data are stored across the cluster to ensure fault tolerance.

## Write and Read Paths
* **Write Path:** Data is first written to a commit log (for durability) and then to an in-memory structure called a Memtable. When the Memtable is full, it is flushed to disk as an Immutable SSTable (Sorted String Table).
* **Read Path:** Cassandra reads data from the Memtable first. If the data is not found, it checks Bloom Filters and partition keys to locate the relevant SSTables on disk, merging the results before returning them to the client.