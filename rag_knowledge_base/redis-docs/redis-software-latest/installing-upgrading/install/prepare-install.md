# Prepare to install Redis Software

```json metadata
{
  "schema_version": 2,
  "title": "Prepare to install Redis Software",
  "description": "Prepare to install Redis Software.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": []
}
```


Before you install Redis Software:

- [Download an installation package](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/prepare-install/download-install-package).

- [View installation questions](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/manage-installation-questions) and optionally prepare answers before installation.

- Review the [security considerations](https://redis.io/docs/latest/operate/rs/security) for your deployment.

- Check that you have root-level access to each node, either directly or with `sudo`.

- Check that all [required ports are available](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/prepare-install/port-availability).

- [Turn off Linux swap](https://redis.io/docs/latest/operate/rs/installing-upgrading/configuring/linux-swap) on all cluster nodes.

- If you require the `redislabs` UID (user ID) and GID (group ID) numbers to be the same on all the nodes, create the `redislabs` user and group with the required numbers on each node.

- If you want to use Auto Tiering for your databases, see [Auto Tiering installation](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/install-on-linux#auto-tiering-installation).

## Next steps

- View [installation script options](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/install-script) before starting the installation.

- [Install Redis Software](https://redis.io/docs/latest/operate/rs/installing-upgrading/install).

