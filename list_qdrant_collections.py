
from qdrant_config import get_qdrant_client

client = get_qdrant_client()
if client:
    collections = client.get_collections()
    print("Qdrant Collections:")
    for col in collections.collections:
        print(f"- {col.name}")
else:
    print("Could not connect to Qdrant")
