# Install Redis on macOS

```json metadata
{
  "schema_version": 2,
  "title": "Install Redis on macOS",
  "description": "Use Homebrew to install and start Redis on macOS",
  "categories": ["docs","operate","stack","oss"],
  "tableOfContents": {"sections":[{"id":"prerequisites","title":"Prerequisites"},{"id":"installation","title":"Installation"},{"children":[{"id":"starting-and-stopping-redis-using-launchd","title":"Starting and stopping Redis using launchd"}],"id":"starting-and-stopping-redis-in-the-foreground","title":"Starting and stopping Redis in the foreground"},{"id":"connect-to-redis","title":"Connect to Redis"},{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": []
}
```


This guide shows you how to install Redis on macOS using Homebrew. Homebrew is the easiest way to install Redis on macOS. If you'd prefer to build Redis from the source files on macOS, see [Installing Redis from Source](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-from-source).

> [!NOTE]
> The Homebrew distribution of Redis Open Source is only supported on macOS.

## Prerequisites

First, make sure you have Homebrew installed. From the terminal, run:


brew --version


If this command fails, you'll need to [follow the Homebrew installation instructions](https://brew.sh/).

## Installation

From the terminal, run:


brew install redis


This will install Redis on your system.

## Starting and stopping Redis in the foreground

To test your Redis installation, you can run the `redis-server` executable from the command line:


redis-server


If successful, you'll see the startup logs for Redis, and Redis will be running in the foreground.

To stop Redis, enter `Ctrl-C`.

### Starting and stopping Redis using launchd

As an alternative to running Redis in the foreground, you can also use `launchd` to start the process in the background:


brew services start redis


This launches Redis and restarts it at login. You can check the status of a `launchd` managed Redis by running the following:


brew services info redis


If the service is running, you'll see output like the following:


redis (homebrew.mxcl.redis)
Running: ✔
Loaded: ✔
User: miranda
PID: 67975


To stop the service, run:


brew services stop redis


## Connect to Redis

Once Redis is running, you can test it by running `redis-cli`:


redis-cli


Test the connection with the `ping` command:


127.0.0.1:6379> ping
PONG


You can also test that your Redis server is running using
[Redis Insight](https://redis.io/docs/latest/develop/tools/insight).

## Next steps

Once you have a running Redis instance, you may want to:

* Try the [Redis CLI tutorial](https://redis.io/docs/latest/develop/tools/cli)
* Connect using one of the [Redis clients](https://redis.io/docs/latest/develop/clients)
* [Install Redis "properly"](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis#install-redis-properly)
  for production use.
  

