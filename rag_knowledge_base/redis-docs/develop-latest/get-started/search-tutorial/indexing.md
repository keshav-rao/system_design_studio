# Create an index

```json metadata
{
  "schema_version": 2,
  "title": "Create an index",
  "description": "Create a search index over your JSON documents with FT.CREATE, choose the right field types, and understand how Redis indexes arrays.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"what-an-index-does","title":"What an index does"},{"id":"field-types","title":"Field types"},{"id":"create-the-index","title":"Create the index"},{"id":"indexing-arrays-the--you-should-not-forget","title":"Indexing arrays: the [*] you should not forget"},{"id":"check-the-index","title":"Check the index"},{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": [{"codetabsId":"search_tutorial-stepload_data","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"}],"description":"Foundational: Load the tutorial dataset as JSON documents under a shared key prefix using JSON.SET","difficulty":"beginner","id":"load_data","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_search_tutorial-stepload_data"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_search_tutorial-stepload_data"}]},{"codetabsId":"search_tutorial-stepcreate_index","commands":[{"acl_categories":["@search"],"complexity":"O(K)","name":"FT.CREATE"}],"description":"Foundational: Create an index over JSON documents with FT.CREATE, mapping JSONPaths to TEXT, TAG, and NUMERIC fields","difficulty":"beginner","id":"create_index","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_search_tutorial-stepcreate_index"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_search_tutorial-stepcreate_index"}]},{"codetabsId":"search_tutorial-stepindex_info","commands":[{"acl_categories":["@search"],"complexity":"O(1)","name":"FT.INFO"}],"description":"Foundational: Inspect an index with FT.INFO to confirm it exists and see how many documents it contains","difficulty":"beginner","id":"index_info","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_search_tutorial-stepindex_info"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_search_tutorial-stepindex_info"}]}]
}
```

## Code Examples Legend

The code examples below show how to perform the same operations in different programming languages and client libraries:

- **Redis CLI**: Command-line interface for Redis
- **C# (Synchronous)**: StackExchange.Redis synchronous client
- **C# (Asynchronous)**: StackExchange.Redis asynchronous client
- **Go**: go-redis client
- **Java (Synchronous - Jedis)**: Jedis synchronous client
- **Java (Asynchronous - Lettuce)**: Lettuce asynchronous client
- **Java (Reactive - Lettuce)**: Lettuce reactive/streaming client
- **JavaScript (Node.js)**: node-redis client
- **PHP**: Predis client
- **Python**: redis-py client
- **Rust (Synchronous)**: redis-rs synchronous client
- **Rust (Asynchronous)**: redis-rs asynchronous client

Each code example demonstrates the same basic operation across different languages. The specific syntax and patterns vary based on the language and client library, but the underlying Redis commands and behavior remain consistent.

---


This is step 2 of the [Redis Search tutorial](https://redis.io/docs/latest/develop/get-started/search-tutorial).

Currently, you can fetch a product only if you already know its key. An **index** &mdash; also called a *secondary index*, because it's a lookup structure maintained alongside your primary data &mdash; changes that: it tells Redis which fields to track and how, so you can ask questions like "which products cost less than $100?" or "which ones mention *wireless*?" and get answers quickly.

## What an index does

When you create an index, you give Redis three things:

1. **What to index** &mdash; which keys belong to the index, selected by a key prefix (here, `product:`).
2. **The data type** &mdash; whether those keys hold hashes (`ON HASH`) or JSON documents (`ON JSON`).
3. **The schema** &mdash; which fields to index, the path to each one, and what type each field is.

Once the index exists, Redis keeps it up to date automatically. Any `product:` document you add or change after creating the index is indexed immediately, and the documents you loaded earlier are indexed right away.

## Field types

Redis Search has a few core field types. Choosing the right one for each field determines how you can query it:

| Field type | Use it for | Example query |
| --- | --- | --- |
| `TEXT` | Human language you want to search by words and partial matches. | find products whose description contains *wireless* |
| `TAG` | Exact-value labels and categories you filter on as a whole. | find products where category is exactly *Audio* |
| `NUMERIC` | Numbers you filter by range or sort by. | find products priced between 0 and 100 |
| `VECTOR` | Embeddings for similarity search (covered in the [last step](https://redis.io/docs/latest/develop/get-started/search-tutorial/vector-search)). | find products similar in meaning to a query |

For the catalog, a good mapping is: `name` and `description` are `TEXT` (you want word search), `brand` and `category` are `TAG` (exact labels), and `price`, `rating`, `review_count`, `stock`, and `release_year` are `NUMERIC`. The `features` field is a list of exact labels, so it is also a `TAG`.

## Create the index

<details><summary>Reload products data</summary>
Foundational: Load the tutorial dataset as JSON documents under a shared key prefix using JSON.SET

**Difficulty:** Beginner

**Commands:** JSON.SET

**Complexity:**
- JSON.SET: O(M+N)

**Available in:** Redis CLI, Python

##### Redis CLI

```
> JSON.SET product:1 $ '{"name":"Aurora AcousticPro Headphones","brand":"Aurora","category":"Audio","price":199.99,"rating":4.6,"features":["wireless","noise-cancelling","bluetooth"],"specs":{"color":"midnight black","weight_grams":268}}'
> JSON.SET product:2 $ '{"name":"Aurora BudsMini Earbuds","brand":"Aurora","category":"Audio","description":"Tiny true-wireless earbuds with a secure in-ear fit and sweat resistance for workouts. The compact charging case slips into a pocket and delivers three full recharges on the go.","price":89.99,"rating":4.3,"review_count":942,"stock":130,"release_year":2023,"features":["wireless","bluetooth","in-ear","water-resistant"],"specs":{"color":"pearl white","weight_grams":5,"warranty_years":1}}'
... output truncated for AI-facing Markdown ...
> JSON.SET product:12 $ '{"name":"Vista Action Cam 4K","brand":"Vista","category":"Cameras","description":"A pocket-sized action camera that shoots stabilized 4K video and is waterproof without a case. Mount it on a helmet or bike and capture your adventures in sharp detail.","price":299.0,"rating":4.3,"review_count":455,"stock":33,"release_year":2023,"features":["camera","4k","waterproof","wifi"],"specs":{"color":"black","weight_grams":128,"warranty_years":1}}'
```

##### Python

```python
catalog = [
    {
        "name": "Aurora AcousticPro Headphones",
        "brand": "Aurora",
        "category": "Audio",
        "description": (
            "Over-ear wireless headphones with active noise cancelling and a "
            "40-hour battery. Plush memory-foam earcups and a lightweight frame "
            "make them comfortable for all-day listening, whether you are "
            "commuting, working, or relaxing at home."
        ),
        "price": 199.99,
        "rating": 4.6,
        "review_count": 1284,
        "stock": 42,
        "release_year": 2024,
        "features": ["wireless", "noise-cancelling", "bluetooth", "over-ear"],
        "specs": {"color": "midnight black", "weight_grams": 268, "warranty_years": 2},
    },
    {
        "name": "Aurora BudsMini Earbuds",
        "brand": "Aurora",
        "category": "Audio",
        "description": (
            "Tiny true-wireless earbuds with a secure in-ear fit and sweat "
            "resistance for workouts. The compact charging case slips into a "
            "pocket and delivers three full recharges on the go."
        ),
        "price": 89.99,
        "rating": 4.3,
        "review_count": 942,
        "stock": 130,
        "release_year": 2023,
        "features": ["wireless", "bluetooth", "in-ear", "water-resistant"],
        "specs": {"color": "pearl white", "weight_grams": 5, "warranty_years": 1},
    },
    {
        "name": "Sonus Boom Portable Speaker",
        "brand": "Sonus",
        "category": "Audio",
        "description": (
            "A rugged portable Bluetooth speaker with deep bass and a waterproof "
            "shell. Toss it in a bag for the beach or a campsite and enjoy "
            "room-filling sound for up to 20 hours per charge."
        ),
        "price": 129.5,
        "rating": 4.5,
        "review_count": 512,
        "stock": 64,
        "release_year": 2024,
        "features": ["wireless", "bluetooth", "portable", "waterproof"],
        "specs": {"color": "slate gray", "weight_grams": 540, "warranty_years": 1},
    },
    {
        "name": "Pixma Vortex 15 Laptop",
        "brand": "Pixma",
        "category": "Computers",
        "description": (
            "A thin-and-light 15-inch laptop with a fast multi-core processor, "
            "16 GB of memory, and a speedy solid-state drive. The backlit keyboard "
            "and bright display make it a capable companion for work and study."
        ),
        "price": 1399.0,
        "rating": 4.7,
        "review_count": 318,
        "stock": 18,
        "release_year": 2024,
        "features": ["laptop", "ssd", "backlit-keyboard", "lightweight"],
        "specs": {"color": "space silver", "weight_grams": 1600, "warranty_years": 2},
    },
    {
        "name": "Pixma UltraView 27 Monitor",
        "brand": "Pixma",
        "category": "Computers",
        "description": (
            "A 27-inch 4K monitor with an IPS panel for accurate colors and wide "
            "viewing angles. A single USB-C cable carries video and power, keeping "
            "your desk tidy."
        ),
        "price": 329.99,
        "rating": 4.4,
        "review_count": 221,
        "stock": 27,
        "release_year": 2023,
        "features": ["monitor", "4k", "ips", "usb-c"],
        "specs": {"color": "black", "weight_grams": 5200, "warranty_years": 3},
    },
    {
        "name": "Clackr Mechanical Keyboard",
        "brand": "Clackr",
        "category": "Accessories",
        "description": (
            "A compact mechanical keyboard with tactile switches, per-key RGB "
            "lighting, and wireless connectivity. Hot-swappable switches let you "
            "tune the typing feel without soldering."
        ),
        "price": 119.0,
        "rating": 4.8,
        "review_count": 1502,
        "stock": 88,
        "release_year": 2024,
        "features": ["keyboard", "mechanical", "rgb", "wireless"],
        "specs": {"color": "graphite", "weight_grams": 720, "warranty_years": 2},
    },
    {
        "name": "Glide Pro Wireless Mouse",
        "brand": "Glide",
        "category": "Accessories",
        "description": (
            "An ergonomic wireless mouse with a high-precision sensor and a "
            "contoured shape that reduces wrist strain. A single charge lasts for "
            "weeks of everyday use."
        ),
        "price": 59.99,
        "rating": 4.2,
        "review_count": 869,
        "stock": 150,
        "release_year": 2022,
        "features": ["mouse", "wireless", "ergonomic"],
        "specs": {"color": "charcoal", "weight_grams": 98, "warranty_years": 1},
    },
    {
        "name": "Pulse Series 6 Smartwatch",
        "brand": "Pulse",
        "category": "Wearables",
        "description": (
            "A sleek smartwatch with built-in GPS, continuous heart-rate "
            "monitoring, and water resistance for swimming. Track workouts, sleep, "
            "and notifications from your wrist."
        ),
        "price": 249.0,
        "rating": 4.5,
        "review_count": 1733,
        "stock": 51,
        "release_year": 2024,
        "features": ["smartwatch", "gps", "heart-rate", "water-resistant"],
        "specs": {"color": "rose gold", "weight_grams": 38, "warranty_years": 1},
    },
    {
        "name": "Pulse Band Fitness Tracker",
        "brand": "Pulse",
        "category": "Wearables",
        "description": (
            "A lightweight fitness band that tracks steps, heart rate, and sleep "
            "stages. The slim screen shows daily progress and the battery lasts a "
            "full week between charges."
        ),
        "price": 79.99,
        "rating": 4.1,
        "review_count": 2210,
        "stock": 200,
        "release_year": 2023,
        "features": ["fitness-tracker", "heart-rate", "sleep-tracking"],
        "specs": {"color": "ocean blue", "weight_grams": 24, "warranty_years": 1},
    },
    {
        "name": "Lumi Glow Smart Bulb",
        "brand": "Lumi",
        "category": "Home",
        "description": (
            "A color-changing smart bulb that connects over Wi-Fi and works with "
            "voice assistants. Dim it for movie night or set a warm white for "
            "reading, all from your phone."
        ),
        "price": 24.99,
        "rating": 4.0,
        "review_count": 640,
        "stock": 320,
        "release_year": 2022,
        "features": ["smart-home", "wifi", "dimmable", "color"],
        "specs": {"color": "white", "weight_grams": 70, "warranty_years": 2},
    },
    {
        "name": "Lumi Climate Smart Thermostat",
        "brand": "Lumi",
        "category": "Home",
        "description": (
            "A learning smart thermostat that adjusts heating and cooling to your "
            "routine and helps lower energy bills. The crisp display and Wi-Fi app "
            "make scheduling effortless."
        ),
        "price": 149.0,
        "rating": 4.6,
        "review_count": 388,
        "stock": 75,
        "release_year": 2024,
        "features": ["smart-home", "wifi", "energy-saving"],
        "specs": {"color": "white", "weight_grams": 210, "warranty_years": 3},
    },
    {
        "name": "Vista Action Cam 4K",
        "brand": "Vista",
        "category": "Cameras",
        "description": (
            "A pocket-sized action camera that shoots stabilized 4K video and is "
            "waterproof without a case. Mount it on a helmet or bike and capture "
            "your adventures in sharp detail."
        ),
        "price": 299.0,
        "rating": 4.3,
        "review_count": 455,
        "stock": 33,
        "release_year": 2023,
        "features": ["camera", "4k", "waterproof", "wifi"],
        "specs": {"color": "black", "weight_grams": 128, "warranty_years": 1},
    },
]

for product_id, product in enumerate(catalog, start=1):
    r.json().set(f"product:{product_id}", Path.root_path(), product)
```



</details>

Use [FT.CREATE](https://redis.io/docs/latest/commands/ft.create) to define the index. Because the data is JSON, each field is identified by a [JSONPath](https://redis.io/docs/latest/develop/data-types/json/path) expression, and `AS` gives it a short alias to use in queries:

Foundational: Create an index over JSON documents with FT.CREATE, mapping JSONPaths to TEXT, TAG, and NUMERIC fields

**Difficulty:** Beginner

**Commands:** FT.CREATE

**Complexity:**
- FT.CREATE: O(K)

**Available in:** Redis CLI, Python

##### Redis CLI

```
> FT.CREATE idx:catalog ON JSON PREFIX 1 product: SCHEMA $.name AS name TEXT $.brand AS brand TAG SORTABLE $.category AS category TAG $.description AS description TEXT $.price AS price NUMERIC SORTABLE $.rating AS rating NUMERIC SORTABLE $.review_count AS review_count NUMERIC $.stock AS stock NUMERIC $.release_year AS release_year NUMERIC SORTABLE $.features[*] AS features TAG
```

##### Python

```python
schema = (
    TextField("$.name", as_name="name"),
    TagField("$.brand", as_name="brand", sortable=True),
    TagField("$.category", as_name="category"),
    TextField("$.description", as_name="description"),
    NumericField("$.price", as_name="price", sortable=True),
    NumericField("$.rating", as_name="rating", sortable=True),
    NumericField("$.review_count", as_name="review_count"),
    NumericField("$.stock", as_name="stock"),
    NumericField("$.release_year", as_name="release_year", sortable=True),
    TagField("$.features[*]", as_name="features"),
)
index = r.ft("idx:catalog")
index.create_index(
    schema,
    definition=IndexDefinition(prefix=["product:"], index_type=IndexType.JSON),
)
```



A few things to notice:

- **`PREFIX 1 product:`** means "index every key that starts with `product:`". The `1` is the number of prefixes that follow.
- **`AS name`, `AS price`, ...** define the alias you use in queries (`@name`, `@price`). Without an alias, you would have to write the full JSONPath in every query.
- **`SORTABLE`** on a field lets you sort results by it efficiently. Add it to fields you expect to sort by, such as `price` and `rating`.
- **`$.features[*]`** ends in `[*]`, which matters for arrays. More on that next.

You only create an index once. If you make a mistake, remove it with [FT.DROPINDEX](https://redis.io/docs/latest/commands/ft.dropindex) (this deletes the index, not your documents) and create it again.

## Indexing arrays: the `[*]` you should not forget

The `features` field is a JSON array like `["wireless", "bluetooth", "waterproof"]`. To index each element as its own tag, the JSONPath ends in `[*]`:

```
$.features[*] AS features TAG
```

This is the single most common point of confusion when indexing JSON, so it is worth understanding:

- **With `$.features[*]`**, Redis indexes `wireless`, `bluetooth`, and `waterproof` as three separate tags. A query for `@features:{waterproof}` matches the document.
- **With `$.features`** (no `[*]`) on a JSON array, the behavior is not what you want for filtering element-by-element.

> [!NOTE]
> This behavior differs between hashes and JSON, which trips up many newcomers. In a **hash**, a `TAG` field splits on commas by default, so `"wireless,bluetooth"` becomes two tags automatically. In **JSON**, there is no automatic splitting: index array elements with `[*]`, or if you store a comma-separated string, add `SEPARATOR ","` to the field definition. For the full explanation, see [Index JSON arrays as TAG](https://redis.io/docs/latest/develop/ai/search-and-query/indexing#index-json-arrays-as-tag).

## Check the index

After creating the index, you can confirm it picked up your documents. [FT.INFO](https://redis.io/docs/latest/commands/ft.info) reports details about an index, including how many documents it contains:

Foundational: Inspect an index with FT.INFO to confirm it exists and see how many documents it contains

**Difficulty:** Beginner

**Commands:** FT.INFO

**Complexity:**
- FT.INFO: O(1)

**Available in:** Redis CLI, Python

##### Redis CLI

```
> FT.INFO idx:catalog
```

##### Python

```python
info = r.ft("idx:catalog").info()
print("Documents indexed:", info["num_docs"])  # >>> Documents indexed: 12
```



Look for `num_docs` in the output; it should be `12`, one for each product you loaded.

> [!NOTE] Try it in Redis Insight
> In the [Redis Insight Search workspace](https://redis.io/docs/latest/develop/tools/insight/search-workspace), your new `idx:catalog` index appears in the list of indexes. Selecting it shows the schema you just defined &mdash; the fields, their types, and their aliases &mdash; without having to read the raw `FT.INFO` output.

## Next steps

Your data is indexed. Continue to [searching and filtering](https://redis.io/docs/latest/develop/get-started/search-tutorial/search) to start asking questions of it.

