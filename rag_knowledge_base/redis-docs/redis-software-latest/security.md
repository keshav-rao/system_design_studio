# Security

```json metadata
{
  "schema_version": 2,
  "title": "Security",
  "description": "",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"recommended-security-practices","title":"Recommended security practices"},{"id":"redis-trust-center","title":"Redis Trust Center"}]}

,
  "codeExamples": []
}
```


Redis Software provides various features to secure your deployment:

| Login and passwords | Users and roles | Encryption and TLS | Certificates and audit |
|---------------------|-----------------|--------------------|-----------------------|
| [Password attempts and session timeout](https://redis.io/docs/latest/operate/rs/security/access-control/manage-users/login-lockout) | [Cluster and database access explained](https://redis.io/docs/latest/operate/rs/security/access-control) | [Enable TLS](https://redis.io/docs/latest/operate/rs/security/encryption/tls/enable-tls) | [Create certificates](https://redis.io/docs/latest/operate/rs/security/certificates/create-certificates) |
| [Password complexity](https://redis.io/docs/latest/operate/rs/security/access-control/manage-passwords/password-complexity-rules) | [Create users](https://redis.io/docs/latest/operate/rs/security/access-control/create-users) | [Configure TLS protocols](https://redis.io/docs/latest/operate/rs/security/encryption/tls/tls-protocols) | [Monitor certificates](https://redis.io/docs/latest/operate/rs/security/certificates/monitor-certificates) |
| [Password expiration](https://redis.io/docs/latest/operate/rs/security/access-control/manage-passwords/password-expiration) | [Create roles](https://redis.io/docs/latest/operate/rs/security/access-control/create-combined-roles) | [Configure cipher suites](https://redis.io/docs/latest/operate/rs/security/encryption/tls/ciphers) | [Update certificates](https://redis.io/docs/latest/operate/rs/security/certificates/updating-certificates) |
| [Default database access](https://redis.io/docs/latest/operate/rs/security/access-control/manage-users/default-user) | [Redis ACLs](https://redis.io/docs/latest/operate/rs/security/access-control/redis-acl-overview) | [Encrypt private keys on disk](https://redis.io/docs/latest/operate/rs/security/encryption/pem-encryption) | [Enable OCSP stapling](https://redis.io/docs/latest/operate/rs/security/certificates/ocsp-stapling) |
| [Rotate user passwords](https://redis.io/docs/latest/operate/rs/security/access-control/manage-passwords/rotate-passwords) | [Integrate with LDAP](https://redis.io/docs/latest/operate/rs/security/access-control/ldap) | [Internode encryption](https://redis.io/docs/latest/operate/rs/security/encryption/internode-encryption) | [Audit database connections](https://redis.io/docs/latest/operate/rs/security/audit-events) |
| [Single sign-on (SSO)](https://redis.io/docs/latest/operate/rs/security/access-control/saml-sso) | | | |

## Recommended security practices

See [Recommended security practices](https://redis.io/docs/latest/operate/rs/security/recommended-security-practices) to learn how to protect Redis Software.

## Redis Trust Center

Visit our [Trust Center](https://trust.redis.io/) to learn more about Redis security policies. If you find a suspected security bug, you can [submit a report](https://hackerone.com/redis-vdp?type=team).

