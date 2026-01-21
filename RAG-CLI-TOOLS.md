# RAG CLI Tools Overview

Based on my analysis of the repository, the different query scripts offer three distinct levels of insight into the Retrieval-Augmented Generation (RAG) process. While the `README.md` file mentions how to use them, the detailed implementation differences are found within the scripts themselves.

Here’s a breakdown of the approaches in `query_rag.py`, `query_rag_with_chunks.py`, and `query_with_sources.py`:

## 1. `query_rag.py`: Basic Querying (Answer Only)

This script provides the most straightforward interaction with the RAG system.

*   **Approach**: It takes a user's question, passes it to the `RAGAnything` object's `aquery` method, and directly prints the final, synthesized answer.
*   **Functionality**: It is designed for users who only need the answer and are not concerned with the underlying retrieval process. It includes a simple interactive mode for continuous questioning.
*   **Use Case**: When you want a quick answer to a question without needing to verify the source or see the context the LLM used.

```python
# Simplified from query_rag.py
response = await rag.aquery(question, mode=mode)
print(f"\nAnswer:\n{response}\n")
```

## 2. `query_rag_with_chunks.py`: Querying with Context (Answer + Chunks)

This script offers a more transparent view by revealing the specific information the RAG system retrieved to formulate its answer.

*   **Approach**: It performs a two-step process:
    1.  First, it calls the RAG system with the `only_need_context=True` parameter. This retrieves the relevant text chunks from the vector database without generating an answer. These chunks are printed to the console.
    2.  Second, it makes a standard `aquery` call to generate and display the final answer based on that retrieved context.
*   **Functionality**: It allows you to see the exact pieces of text the LLM is "looking at" when it formulations a response. This is useful for debugging or understanding why the model gave a particular answer.
*   **Use Case**: When you want to understand what information the RAG system considered relevant to your question.

```python
# Simplified from query_rag_with_chunks.py

# Step 1: Get and display the context chunks
query_param = QueryParam(mode=mode, only_need_context=True)
context = await rag.lightrag.aquery(question, param=query_param)
# ... code to print the chunks ...

# Step 2: Get and display the final answer
response = await rag.aquery(question, mode=mode)
print(f"\n{response}\n")
```

## 3. `query_with_sources.py`: Querying with Full Attribution (Answer + Chunks + Source Files)

This script provides the highest level of transparency, tracing retrieved information back to its original source document.

*   **Approach**: This is the most complex of the three scripts. It builds on the previous approach by adding a metadata-loading step.
    1.  It loads JSON files from the `rag_storage` directory (`kv_store_text_chunks.json`, `kv_store_doc_status.json`, etc.) to create an in-memory map of chunk IDs to their original source filenames (e.g., `Ada Chen Rekhi.txt`).
    2.  Like the previous script, it retrieves the context chunks.
    3.  It then uses the metadata map to identify and display the source file for each retrieved chunk.
    4.  Finally, it generates and displays the final answer.
*   **Functionality**: It provides full "glass-box" visibility into the RAG pipeline, showing not just what information was used, but where it came from.
*   **Use Case**: Essential for fact-checking, serious research, or when you need to navigate from an answer back to the full context of the original podcast transcript.

```python
# Simplified from query_with_sources.py

# Step 1: Load metadata to map chunks to sources
metadata = load_chunk_metadata()

# Step 2: Get context chunks
query_param = QueryParam(mode=mode, only_need_context=True)
context = await rag.lightrag.aquery(question, param=query_param)

# Step 3: Extract sources and display chunks with their source file
chunks_info = extract_chunk_sources(context, metadata)
# ... code to print chunks grouped by source document ...

# Step 4: Generate the final answer
response = await rag.aquery(question, mode=mode)
print(f"\n{response}\n")
```

In summary, the scripts offer a tiered approach to querying, allowing the user to choose between getting a simple answer, inspecting the retrieved context, or performing a full audit of the information and its sources.