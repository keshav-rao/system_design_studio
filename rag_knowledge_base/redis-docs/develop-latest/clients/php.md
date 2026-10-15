# Predis guide (PHP)

```json metadata
{
  "schema_version": 2,
  "title": "Predis guide (PHP)",
  "description": "Connect your PHP application to a Redis database",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"install","title":"Install"},{"id":"connect-and-test","title":"Connect and test"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": [{"codetabsId":"landing-stepconnect","description":"Foundational: Connect to a Redis server and establish a client connection","difficulty":"beginner","id":"connect","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_landing-stepconnect"}]},{"codetabsId":"landing-stepset_get_string","description":"Foundational: Set and retrieve string values using SET and GET commands","difficulty":"beginner","id":"set_get_string","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_landing-stepset_get_string"}]},{"codetabsId":"landing-stepset_get_hash","description":"Foundational: Store and retrieve hash data structures using HSET and HGETALL","difficulty":"beginner","id":"set_get_hash","languages":[{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_landing-stepset_get_hash"}]}]
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


[`Predis`](https://github.com/predis/predis) is the recommended [PHP](https://php.net/)
client for Redis. 
The sections below explain how to install `Predis` and connect your application to a Redis database.

> [!NOTE]
> Although we provide basic documentation for `Predis`, it is a third-party
> client library and is not developed or supported directly by Redis.

`Predis` requires a running Redis server. See [here](https://redis.io/docs/latest/operate/oss_and_stack/install) for Redis Open Source installation instructions.

## Install

Use [Composer](https://getcomposer.org/) to install the `Predis` library
with the following command line:

```bash
composer require predis/predis
```

## Connect and test

Connect to a locally-running server on the standard port (6379)
with the following code:

Foundational: Connect to a Redis server and establish a client connection

**Difficulty:** Beginner

**Available in:** PHP

##### PHP

```php
<?php

require 'vendor/autoload.php';

use Predis\Client as PredisClient;

$r = new PredisClient([
                'scheme'   => 'tcp',
                'host'     => '127.0.0.1',
                'port'     => 6379,
                'password' => '',
                'database' => 0,
            ]);
```



Store and retrieve a simple string to test the connection:

Foundational: Set and retrieve string values using SET and GET commands

**Difficulty:** Beginner

**Available in:** PHP

##### PHP

```php
echo $r->set('foo', 'bar'), PHP_EOL;
// >>> OK

echo $r->get('foo'), PHP_EOL;
// >>> bar
```



Store and retrieve a [hash](https://redis.io/docs/latest/develop/data-types/hashes)
object:

Foundational: Store and retrieve hash data structures using HSET and HGETALL

**Difficulty:** Beginner

**Available in:** PHP

##### PHP

```php
$r->hset('user-session:123', 'name', 'John');
$r->hset('user-session:123', 'surname', 'Smith');
$r->hset('user-session:123', 'company', 'Redis');
$r->hset('user-session:123', 'age', 29);

echo var_export($r->hgetall('user-session:123')), PHP_EOL;
/* >>>
array (
  'name' => 'John',
  'surname' => 'Smith',
  'company' => 'Redis',
  'age' => '29',
)
*/
```



## More information

The [Predis wiki on Github](https://github.com/predis/predis/wiki) has
information about the different connection options you can use.

See also the pages in this section for more information and examples:

