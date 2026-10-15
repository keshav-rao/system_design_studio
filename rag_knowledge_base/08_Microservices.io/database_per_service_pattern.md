# Database per Service Pattern

## Context
You are breaking a monolithic application down into microservices, or starting a new microservices-based system. 

## Problem
How do you structure your database architecture? If all microservices share a single monolithic database, they remain tightly coupled at the database level, preventing independent deployment, scaling, and schema evolution.

## Solution
Keep each microservice's persistent data private to that service and accessible only via its API. A service's database cannot be accessed directly by other services.

This can be implemented in a few ways:
*   **Private Tables-per-service:** Each service owns a set of tables that must only be accessed by that service.
*   **Schema-per-service:** Each service has a database schema that's private to that service.
*   **Database-server-per-service:** Each service has its own standalone database server.

## Consequences
*   **Benefits:** Ensures loose coupling. Services can be developed, deployed, and scaled independently. Different services can use different database technologies (Polyglot Persistence) best suited for their needs (e.g., Neo4j for a social graph, PostgreSQL for billing).
*   **Drawbacks:** Makes implementing business transactions that span multiple services highly complex (requires the **Saga** pattern). Makes implementing queries that join data across services complex (requires **API Composition** or **CQRS**).