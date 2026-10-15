# Prepare AWS Aurora MySQL/AWS RDS MySQL for RDI

```json metadata
{
  "schema_version": 2,
  "title": "Prepare AWS Aurora MySQL/AWS RDS MySQL for RDI",
  "description": "Enable CDC features in your source databases",
  "categories": ["docs","integrate","rs","rdi"],
  "group": "di",
  "tableOfContents": {"sections":[{"id":"add-an-aurora-reader-node","title":"Add an Aurora reader node"},{"id":"aurora-create-and-apply-parameter-group","title":"Create and apply parameter group"},{"id":"rds-create-and-apply-parameter-group","title":"Create and apply parameter group"}]}

,
  "codeExamples": [{"id":"aurora-create-a-parameter-group"},{"id":"aurora-apply-the-parameter-group"},{"id":"aurora-apply-the-parameter-group-to-the-database"},{"id":"aurora-reboot-the-database-instance"},{"id":"aurora-create-debezium-user"},{"id":"rds-create-a-parameter-group"},{"id":"rds-apply-the-parameter-group"},{"id":"rds-apply-the-parameter-group-to-the-database"},{"id":"rds-reboot-the-database-instance"},{"id":"rds-create-debezium-user"}]
}
```


Follow the steps in the sections below to prepare an [AWS Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_GettingStartedAurora.CreatingConnecting.Aurora.html) or [AWS RDS MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html) database.

Select the steps for your database type.

**AWS Aurora MySQL:**

```checklist {id="auroramysql" nointeractive="true" }
- [ ] [Add an Aurora reader node](#add-an-aurora-reader-node)
- [ ] [Create and apply parameter group](#aurora-create-and-apply-parameter-group)
- [ ] [Create Debezium user](#aurora-create-debezium-user)
```

## Add an Aurora reader node

RDI requires that your Aurora MySQL database has at least one replica or reader node. 

To add a reader node to an existing database, select **Add reader** from the **Actions** menu of the database and [add a reader node](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-replicas-adding.html).

You can also create one during database creation by selecting **Create an Aurora Replica or Reader node in a different AZ (recommended for scaled availability)** under **Availability & durability > Multi-AZ deployment**. 

## Create and apply parameter group {#aurora-create-and-apply-parameter-group}

RDI requires some changes to database parameters. On AWS Aurora, you change these parameters via a parameter group.

```checklist {id="auroramysql-param-group" nointeractive="true" }
- [ ] [Create/modify a parameter group](#aurora-create-a-parameter-group)
- [ ] [Apply the parameter group](#aurora-apply-the-parameter-group)
- [ ] [Apply the parameter group to the database](#aurora-apply-the-parameter-group-to-the-database)
- [ ] [Reboot the database instance](#aurora-reboot-the-database-instance)
```

1. <a id="aurora-create-a-parameter-group"></a>
    In the [Relational Database Service (RDS) console](https://console.aws.amazon.com/rds/), navigate to **Parameter groups**.
    
    If you have no existing parameter group,
    [create a new parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.CreatingCluster.html)
    with the following settings:

    | Name | Value |
    | :-- | :-- |
    | **Parameter group name**  | Enter a suitable parameter group name, like `rdi-mysql` |
    | **Description**  | (Optional) Enter a description for the parameter group |
    | **Engine Type**  | Choose **Aurora MySQL**.  |
    | **Parameter group family**  | Choose **aurora-mysql8.0**. |
    | **Type**  | Select **DB Parameter Group**. |

    Select **Create** to create the parameter group.

    If you *do* have an existing parameter group, select it and then either:

    -   Select **Edit** from **Parameter group actions** to 
        [modify the parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.ModifyingCluster.html)
        with the settings shown in the table above.
    -   Select **Copy** from **Parameter group actions** to
        [copy the existing parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.CopyingCluster.html)
        and then modify the copy with the settings shown in the table above.

1. <a id="aurora-apply-the-parameter-group"></a>
    Ensure that the parameter group you have just created or modified is selected
    and then select **Edit**. Change the following parameters:

    | Name | Value |
    | :-- | :-- |
    | `binlog_format`  | `ROW` |
    | `binlog_row_image`  | `FULL` |
    | `gtid_mode`  | `ON` |
    | `enforce_gtid_consistency`  | `ON` |

    Select **Save Changes** to apply the changes to the parameter group.

1. <a id="aurora-apply-the-parameter-group-to-the-database"></a>
    Go back to your target database on the RDS console, select **Modify** and then scroll down to **Additional Configuration**. Set the **DB Cluster Parameter Group** to the group you just created.

    Select **Save changes** to apply the parameter group to the new database.

1. <a id="aurora-reboot-the-database-instance"></a>
    Reboot your database instance. See [Rebooting a DB instance within an Aurora cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-reboot-db-instance.html) for more information.

<a id="aurora-create-debezium-user"></a>

## Create Debezium user

The Debezium connector needs a user account to connect to MySQL. This
user must have appropriate permissions on all databases where you want Debezium
to capture changes.

1. Connect to your database as an admin user and create a new user for the connector:

    ```sql
    CREATE USER '<username>'@'%' IDENTIFIED BY '<password>';
    ```

    Replace `<username>` and `<password>` with a username and password for the new user.

    The `%` means that the user can connect from any client. If you want to restrict the user to connect only from the RDI host, replace `%` with the IP address of the RDI host.

1. Grant the user the necessary permissions:

    ```sql
    GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT, LOCK TABLES ON *.* TO '<username>'@'%';
    ```

    Replace `<username>` with the username of the Debezium user.

    You can also grant SELECT permissions for specific tables only. The other permissions are global and cannot be restricted to specific tables.

    ```sql
    GRANT RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT, LOCK TABLES ON *.* TO '<username>'@'%';
    GRANT SELECT ON <database>.<table> TO '<username>'@'%';
    ```

1. Finalize the user's permissions:

    ```sql
    FLUSH PRIVILEGES;
    ```

**AWS RDS MySQL:**

```checklist {id="rds-mysql-list" nointeractive="true" }
- [ ] [Create and apply parameter group](#rds-create-and-apply-parameter-group)
- [ ] [Create Debezium user](#rds-create-debezium-user)
```

## Create and apply parameter group {#rds-create-and-apply-parameter-group}

RDI requires some changes to database parameters. On AWS RDS, you change these parameters via a parameter group.

```checklist {id="rds-mysql-param-group" nointeractive="true" }
- [ ] [Create/modify a parameter group](#rds-create-a-parameter-group)
- [ ] [Apply the parameter group](#rds-apply-the-parameter-group)
- [ ] [Apply the parameter group to the database](#rds-apply-the-parameter-group-to-the-database)
- [ ] [Reboot the database instance](#rds-reboot-the-database-instance)
```

1. <a id="rds-create-a-parameter-group"></a>
    In the [Relational Database Service (RDS) console](https://console.aws.amazon.com/rds/), navigate to **Parameter groups**.
    
    If you have no existing parameter group,
    [create a new parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.CreatingCluster.html)
    with the following settings:

    | Name | Value |
    | :-- | :-- |
    | **Parameter group name**  | Enter a suitable parameter group name, like `rdi-mysql` |
    | **Description**  | (Optional) Enter a description for the parameter group |
    | **Engine Type**  | Choose **MySQL Community**.  |
    | **Parameter group family**  | Choose **mysql8.0**. |

    Select **Create** to create the parameter group.

    If you *do* have an existing parameter group, select it and then either:

    -   Select **Edit** from **Parameter group actions** to 
        [modify the parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.ModifyingCluster.html)
        with the settings shown in the table above.
    -   Select **Copy** from **Parameter group actions** to
        [copy the existing parameter group](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_WorkingWithParamGroups.CopyingCluster.html)
        and then modify the copy with the settings shown in the table above.

1. <a id="rds-apply-the-parameter-group"></a>
    Ensure that the parameter group you have just created or modified is selected
    and then select **Edit**. Change the following parameters:

    | Name | Value |
    | :-- | :-- |
    | `binlog_format`  | `ROW` |
    | `binlog_row_image`  | `FULL` |

    Select **Save Changes** to apply the changes to the parameter group.

1. <a id="rds-apply-the-parameter-group-to-the-database"></a>
    Go back to your target database on the RDS console, select **Modify** and then scroll down to **Additional Configuration**. Set the **DB Cluster Parameter Group** to the group you just created.

    Select **Save changes** to apply the parameter group to the new database.

1. <a id="rds-reboot-the-database-instance"></a>
    Reboot your database instance. See [Rebooting a DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_RebootInstance.html) for more information.

<a id="rds-create-debezium-user"></a>

## Create Debezium user

The Debezium connector needs a user account to connect to MySQL. This
user must have appropriate permissions on all databases where you want Debezium
to capture changes.

1. Connect to your database as an admin user and create a new user for the connector:

    ```sql
    CREATE USER '<username>'@'%' IDENTIFIED BY '<password>';
    ```

    Replace `<username>` and `<password>` with a username and password for the new user.

    The `%` means that the user can connect from any client. If you want to restrict the user to connect only from the RDI host, replace `%` with the IP address of the RDI host.

1. Grant the user the necessary permissions:

    ```sql
    GRANT SELECT, RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT, LOCK TABLES ON *.* TO '<username>'@'%';
    ```

    Replace `<username>` with the username of the Debezium user.

    You can also grant SELECT permissions for specific tables only. The other permissions are global and cannot be restricted to specific tables.

    ```sql
    GRANT RELOAD, SHOW DATABASES, REPLICATION SLAVE, REPLICATION CLIENT, LOCK TABLES ON *.* TO '<username>'@'%';
    GRANT SELECT ON <database>.<table> TO '<username>'@'%';
    ```

1. Finalize the user's permissions:

    ```sql
    FLUSH PRIVILEGES;
    ```



