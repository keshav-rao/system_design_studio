# Install, set up, and upgrade Redis Software

```json metadata
{
  "schema_version": 2,
  "title": "Install, set up, and upgrade Redis Software",
  "description": "Learn how to install, set up, and upgrade Redis Software.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"quickstarts","title":"Quickstarts"},{"id":"install-redis-software","title":"Install Redis Software"},{"id":"upgrade-existing-deployment","title":"Upgrade existing deployment"},{"id":"install-and-upgrade-modules","title":"Install and upgrade modules"},{"id":"uninstall-redis-software","title":"Uninstall Redis Software"},{"id":"more-info-and-options","title":"More info and options"},{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": []
}
```


You can run self-managed Redis Software in an on-premises data center or on your preferred cloud platform. 

If you prefer a fully managed Redis database-as-a-service, available on major public cloud services, consider setting up a [Redis Cloud](https://redis.io/docs/latest/operate/rc) subscription. You can [try Redis Cloud](https://redis.io/try-free/) for free.

## Quickstarts

If you want to try out Redis Software, see the following quickstarts:

- [Redis Software quickstart](https://redis.io/docs/latest/operate/rs/installing-upgrading/quickstarts/redis-enterprise-software-quickstart)

- [Docker quickstart for Redis Software](https://redis.io/docs/latest/operate/rs/installing-upgrading/quickstarts/docker-quickstart)

## Install Redis Software

To install Redis Software on a [supported platform](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/supported-platforms), you need to:

1. [Plan your deployment](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment).

1. [Prepare to install](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/prepare-install).

1. [Perform the install](https://redis.io/docs/latest/operate/rs/installing-upgrading/install).

Depending on your needs, you may also want to [customize the installation](#more-info-and-options).

If you're moving from a self-managed Redis Open Source deployment, see [Move from Redis Open Source to Redis Software](https://redis.io/docs/latest/operate/rs/installing-upgrading/move-from-open-source) for how configuration and deployment differ.

## Upgrade existing deployment

If you already installed Redis Software, you can:

- [Upgrade a cluster](https://redis.io/docs/latest/operate/rs/installing-upgrading/upgrading/upgrade-cluster)

- [Upgrade a database](https://redis.io/docs/latest/operate/rs/installing-upgrading/upgrading/upgrade-database)

- [Upgrade an Active-Active database](https://redis.io/docs/latest/operate/rs/installing-upgrading/upgrading/upgrade-active-active)

## Install and upgrade modules

To add capabilities with modules, you can:

- [Install a module on a cluster](https://redis.io/docs/latest/operate/rs/installing-upgrading/modules/add-module-to-cluster)

- [Enable a module for a database](https://redis.io/docs/latest/operate/rs/installing-upgrading/modules/add-module-to-database)

- [Upgrade modules](https://redis.io/docs/latest/operate/rs/installing-upgrading/modules/upgrade-module)

For module versioning and end-of-life dates, see [Module lifecycle](https://redis.io/docs/latest/operate/rs/installing-upgrading/modules-lifecycle).

## Uninstall Redis Software

- [Uninstall existing deployment](https://redis.io/docs/latest/operate/rs/installing-upgrading/uninstalling)

## More info and options

More information is available to help with customization and related questions:

- [CentOS/RHEL firewall configuration](https://redis.io/docs/latest/operate/rs/installing-upgrading/configuring/centos-rhel-firewall)
- [Change socket file location](https://redis.io/docs/latest/operate/rs/installing-upgrading/configuring/change-location-socket-files)
- [Cluster DNS configuration](https://redis.io/docs/latest/operate/rs/networking/cluster-dns)
- [Cluster load balancer setup](https://redis.io/docs/latest/operate/rs/networking/cluster-lba-setup)
- [File locations](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/file-locations)
- [Linux swap space configuration](https://redis.io/docs/latest/operate/rs/installing-upgrading/configuring/linux-swap)
- [mDNS client prerequisites](https://redis.io/docs/latest/operate/rs/networking/mdns)
- [User and group ownership](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/customize-user-and-group)

## Next steps

After you install Redis Software and set up your cluster, you can:

- [Add users](https://redis.io/docs/latest/operate/rs/security/access-control/create-users) to the cluster with specific permissions.  To begin, start with [Access control](https://redis.io/docs/latest/operate/rs/security/access-control).

- [Create databases](https://redis.io/docs/latest/operate/rs/databases/create) to use with your applications.


