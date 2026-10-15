# Migrate to role-based LDAP

```json metadata
{
  "schema_version": 2,
  "title": "Migrate to role-based LDAP",
  "description": "Describes how to migrate existing cluster-based LDAP deployments to role-based LDAP.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"migration-checklist","title":"Migration checklist"},{"id":"test-ldap-access","title":"Test LDAP access"},{"id":"more-info","title":"More info"}]}

,
  "codeExamples": []
}
```


Redis Software supports LDAP through a [role-based mechanism](https://redis.io/docs/latest/operate/rs/security/access-control/ldap), first introduced [in v6.0.20](https://redis.io/docs/latest/operate/rs/release-notes/rs-6-0-20-april-2021).

Earlier versions of Redis Software supported a cluster-based mechanism; however, that mechanism was removed in v6.2.12.

If you're using the cluster-based mechanism to enable LDAP authentication, you need to migrate to the role-based mechanism before upgrading to Redis Software v6.2.12 or later.

## Migration checklist

This checklist covers the basic process:

1.  Identify accounts per app on the customer end.

1.  Create or identify an LDAP user account on the server that is responsible for LDAP authentication and authorization.

1.  Create or identify an LDAP group that contains the app team members.

1.  Verify or configure the Redis Software ACLs.

1.  Configure each database ACL.

1.  Remove the earlier "external" (LDAP) users from Redis Software.

1.  _(Recommended)_ Update cluster configuration to replace the cluster-based configuration file.

    You can use `rladmin` to update the cluster configuration:

    ``` bash
    $ touch /tmp/saslauthd_empty.conf
    $ rladmin cluster config saslauthd_ldap_conf \
         /tmp/saslauthd_empty.conf
    ```

    Here, a blank file replaces the earlier configuration.

1.  Use **Access Control > LDAP > Configuration** to enable role-based LDAP.

1.  Map your LDAP groups to access control roles.

1.  Test application connectivity using the LDAP credentials of an app team member.

1.  _(Recommended)_ Turn off default access for the database to avoid anonymous client connections.

 Because deployments and requirements vary, you’ll likely need to adjust these guidelines.

## Test LDAP access

To test your LDAP integration, you can:

- Connect with `redis-cli` and use the [`AUTH` command](https://redis.io/docs/latest/commands/auth) to test LDAP username/password credentials.

- Sign in to the Cluster Manager UI using LDAP credentials authorized for admin access.

- Use [Redis Insight](https://redis.io/docs/latest/develop/tools/insight) to access a database using authorized LDAP credentials.

- Use the [REST API](https://redis.io/docs/latest/operate/rs/references/rest-api) to connect using authorized LDAP credentials.

## More info

- Enable and configure [role-based LDAP](https://redis.io/docs/latest/operate/rs/security/access-control/ldap/enable-role-based-ldap)
- Map LDAP groups to [access control roles](https://redis.io/docs/latest/operate/rs/security/access-control/ldap/map-ldap-groups-to-roles)
- Update database ACLs to [authorize LDAP access](https://redis.io/docs/latest/operate/rs/security/access-control/ldap/update-database-acls)
- Learn more about Redis Software [security and practices](https://redis.io/docs/latest/operate/rs/security)

