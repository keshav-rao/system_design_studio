# System logs

```json metadata
{
  "schema_version": 2,
  "title": "System logs",
  "description": "You can view and export system logs to track any activity associated with your subscriptions and databases.",
  "categories": ["docs","operate","rc"],
  "tableOfContents": {"sections":[{"id":"get-system-logs-using-rest-api","title":"Get system logs using REST API"}]}

,
  "codeExamples": []
}
```

The **Logs** page contains events, alerts, and logs from the activities, databases, and subscriptions associated with your account.

![Choose the Logs page from the Redis Cloud console menu to view your subscription system log.](https://redis.io/docs/latest/images/rc/system-logs.png)

You can:

* Sort the list by a specific field in descending or ascending order. Supported fields include *Time*, *Originator*, *Database name*, *API key name*, and *Activity*.

    ![Use the arrows in the list header to sort the list.](https://redis.io/docs/latest/images/rc/icon-list-sort-asc.png#no-click)&nbsp;![The direction of the arrow corresponds to the direction of the sort.](https://redis.io/docs/latest/images/rc/icon-list-sort-desc.png#no-click)    
    
    Select the arrow icon to change the sort order.  You can only sort by one field at a time.

* Use the **Export all** button to export all logs as a comma-separated values (CSV) file for use in other systems and programs.

    ![Use the export all button in the top right to export all logs to a CSV file](https://redis.io/docs/latest/images/rc/system-logs-export.png)

* Use the refresh button to refresh the system logs.

    ![Use the refresh button in the top right to refresh the system logs](https://redis.io/docs/latest/images/rc/system-logs-refresh.png)

* Use the search bar to search for specific entries. Supported fields include *Originator*, *Database name*, *API key name*, *Activity*, and *Description*.

## Get system logs using REST API

Use [`GET /logs`](https://redis.io/docs/latest/operate/rc/api/api-reference#tag/Account/operation/getAccountSystemLogs) to get the system logs using the REST API. See [Audit system logs](https://redis.io/docs/latest/operate/rc/api/examples/audit-system-logs) for more information.
