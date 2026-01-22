
from typing import Optional
import chainlit as cl
import os
import sys
import asyncio
from dotenv import load_dotenv
import numpy as np
from chainlit.data.sql_alchemy import SQLAlchemyDataLayer

# Add project root to path so we can import src.*
from pathlib import Path
root_dir = Path(__file__).parent.parent.parent
if str(root_dir) not in sys.path:
    sys.path.append(str(root_dir))

# Load environment variables
load_dotenv()

# Ensure Qdrant env var
if not os.getenv("QDRANT_URL"):
    os.environ["QDRANT_URL"] = "http://localhost:6333"

@cl.data_layer
def get_data_layer():
    # chainlit.db is now in the same directory as app.py
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
        rag = await create_rag_instance_wrapper()
        
        # Store in user session
        cl.user_session.set("rag", rag)
        cl.user_session.set("history", []) # Initialize chat history
        
        # 4. Ready!
        msg.content = "**RAG System Ready!** 🚀\n\nAsk me anything about the podcasts. Example: *'What is a curiosity loop?'*"
        await msg.update()
        
    except Exception as e:
        msg.content = f"❌ **Initialization Failed**\nError: {str(e)}\n\nMake sure Qdrant is running (`scripts/qdrant/start_qdrant.sh`)"
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
            
            max_history_messages = int(os.getenv("MAX_HISTORY_MESSAGES", "10"))
            
            if len(history) > max_history_messages:
                history = history[-max_history_messages:]
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
    
    # 1. Access Mode (default hybrid)
    max_truncation = int(os.getenv("MAX_CONTENT_TRUNCATION_LENGTH", "200"))
    
    # Construct a simple history string or list for the prompt
    history_str = ""
    for msg in history:
        role = "User" if msg["role"] == "user" else "Assistant"
        content = msg["content"]
        # Truncate content slightly if too long to save tokens
        if len(content) > max_truncation:
            content = content[:max_truncation] + "..."
        history_str += f"{role}: {content}\n"
        
    prompt = f"""Given the following conversation history and a new user question, rewrite the user's question to be a standalone query that captures all necessary context. 
If the question is already standalone, return it exactly as is.
DO NOT answer the question. JUST rewrite it.

Chat History:
{history_str}

User's New Question: {current_query}

Standalone Query:"""

    try:
        # The RAG instance's llm_model_func is used to rewrite the query.
        rewritten = await rag.llm_model_func(prompt)
        return rewritten.strip()
    except Exception as e:
        # Fallback if something fails
        print(f"Rewrite failed: {e}")
        return current_query


async def create_rag_instance_wrapper():
    """Wrapper to initialize RAG from the common engine."""
    from src.core.engine import create_rag_instance
    
    # Use path relative to project root
    working_dir = os.path.join(root_dir, "storage/rag")
    return await create_rag_instance(working_dir=working_dir)
