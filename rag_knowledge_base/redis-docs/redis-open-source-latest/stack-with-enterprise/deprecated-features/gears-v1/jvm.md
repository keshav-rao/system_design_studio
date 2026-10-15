# RedisGears JVM plugin

```json metadata
{
  "schema_version": 2,
  "title": "RedisGears JVM plugin",
  "description": "The RedisGears JVM plugin allows you to run RedisGears functions in the Java virtual machine.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"more-info","title":"More info"}]}

,
  "codeExamples": []
}
```


With the [RedisGears JVM plugin](https://github.com/RedisGears/JVMPlugin), you can write RedisGears functions in [Java](https://en.wikipedia.org/wiki/Java_(programming_language)) and run them on a [Redis Software](https://redis.io/docs/latest/operate/rs) cluster. It currently supports [JVM](https://en.wikipedia.org/wiki/Java_virtual_machine) version 11.

Similar to the Python plugin, the JVM plugin allows both batch processing and event-driven processing.

Before you can run RedisGears with Java, you will need to [install the RedisGears module and the JVM plugin](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/installing-redisgears#install-redisgears) on your Redis Software cluster and [enable them for your database](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/install).

Once you have written your code, compile and package it into a [JAR](https://en.wikipedia.org/wiki/JAR_(file_format)) file and upload it to a node on your Redis Software cluster. Use the `RG.JEXECUTE` command with the `redis-cli` command-line tool to run your code.

## More info

- [RedisGears JVM quick start](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/quickstart)
- [RedisGears Java classes and functions](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes)
- [RedisGears recipes](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/recipes)
