# CAP Theorem and PACELC Trade-offs

## Overview
The CAP theorem (Brewer's theorem) states that any distributed data store can simultaneously provide at most two out of three guarantees:
- **Consistency (C)**: Every read receives the most recent write or an error.
- **Availability (A)**: Every non-failing node returns a non-error response for every request, without guarantee that it contains the most recent write.
- **Partition Tolerance (P)**: The system continues to operate despite an arbitrary number of messages being dropped or delayed by the network between nodes.

In any real-world distributed network, network partitions are inevitable. Therefore, a distributed system must choose between Consistency (CP) and Availability (AP) during a network partition.

## PACELC Theorem Extension
Daniel Abadi formulated PACELC to describe distributed trade-offs even when the network is running normally:
- If there is a **Partition (P)**, trade off **Availability (A)** vs **Consistency (C)**.
- **Else (E)**, trade off **Latency (L)** vs **Consistency (C)**.

### Common Categorizations
- **CP / PC/EC**: Google Spanner, Apache HBase, CockroachDB. Strong consistency at the expense of write latency during partitions.
- **AP / PA/EL**: Apache Cassandra, Amazon DynamoDB (with eventual consistency mode), CouchDB. High availability and ultra-low latency reads/writes.
- **Tunable Consistency**: MongoDB and Cassandra allow tuning `W` (write quorum) and `R` (read quorum) per request. When `R + W > N` (where N is the replica count), strong consistency is achieved.

## Architectural Guidelines
1. Financial ledgers and inventory balances demand CP systems with strict serializability.
2. Social media feeds, analytics counters, and swipe queues benefit from AP systems with eventual consistency.
