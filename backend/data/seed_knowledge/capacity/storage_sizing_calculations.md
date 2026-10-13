# Storage Sizing and Tiered Retention Modeling

## Data Lifecycle Tiers
Storage costs in cloud architecture vary by more than an order of magnitude across access tiers:
- **Hot Tier (In-Memory / Fast NVMe SSD)**: $0.10–$0.25 / GB / month. Sub-millisecond latency. Suitable for active working sets (last 7–30 days).
- **Warm Tier (Object Storage Standard)**: $0.02–$0.023 / GB / month. 10–50ms time-to-first-byte. Suitable for current-year media and relational snapshots.
- **Cold Tier (Infrequent Access / Glacier)**: $0.004–$0.0125 / GB / month. Retrieval fee applies. Suitable for 1–3 year compliance logs.
- **Deep Archive**: $0.00099 / GB / month ($1 / TB / month). 12-hour retrieval SLA. Suitable for regulatory backups.

## 80/20 Working Set Rule (Pareto Principle)
In social apps, media platforms, and e-commerce catalogs:
- $80\%$ of read traffic targets $20\%$ of the data (recent posts, trending items, active user profiles).
- If total database storage is $10\text{ TB}$, sizing the caching tier to hold $20\%$ of the data ($2\text{ TB}$ of RAM/Redis cluster) achieves an $\approx 80\text{–}90\%$ cache hit ratio, shielding the disk tier from overwhelming load.

## Replication Overhead Formula
Always multiply raw storage calculations by the durability and replication factor:
- Relational Primary + 2 Read Replicas: $3\times$ raw data size.
- Append-only WAL logs and daily retention snapshots: add $+20\text{–}30\%$ storage buffer.
- Elastic Block Storage (EBS) should always maintain at least $20\%$ unallocated headroom to avoid filesystem write freezes.
