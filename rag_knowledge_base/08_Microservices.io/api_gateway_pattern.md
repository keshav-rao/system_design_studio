# API Gateway Pattern

## Context
You are building an application with a microservice architecture. You have multiple distinct client apps (e.g., web browser, native mobile app, third-party consumers).

## Problem
How do the clients of a microservices-based application access the individual services? If clients call services directly, it leads to tight coupling, too many round trips, and security concerns.

## Solution
Implement an **API Gateway** that acts as a single entry point for all clients. The API Gateway handles requests in one of two ways:
1.  **Routing/Proxying:** Some requests are simply routed/proxied to the appropriate service.
2.  **API Composition:** Other requests are fanned out to multiple services, and the API gateway aggregates the results into a single response for the client.

The API Gateway is also responsible for cross-cutting concerns like:
*   Authentication and Authorization
*   Rate limiting and throttling
*   Load balancing
*   Protocol translation (e.g., from public HTTP/REST to internal gRPC)

## Consequences
*   **Benefits:** Insulates clients from how the application is partitioned into microservices. Reduces the number of round trips between the client and the application. Simplifies the client code.
*   **Drawbacks:** The API Gateway is a highly available component that must be developed, deployed, and managed. It can become a development bottleneck if not managed properly (e.g., using the "Backends for Frontends" pattern to split it up).