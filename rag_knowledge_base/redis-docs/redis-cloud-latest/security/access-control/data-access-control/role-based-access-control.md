# Enable Role-based access control

```json metadata
{
  "schema_version": 2,
  "title": "Enable Role-based access control",
  "description": "Lets you define multiple users with fine-grained data authorization features.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"set-up-rbac","title":"Set up RBAC"},{"id":"redis-acls-vs-redis-cloud-rbac","title":"Redis ACLs vs. Redis Cloud RBAC"}]}

,
  "codeExamples": []
}
```


Role-based access control (RBAC) lets you define *roles* with specific sets of *permissions*. You can then assign *users* to these roles
to provide appropriate levels of access.

RBAC effectively lets you implement the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege). For example, you can provide
read-only access to an application whose only job is to display Redis data. Similarly, you can prevent new developers from running dangerous administrative commands.


## Set up RBAC

To set up RBAC, first navigate to the **Data Access Control** screen.

There are three tabs on this screen: **Users**, **Roles**, and **Redis ACLs**.

In the **Redis ACLs** tab, you [define named *permissions*](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/configure-acls) for specific Redis commands, keys, and pub/sub channels.

![Data access control screen.](https://redis.io/docs/latest/images/rc/data-access-control-acls.png)

In the **Roles** tab, you [create roles](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/create-roles). Each role consists of a set of permissions for one or more Redis Cloud databases.

![Data access control screen.](https://redis.io/docs/latest/images/rc/data-access-control-roles.png)

Finally, in the **Users** tab, you [create users](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/create-assign-users) and [assign each user a role](https://redis.io/docs/latest/operate/rc/security/access-control/data-access-control/create-assign-users#assign-roles-to-existing-users).

![Data access control screen.](https://redis.io/docs/latest/images/rc/data-access-control-users.png)

> [!NOTE]
> Database access users are different from account access users. To learn more, see [Access management](https://redis.io/docs/latest/operate/rc/security/access-control).


## Redis ACLs vs. Redis Cloud RBAC

In Redis, you can create users and assign ACLs to them using the `ACL` command. However, 
Redis does not support generic roles.

In Redis Cloud, you configure RBAC using the Redis Cloud console. As a result, certain Redis ACL
subcommands are not available in Redis Cloud. The following table shows which ACL commands are supported.

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


In Redis, you must explicitly provide access to the `MULTI`, `EXEC`, and `DISCARD` commands.
In Redis Cloud, these commands, which are used in transactions, are always permitted. However, the commands
run within the transaction block are subject to RBAC permissions.

When you run multi-key commands on multi-slot keys, the return value is `failure` but the command runs on the keys that are allowed.




