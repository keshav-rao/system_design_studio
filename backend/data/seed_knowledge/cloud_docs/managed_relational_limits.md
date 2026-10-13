# Managed Relational Database Limits and Connection Pooling

## Compute and Connection Bounds (AWS Aurora / Cloud SQL)
PostgreSQL and MySQL instances have strict concurrency and connection limits determined by available RAM and CPU cores:
- Each PostgreSQL connection forks a dedicated backend operating system process consuming $5\text{–}10\text{ MB}$ of memory.
- An instance with 16 GB RAM typically caps `max_connections` between 1,000 and 5,000.
- Attempting to handle thousands of concurrent application client threads directly against PostgreSQL causes context-switching thrashing and connection exhaustion errors (`FATAL: remaining connection slots are reserved`).

## Connection Pooling (PgBouncer / AWS RDS Proxy)
- **Transaction Pooling**: The proxy maintains a lean persistent connection pool to PostgreSQL (e.g. 50–100 actual database connections) while multiplexing tens of thousands of idle client microservice connections.
- Connections are leased to clients only for the active duration of an atomic transaction and returned to the pool immediately upon `COMMIT` or `ROLLBACK`.

## Storage and IOPS Limits
- **GP3 Storage**: Baseline 3,000 IOPS, 125 MB/s throughput; scalable up to 64,000 IOPS.
- **Io2 Block Storage**: Up to 256,000 IOPS for extreme OLTP requirements.
- **Read Replicas**: Aurora supports up to 15 auto-scaling read replicas sharing a single distributed storage layer with sub-10ms replication lag. Route analytical read queries and read-heavy API traffic to replicas using separate read/write endpoints.
