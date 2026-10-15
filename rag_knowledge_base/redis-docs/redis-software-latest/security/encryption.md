# Encryption in Redis Software

```json metadata
{
  "schema_version": 2,
  "title": "Encryption in Redis Software",
  "description": "Encryption in Redis Software.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"tls","title":"TLS"},{"id":"internode-encryption","title":"Internode encryption"},{"id":"require-https-for-rest-api-endpoints","title":"Require HTTPS for REST API endpoints"}],"id":"encrypt-data-in-transit","title":"Encrypt data in transit"},{"children":[{"id":"file-system-encryption","title":"File system encryption"},{"id":"private-key-encryption","title":"Private key encryption"}],"id":"encrypt-data-at-rest","title":"Encrypt data at rest"},{"children":[{"id":"client-side-encryption","title":"Client-side encryption"}],"id":"encrypt-data-in-use","title":"Encrypt data in use"}]}

,
  "codeExamples": []
}
```


Redis Software uses encryption to secure communications between clusters, nodes, databases, and clients and to protect [data in transit](https://en.wikipedia.org/wiki/Data_in_transit), [at rest](https://en.wikipedia.org/wiki/Data_at_rest), and [in use](https://en.wikipedia.org/wiki/Data_in_use).

## Encrypt data in transit

### TLS

Redis Software uses [Transport Layer Security (TLS)](https://redis.io/docs/latest/operate/rs/security/encryption/tls) to encrypt communications for the following:

- Cluster Manager UI

- Command-line utilities

- REST API

- Internode communication

You can also [enable TLS authentication](https://redis.io/docs/latest/operate/rs/security/encryption/tls/enable-tls) for the following:

- Communication from clients or applications to your database

- Communication from your database to other clusters for replication using [Replica Of](https://redis.io/docs/latest/operate/rs/databases/import-export/replica-of)

- Communication to and from your database to other clusters for [Active-Active](https://redis.io/docs/latest/operate/rs/databases/active-active) synchronization

### Internode encryption

[Internode encryption](https://redis.io/docs/latest/operate/rs/security/encryption/internode-encryption) uses TLS to encrypt data in transit between cluster nodes.

By default, internode encryption is enabled for the control plane, which manages the cluster and databases. If you also want to encrypt replication and proxy communications between database shards on different nodes, [enable data internode encryption](https://redis.io/docs/latest/operate/rs/security/encryption/internode-encryption#enable-data-internode-encryption).

### Require HTTPS for REST API endpoints

By default, the Redis Software API supports communication over HTTP and HTTPS. However, you can [turn off HTTP support](https://redis.io/docs/latest/operate/rs/references/rest-api/encryption) to ensure that API requests are encrypted.

## Encrypt data at rest

### File system encryption

To encrypt data stored on disk, use file system-based encryption capabilities available on Linux operating systems before you install Redis Software.

### Private key encryption

Enable PEM encryption to [encrypt all private keys](https://redis.io/docs/latest/operate/rs/security/encryption/pem-encryption) on disk.

## Encrypt data in use

### Client-side encryption

Use client-side encryption to encrypt the data an application stores in a Redis database. The application decrypts the data when it retrieves it from the database.

You can add client-side encryption logic to your application or use built-in client functions.

Client-side encryption has the following limitations:

- Operations that must operate on the data, such as increments, comparisons, and searches will not function properly.

- Increases management overhead.

- Reduces performance.

