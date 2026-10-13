# Content Delivery Networks (CDNs) and Edge Caching

## Global Edge Architecture (Cloudflare / CloudFront / Fastly)
A Content Delivery Network terminates TLS and serves static media (JavaScript bundles, images, CSS, video segments) from Points of Presence (PoPs) located physically close to end users.
- Reduces round-trip time (RTT) from $> 150\text{ ms}$ transcontinental to $< 10\text{–}20\text{ ms}$ at local edge nodes.
- Absorbs up to $90\text{–}98\%$ of bandwidth traffic before it ever touches origin cloud data centers.

## HTTP Cache-Control Directives
- `public, max-age=31536000, immutable`: Used for content-hashed assets (e.g. `main.a9f4c.js`). Never revalidated; cached in browser and CDN edge for 1 year.
- `s-maxage=3600, max-age=60`: `s-maxage` overrides public CDN edge TTL without affecting private browser cache TTL.
- `stale-while-revalidate=86400`: Instructs the edge to serve a stale cached response immediately while asynchronously fetching an updated version from the origin server in the background.

## Dynamic Acceleration and Edge Compute
- **Connection Optimization**: Edge terminates TCP 3-way handshake and TLS sessions near the client, utilizing persistent pre-warmed connection pools back to the origin server.
- **Edge Functions (Cloudflare Workers / Lambda@Edge)**: Execute lightweight logic (A/B testing, JWT verification, geolocation routing, image resizing) at edge PoPs in sub-5ms without routing back to central application servers.
