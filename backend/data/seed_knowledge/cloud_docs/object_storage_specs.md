# Cloud Object Storage Specifications and Limits

## Architecture and Scalability (AWS S3 / GCS / Azure Blob)
Object storage systems are distributed, highly durable key-value stores designed for unstructured media (images, videos, backups, document attachments).
- **Durability Guarantee**: $99.999999999\%$ (11 nines) achieved via erasure coding across multiple availability zones.
- **Availability Target**: $99.9\%$ to $99.99\%$ SLA depending on storage tier.

## Throughput Limits and Partitioning
- **Per-Prefix Request Limits (Amazon S3)**:
  - 3,500 `PUT/COPY/POST/DELETE` requests per second per prefix.
  - 5,500 `GET/HEAD` requests per second per prefix.
  - There is no limit to the number of prefixes in a bucket. Distribute high-volume media across partitioned prefixes (e.g. `/media/user_123/`, `/media/user_456/`) to scale throughput horizontally to millions of RPS.

## Optimization Strategies
1. **Pre-Signed URLs**:
   - Clients obtain temporary cryptographically signed upload/download URLs directly from the application API.
   - Files upload and download directly between client and S3, bypassing backend application servers and eliminating bandwidth saturation.
2. **Multipart Uploads**:
   - Mandatory for objects $> 100\text{ MB}$, supported up to $5\text{ TB}$.
   - Chunks upload concurrently in parallel; failed chunks retry independently without restarting the entire file.
3. **Storage Tiers & Lifecycle Policies**:
   - Transition objects from Standard to Infrequent Access (IA) at 30 days, Glacier Flexible at 90 days, Glacier Deep Archive at 180 days to reduce storage spend by up to $85\%$.
