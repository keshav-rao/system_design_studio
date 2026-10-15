# Offline installation

```json metadata
{
  "schema_version": 2,
  "title": "Offline installation",
  "description": "If you install Redis Software on a machine with no internet connection, you need to perform two tasks manually.",
  "categories": ["docs","operate","rs"],
  "tableOfContents": {"sections":[{"id":"install-required-dependency-packages","title":"Install required dependency packages"},{"id":"set-up-ntp-time-synchronization","title":"Set up NTP time synchronization"}]}

,
  "codeExamples": []
}
```

By default, the installation process requires an internet connection to
enable installing dependency packages and for [synchronizing the
operating system clock](https://redis.io/docs/latest/operate/rs/clusters/configure/sync-clocks) against an NTP server.

If you install Redis Software on a machine without an
internet connection, you need to perform two tasks manually.

## Install required dependency packages

When you install Redis Software on a machine that is not connected to the internet, the installation process fails and displays an error message informing you it failed to automatically install dependencies. Review the installation steps in the console to see which missing dependencies the process attempted to install. Install all these dependency packages and then run the installation again.

## Set up NTP time synchronization

At the end of the installation, the process asks if you want to set up NTP time synchronization. If you choose `Yes` while you are not connected to the internet, the action fails and displays the appropriate error message, but the installation completes successfully. Despite the successful completion of the installation, you still have to configure all nodes for [NTP time synchronization](https://redis.io/docs/latest/operate/rs/clusters/configure/sync-clocks).

