
from raganything import RAGAnything
import inspect

try:
    sig = inspect.signature(RAGAnything.aquery)
    print(f"aquery Signature: {sig}")
    
    # Also check if there is a 'query' method
    if hasattr(RAGAnything, 'query'):
        sig_q = inspect.signature(RAGAnything.query)
        print(f"query Signature: {sig_q}")
except Exception as e:
    print(f"Error getting signature: {e}")

# Check docstring
print("\nDocstring for aquery:")
print(RAGAnything.aquery.__doc__)
