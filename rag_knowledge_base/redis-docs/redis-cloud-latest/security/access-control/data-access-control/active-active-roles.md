# Create roles for Active-Active databases

```json metadata
{
  "schema_version": 2,
  "title": "Create roles for Active-Active databases",
  "description": "",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


For [Active-Active databases](https://redis.io/docs/latest/operate/rc/databases/active-active), you can define roles with different levels of access for different regions. For example, you can define a user role with full database access in one region and read-only access in another. Or, you can prevent a user from running any commands in a specified region.

1. Go to **Data Access Control > Roles** and either select `+` to create a new role or point to an existing role and select the pencil icon to edit it.

    ![Add or edit a role.](https://redis.io/docs/latest/images/rc/data-access-control-roles-add-or-edit.png)

1. In the **Associations** section of the **Edit role** or **Create new role** screen, you can select `+` to create a new association or point to an existing association and select the pencil icon to edit it.

1. Select one or more Active-Active databases from the **Databases** list. Active-Active databases are marked with a globe icon.

    ![List of databases. Active-Active databases are marked with a globe icon.](https://redis.io/docs/latest/images/rc/roles-select-aa-database.png)

1. To set the role's default level of access to the selected databases, choose a **Redis ACL** from the list and select the check mark to confirm the association.

    > [!NOTE]
    > The default level of access to the selected database only applies to regions that exist when the role is created. If you add a new region to your Active-Active subscription, the new region will default to **No Access** for the role.
    >

1. Select the ACL name next to a region to change which ACL applies to that region.

    ![Assign different ACL rules for different regions.](https://redis.io/docs/latest/images/rc/roles-assign-rules-active-active.png)

    In addition to the ACL rules that are already configured, you can set a role to have **No-Access** in a region. This is a special rule that prevents a user with this role from running any commands when connecting to the database in that region.

1. Select **Save role**.

When you assign a user-defined ACL rule to a role and associate it with one or more databases, Redis will verify that the ACL rule will work with the selected databases. Verify that the [syntax](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/configure-acls#define-permissions-with-acl-syntax) of the ACL rule is correct if you receive an error.

After you create a role, you can assign it to a user. Users with this role can access the databases according to the role's associated Redis ACLs. For more information, see [Assign roles to users](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/create-assign-users#assign-roles-to-existing-users).

> [!NOTE]
> Applying ACLs to the database is an asynchronous operation. You may notice a delay before an ACL is fully applied to the database. 
