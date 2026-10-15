# Install Redis Open Source on Linux

```json metadata
{
  "schema_version": 2,
  "title": "Install Redis Open Source on Linux",
  "description": "How to install Redis Open Source using APT",
  "categories": ["docs","operate","stack","oss"],
  "tableOfContents": {"sections":[{"id":"install-redis-open-source-on-ubuntu-or-debian-linux-using-apt","title":"Install Redis Open Source on Ubuntu or Debian Linux using APT"}]}

,
  "codeExamples": []
}
```


## Install Redis Open Source on Ubuntu or Debian Linux using APT

> [!NOTE]
> If you only need the Redis CLI (`redis-cli`) and not the full Redis Open Source distribution, see [Install redis-cli](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/install-redis-cli).

Add the repository to the APT index, update it, and install Redis Open Source:


sudo apt-get install lsb-release curl gpg
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg
sudo chmod 644 /usr/share/keyrings/redis-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] https://packages.redis.io/deb $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/redis.list
sudo apt-get update
sudo apt-get install redis


The most recent version of Redis Open Source will be installed, along with the redis-tools package (redis-cli, etc.).
If you need to install an earlier version, run the following command to list the available versions:


apt policy redis

redis:
  Installed: (none)
  Candidate: 6:8.6.1-1rl1~noble1
  Version table:
     6:8.6.1-1rl1~noble1 500
        500 https://packages.redis.io/deb noble/main amd64 Packages
        500 https://packages.redis.io/deb noble/main all Packages
     6:8.6.0-1rl1~noble1 500
        500 https://packages.redis.io/deb noble/main amd64 Packages
        500 https://packages.redis.io/deb noble/main all Packages
     ...
     6:8.0.0-1rl1~noble1 500
        500 https://packages.redis.io/deb noble/main amd64 Packages
        500 https://packages.redis.io/deb noble/main all Packages
     6:7.4.8-1rl1~noble1 500
        500 https://packages.redis.io/deb noble/main amd64 Packages
        500 https://packages.redis.io/deb noble/main all Packages


For example, to install Redis Open Source v7.4.8 on Ubuntu LTS 24.04 (Noble Numbat), run the following command:


sudo apt-get install \
redis=6:7.4.8-1rl1~noble1 \
redis-server=6:7.4.8-1rl1~noble1 \
redis-sentinel=6:7.4.8-1rl1~noble1 \
redis-tools=6:7.4.8-1rl1~noble1


Alternatively, you can also set up a preferences file to pin a particular release:


Package: redis redis-server redis-sentinel redis-tools
Pin: version 6:7.4.*
Pin-Priority: 1001


See [this document](https://manpages.debian.org/buster/apt/apt_preferences.5.en.html#How_APT_Interprets_Priorities) for more information on `Pin-Priority`.

With the example preferences file give above, `6:7.4.8-1rl1~noble1` is the latest version that matches the pinned version and it will be installed when you run this command:


sudo apt-get install redis-server redis-sentinel redis-tools


Redis should start automatically after the initial installation and also at boot time.
Should that not be the case on your system, run the following commands:


sudo systemctl enable redis-server
sudo systemctl start redis-server


