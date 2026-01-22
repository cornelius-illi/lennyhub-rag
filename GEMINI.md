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

The `setup_rag.py` script automates the process of setting up the Qdrant database and indexing the podcast transcripts.

-   **Quick setup (recommended for first-time use):**
    This processes a small subset of transcripts to quickly verify the setup.
    ```bash
    python setup_rag.py --source-dir data/lennys-podcast --quick
    ```
-   **Full setup (parallel mode for speed):**
    This processes all transcripts. The `--parallel` flag significantly speeds up the process.
    ```bash
    python setup_rag.py --source-dir data/lennys-podcast --parallel
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
    python query_rag.py --interactive
    ```
-   **Single query:**
    ```bash
    python query_rag.py "What are the best practices for user onboarding?"
    ```
-   **Query with sources:**
    ```bash
    python query_with_sources.py "How do you build a great product team?"
    ```

## 5. Knowledge Graph Viewer

To explore the knowledge graph of people and their connections, you can serve the interactive visualization:

```bash
python serve_graph.py
```

This will open the graph viewer in your browser.

# Development Conventions

- **Code Style**: The project follows standard Python conventions (PEP 8).
- **Dependencies**: Python packages are managed through `requirements.txt`.
- **Configuration**: Environment variables (e.g., API keys, Qdrant settings) are managed in a `.env` file.
- **Modularity**: The project is structured with separate scripts for different concerns:
    - `setup_rag.py`: Initial setup and data indexing.
    - `chainlit_app.py`: The main file for the web application.
    - `query_*.py`: A set of scripts for CLI-based querying.
- **Testing**: While no formal testing framework is explicitly defined in the project structure, the `setup_rag.py --quick` command serves as a quick integration test to ensure the core components are working together correctly.
