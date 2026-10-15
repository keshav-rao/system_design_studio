# Manage database tags

```json metadata
{
  "schema_version": 2,
  "title": "Manage database tags",
  "description": "",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"children":[{"id":"configuration-tab","title":"Open tag manager from the Configuration tab"},{"id":"database-list","title":"Open tag manager from the database list"},{"id":"tag-manager","title":"Use the tag manager"}],"id":"manage-tags","title":"Manage tags"}]}

,
  "codeExamples": []
}
```


Tags are key-value pairs that let you categorize your databases. You can create tags and add them to your databases to associate them with each other. Once you've added tags, you can filter your databases in the [database list](https://redis.io/docs/latest/operate/rc/databases/view-edit-database#manage-the-database-list) or in the [cost report](https://redis.io/docs/latest/operate/rc/billing-and-payments/cost-report) by tag key or value. 

## Manage tags

You can manage tags from the [Redis Cloud console](https://cloud.redis.io/#/) in the [tag manager](#tag-manager). You can find the tag manager in the following places: 

- [From your database in the **Configuration** tab](#configuration-tab)
- [From the database list](#database-list)

After you open the [tag manager](#tag-manager), you can use it to add, edit, or delete tags.

### Open tag manager from the Configuration tab {#configuration-tab}

To learn how to navigate to your database, see [View and edit databases](https://redis.io/docs/latest/operate/rc/databases/view-edit-database). Select the **Configuration** tab to view the tags that are set for your database. For Essentials databases, the **Manage tags** button is at the top of the tab; for Pro databases, go to the **General** section.

![The Configuration tab of the Database details screen.](https://redis.io/docs/latest/images/rc/database-details-configuration-tab-general-flexible.png)

Select **Manage Tags** to open the [tag manager](#tag-manager).

![The Manage tags button.](https://redis.io/docs/latest/images/rc/tags-button-manage-tags.png)

### Open tag manager from the database list {#database-list}

Using the database list allows you to manage tags for multiple databases without having to go into each database's **Tags** tab.

To get to the database list, select **Databases** from the main menu. 

![The database list with databases that are tagged.](https://redis.io/docs/latest/images/rc/tags-database-list.png)

Hover over the database and select **Manage tags**, or select **More actions** > **Manage tags** to open the [tag manager](#tag-manager).

![Manage tags button.](https://redis.io/docs/latest/images/rc/tags-icon-manage-tags.png#no-click)
![More actions button.](https://redis.io/docs/latest/images/rc/tags-icon-more-actions.png#no-click)

### Use the tag manager {#tag-manager}

The tag manager shows any tags that are associated with the database and allows you to create, edit, or delete tags.

![The tag manager.](https://redis.io/docs/latest/images/rc/tags-tag-manager.png)

You can select the tag's **Key** and **Value** from the suggestions, or you can enter your own.

![The New tag fields.](https://redis.io/docs/latest/images/rc/tags-new-tag.png)

A valid tag must follow these guidelines:
- Tag keys must be between 1 and 64 characters long, and values must be at least 1 character long.
- Tags can only have lowercase letters, numbers, spaces, and these special characters: `-`, `_`, `.`, `+`, `@`, and `:`.

After you add your first tag, you can:

- Select the **Key** or **Value** field of an existing tag and enter new text to edit it.

- Select **Delete** next to a tag to delete it.

    ![Delete button.](https://redis.io/docs/latest/images/rc/icon-delete-lb.png)

- Select **Add additional tag** to add another tag.

    ![The Add additional tag button.](https://redis.io/docs/latest/images/rc/tags-button-add-additional-tag.png)

Select **Save tags** to save your changes.

![The Save tags button.](https://redis.io/docs/latest/images/rc/tags-button-save-tags.png)

