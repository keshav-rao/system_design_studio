# Network port configurations

```json metadata
{
  "schema_version": 2,
  "title": "Network port configurations",
  "description": "This document describes the various network port ranges and their uses.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"ports-and-port-ranges-used-by-redis-software","title":"Ports and port ranges used by Redis Software"},{"children":[{"id":"reserve-ports","title":"Reserve ports"},{"id":"change-the-cluster-manager-ui-port","title":"Change the Cluster Manager UI port"},{"id":"change-the-envoy--ports","title":"Change the envoy  ports"},{"id":"change-the-rest-api-port","title":"Change the REST API port"},{"id":"os-conflicts-with-port-53","title":"OS conflicts with port 53"},{"id":"update-sysctlconf-to-avoid-port-collisions","title":"Update sysctl.conf to avoid port collisions"}],"id":"change-port-configuration","title":"Change port configuration"},{"children":[{"id":"require-https-for-api-endpoints","title":"Require HTTPS for API endpoints"},{"id":"http-to-https-redirection","title":"HTTP to HTTPS redirection"}],"id":"configure-https","title":"Configure HTTPS"},{"id":"nodes-on-different-vlans","title":"Nodes on different VLANs"}]}

,
  "codeExamples": []
}
```


All Redis Software deployments span multiple physical/virtual nodes. You'll need to keep several ports open between these nodes. This document describes the various port ranges and their uses.

> [!NOTE]
> Whenever you create a new database, you must verify that the ports assigned to the new database's endpoints are open. The cluster will not perform this verification for you.

## Ports and port ranges used by Redis Software

Redis Software's port usage falls into three general categories:

- Internal: For traffic between or within cluster nodes
- External: For traffic from client applications or external monitoring resources
- Active-Active: For traffic to and from clusters hosting Active-Active databases

| Protocol | Port | Configurable | Connection source | Description |
|----------|------|--------------|-------------------|-------------|
| TCP | 8001 | <span title="Not configurable">&#x274c; No</span> | Internal, External | Traffic from application to Redis Software [Discovery Service](https://redis.io/docs/latest/operate/rs/databases/durability-ha/discovery-service) |
| TCP | 8070 | <span title="Not configurable">&#x274c; No</span> | External | Metrics exported and managed by the web proxy |
| TCP | 3347-3349, 8000, 8071, 9091, 9125 | <span title="Not configurable">&#x274c; No</span> | Internal | Internal metrics ports |
| TCP | 8443 | <span title="Configurable">&#x2705; Yes</span> | Internal, External | Secure (HTTPS) access to the management web UI |
| TCP | 9081 | <span title="Configurable">&#x2705; Yes</span> | Internal | CRDB coordinator for Active-Active management (internal) |
| TCP | 9082 | <span title="Not configurable">&#x274c; No</span> | Internal | Cluster API internal port |
| TCP | 9443, 8080, 3346 | <span title="Configurable">&#x2705; Yes</span> | Internal, External, Active-Active | REST API traffic, including cluster management and node bootstrap |
| TCP | 10050 | <span title="Not configurable">&#x274c; No</span> | Internal | Zabbix monitoring |
| TCP | 10000-10049, 10051-19999 | <span title="Configurable">&#x2705; Yes</span> | Internal, External, Active-Active | Database traffic |
| UDP | 53, 5353 | <span title="Not configurable">&#x274c; No</span> | Internal, External | DNS/mDNS traffic |
| TCP | 1968 | <span title="Not configurable">&#x274c; No</span> | Internal | Proxy traffic |
| TCP | 3333-3345, 3350-3354, 36379 | <span title="Not configurable">&#x274c; No</span> | Internal | Internode communication |
| TCP | 3355 | <span title="Configurable">&#x2705; Yes</span> | Internal | Authentication service internal port |
| TCP | 3357 | <span title="Not configurable">&#x274c; No</span> | Internal | Internal communication |
| TCP | 20000-29999 | <span title="Not configurable">&#x274c; No</span> | Internal | Database shard traffic |
| TCP | 8002, 8004, 8006 | <span title="Configurable">&#x2705; Yes</span> | Internal | Default system health monitoring (envoy admin, envoy management server, gossip envoy admin)|
| TCP | 8444, 9080 | <span title="Not configurable">&#x274c; No</span> | Internal | Traffic between web proxy and cnm_http/cm |

> [!NOTE]
> The cluster uses ports 20000-29999 for internal shard traffic. You can't change the range, but `reserved_ports` excludes specific ports or port ranges from shard assignment.

## Change port configuration

### Reserve ports

Redis Software reserves some ports by default (`system_reserved_ports`). To reserve other ports or port ranges and prevent the cluster from assigning them to database endpoints or internal shard traffic, configure `reserved_ports` using one of the following methods:

- [rladmin cluster config](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/config)

    ```sh
    rladmin cluster config reserved_ports <list of ports/port ranges>
    ```

    For example:

    ```sh
    rladmin cluster config reserved_ports 11000 13000-13010 20048
    ```

- [Update cluster settings](https://redis.io/docs/latest/operate/rs/references/rest-api/requests/cluster#put-cluster) REST API request

    ```sh
    PUT /v1/cluster
    { "reserved_ports": ["list of ports/port ranges"] }
    ```

    For example:

    ```sh
    PUT /v1/cluster
    { "reserved_ports": ["11000", "13000-13010", "20048"] }
    ```

### Change the Cluster Manager UI port

The Redis Software Cluster Manager UI uses port 8443, by default. You can change this to a custom port as long as the new port is not in use by another process.

To change this port, run:

```sh
rladmin cluster config cm_port <custom-port>
```

After you change the Cluster Manager UI port, use the new port in the URL when accessing the UI on any node in the cluster. Example: `https://newnode.mycluster.example.com:<custom-port>`

### Change the envoy  ports

For system health monitoring, Redis uses the following ports by default:

- Port 8002 for envoy admin

- Port 8004 for envoy management server

- Port 8006 for gossip envoy admin

You can change each envoy port to a custom port using the [`rladmin cluster config`](https://redis.io/docs/latest/operate/rs/references/cli-utilities/rladmin/cluster/config) command as long as the new port is not in use by another process. When you change `envoy_admin_port`, expect a restart of envoy.

To change the envoy admin port, run:

```sh
$ rladmin cluster config envoy_admin_port <new-port>
Updating envoy_admin_port... restarting now
```

To change the envoy management server port, run:

```sh
$ rladmin cluster config envoy_mgmt_server_port <new-port>
Cluster configured successfully
```

To change the gossip envoy admin port, run:

```sh
$ rladmin cluster config gossip_envoy_admin_port <new-port>
Cluster configured successfully
```

### Change the REST API port

For the REST API, Redis Software uses port 9443 (secure) and port 8080 (not secure), by default. You can change this to a custom port as long as the new port is not in use by another process.

To change these ports, run:

```sh
rladmin cluster config cnm_http_port <new-port>
```

```sh
rladmin cluster config cnm_https_port <new-port>
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



### Update `sysctl.conf` to avoid port collisions

To avoid port collision, update `/etc/sysctl.conf` to include:

``` sh
net.ipv4.ip_local_port_range = 30000 65535
```



## Configure HTTPS

### Require HTTPS for API endpoints

By default, the Redis Software API supports communication over HTTP and HTTPS. However, you can turn off HTTP support to ensure that API requests are encrypted.

Before you turn off HTTP support, make sure you migrate any scripts or proxy configurations that use HTTP to the encrypted API endpoint to prevent broken connections.

To turn off HTTP support for API endpoints, run:

```sh
rladmin cluster config http_support disabled
```

After you turn off HTTP support, traffic sent to the unencrypted API endpoint is blocked.


### HTTP to HTTPS redirection
Starting with version 6.0.12, you cannot use automatic HTTP to HTTPS redirection.
To poll metrics from the `metrics_exporter` or to access the Cluster Manager UI, use HTTPS in your request. HTTP requests won't be automatically redirected to HTTPS for those services. 

## Nodes on different VLANs

Nodes in the same cluster must reside on the same VLAN. If you can't
host the nodes on the same VLAN, then you must open [all ports](https://redis.io/docs/latest/operate/rs/networking/port-configurations) between them.

