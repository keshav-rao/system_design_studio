# Redis for AI

```json metadata
{
  "schema_version": 2,
  "title": "Redis for AI",
  "description": "Build AI applications with Redis vector database and semantic caching",
  "categories": ["docs","integrate","oss","rs","rc"],
  "group": "library",
  "tableOfContents": {"sections":[{"id":"overview","title":"Overview"},{"id":"key-features","title":"Key Features"},{"children":[{"id":"redisvl-python","title":"RedisVL (Python)"},{"id":"langchain-integration","title":"LangChain Integration"},{"id":"client-libraries-with-vector-search","title":"Client Libraries with Vector Search"}],"id":"ai-libraries","title":"AI Libraries"},{"children":[{"id":"quick-start-guides","title":"Quick Start Guides"},{"id":"tutorials-and-examples","title":"Tutorials and Examples"},{"id":"video-tutorials","title":"Video Tutorials"}],"id":"getting-started","title":"Getting Started"},{"id":"use-cases","title":"Use Cases"},{"id":"additional-resources","title":"Additional Resources"}]}

,
  "codeExamples": []
}
```


Build powerful AI applications using Redis as your vector database with specialized libraries for Python, JavaScript, and Java.

## Overview

Redis provides comprehensive AI libraries and tools to help you build intelligent applications with vector search, retrieval-augmented generation (RAG), semantic caching, and more. Whether you're working with LangChain, LlamaIndex, or building custom AI solutions, Redis has the tools you need.

[Explore the complete Redis for AI documentation](https://redis.io/docs/latest/develop/ai)

## Key Features

- **Vector Search**: Store and query vector embeddings with HNSW and FLAT index types
- **Semantic Caching**: Cache LLM responses to reduce costs and improve performance
- **RAG Support**: Build retrieval-augmented generation applications with popular frameworks
- **Multi-language Support**: Libraries available for Python, JavaScript, and Java
- **Real-time Performance**: Sub-millisecond query latency for production AI applications

## AI Libraries

### RedisVL (Python)

The Redis Vector Library (RedisVL) is a Python client library for building AI applications with Redis.

- **Vector Search**: Create and query vector indexes with ease
- **Semantic Caching**: Built-in LLM cache for faster responses
- **RAG Utilities**: Tools for building retrieval-augmented generation apps
- **Framework Integration**: Works with LangChain, LlamaIndex, and more

[Learn more about RedisVL](https://redis.io/docs/latest/develop/ai/redisvl)

### LangChain Integration

Use Redis with LangChain for vector stores, semantic caching, and chat message history.

- **Vector Store**: Store and retrieve embeddings for RAG applications
- **Semantic Cache**: Cache LLM responses based on semantic similarity
- **Chat History**: Persist conversation history for AI agents

[Learn more about LangChain integration](https://redis.io/docs/latest/integrate/langchain-redis)

### Client Libraries with Vector Search

All major Redis client libraries support vector search operations:

- **redis-py (Python)**: [Vector search guide](https://redis.io/docs/latest/develop/clients/redis-py/vecsearch)
- **node-redis (JavaScript)**: [Vector search guide](https://redis.io/docs/latest/develop/clients/nodejs/vecsearch)
- **Jedis (Java)**: [Vector search guide](https://redis.io/docs/latest/develop/clients/jedis/vecsearch)
- **NRedisStack (C#/.NET)**: [Vector search guide](https://redis.io/docs/latest/develop/clients/dotnet/nredisstack/vecsearch)
- **go-redis (Go)**: [Vector search guide](https://redis.io/docs/latest/develop/clients/go/vecsearch)

## Getting Started

### Quick Start Guides

- [Redis vector database quick start](https://redis.io/docs/latest/develop/get-started/search-tutorial/vector-search)
- [RAG quick start guide](https://redis.io/docs/latest/develop/get-started/rag)

### Tutorials and Examples

Explore our [AI notebooks collection](https://redis.io/docs/latest/develop/ai/notebook-collection) with examples for:

- RAG implementations with RedisVL, LangChain, and LlamaIndex
- Advanced RAG techniques and optimizations
- Integration with cloud platforms like Azure and Vertex AI

### Video Tutorials

Watch our [AI video collection](https://redis.io/docs/latest/develop/ai/ai-videos) for practical demonstrations.

## Use Cases

- **Retrieval-Augmented Generation (RAG)**: Enhance LLM responses with relevant context
- **Semantic Search**: Find similar documents, images, or products
- **Recommendation Systems**: Build real-time personalized recommendations
- **AI Agents**: Create autonomous agents with memory and tool use
- **Chatbots**: Build conversational AI with context and history

## Additional Resources

- [Complete AI documentation](https://redis.io/docs/latest/develop/ai)
- [Ecosystem integrations](https://redis.io/docs/latest/develop/ai/ecosystem-integrations)
- [Vector search benchmarks](https://redis.io/blog/benchmarking-results-for-vector-databases/)
- [RAG best practices](https://redis.io/blog/get-better-rag-responses-with-ragas/)


