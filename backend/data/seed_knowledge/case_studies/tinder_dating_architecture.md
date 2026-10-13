# Case Study: Tinder Dating App Real-Time Architecture

## System Requirements and Scale
- 50+ million Daily Active Users (DAU), 1.6 billion daily profile swipes.
- Low-latency geospatial discovery feed (profiles within radius $R$ km).
- Real-time mutual match notification (when User A likes User B and User B likes User A).
- Direct bi-directional messaging between matched users.

## Core Architectural Components
1. **Geospatial Discovery Engine**:
   - Geohash / S2 / Uber H3 spatial indexing.
   - User coordinates are mapped to grid cells. Active users are indexed into Redis geospatial (`GEOADD`, `GEORADIUS`) or Elasticsearch.
   - Recommendation pipeline pre-computes batches of prospective match candidates filtered by distance, age preference, and mutual attraction score, populating an in-memory swipe deck buffer.
2. **Swipe Pipeline & Match Engine**:
   - Client sends swipe: `POST /swipes {swiper_id, target_id, direction: 'LIKE'|'PASS'}`.
   - Swipes are ingested via Kafka or AWS SQS to buffer peak traffic spikes.
   - **Bidirectional Match Check**:
     - Check Redis Key: `EXISTS swipe:{target_id}:{swiper_id}`.
     - If exists and value is `LIKE`: Mutual Match!
     - Publish `MatchEvent` to Redis Pub/Sub and trigger real-time push notification via WebSocket / APNs / FCM.
     - Persist match relation in PostgreSQL or DynamoDB.
   - If not match: Save `SET swipe:{swiper_id}:{target_id} = LIKE EX 86400*30`.
3. **Chat and Ephemeral Presence**:
   - WebSocket gateway with Redis Pub/Sub cluster backplane.
   - Messages written to Cassandra/DynamoDB partitioned by `conversation_id`, ordered by timeuuid.
4. **Media Storage**:
   - Profile photos uploaded directly to S3 via pre-signed URLs.
   - CloudFront CDN edge cache with image resizing Lambda pipeline (thumbnail, card, full-res).
