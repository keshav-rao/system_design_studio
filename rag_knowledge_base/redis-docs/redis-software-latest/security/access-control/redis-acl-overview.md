# Overview of Redis ACLs in Redis Software

```json metadata
{
  "schema_version": 2,
  "title": "Overview of Redis ACLs in Redis Software",
  "description": "An overview of Redis ACLs, syntax, and ACL command support in Redis Software.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"predefined-redis-acls","title":"Predefined Redis ACLs"},{"children":[{"id":"commands-and-categories","title":"Commands and categories"},{"id":"key-patterns","title":"Key patterns"},{"id":"pubsub-channels","title":"Pub/sub channels"},{"id":"selectors","title":"Selectors"}],"id":"redis-acl-syntax","title":"Redis ACL syntax"},{"children":[{"id":"prepare-for-restrictive-pubsub-permissions","title":"Prepare for restrictive pub/sub permissions"},{"id":"change-default-pubsub-permissions","title":"Change default pub/sub permissions"}],"id":"default-pubsub-permissions","title":"Default pub/sub permissions"},{"id":"acl-command-support","title":"ACL command support"},{"id":"see-also","title":"See also"}]}

,
  "codeExamples": []
}
```


Redis access control lists (Redis ACLs) allow you to define named permissions for specific Redis commands, keys, and pub/sub channels. You can use defined Redis ACLs for multiple databases and roles.

## Predefined Redis ACLs

Redis Software provides one predefined Redis ACL named **Full Access**. This ACL allows all commands on all keys and cannot be edited.

## Redis ACL syntax

Redis ACLs are defined by a set of rules where you specify the commands or command categories that are allowed for specific keys.

### Commands and categories

Redis ACL rules can allow or block specific [Redis commands](/content/commands) or [command categories](https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl#command-categories).

- `+` includes commands

- `-` excludes commands

- `+@` includes command categories

- `-@` excludes command categories

The following example allows all `read` commands and the `SET` command:

```sh
+@read +SET
```

For database versions earlier than Redis 8.2, module commands have several ACL limitations:

- [Redis modules](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise) do not have command categories.

- Other [command category](https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl#command-categories) ACLs, such as `+@read` and `+@write`, do not include Redis module commands. `+@all` is the only exception because it allows all Redis commands.

- You have to include individual module commands in a Redis ACL rule to allow them.

    For example, the following Redis ACL rule allows read-only commands and the Redis Search commands `FT.INFO` and `FT.SEARCH`:

    ```sh
    +@read +FT.INFO +FT.SEARCH
    ```

### Key patterns

To define access to specific keys or key patterns, use the following prefixes:

- `~` or `%RW~` allows read and write access to keys.

- `%R~` allows read access to keys.

- `%W~` allows write access to keys.

`%RW~`, `%R~`, and `%W~` are only supported for databases with Redis version 7.2 or later.

The following example allows read and write access to all keys that start with "app1" and read-only access to all keys that start with "app2":

```sh
~app1* %R~app2*
```

### Pub/sub channels

The `&` prefix allows access to [pub/sub channels](https://redis.io/docs/latest/develop/pubsub) (only supported for databases with Redis version 6.2 or later).

To limit access to specific channels, include `resetchannels` before the allowed channels:

```sh
resetchannels &channel1 &channel2
```

### Selectors

[Selectors](https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl#selectors) let you define multiple sets of rules in a single Redis ACL (only supported for databases with Redis version 7.2 or later). A command is allowed if it matches the base rule or any selector in the Redis ACL.

- `(<rule set>)` creates a new selector.

- `clearselectors` deletes all existing selectors for a user. This action does not delete the base ACL rule.

In the following example, the base rule allows `GET key1` and the selector allows `SET key2`:

```sh
+GET ~key1 (+SET ~key2)
```

## Default pub/sub permissions

Redis database version 6.2 introduced pub/sub ACL rules that determine which [pub/sub channels](https://redis.io/docs/latest/develop/pubsub) a user can access.

The configuration option `acl-pubsub-default`, added in Redis Software version 6.4.2, determines the cluster-wide default level of access for all pub/sub channels. Redis Software uses the following pub/sub permissions by default:

- For versions 6.4.2 and 7.2, `acl-pubsub-default` is permissive (`allchannels` or `&*`) by default to accommodate earlier Redis versions.

- In future versions, `acl-pubsub-default` will change to restrictive (`resetchannels`). Restrictive permissions block all pub/sub channels by default, unless explicitly permitted by an ACL rule.

If you use ACLs and pub/sub channels, you should review your databases and ACL settings and plan to transition your cluster to restrictive pub/sub permissions in preparation for future Redis Software releases.

### Prepare for restrictive pub/sub permissions

To secure pub/sub channels and prepare your cluster for future Redis Software releases that default to restrictive pub/sub permissions:

1. Upgrade Redis databases:

    - For Redis Software version 6.4.2, upgrade all databases in the cluster to Redis DB version 6.2.
    
    - For Redis Software version 7.2, upgrade all databases in the cluster to Redis DB version 7.2 or 6.2.

1. Create or update ACLs with permissions for specific channels using the `resetchannels &channel` format.

1. Associate the ACLs with relevant databases.

1. Set default pub/sub permissions (`acl-pubsub-default`) to restrictive. See [Change default pub/sub permissions](#change-default-pubsub-permissions) for details.

1. If any issues occur, you can temporarily change the default pub/sub setting back to permissive. Resolve any problematic ACLs before making pub/sub permissions restrictive again.

> [!NOTE]
> When you change the cluster's default pub/sub permissions to restrictive, `&*` is added to the **Full Access** ACL. Before you make this change, consider the following:
>
> - Because pub/sub ACL syntax was added in Redis 6.2, you can't associate the **Full Access** ACL with database versions 6.0 or lower after this change.
>
> - The **Full Access** ACL is not reverted if you change `acl-pubsub-default` to permissive again.
>
> - Every database with the default user enabled uses the **Full Access** ACL.

### Change default pub/sub permissions

As of Redis Software version 6.4.2, you can configure `acl_pubsub_default`, which determines the default pub/sub permissions for all databases in the cluster. You can set `acl_pubsub_default` to the following values:

- `resetchannels` is restrictive and blocks access to all channels by default.

- `allchannels` is permissive and allows access to all channels by default. 

To make default pub/sub permissions restrictive:

1. [Upgrade all databases](https://redis.io/docs/latest/operate/rs/installing-upgrading/upgrading/upgrade-database) in the cluster to Redis version 6.2 or later.

1. Set the default to restrictive (`resetchannels`) using one of the following methods:

    **Cluster Manager UI:**

To set the default pub/sub permissions using the Cluster Manager UI:
    
1. Navigate to **Access Control > Roles > Pub/Sub ACLs** and click **Edit**.

1. Read the warning, then click **Continue**.
        
1. For **Default permissions for Pub/Sub ACLs**, select **Restrictive**, then **Save**.

**rladmin:**

To set the default pub/sub permissions using `rladmin`, run the [`rladmin tune cluster`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/tune#tune-cluster) command:

```sh
rladmin tune cluster acl_pubsub_default resetchannels
```

**REST API:**

To set the default pub/sub permissions using the REST API, use an [update cluster policy](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/cluster/policy#put-cluster-policy) request:

```sh
PUT /v1/cluster/policy
{ "acl_pubsub_default": "resetchannels" }
```



## ACL command support

Redis Software does not support certain Redis ACL commands. Instead, you can manage access controls from the Cluster Manager UI.

| Command | Supported |
|:--------|:----------|
| [ACL CAT](https://redis.io/docs/latest/commands/acl-cat) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> 
| [ACL DELUSER](https://redis.io/docs/latest/commands/acl-deluser) | <span title="Not supported">&#x274c; Not supported</span>| <span title="Not supported">&#x274c; Not supported</span>|  |
| [ACL DRYRUN](https://redis.io/docs/latest/commands/acl-dryrun) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> 
| [ACL GENPASS](https://redis.io/docs/latest/commands/acl-genpass) | <span title="Not supported">&#x274c; Not supported</span>| <span title="Not supported">&#x274c; Not supported</span>|  |
| [ACL GETUSER](https://redis.io/docs/latest/commands/acl-getuser) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> 
| [ACL HELP](https://redis.io/docs/latest/commands/acl-help) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> 
| [ACL LIST](https://redis.io/docs/latest/commands/acl-list) | <span title="Supported">&#x2705; Supported</span> | <span title="Supported">&#x2705; Supported</span> 
| [ACL LOAD](https://redis.io/docs/latest/commands/acl-load) | <span title="Not supported">&#x274c; Not supported</span>| <span title="Not supported">&#x274c; Not supported</span>|  |
| [ACL LOG](https://redis.io/docs/latest/commands/acl-log) | <span title="Not supported">&#x274c; Not supported</span>| <span title="Not supported">&#x274c; Not supported</span>|  |
| [ACL SAVE](https://redis.io/docs/latest/commands/acl-save) | <span title="Not supported">&#x274c; Not supported</span>| <span title="Not supported">&#x274c; Not supported</span>|  |
| [ACL SETUSER](https://redis.io/docs/latest/commands/acl-setuser) | <span title="Not supported">&#x274c; Not supported</span>| <span title="Not supported">&#x274c; Not supported</span>|  |
| [ACL USERS](https://redis.io/docs/latest/commands/acl-users) | <span title="Supported">&#x2705; Supported</span> |
| [ACL WHOAMI](https://redis.io/docs/latest/commands/acl-whoami) | <span title="Supported">&#x2705; Supported</span> |


Redis ACLs also have the following differences in Redis Software:

- The `MULTI`, `EXEC`, `DISCARD` commands are always allowed, but ACLs are enforced on `MULTI` subcommands.

- Nested selectors are not supported.

    For example, the following selectors are not valid in Redis Software: <nobr>`+GET ~key1 (+SET (+SET ~key2) ~key3)`</nobr>

- Key and pub/sub patterns do not allow the following characters: `'(', ')'`

- The following password configuration syntax is not supported: `'>', '<', '#!', 'resetpass'`

    To configure passwords in Redis Software, use one of the following methods:

    - [`rladmin cluster reset_password`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/reset_password):
    
        ```sh
        rladmin cluster reset_password <user email>
        ```

    - REST API [`PUT /v1/users`](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/users#put-user) request and provide `password`

## See also

[Redis ACL rules](https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl)

