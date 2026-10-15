# Install Redis from Source

```json metadata
{
  "schema_version": 2,
  "title": "Install Redis from Source",
  "description": "Compile and install Redis from source",
  "categories": ["docs","operate","stack","oss"],
  "tableOfContents": {"sections":[{"id":"downloading-the-source-files","title":"Downloading the source files"},{"children":[{"id":"starting-and-stopping-redis-in-the-foreground","title":"Starting and stopping Redis in the foreground"}],"id":"compiling-redis","title":"Compiling Redis"}]}

,
  "codeExamples": []
}
```


You can compile and install Redis from source on variety of platforms and operating systems including Linux and macOS. Redis has no dependencies other than a C  compiler and `libc`.

## Downloading the source files

The Redis source files are available from the [Download](https://redis.io/downloads) page. You can verify the integrity of these downloads by checking them against the digests in the [redis-hashes git repository](https://github.com/redis/redis-hashes).

To obtain the source files for the latest stable version of Redis from the Redis downloads site, run:


wget https://download.redis.io/redis-stable.tar.gz


## Compiling Redis

To compile Redis, first extract the tarball, change to the root directory, and then run `make`:


tar -xzvf redis-stable.tar.gz
cd redis-stable
make


To build with TLS support, you'll need to install OpenSSL development libraries (e.g., libssl-dev on Debian/Ubuntu) and then run:


make BUILD_TLS=yes


If the compile succeeds, you'll find several Redis binaries in the `src` directory, including:

* **redis-server**: the Redis Server itself
* **redis-cli** is the command line interface utility to talk with Redis.

To install these binaries in `/usr/local/bin`, run:


sudo make install


### Starting and stopping Redis in the foreground

Once installed, you can start Redis by running


redis-server


If successful, you'll see the startup logs for Redis, and Redis will be running in the foreground.

To stop Redis, enter `Ctrl-C`.

For a more complete installation, continue with [these instructions](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis#install-redis-properly).

