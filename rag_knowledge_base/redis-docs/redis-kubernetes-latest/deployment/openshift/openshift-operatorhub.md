# Deploy Redis Enterprise with OpenShift OperatorHub

```json metadata
{
  "schema_version": 2,
  "title": "Deploy Redis Enterprise with OpenShift OperatorHub",
  "description": "OpenShift provides the OperatorHub where you can install the Redis Enterprise operator from the administrator user interface.",
  "categories": ["docs","operate","kubernetes"],
  "tableOfContents": {"sections":[{"id":"install-the-redis-enterprise-operator","title":"Install the Redis Enterprise operator"},{"id":"security-context-constraints","title":"Security context constraints"},{"id":"create-redis-enterprise-custom-resources","title":"Create Redis Enterprise custom resources"}]}

,
  "codeExamples": []
}
```

You can deploy Redis Enterprise for Kubernetes from the Red Hat OpenShift CLI. You can also use a UI, [OperatorHub](https://docs.openshift.com/container-platform/4.11/operators/index.html) (Red Hat) to install operators and create custom resources.

> [!NOTE]
> If you suspect your file descriptor limits are below 100,000, you must either manually increase limits or [Allow automatic resource adjustment](https://redis.io/docs/latest/operate/kubernetes/security/allow-resource-adjustment). Most major cloud providers and standard container runtime configurations set default file descriptor limits well above the minimum required by Redis Enterprise. In these environments, you can safely run without enabling automatic resource adjustment.

To see which version of Redis Enterprise for Kubernetes supports your OpenShift version, see [Supported Kubernetes distributions](https://redis.io/docs/latest/operate/kubernetes/reference/supported_k8s_distributions).

## Install the Redis Enterprise operator

> [!WARNING]
>  If using version 6.2.18-41 or earlier, [Install the security context constraint](#install-security-context-constraint) before installing the operator. 

1. Select **Operators > OperatorHub**.

2. Search for _Redis Enterprise_ in the search dialog and select the **Redis Enterprise Operator provided by Redis** marked as **Certified**.

    By default, the image is pulled from Red Hat's registry.

3. On the **Install Operator** page, specify the namespace for the operator.

    Only one namespace per operator is supported.

4. Update the **channel** with the version you're installing.

    For more information about specific versions, see the [release notes](https://redis.io/docs/latest/operate/kubernetes/release-notes).

5. Choose an approval strategy.

    Use **Manual** for production systems to ensure the operator is only upgraded by approval.

6. Select **Install** and approve the install plan.

   You can monitor the subscription status in **Operators > Installed Operators**.

> [!WARNING]
> DO NOT modify or delete the StatefulSet created during the deployment process. Doing so could destroy your Redis Enterprise cluster (REC).

## Security context constraints

Versions 7.22.0-6 and later run in without permissions to [allow automatic resource adjustment](https://redis.io/docs/latest/operate/kubernetes/security/allow-resource-adjustment). If you use the recommended default security constraints, remove the existing `redis-enterprise-scc-v2` SCC and unbind it from the REC service account after upgrading.

## Create Redis Enterprise custom resources

The **Installed Operators**->**Operator details** page shows the provided APIs: **RedisEnterpriseCluster** and **RedisEnterpriseDatabase**. You can select **Create instance** to create custom resources using the OperatorHub interface.


Use the YAML view to create a custom resource file or let OperatorHub generate the YAML file for you by specifying your configuration options in the form view.

> [!NOTE]
> If you suspect your file descriptor limits are below 100,000, you must either manually increase limits or [Allow automatic resource adjustment](https://redis.io/docs/latest/operate/kubernetes/security/allow-resource-adjustment). Most major cloud providers and standard container runtime configurations set default file descriptor limits well above the minimum required by Redis Enterprise. In these environments, you can safely run without enabling automatic resource adjustment.

<note> The REC name cannot be changed after cluster creation.</note>

For more information on creating and maintaining Redis Enterprise custom resources, see [Redis Enterprise clusters (REC)](https://redis.io/docs/latest/operate/kubernetes/re-clusters) and [Redis Enterprise databases (REDB)](https://redis.io/docs/latest/operate/kubernetes/re-databases).

