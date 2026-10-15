# Security

```json metadata
{
  "schema_version": 2,
  "title": "Security",
  "description": "Configure security settings for Redis Software clusters and databases on Kubernetes.",
  "categories": ["docs","operate","kubernetes"],
  "tableOfContents": {"sections":[{"id":"access-control","title":"Access control"},{"id":"authentication","title":"Authentication"},{"id":"certificates-and-encryption","title":"Certificates and encryption"},{"id":"secret-management","title":"Secret management"},{"id":"resource-management","title":"Resource management"},{"id":"compliance","title":"Compliance"}]}

,
  "codeExamples": []
}
```


Configure security settings for Redis for Kubernetes. Security covers access control, cluster credentials, external identity providers, TLS certificates and encryption, and external secret management.

## Access control

- [Access control](https://redis.io/docs/latest/operate/kubernetes/security/access-control) — manage Redis Software users, roles, ACLs, and role bindings as Kubernetes custom resources.

## Authentication

- [Authentication](https://redis.io/docs/latest/operate/kubernetes/security/authentication) — manage cluster credentials, LDAP, SAML SSO, and configuration secrets.

## Certificates and encryption

- [Certificates and encryption](https://redis.io/docs/latest/operate/kubernetes/security/certificates) — provision TLS certificates, integrate cert-manager, add client certificates, and enable internode encryption.

## Secret management

- [HashiCorp Vault integration](https://redis.io/docs/latest/operate/kubernetes/security/vault) — use HashiCorp Vault as the centralized secret store for Redis for Kubernetes.

## Resource management

- [Allow resource adjustment](https://redis.io/docs/latest/operate/kubernetes/security/allow-resource-adjustment) — enable automatic adjustment of system resources for security compliance.

## Compliance

- [FIPS compliance](https://redis.io/docs/latest/operate/kubernetes/security/fips) — run your cluster in FIPS 140-3 compliance mode.

