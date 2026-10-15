# Install redis-cli

```json metadata
{
  "schema_version": 2,
  "title": "Install redis-cli",
  "description": "How to install just the Redis CLI (redis-cli) without installing all of Redis",
  "categories": ["docs","operate","stack","oss"],
  "tableOfContents": {"sections":[{"children":[{"id":"install-a-specific-version","title":"Install a specific version"},{"id":"choose-the-installation-directory","title":"Choose the installation directory"}],"id":"install-redis-cli","title":"Install redis-cli"},{"id":"connect-to-redis","title":"Connect to Redis"},{"id":"next-steps","title":"Next steps"}]}

,
  "codeExamples": []
}
```


If you only need the [Redis CLI](https://redis.io/docs/latest/develop/tools/cli) (`redis-cli`) to connect to a remote Redis server, you can install it on its own, without installing the full Redis Open Source distribution or building it from source.

The installer downloads a single, statically linked `redis-cli` binary, so it works even on minimal images (such as Amazon Linux, openSUSE, or distroless). It requires only `curl` or `wget`.

> [!NOTE]
> This installation method is supported on **Linux** and **macOS** only, on `x86_64`/`amd64` and `arm64`/`aarch64` processors. It does not run on native Windows. You have two options:
>
> 1. You can run it under the [Windows Subsystem for Linux (WSL)](https://learn.microsoft.com/windows/wsl/).
> 1. You can use it with Docker; see [Run Redis Open Source on Docker](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack/docker) for more information.

## Install redis-cli

Run the following command:


curl -fsSL https://packages.redis.io/redis-cli/install.sh | sh


The script detects your operating system and architecture, downloads the matching `redis-cli` binary, verifies its SHA-256 checksum, and installs it to `/usr/local/bin` (using `sudo` if required). If `/usr/local/bin` is not writable, it installs to `~/.local/bin` instead.

> [!NOTE]
> As with any `curl ... | sh` command, review the [install script](https://packages.redis.io/redis-cli/install.sh) before running it if you want to see exactly what it does.

### Install a specific version

By default, the script installs the latest stable release. To install a particular version, set the `REDIS_CLI_VERSION` environment variable:


curl -fsSL https://packages.redis.io/redis-cli/install.sh | REDIS_CLI_VERSION=8.8.0 sh


### Choose the installation directory

To install `redis-cli` to a location of your choice, set the `REDIS_CLI_INSTALL_DIR` environment variable:


curl -fsSL https://packages.redis.io/redis-cli/install.sh | REDIS_CLI_INSTALL_DIR="$HOME/bin" sh


If the installation directory is not on your `PATH`, the script prints a note reminding you to add it.

## Connect to Redis

Once `redis-cli` is installed, you can use it to connect to any Redis instance. For example, to connect to a server running on `localhost` on the default port:


redis-cli


To connect to a remote server, specify the host and port:


redis-cli -h <host> -p <port>


Test the connection with the `ping` command:


127.0.0.1:6379> PING
PONG


## Next steps

- Try the [Redis CLI tutorial](https://redis.io/docs/latest/develop/tools/cli).
- If you need a full Redis installation, see the other [installation guides](https://redis.io/docs/latest/operate/oss_and_stack/install/install-stack).

