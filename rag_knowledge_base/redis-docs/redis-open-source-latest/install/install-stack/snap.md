# Install Redis Open Source on Linux

```json metadata
{
  "schema_version": 2,
  "title": "Install Redis Open Source on Linux",
  "description": "How to install Redis Open Source using Snap",
  "categories": ["docs","operate","stack","oss"],
  "tableOfContents": {"sections":[{"id":"install-redis-open-source-on-ubuntu-linux-using-snap","title":"Install Redis Open Source on Ubuntu Linux using Snap"},{"id":"connect-to-redis","title":"Connect to Redis"}]}

,
  "codeExamples": []
}
```


## Install Redis Open Source on Ubuntu Linux using Snap

> [!NOTE]
> If you only need the Redis CLI (`redis-cli`) and not the full Redis Open Source distribution, see [Install redis-cli](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/install-redis-cli).

To install Redis via snap, run the following commands:


sudo apt update
sudo apt install redis-tools # this will install `redis-cli`
sudo snap install redis


Redis will start automatically after installation and also at boot time.

## Connect to Redis

Once Redis is running, you can test it by running `redis-cli`:


redis-cli


Test the connection with the `ping` command:


127.0.0.1:6379> PING
PONG


