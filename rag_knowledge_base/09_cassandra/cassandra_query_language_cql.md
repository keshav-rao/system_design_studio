# Cassandra Query Language (CQL)

## Overview
CQL is the primary interface for communicating with Apache Cassandra. It is designed to be similar to SQL (Structured Query Language) to lower the learning curve, but it operates over a completely different underlying architecture.

## Hierarchy of Data
* **Keyspace:** The outermost container for data in Cassandra (similar to a schema in RDBMS). It defines the replication strategy and replication factor.
* **Table:** Contains the rows and columns.
* **Partition:** A subset of a table's data, grouped by the partition key and stored on a specific node.

## Key Differences from SQL
* **No JOINs:** Because data is distributed, joining tables across nodes is too expensive. You must denormalize data instead.
* **No Subqueries:** CQL does not support subqueries.
* **Filtering Limitations:** `WHERE` clauses are strictly limited. You generally can only filter on the Primary Key. Using `ALLOW FILTERING` on non-indexed, non-primary key columns is strongly discouraged in production as it scans the entire cluster.

## Example
```cql
CREATE KEYSPACE IF NOT EXISTS store WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3};
USE store;
CREATE TABLE users ( user_id uuid PRIMARY KEY, name text, email text );
INSERT INTO users (user_id, name, email) VALUES (uuid(), 'Alice', 'alice@example.com');
```