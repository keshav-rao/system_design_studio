# ACID vs BASE Consistency Models

## ACID Guarantees in Relational Systems
Traditional Relational Database Management Systems (PostgreSQL, MySQL, Oracle) prioritize ACID:
- **Atomicity**: All operations in a transaction succeed, or the entire transaction rolls back cleanly.
- **Consistency**: A transaction moves the database from one valid state satisfying all invariants (unique constraints, foreign keys) to another.
- **Isolation**: Concurrent transactions execute without cross-contamination. Isolation levels range from Read Uncommitted, Read Committed, Repeatable Read, to Serializable (via 2PL, MVCC, or SSI).
- **Durability**: Committed data survives system crashes via write-ahead logs (WAL) flushed to non-volatile storage.

## BASE Model in Distributed NoSQL
High-scale distributed systems frequently adopt BASE to maintain horizontal scalability and high availability:
- **Basically Available**: The system guarantees availability by decoupling components and tolerating localized node partitions.
- **Soft State**: System state may drift without user input due to ongoing background replication or gossip protocols.
- **Eventual Consistency**: Given no further updates, all replicas eventually converge to the identical value (convergence via Last-Write-Wins, CRDTs, or vector clocks).

## When to Choose Which
- **Choose ACID**: Order checkouts, account wallets, seat reservations, state machines where read-your-own-writes and conflict serialization are strictly mandatory.
- **Choose BASE**: Activity timelines, analytics logging, chat presence counters, messaging status receipts, metadata caches where momentary skew is acceptable.
