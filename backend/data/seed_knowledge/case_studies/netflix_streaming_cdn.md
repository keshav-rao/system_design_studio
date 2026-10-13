# Case Study: Netflix Open Connect CDN and Playback Architecture

## Streaming Scale
- Over 250 million paid memberships globally, accounting for up to 15% of total downstream global internet traffic during peak evening hours.
- Requires buffer-free instant video startup and sub-second catalog navigation.

## Open Connect Custom Appliance Network
Instead of relying entirely on commercial public third-party CDNs (which would cost hundreds of millions annually in egress fees), Netflix engineered **Open Connect**:
- Custom hardware caching appliances (OCAs) deployed directly inside thousands of Internet Service Provider (ISP) data centers and Internet Exchange Points (IXPs) worldwide.
- Over 95% of Netflix streaming bits are served from an OCA physically located within the subscriber's local ISP network, with zero transit across the public internet backbone.

## Pre-Positioning and Nighttime Fill Algorithms
- User viewing patterns follow strict diurnal circadian cycles (peak between 8 PM and 11 PM; trough at 3 AM to 6 AM).
- **Predictive Pre-Caching**:
  - Machine learning algorithms predict localized show popularity per region and ISP.
  - During off-peak night hours, OCAs proactively download newly released seasons and trending movies from AWS S3 origins.
  - When users press play at 8 PM, the video chunks are already sitting on their local ISP OCA flash storage.

## AWS Cloud Control Plane vs Open Connect Data Plane
- **AWS Cloud**: Houses all user accounts, billing, recommendation engine, playback authorization tokens, and metadata APIs.
- **Open Connect**: Pure streaming data plane delivering audio and video chunk files directly to Netflix smart TV and mobile apps.
