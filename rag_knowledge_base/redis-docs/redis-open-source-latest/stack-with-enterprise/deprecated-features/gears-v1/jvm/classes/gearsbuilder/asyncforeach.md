# AsyncForeach

```json metadata
{
  "schema_version": 2,
  "title": "AsyncForeach",
  "description": "For each record in the pipe, asynchronously runs some operations.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"parameters","title":"Parameters"},{"id":"returns","title":"Returns"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


```java
public GearsBuilder<T> asyncForeach​(
    gears.operations.AsyncForeachOperation<T> foreach)
```

The `asyncForeach` function allows you to use a [`GearsFuture`](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsfuture) object to define a set of operations and run them asynchronously for each record in the pipe.

## Parameters

| Name | Type | Description |
|------|------|-------------|
| foreach | AsyncForeachOperation<T> | The set of operations to run for each record |

## Returns

Returns a GearsBuilder object with a new template type.

## Example

```java
GearsBuilder.CreateGearsBuilder(reader).map(r->r.getKey()).
	asyncForeach(r->{
		GearsFuture<Serializable> f = new GearsFuture<Serializable>();
		new Thread(new Runnable() {
				
			@Override
			public void run() {
				try {
					Thread.sleep(1);
						
					f.setResult(r);
				} catch (Exception e) {
					e.printStackTrace();
				}					
			}
		}).start();
		return f;
});
```
