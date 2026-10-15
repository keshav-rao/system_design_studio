# Install Redis on Linux

```json metadata
{
  "schema_version": 2,
  "title": "Install Redis on Linux",
  "description": "How to install Redis on Linux",
  "categories": ["docs","operate","stack","oss"],
  "tableOfContents": {"sections":[{"id":"install-on-ubuntudebian","title":"Install on Ubuntu/Debian"},{"id":"install-on-red-hatrocky","title":"Install on Red Hat/Rocky"},{"id":"install-on-ubuntu-using-snap","title":"Install on Ubuntu using Snap"},{"id":"starting-and-stopping-redis-in-the-background","title":"Starting and stopping Redis in the background"},{"id":"connect-to-redis","title":"Connect to Redis"},{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": []
}
```


Most major Linux distributions provide packages for Redis.

## Install on Ubuntu/Debian

Add the repository to the APT index, update it, and install Redis:


sudo apt-get install lsb-release curl gpg
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
sudo chmod 644 /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update
sudo apt-get install redis


Redis will start automatically, and it should restart at boot time. If Redis doesn't start across reboots, you may need to manually enable it:


sudo systemctl enable redis-server
sudo systemctl start redis-server


## Install on Red Hat/Rocky


sudo yum install redis
sudo systemctl enable redis
sudo systemctl start redis


Redis will restart at boot time.

## Install on Ubuntu using Snap

To install via Snap, run:


sudo apt update
sudo apt install redis-tools # for redis-cli
sudo snap install redis


Redis will start automatically, but it won't restart at boot time. To do this, run:


sudo snap set redis service.start=true


You can use these additional snap-related commands to start, stop, restart, and check the status of Redis:

* `sudo snap start redis`
* `sudo snap stop redis`
* `sudo snap restart redis`
* `sudo snap services redis`

If your Linux distribution does not currently have Snap installed, you can install it using the instructions described  [here](https://snapcraft.io/docs/installing-snapd). Then, consult the [Snapcraft store](https://snapcraft.io/redis) for instructions on installing Redis using Snap for your distribution.

## Starting and stopping Redis in the background

You can start the Redis server as a background process using the `systemctl` command. This only applies to Ubuntu/Debian when installed using `apt`, and Red Hat/Rocky when installed using `yum`.


sudo systemctl start <redis-service-name> # redis or redis-server depending on platform


To stop the server, use:


sudo systemctl stop <redis-service-name> # redis or redis-server depending on platform


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
  

