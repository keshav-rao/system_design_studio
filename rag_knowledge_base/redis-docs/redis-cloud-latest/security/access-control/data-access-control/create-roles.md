# Assign permissions to roles

```json metadata
{
  "schema_version": 2,
  "title": "Assign permissions to roles",
  "description": "",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


To assign [Redis ACLs](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/configure-acls) to a data access role:

1. Go to **Data Access Control** from the [Redis Cloud console](https://cloud.redis.io/#/) menu.

    ![Menu for database access control.](https://redis.io/docs/latest/images/rc/data-access-control-menu.png)

1. Select the **Roles** tab.

    ![Role configuration area.](https://redis.io/docs/latest/images/rc/data-access-control-roles.png)

1. Select `+` to create a new role or point to an existing role and select the pencil icon to edit it.

    ![Add or edit a role.](https://redis.io/docs/latest/images/rc/data-access-control-roles-add-or-edit.png)

1. Enter a name for the role.

    ![Role add screen.](https://redis.io/docs/latest/images/rc/data-access-control-roles-add.png)

1. Select an **ACL rule** to assign to the role.

    ![Select an ACL Rule.](https://redis.io/docs/latest/images/rc/data-access-control-roles-select-acl.png)

1. Select one or more databases from the **Databases** list and click the check mark to confirm the association.

    ![Select databases.](https://redis.io/docs/latest/images/rc/data-access-control-roles-select-databases.png)

1. Select **Save role**.

When you assign a user-defined ACL rule to a role and associate it with one or more databases, we'll verify that the ACL rule will work with the selected databases. The database may go into an Inactive state for a few seconds while we verify the ACL rule.

After you create a role, you can assign it to a user. Users with this role can access the databases according to the role's associated Redis ACLs. For more information, see [Assign roles to users](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/create-assign-users#assign-roles-to-existing-users).

To assign Redis ACLs to a role for an [Active-Active database](https://redis.io/docs/latest/operate/rc/databases/active-active), see [Active-Active access roles](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/active-active-roles).

> [!NOTE]
> Applying ACLs to the database is an asynchronous operation. You may notice a delay before an ACL is fully applied to the database. 
