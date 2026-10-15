# Redis Cloud changelog (November 2024)

```json metadata
{
  "schema_version": 2,
  "title": "Redis Cloud changelog (November 2024)",
  "description": "New features, enhancements, and other changes added to Redis Cloud during November 2024.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"pro-subscription-version-upgrade","title":"Pro subscription version upgrade"}],"id":"new-features","title":"New Features"}]}

,
  "codeExamples": []
}
```


## New Features

### Pro subscription version upgrade

You can now upgrade all databases in your Pro subscription from your [subscription page](https://redis.io/docs/latest/operate/rc/subscriptions/view-pro-subscription). 

Select **Version upgrade** to request to upgrade your subscription and databases if there is a later version available.

![Version upgrade button.](https://redis.io/docs/latest/images/rc/button-version-upgrade.png)

Select the version to upgrade your databases from the list and select **Upgrade** to submit the upgrade request.

![Version upgrade request list with version 7.4 selected.](https://redis.io/docs/latest/images/rc/version-upgrade-request.png)

The upgrade will start one week from your request, according to your subscription's [maintenance windows](https://redis.io/docs/latest/operate/rc/subscriptions/maintenance/set-maintenance-windows). 

Review the [7.2 breaking changes](https://redis.io/docs/latest/operate/rc/changelog/2023/june-2023#redis-72-breaking-changes) or [7.4 breaking changes](https://redis.io/docs/latest/operate/rc/changelog/2024/july-2024#redis-74-breaking-changes) before you request to upgrade.
