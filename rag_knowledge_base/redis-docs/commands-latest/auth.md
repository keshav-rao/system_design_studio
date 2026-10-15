# AUTH

```json metadata
{
  "schema_version": 2,
  "title": "AUTH",
  "description": "Authenticates the connection.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "arguments": [{"display_text":"username","name":"username","optional":true,"since":"6.0.0","type":"string"},{"display_text":"password","name":"password","type":"string"}],
  "syntax_fmt": "AUTH [username] password",
  "complexity": "O(N) where N is the number of passwords defined for the user",
  "group": "connection",
  "command_flags": ["noscript","loading","stale","fast","no_auth","allow_busy"],
  "acl_categories": ["@fast","@connection"],
  "since": "1.0.0",
  "arity": -2,
  "tableOfContents": {"sections":[{"id":"required-arguments","title":"Required arguments"},{"id":"optional-arguments","title":"Optional arguments"},{"children":[{"id":"security-notice","title":"Security notice"}],"id":"details","title":"Details"},{"id":"redis-software-and-redis-cloud-compatibility","title":"Redis Software and Redis Cloud compatibility"},{"id":"return-information","title":"Return information"}]}

,
  "codeExamples": [{"codetabsId":"cmds_cnxmgmt-stepauth1","description":"Foundational: Authenticate with a password using AUTH when the Redis server is protected by requirepass","difficulty":"beginner","id":"auth1","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_cnxmgmt-stepauth1"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_cnxmgmt-stepauth1"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_cnxmgmt-stepauth1"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_cnxmgmt-stepauth1"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_cnxmgmt-stepauth1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_cnxmgmt-stepauth1"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_cnxmgmt-stepauth1"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_cnxmgmt-stepauth1"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_cnxmgmt-stepauth1"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_cnxmgmt-stepauth1"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_cmds_cnxmgmt-stepauth1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_cnxmgmt-stepauth1"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_cnxmgmt-stepauth1"}]},{"codetabsId":"cmds_cnxmgmt-stepauth2","description":"ACL authentication: Authenticate with username and password using AUTH when Redis ACL system is enabled (Redis 6.0\u0026#43;)","difficulty":"intermediate","id":"auth2","languages":[{"id":"redis-cli","panelId":"panel_redis-cli_cmds_cnxmgmt-stepauth2"},{"clientId":"redis-py","clientName":"redis-py","id":"Python","langId":"python","panelId":"panel_Python_cmds_cnxmgmt-stepauth2"},{"id":"Node-js","panelId":"panel_Nodejs_cmds_cnxmgmt-stepauth2"},{"clientId":"ioredis","clientName":"ioredis","id":"ioredis","langId":"javascript","panelId":"panel_ioredis_cmds_cnxmgmt-stepauth2"},{"clientId":"jedis","clientName":"Jedis","id":"Java-Sync","langId":"java","panelId":"panel_Java-Sync_cmds_cnxmgmt-stepauth2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Async","langId":"java","panelId":"panel_Java-Async_cmds_cnxmgmt-stepauth2"},{"clientId":"lettuce","clientName":"Lettuce","id":"Java-Reactive","langId":"java","panelId":"panel_Java-Reactive_cmds_cnxmgmt-stepauth2"},{"clientId":"go-redis","clientName":"go-redis","id":"Go","langId":"go","panelId":"panel_Go_cmds_cnxmgmt-stepauth2"},{"id":"dotnet-Sync (SE-Redis)","panelId":"panel_Csharp-Sync (SERedis)_cmds_cnxmgmt-stepauth2"},{"clientId":"predis","clientName":"Predis","id":"PHP","langId":"php","panelId":"panel_PHP_cmds_cnxmgmt-stepauth2"},{"clientId":"redis-rb","clientName":"redis-rb","id":"Ruby","langId":"ruby","panelId":"panel_Ruby_cmds_cnxmgmt-stepauth2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Sync","langId":"rust","panelId":"panel_Rust-Sync_cmds_cnxmgmt-stepauth2"},{"clientId":"redis-rs","clientName":"redis-rs","id":"Rust-Async","langId":"rust","panelId":"panel_Rust-Async_cmds_cnxmgmt-stepauth2"}]}]
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

The AUTH command authenticates the current connection in two cases:

1. If the Redis server is password protected via the `requirepass` option.
2. A Redis 6.0 instance, or greater, is using the [Redis ACL system](https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl).

Redis versions prior of Redis 6 were only able to understand the one argument
version of the command:

Foundational: Authenticate with a password using AUTH when the Redis server is protected by requirepass

**Difficulty:** Beginner

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
AUTH "temp-pass"
```

##### C#

```csharp
        var res1 = db.Execute("AUTH", "temp_pass");
        Console.WriteLine(res1); // >>> OK

        var res2 = db.Execute("AUTH", "default", "temp_pass");
        Console.WriteLine(res2); // >>> OK
```

##### Go

```go
	authResult1, err := conn.Auth(ctx, "temp_pass").Result()

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(authResult1) // >>> OK

	authResult2, err := conn.AuthACL(ctx, "default", "temp_pass").Result()

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(authResult2) // >>> OK
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> authExample1 = asyncCommands.auth("temp_pass")
                    .thenCompose(res1 -> {
                        System.out.println(res1); // >>> OK
                        return asyncCommands.auth("default", "temp_pass");
                    }).thenAccept(res2 -> {
                        System.out.println(res2); // >>> OK
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> authExample1 = reactiveCommands.auth("temp_pass")
                    .doOnNext(res1 -> {
                        System.out.println(res1); // >>> OK
                    })
                    .then(reactiveCommands.auth("default", "temp_pass"))
                    .doOnNext(res2 -> {
                        System.out.println(res2); // >>> OK
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        // Note: you must use the `Jedis` class rather than `RedisClient`
        // to access the `auth` commands.
        String authResult1 = jedis.auth("default",  "temp_pass");
        System.out.println(authResult1); // >>> OK
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.auth({ password: 'temp_pass' });
console.log(res1); // OK

const res2 = await client.auth({ username: 'default', password: 'temp_pass' });
console.log(res2); // OK

```

##### JavaScript (Node.js)

```javascript
const res1 = await redis.auth('temp_pass');
console.log(res1); // >>> OK

const res2 = await redis.auth('default', 'temp_pass');
console.log(res2); // >>> OK
```

##### JavaScript (Node.js)

```javascript
const res1 = await client.auth({ password: 'temp_pass' });
console.log(res1); // OK

const res2 = await client.auth({ username: 'default', password: 'temp_pass' });
console.log(res2); // OK

```

##### JavaScript (Node.js)

```javascript
const res1 = await redis.auth('temp_pass');
console.log(res1); // >>> OK

const res2 = await redis.auth('default', 'temp_pass');
console.log(res2); // >>> OK
```

##### PHP

```php
        $res1 = $r->auth('temp_pass');
        echo $res1 . PHP_EOL; // >>> OK

        $res2 = $r->auth('default', 'temp_pass');
        echo $res2 . PHP_EOL; // >>> OK
```

##### Python

```python
res1 = r.auth(password="temp_pass")
print(res1) # >>> True

res2 = r.auth(password="temp_pass", username="default")
print(res2) # >>> True

```

##### Ruby

```ruby
res1 = r.auth('temp_pass')
puts res1 # >>> OK

res2 = r.auth('default', 'temp_pass')
puts res2 # >>> OK
```

##### Rust (Asynchronous)

```rust
        if let Ok(res1) = redis::cmd("AUTH").arg("temp_pass").query_async::<String>(&mut r).await {
            println!("{res1}"); // >>> OK
        }

        if let Ok(res2) = redis::cmd("AUTH").arg("default").arg("temp_pass").query_async::<String>(&mut r).await {
            println!("{res2}"); // >>> OK
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res1) = redis::cmd("AUTH").arg("temp_pass").query::<String>(&mut r) {
            println!("{res1}"); // >>> OK
        }

        if let Ok(res2) = redis::cmd("AUTH").arg("default").arg("temp_pass").query::<String>(&mut r) {
            println!("{res2}"); // >>> OK
        }
```



This form just authenticates against the password set with `requirepass`.
In this configuration Redis will deny any command executed by the just
connected clients, unless the connection gets authenticated via `AUTH`.

If the password provided via AUTH matches the password in the configuration file, the server replies with the `OK` status code and starts accepting commands.
Otherwise, an error is returned and the clients needs to try a new password.

When Redis ACLs are used, the command should be given in an extended way:

ACL authentication: Authenticate with username and password using AUTH when Redis ACL system is enabled (Redis 6.0+)

**Difficulty:** Intermediate

**Available in:** Redis CLI, C#, Go, Java (Asynchronous - Lettuce), Java (Reactive - Lettuce), Java (Synchronous - Jedis), JavaScript (Node.js), JavaScript (Node.js), PHP, Python, Ruby, Rust (Asynchronous), Rust (Synchronous)

##### Redis CLI

```
AUTH "test-user" "strong_password"
```

##### C#

```csharp
        var res3 = db.Execute("AUTH", "test-user", "strong_password");
        Console.WriteLine(res3); // >>> OK
```

##### Go

```go
	authResult3, err := conn.AuthACL(ctx, "test-user", "strong_password").Result()

	if err != nil {
		fmt.Println(err)
	}

	fmt.Println(authResult3) // >>> OK
```

##### Java (Asynchronous - Lettuce)

```java
            CompletableFuture<Void> authExample2 = asyncCommands.auth("test-user", "strong_password")
                    .thenAccept(res3 -> {
                        System.out.println(res3); // >>> OK
                    }).toCompletableFuture();
```

##### Java (Reactive - Lettuce)

```java
            Mono<Void> authExample2 = reactiveCommands.auth("test-user", "strong_password")
                    .doOnNext(res3 -> {
                        System.out.println(res3); // >>> OK
                    })
                    .then();
```

##### Java (Synchronous - Jedis)

```java
        // Note: you must use the `Jedis` class rather than `RedisClient`
        // to access the `auth` commands.
        String authResult2 = jedis.auth("test-user", "strong_password");
        System.out.println(authResult2); // >>> OK
```

##### JavaScript (Node.js)

```javascript
const res3 = await client.auth({ username: 'test-user', password: 'strong_password' });
console.log(res3); // OK

```

##### JavaScript (Node.js)

```javascript
const res3 = await redis.auth('test-user', 'strong_password');
console.log(res3); // >>> OK
```

##### JavaScript (Node.js)

```javascript
const res3 = await client.auth({ username: 'test-user', password: 'strong_password' });
console.log(res3); // OK

```

##### JavaScript (Node.js)

```javascript
const res3 = await redis.auth('test-user', 'strong_password');
console.log(res3); // >>> OK
```

##### PHP

```php
        $res3 = $r->auth('test-user', 'strong_password');
        echo $res3 . PHP_EOL; // >>> OK
```

##### Python

```python
res = r.auth(username="test-user", password="strong_password")
print(res) # >>> True

```

##### Ruby

```ruby
res3 = r.auth('test-user', 'strong_password')
puts res3 # >>> OK
```

##### Rust (Asynchronous)

```rust
        if let Ok(res3) = redis::cmd("AUTH").arg("test-user").arg("strong_password").query_async::<String>(&mut r).await {
            println!("{res3}"); // >>> OK
        }
```

##### Rust (Synchronous)

```rust
        if let Ok(res3) = redis::cmd("AUTH").arg("test-user").arg("strong_password").query::<String>(&mut r) {
            println!("{res3}"); // >>> OK
        }
```



In order to authenticate the current connection with one of the connections
defined in the ACL list (see [`ACL SETUSER`](https://redis.io/docs/latest/commands/acl-setuser)) and the official [ACL guide](https://redis.io/docs/latest/operate/oss_and_stack/management/security/acl) for more information.

When ACLs are used, the single argument form of the command, where only the password is specified, assumes that the implicit username is "default".

## Required arguments

<details open><summary><code>password</code></summary>

The password to authenticate with. With `requirepass`, this is the server password; with ACLs, it is the user's password.

</details>

## Optional arguments

<details open><summary><code>username</code></summary>

The ACL username to authenticate as. If omitted, the `default` user is used.

</details>

## Details

### Security notice

Because of the high performance nature of Redis, it is possible to try
a lot of passwords in parallel in very short time, so make sure to generate a
strong and very long password so that this attack is infeasible.
A good way to generate strong passwords is via the [`ACL GENPASS`](https://redis.io/docs/latest/commands/acl-genpass) command.

## Redis Software and Redis Cloud compatibility

| Redis<br />Software | Redis<br />Cloud | <span style="min-width: 9em; display: table-cell">Notes</span> |
|:----------------------|:-----------------|:------|
| <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> | <span title="Supported">&#x2705; Standard</span><br /><span title="Supported"><nobr>&#x2705; Active-Active</nobr></span> |  |

## Return information

**RESP2:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`, or an error if the password, or username/password pair, is invalid.

**RESP3:**

[Simple string reply](../../develop/reference/protocol-spec#simple-strings): `OK`, or an error if the password, or username/password pair, is invalid.



