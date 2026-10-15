# Cassandra Vector Search Overview

## Overview
Introduced in Apache Cassandra 5.0, Vector Search enables AI and machine learning workloads directly within the database. It allows developers to store vector embeddings (mathematical representations of text, images, or audio) and perform similarity searches.

## How it Works
Cassandra uses Approximate Nearest Neighbor (ANN) search to quickly find vectors that are most similar to a query vector. Cassandra's implementation utilizes JVector, a state-of-the-art graph-based ANN library, integrated directly into the storage engine.

## Core Features
* **VECTOR Data Type:** A new primitive data type for storing dense float vectors.
* **Storage-Attached Indexing (SAI):** Vector search is built on top of Cassandra's SAI framework, allowing for efficient secondary indexing.
* **ANN Operator:** CQL includes a new `ORDER BY ... ANN OF` syntax to retrieve the most relevant embeddings.

## Example Usage
```cql
-- Create a table with a vector column (e.g., 1536 dimensions for OpenAI embeddings)
CREATE TABLE products ( id uuid PRIMARY KEY, name text, description_embedding vector<float, 1536> );

-- Create a custom index for vector search
CREATE CUSTOM INDEX ON products(description_embedding) USING 'StorageAttachedIndex';

-- Query using Approximate Nearest Neighbor (ANN)
SELECT id, name FROM products 
ORDER BY description_embedding ANN OF [0.1, 0.5, -0.2, ...] LIMIT 5;
```