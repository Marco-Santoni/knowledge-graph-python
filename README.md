## Setup

Install [Ollama](https://github.com/ollama/ollama?tab=readme-ov-file#ollama) and download the model:

```bash
ollama pull llama3.1
```

Download txt files to the `data/` folder.

```bash
mkdir data
curl -o data/paul_graham_essay.txt https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/paul_graham/paul_graham_essay.txt
```

## Overview

1. explore how LLamaIndex works
2. build a knowledge graph using Neo4J as the graph store and free-form extraction of nodes and edges using LLMs

## Explore LLamaIndex

Run the script:

```bash
uv run main.py
```

## Build Knowledge Graph

### Setup Neo4J

You need Docker installed.

Run Neo4J with:

```bash
cd neo4j
docker compose up -d
```

You can view the Neo4J browser at: http://localhost:7474 (username: `neo4j`, password: `password`).

To stop it:

```bash
docker compose down
```

### Run the Knowledge Graph Script
Run the script that builds the knowledge graph via free-form extraction from a local markdown file:

```bash
uv run freeform.py
```