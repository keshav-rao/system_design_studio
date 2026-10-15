# Install Redis Open Source on Linux

```json metadata
{
  "schema_version": 2,
  "title": "Install Redis Open Source on Linux",
  "description": "How to install Redis Open Source using RPM",
  "categories": ["docs","operate","stack","oss"],
  "tableOfContents": {"sections":[{"id":"install-redis-open-source-on-rocky-linux-8-and-9-or-almalinux-8-and-9-using-rpm","title":"Install Redis Open Source on Rocky Linux 8 and 9, or AlmaLinux 8 and 9 using RPM"}]}

,
  "codeExamples": []
}
```


## Install Redis Open Source on Rocky Linux 8 and 9, or AlmaLinux 8 and 9 using RPM

> [!NOTE]
> If you only need the Redis CLI (`redis-cli`) and not the full Redis Open Source distribution, see [Install redis-cli](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/install-redis-cli).

Follow these steps to install Redis Open Source.

1. Create the file `/etc/yum.repos.d/redis.repo` with the following contents.

    - For Rocky Linux 9 and AlmaLinux 9
    
    [Redis]
    name=Redis
    baseurl=http://packages.redis.io/rpm/rockylinux9
    enabled=1
    gpgcheck=1
    

    - For Rocky Linux 8 and AlmaLinux 8
    
    [Redis]
    name=Redis
    baseurl=http://packages.redis.io/rpm/rockylinux8
    enabled=1
    gpgcheck=1
    

2. Run the following commands:

    
    curl -fsSL https://packages.redis.io/gpg > /tmp/redis.key
    sudo rpm --import /tmp/redis.key
    sudo yum install redis
    

Redis will not start automatically, nor will it start at boot time. To do this, run the following commands.


sudo systemctl enable redis
sudo systemctl start redis


