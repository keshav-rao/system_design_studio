```json
{
  "topic": "reference_architecture",
  "component": "video_streaming_platform",
  "decision_type": "reference_architecture",
  "content_type": "reference_architecture",
  "cloud_provider": "provider_neutral",
  "source_url": "https://netflixtechblog.com/",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# Reference Architecture: Video Streaming Platform (Netflix / YouTube Scale)

## 1. High-Level Architecture
Video streaming architectures split cleanly into two distinct planes:
1. **The Control Plane (Cloud)**: User authentication, billing, search, recommendations, metadata management, and encoding pipelines (AWS / GCP).
2. **The Data Plane (Edge CDN)**: High-throughput video chunk delivery directly to smart TVs, mobile devices, and browsers via edge Open Connect appliances or commercial CDNs.

```
[Content Creator / Studio]
          │ (Raw 4K ProRes Video Upload ~500 GB)
          ▼
[Amazon S3 Raw Storage Bucket]
          │ (S3 Event Notification)
          ▼
[Distributed Transcoding Pipeline (AWS Batch / Fargate / GPU Workers)]
          ├── Chunking (Split into 2-second .ts / .m4s fragments)
          ├── Multi-bitrate encoding (H.264, HEVC, AV1: 240p up to 4K HDR)
          └── Manifest Generation (.mpd DASH / .m3u8 HLS)
          │
          ▼
[Origin S3 Static Video Bucket]
          │
          ▼
[Global Edge CDN (CloudFront / Fastly / Netflix Open Connect)]
          │ (HTTP GET range requests)
          ▼
   [Client Video Player]
 (ExoPlayer / AVPlayer with Adaptive Bitrate Streaming)
```

---

## 2. Adaptive Bitrate (ABR) Streaming
- Video files are never streamed as one massive 2-hour MP4 file.
- Instead, files are chunked into small, 2-to-6 second segments encoded across multiple resolutions and bitrates (e.g., 300 kbps for 360p, 2500 kbps for 1080p, 15000 kbps for 4K).
- The client player inspects its local network throughput and buffer fullness every few seconds:
  - If bandwidth drops, the player seamlessly requests the next 2-second chunk at 720p without buffering or playback interruption.
  - If bandwidth stabilizes, it steps back up to 4K.

---

## 3. Storage and CDN Caching Economics
- **80/20 Rule in Media**: 80% of video bandwidth comes from the top 5% of trending content.
- Pre-positioning: Popular new releases (e.g., Stranger Things) are pre-seeded to edge CDN caches overnight before release, preventing origin server collapse.
- Cold catalog videos remain in S3 Glacier/Standard and are fetched to CDN only on demand.
