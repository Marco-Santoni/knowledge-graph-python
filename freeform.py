from llama_index.core import PropertyGraphIndex
from llama_index.core import SimpleDirectoryReader
from llama_index.core.indices.property_graph import SimpleLLMPathExtractor
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.graph_stores.neo4j import Neo4jPropertyGraphStore

documents = SimpleDirectoryReader(input_files=["data/dev-journey-2-databricks-obj-management.md"]).load_data()
print(f"Loaded {len(documents)} documents.")

# Configure local LLM
## Ollama also supports a JSON mode, which tries to ensure all responses are valid JSON.
## This is particularly useful when trying to run tools that need to parse structured outputs.
llm = Ollama(
        model="llama3.1",
        request_timeout=3600.0,
        json_mode=True,
        # Manually set the context window to limit memory usage
        context_window=8000,
    )

# Configure local embeddings to avoid OpenAI
embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-small-en-v1.5")

# Set global defaults to use local models
Settings.llm = llm
Settings.embed_model = embed_model

kg_extractor = SimpleLLMPathExtractor(llm=llm)

# https://developers.llamaindex.ai/python/examples/property_graph/property_graph_advanced/
graph_store = Neo4jPropertyGraphStore(
    username="neo4j",
    password="password",
    url="bolt://localhost:7687",
)

print("Extracting knowledge graph...")
index = PropertyGraphIndex.from_documents(
    documents,
    kg_extractor=kg_extractor,
    embed_model=embed_model,
    property_graph_store=graph_store,
    show_progress=True
)
print("Created property graph index.")