# Transport Layer Security (TLS)

```json metadata
{
  "schema_version": 2,
  "title": "Transport Layer Security (TLS)",
  "description": "An overview of Transport Layer Security (TLS).",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"protocols-and-ciphers","title":"Protocols and ciphers"},{"id":"troubleshooting","title":"Troubleshooting"}]}

,
  "codeExamples": []
}
```

[Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security), a successor to SSL, ensures the privacy of data sent between applications and Redis databases. TLS also secures connections between Redis Software nodes.

You can [use TLS authentication](https://redis.io/docs/latest/operate/rs/security/encryption/tls/enable-tls) for the following types of communication:

- Communication from clients (applications) to your database
- Communication from your database to other clusters for replication using [Replica Of](https://redis.io/docs/latest/operate/rs/databases/import-export/replica-of)
- Communication to and from your database to other clusters for synchronization using [Active-Active](https://redis.io/docs/latest/operate/rs/databases/active-active)

## Protocols and ciphers

TLS protocols and ciphers define the overall suite of algorithms that clients are able to connect to the servers with.

You can change the [TLS protocols](https://redis.io/docs/latest/operate/rs/security/encryption/tls/tls-protocols) and [ciphers](https://redis.io/docs/latest/operate/rs/security/encryption/tls/ciphers) to improve the security of your Redis Software cluster and databases. The default settings are in line with industry best practices, but you can customize them to match the security policy of your organization.

## Troubleshooting

For help troubleshooting TLS failures, see the following knowledge base guides:

- [Troubleshooting TLS Failures](https://support.redislabs.com/hc/en-us/articles/26867190871314-Troubleshooting-TLS-Failures)

- [Troubleshooting TLS Connection Failures Caused by Certificate Expiration](https://support.redislabs.com/hc/en-us/articles/27021922067090-Troubleshooting-TLS-Connection-Failures-Caused-by-Certificate-Expiration)

