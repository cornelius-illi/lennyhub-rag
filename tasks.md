# Implementation Task Breakdown

This document lists the concrete tasks required to implement the multi-source and multimodal data onboarding plan.

## Phase 1: File System and Configuration
- [x] **Task 1.1: Create `data/lennys-podcast` directory.**
- [x] **Task 1.2: Move all existing podcast transcripts (`*.txt`) from `data/` into the new `data/lennys-podcast/` directory.**
- [x] **Task 1.3: Add new dependencies to `requirements.txt`.**
  - [x] Add `fastembed` for multimodal embeddings.
  - [x] Add `Pillow` for loading and handling images.

## Phase 2: Refactor Core Indexing Logic
- [x] **Task 2.1: Modify `setup_rag.py` to accept new command-line arguments.**
  - [x] Add `--source-dir` to specify the data location.
  - [x] Add `--collection-name` to specify the Qdrant collection.
- [x] **Task 2.2: Pass arguments to underlying build scripts.**
  - [x] Update `setup_rag.py` to forward the new arguments to `build_transcript_rag.py` and `build_transcript_rag_parallel.py`.
- [x] **Task 2.3: Update build scripts to use the new parameters.**
  - [x] Refactor `build_transcript_rag.py` and `build_transcript_rag_parallel.py` to use the `source_dir` and `collection_name` parameters instead of hardcoded values.
- [ ] **Task 2.4 (Optional but Recommended): Implement a one-time utility to rename the existing `lennyhub` collection to `lennys-podcast` to maintain consistency.**

## Phase 3: Implement Multimodal Indexing
- [x] **Task 3.1: Enhance Qdrant configuration logic.**
  - [x] Modify `qdrant_config.py` to dynamically configure collections with multiple named vectors (e.g., for text and images). This may involve a new argument in `setup_rag.py` like `--multimodal`.
- [x] **Task 3.2: Create a multimodal processing workflow.**
  - [x] In the build scripts, add logic to detect the data type (e.g., `.txt` vs `.md`).
  - [x] For markdown files, implement a function to parse the content and extract image paths.
- [x] **Task 3.3: Implement image embedding.**
  - [x] Create a new module or function that initializes a CLIP model (from `fastembed`) and generates an embedding for a given image file.
- [x] **Task 3.4: Modify data upload to Qdrant.**
  - [x] Update the logic that constructs the data points to be uploaded to Qdrant, allowing it to handle payloads with multiple named vectors (`text` and `image`).
