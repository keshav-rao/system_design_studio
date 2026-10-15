# Redis Enterprise Software Release Notes 5.5 Preview (April 2019)

```json metadata
{
  "schema_version": 2,
  "title": "Redis Enterprise Software Release Notes 5.5 Preview (April 2019)",
  "description": "Preview release. Databases support multiple modules.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"new-features","title":"New features"},{"id":"preview-considerations","title":"Preview considerations"},{"id":"installation-instructions","title":"Installation instructions"}]}

,
  "codeExamples": []
}
```

Redis Enterprise Software (RS) 5.5 Preview Edition is now available.

RS 5.5 is a preview version that includes all the capabilities of Redis Enterprise 5.4,
plus support for creation of Redis databases with multiple modules and support for these modules:

- RediSearch (GA)
- RedisGraph (GA)
- RedisBloom (GA)
- RedisJSON (GA)
- RedisAI (Preview Version)
- RedisTimeSeries (Preview Version)
- RedisGears (Preview Version)

## New features

RS 5.5 lets you create Redis databases with multiple Redis modules.



## Preview considerations

This preview version is a standalone version and is not supported for production environments.
You cannot upgrade to it from a lower version or upgrade from it to a higher version.
Unexpected behaviors/issues found in this release will be addressed in future releases.

This preview version is not supported for networks that are isolated from the internet.

## Installation instructions

To set up a cluster with nodes that can host databases with multiple modules, you must follow this procedure on each node in the cluster:

1. [Install RS 5.5](https://redis.io/docs/latest/operate/rs/installing-upgrading/quickstarts/redis-enterprise-software-quickstart).
1. To install the modules, run: `sudo ./install-modules.sh`
1. Either:
    - Set up the node as the [first node in the cluster](https://redis.io/docs/latest/operate/rs/clusters/new-cluster-setup).
    - [Join the node to an existing cluster](https://redis.io/docs/latest/operate/rs/clusters/add-node).

