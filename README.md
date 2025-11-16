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

## Run

Run the script:

```bash
uv run main.py
```