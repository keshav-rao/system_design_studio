# Data access control

```json metadata
{
  "schema_version": 2,
  "title": "Data access control",
  "description": "Control who can access your databases using the default user database password and role-based access control.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"default-user","title":"Default user"},{"id":"role-based-access-control","title":"Role-based access control"}]}

,
  "codeExamples": []
}
```


## Default user

When you create a Redis Cloud database, your database is given a randomly generated password called the [**Default user password**](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/default-user). Learn how to [change the default user password](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/default-user#change-password) or [turn off default user access](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/default-user#turn-off-default-user).

## Role-based access control

With [role-based access control (RBAC)](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/role-based-access-control), you create roles and assign users to those roles to grant different levels of access to the database.

- [Enable RBAC](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/role-based-access-control)
- [Configure ACLs](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/configure-acls)
- [Create roles](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/create-roles)
- [Create and edit database users](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/create-assign-users)
- [Active-Active roles](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/active-active-roles)
