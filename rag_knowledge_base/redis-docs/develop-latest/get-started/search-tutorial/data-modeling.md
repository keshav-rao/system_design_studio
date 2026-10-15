# Data modeling for search

```json metadata
{
  "schema_version": 2,
  "title": "Data modeling for search",
  "description": "Learn how to store records in Redis so they can be searched, and when to choose hashes versus JSON documents.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"a-record-as-a-hash","title":"A record as a hash"},{"id":"a-record-as-a-json-document","title":"A record as a JSON document"},{"id":"which-should-you-use","title":"Which should you use?"},{"id":"load-the-dataset","title":"Load the dataset"},{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": [{"codetabsId":"search_tutorial-stephash_example","commands":[{"acl_categories":["@write","@hash","@fast"],"complexity":"O(1)","name":"HSET"}],"description":"Foundational: Store a record as a hash with HSET when your data is a flat set of fields","difficulty":"beginner","id":"hash_example","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_search_tutorial-stephash_example"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_search_tutorial-stephash_example"}]},{"codetabsId":"search_tutorial-stepjson_example","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"}],"description":"Foundational: Store a record as a JSON document with JSON.SET when your data has nested objects or arrays","difficulty":"beginner","id":"json_example","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_search_tutorial-stepjson_example"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_search_tutorial-stepjson_example"}]},{"codetabsId":"search_tutorial-stepload_data","commands":[{"acl_categories":["@write","@json"],"complexity":"O(M+N)","name":"JSON.SET"}],"description":"Foundational: Load the tutorial dataset as JSON documents under a shared key prefix using JSON.SET","difficulty":"beginner","id":"load_data","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_search_tutorial-stepload_data"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_search_tutorial-stepload_data"}]},{"codetabsId":"search_tutorial-stepget_one","commands":[{"acl_categories":["@read","@json"],"complexity":"O(N)","name":"JSON.GET"}],"description":"Foundational: Read one JSON document back by its key with JSON.GET","difficulty":"beginner","id":"get_one","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_search_tutorial-stepget_one"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_search_tutorial-stepget_one"}]}]
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


This is step 1 of the [Redis Search tutorial](https://redis.io/docs/latest/develop/get-started/search-tutorial).

Before you can search anything, you need to decide how to store it. Redis gives you two natural ways to represent a structured record like a product: as a **hash** or as a **JSON document**. Both can be indexed and searched. This page explains the difference, helps you choose, and then loads the tutorial dataset.

## A record as a hash

A [hash](https://redis.io/docs/latest/develop/data-types/hashes) stores a flat set of field-value pairs under a single key. It is the simplest way to represent a record and maps neatly onto a row of fields:

Foundational: Store a record as a hash with HSET when your data is a flat set of fields

**Difficulty:** Beginner

**Commands:** HSET

**Complexity:**
- HSET: O(1)

**Available in:** Redis CLI, Python

##### Redis CLI

```
> HSET hproduct:1 name "Aurora AcousticPro Headphones" brand "Aurora" category "Audio" price 199.99 rating 4.6
(integer) 5
```

##### Python

```python
r.hset(
    "product:1",
    mapping={
        "name": "Aurora AcousticPro Headphones",
        "brand": "Aurora",
        "category": "Audio",
        "price": 199.99,
        "rating": 4.6,
    },
)
# >>> 5
```



Hashes are compact and fast, but they are **flat**: every value is a string or number. There is no natural place to put a nested object (like a `specs` sub-record) or a list of values (like multiple `features`) without flattening or encoding it yourself.

## A record as a JSON document

The [JSON](https://redis.io/docs/latest/develop/data-types/json) data type stores a full JSON document under a key. It can represent nested objects and arrays directly, which matches how application data usually looks:

Foundational: Store a record as a JSON document with JSON.SET when your data has nested objects or arrays

**Difficulty:** Beginner

**Commands:** JSON.SET

**Complexity:**
- JSON.SET: O(M+N)

**Available in:** Redis CLI, Python

##### Redis CLI

```
> JSON.SET product:1 $ '{"name":"Aurora AcousticPro Headphones","brand":"Aurora","category":"Audio","price":199.99,"rating":4.6,"features":["wireless","noise-cancelling","bluetooth"],"specs":{"color":"midnight black","weight_grams":268}}'
```

##### Python

```python
r.json().set(
    "product:1",
    Path.root_path(),
    {
        "name": "Aurora AcousticPro Headphones",
        "brand": "Aurora",
        "category": "Audio",
        "price": 199.99,
        "rating": 4.6,
        "features": ["wireless", "noise-cancelling", "bluetooth"],
        "specs": {"color": "midnight black", "weight_grams": 268},
    },
)
# >>> True
```



Notice that `features` is a real array and `specs` is a real nested object. You did not have to flatten them.

## Which should you use?

Both hashes and JSON documents can be indexed and searched by Redis Search, so you can search either one. Use this as a guide:

| Choose **hashes** when... | Choose **JSON** when... |
| --- | --- |
| Your records are flat (no nesting). | Your records have nested objects or arrays. |
| You want the smallest possible memory footprint. | You want your stored shape to match your application objects. |
| You frequently update individual fields. | You want to read, update, or index nested paths directly. |

For this tutorial, the catalog records have arrays (`features`) and a nested object (`specs`), so **we will use JSON documents** for the rest of the tutorial. If you are coming from a background where every record is a flat row, JSON is also a gentle way to keep your existing object shapes.

> [!NOTE]
> This is a modeling choice, not a limitation. The indexing and query commands you will learn (`FT.CREATE`, `FT.SEARCH`, `FT.AGGREGATE`) work with both hashes and JSON. The main practical difference shows up when indexing arrays, which you will see on the [next page](https://redis.io/docs/latest/develop/get-started/search-tutorial/indexing).

## Load the dataset

Now load the full catalog of 12 products. Each product is stored as a JSON document under a key with the prefix `product:`. The key prefix matters: in the next step you will tell Redis to index every key that starts with `product:`.

Foundational: Load the tutorial dataset as JSON documents under a shared key prefix using JSON.SET

**Difficulty:** Beginner

**Commands:** JSON.SET

**Complexity:**
- JSON.SET: O(M+N)

**Available in:** Redis CLI, Python

##### Redis CLI

```
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



You can read any single document back by its key with [JSON.GET](https://redis.io/docs/latest/commands/json.get):

Foundational: Read one JSON document back by its key with JSON.GET

**Difficulty:** Beginner

**Commands:** JSON.GET

**Complexity:**
- JSON.GET: O(N)

**Available in:** Redis CLI, Python

##### Redis CLI

```
> JSON.GET product:1 $.name
"[\"Aurora AcousticPro Headphones\"]"
```

##### Python

```python
res = r.json().get("product:1", "$.name")
print(res)  # >>> ['Aurora AcousticPro Headphones']
```



At this point the data is in Redis, but you can only fetch it one key at a time. To *search* across all products, you need an index.

## Next steps

Continue to [creating an index](https://redis.io/docs/latest/develop/get-started/search-tutorial/indexing) to make this data searchable.

