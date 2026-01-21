# Implementation Plan: Multi-Source & Multimodal Data Onboarding

This document outlines the strategy for restructuring the project's data directory, modifying the data indexing process to support multiple, separate data sources within Qdrant, and extending the system to handle multimodal (text + image) data.

## Part 1: Data Directory Restructuring

**Objective:** Isolate the existing Lenny's Podcast transcripts into a dedicated subdirectory to create a clear and scalable data structure for future sources.

### 1.1 Action Steps:

1.  **Create Directory:** Create a new directory at `data/lennys-podcast/`.
2.  **Move Files:** Move all `*.txt` files from the root of `data/` into the new `data/lennys-podcast/` directory.
3.  **Resulting Structure:**

    ```
    .
    └── data/
        ├── lennys-podcast/
        │   ├── Ada Chen Rekhi.txt
        │   └── ...
        └── cutlefish.substack.com/
            ├── some-post.md
            └── attachments/
                └── some-image.png
    ```

---

## Part 2: Strategy for Separate & Persistent Database Indexing

**Objective:** Generalize the data indexing process to allow creating and populating distinct Qdrant collections for different data sources while ensuring existing data is preserved.

### 2.1 Data Preservation Guarantee:

**The existing `lennyhub` Qdrant collection will not be modified or deleted.** The strategy below focuses on creating *new*, separate collections for each data source. The costly and time-consuming initial build will be preserved. For consistency, we can rename the existing collection from `lennyhub` to `lennys-podcast` using a non-destructive Qdrant operation.

### 2.2 Proposed Modifications:

The core of this plan is to refactor `setup_rag.py` to make it a generic indexing entry point.

1.  **Introduce Command-Line Arguments:** Modify `setup_rag.py` to accept:
    *   `--source-dir`: The path to the directory containing the source documents.
    *   `--collection-name`: The desired name for the Qdrant collection.

2.  **Update Indexing Logic:**
    *   The script will use these arguments to process files from the specified directory and index them into the specified Qdrant collection. This ensures strict data isolation.

### 2.3 Example Usage:

**A) To index the Cuttlefish blog (new):**
```bash
python setup_rag.py --source-dir data/cutlefish.substack.com --collection-name cuttlefish-blog --parallel
```

**B) To index Lenny's Podcast in the future (if needed):**
```bash
python setup_rag.py --source-dir data/lennys-podcast --collection-name lennys-podcast --parallel
```

---

## Part 3: Multimodal RAG for Image Support

**Objective:** Extend the RAG system to index and retrieve images from the Cuttlefish blog posts alongside text.

### 3.1 Proposed Technology:

*   **Multimodal Embeddings:** Use a **CLIP model** from the `fastembed` library to generate vector embeddings for images. CLIP models embed images and text in the same vector space, enabling text-to-image search.
*   **Multi-Vector Storage:** Utilize **Qdrant's Named Vectors** feature to store both a `text` vector (from OpenAI) and an `image` vector (from CLIP) for each document point.

### 3.2 Implementation Strategy:

1.  **Dependency:** Add `fastembed` to `requirements.txt`.
2.  **Qdrant Collection Setup:** When creating the `cuttlefish-blog` collection, configure it to support two named vectors: `text` and `image`.
3.  **Update Indexing Process:** When processing the Cuttlefish blog posts, the script will:
    a. Parse the Markdown to find image links (e.g., `![...](attachments/image.png)`).
    b. For each post with an image, it will generate **two embeddings**:
        i. A text embedding from the post's content using the existing OpenAI model.
        ii. An image embedding from the referenced image file using a CLIP model.
    c. Both embeddings will be uploaded to a single point in Qdrant, identified by the `text` and `image` vector names. Posts without images will only contain a `text` vector.

### 3.3 Retrieval Strategy (Future Work):

When querying the `cuttlefish-blog` collection, the user's text query will be embedded twice: once with the OpenAI model and once with the CLIP model. The system will then perform two searches in Qdrant—one against `text` vectors and one against `image` vectors—and merge the results to retrieve the most relevant text and image content.

---

## Part 4: Future Considerations - Querying

This implementation focuses on data ingestion. As a next step, the querying interfaces (`streamlit_app.py`, `query_rag.py`, etc.) will need to be updated. They will require a mechanism (e.g., a dropdown in the UI or a command-line flag) to allow the user to select which Qdrant collection they wish to query against.