"""
Worker script for RAG queries - runs in a separate process to avoid event loop conflicts.
Called by streamlit_app.py via subprocess.
"""

import sys
import os
import json
import asyncio
import argparse

# Ensure environment variables are set
os.environ.setdefault("QDRANT_URL", "http://localhost:6333")

from dotenv import load_dotenv
load_dotenv()


async def run_query(question: str, mode: str = "hybrid", collection_name: str = None) -> dict:
    """Run a RAG query and return the result"""
    try:
        from raganything import RAGAnything, RAGAnythingConfig
        from lightrag.llm.openai import openai_complete_if_cache, openai_embed
        from lightrag.utils import EmbeddingFunc
        from qdrant_config import get_lightrag_kwargs
        import numpy as np

        config = RAGAnythingConfig(
            working_dir="./rag_storage",
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

        lightrag_kwargs = get_lightrag_kwargs(collection_name=collection_name, verbose=False)

        rag = RAGAnything(
            config=config,
            llm_model_func=llm_model_func,
            embedding_func=EmbeddingFunc(
                embedding_dim=1536,
                max_token_size=8192,
                func=embedding_func
            ),
            lightrag_kwargs=lightrag_kwargs
        )

        # Initialize and query
        await rag._ensure_lightrag_initialized()
        response = await rag.aquery(question, mode=mode)
        
        # Cleanup
        try:
            await rag.finalize_storages()
        except:
            pass
        try:
            rag.close()
        except:
            pass

        return {"success": True, "response": response, "error": None}

    except Exception as e:
        import traceback
        return {"success": False, "response": None, "error": f"{e}\n{traceback.format_exc()}"}


def main():
    """Main entry point - reads question from command line args"""
    parser = argparse.ArgumentParser(description="RAG Query Worker")
    parser.add_argument("question", type=str, help="The question to ask the RAG system")
    parser.add_argument("mode", type=str, nargs='?', default="hybrid", help="The query mode (e.g., hybrid, local)")
    parser.add_argument("--collection", type=str, default=None, help="The Qdrant collection to query against")
    args = parser.parse_args()
    
    # Run the query
    result = asyncio.run(run_query(args.question, args.mode, args.collection))
    
    # Output as JSON
    print(json.dumps(result))


if __name__ == "__main__":
    main()
