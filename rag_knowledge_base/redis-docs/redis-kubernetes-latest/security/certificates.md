# Certificates and encryption

```json metadata
{
  "schema_version": 2,
  "title": "Certificates and encryption",
  "description": "Manage TLS certificates, client certificates, and internode encryption for Redis Software on Kubernetes.",
  "categories": ["docs","operate","kubernetes"],
  "tableOfContents": {"sections":[{"id":"how-certificates-work-on-redis-for-kubernetes","title":"How certificates work on Redis for Kubernetes"},{"id":"whats-the-same-as-redis-software","title":"What's the same as Redis Software"},{"id":"whats-different-on-kubernetes","title":"What's different on Kubernetes"},{"id":"in-this-section","title":"In this section"}]}

,
  "codeExamples": []
}
```


Certificates and encryption use Kubernetes Secrets and cert-manager integration to provision, distribute, and rotate the TLS certificates that Redis Software relies on. The operator distributes referenced certificates across every cluster node.

## How certificates work on Redis for Kubernetes

- **Cluster certificates** live in Kubernetes Secrets that the `RedisEnterpriseCluster` spec references. The operator distributes them to every cluster node.
- **cert-manager** can issue and rotate certificates automatically.
- **Client certificates** live in a Secret that the database references for mutual TLS authentication.
- **Internode encryption** is configured on the REC spec. The operator places the certificates on each node.

## What's the same as Redis Software

The underlying certificate roles, requirements, and TLS behavior are unchanged. For concepts and reference details, see the existing Redis Software docs:

- [Certificate roles and types](https://redis.io/docs/latest/operate/rs/security/certificates) — which certificate is used for what.
- [Create certificates](https://redis.io/docs/latest/operate/rs/security/certificates/create-certificates) — certificate requirements (SAN, CN, validity).
- [Update certificates](https://redis.io/docs/latest/operate/rs/security/certificates/updating-certificates) — rotation considerations on Redis Software.
- [Monitor certificates](https://redis.io/docs/latest/operate/rs/security/certificates/monitor-certificates) — certificate expiration alerts.
- [Client certificate authentication](https://redis.io/docs/latest/operate/rs/security/certificates/certificate-based-authentication) — how the cluster validates client certificates.
- [TLS protocols](https://redis.io/docs/latest/operate/rs/security/encryption/tls/tls-protocols) and [ciphers](https://redis.io/docs/latest/operate/rs/security/encryption/tls/ciphers) — protocol and cipher selection.
- [Enable TLS](https://redis.io/docs/latest/operate/rs/security/encryption/tls/enable-tls) — TLS for management, replication, and client connections.
- [Internode encryption](https://redis.io/docs/latest/operate/rs/security/encryption/internode-encryption) — purpose and scope.
- [PEM encryption](https://redis.io/docs/latest/operate/rs/security/encryption/pem-encryption) — encrypted private keys.

## What's different on Kubernetes

- **You capture certificates in Kubernetes Secrets and reference them declaratively in the REC spec.** The operator applies them to the cluster through the Redis Software REST API — the same way certificates are applied on Redis Software, cluster-wide rather than file-by-file on each node.
- **cert-manager can issue and rotate certificates automatically**, replacing manual rotation steps.

## In this section

- [Manage REC certificates](https://redis.io/docs/latest/operate/kubernetes/security/certificates/manage-rec-certificates) — configure cluster TLS certificates.
- [cert-manager integration](https://redis.io/docs/latest/operate/kubernetes/security/certificates/cert-manager) — automate certificate issuance and rotation with cert-manager.
- [Add client certificates](https://redis.io/docs/latest/operate/kubernetes/security/certificates/add-client-certificates) — enable client certificate authentication for databases.
- [Internode encryption](https://redis.io/docs/latest/operate/kubernetes/security/certificates/internode-encryption) — enable encryption between cluster nodes.

