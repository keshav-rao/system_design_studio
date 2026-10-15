# Hashtag

```json metadata
{
  "schema_version": 2,
  "title": "Hashtag",
  "description": "Returns a string that maps to the current shard.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"parameters","title":"Parameters"},{"id":"returns","title":"Returns"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


```java
public static java.lang.String hashtag()
```

Returns a string that maps to the current shard according to the cluster slot mapping.

> [!NOTE]
> You can use the `hashtag` function when you need to create a key that resides on the current shard. 

## Parameters

None

## Returns

Returns a string that maps to the current shard.

## Example

The following example uses the `hashtag` function to calculate the hslot. The string maps to the current shard.

```java
GearsBuilder.execute(
    "SET", 
    String.format("key{%s}", GearsBuilder.hashtag()), 
    "1"
);
```

