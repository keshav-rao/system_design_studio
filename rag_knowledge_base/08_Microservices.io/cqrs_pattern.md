# CQRS (Command Query Responsibility Segregation)

## Context
You have applied the Database per Service pattern. Data is fragmented across multiple services, making it difficult to implement queries that join data from multiple services. 

## Problem
How do you implement a query that retrieves data from multiple services in a microservice architecture?

## Solution
Define a architecture that strictly segregates operations that update data (**Commands**) from operations that read data (**Queries**) by using the CQRS pattern. 

*   **Command Side:** Handles create, update, and delete operations. It processes business logic and updates the primary database.
*   **Query Side:** Handles read operations. It maintains one or more materialized views (often in separate, read-optimized databases like NoSQL document stores or search indexes) of the data. 

The Query side database is kept up to date by subscribing to Domain Events published by the Command side whenever data changes.

## Consequences
*   **Benefits:** Supports efficient querying in a microservices architecture. Enables independent scaling of read and write workloads. Allows optimization of the read schema.
*   **Drawbacks:** Increased architectural complexity. Eventual consistency between the write and read sides (the view might be slightly out of date).