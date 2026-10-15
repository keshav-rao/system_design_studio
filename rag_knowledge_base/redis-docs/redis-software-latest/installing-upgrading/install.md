# Install Redis Software

```json metadata
{
  "schema_version": 2,
  "title": "Install Redis Software",
  "description": "Install Redis Software on Linux.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"permissions-and-access","title":"Permissions and access"},{"id":"more-info-and-options","title":"More info and options"},{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": []
}
```


After you [plan your deployment](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment), [download a Redis Software installation package](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/prepare-install/download-install-package), and finish [installation preparation](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/prepare-install):

1. [Install the Redis Software package](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/install-on-linux) on one of the nodes in the cluster.

1. Repeat this process for each node in the cluster.

For installation on machines without an internet connection, see [Offline installation](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/offline-installation).

## Permissions and access

- Redis Software installation creates the `redislabs:redislabs` user and group. 

    Assigning other users to the `redislabs` group is optional. Users belonging to the `redislabs` group have permission to read and execute (e.g. use the `rladmin` status command) but are not allowed to write (or delete) files or directories.

- Redis Software is certified to run with permissions set to `750`, an industry standard.

    > [!WARNING]
    > Do not reduce permissions to `700`. This configuration has not been tested and is not supported.

- Redis Software requires `umask` to be `0022` during installation to correctly set permissions for the installed directories and files.

## More info and options

If you've already installed Redis Software, you can also:

- [Upgrade an existing deployment](https://redis.io/docs/latest/operate/rs/installing-upgrading/upgrading).

- [Uninstall an existing deployment](https://redis.io/docs/latest/operate/rs/installing-upgrading/uninstalling).

To learn more about customization and find answers to related questions, see:

- [CentOS/RHEL Firewall configuration](https://redis.io/docs/latest/operate/rs/installing-upgrading/configuring/centos-rhel-firewall)
- [Change socket file location](https://redis.io/docs/latest/operate/rs/installing-upgrading/configuring/change-location-socket-files)
- [Cluster DNS configuration](https://redis.io/docs/latest/operate/rs/networking/cluster-dns)
- [Cluster load balancer setup](https://redis.io/docs/latest/operate/rs/networking/cluster-lba-setup)
- [File locations](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/file-locations)
- [Supported platforms](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/supported-platforms)
- [Manage installation questions](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/manage-installation-questions)
- [mDNS client prerequisites](https://redis.io/docs/latest/operate/rs/networking/mdns)
- [User and group ownership](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/customize-user-and-group)

## Next steps

After your cluster is set up with nodes, you can:

- [Add users](https://redis.io/docs/latest/operate/rs/security/access-control/create-users) to the cluster with specific permissions.  To begin, start with [Access control](https://redis.io/docs/latest/operate/rs/security/access-control).
- [Create databases](https://redis.io/docs/latest/operate/rs/databases/create) to use with your applications.


