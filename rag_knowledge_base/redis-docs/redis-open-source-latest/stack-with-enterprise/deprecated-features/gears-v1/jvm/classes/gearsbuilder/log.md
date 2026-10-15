# Log

```json metadata
{
  "schema_version": 2,
  "title": "Log",
  "description": "Writes a log message to the Redis log file.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"parameters","title":"Parameters"},{"id":"returns","title":"Returns"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


```java
public static void log​(java.lang.String msg)

public static void log​(java.lang.String msg, LogLevel level)
```

Writes a log message to the Redis log file. If you do not specify a `LogLevel`, it will default to `NOTICE`.

## Parameters

| Name | Type | Description |
|------|------|-------------|
| msg | string | The message to write to the log |
| level | LogLevel | The log level (DEBUG, NOTICE, VERBOSE, WARNING) |

## Returns

None

## Example

```java
GearsBuilder.log(
    "Setting keys to expire after 1 month", 
    LogLevel.WARNING
);
```
