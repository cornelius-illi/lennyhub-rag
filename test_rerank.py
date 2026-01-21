
import asyncio
from fastembed.rerank.cross_encoder import TextCrossEncoder

async def test_rerank():
    print("Initializing reranker...")
    model = TextCrossEncoder(model_name="jinaai/jina-reranker-v1-turbo-en")
    
    query = "What is the best way to grow a product?"
    documents = [
        "Product growth is best achieved through a combination of SEO and content marketing.",
        "The best way to grow a product is to build something people want and use a curiosity loop.",
        "Today is a sunny day in San Francisco.",
        "I like eating pizza with pineapples."
    ]
    
    print(f"Query: {query}")
    print("Reranking...")
    
    results = list(model.rerank(query, documents))
    
    print("\nResults:")
    for i, score in enumerate(results):
        print(f"Score: {score:.4f} | Index: {i} | Content: {documents[i][:50]}...")

if __name__ == "__main__":
    asyncio.run(test_rerank())
