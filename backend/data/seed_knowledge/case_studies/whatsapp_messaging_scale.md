# Case Study: WhatsApp Messaging at Massive Scale

## Scale Characteristics
- 2+ billion active users, 100+ billion messages per day.
- Ultra-low latency delivery (< 100ms globally).
- End-to-end encryption (Signal Protocol).
- Minimal persistent server storage (messages deleted from servers immediately upon delivery confirmation).

## Architectural Pillars
1. **Erlang / BEAM Actor Model**:
   - Lightweight Erlang processes (actors) require only $\approx 2.5\text{ KB}$ memory per connection, allowing WhatsApp to sustain over 2 million concurrent TCP connections per FreeBSD/Linux server node.
2. **Ephemeral Message Pipeline**:
   - Server acts as an asynchronous store-and-forward relay.
   - Incoming message payload is encrypted client-side; server cannot read message content.
   - Message is queued in an in-memory or transient disk queue (Mnesia / local spool) until the recipient connects.
   - Once client device sends ACK (Double Grey Tick / Double Blue Tick), server drops message from queue permanently.
3. **Media Upload & Delivery**:
   - Media (images, videos, voice notes) is AES-256 encrypted on the sending device.
   - Ciphertext is uploaded to an HTTP object storage / CDN cluster.
   - Only the encrypted decryption key and media hash are transmitted over the chat channel.
   - Recipient downloads encrypted blob from CDN and decrypts locally on device.
