# Case Study: Uber Real-Time Geospatial Marketplace with H3

## Marketplace Requirements
- Hundreds of thousands of concurrent active drivers sending GPS pings every 4 seconds.
- Real-time location matching: pairing riders with nearby available drivers in $< 1\text{ second}$.
- Dynamic surge pricing dynamically calculated per micro-neighborhood.

## Geospatial Indexing with Uber H3 Hexagonal Grid
- **Why Hexagons instead of Squares (Geohash / S2)?**:
  - In a square grid, orthogonal neighbors have distance $1$, while diagonal neighbors have distance $\sqrt{2} \approx 1.414$.
  - In a regular hexagonal grid, all 6 adjacent neighbors are equidistant. This simplifies radius search, distance decay, and continuous spatial smoothing.
- **Hierarchical Resizing**:
  - H3 tessellates the entire planet into hierarchical hexagonal cells across 16 resolution levels.
  - Uber represents driver locations at Resolution 8 or 9 ($\approx 100\text{–}400\text{ meters}$ across).
  - Hexagon index is a 64-bit integer, making spatial lookups fast bitwise operations.

## Architecture Pipeline (DISCO - Dispatch Service)
1. **Location Ingestion**:
   - Drivers emit telemetry via WebSockets/gRPC to Location Gateway.
   - GPS coordinates mapped to H3 index.
   - Ephemeral driver state stored in in-memory geospatial cache (Ringpop / Redis Cluster).
2. **Dispatch Matching**:
   - Rider requests pickup at H3 cell $C$.
   - System queries cell $C$ and concentric rings of $k$-ring neighbor hexagons.
   - Filters candidate drivers by ETA, status, and vehicle tier.
   - Sends dispatch offer to selected driver with 15-second acceptance countdown.
