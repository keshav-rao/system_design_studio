# Set password policies

```json metadata
{
  "schema_version": 2,
  "title": "Set password policies",
  "description": "Set password policies.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


Redis Software provides several ways to manage the passwords of local accounts, including:

- [Password complexity rules](https://redis.io/docs/latest/operate/rs/security/access-control/manage-passwords/password-complexity-rules)

- [Password expiration](https://redis.io/docs/latest/operate/rs/security/access-control/manage-passwords/password-expiration)

- [Password rotation](https://redis.io/docs/latest/operate/rs/security/access-control/manage-passwords/rotate-passwords)

You can also manage a user's ability to [sign in](https://redis.io/docs/latest/operate/rs/security/access-control/manage-users/login-lockout#user-login-lockout) and control [session timeout](https://redis.io/docs/latest/operate/rs/security/access-control/manage-users/login-lockout#session-timeout).

To enforce more advanced password policies, we recommend using [LDAP integration](https://redis.io/docs/latest/operate/rs/security/access-control/ldap) with an external identity provider, such as Active Directory.

> [!NOTE]
> Redis Software securely stores all user passwords using a cryptographic hash function. The default password hashing algorithm is `SHA-256`, but you can [change the password hashing algorithm](https://redis.io/docs/latest/operate/rs/security/access-control/manage-passwords/password-hashing-algorithm) to `PBKDF2` as of Redis Software version 7.8.6-13.

