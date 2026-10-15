# Plan Redis Software deployment

```json metadata
{
  "schema_version": 2,
  "title": "Plan Redis Software deployment",
  "description": "Plan a deployment of Redis Software.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": []
}
```


Before installing Redis Software, you need to:

- Set up your hardware. See [Hardware requirements](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/hardware-requirements) and [Persistent and ephemeral node storage 
](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/persistent-ephemeral-storage) for more information.

- Choose your [deployment platform](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/supported-platforms).

    Redis Software supports a variety of platforms, including:

    - Multiple Linux distributions (Ubuntu, Red Hat Enterprise Linux (RHEL), IBM CentOS, Oracle Linux)
    - [Amazon AWS AMI](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/configuring-aws-instances)
    - [Docker container](https://redis.io/docs/latest/operate/rs/installing-upgrading/quickstarts/docker-quickstart) (for development and testing only)
    - [Kubernetes](https://redis.io/docs/latest/operate/kubernetes)

    For more details, see [Supported platforms](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/plan-deployment/supported-platforms).

- Open appropriate [network ports](https://redis.io/docs/latest/operate/rs/networking/port-configurations) in the firewall to allow connections to the nodes.

- Configure [cluster DNS](https://redis.io/docs/latest/operate/rs/networking/cluster-dns) so that cluster nodes can reach each other by DNS names.
- By default, the installation process requires an internet connection to install dependencies and synchronize the operating system clock. To learn more, see [Offline installation](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/offline-installation).

- [Configure different mount points for data and log directories](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/customize-install-directories#config-diff-data-log-dirs).

## Next steps

After you finish planning your deployment, you can:

- [Download an installation package](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/prepare-install/download-install-package).

- [Prepare to install](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/prepare-install) Redis Software.

- [View installation questions](https://redis.io/docs/latest/operate/rs/installing-upgrading/install/manage-installation-questions) and prepare answers before installation.

