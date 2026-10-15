# AsyncMap

```json metadata
{
  "schema_version": 2,
  "title": "AsyncMap",
  "description": "Asynchronously maps records one-to-one.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"parameters","title":"Parameters"},{"id":"returns","title":"Returns"},{"id":"example","title":"Example"}]}

,
  "codeExamples": []
}
```


```java
public <I extends java.io.Serializable> GearsBuilder<I> asyncMap​(
	gears.operations.AsyncMapOperation<T,​I> mapper)
```

The `asyncMap` function allows you to use a [`GearsFuture`](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsfuture) object to asynchronously map each input record in the pipe to an output record, one-to-one.

## Parameters
 
Type parameters:

| Name | Description |
|------|-------------|
| I | The template type of the returned builder |

Function parameters:

| Name | Type | Description |
|------|------|-------------|
| mapper | <nobr>AsyncMapOperation<T,​I></nobr> | For each input record, returns a new output record |

## Returns

Returns a GearsBuilder object with a new template type.

## Example

```java
GearsBuilder.CreateGearsBuilder(reader).
	asyncMap(r->{
		GearsFuture<String> f = new GearsFuture<String>();
		new Thread(new Runnable() {
				
			@Override
			public void run() {
				try {
					Thread.sleep(1);
					
					f.setResult("done");
				} catch (Exception e) {
					e.printStackTrace();
				}					
			}
		}).start();
		return f;
});
```

