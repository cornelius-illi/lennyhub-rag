import os
import numpy as np
from typing import Optional
from raganything import RAGAnything, RAGAnythingConfig
from lightrag.llm.openai import openai_complete_if_cache, openai_embed
from lightrag.utils import EmbeddingFunc
from .config import get_lightrag_kwargs

async def create_rag_instance(working_dir: Optional[str] = None, verbose: bool = False):
    """
    Create and initialize a RAG instance with standard configuration.
    
    Args:
        working_dir: Path to the RAG storage directory. 
                    Defaults to 'storage/rag' relative to the project root.
        verbose: Whether to print verbose output during initialization.
    """
    # Default working directory if not provided
    if working_dir is None:
        # If we are running from the root, it's storage/rag
        # If we are running from a subdirectory, we might need to adjust
        # But generally, we should try to use absolute paths or paths relative to root
        working_dir = os.path.join(os.getcwd(), "storage/rag")

    config = RAGAnythingConfig(
        working_dir=working_dir,
        parser="mineru",
        enable_image_processing=False,
        enable_table_processing=False,
        enable_equation_processing=False,
    )

    async def llm_model_func(prompt, system_prompt=None, history_messages=[], **kwargs):
        return await openai_complete_if_cache(
            "gpt-4o-mini",
            prompt,
            system_prompt=system_prompt,
            history_messages=history_messages,
            **kwargs
        )

    async def embedding_func(texts: list[str]) -> np.ndarray:
        return await openai_embed(texts, model="text-embedding-3-small")

    async def rerank_model_func(query: str, documents: list[str], top_n: int = None, **kwargs) -> list[dict]:
        """Local reranker function using fastembed."""
        from fastembed.rerank.cross_encoder import TextCrossEncoder
        
        # Lazy load model to save memory if not used and avoid startup delay
        if not hasattr(rerank_model_func, "model"):
            rerank_model_func.model = TextCrossEncoder(model_name="jinaai/jina-reranker-v1-turbo-en")
        
        # TextCrossEncoder.rerank returns an iterable of floats (scores)
        # in the same order as the input documents.
        scores = list(rerank_model_func.model.rerank(query, documents))
        
        # Convert to expected format: list of dicts with 'index' and 'relevance_score'
        results = [
            {"index": i, "relevance_score": score} 
            for i, score in enumerate(scores)
        ]

        # Sort by score descending
        results.sort(key=lambda x: x["relevance_score"], reverse=True)

        # Apply top_n if provided
        if top_n is not None:
            results = results[:top_n]
            
        return results

    # Get Qdrant config
    lightrag_kwargs = get_lightrag_kwargs(verbose=verbose)
    
    # Inject rerank config
    if "vector_db_storage_cls_kwargs" not in lightrag_kwargs:
        lightrag_kwargs["vector_db_storage_cls_kwargs"] = {}
    
    # These are LightRAG level kwargs
    lightrag_kwargs.update({
        "rerank_model_func": rerank_model_func,
        "min_rerank_score": 0.3 # Allow some lower scores but exclude noise
    })

    rag = RAGAnything(
        config=config,
        llm_model_func=llm_model_func,
        embedding_func=EmbeddingFunc(
            embedding_dim=1536,
            max_token_size=8192,
            func=embedding_func,
            model_name="text-embedding-3-small"
        ),
        lightrag_kwargs=lightrag_kwargs
    )

    # Ensure LightRAG is initialized (loads graphs/vdb)
    await rag._ensure_lightrag_initialized()
    return rag
