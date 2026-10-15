# Create and edit database users

```json metadata
{
  "schema_version": 2,
  "title": "Create and edit database users",
  "description": "Create a database user and assign it a role.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"create-a-user","title":"Create a user"},{"id":"assign-roles-to-existing-users","title":"Assign roles to existing users"}]}

,
  "codeExamples": []
}
```


Before you create a database user, you must [create a data access role](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/create-roles) to assign to that user.

## Create a user

To create a user:

1. Go to **Data Access Control** from the [Redis Cloud console](https://cloud.redis.io/#/) menu.

    ![Menu for database access control.](https://redis.io/docs/latest/images/rc/data-access-control-menu.png)

1. Select the **Users** tab.

    ![User configuration area.](https://redis.io/docs/latest/images/rc/data-access-control-users-no-users.png)

2. Select `+` to create a new user.

    ![User add or edit.](https://redis.io/docs/latest/images/rc/data-access-control-users-add-or-edit.png)

3. Enter a username in the **Username** field.

    ![User add username.](https://redis.io/docs/latest/images/rc/data-access-control-users-add.png)

    > [!NOTE]
    > An error occurs if a user tries to connect to a memcached database with the username `admin`. Do not use `admin` for a username if the user will be connecting to a memcached database.
    >

1. Select a [**Role**](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/create-roles) from the list.

    ![User select role.](https://redis.io/docs/latest/images/rc/data-access-control-users-add-role.png)

1. Enter and confirm the user's password. ACL user passwords must be between 8 and 128 characters long.

    Then, select the check mark to save the user. 

    ![User add password and finish.](https://redis.io/docs/latest/images/rc/data-access-control-users-password-and-finish.png)


## Assign roles to existing users

To assign a data access role to an existing user:

1. Go to **Data Access Control** from the [Redis Cloud console](https://cloud.redis.io/#/) menu.

    ![Menu for database access control.](https://redis.io/docs/latest/images/rc/data-access-control-menu.png)

1. Select the **Users** tab.

    ![User configuration area.](https://redis.io/docs/latest/images/rc/data-access-control-users.png)

1. Point to the user and select the **Edit*** icon when it appears.

    ![User add or edit.](https://redis.io/docs/latest/images/rc/data-access-control-users-add-or-edit.png)

1. Select a [**Role**](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/create-roles) from the list.

    ![User select role.](https://redis.io/docs/latest/images/rc/data-access-control-users-add-role.png)

1. Select the check mark to save the user. 

    ![User add password and finish.](https://redis.io/docs/latest/images/rc/data-access-control-users-password-and-finish.png)
