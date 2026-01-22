# 🎙️ LennyHub RAG

A production-ready RAG (Retrieval-Augmented Generation) system built on transcripts from [Lenny's Podcast](https://www.lennysnewsletter.com/podcast), featuring conversations with top product leaders and growth experts.

## 🌟 Key Features

- **🚀 One-Command Setup**: Automated installation and indexing with `setup_rag.py`
- **💬 Conversational Interface**: Beautiful Chainlit UI for interactive querying and follow-up questions
- **🕸️ Interactive Graph Viewer**: Explore 544 people and their connections with clickable network visualization
- **🗄️ Qdrant Vector Database**: Production-grade local vector storage (no Docker needed)
- **📊 Knowledge Graph RAG**: Advanced retrieval with LightRAG entity and relationship extraction
- **🔍 Multiple Search Modes**: Hybrid, local, global, and naive search strategies
- **📚 297 Podcast Transcripts**: Comprehensive knowledge base from industry leaders
- **⚡ Fast & Efficient**: Caching, parallel processing, and optimized embeddings

## 📊 Dataset

### 297 Podcast Transcripts Available

Featuring conversations with:
- **Product Leaders**: Julie Zhuo, Shreyas Doshi, Adam Fishman
- **Growth Experts**: Brian Balfour, Elena Verna, Kevin Kwok
- **Founders**: Patrick Collison, Amjad Masad, Andrew Wilkinson
- **Executives**: Ada Chen Rekhi, Claire Hughes Johnson, Gokul Rajaram
- And many more!

**Topics covered**: Product management, growth strategy, career development, startup advice, leadership, decision-making frameworks, and more.

## 🚀 Quick Start (4 Steps)

### 1. Clone the Repository

```bash
git clone https://github.com/traversaal-ai/lennyhub-rag.git
cd lennyhub-rag
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Key

```bash
# Copy example environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=your-key-here
```

### 4. Run Automated Setup

```bash
# Process all 297 transcripts into the unified collection
python setup_rag.py --source-dir data/lennys-podcast --parallel
```

**Quick Test (first 10 transcripts):**
```bash
python setup_rag.py --source-dir data/lennys-podcast --quick
```

**What this does:**
- ✅ Installs Qdrant locally (if needed)
- ✅ Starts Qdrant server
- ✅ Builds embeddings and knowledge graph (sequential or parallel)
- ✅ Automatically resumes from where you left off
- ✅ Tests the system automatically

## 💬 Web Interface (Chainlit)

Launch the conversational web UI:

```bash
./run_chainlit.sh
```

**Features:**
- 🔍 **Interactive Querying**: Ask questions and get cited answers
- 🔄 **Conversational Memory**: Keep track of the context for follow-up questions
- ⚙️ **Advanced Settings**: Toggle search modes (hybrid, local, global, naive) in real-time
- 📊 **Citations**: See exactly which transcripts were used to generate the answer

## 🕸️ Knowledge Graph Viewer

Explore the network of people and their connections from Lenny's podcasts with an interactive graph visualization.

```bash
python serve_graph.py
```

The graph will automatically open in your browser at `http://localhost:8000/graph_viewer_simple.html`

## 💻 Command Line Interface

### Interactive Query Mode

```bash
python query_rag.py --interactive
```

### Single Queries

```bash
python query_rag.py "What is a curiosity loop?"
python query_with_sources.py "How do you build a great product team?"
```

## 🏗️ Technical Stack

- **RAG Framework**: [RAG-Anything](https://github.com/HKUDS/RAG-Anything)
- **Knowledge Graph**: [LightRAG](https://github.com/HKUDS/LightRAG)
- **Vector Database**: [Qdrant](https://qdrant.tech/)
- **LLM & Embeddings**: OpenAI GPT-4o-mini & text-embedding-3-small
- **Web UI**: Chainlit
- **Language**: Python 3.8+

## ⚙️ System Requirements

- **OS**: macOS, Linux, or Windows
- **Python**: 3.8 or higher (3.11 recommended)
- **RAM**: 2GB+ recommended
- **Internet**: Required for OpenAI API calls

## 🤝 Contributing

Contributions welcome! See [LICENSE](LICENSE) for details.

Built with ❤️ using RAG-Anything, LightRAG, Qdrant, and Chainlit
