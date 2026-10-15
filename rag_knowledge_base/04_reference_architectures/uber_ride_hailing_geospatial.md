```json
{
  "topic": "reference_architecture",
  "component": "ride_hailing_and_dispatch",
  "decision_type": "reference_architecture",
  "content_type": "reference_architecture",
  "cloud_provider": "provider_neutral",
  "source_url": "https://www.uber.com/en-US/blog/engineering/",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# Reference Architecture: Geospatial Dispatch & Ride Hailing (Uber / Lyft Scale)

## 1. System Requirements & The Geospatial Problem
- **Scale**: 5 million active drivers emitting GPS pings every 4 seconds = 1.25 million writes/second.
- **Goal**: Rider requests a pickup at `(latitude, longitude)`. System must find the top 5 closest available drivers within a 3-mile radius, calculate ETA via road routing, and dispatch offers in < 2 seconds.

---

## 2. Geospatial Indexing: H3 Hexagonal Hierarchical Spatial Index

```
            / \
          /     \
         |   H3  |   <-- Hexagons have equal distance to all 6 neighbors!
         |  Cell |       Unlike square grids (where diagonal distance is √2 * edge),
          \     /        hexagonal grids provide uniform neighbor search.
            \ /
```

- **Uber H3 Algorithm**:
  - Partitions the globe into hexagonal cells across 16 resolution levels.
  - Resolution 8 (~460 meters across) or Resolution 9 (~174 meters across) is ideal for urban driver matching.
  - Every lat/long coordinate maps deterministically to a single 64-bit integer H3 Index: `h3_index = geo_to_h3(lat, lon, resolution=8)`.
- **Finding Neighbors**:
  - `k_ring(origin_cell, k=1)` returns the origin cell plus all 6 immediate surrounding neighbor cells in $O(1)$ computation without spherical trigonometry!

---

## 3. High-Throughput Write Path for Location Pings

- Writing 1.25 million GPS coordinates/sec directly to PostgreSQL or MySQL causes instant disk IOPS failure.
- **Solution: In-Memory Ring Buffer / Redis Cluster**:
  1. Driver app sends UDP/gRPC ping: `{ driver_id: 1234, lat: 37.7749, lon: -122.4194, heading: 90 }`.
  2. Location Ingestion Service converts to H3 index `8828308281fffff`.
  3. Updates Redis in-memory set: `SADD h3:8828308281fffff:drivers 1234` with a 10-second TTL.
  4. Geospatial state is kept purely volatile in RAM. If a driver crashes or loses cellular signal, their entry expires automatically without manual cleanup.
- **Dispatch Match Algorithm**:
  1. Rider requests pickup at H3 cell $C$.
  2. Dispatcher queries `k_ring(C, radius=2)` to fetch all candidate H3 cells.
  3. Executes `SUNION` across candidate cells to retrieve all available driver IDs.
  4. Calls Routing Engine for the top 5 candidates to compute real street-network ETAs.
  5. Dispatches ride offer to the closest driver via WebSocket push.
