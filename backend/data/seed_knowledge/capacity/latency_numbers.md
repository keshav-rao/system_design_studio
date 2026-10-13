# Latency Numbers Every Systems Engineer Should Know

## Standard Hardware Latency Hierarchy
Compiled by Peter Norvig and Jeff Dean, these order-of-magnitude numbers provide the foundation for system design capacity calculations:

| Operation | Latency (ns) | Human Equivalent (scaled to 1s = L1 ref) |
|---|---|---|
| L1 cache reference | 0.5 ns | 1 second |
| Branch mispredict | 5 ns | 10 seconds |
| L2 cache reference | 7 ns | 14 seconds |
| Mutex lock/unlock | 25 ns | 50 seconds |
| Main memory (RAM) reference | 100 ns | 3.3 minutes |
| Compress 1 KB with Snappy | 2,000 ns (2 µs) | 1 hour |
| Send 1 KB over 1 Gbps network | 10,000 ns (10 µs) | 5.5 hours |
| Read 1 MB sequentially from RAM | 250,000 ns (250 µs) | 5.7 days |
| Round trip within same datacenter | 500,000 ns (500 µs) | 11.5 days |
| Read 1 MB sequentially from NVMe SSD | 1,000,000 ns (1 ms) | 23 days |
| Disk seek (spinning platter) | 10,000,000 ns (10 ms) | 7.6 months |
| Read 1 MB sequentially from HDD | 20,000,000 ns (20 ms) | 1.3 years |
| Send packet California to Netherlands | 150,000,000 ns (150 ms) | 9.5 years |

## Practical Architectural Implications
1. **Memory vs Disk**: Reading from RAM is $\approx 10,000\times$ faster than spinning disk seeks and $\approx 10\times$ faster than NVMe SSDs.
2. **Sequential vs Random I/O**: Sequential reads are orders of magnitude faster than random seeks on all mediums. Append-only write logs (WAL / Kafka / LSM trees) maximize sequential throughput.
3. **Datacenter Latency vs Cross-Continent**: A network hop within the same availability zone is $< 0.5\text{ ms}$, while cross-continent round-trips take $100\text{–}150\text{ ms}$. Distributed transactions spanning regions must minimize synchronous round-trips.
