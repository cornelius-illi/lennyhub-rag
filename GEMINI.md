# Project Overview

This project is a Retrieval-Augmented Generation (RAG) system called "LennyHub RAG". It provides a searchable knowledge base built from transcripts of "Lenny's Podcast," which features conversations with leaders in product management, growth, and startups.

The core of the project is built with Python and utilizes several key technologies:
- **`raganything` and `lightrag`**: These are the primary frameworks used to build the RAG system, including entity and relationship extraction for knowledge graph-based retrieval.
- **`Qdrant`**: A vector database used for storing embeddings and enabling efficient similarity search. It is set up to run locally without requiring Docker.
- **`Chainlit`**: This library is used to create a conversational AI interface for interacting with the RAG system.
- **`OpenAI`**: The project leverages OpenAI's models (GPT-4o-mini and text-embedding-3-small) for generating answers and creating text embeddings.

The system offers both a web-based UI and a command-line interface for querying. It also includes an interactive knowledge graph viewer to explore connections between people mentioned in the podcasts.

# Building and Running

## 1. Installation

First, install the necessary Python dependencies:

```bash
pip install -r requirements.txt
```

## 2. Configuration

The project requires an OpenAI API key to function.

1.  Copy the example environment file:
    ```bash
    cp .env.example .env
    ```
2.  Edit the `.env` file and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your-key-here
    ```

## 3. Initial Setup and Data Indexing

The `scripts/setup_rag.py` script automates the process of setting up the Qdrant database and indexing the podcast transcripts.

-   **Quick setup (recommended for first-time use):**
    This processes a small subset of transcripts to quickly verify the setup.
    ```bash
    python scripts/setup_rag.py --source-dir data/lennys-podcast --quick
    ```
-   **Full setup (parallel mode for speed):**
    This processes all transcripts. The `--parallel` flag significantly speeds up the process.
    ```bash
    python scripts/setup_rag.py --source-dir data/lennys-podcast --parallel
    ```

## 4. Running the Application

### Web Interface (Chainlit)

To launch the web-based interface, run the following command:

```bash
./run_chainlit.sh
```

### Command-Line Interface (CLI)

For command-line querying, you can use the following scripts:

-   **Interactive mode:**
    ```bash
    python src/cli/query.py --interactive
    ```
-   **Single query:**
    ```bash
    python src/cli/query.py "What are the best practices for user onboarding?"
    ```
-   **Query with sources:**
    ```bash
    python src/cli/sources.py "How do you build a great product team?"
    ```

## 5. Knowledge Graph Viewer

To explore the knowledge graph of people and their connections, you can serve the interactive visualization:

```bash
python apps/explorer/server.py
```

This will open the graph viewer in your browser at `http://localhost:8000/viewer.html`.

# Repository Structure

- **`apps/`**: Interactive applications (Chat, Explorer).
- **`src/`**: Shared core logic (`core/`), CLI tools (`cli/`), and maintenance utilities (`tools/`).
- **`scripts/`**: Setup, indexing, and infrastructure management (Qdrant).
- **`docs/`**: Consolidated user and technical documentation.
- **`storage/`**: Unified persistent storage for the RAG system and vector database.

# Development Conventions

- **Code Style**: The project follows standard Python conventions (PEP 8).
- **Dependencies**: Managed through `pyproject.toml` and `requirements.txt`.
- **Configuration**: Environment variables (e.g., API keys, Qdrant settings) are managed in a `.env` file.
- **Common Engine**: All tools use the shared RAG engine in `src/core/engine.py` for consistent behavior.
- **Testing**: Use `python scripts/setup_rag.py --quick` as an integration test to verify the core components.
