# RedisGears Python plugin

```json metadata
{
  "schema_version": 2,
  "title": "RedisGears Python plugin",
  "description": "The RedisGears Python plugin allows you to run RedisGears functions with Python.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"more-info","title":"More info"}]}

,
  "codeExamples": []
}
```


With the RedisGears Python plugin, you can write RedisGears functions in [Python](https://www.python.org/) and run them on a [Redis Software](https://redis.io/docs/latest/operate/rs) cluster.

The Python plugin allows both batch processing and event-driven processing.

Before you can run RedisGears with Python, you will need to [install the RedisGears module and the Python plugin](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/installing-redisgears#install-redisgears) on your Redis Software cluster and [enable them for your database](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/python/install).

Once you have written your code, upload it to a node on your Redis Software cluster. Use the `RG.PYEXECUTE` command with the `redis-cli` command-line tool to run your code.

## More info

- [RedisGears Python quick start](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/python/quickstart)
- [RedisGears recipes](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/python/recipes)
