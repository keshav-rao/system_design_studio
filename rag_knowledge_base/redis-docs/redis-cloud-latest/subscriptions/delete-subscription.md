# Delete a subscription

```json metadata
{
  "schema_version": 2,
  "title": "Delete a subscription",
  "description": "",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[]}

,
  "codeExamples": []
}
```


> [!NOTE]
> Once a subscription is deleted, it cannot be recovered. We recommend [backing up your data](https://redis.io/docs/latest/operate/rc/databases/back-up-data) before removing databases or subscriptions.

To delete a subscription:

1.  [Delete all databases](https://redis.io/docs/latest/operate/rc/databases/delete-database) from the subscription.

    The number of databases for the subscription is shown in the subscription list. You cannot delete a subscription until there are zero databases in the subscription.

    ![The number of databases is shown in the bottom, left of the subscription in the subscription list.](https://redis.io/docs/latest/images/rc/subscription-list-pro-no-databases.png)

2.  View the subscription details.  

    If you have more than one subscription, select the target subscription from the subscription list.

3.  Select the **Overview** tab.

    ![The Overview tab displays the details of your subscription.](https://redis.io/docs/latest/images/rc/subscription-details-overview-flexible.png)

4.  Select the **Delete subscription** button.

    ![Use the Delete subscription button to delete your subscription plan.](https://redis.io/docs/latest/images/rc/button-subscription-delete.png)

    ![Select the Yes, cancel button to confirm the subscription cancellation.](https://redis.io/docs/latest/images/rc/subscription-delete-confirm-dialog.png)


5.  Select the **Delete subscription** button to confirm your choice.

