# Database Connection Pool Sizing and Little's Law

## Little's Law in Request Processing
Little's Law defines the fundamental relationship in queuing theory:
$$L = \lambda \times W$$
where:
- $L$ = Average number of concurrent active requests in the system.
- $\lambda$ = Arrival rate (throughput in Requests Per Second, RPS).
- $W$ = Average processing time (latency per request in seconds).

### Calculation Example
If an API receives $10,000\text{ RPS}$ ($\lambda = 10,000$) and average database query duration is $10\text{ ms}$ ($W = 0.01\text{ s}$):
$$L = 10,000 \times 0.01 = 100\text{ concurrent database connections}.$$
If query latency spikes from $10\text{ ms}$ to $500\text{ ms}$ due to a missing table index:
$$L = 10,000 \times 0.5 = 5,000\text{ concurrent connections}.$$
The connection pool instantly exhausts, queueing requests and triggering cascading server 504 Gateway Timeouts.

## HikariCP / Database Pool Formula
The optimal pool size formula recommended by PostgreSQL and Oracle performance benchmarks:
$$\text{pool\_size} = 2 \times \text{CPU\_cores} + \text{effective\_spindle\_count}$$
- For modern multi-threaded NVMe SSDs, a pool of $20\text{–}50$ active connections per PostgreSQL instance can deliver peak throughput without incurring CPU context-switching degradation.
- Adding hundreds of unmanaged connections to a database degrades throughput; throttling concurrency via connection pools actually maximizes system performance.
