# Redis Agent Memory REST API quickstart

```json metadata
{
  "schema_version": 2,
  "title": "Redis Agent Memory REST API quickstart",
  "description": "Explore session memory, automatic extraction, summarization, custom memory types, and sensitive-data exclusions with the Redis Agent Memory REST API.",
  "categories": ["docs","develop","ai"],
  "tableOfContents": {"sections":[{"id":"before-you-begin","title":"Before you begin"},{"id":"create-a-redis-agent-memory-service","title":"Create a Redis Agent Memory service"},{"id":"save-the-connection-values","title":"Save the connection values"},{"id":"check-the-service-health","title":"Check the service health"},{"id":"1-build-conversation-context-with-session-memory","title":"1. Build conversation context with session memory"},{"id":"2-recall-automatically-extracted-information","title":"2. Recall automatically extracted information"},{"children":[{"id":"add-conversation-turns","title":"Add conversation turns"},{"id":"retrieve-the-summarized-session","title":"Retrieve the summarized session"}],"id":"3-keep-long-conversations-concise-with-automatic-summarization","title":"3. Keep long conversations concise with automatic summarization"},{"id":"4-extract-business-specific-data-with-a-custom-memory-type","title":"4. Extract business specific data with a custom memory type"},{"id":"5-guide-extraction-away-from-sensitive-data","title":"5. Guide extraction away from sensitive data"},{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": []
}
```


Use this quickstart to follow a travel planning conversation through Redis Agent Memory. You will retrieve the conversation from session memory, recall information extracted in the background, inspect an automatically generated session summary, extract structured travel information, and guide extraction away from sensitive data.

## Before you begin

To complete this quickstart, you need:

* A Redis Cloud account that can create Redis Agent Memory services.
* An eligible Redis Cloud database, or permission to create one.
* A shell with `curl` and `jq` installed.

## Create a Redis Agent Memory service

1. Sign in to the [Redis Cloud console](https://cloud.redis.io/).
1. Select **Agent Memory** from the navigation menu.
1. If Redis Cloud displays the public preview terms, review and accept them.
1. Select **Create custom service**.
1. Enter a service name, select an eligible database, and select its `default` user.
1. Under **Memory configuration**, enter these values:

    | Setting | Value | What it controls |
    |:--------|:------|:-----------------|
    | **Short-term TTL** | `1` day | How long session memory is retained. |
    | **Long-term TTL** | `365` days | How long long-term memories are retained. |
    | **Extraction cadence** | `1` minute | How often session events are processed for extraction. One minute is for this quickstart; use a longer production interval unless you need rapid extraction. |
    | **Automatic summarization** | Enabled | Whether older session events are condensed into a summary. |
    | **Summarize after (messages)** | `6` | The event count that triggers summarization. Six is for this quickstart; use a higher production threshold. |
    | **Keep most recent (messages)** | `2` | How many recent events remain in full. Two is for this quickstart; retain more in production when recent turns are needed. |

1. Under **Memory types & extraction**, select **Add type** and configure this custom memory type:

    | Setting | Value | What it controls |
    |:--------|:------|:-----------------|
    | **Name** | `trip_preference` | The identifier stored in `memoryType` and used in search filters. |
    | **Description** | `Structured requirements for a planned trip` | The purpose of the custom memory type. |
    | **Extraction prompt** | `Extract trip requirements only when the user states a destination or travel plan. Preserve explicit dietary requirements and food preferences.` | When to create the memory and which information to capture. |
    | **Enabled** | Enabled | Whether new memories of this type are extracted. |

1. Add these custom fields:

    | Field | Type | Description |
    |:------|:-----|:------------|
    | `destinations` | `list[str]` | Cities or countries the user plans to visit. |
    | `travel_period` | `str` | When the user plans to travel. |
    | `dietary_requirements` | `list[str]` | Dietary requirements that affect recommendations. |
    | `food_preferences` | `list[str]` | Cuisines, flavors, or dining preferences stated by the user. |

1. Under **Sensitive-data exclusions**, enable **Semantic exclusions** and enter this exclusion prompt:

    ```text
    Do not keep passwords, access tokens, recovery codes, payment card information, or booking confirmation codes in long-term memory.
    ```

1. Select **Create**.
1. Copy the Redis Agent Memory API key and store it securely.

> [!WARNING]
> Redis Cloud displays the Redis Agent Memory API key only once. If you lose it, [generate a new API key](https://redis.io/docs/latest/operate/iris/agent-memory/view-service#replace-service-api-key).

These settings keep the background stages short enough to observe during the quickstart. For screenshots and configuration details, see [create a Redis Agent Memory service](https://redis.io/docs/latest/operate/iris/agent-memory/create-service).

> [!WARNING]
> Sensitive-data exclusions guide the extraction model but do not guarantee exclusion. Sensitive session content still reaches the model provider. Exclusions do not apply when an application creates long-term memories directly.


## Save the connection values

1. Open the Redis Agent Memory service in the Redis Cloud console.
1. On the **Configuration** tab, copy the **Endpoint** and **Store ID**.
1. Export the values in your shell:

    ```sh
    export AGENT_MEMORY_URL='<ENDPOINT>'
    export STORE_ID='<STORE_ID>'
    export API_KEY='<API_KEY>'
    export SESSION_ID='travel-planning-session'
    export OWNER_ID='quickstart-user'
    ```

`AGENT_MEMORY_URL` must include `https://`. Keep the API key out of source control, application logs, and other unsecured locations.

## Check the service health

Verify that the service is available:

```sh
curl --fail-with-body --silent --show-error \
  --header "Authorization: Bearer $API_KEY" \
  "$AGENT_MEMORY_URL/health" | jq
```

## 1. Build conversation context with session memory

Session memory stores a conversation as an ordered sequence of events. Add a user message that contains details the travel agent will need later:

```sh
export EVENT_CREATED_AT="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"

curl --fail-with-body --silent --show-error \
  --request POST \
  --header "Authorization: Bearer $API_KEY" \
  --header 'Content-Type: application/json' \
  --data @- \
  "$AGENT_MEMORY_URL/v1/stores/$STORE_ID/session-memory/events" <<JSON | jq
{
  "sessionId": "$SESSION_ID",
  "actorId": "$OWNER_ID",
  "role": "USER",
  "content": [
    {
      "text": "I am visiting Tokyo and Kyoto next month. I am vegetarian and prefer spicy food."
    }
  ],
  "createdAt": "$EVENT_CREATED_AT"
}
JSON
```

Retrieve the session:

```sh
curl --fail-with-body --silent --show-error \
  --header "Authorization: Bearer $API_KEY" \
  "$AGENT_MEMORY_URL/v1/stores/$STORE_ID/session-memory/$SESSION_ID" | jq
```

The `events` array contains the stored message, its role, actor, and timestamps. An application can retrieve this session before the next agent turn and add the events to the model's context.

> [!NOTE]
> **What to expect:** The `events` array contains the travel message. Redis Agent Memory adds an `eventId` and `systemTimestamp`, showing that the application can recover the complete event later using only the session ID.

## 2. Recall automatically extracted information

Redis Agent Memory processes session events in the background and creates long term memories for information that may be useful in later conversations. You configured the extraction cadence to one minute when you created the service. You do not need to submit a separate memory creation request.

Wait at least one minute, then search for the user's dietary requirements:

```sh
curl --fail-with-body --silent --show-error \
  --request POST \
  --header "Authorization: Bearer $API_KEY" \
  --header 'Content-Type: application/json' \
  --data @- \
  "$AGENT_MEMORY_URL/v1/stores/$STORE_ID/long-term-memory/search" <<JSON | jq
{
  "text": "What dietary requirements and food preferences does the user have?",
  "filter": {
    "ownerId": {
      "eq": "$OWNER_ID"
    }
  },
  "limit": 5
}
JSON
```

The `items` array should contain memories derived from the conversation, such as the vegetarian requirement or preference for spicy food. Extraction is asynchronous, so run the search again if the array is empty.

> [!NOTE]
> **What to expect:** Results similar to `User is a vegetarian` and `User prefers spicy food`. Your application did not create these memories directly. Redis Agent Memory derived them from the session event. The exact text and memory types can vary.

The extracted memory remains searchable after the session expires, subject to the long term memory TTL. You can change the extraction cadence and both TTLs in the [Redis Agent Memory service configuration](https://redis.io/docs/latest/operate/iris/agent-memory/create-service#memory-configuration).

## 3. Keep long conversations concise with automatic summarization

Automatic summarization condenses older events and retains the most recent events in full. The retrieved session then contains a `summary` object and the recent `events` array, so the application can provide useful history without filling the model's context window with every original message.

You enabled automatic summarization when you created the service. When the session reaches six events, Redis Agent Memory summarizes the older events and retains the two most recent events in full.

### Add conversation turns

Add enough user and assistant events to reach the configured threshold. Use the request from the first step and change `role`, `actorId`, `content`, and `createdAt` for each event. The Python and TypeScript quickstarts use six additional turns about travel dates, restaurant style, and budget.

Summarization runs in the background after the session reaches the threshold.

### Retrieve the summarized session

After a short wait, retrieve the session again:

```sh
curl --fail-with-body --silent --show-error \
  --header "Authorization: Bearer $API_KEY" \
  "$AGENT_MEMORY_URL/v1/stores/$STORE_ID/session-memory/$SESSION_ID" | jq
```

Repeat the retrieval after a short wait if `summary` is not present. Compare `summary.text` with the recent events. The summary should preserve earlier decisions about the trip while recent turns remain available in full.

> [!NOTE]
> **What to expect:** A `summary` object that preserves details such as Tokyo, Kyoto, the travel dates, and food preferences. `summarizedUpToEventId` identifies the last event covered by the summary, while `events` contains the newer turns that remain in full. The exact summary text can vary.

See [automatic summarization configuration](https://redis.io/docs/latest/operate/iris/agent-memory/create-service#automatic-summarization) for details.

## 4. Extract business specific data with a custom memory type

Built in memories preserve generally useful information. Custom memory types let an application extract structured information for its business domain. You configured `trip_preference` when you created the service, so it processed the same travel planning event independently.

Search for the structured memory:

```sh
curl --fail-with-body --silent --show-error \
  --request POST \
  --header "Authorization: Bearer $API_KEY" \
  --header 'Content-Type: application/json' \
  --data @- \
  "$AGENT_MEMORY_URL/v1/stores/$STORE_ID/long-term-memory/search" <<JSON | jq
{
  "text": "What are the requirements for the user's trip?",
  "filter": {
    "ownerId": {
      "eq": "$OWNER_ID"
    },
    "memoryType": {
      "eq": "trip_preference"
    }
  },
  "limit": 5
}
JSON
```

The result uses `trip_preference` as its `memoryType` and contains travel information extracted from the conversation. The exact text and returned fields depend on the conversation, extraction model, and client.

> [!NOTE]
> **What to expect:** A result with `memoryType` set to `trip_preference` that combines the destinations, travel period, and dietary preferences. This shows that the custom type processed the same conversation independently from the built-in memory types.

See [custom memory types](https://redis.io/docs/latest/operate/iris/agent-memory/create-service#custom-memory-types) for configuration requirements and limits.

## 5. Guide extraction away from sensitive data

The semantic exclusion prompt tells Redis Agent Memory which information should not be kept in long-term memory. Add an event containing a fictional booking code and information that is safe to retain:

```sh
export EVENT_CREATED_AT="$(date -u +'%Y-%m-%dT%H:%M:%SZ')"

curl --fail-with-body --silent --show-error \
  --request POST \
  --header "Authorization: Bearer $API_KEY" \
  --header 'Content-Type: application/json' \
  --data @- \
  "$AGENT_MEMORY_URL/v1/stores/$STORE_ID/session-memory/events" <<JSON | jq
{
  "sessionId": "$SESSION_ID",
  "actorId": "$OWNER_ID",
  "role": "USER",
  "content": [
    {
      "text": "I booked Hotel Sakura in Tokyo. For this example, the fictional booking confirmation code is DEMO-7QX9."
    }
  ],
  "createdAt": "$EVENT_CREATED_AT"
}
JSON
```

Wait at least one minute and search for the safe hotel information:

```sh
curl --fail-with-body --silent --show-error \
  --request POST \
  --header "Authorization: Bearer $API_KEY" \
  --header 'Content-Type: application/json' \
  --data @- \
  "$AGENT_MEMORY_URL/v1/stores/$STORE_ID/long-term-memory/search" <<JSON | jq
{
  "text": "Where is the user staying in Tokyo?",
  "filter": {
    "ownerId": {
      "eq": "$OWNER_ID"
    }
  },
  "limit": 5
}
JSON
```

Inspect the returned memories. They can retain the hotel name, but should not contain `DEMO-7QX9` because the exclusion prompt covers booking confirmation codes.

> [!NOTE]
> **What to expect:** A memory similar to `User booked Hotel Sakura in Tokyo` without the fictional confirmation code. If the code appears, refine the exclusion prompt and test again. Exclusions remain advisory.

> [!WARNING]
> Semantic exclusions are advisory and do not guarantee that sensitive information is excluded. Session content still reaches the extraction model provider. Do not use real sensitive data in this exercise. Exclusions do not apply to directly created long-term memories.

See [sensitive-data exclusions](https://redis.io/docs/latest/operate/iris/agent-memory/create-service#sensitive-data-exclusions) for configuration details.

## Next steps

* Follow the [Python SDK quickstart](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory/python-sdk-quickstart) or [TypeScript SDK quickstart](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory/typescript-sdk-quickstart).
* Learn when to [create long term memories directly](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory/developer-guide#create-long-term-memories).
* Use the [Redis Agent Memory API reference](https://redis.io/docs/latest/develop/ai/context-engine/agent-memory/api-reference) for endpoint and schema details.

