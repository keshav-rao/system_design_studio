# Register events

```json metadata
{
  "schema_version": 2,
  "title": "Register events",
  "description": "Register RedisGears functions to run when certain events occur in a Redis database.",
  "categories": ["docs","operate","stack"],
  "tableOfContents": {"sections":[{"id":"register-on-events","title":"Register on events"},{"id":"event-types","title":"Event types"},{"id":"active-active-event-types","title":"Active-Active event types"}]}

,
  "codeExamples": []
}
```


You can register RedisGears functions to run when certain events occur in a Redis database.

## Register on events

To register RedisGears functions to run on an event, your code needs to:

1. Pass `KeysReader` to a `GearsBuilder` object.

1. Call the `GearsBuilder.register()` function.

1. Pass the `eventTypes` parameter to either:

    - The `register` function for Python.
    
    - The `KeysReader` object for Java.

For more information and examples of event registration, see:

- Java references:

    - [`KeysReader`](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/readers/keysreader)

    - [`GearsBuilder.register()`](https://redis.io/docs/latest/operate/oss_and_stack/stack-with-enterprise/deprecated-features/gears-v1/jvm/classes/gearsbuilder/register)

## Event types

For the list of event types you can register on, see the [Redis keyspace notification documentation](https://redis.io/docs/latest/develop/pubsub/keyspace-notifications#events-generated-by-different-commands).

## Active-Active event types

In addition to standard Redis [events](https://redis.io/docs/latest/develop/pubsub/keyspace-notifications#events-generated-by-different-commands), [Redis Software Active-Active databases](https://redis.io/docs/latest/operate/rs/databases/active-active) also support the registration of RedisGears functions for the following event types:

- `change`: This event occurs when a key changes on another replica of the Active-Active database.

