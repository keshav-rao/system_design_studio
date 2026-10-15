# Upgrade Redis database version

```json metadata
{
  "schema_version": 2,
  "title": "Upgrade Redis database version",
  "description": "Describes when you can upgrade your database to the latest available version for each plan type.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"upgrade-database","title":"Upgrade database"},{"id":"manually-revert-upgrade","title":"Manually revert upgrade"}]}

,
  "codeExamples": []
}
```


You can upgrade databases that are not on the latest available version of Redis to a later database version at any time.

> [!NOTE]
> Please keep in mind the following before upgrading your database version:
>
> - We recommend that you [back up your data](https://redis.io/docs/latest/operate/rc/databases/back-up-data) before upgrading to make it easier to [manually revert the upgrade](#manually-revert-upgrade) if needed.
>
> - We recommend that you upgrade your database during off-peak hours or during application maintenance to minimize reconnections.
>
> - Review the breaking changes for the new database version before upgrading: 
>     - [Redis 7.2](https://redis.io/docs/latest/operate/rc/changelog/version-release-notes/7-2) 
>     - [Redis 7.4](https://redis.io/docs/latest/operate/rc/changelog/version-release-notes/7-4)
>     - [Redis 8.0](https://redis.io/docs/latest/operate/rc/changelog/version-release-notes/8-0)
>     - [Redis 8.2](https://redis.io/docs/latest/operate/rc/changelog/version-release-notes/8-2)
>     - [Redis 8.4](https://redis.io/docs/latest/operate/rc/changelog/version-release-notes/8-4)
>     - [Redis 8.6](https://redis.io/docs/latest/operate/rc/changelog/version-release-notes/8-6)
>
> - You must upgrade the target database in an [Active-Passive](https://redis.io/docs/latest/operate/rc/databases/migrate-databases#sync-using-active-passive) setup before you upgrade the source database to prevent compatibility issues.

## Upgrade database

To upgrade a single-region Redis Cloud database: 

1. Choose your database from the **Databases** list to open your database page. Select **More actions > Version upgrade**.

    ![The More Actions menu on the Database page.](https://redis.io/docs/latest/images/rc/databases-more-actions-menu.png)
    
    You can also select **More actions > Version upgrade** from the database list.

1. Select the target version from the **Select version** list.

    ![The Redis version upgrade screen.](https://redis.io/docs/latest/images/rc/database-version-upgrade.png)

    If your database has not been backed up before, we recommend that you back up your database. Select **Go to backup** to go to the [backup settings](https://redis.io/docs/latest/operate/rc/databases/back-up-data).

1. Select **Upgrade Now** to start the upgrade.

    ![The upgrade button.](https://redis.io/docs/latest/images/rc/button-upgrade-now.png)

The database will start upgrading to the selected version immediately. The upgrade may take a few minutes. 

You can continue to use the Redis Cloud console for other tasks during the upgrade.


## Manually revert upgrade

Automatically reverting to a previous Redis database version is not supported on Redis Cloud.

If you [backed up your database](https://redis.io/docs/latest/operate/rc/databases/back-up-data) before you upgraded your database version, you can:

1. [Delete your database](https://redis.io/docs/latest/operate/rc/databases/delete-database) without deleting your subscription.
1. [Create a new database](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-existing) in your subscription with the following settings:
    - **Port number**: Use the same port number as the old database.
    - **Version**: Select the original version of Redis.
1. [Import the backup files](https://redis.io/docs/latest/operate/rc/databases/import-data) into the new database.

This allows you to connect to the database on the previous version without changing your connection details in your application.

If you did not back up your database before upgrading:

1. [Back up your database](https://redis.io/docs/latest/operate/rc/databases/back-up-data).
1. [Create a new database](https://redis.io/docs/latest/operate/rc/databases/create-database/create-pro-database-existing) in your subscription and select the original version of Redis.
1. [Import the backup files](https://redis.io/docs/latest/operate/rc/databases/import-data) into the new database.
1. Change connection details in your application from the old database to the new database.
