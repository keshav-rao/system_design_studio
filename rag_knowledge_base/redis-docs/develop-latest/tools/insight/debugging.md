# Redis Insight debugging information

```json metadata
{
  "schema_version": 2,
  "title": "Redis Insight debugging information",
  "description": "Redis Insight debugging information",
  "categories": ["docs","develop","stack","oss","rs","rc","oss","kubernetes","clients"],
  "tableOfContents": {"sections":[{"children":[{"id":"1-launch-redis-insight-in-debug-mode","title":"1. Launch Redis Insight in debug mode"},{"id":"2-investigate-logs","title":"2. Investigate logs"}],"id":"connection-issues","title":"Connection issues"},{"children":[{"id":"to-debug-issues-other-than-connectivity","title":"To debug issues other than connectivity"},{"id":"get-detailed-redis-insight-logs","title":"Get detailed Redis Insight logs"},{"id":"to-log-everything","title":"To log everything"}],"id":"other-issues","title":"Other issues"}]}

,
  "codeExamples": []
}
```


If you are experiencing errors or other issues when using Redis Insight, follow the steps below to learn more about the errors and to identify root cause.

## Connection issues

If you experience connection issues, try these steps.

### 1. Launch Redis Insight in debug mode

Run the following command to launch Redis Insight in debug mode to investigate connection issues:

* **Windows**:

    `cmd /C "set DEBUG=ioredis* && ".\Redis Insight.exe""`

* **macOS** (from the Applications folder):

    `DEBUG=ioredis* open "Redis Insight.app"`

* **Linux**:

    `DEBUG=ioredis* "redis insight"`

### 2. Investigate logs

You can review the Redis Insight log files (files with a `.log` extension) to get detailed information about system issues.
These are the locations on supported platforms:

- **Docker**: In the `/data/logs` directory *inside the container*.
- **macOS**: In the `/Users/<your-username>/.redis-insight` directory.
- **Windows**: In the `C:\Users\<your-username>\.redis-insight` directory.
- **Linux**: In the `/home/<your-username>/.redis-insight` directory.

## Other issues
### To debug issues other than connectivity

* **Windows**:

    `cmd /C "set DEBUG=* && ".\Redis Insight.exe""`

* **macOS** (from the Applications folder):

    `DEBUG=* open "Redis Insight.app"`

* **Linux**:

    `DEBUG=* "redis insight"`

### Get detailed Redis Insight logs

* **Windows**:

    `cmd /C "set STDOUT_LOGGER=true && set LOG_LEVEL=debug && set LOGGER_OMIT_DATA=false && ".\Redis Insight.exe""`

* **macOS** (from the Applications folder):

    `LOG_LEVEL=debug LOGGER_OMIT_DATA=false open "Redis Insight.app"`

* **Linux**:

    `LOG_LEVEL=debug LOGGER_OMIT_DATA=false "redis insight"`

    Note: if you use LOGGER_OMIT_DATA=false, logs may contain sensitive data.

### To log everything
* **Windows**:

    `cmd /C "set STDOUT_LOGGER=true && set LOG_LEVEL=debug && set LOGGER_OMIT_DATA=false && set DEBUG=* && ".\Redis Insight.exe""`

* **macOS** (from the Applications folder):

    `LOG_LEVEL=debug LOGGER_OMIT_DATA=false DEBUG=* open "Redis Insight.app"`

* **Linux**:

    `LOG_LEVEL=debug LOGGER_OMIT_DATA=false DEBUG=* "redis insight"`

    Note: if you use LOGGER_OMIT_DATA=false or DEBUG=*, logs may contain sensitive data.
