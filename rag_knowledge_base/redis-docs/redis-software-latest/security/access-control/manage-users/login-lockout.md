# Manage user login

```json metadata
{
  "schema_version": 2,
  "title": "Manage user login",
  "description": "Manage user login lockout and session timeout.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"view-login-lockout-settings","title":"View login lockout settings"},{"id":"configure-user-login-lockout","title":"Configure user login lockout"},{"id":"change-allowed-login-attempts","title":"Change allowed login attempts"},{"id":"change-time-before-login-attempts-reset","title":"Change time before login attempts reset"},{"id":"change-login-lockout-duration","title":"Change login lockout duration"},{"id":"unlock-locked-user-accounts","title":"Unlock locked user accounts"},{"id":"turn-off-login-lockout","title":"Turn off login lockout"}],"id":"user-login-lockout","title":"User login lockout"},{"id":"configure-session-timeout","title":"Configure session timeout"}]}

,
  "codeExamples": []
}
```


Redis Software secures user access in a few different ways, including automatically:

- Locking user accounts after a series of authentication failures (invalid passwords)

- Signing sessions out after a period of inactivity

Here, you learn how to configure the relevant settings.

## User login lockout

By default, after 5 failed login attempts within 15 minutes, the user account is locked for 30 minutes. You can change the user login lockout settings in the Cluster Manager UI or with [`rladmin`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin).

### View login lockout settings

You can view the cluster's user login lockout settings from **Cluster > Security > Preferences > Lockout threshold** in the Cluster Manager UI or with [`rladmin info cluster`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/info#info-cluster):

```sh
$ rladmin info cluster | grep login_lockout
    login_lockout_counter_reset_after: 900
    login_lockout_duration: 1800
    login_lockout_threshold: 5
```

### Configure user login lockout

To change the user login lockout settings using the Cluster Manager UI:

1. Go to **Cluster > Security > Preferences**, then select **Edit**.

1. In the **Lockout threshold** section, make sure the checkbox is selected.

    ![The Lockout threshold configuration section](https://redis.io/docs/latest/images/rs/screenshots/cluster/security-preferences-lockout-threshold.png)

1. Configure the following **Lockout threshold** settings:

    1. **Log-in attempts until user is revoked** - The number of failed login attempts allowed before the user account is locked.

    1. **Time between failed login attempts** in seconds, minutes, or hours - The amount of time during which failed login attempts are counted.

    1. For **Unlock method**, select one of the following:

        - **Locked duration** to set how long the user account is locked after excessive failed login attempts.

        - **Only Admin can unlock the user by resetting the password**.

1. Select **Save**.

### Change allowed login attempts

To change the number of failed login attempts allowed before the user account is locked, use one of the following methods:

- [Cluster Manager UI](#configure-user-login-lockout)

- [`rladmin tune cluster`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/tune#tune-cluster):

    ```sh
    rladmin tune cluster login_lockout_threshold <integer>
    ```

    For example, to set the lockout threshold to 10 failed login attempts, run:

    ```sh
    rladmin tune cluster login_lockout_threshold 10
    ```

    If you set the lockout threshold to 0, it turns off account lockout, and the cluster settings show `login_lockout_threshold: disabled`.

    ```sh
    rladmin tune cluster login_lockout_threshold 0
    ```

### Change time before login attempts reset

To change the amount of time during which failed login attempts are counted, use one of the following methods:

- [Cluster Manager UI](#configure-user-login-lockout)

- [`rladmin tune cluster`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/tune#tune-cluster):

    ```sh
    rladmin tune cluster login_lockout_counter_reset_after <seconds>
    ```

    For example, to set the lockout reset to 1 hour, run:

    ```sh
    rladmin tune cluster login_lockout_counter_reset_after 3600
    ```

### Change login lockout duration

To change the amount of time that the user account is locked after excessive failed login attempts, use one of the following methods:

- [Cluster Manager UI](#configure-user-login-lockout)

- [`rladmin tune cluster`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/tune#tune-cluster):

    ```sh
    rladmin tune cluster login_lockout_duration <login_lockout_duration>
    ```

    For example, to set the lockout duration to 1 hour, run:

    ```sh
    rladmin tune cluster login_lockout_duration 3600
    ```

    If you set the lockout duration to 0, then the account can be unlocked only when an administrator changes the account's password.

    ```sh
    rladmin tune cluster login_lockout_duration 0
    ```

    The cluster settings now show `login_lockout_duration: admin-release`.

### Unlock locked user accounts

To unlock a locked user account as an admin, use one of the following methods:

**Cluster Manager UI:**

To unlock a user account in the Cluster Manager UI:

1. Go to **Access Control > Users**. Locked users have a "User is locked out" label:

   ![The Access Control > Users configuration screen in the Cluster Manager UI](https://redis.io/docs/latest/images/rs/screenshots/access-control/7-22-updates/users-locked-out.png)

1. Point to the "User is locked out" label, then click **Reset to unlock** when it appears:

   ![Reset to unlock button appears when you point to a locked user in the list](https://redis.io/docs/latest/images/rs/screenshots/access-control/7-22-updates/users-reset-to-unlock.png)

1. In the **Reset user password** dialog, enter a new password for the user:

   ![Reset user password dialog](https://redis.io/docs/latest/images/rs/screenshots/access-control/users-reset-user-password-dialog.png)

1. Select **Save** to reset the user's password and unlock their account.

**rladmin:**

To unlock a user account or reset a user password with `rladmin`, run the [`rladmin cluster reset_password`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/reset_password) command:

```sh
rladmin cluster reset_password <user_email>
```

**REST API:**

To unlock a user account or reset a user password with the REST API, use [`PUT /v1/users`](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/users#put-user):

```sh
PUT /v1/users
{"password": "<new_password>"}
```



### Turn off login lockout

To turn off user login lockout and allow unlimited login attempts, use one of the following methods:

**Cluster Manager UI:**

To turn off user login lockout using the Cluster Manager UI:

1. Go to **Cluster > Security > Preferences**, then select **Edit**.

1. Clear the **Lockout threshold** checkbox.

1. Select **Save**.

**rladmin:**

To turn off user login lockout using `rladmin`, run the [`rladmin tune cluster`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/tune#tune-cluster) command:

```sh
rladmin tune cluster login_lockout_threshold 0
```



The cluster settings show `login_lockout_threshold: disabled`.

## Configure session timeout

The Redis Software Cluster Manager UI supports session timeouts. By default, users are automatically logged out after 15 minutes of inactivity.

To customize the session timeout, use one of the following methods:

**Cluster Manager UI:**

To configure the session timeout using the Cluster Manager UI:

1. Go to **Cluster > Security > Preferences**, then select **Edit**.

1. For **Session timeout**, select minutes or hours from the list and enter the timeout value.

1. Select **Save**.

**rladmin:**

To configure the session timeout using `rladmin`, run the [`rladmin cluster config`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/config) command:

```sh
rladmin cluster config cm_session_timeout_minutes <number_of_min>
```

The `<number_of_min>` is the number of minutes after which sessions will time out.



