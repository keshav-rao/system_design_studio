# Cassandra Data Modeling

## Overview
Data modeling in Cassandra is fundamentally different from relational databases. Instead of modeling around entities and relationships (normalization), you model around your application's queries (denormalization).

## Query-First Approach
In Cassandra, you must know your queries before you design your tables. A single query should ideally read from a single partition to ensure predictable performance. 

## Core Components
* **Primary Key:** Uniquely identifies a row and determines how data is distributed and sorted. It consists of two parts:
  * **Partition Key:** Determines which node stores the data. Essential for data distribution.
  * **Clustering Columns (Optional):** Determines how data is sorted physically on disk within that partition.

## Best Practices
1. **Spread Data Evenly:** Avoid hot spots by choosing a partition key that distributes data evenly across the cluster.
2. **Minimize Partitions Read:** Design tables so that a query only needs to read from one (or very few) partitions.
3. **Denormalize:** It is standard practice to duplicate data across multiple tables to satisfy different query access patterns. There are no `JOIN` operations in Cassandra.