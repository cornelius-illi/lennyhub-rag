
import asyncio
import aiosqlite
import os

from pathlib import Path
import sys

# Add project root to path
root_dir = Path(__file__).parent.parent.parent

async def init_db():
    default_db_path = root_dir / "apps/chat/chainlit.db"
    db_path = os.getenv("CHAINLIT_DB_PATH", str(default_db_path))
    print(f"Initializing database: {db_path}")

    async with aiosqlite.connect(db_path) as db:
        # Users table
        await db.execute("""
            CREATE TABLE IF NOT EXISTS users (
                "id" TEXT PRIMARY KEY,
                "identifier" TEXT NOT NULL UNIQUE,
                "createdAt" TEXT NOT NULL,
                "metadata" TEXT
            );
        """)

        # Threads table
        await db.execute("""
            CREATE TABLE IF NOT EXISTS threads (
                "id" TEXT PRIMARY KEY,
                "createdAt" TEXT,
                "name" TEXT,
                "userId" TEXT,
                "userIdentifier" TEXT,
                "tags" TEXT,
                "metadata" TEXT,
                FOREIGN KEY("userId") REFERENCES users("id")
            );
        """)

        # Steps table
        await db.execute("""
            CREATE TABLE IF NOT EXISTS steps (
                "id" TEXT PRIMARY KEY,
                "name" TEXT NOT NULL,
                "type" TEXT NOT NULL,
                "threadId" TEXT NOT NULL,
                "parentId" TEXT,
                "streaming" BOOLEAN,
                "waitForAnswer" BOOLEAN,
                "isError" BOOLEAN,
                "metadata" TEXT,
                "tags" TEXT,
                "input" TEXT,
                "output" TEXT,
                "createdAt" TEXT,
                "start" TEXT,
                "end" TEXT,
                "generation" TEXT,
                "showInput" TEXT,
                "language" TEXT,
                "indent" INTEGER,
                "defaultOpen" BOOLEAN,
                FOREIGN KEY("threadId") REFERENCES threads("id")
            );
        """)
        
        # Elements table
        await db.execute("""
            CREATE TABLE IF NOT EXISTS elements (
                "id" TEXT PRIMARY KEY,
                "threadId" TEXT,
                "type" TEXT,
                "url" TEXT,
                "chainlitKey" TEXT,
                "name" TEXT NOT NULL,
                "display" TEXT,
                "objectKey" TEXT,
                "size" TEXT,
                "page" INTEGER,
                "language" TEXT,
                "forId" TEXT,
                "mime" TEXT,
                "props" TEXT,
                "autoPlay" BOOLEAN,
                "playerConfig" TEXT,
                FOREIGN KEY("threadId") REFERENCES threads("id")
            );
        """)
        
        # Feedbacks table
        await db.execute("""
            CREATE TABLE IF NOT EXISTS feedbacks (
                "id" TEXT PRIMARY KEY,
                "forId" TEXT NOT NULL,
                "value" INTEGER NOT NULL,
                "comment" TEXT,
                FOREIGN KEY("forId") REFERENCES steps("id")
            );
        """)

        await db.commit()
    
    print("Database initialization complete.")

if __name__ == "__main__":
    asyncio.run(init_db())
