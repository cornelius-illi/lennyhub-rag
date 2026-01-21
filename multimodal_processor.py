"""
Multimodal Processing Module for LennyHub RAG

This module provides utilities for handling multimodal data, specifically
for parsing images from markdown files and generating embeddings for them
using CLIP models.
"""

import re
from pathlib import Path
from typing import List, Optional
import numpy as np
from PIL import Image

# Global cache for the embedding model
_image_embedder = None


def parse_markdown_images(content: str, file_path: Path) -> List[Path]:
    """
    Find all local image links in markdown content and return their absolute paths.

    Args:
        content: The markdown text content.
        file_path: The path to the markdown file, used to resolve relative image paths.

    Returns:
        A list of absolute Path objects for each found image.
    """
    # Regex to find markdown image syntax: ![alt text](path)
    # It specifically avoids matching http/https URLs.
    image_pattern = re.compile(r"!\[.*?\]\((?!https?://)(.*?)\)")
    image_paths = image_pattern.findall(content)

    absolute_paths = []
    base_dir = file_path.parent
    for img_path in image_paths:
        abs_path = base_dir / img_path
        if abs_path.exists():
            absolute_paths.append(abs_path)
        else:
            print(f"Warning: Image not found at path: {abs_path}")
    return absolute_paths


class ImageEmbedder:
    """
    A class to handle the embedding of images using FastEmbed's CLIP models.
    """

    def __init__(self, model_name: str = "clip-ViT-B-32-multilingual-v1"):
        """
        Initializes the ImageEmbedder and loads the specified CLIP model.
        """
        try:
            from fastembed.embedding import ImageEmbedding

            self.model = ImageEmbedding(model_name=model_name)
        except ImportError:
            print("Error: fastembed is not installed. Please run 'pip install fastembed'.")
            self.model = None
        except Exception as e:
            print(f"Error initializing FlagEmbedding model: {e}")
            self.model = None

    def embed(self, image_paths: List[Path]) -> Optional[List[np.ndarray]]:
        """
        Generates embeddings for a list of image files.

        Args:
            image_paths: A list of Path objects for the images to embed.

        Returns:
            A list of numpy arrays representing the embeddings, or None if the model is not available.
        """
        if not self.model:
            return None
        try:
            # fastembed's FlagEmbedding model can take a list of image paths directly
            embeddings = list(self.model.embed(image_paths))
            return embeddings
        except Exception as e:
            print(f"Error generating image embeddings: {e}")
            return None


def get_image_embedder():
    """
    Returns a cached, global instance of the ImageEmbedder.
    """
    global _image_embedder
    if _image_embedder is None:
        _image_embedder = ImageEmbedder()
    return _image_embedder

