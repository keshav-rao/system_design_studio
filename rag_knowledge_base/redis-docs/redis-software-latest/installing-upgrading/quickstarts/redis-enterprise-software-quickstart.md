# Redis Software quickstart

```json metadata
{
  "schema_version": 2,
  "title": "Redis Software quickstart",
  "description": "Set up a test deployment of Redis Software for Linux.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"children":[{"id":"update-sysctlconf-to-avoid-port-collisions","title":"Update sysctl.conf to avoid port collisions"},{"id":"os-conflicts-with-port-53","title":"OS conflicts with port 53"},{"id":"configuration-for-aws-and-gcp","title":"Configuration for AWS and GCP"}],"id":"ensure-port-availability","title":"Ensure port availability"},{"id":"install-redis-software","title":"Install Redis Software"},{"id":"set-up-a-cluster","title":"Set up a cluster"},{"id":"create-a-database","title":"Create a database"},{"id":"connect-to-your-database","title":"Connect to your database"},{"id":"supported-web-browsers","title":"Supported web browsers"},{"id":"continue-learning-with-redis-university","title":"Continue learning with Redis University"}]}

,
  "codeExamples": []
}
```

This guide helps you install Redis Software on a Linux host to test its capabilities.

When finished, you'll have a simple cluster with a single node:

1. [Ensure port availability](#ensure-port-availability)

1. [Install Redis Software](#install-redis-enterprise-software)

1. [Set up a Redis Software cluster](#set-up-a-cluster)

1. [Create a new Redis database](#create-a-database)

1. [Connect to your Redis database](#connect-to-your-database)

> [!NOTE]
> **This quickstart is designed for local testing only.**
> For production environments, see the [install and setup](https://redis.io/docs/latest/operate/rs/installing-upgrading#install-redis-enterprise-software) guide for deployment options and instructions.

## Ensure port availability

If ports that Redis assigns to the database are being used by the operating system or other processes, the installation fails.

Follow the relevant sections to configure required ports.

For recommended and optional port configuration, see [Network port configurations](https://redis.io/docs/latest/operate/rs/networking/port-configurations).

### Update `sysctl.conf` to avoid port collisions

To avoid port collision, update `/etc/sysctl.conf` to include:

``` sh
net.ipv4.ip_local_port_range = 30000 65535
```


### OS conflicts with port 53

If port 53 is in use, the installation fails. This issue can occur in default installations of certain operating systems in which `systemd-resolved` (DNS server) or `dnsmasq` is running.

To prevent this issue, change the system configuration to make this port available before installation.

To prevent `systemd-resolved` from using port 53:

1. Edit `/etc/systemd/resolved.conf`: 

    ```sh
    sudo vi /etc/systemd/resolved.conf
    ```

1. Add `DNSStubListener=no` as the last line in the file and save the file.

1. Rename the current `/etc/resolv.conf` file:

    ```sh
    sudo mv /etc/resolv.conf /etc/resolv.conf.orig
    ```

1. Create a symbolic link for `/etc/resolv.conf`:

    ```sh
    sudo ln -s /run/systemd/resolve/resolv.conf /etc/resolv.conf
    ```

    > [!NOTE]
    > You might encounter a temporary name resolution error (`sudo: unable to resolve host {hostname}: Temporary failure in name resolution`), which should be fixed when you restart `systemd-resolved` in the next step.

2. Restart the DNS service:

    ```sh
    sudo service systemd-resolved restart
    ```

To prevent `dnsmasq` from using port 53:

1. Stop the `dnsmasq` service if it's running:

    ```sh
    sudo systemctl stop dnsmasq
    ```

1. Prevent `dnsmasq` from starting automatically at system boot:

    ```sh
    sudo systemctl disable dnsmasq
    ```

1. Mask `dnsmasq` to prevent it from being started manually or by other services:

    ```sh
    sudo systemctl mask dnsmasq
    ```

1. Verify `dnsmasq` is no longer active and won't start at system boot:

    ```sh
    sudo systemctl status dnsmasq
    ```



### Configuration for AWS and GCP

For detailed configuration instructions, see your cloud provider's documentation.

1. Create a VPC that you can use with regional subnets.

1. Within this VPC, create firewall rules that allow external and internal access for Redis Software.


| Ingress/Egress   | Source                                             | Protocol  | Ports                                    | Other protocols  |
|------------------|----------------------------------------------------|-----------|------------------------------------------|------------------|
| Ingress          | 0.0.0.0/0                                          | TCP       | 21, 22, 53, 8001, 8443, 9443, 8070, <nobr>10000-19999</nobr> | ICMP             |
| Ingress          | 0.0.0.0/0                                          | UDP       | 53, 5353                                  |                  |
| Ingress          | 10.0.0.0/8  (if subnets use 10. ranges) | all       | all                                      |                  | 


## Install Redis Software

To install Redis Software:

1. Download the installation files from the [Redis Software Download Center](https://redis.io/downloads/#Redis_Software)
and copy the download package to a machine with a Linux-based OS. 

    > [!NOTE]
    > You are required to create a free account to access the download center.

1. Extract the installation files:

    ```sh
    tar vxf <downloaded tar file name>
    ```

1. Run the `install.sh` script in the current directory:

    ```sh
    sudo ./install.sh -y
    ```

## Set up a cluster

To set up your machine as a Redis Software cluster:

1. In a browser, go to `https://<name-or-IP-address-of-the-machine-with-Redis-Enterprise-Software-installed>:8443` to access the Cluster Manager UI. If you use a browser on the host machine, you can also access the Cluster Manager UI at `https://localhost:8443`.

    The cluster generates self-signed TLS certificates to secure the connection. Because these self-signed certificates are unknown to the browser, you must accept them before you proceed.

    If the server does not show the sign-in screen, try again after a few minutes.

1. Select **Create new cluster**.

    ![When you first install Redis Software, you need to set up a cluster.](https://redis.io/docs/latest/images/rs/screenshots/cluster/setup/create-cluster.png)

2. Enter an email and password for the administrator account, then select **Next** to proceed to cluster setup.

    ![Set the credentials for your admin user.](https://redis.io/docs/latest/images/rs/screenshots/cluster/setup/admin-credentials.png)

    You can also use these credentials to connect to the [REST API](https://redis.io/docs/latest/operate/rs/references/rest-api).

3. Enter your cluster license key if you have one. Otherwise, a trial version is installed.

    ![Enter your cluster license key if you have one.](https://redis.io/docs/latest/images/rs/screenshots/cluster/setup/cluster-license-key.png)

4. In the **Configuration** section, enter a cluster FQDN such as `cluster.local`, then select **Next**.

    ![Configure the cluster FQDN.](https://redis.io/docs/latest/images/rs/screenshots/cluster/setup/config-cluster.png)

    > [!WARNING]
    > If the FQDN is `cluster.local`, you cannot configure DNS. You cannot change the FQDN after cluster creation.

1. On the node setup screen, select **Create cluster** to accept the defaults.

    ![Configure the node specific settings.](https://redis.io/docs/latest/images/rs/screenshots/cluster/setup/node-settings.png)

6. Select **OK** to acknowledge the replacement of the HTTPS TLS certificate on the node.  If you receive a browser warning, you can proceed safely.

    ![Modal shown when a page refresh is needed because the certificates have been updated.](https://redis.io/docs/latest/images/rs/screenshots/cluster/setup/https-page-refresh-modal.png)


## Create a database

1. On the **Databases** screen, select **Quick database**.

    ![Select Quick database on the Databases screen.](https://redis.io/docs/latest/images/rs/screenshots/databases/db-screen.png)

1. Enter 12000 for the **Port**.

    If port 12000 is not available, enter any available port number between 10000 to 19999 or leave it blank to let the cluster assign a port number for you. You will use this port number to connect to the database.

    ![Create a quick database.](https://redis.io/docs/latest/images/rs/screenshots/databases/quick-db-7-8-2.png)

1. Select **Create** to create your database.

When you see **Database active** appear on the database configuration screen, the database is activated and ready for you to use.

![Database active icon.](https://redis.io/docs/latest/images/rs/icons/db-active-icon.png)


You now have a Redis database!

## Connect to your database

After you create the Redis database, you can connect to it and store data.
See [Test client connection](https://redis.io/docs/latest/operate/rs/databases/connect/test-client-connectivity) for connection options and examples.

## Supported web browsers

To use the Redis Software Cluster Manager UI, you need a modern browser with JavaScript enabled.
 
The Cluster Manager UI is officially supported for the latest version of [Google Chrome](https://www.google.com/chrome/), as well as the three previous and three subsequent versions.

## Continue learning with Redis University




