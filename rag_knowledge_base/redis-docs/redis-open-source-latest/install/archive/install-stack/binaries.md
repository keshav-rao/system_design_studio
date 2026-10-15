# Install Redis Stack from binaries

```json metadata
{
  "schema_version": 2,
  "title": "Install Redis Stack from binaries",
  "description": "How to install Redis Stack using tarballs",
  "categories": ["docs","operate","stack","oss"],
  "tableOfContents": {"sections":[{"children":[{"id":"add-the-binaries-to-your-path","title":"Add the binaries to your PATH"}],"id":"start-redis-stack-server","title":"Start Redis Stack Server"}]}

,
  "codeExamples": []
}
```


## Start Redis Stack Server

Install the openssl libraries for your platform. For example, on a Debian or Ubuntu instance run:


sudo apt install libssl-dev


After untarring or unzipping your redis-stack-server download, you can start Redis Stack Server as follows:


/path/to/redis-stack-server/bin/redis-stack-server


### Add the binaries to your PATH

You can add the redis-stack-server binaries to your `$PATH` as follows:

Open the file `~/.bashrc` or `~/zshrc` (depending on your shell), and add the following lines.


export PATH=/path/to/redis-stack-server/bin:$PATH


If you have an existing Redis installation on your system, then you can choose override those override those PATH variables as before, or you can choose to only add redis-stack-server binary as follows:


export PATH=/path/to/redis-stack-server/bin/redis-stack-server:$PATH


If you're running redis-stack-server on a mac, please ensure you have openssl installed, via [homebrew](https://brew.sh/).

Now you can start Redis Stack Server as follows:


redis-stack-server


