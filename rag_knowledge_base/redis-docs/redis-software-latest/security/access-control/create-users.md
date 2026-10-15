# Create users

```json metadata
{
  "schema_version": 2,
  "title": "Create users",
  "description": "Create users and assign access control roles.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"prerequisites","title":"Prerequisites"},{"id":"add-users","title":"Add users"},{"id":"assign-roles-to-users","title":"Assign roles to users"},{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": []
}
```


## Prerequisites

Before you create other users:

1. Review the [access control overview](https://redis.io/docs/latest/operate/rs/security/access-control) to learn how to use role-based access control (RBAC) to manage users' cluster access and database access.

1. Create roles you can assign to users. See [Create roles with cluster access only](https://redis.io/docs/latest/operate/rs/security/access-control/create-cluster-roles), [Create roles with database access only](https://redis.io/docs/latest/operate/rs/security/access-control/create-db-roles), or [Create roles with combined access](https://redis.io/docs/latest/operate/rs/security/access-control/create-combined-roles) for instructions.

## Add users

To add a user to the cluster:

1. From the **Access Control > Users** tab in the Cluster Manager UI, select **+ Add user**.

    ![The list of existing users on the Access Control > Users screen.](https://redis.io/docs/latest/images/rs/screenshots/access-control/7-22-updates/users-screen.png)

1. Enter the name, email, and password of the new user.

    > [!NOTE]
    > - Usernames must contain ASCII characters only.
    >
    > - To use [single sign-on (SSO)](https://redis.io/docs/latest/operate/rs/security/access-control/saml-sso), users must have email addresses.
    >     

    ![Create user panel with fields for username, email, password, and alerts.](https://redis.io/docs/latest/images/rs/screenshots/access-control/7-22-updates/create-user-panel.png)

1. Select the **Alerts** the user should receive by email:

    - **Receive alerts for databases** - The alerts that are enabled for the selected databases will be sent to the user. Choose **All databases** or **Customize** to select the individual databases to send alerts for.
    
    - **Receive cluster alerts** - The alerts that are enabled for the cluster in **Cluster > Alerts Settings** are sent to the user.

1. Click **Add permissions**.

1. Assign a **Role** to the user to grant permissions for cluster management and data access.

    ![Add role to new user.](https://redis.io/docs/latest/images/rs/screenshots/access-control/7-22-updates/create-user-role-select.png)

1. Click **Save user**.

## Assign roles to users

Assign a role, associated with specific databases and access control lists (ACLs), to a user to grant database access:

1. From the **Access Control > Users** tab in the Cluster Manager UI, select an existing user from the list of users.

1. Click the **Edit** button.

1. In the **User roles** section, click **Edit**.

    ![The User roles section of the Edit user panel.](https://redis.io/docs/latest/images/rs/screenshots/access-control/7-22-updates/edit-user-roles.png)

1. Select a role to assign to the user.

    ![Select role for user.](https://redis.io/docs/latest/images/rs/screenshots/access-control/7-22-updates/edit-user-select-role.png)

1. Click **Done** to close the **Roles** dialog.

1. Click **Save**.

## Next steps

Depending on the type of the user's assigned role (cluster management role or data access role), the user can now:

- [Connect to a database](https://redis.io/docs/latest/operate/rs/databases/connect) associated with the role and run limited Redis commands, depending on the role's Redis ACLs.

- Sign in to the Redis Software Cluster Manager UI.

- Make a [REST API](https://redis.io/docs/latest/operate/rs/references/rest-api) request.

