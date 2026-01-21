#!/bin/bash
#
# Run Chainlit App for LennyHub RAG
#

set -e

echo "========================================"
echo "LennyHub RAG Chainlit App"
echo "========================================"
echo ""

# Check if Qdrant is running
if curl -s http://localhost:6333/ > /dev/null 2>&1; then
    echo "✓ Qdrant is running"
else
    echo "⚠️  Qdrant is not running"
    echo ""
    echo "Would you like to start Qdrant? (y/n)"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        ./start_qdrant.sh
        echo ""
    else
        echo "You can start Qdrant later with: ./start_qdrant.sh"
        echo ""
    fi
fi


# Initialize SQLite database schema
if [ ! -f "chainlit.db" ]; then
    echo "Initializing database schema..."
    python init_db.py
else
    # Always run init_db in case of schema updates (idempotent)
    echo "Verifying database schema..."
    python init_db.py
fi

# Check if chainlit is installed
if ! command -v chainlit &> /dev/null; then
    echo "⚠️  Chainlit not found. Please install dependencies from requirements.txt:"
    echo "   pip install -r requirements.txt"
    exit 1
fi

echo "Starting Chainlit app..."
echo ""

# Run Chainlit
chainlit run chainlit_app.py -w
