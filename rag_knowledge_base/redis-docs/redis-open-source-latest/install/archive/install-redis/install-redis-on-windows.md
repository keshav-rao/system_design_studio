# Install Redis on Windows

```json metadata
{
  "schema_version": 2,
  "title": "Install Redis on Windows",
  "description": "Use Redis on Windows through Memurai, official Redis partner for Windows compatibility",
  "categories": ["docs","operate","stack","oss"],
  "tableOfContents": {"sections":[{"id":"run-redis-on-windows-using-memurai","title":"Run Redis on Windows using Memurai"},{"children":[{"id":"install-or-enable-wsl2","title":"Install or enable WSL2"},{"id":"install-redis","title":"Install Redis"},{"id":"connect-to-redis","title":"Connect to Redis"}],"id":"run-redis-on-windows-using-wsl-windows-subsystem-for-linux","title":"Run Redis on Windows using WSL (Windows Subsystem for Linux)"},{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": []
}
```


## Run Redis on Windows using Memurai

Redis is now natively supported on Windows through [Memurai](https://www.memurai.com/), the official Redis partner for Windows compatibility.

## Run Redis on Windows using WSL (Windows Subsystem for Linux)

To install Redis on Windows using WSL, you'll first need to enable [WSL2](https://docs.microsoft.com/en-us/windows/wsl/install) (Windows Subsystem for Linux). WSL2 lets you run Linux binaries natively on Windows. For this method to work, you'll need to be running Windows 10 version 2004 and higher or Windows 11.

### Install or enable WSL2

Microsoft provides [detailed instructions for installing WSL](https://docs.microsoft.com/en-us/windows/wsl/install). Follow these instructions, and take note of the default Linux distribution it installs. This guide assumes Ubuntu.

### Install Redis

Once you're running Ubuntu on Windows, you can follow the steps detailed at [Install on Ubuntu/Debian](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-linux#install-on-ubuntu-debian) to install recent stable versions of Redis from the official `packages.redis.io` APT repository.
Add the repository to the <code>apt</code> index, update it, and then install:


curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list

sudo apt-get update
sudo apt-get install redis


Lastly, start the Redis server like so:


redis-server --daemonize yes


### Connect to Redis

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

