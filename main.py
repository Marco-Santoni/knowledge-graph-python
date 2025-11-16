import asyncio
from llama_index.core.agent.workflow import AgentWorkflow
from llama_index.llms.ollama import Ollama
from llama_index.core.workflow import Context
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader


# Define a simple calculator tool
def multiply(a: float, b: float) -> float:
    """Useful for multiplying two numbers."""
    return a * b

embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-base-en-v1.5")
llm = Ollama(
        model="llama3.1",
        request_timeout=360.0,
        # Manually set the context window to limit memory usage
        context_window=8000,
    )

# Create a RAG tool using LlamaIndex
documents = SimpleDirectoryReader("data").load_data()
print(f"Loaded {len(documents)} documents.")
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model,
)
print("Created vector store index.")
query_engine = index.as_query_engine(
    llm=llm,
)

# create context
ctx = Context(agent)

async def main():
    # Run the agent
    response = await agent.run("What is 1234 * 4567?", ctx=ctx)
    print(str(response))
    response = await agent.run("What was the multiplication? Write only the 2 numbers.", ctx=ctx)
    print(str(response))
    response = await agent.run("What did the author do in college?", ctx=ctx)
    print(str(response))

async def search_documents(query: str) -> str:
    """Useful for answering natural language questions about an personal essay written by Paul Graham."""
    response = await query_engine.aquery(query)
    return str(response)

# Create an enhanced workflow with both tools
agent = AgentWorkflow.from_tools_or_functions(
    [multiply, search_documents],
    llm=llm,
    system_prompt="""You are a helpful assistant that can perform calculations
    and search through documents to answer questions.""",
)


# Run the agent
if __name__ == "__main__":
    asyncio.run(main())