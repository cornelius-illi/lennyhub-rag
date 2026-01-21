
from typing import Optional
import chainlit as cl
import os
import sys
import asyncio
from dotenv import load_dotenv
import numpy as np
from chainlit.data.sql_alchemy import SQLAlchemyDataLayer

# Add current directory to path so we can import local modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Load environment variables
load_dotenv()

# Ensure Qdrant env var
if not os.getenv("QDRANT_URL"):
    os.environ["QDRANT_URL"] = "http://localhost:6333"

@cl.data_layer
def get_data_layer():
    return SQLAlchemyDataLayer(conninfo="sqlite+aiosqlite:///chainlit.db")

@cl.password_auth_callback
def auth_callback(username: str, password: str):
    """Authenticate the user."""
    import os
    # Default to admin/admin if not set in env
    valid_username = os.getenv("CHAINLIT_USERNAME")
    valid_password = os.getenv("CHAINLIT_PASSWORD")
    
    if (username, password) == (valid_username, valid_password):
        return cl.User(
            identifier=username,
            metadata={"role": "admin", "provider": "credentials"}
        )
    return None

@cl.on_chat_start
async def start():
    """Initialize the RAG system when a new chat session starts."""
    
    # 1. Check API Key
    if not os.getenv("OPENAI_API_KEY"):
        await cl.Message(
            content="⚠️ **OpenAI API Key is missing!**\nPlease set `OPENAI_API_KEY` in your `.env` file and restart."
        ).send()
        return

    # 2. Notify user that we are initializing
    msg = cl.Message(content="Initializing RAG system... (this may take a few seconds)")
    await msg.send()

    try:
        # 3. Create RAG instance (Async)
        rag = await create_rag_instance()
        
        # Store in user session
        cl.user_session.set("rag", rag)
        cl.user_session.set("history", []) # Initialize chat history
        
        # 4. Ready!
        msg.content = "**RAG System Ready!** 🚀\n\nAsk me anything about the podcasts. Example: *'What is a curiosity loop?'*"
        await msg.update()
        
    except Exception as e:
        msg.content = f"❌ **Initialization Failed**\nError: {str(e)}\n\nMake sure Qdrant is running (`./start_qdrant.sh`)"
        await msg.update()

@cl.on_message
async def main(message: cl.Message):
    """Handle incoming user messages."""
    
    rag = cl.user_session.get("rag")
    history = cl.user_session.get("history")
    
    if not rag:
        await cl.Message(content="⚠️ RAG system is not initialized. Please restart the session.").send()
        return

    # Visual "Thinking" Steps
    async with cl.Step(name="RAG Processing", type="run") as step:
        step.input = message.content
        
        try:
            # 1. Access Mode (default hybrid)
            mode = "hybrid"
            
            # 2. Rewrite Query if history exists
            final_query = message.content
            if history:
                async with cl.Step(name="Contextualizing", type="llm") as rewrite_step:
                    rewrite_step.input = message.content
                    final_query = await rewrite_query(rag, history, message.content)
                    rewrite_step.output = final_query
            
            # 3. Execute Query
            response = await rag.aquery(final_query, mode=mode, enable_rerank=True)
            
            # 4. Update History
            history.append({"role": "user", "content": message.content}) # Store original query
            history.append({"role": "assistant", "content": response})
            # Keep history short-ish to avoid context window issues (e.g., last 10 turns)
            if len(history) > 10:
                history = history[-10:]
            cl.user_session.set("history", history)
            
            step.output = "Query Completed"
            
        except Exception as e:
            step.output = f"Error: {str(e)}"
            await cl.Message(content=f"❌ **Query Failed**: {str(e)}").send()
            return

    # 5. Send final response
    await cl.Message(content=response).send()


async def rewrite_query(rag, history, current_query):
    """Rewrite the current query based on history to be standalone."""
    
    # Construct a simple history string or list for the prompt
    history_str = ""
    for msg in history:
        role = "User" if msg["role"] == "user" else "Assistant"
        content = msg["content"]
        # Truncate content slightly if too long to save tokens
        if len(content) > 200:
            content = content[:200] + "..."
        history_str += f"{role}: {content}\n"
        
    prompt = f"""Given the following conversation history and a new user question, rewrite the user's question to be a standalone query that captures all necessary context. 
If the question is already standalone, return it exactly as is.
DO NOT answer the question. JUST rewrite it.

Chat History:
{history_str}

User's New Question: {current_query}

Standalone Query:"""

    # We use the RAG's internal LLM function. 
    # Validating if we can access it directly or via a wrapper.
    # rag.llm_model_func is available from our create_rag_instance definition.
    
    try:
        # We need to call the llm function. 
        # The rag instance stores `llm_model_func`.
        # Note: raganything might wrap it, but we passed it in `create_rag_instance`.
        # Inspecting the file `chainlit_app.py`, we defined `llm_model_func` locally inside `create_rag_instance`, 
        # so it's not directly a method on `rag` unless `RAGAnything` exposes it.
        #
        # Looking at `RAGAnything` class standard usage (from `multimodal_processor.py` or `query_rag.py`), 
        # it usually assigns the function to `self.llm_model_func`.
        # Let's assume `rag.llm_model_func` is accessible.
        
        rewritten = await rag.llm_model_func(prompt)
        return rewritten.strip()
    except Exception as e:
        # Fallback if something fails
        print(f"Rewrite failed: {e}")
        return current_query


async def create_rag_instance():
    """Create a fresh RAG instance."""
    from raganything import RAGAnything, RAGAnythingConfig
    from lightrag.llm.openai import openai_complete_if_cache, openai_embed
    from lightrag.utils import EmbeddingFunc
    from qdrant_config import get_lightrag_kwargs

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
    lightrag_kwargs = get_lightrag_kwargs(verbose=False)
    
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
            func=embedding_func
        ),
        lightrag_kwargs=lightrag_kwargs
    )

    # Ensure LightRAG is initialized (loads graphs/vdb)
    await rag._ensure_lightrag_initialized()

    return rag
