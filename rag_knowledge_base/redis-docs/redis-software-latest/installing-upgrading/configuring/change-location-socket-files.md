# Change socket file locations

```json metadata
{
  "schema_version": 2,
  "title": "Change socket file locations",
  "description": "Change socket file locations.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"default-socket-file-locations","title":"Default socket file locations"},{"id":"during-install","title":"Specify socket file location during install"},{"children":[{"id":"replace-nodes","title":"Replace nodes"},{"id":"migrate-replica-of","title":"Migrate cluster using Replica Of"}],"id":"after-cluster-setup","title":"Change socket file location for an existing cluster"}]}

,
  "codeExamples": []
}
```


## Default socket file locations

There are two default locations for the socket files in Redis Software:

- `/tmp` - In clean installations of Redis Software version earlier than 5.2.2
- `/var/opt/redislabs/run` - In clean installations of Redis Software version 5.2.2 and later

    > [!NOTE]
    > The default location was changed in case you run any maintenance procedures that delete the `/tmp` directory.

When you upgrade Redis Software from an earlier version to 5.2.2 or later, the socket files are not moved to the new location by default. You need to specify the socket file location [during installation](#during-install).

## Specify socket file location during install {#during-install}

To specify the socket file location during a new installation, follow the [Install Redis Software on Linux](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/install-on-linux) instructions, but use the `-s` [installation script option](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/install-script):

```sh
sudo ./install.sh -s </path/to/socket/files>
```

## Change socket file location for an existing cluster {#after-cluster-setup}

Directly changing the socket file location directly is not supported for bootstrapped nodes. If you need to change the socket file location for an existing cluster, use one of the following methods instead:

- [Replace nodes](#replace-nodes)

- [Migrate the cluster using Replica Of](#migrate-replica-of)

### Replace nodes {#replace-nodes}

To change the socket file location for all nodes in a cluster, follow these steps:

1. Install Redis Software on a new node with the new socket file location. Follow the [Install Redis Software on Linux](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/install-on-linux) instructions, but use the -s [installation script option](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/install-script):

    ```sh
    sudo ./install.sh -s </path/to/socket/files>
    ```

1. [Add the new node](https://redis.io/docs/latest/operate/rs/clusters/add-node) to the existing cluster.

1. [Remove a node](https://redis.io/docs/latest/operate/rs/clusters/remove-node#remove-a-node) with the old socket file location.

1. Repeat the previous steps until all nodes with the old socket file location have been replaced.

### Migrate cluster using Replica Of {#migrate-replica-of}

To migrate an existing cluster to a new cluster with a different socket file location:

1. Create a new cluster with the new socket file location. To do so, follow the [Install Redis Software on Linux](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/install-on-linux) instructions, but use the `-s` [installation script option](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/install-script):

    ```
    sudo ./install.sh -s </path/to/socket/files>
    ```

1. Use Replica Of to migrate your databases from the original cluster to the new cluster. For detailed steps, see the procedure to [configure Replica Of with different Redis Software clusters](https://redis.io/docs/latest/operate/rs/databases/import-export/replica-of/create#different-cluster).

