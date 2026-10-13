# Network Bandwidth and Cloud Egress Cost Capacity

## Bits vs Bytes Conversion Rule
Always convert between bits (network transit speed) and bytes (storage units) accurately:
- 1 Byte = 8 bits ($1\text{ B} = 8\text{ b}$).
- 100 Megabits per second ($100\text{ Mbps}$) $\approx 12.5\text{ Megabytes per second}$ ($12.5\text{ MB/s}$).
- 1 Gigabit per second ($1\text{ Gbps}$) $\approx 125\text{ MB/s} \approx 450\text{ GB/hour} \approx 10.8\text{ TB/day}$.

## Cloud Egress Cost Economics (AWS / GCP / Azure)
Data transfer into the cloud is free, but internet egress is one of the largest hidden drivers of cloud bills:
- Direct Internet Egress from Cloud Compute (EC2 / VM): $\approx \$0.08\text{–}\$0.09\text{ per GB}$.
- CDN Egress (CloudFront / Cloudflare): $\approx \$0.02\text{–}\$0.08\text{ per GB}$ (or flat-rate pricing on Cloudflare).
- Cross-Availability-Zone Transfer: $\approx \$0.01\text{–}\$0.02\text{ per GB}$ round-trip between microservices in different AZs.

### Offload Ratio Value
If an application streams 100 TB of images monthly:
- Without CDN: $100,000\text{ GB} \times \$0.09 = \$9,000/\text{month}$ egress cost, plus high compute server load.
- With 95% CDN Cache Hit Ratio: Only 5 TB hits cloud origin ($5,000 \times \$0.09 = \$450$), saving over $85\%$ on egress and eliminating origin server scaling spikes.
