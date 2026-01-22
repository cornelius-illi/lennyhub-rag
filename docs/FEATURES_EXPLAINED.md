# Knowledge Graph Viewer

A simplified, working knowledge graph visualization for the LennyHub RAG system.

## What's New

This is a simpler, more reliable version that:
- ✅ Uses D3.js force-directed graph (lighter & faster)
- ✅ Dark theme that's easy on the eyes
- ✅ Better error handling and loading states
- ✅ Works with large graphs (5000+ nodes)
- ✅ Interactive controls (drag, zoom, search, click)
- ✅ Built-in Python server for easy viewing

## Quick Start

### Option 1: Using Python Server (Recommended)

```bash
# Start the server
python serve_graph.py

# The graph will open automatically in your browser
# If not, visit: http://localhost:8000/graph_viewer_simple.html
```

### Option 2: Using Any HTTP Server

```bash
# Using Python's built-in server
python -m http.server 8000

# Then open: http://localhost:8000/graph_viewer_simple.html
```

**Important**: Don't open the HTML file directly (file:// protocol) - it needs to be served via HTTP to load the JSON data.

## Features

### Interactive Controls
- **Drag nodes**: Click and drag any node to reposition it
- **Zoom**: Scroll wheel to zoom in/out
- **Pan**: Drag the background to move around
- **Search**: Type in the search box to find and highlight entities
- **Click node**: View detailed information in the sidebar
- **Double-click node**: Focus and zoom to that node

### Sidebar
- **Stats**: Total nodes and links
- **Search**: Find entities by name or description
- **Reset View**: Return to default zoom and position
- **Restart Simulation**: Re-run the physics simulation
- **Node Details**: Click any node to see its full information

### Color Coding
- 🔴 **Red**: Person
- 🔵 **Blue**: Organization/Platform
- 🟣 **Purple**: Concept
- 🟠 **Orange**: Method
- 🟢 **Green**: Product
- ⚫ **Gray**: Other types

## Performance Notes

- The graph automatically limits edges to 5,000 for performance
- Labels are shown for the first 100 nodes only
- Hover over any node to see its name
- The simulation will stabilize after a few seconds

## Files

- `graph_viewer_simple.html` - The main visualization file
- `graph_data.json` - Your knowledge graph data
- `serve_graph.py` - Simple Python server to view the graph

## Troubleshooting

### Graph won't load
- Make sure `graph_data.json` exists in the same directory
- Ensure you're using HTTP (not file://) to serve the page
- Check browser console (F12) for error messages

### Performance issues
- The graph limits edges automatically
- Try restarting the simulation with the button
- Close other browser tabs
- Disable the physics simulation by commenting out the force simulation restart

### Can't see all nodes
- Use the search function to find specific entities
- Zoom out using the Zoom - button or scroll wheel
- Reset the view with the Reset View button

## Technical Details

- **Visualization**: D3.js v7 force-directed graph
- **Data format**: JSON with nodes and edges arrays
- **Browser compatibility**: Modern browsers (Chrome, Firefox, Safari, Edge)
- **File size**: Optimized for graphs up to 10,000 nodes

## Next Steps

Want to customize the visualization? Edit `graph_viewer_simple.html`:
- Line 24-46: Adjust colors and styling
- Line 417-420: Modify force simulation parameters
- Line 442-444: Change node appearance
- Line 486-494: Customize search behavior

Enjoy exploring your knowledge graph! 🎉
# Querying RAG with Chunk-Level Source Attribution

This guide explains how to query the RAG system and see the **specific chunks** used to generate answers, rather than just the overall source document.

## Available Query Scripts

### 1. `query_rag.py` (Original)
**Shows:** Final answer only

```bash
python query_rag.py "What is a curiosity loop?"
python query_rag.py --interactive
```

**Output:**
- ✅ Generated answer
- ❌ No source information
- ❌ No chunk details

---

### 2. `query_rag_with_chunks.py` (NEW)
**Shows:** Retrieved chunks + Final answer

```bash
python query_rag_with_chunks.py "What is a curiosity loop?"
python query_rag_with_chunks.py --interactive
```

**Output:**
```
📚 RETRIEVED CHUNKS (Used to generate the answer):
================================================================================

Found 5 relevant chunks:

────────────────────────────────────────────────────────────────────────────────
CHUNK 1:
────────────────────────────────────────────────────────────────────────────────
[Actual text content from the knowledge base that was used...]

────────────────────────────────────────────────────────────────────────────────
CHUNK 2:
────────────────────────────────────────────────────────────────────────────────
[More text content...]

💡 GENERATED ANSWER:
================================================================================
[Final synthesized answer based on the chunks above]
```

**Interactive Mode Commands:**
- `show-chunks` - Enable chunk display
- `no-chunks` - Disable chunk display
- `quit` - Exit

---

### 3. `query_with_sources.py` (NEW - Most Detailed)
**Shows:** Retrieved chunks + Source documents + Final answer

```bash
python query_with_sources.py "What is a curiosity loop?"
```

**Output:**
```
📚 RETRIEVED SOURCES:
====================================================================================================

Retrieved from 2 source document(s):

════════════════════════════════════════════════════════════════════════════════════════════════════
📄 SOURCE: Ada Chen Rekhi
   Chunks used: 3
════════════════════════════════════════════════════════════════════════════════════════════════════

┌─ Chunk 1 ───────────────────────────────────────────────────────────────────────────────────────
│ Chunk ID: chunk-3ef01b14864e33f95632c541afb0e371
│
│ [Specific text from Ada Chen Rekhi transcript...]
└──────────────────────────────────────────────────────────────────────────────────────────────────

┌─ Chunk 2 ───────────────────────────────────────────────────────────────────────────────────────
│ Chunk ID: chunk-813fa4d6ddad5e5e9b3c0409a3eb009e
│
│ [More text from Ada Chen Rekhi transcript...]
└──────────────────────────────────────────────────────────────────────────────────────────────────

════════════════════════════════════════════════════════════════════════════════════════════════════
📄 SOURCE: Adam Fishman
   Chunks used: 2
════════════════════════════════════════════════════════════════════════════════════════════════════

[Additional chunks from different source...]

💡 GENERATED ANSWER:
====================================================================================================
[Final answer with citation traceability]

✓ Answer generated using 5 chunk(s) from 2 source(s)
```

---

## How It Works

### The `only_need_context` Parameter

LightRAG provides a parameter called `only_need_context` that:
- ✅ Performs the full retrieval process (vector search + knowledge graph traversal)
- ✅ Returns the retrieved chunks
- ❌ Skips LLM answer generation

**Example:**
```python
from lightrag import QueryParam

# Get chunks without generating answer
query_param = QueryParam(mode="hybrid", only_need_context=True)
context = await rag.lightrag.aquery(question, param=query_param)

# context contains the retrieved chunks as a string
```

### Chunk Metadata

Each chunk is stored with metadata including:
- **Chunk ID**: Unique identifier (e.g., `chunk-3ef01b14864e33f95632c541afb0e371`)
- **Content**: The actual text segment
- **Source Document**: Which transcript/file it came from
- **Embeddings**: Vector representation for similarity search

This metadata is stored in:
- `rag_storage/kv_store_text_chunks.json` - Chunk content and metadata
- `rag_storage/kv_store_doc_status.json` - Document-to-chunk mappings
- `rag_storage/vdb_chunks.json` - Vector embeddings

---

## Comparison Table

| Feature | query_rag.py | query_rag_with_chunks.py | query_with_sources.py |
|---------|--------------|--------------------------|----------------------|
| Final Answer | ✅ | ✅ | ✅ |
| Retrieved Chunks | ❌ | ✅ | ✅ |
| Source Document Names | ❌ | ❌ | ✅ |
| Chunk IDs | ❌ | ❌ | ✅ |
| Grouped by Source | ❌ | ❌ | ✅ |
| Interactive Mode | ✅ | ✅ | ❌ |

---

## Use Cases

### When to Use `query_rag.py`
- Quick queries where you just need the answer
- Production use cases where users don't need to see sources
- When minimizing output length

### When to Use `query_rag_with_chunks.py`
- Debugging: Understanding what context was retrieved
- Research: Seeing the raw text that informed the answer
- Transparency: Showing users what information was used

### When to Use `query_with_sources.py`
- Maximum transparency: Need to trace back to exact source documents
- Multi-document scenarios: Want to see which transcripts contributed
- Citation requirements: Need proper attribution with chunk IDs
- Quality assurance: Verifying retrieval quality

---

## Example Queries

### Question 1: Single-source question
```bash
python query_with_sources.py "What is a curiosity loop?"
```
Expected: Chunks primarily from Ada Chen Rekhi transcript

### Question 2: Multi-source question
```bash
python query_with_sources.py "What are frameworks for career development?"
```
Expected: Chunks from multiple transcripts (Ada Chen Rekhi, Adam Fishman, etc.)

### Question 3: Specific person question
```bash
python query_with_sources.py "What does Adam Fishman say about onboarding?"
```
Expected: Chunks specifically from Adam Fishman transcript

---

## Technical Details

### Retrieval Process

1. **Query Embedding**: Question is converted to vector representation
2. **Entity Search**: Find relevant entities in knowledge graph
3. **Relationship Traversal**: Follow entity connections
4. **Chunk Retrieval**: Get text chunks associated with entities
5. **Ranking**: Sort chunks by relevance
6. **Context Assembly**: Combine chunks with separators
7. **Answer Generation**: LLM synthesizes final answer from context

### Context Format

LightRAG returns context with chunks separated by `"-----"`:
```
[Chunk 1 content]
-----
[Chunk 2 content]
-----
[Chunk 3 content]
```

The scripts parse this format and enhance it with source attribution.

### Chunk Size

Default chunk settings:
- **Max tokens per chunk**: 4000 tokens
- **Overlap**: Configurable (helps maintain context across boundaries)
- **Separator**: `"-----"` between chunks

---

## Benefits of Chunk-Level Attribution

1. **Transparency**: Users see exactly what text informed the answer
2. **Verification**: Easy to check if retrieval is working correctly
3. **Trust**: Builds confidence by showing sources
4. **Debugging**: Identify when wrong chunks are retrieved
5. **Citation**: Proper attribution to original sources
6. **Quality Control**: Spot-check chunk relevance

---

## Cost Implications

### `only_need_context=True` (Chunks Only)
- **Embedding cost**: ~$0.0001 per query
- **No LLM cost**: Skips answer generation
- **Total**: ~$0.0001 per query

### Standard Query (Chunks + Answer)
- **Embedding cost**: ~$0.0001
- **LLM cost**: ~$0.001-0.01 (depending on context size)
- **Total**: ~$0.001-0.01 per query

The new scripts call the API twice (once for chunks, once for answer), so cost is slightly higher but still minimal (~$0.002-0.02 per query).

---

## Next Steps

1. **Try the scripts**: Run example queries with each script
2. **Compare outputs**: See the difference in transparency
3. **Choose the right tool**: Pick the script that fits your needs
4. **Integrate**: Use `only_need_context` in your own applications

---

## References

- **LightRAG Documentation**: https://github.com/HKUDS/LightRAG
- **QueryParam Class**: Includes `only_need_context`, `top_k`, `mode`, etc.
- **RAG-Anything**: https://github.com/HKUDS/RAG-Anything

---

**Created**: January 2026
**Last Updated**: January 2026
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

In summary, the scripts offer a tiered approach to querying, allowing the user to choose between getting a simple answer, inspecting the retrieved context, or performing a full audit of the information and its sources.# Transcript RAG System

This directory contains a RAG (Retrieval-Augmented Generation) system built on podcast transcripts using the RAG-Anything package.

## Transcripts

The system includes two podcast transcripts from Lenny's Podcast:

1. **Ada Chen Rekhi.txt** - Executive coach and co-founder of Notejoy
   - Topics: Curiosity loops, career strategy, values exercises, working with partners

2. **Adam Fishman.txt** - Former VP of Growth at Lyft and Patreon
   - Topics: Growth competency model, onboarding optimization, company selection framework

## Setup Instructions

### Prerequisites

1. **Install the package** (already done):
   ```bash
   pip install raganything
   ```

2. **Set up OpenAI API key**:
   ```bash
   export OPENAI_API_KEY='your-api-key-here'
   ```

   Get your API key from: https://platform.openai.com/api-keys

### Build the RAG System

Run the provided script to index the transcripts:

```bash
python build_transcript_rag.py
```

This script will:
- Initialize the RAG system with LightRAG
- Process both transcript files
- Build a knowledge graph from the content
- Create embeddings for semantic search

## Sample Questions

Here are example questions you can ask the RAG system:

### About Ada Chen Rekhi:

1. **What is a curiosity loop and how does it work?**
   - Learn about Ada's structured approach to gathering advice

2. **What are Ada's personal values?**
   - Understand the values exercise and how to apply it

3. **What advice does Ada give about building an early career?**
   - Explore the "explore and exploit" framework

4. **What is the 'eating your vegetables' concept?**
   - Learn about developing skills through deliberate practice

5. **Should you start a company with your partner?**
   - Hear Ada's experience and advice on co-founding with a spouse

6. **What is the explore and exploit framework for career development?**
   - Understand when to explore new opportunities vs. double down

7. **How do you avoid being the 'boiled frog' in your career?**
   - Learn to recognize when it's time to make a change

### About Adam Fishman:

8. **What is Adam Fishman's growth competency model?**
   - Understand the framework for hiring and evaluating growth people

9. **What are the four main components of the growth competency model?**
   - Growth execution, customer knowledge, growth strategy, communication & influence

10. **Why is onboarding important for growth?**
    - Learn about the outsized impact of onboarding optimization

11. **What is the PMF framework for choosing a company to work at?**
    - People, Mission, Financials - how to evaluate job opportunities

12. **How can onboarding improve retention?**
    - Real examples of 10-25% improvements in cohort retention

13. **What mistakes do founders make when hiring growth people?**
    - Common pitfalls and how to avoid them

## Query the RAG System

Once the RAG is built, you can query it with:

```python
import asyncio
from raganything import RAGAnything, RAGAnythingConfig
from lightrag.llm import openai_complete_if_cache, openai_embedding
from lightrag.utils import EmbeddingFunc
import numpy as np

async def query_rag(question: str):
    # Configure RAG
    config = RAGAnythingConfig(working_dir="./rag_storage")

    # Set up LLM functions
    async def llm_model_func(prompt, system_prompt=None, history_messages=[], **kwargs):
        return await openai_complete_if_cache(
            "gpt-4o-mini", prompt,
            system_prompt=system_prompt,
            history_messages=history_messages,
            **kwargs
        )

    async def embedding_func(texts: list[str]) -> np.ndarray:
        return await openai_embedding(texts, model="text-embedding-3-small")

    # Initialize RAG
    rag = RAGAnything(
        config=config,
        llm_model_func=llm_model_func,
        embedding_func=EmbeddingFunc(
            embedding_dim=1536,
            max_token_size=8192,
            func=embedding_func
        )
    )

    # Ensure LightRAG is initialized
    await rag._ensure_lightrag_initialized()

    # Query the RAG
    response = await rag.aquery(question, mode="hybrid")
    print(f"\nQuestion: {question}")
    print(f"\nAnswer:\n{response}\n")

    rag.close()

# Example usage
asyncio.run(query_rag("What is a curiosity loop and how does it work?"))
```

## Query Modes

The RAG system supports different query modes:

- **`naive`**: Simple keyword search
- **`local`**: Local context-based search
- **`global`**: Global knowledge graph search
- **`hybrid`**: Combines local and global (recommended)
- **`mix`**: Mixes multiple approaches

## Tips for Best Results

1. **Be specific**: Ask focused questions rather than broad topics
2. **Use names**: Mention "Ada" or "Adam" to get person-specific insights
3. **Ask about frameworks**: The transcripts contain many frameworks and models
4. **Follow up**: Ask clarifying questions based on initial responses

## File Structure

```
rag-anything/
├── data/
│   ├── Ada Chen Rekhi.txt
│   └── Adam Fishman.txt
├── rag_storage/          # Generated after building RAG
├── build_transcript_rag.py
├── query_rag.py          # Simple query script
└── README_TRANSCRIPT_RAG.md
```

## Troubleshooting

### "OPENAI_API_KEY not set"
- Make sure you export the API key in your terminal session
- Or add it to your `.env` file

### "ModuleNotFoundError: No module named 'raganything'"
- Activate the correct conda environment
- Or reinstall: `pip install raganything`

### Memory issues
- The transcripts are large (~80-90KB each)
- Ensure you have enough RAM
- Consider processing one transcript at a time if needed

## Cost Estimate

Building the RAG system will use OpenAI API:
- Embeddings: ~$0.01-0.02 per transcript
- Knowledge graph extraction: ~$0.10-0.20 total
- Queries: ~$0.001-0.01 per query

Total setup cost: **~$0.25**

## Next Steps

1. Build the RAG system with the provided script
2. Try the sample questions
3. Explore the transcripts with your own questions
4. Combine insights from both Ada and Adam on career and growth topics!
