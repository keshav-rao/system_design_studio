# Manage default user

```json metadata
{
  "schema_version": 2,
  "title": "Manage default user",
  "description": "Manage a database's default user.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"authenticate-as-default-user","title":"Authenticate as default user"},{"id":"change-default-database-password","title":"Change default database password"},{"id":"deactivate-default-user","title":"Deactivate default user"}]}

,
  "codeExamples": []
}
```


When you [create a database](https://redis.io/docs/latest/operate/rs/databases/create), default user database access is enabled by default (**Unauthenticated access** is selected). This gives the default user full access to the database and enables compatibility with versions of Redis before Redis 6.

Select **Password-only authentication**, then enter and confirm a default database password to require authentication for connections to the database.

![Select Password-only authentication to require a password to access the database.](https://redis.io/docs/latest/images/rs/screenshots/databases/security-access-control-password-only.png)

## Authenticate as default user

When you configure a password for your database, all connections to the database must authenticate using the [AUTH](https://redis.io/docs/latest/commands/auth) command. See Redis security's [authentication](https://redis.io/docs/latest/operate/oss_and_stack/management/security#authentication) section for more information.

```sh
AUTH <default-database-password>
```

## Change default database password

To change the default user's password:

1. From the database's **Security** tab, select **Edit**.

1. In the **Access Control** section, select **Password-only authentication** as the **Access method**.

1. Enter and re-enter the new password.

1. Select **Save**.

## Deactivate default user

If you set up [role-based access control](https://redis.io/docs/latest/operate/rs/security/access-control) with [access control lists](https://redis.io/docs/latest/operate/rs/security/access-control/create-db-roles) (ACLs) for your database and don't require backwards compatibility with versions earlier than Redis 6, you can [deactivate the default user](https://redis.io/docs/latest/operate/rs/security/access-control/manage-users/default-user).

> [!WARNING]
> - Before you deactivate default user access, make sure the role associated with the database is [assigned to a user](https://redis.io/docs/latest/operate/rs/security/access-control/create-users). Otherwise, the database will be inaccessible.
>
> - If you enabled the default database password during the creation of an [Active-Active database](https://redis.io/docs/latest/operate/rs/databases/active-active), you should not turn off the default database password because it could prevent the removal of participating database instances.

To deactivate the default user:

1. From the database's **Security** tab, select **Edit**.

1. In the **Access Control** section, select **Using ACL only** as the **Access method**.

    ![Select Using ACL only to deactivate default user access to the database.](https://redis.io/docs/latest/images/rs/screenshots/databases/security-access-control-acl-only.png)

1. Choose at least one role and Redis ACL to access the database.

1. Select **Save**.

