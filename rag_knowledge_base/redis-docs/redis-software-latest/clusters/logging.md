# Logging events

```json metadata
{
  "schema_version": 2,
  "title": "Logging events",
  "description": "Management actions performed with Redis Software are logged to make sure system management tasks are appropriately performed or monitored by administrators and for compliance with regulatory standards.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"view-logs-in-the-ui","title":"View logs in the UI"},{"id":"view-logs-on-the-server","title":"View logs on the server"},{"id":"configure-log-timestamps","title":"Configure log timestamps"}]}

,
  "codeExamples": []
}
```

Management actions performed with Redis Software are logged to make sure system management tasks are appropriately performed or monitored by administrators and for compliance with regulatory standards.

Log entries contain the
following information:

1. Who performed the action?
1. What exactly was the performed action?
1. When was the action performed?
1. Did the action succeed or not?

To get the list of logged events, you can use the REST API or
the **Logs** screen in the UI. The **Logs** screen displays the system and user
events regarding alerts, notifications, and configuration.

![Logs screen in the new Cluster Manager UI.](https://redis.io/docs/latest/images/rs/screenshots/cluster/cluster-logs.png)

You can use the **Logs** screen to review what actions a user has performed, such as editing a database's configuration.

- [Redis slow
    log](https://redis.io/docs/latest/operate/rs/clusters/logging/redis-slow-log)
- [rsyslog logging](https://redis.io/docs/latest/operate/rs/clusters/logging/rsyslog-logging)

## View logs in the UI

Redis Software provides log files for auditing cluster management actions and troubleshooting. You can view these logs in the UI and on the host operating system.

To view event logs in the new Cluster Manager UI, go to **Cluster > Logs**.

## View logs on the server

Server logs can be found by default in the directory `/var/opt/redislabs/log/`.

These log files are used by the Redis support team to troubleshoot issues. The logs you will most frequently interact with is 'event_log.log'. This log file is where logs of configuration actions within Redis are stored and is useful to determine events that occur within Redis Software.

## Configure log timestamps

Redis Software allows you to configure log timestamps. To configure log timestamps in the new Cluster Manager UI:

1. Go to **Cluster > Configuration > General**.

1. Change the **Time zone** for the logs based on your location.

