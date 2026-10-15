# hiredis guide (C)

```json metadata
{
  "schema_version": 2,
  "title": "hiredis guide (C)",
  "description": "Connect your C application to a Redis database.",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"id":"build-and-install","title":"Build and install"},{"id":"connect-and-test","title":"Connect and test"},{"id":"more-information","title":"More information"}]}

,
  "codeExamples": []
}
```


[`hiredis`](https://github.com/redis/hiredis) is the
[C language](https://en.wikipedia.org/wiki/C_(programming_language))
client for Redis.
The sections below explain how to install `hiredis` and connect your application
to a Redis database.

`hiredis` requires a running Redis or [Redis Stack](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack) server. See [Getting started](https://redis.io/docs/latest/operate/oss_and_stack/install) for Redis installation instructions.

## Build and install

Clone or download the `hiredis` source from the [Github repository](https://github.com/redis/hiredis).
Then, in a terminal, go into the `hiredis` folder and run the `make` command to build
the dynamically-loaded library for `hiredis` (this has the name `libhiredis.dylib` on
MacOS and `libhiredis.so` on Linux). You can copy this library to your
project folder or run `sudo make install` to install it to `/usr/local/lib`.

## Connect and test

The code in the example below connects to the server, stores and retrieves
a string key using [`SET`](https://redis.io/docs/latest/commands/set) and
[`GET`](https://redis.io/docs/latest/commands/get), and then finally closes the
connection. An explanation of the code follows the example.

Foundational: Connect to a Redis server, set and retrieve string values using SET and GET, then close the connection

```c
// The following comment is required to make the example interactive.
//%cflags:-lhiredis
#include <stdio.h>
#include <stdlib.h>

#include <hiredis/hiredis.h>


int main() {
    // The `redisContext` type represents the connection
    // to the Redis server. Here, we connect to the
    // default host and port.
    redisContext *c = redisConnect("127.0.0.1", 6379);

    // Check if the context is null or if a specific
    // error occurred.
    if (c == NULL || c->err) {
        if (c != NULL) {
            printf("Error: %s\n", c->errstr);
            // handle error
        } else {
            printf("Can't allocate redis context\n");
        }

        exit(1);
    }

    // Set a string key.
    redisReply *reply = redisCommand(c, "SET foo bar");
    printf("Reply: %s\n", reply->str);
    freeReplyObject(reply);

    // Get the key we have just stored.
    reply = redisCommand(c, "GET foo");
    printf("Reply: %s\n", reply->str);
    freeReplyObject(reply);

    // Close the connection.
    redisFree(c);
}
```



For a real project, you would build your code with a makefile, but for
this simple test, you can just place it in a file called `main.c` and
build it with the following command. (If you didn't install `hiredis`
using `make install`, then you should also use the `-I` option to
specify the folder that contains the `hiredis` headers.)

```bash
cc main.c -L/usr/local/lib -lhiredis
```

The default executable filename is `a.out`. If you run this file from
the terminal, you should see the following output:

```
% ./a.out                             
Reply: OK
Reply: bar
```

The code first uses `redisConnect()` to open the connection for
all subsequent commands to use. See
[Connect](https://redis.io/docs/latest/develop/clients/hiredis/connect) for
more information about connecting to Redis.

The `redisCommand()` function
issues commands to the server, each of which returns a
`redisReply` pointer. Here, the reply is a string, which you can
access using the `str` field of the reply. The `redisCommand()`
call allocates memory for the reply, so you should free this
with `freeReplyObject()` when you have finished using it.
See [Issue commands](https://redis.io/docs/latest/develop/clients/hiredis/issue-commands)
and [Handle replies](https://redis.io/docs/latest/develop/clients/hiredis/handle-replies)
for more information.

Finally, you should close the connection to Redis with a
call to `redisFree()`. This is not strictly necessary
for this short test program, but real-world code will typically
open and use many connections. You must free them after using them
to prevent errors.

## More information

The [`hiredis`](https://github.com/redis/hiredis) Github repository contains
examples and details that may be useful if you are using `hiredis` to
implement a higher-level client for another programming language. There are
also examples showing how to use `hiredis` adapter headers to integrate with
various event handling frameworks.

See the other pages in this section for more information and examples.

