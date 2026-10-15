# RDI on Redis Cloud quick start

```json metadata
{
  "schema_version": 2,
  "title": "RDI on Redis Cloud quick start",
  "description": "Learn how to create a data pipeline between a PostgreSQL source database created with Terraform and a Redis Cloud target database.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"prerequisites","title":"Prerequisites"},{"id":"create-a-data-integration-workspace","title":"Create a data integration workspace"},{"id":"get-required-arns","title":"Get required ARNs"},{"id":"create-the-source-database-and-network-resources","title":"Create the source database and network resources"},{"id":"resume-pipeline-setup","title":"Resume pipeline setup"},{"id":"delete-sample-resources","title":"Delete sample resources"}]}

,
  "codeExamples": []
}
```


The [`rdi-cloud-automation` GitHub repository](https://github.com/redis/rdi-cloud-automation) contains a Terraform script that quickly sets up a PostgreSQL source database on an EC2 instance and all required permissions and network setup to connect it to a Redis Cloud target database.

> [!NOTE]
> This guide is for demonstration purposes only. It is not recommended for production use.

## Prerequisites

To follow this guide, you need to:

1. Create a [Redis Cloud Pro database](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-new) hosted on Amazon Web Services (AWS).

    Turn on Multi-AZ replication and [manually select the availability zones](https://redis.io/docs/latest/operate/rc/databases/configuration/high-availability#availability-zones) when creating the database.

1. Install the [AWS CLI](https://aws.amazon.com/cli/) and set up [credentials for the CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-sso.html).

1. Install [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli).

## Create a data integration workspace

Before you can create your first Data Integration pipeline for a Redis Cloud subscription, you must first deploy the cloud infrastructure needed to host the pipeline and run the workers associated with the pipeline. In Redis Cloud, this is called a **Workspace**. See [Create and manage Data Integration workspace](https://redis.io/docs/latest/operate/rc/rdi/create-workspace) for more information.

To create a Data Integration workspace for an existing [Pro subscription](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-new):

1. In the Redis Cloud console, select **Data Integration**.

2. Select **Create workspace** if you have no workspaces yet.

    ![The create workspace button.](https://redis.io/docs/latest/images/rc/rdi/rdi-create-workspace-button.png)

    If you already have a workspace, select **New workspace**.

    ![The new workspace button.](https://redis.io/docs/latest/images/rc/rdi/rdi-new-workspace-button.png)

    You can also open **Data Integration** from a subscription or database page.
    Select **Create workspace** to use that subscription.

    ![The create workspace button.](https://redis.io/docs/latest/images/rc/rdi/rdi-create-workspace-button.png)

3. Select your Pro subscription if it is not already selected.

    ![The select pro subscription drop down.](https://redis.io/docs/latest/images/rc/rdi/rdi-create-workspace-select-subscription.png)

4. Review **Data Integration subnet (CIDR)**. The console suggests a dedicated
   `/22` Classless Inter-Domain Routing (CIDR) range for the workspace.

    [Plan network capacity for all pipelines](https://redis.io/docs/latest/operate/rc/rdi/scale-pipeline#plan-workspace-network-capacity)
    before you create the workspace. Choose a `/21` or larger range if you plan
    more than 5 sources or more than 5 processor replicas in total.
    These counts are a conservative planning trigger, not a capacity limit.
    You cannot enlarge the workspace CIDR after creation.

    For Amazon Web Services (AWS), the RDI workspace CIDR must:

    - Be in the same [RFC 1918 private address range](https://datatracker.ietf.org/doc/html/rfc1918#section-3) as the subscription virtual private cloud (VPC)'s primary CIDR: `10.0.0.0/8`, `172.16.0.0/12`, or `192.168.0.0/16`.
    - Not overlap with existing subscription, peering, transit gateway (TGW), application, database, or RDI workspace CIDR ranges.

    For example, a subscription VPC has the primary CIDR `10.238.252.0/24`.
    The range `192.168.0.0/22` is invalid because it is in a different
    RFC 1918 range. An unused range such as `10.239.0.0/22` is valid.

    If the suggestion is missing or unsuitable, select another unused range.
    It must meet your capacity needs and use the same private address range.
    See [VPC CIDR block association restrictions](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-cidr-blocks.html#vpc-resize).

    ![The select pro subscription drop down.](https://redis.io/docs/latest/images/rc/rdi/rdi-create-workspace-cidr.png)

5. Select **Create workspace**.

    ![The create workspace button.](https://redis.io/docs/latest/images/rc/rdi/rdi-create-workspace-button.png)

Redis Cloud creates the workspace in the background. Select **Create pipeline**
to [create your pipeline](https://redis.io/docs/latest/operate/rc/rdi/define) while it provisions.
Select **Create pipeline later** to return to the Redis Cloud console.


## Get required ARNs

This example creates one PostgreSQL source. You can [add more sources](https://redis.io/docs/latest/operate/rc/rdi/view-edit#add-source) after the pipeline is running.

1. On the [Redis Cloud console](https://cloud.redis.io/), open your target database's **Data Integration** tab and select **Add pipeline**.

    ![The Add pipeline control is available while the workspace is being created.](https://redis.io/docs/latest/images/rc/rdi/rdi-workspace-add-pipeline.png)

1. In **Settings**, select your target database and choose **Hash** or **JSON** as the default data structure, then select **Continue**.
1. In **Add sources**, select **PostgreSQL**.
1. Enter a **Source name** of your choice, for example `inventory-postgres`.
1. Select **Continue** to open **Configure source**.
1. Under **Source connectivity**, copy the **Role ARN**. Use it as `redis_privatelink_arn` in the Terraform configuration.

    ![The source connectivity Role ARN and availability zones.](https://redis.io/docs/latest/images/rc/rdi/rdi-setup-connectivity-arn.png)

1. Under **Secrets**, copy the **Role ARN**. Use it as `redis_secrets_arn` in the Terraform configuration.

    ![The Role ARN in the Secrets section.](https://redis.io/docs/latest/images/rc/rdi/rdi-credentials-arn.png)

1. Select **Save & exit** while you create the source resources.

## Create the source database and network resources

1. Clone or download the [`rdi-cloud-automation` GitHub repository](https://github.com/redis/rdi-cloud-automation).

1. In a terminal window, go to the `examples/aws-ec2-privatelink` directory.

1. Run `terraform init` to initialize the Terraform working directory.

1. Open the `example.tfvars` file and edit the following variables:

    - `region`: The AWS region where your Redis Cloud database is deployed.
    - `azs`: The availability zone IDs where your Redis Cloud database is deployed.
    - `port`: The port number for the new PostgreSQL source database.
    - `name`: A prefix for all of the created AWS resources.
    - `redis_secrets_arn`: The role ARN from **Secrets** in the Redis Cloud console.
    - `redis_privatelink_arn`: The role ARN from **Source connectivity** in the Redis Cloud console.

1. To view the configuration, run:

    ```sh
    terraform plan -var-file=example.tfvars
    ```

1. To create the AWS resources, run:

    ```sh
    terraform apply -var-file=example.tfvars
    ```

    This example creates the following resources on your AWS account:

    - An AWS KMS key with the required permissions for RDI
    - A VPC with a public and private subnet and all necessary route tables
    - An EC2 instance running a PostgreSQL database with a security group that allows access from Redis Cloud
    - An AWS Secrets Manager secret for the PostgreSQL database credentials
    - A Network Load Balancer (NLB), a listener, and target group to route traffic to the EC2 instance with AWS PrivateLink
    - An AWS PrivateLink endpoint service for the PostgreSQL database

Creating the AWS resources will take some time. After the resources are created, you'll be able to view them in the AWS management console.

Save the following outputs:

- `database`: The name of the PostgreSQL database.
- `port`: The port number for the PostgreSQL database.
- `secret_arn`: The ARN of the AWS Secrets Manager secret for the PostgreSQL database credentials.
- `vpc_endpoint_service_name`: The name of the AWS PrivateLink endpoint service for the PostgreSQL database.

If you lose any outputs, run `terraform output` to view them again.

## Resume pipeline setup

1. Return to your database's **Data Integration** tab in the [Redis Cloud console](https://cloud.redis.io/).
1. Open the draft pipeline's actions menu and select **Resume pipeline setup**.
1. Open **Configure source** and select your PostgreSQL source in the **Sources** list.
1. Under **Source connectivity**, enter the Terraform `vpc_endpoint_service_name` output as the **Private Link service name**.
1. Select **Connect to Private Link** and wait for connectivity to complete.

    ![AWS Private Link connectivity with the service name and Connect to Private Link control.](https://redis.io/docs/latest/images/rc/rdi/rdi-source-configuration-source-connectivity-privatelink.png)

1. Under **Secrets**, enter the `secret_arn` output as **Credentials Secret ARN**.
1. Select **Validate** to check access to the secret.

    ![The Credentials Secret ARN field, transit security options, and Validate control.](https://redis.io/docs/latest/images/rc/rdi/rdi-source-configuration-secrets.png)

1. Under **Source configuration**, enter the `database` and `port` Terraform outputs in the matching fields.
1. Select **Test source** and correct any validation errors, then select **Continue**.
1. In **Select data**, select the schemas, tables, and columns to ingest. Review the selected key for each table.

    ![Selecting a schema shows its tables for ingestion.](https://redis.io/docs/latest/images/rc/rdi/rdi-dataset-schema-selected.png)

    ![Selecting a table shows its columns and the columns selected for ingestion.](https://redis.io/docs/latest/images/rc/rdi/rdi-select-columns.png)

1. Select **Continue** to open **Add transformations**. For this example, you can keep the default mapping without adding jobs.
1. Select **Continue to review & deploy**.
1. Review the source and target, then select **Deploy pipeline**.

    ![The Deploy pipeline button.](https://redis.io/docs/latest/images/rc/rdi/rdi-confirm-deploy.png)

The source first imports its selected data, then captures ongoing changes. Open the pipeline's **Dashboard** or **Metrics** tab to follow its progress.

The following example shows the metrics for one selected source in a pipeline with multiple sources.

![Metrics for one selected source in a pipeline, including snapshot progress and per-table record counts.](https://redis.io/docs/latest/images/rc/rdi/rdi-2-metrics.png)

See [View and edit data pipeline](https://redis.io/docs/latest/operate/rc/rdi/view-edit) for source actions, dataset changes, and monitoring.

## Delete sample resources

> [!WARNING]
> Make sure to [delete your data pipeline](https://redis.io/docs/latest/operate/rc/rdi/view-edit#delete-pipeline) before deleting the sample resources.

To delete the sample resources created by Terraform, run:

```sh
terraform destroy -var-file=example.tfvars
```

