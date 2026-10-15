# ConfigGet

```json metadata
{
  "schema_version": 2,
  "title": "ConfigGet",
  "description": "Gets the value of a RedisGears configuration setting.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"parameters","title":"Parameters"},{"id":"returns","title":"Returns"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


```java
public static java.lang.String configGet​(java.lang.String key)
```

Gets the value of a RedisGears [configuration setting](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/triggers-and-functions/Configuration).

> [!NOTE]
> You can set configuration values when you load the module or use the `RG.CONFIGSET` command.

## Parameters

| Name | Type | Description |
|------|------|-------------|
| key | string | The configuration setting to get |

## Returns

Returns the configuration value of a RedisGears configuration setting.

## Example

```java
GearsBuilder.configGet("ExecutionMaxIdleTime");
```
