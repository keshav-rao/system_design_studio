# Case Study: YouTube Distributed Video Ingestion and Delivery

## Ingestion and Transcoding Scale
- 500+ hours of video uploaded every minute.
- Videos range from seconds to multiple hours, requiring adaptive encoding into 10+ resolution and format variants (144p to 4K, H.264, VP9, AV1).

## Distributed Transcoding Pipeline
1. **Raw Upload**:
   - Client uploads raw video stream in 10–50 MB chunks via HTTP resumable upload protocol to Google Cloud Storage / Blob store.
2. **Chunked Split & MapReduce Transcoding**:
   - Splitting: Video is divided into short 2-to-5 second GoP (Group of Pictures) chunks at keyframe boundaries.
   - Workers: Thousands of worker nodes transcode independent GoP chunks concurrently in parallel (Map phase).
   - Stitching: Transcoded chunks are assembled and manifest playlists (`.m3u8` for HLS, `.mpd` for MPEG-DASH) are generated.
3. **Adaptive Bitrate Streaming (ABR)**:
   - Video player client continuously monitors downstream bandwidth and buffer health.
   - Seamlessly switches video quality between chunks (e.g. shifts down from 1080p to 720p when network degrades, without playback stalling).
4. **Metadata & Search Index**:
   - Video metadata (title, tags, channel, view count) stored in Bigtable / Spanner.
   - Search indexed in Google indexing infrastructure with real-time video recommendations based on deep neural network collaborative filtering.
