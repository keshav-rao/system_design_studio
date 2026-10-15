```json
{
  "topic": "reference_architecture",
  "component": "notification_engine",
  "decision_type": "reference_architecture",
  "content_type": "reference_architecture",
  "cloud_provider": "provider_neutral",
  "source_url": "https://docs.aws.amazon.com/sns/latest/dg/welcome.html",
  "version": "1.0",
  "licence": "CC-BY-4.0",
  "last_verified": "2026-10-14"
}
```

# Reference Architecture: Multi-Channel Distributed Notification System

## 1. System Requirements & Challenges
- **Channels**: Mobile Push (APNs, Firebase FCM), SMS (Twilio), Email (SendGrid, AWS SES), Webhooks / In-App alerts.
- **Scale**: 100 million notifications/day.
- **Core Requirements**: Strict rate limiting per user (prevent spamming), user preference management (opt-out), priority queues (OTP verification vs. marketing promotions), and guaranteed idempotency.

---

## 2. Notification Pipeline Architecture

```
[Internal Services (Auth, Billing, Social)]
                    │
                    ▼
[Notification Ingress Service (Validates & Deduplicates)]
                    │
                    ▼
[Priority Message Queues (RabbitMQ / SQS)]
        ├── High Priority (OTP SMS, Fraud Alerts, Password Reset)
        ├── Medium Priority (Direct Messages, Matches, Order Updates)
        └── Low Priority (Marketing Newsletters, Weekly Digest)
                    │
                    ▼
      [Worker Fleet (Workers by Channel)]
        ├── Push Workers  ──> [Apple APNs / Google FCM HTTP/2 API]
        ├── SMS Workers   ──> [Twilio / AWS SNS API]
        └── Email Workers ──> [SendGrid / AWS SES API]
                    │
                    ▼
    [Notification Delivery Status & DLQ]
 (Dead Letter Queue + PostgreSQL Delivery History)
```

---

## 3. Critical Architectural Mechanisms

### 3.1 Idempotency and Deduplication
- Mobile networks experience frequent retries. A user must never receive the same OTP or charge notification twice.
- **Idempotency Key**: Sender attaches a deterministic hash:
  $$\text{idempotency\_key} = \text{SHA256}(\text{user\_id} + \text{event\_type} + \text{event\_id})$$
- Ingress worker executes `SET notification:idempotency:<key> 1 NX EX 86400` in Redis.
- If Redis returns nil (key already exists), the duplicate request is safely dropped.

### 3.2 User Frequency Capping & Quiet Hours
- Protects users from notification fatigue:
  - Max 3 marketing notifications per day per user.
  - Do not deliver marketing messages between 10:00 PM and 8:00 AM in user's local timezone.
- Check user preferences and rate limit counters in Redis before dispatching to delivery workers.
