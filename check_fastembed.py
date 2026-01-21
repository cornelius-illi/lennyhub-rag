
import sys

try:
    import fastembed
    print(f"fastembed version: {fastembed.__version__}")
except ImportError:
    print("fastembed not installed")

try:
    from fastembed.embedding import ImageEmbedding
    print("Import from fastembed.embedding successful")
except ImportError as e:
    print(f"Import from fastembed.embedding failed: {e}")

try:
    from fastembed import ImageEmbedding
    print("Import from fastembed successful")
except ImportError as e:
    print(f"Import from fastembed failed: {e}")

try:
    from fastembed.vision import ImageEmbedding
    print("Import from fastembed.vision successful")
except ImportError as e:
    print(f"Import from fastembed.vision failed: {e}")
