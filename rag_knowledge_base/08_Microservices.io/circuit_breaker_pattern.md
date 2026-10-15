# Circuit Breaker Pattern

## Context
In a microservices architecture, services often need to call other services synchronously. Because these services are running in different processes, there is always a risk that the downstream service is slow, unresponsive, or completely down.

## Problem
How do you prevent a network or service failure from cascading to other services? If one service blocks while waiting for a timeout from a failed downstream service, it consumes vital resources (like threads). This can bring down the calling service, creating a chain reaction.

## Solution
Invoke the remote service via a proxy that functions similarly to an electrical **Circuit Breaker**. 

The proxy monitors the number of consecutive failures (or slow responses). 
*   **Closed State:** If the failure rate is below a threshold, requests flow through normally.
*   **Open State:** If the failure rate crosses a threshold, the circuit breaker trips. All attempts to invoke the remote service fail immediately without actually making the network call. 
*   **Half-Open State:** After a timeout period, the circuit breaker allows a limited number of test requests to pass through. If those succeed, it closes the circuit. If they fail, it opens the circuit again.

## Consequences
*   **Benefits:** Improves system resilience. Prevents cascading failures. Allows services to fail fast and recover quickly, or serve fallback/cached data.
*   **Drawbacks:** Adds a layer of complexity to service calls. Requires careful tuning of timeout and failure threshold parameters.