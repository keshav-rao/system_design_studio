```json
{
  "topic": "object_storage",
  "component": "s3_compatible_storage",
  "decision_type": "technology_selection",
  "content_type": "official_documentation",
  "cloud_provider": "provider_neutral",
  "source_url": "https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html",
  "version": "1.0",
  "licence": "Open-Documentation",
  "last_verified": "2026-10-14"
}
```

# Object Storage Decision Guide: Amazon S3 & Blob Storage Patterns

## 1. Storage Architecture Fundamentals

Object storage stores data as unstructured objects (composed of the file payload, a unique key, and customizable metadata) inside flat buckets, accessed via standard HTTP REST APIs (`GET`, `PUT`, `DELETE`).

### Comparison with Block and File Storage
| Dimension | Object Storage (S3, GCS, Blob) | Block Storage (EBS, Persistent Disk) | File Storage (EFS, NFS) |
| :--- | :--- | :--- | :--- |
| **Interface** | HTTP REST API (`/bucket/key`) | Block device via SCSI/NVMe (`/dev/xvdf`) | POSIX filesystem (`/mnt/share`) |
| **Max Capacity** | Virtually infinite per bucket | Fixed volume size (e.g., up to 64 TB) | Multi-petabyte elastic |
| **Latency** | 20–100 ms first-byte latency | Single-digit ms (sub-millisecond SSD) | 2–10 ms |
| **Modification** | Whole object overwrite (immutable) | In-place byte range mutation | In-place file modification |
| **Cost per GB/Mo** | ~$0.021–$0.023 / GB | ~$0.08–$0.12 / GB | ~$0.30 / GB |
| **Durability** | 99.999999999% (11 Nines) | 99.8% – 99.999% per volume | 99.999999999% (11 Nines) |

---

## 2. Production Patterns: Uploading Media at Scale

### 2.1 The Direct-Upload Anti-Pattern vs. Presigned URLs
- **Anti-Pattern**: Mobile app sends 20 MB image or 500 MB video directly to the backend application server. The backend buffers bytes in RAM and streams them to S3.
  - *Consequences*: Backend API servers burn precious CPU, memory, and bandwidth handling slow uploads; connection starvation locks web server threads.
- **Production Pattern: Presigned URLs / Direct Upload**:
  1. Client sends lightweight metadata request to API Gateway: `POST /api/v1/photos/presign { filename: "profile.jpg", size: 5242880 }`.
  2. API validates authentication, rate limits, and permissions, then generates a cryptographically signed HMAC URL with an expiration (e.g., 5 minutes):
     `https://my-bucket.s3.amazonaws.com/uploads/uuid.jpg?X-Amz-Signature=...`
  3. Client uploads file bytes directly from mobile device to S3 using HTTP `PUT`.
  4. S3 triggers an event (S3 Event Notification / SNS / SQS) notifying the backend worker service that upload is complete.
  5. Asynchronous worker processes image: generates thumbnails, runs NSFW safety checks, and updates user profile in database.

### 2.2 Multipart Uploads
- Required for files > 100 MB, recommended for files > 20 MB.
- Breaks file into chunks (5 MB to 5 GB each) and uploads parts in parallel.
- If network connection drops on chunk 14 of 20, client retries only chunk 14 without re-uploading the entire file.

---

## 3. Cost Optimization and Lifecycle Tiers
- **Standard Tier**: High frequency access (~$0.023/GB/mo).
- **Intelligent-Tiering**: Automatically moves objects between frequent, infrequent, and archive access tiers without operational overhead or retrieval fees.
- **Glacier Flexible / Deep Archive**: For long-term backups and compliance archives (~$0.00099/GB/mo = < $1/TB/mo). Retrieval latency: minutes to hours.
- **Data Transfer Egress Trap**: Putting data into S3 is free; transferring data *out* of AWS over the public internet costs ~$0.09/GB!
  - *Mitigation*: Always place a CDN (CloudFront) in front of S3. CloudFront data transfer out is discounted, and cached edge hits avoid S3 egress charges entirely.
