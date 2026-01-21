
from fastembed.image import ImageEmbedding
import json

try:
    models = ImageEmbedding.list_supported_models()
    print(json.dumps(models, indent=2))
except Exception as e:
    print(f"Error listing models: {e}")
