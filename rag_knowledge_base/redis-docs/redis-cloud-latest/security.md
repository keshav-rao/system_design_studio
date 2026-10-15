# Security

```json metadata
{
  "schema_version": 2,
  "title": "Security",
  "description": "",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"admin-console-security","title":"Redis Cloud console security"},{"id":"database-security","title":"Database security"},{"id":"api-security","title":"API security"},{"id":"continue-learning-with-redis-university","title":"Continue learning with Redis University"}]}

,
  "codeExamples": []
}
```


Redis Cloud provides a number of ways to secure subscriptions and databases.

As a Redis Cloud user, consider these security domains:

- The [Redis Cloud console](#admin-console-security)
- [Your databases](https://redis.io/docs/latest/operate/rc/security/database-security)
- The [Redis Cloud API](https://redis.io/docs/latest/operate/rc/api/get-started/enable-the-api)

First, you might want to review our [shared responsibility model](https://redis.io/docs/latest/operate/rc/security/shared-responsibility-model) for security.

## Redis Cloud console security {#admin-console-security}

The Redis Cloud console is the web application you use to manage your Redis Cloud deployments. 

Secure access to the Redis Cloud console by:

- Assigning appropriate roles to [team members with access](https://redis.io/docs/latest/operate/rc/security/access-control/access-management#team-management-roles).

- Enabling [multi-factor authentication](https://redis.io/docs/latest/operate/rc/security/access-control/multi-factor-authentication).

- Enabling [SAML SSO](https://redis.io/docs/latest/operate/rc/security/access-control/saml-sso).

> [!NOTE]
> A user session on Redis Cloud expires after 30 minutes. You'll be signed out of Redis Cloud after 30 minutes of inactivity.

## Database security

You have several options when it comes to securing your Redis Cloud databases. For more information, see [Cloud database security](https://redis.io/docs/latest/operate/rc/security/database-security). Options include:

- [Encryption at rest](https://redis.io/docs/latest/operate/rc/security/encryption-at-rest)
- [Role-based access control](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/role-based-access-control)
- [TLS](https://redis.io/docs/latest/operate/rc/security/database-security/tls-ssl)
- [Network security](https://redis.io/docs/latest/operate/rc/security/database-security/network-security) using
- [VPC peering](https://redis.io/docs/latest/operate/rc/security/vpc-peering) and [CIDR whitelist](https://redis.io/docs/latest/operate/rc/security/cidr-whitelist)

## API security

The Redis Cloud API allows you to programmatically administer your subscriptions and database deployments. This API is disabled by default. When you [enable the API](https://redis.io/docs/latest/operate/rc/api/get-started/enable-the-api), you can then [manage the API keys](https://redis.io/docs/latest/operate/rc/api/get-started/manage-api-keys) for all owners of your Redis Cloud account. For an overview of the security features of the API, see the [API authentication documentation](https://redis.io/docs/latest/operate/rc/api/get-started).

## Continue learning with Redis University


