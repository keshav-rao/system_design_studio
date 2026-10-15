```json
{
  "topic": "capacity_planning",
  "component": "estimation_framework",
  "decision_type": "capacity_planning",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://github.com/donnemartin/system-design-primer#back-of-the-envelope-calculations",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# Back-of-the-Envelope Capacity Estimation Formulas and Rules of Thumb

## 1. Golden Constants for Mental Calculations

### 1.1 Time Conversions
- **Seconds per day**: $24 \times 60 \times 60 = 86,400\text{ seconds}$ (round to $\approx 100,000$ for quick mental estimations).
- **Seconds per month**: $\approx 2.5 \times 10^6\text{ seconds}$.
- **Seconds per year**: $\approx 3.15 \times 10^7\text{ seconds}$.
- **Mental Math Shortcut**:
  $$1\text{ million requests / day} \approx \frac{1,000,000}{86,400} \approx 11.6 \text{ requests / second (QPS)}$$
  $$10\text{ million requests / day} \approx 116 \text{ QPS}$$
  $$100\text{ million requests / day} \approx 1,160 \text{ QPS}$$
  $$1\text{ billion requests / day} \approx 11,600 \text{ QPS}$$

### 1.2 Binary Storage Units (Powers of 2)
| Power of 2 | Exact Decimal Value | Unit | Shorthand |
| :--- | :--- | :--- | :--- |
| $2^{10}$ | 1,024 bytes | 1 Kilobyte (KB) | $10^3$ bytes |
| $2^{20}$ | 1,048,576 bytes | 1 Megabyte (MB) | $10^6$ bytes |
| $2^{30}$ | 1,073,741,824 bytes | 1 Gigabyte (GB) | $10^9$ bytes |
| $2^{40}$ | 1,099,511,627,776 bytes | 1 Terabyte (TB) | $10^{12}$ bytes |
| $2^{50}$ | 1,125,899,906,842,624 bytes | 1 Petabyte (PB) | $10^{15}$ bytes |

---

## 2. Step-by-Step Capacity Estimation Framework

### Step 1: Queries Per Second (QPS)
$$\text{Average QPS} = \frac{\text{Daily Active Users (DAU)} \times \text{Requests per User / Day}}{86,400}$$
$$\text{Peak QPS} = \text{Average QPS} \times \text{Peak Multiplier (typically } 2\times \text{ to } 3\times)$$

*Example (Tinder-like App with 10M DAU)*:
- Swipes per user/day: 100
- Total swipes/day: $10\text{M} \times 100 = 1\text{ Billion swipes/day}$
- Average Swipe QPS: $\frac{1,000,000,000}{86,400} \approx 11,574\text{ QPS}$
- Peak Swipe QPS ($2.5\times$ during 8 PM–11 PM): $11,574 \times 2.5 \approx 28,935\text{ QPS}$

### Step 2: Storage Sizing (Daily & 5-Year Projections)
$$\text{Daily Ingestion} = \text{Daily Writes} \times \text{Average Record Payload Size}$$
$$\text{Storage Required (5 Years)} = \text{Daily Ingestion} \times 365 \times 5 \times \text{Replication Factor (typically } 3\times)$$

*Example*:
- Each swipe event payload: `{ swiper_id: UUID, target_id: UUID, action: byte, timestamp: int64 } \approx 100\text{ bytes}`
- With indexing and JSON/BSON overhead: $\approx 200\text{ bytes / record}$
- Daily storage: $1\text{ Billion} \times 200\text{ bytes} = 200\text{ GB / day}$
- 1-Year raw storage: $200\text{ GB} \times 365 \approx 73\text{ TB / year}$
- 5-Year storage with $3\times$ replication: $73\text{ TB} \times 5 \times 3 \approx 1,095\text{ TB} \approx 1.1\text{ Petabytes}$

### Step 3: Network Bandwidth Throughput
$$\text{Ingress Bandwidth} = \text{Peak Write QPS} \times \text{Average Request Payload Size}$$
$$\text{Egress Bandwidth} = \text{Peak Read QPS} \times \text{Average Response Payload Size}$$

*Example (Photo Profile Deck)*:
- Each profile view loads 3 compressed photos averaging 150 KB each = 450 KB total.
- Deck fetch rate: 2,000 deck requests/sec.
- Egress throughput: $2,000 \times 450\text{ KB} = 900,000\text{ KB/sec} = 900\text{ MB/sec} \approx 7.2\text{ Gbps}$.
- *Architectural Implication*: Requires direct CDN edge offloading. Pushing 7.2 Gbps directly through origin API servers would require 10+ large network-optimized instances and incur massive data transfer costs.
