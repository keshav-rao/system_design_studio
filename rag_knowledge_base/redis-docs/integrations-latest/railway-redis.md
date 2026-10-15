# Redis on Railway

```json metadata
{
  "schema_version": 2,
  "title": "Redis on Railway",
  "description": "Deploy and host Redis on Railway. The Railway Redis database template allows you to provision and connect to a Redis database with zero configuration.",
  "categories": ["docs","integrate","oss","rs"],
  "group": "cloud-service",
  "tableOfContents": {"sections":[{"id":"deploy-redis-to-railway","title":"Deploy Redis to Railway"},{"id":"connecting-to-your-railway-redis-service","title":"Connecting to your Railway Redis Service"},{"id":"backup-and-monitoring","title":"Backup and Monitoring"},{"id":"additional-resources","title":"Additional Resources"}]}

,
  "codeExamples": []
}
```


[Railway](https://railway.com?utm_medium=integration&utm_source=docs&utm_campaign=redis) simplifies your infrastructure stack from databases to servers to observability with a single, scalable, easy-to-use platform. Companies of all sizes deploy full-stack applications on Railway and benefit from highly performant networking, intuitive vertical and horizontal scaling, and isolated environments with pull request deploys. Railway's template marketplace includes thousands of one-click deploy templates, including Redis.

![](https://redis.io/docs/latest/images/rc/railway-redis-canvas.png)

This is a guide to deploying Redis on Railway, using the official template.

## Deploy Redis to Railway

Navigate to a new Railway project at [railway.com/new](https://railway.com/new?utm_medium=integration&utm_source=docs&utm_campaign=redis). Add a Redis database to your project via the `ctrl / cmd + k` menu, and type `Redis`.

You can also deploy it via the [template](https://railway.com/deploy/redis) from the Railway template marketplace.

![](https://redis.io/docs/latest/images/rc/railway-redis-add.gif)

Upon deployment, you will have a Redis service running in your project, deployed from the [redis](https://hub.docker.com/_/redis) Docker image.

Since the deployed container is pulled from the [redis](https://hub.docker.com/_/redis) image in Docker Hub, you can modify the deployment based on the [instructions in Docker Hub](https://hub.docker.com/_/redis).

## Connecting to your Railway Redis Service

It is possible to connect to Redis externally by using the [TCP Proxy](https://docs.railway.com/deploy/exposing-your-app?utm_medium=integration&utm_source=docs&utm_campaign=redis#tcp-proxying) which is enabled by default.

## Backup and Monitoring

Especially for production environments, performing backups and monitoring the health of your data is essential. Consider adding:

- **Backups**: Automate regular backups to ensure data recovery in case of failure. We suggest checking out Railway's native [Backups](https://docs.railway.com/reference/backups?utm_medium=integration&utm_source=docs&utm_campaign=redis) feature.

- **Observability**: Implement monitoring for insights into performance and health of your Redis cluster. You can integrate a Redis exporter for Prometheus, although we do not provide a specific template at this time.

## Additional Resources

- [Railway Redis guide](https://docs.railway.com/guides/redis?utm_medium=integration&utm_source=docs&utm_campaign=redis)
- [Railway platform features](https://railway.com/features?utm_medium=integration&utm_source=docs&utm_campaign=redis)
