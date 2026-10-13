# Back-of-the-Envelope Capacity Estimation

## Core Conversion Constants
- Seconds in a day: $24 \times 3600 \approx 86,400 \approx 10^5\text{ seconds}$ (useful approximation: $1\text{ request/sec} \approx 100,000\text{ requests/day}$).
- $10^6\text{ requests/day} \approx 12\text{ requests/sec}$ (QPS).
- $10^9\text{ requests/day} \approx 12,000\text{ QPS}$.
- Peak traffic multiplier: typically $2\times$ to $5\times$ average QPS.

## Power of Two Data Units
- $2^{10} = 1,024 \approx 1\text{ KB}$ ($10^3$)
- $2^{20} = 1,048,576 \approx 1\text{ MB}$ ($10^6$)
- $2^{30} = 1,073,741,824 \approx 1\text{ GB}$ ($10^9$)
- $2^{40} \approx 1\text{ TB}$ ($10^{12}$)
- $2^{50} \approx 1\text{ PB}$ ($10^{15}$)

## Step-by-Step Capacity Calculation Workflow
1. **Traffic Sizing (QPS)**:
   - Given: 50 million Daily Active Users (DAU), each performing 20 read actions and 2 write actions per day.
   - Total reads per day: $50\text{M} \times 20 = 1\text{ billion reads/day}$.
   - Average Read QPS: $10^9 / 86,400 \approx 11,600\text{ QPS}$.
   - Peak Read QPS ($2\times$ factor): $\approx 23,200\text{ QPS}$.
   - Total writes per day: $50\text{M} \times 2 = 100\text{ million writes/day}$.
   - Average Write QPS: $10^8 / 86,400 \approx 1,160\text{ QPS}$.
2. **Storage Accumulation**:
   - Given: Each write produces 500 bytes of structured metadata and 200 KB image.
   - Daily metadata: $10^8 \times 500\text{ B} = 50\text{ GB/day}$.
   - Annual metadata: $50\text{ GB} \times 365 \approx 18.25\text{ TB/year}$.
   - Daily media: $10^8 \times 200\text{ KB} = 20\text{ TB/day}$.
   - Annual media: $20\text{ TB} \times 365 \approx 7.3\text{ PB/year}$.
3. **Bandwidth Sizing**:
   - Daily incoming traffic: $20\text{ TB/day} / 86,400\text{s} \approx 231\text{ MB/s} \approx 1.85\text{ Gbps}$.
   - Outgoing traffic (assuming read:write ratio of 10:1): $18.5\text{ Gbps}$ egress.
