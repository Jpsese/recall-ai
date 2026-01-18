from datetime import datetime

from sentence_transformers import SentenceTransformer

from recall_ai.ai.memory.models import Embedding


class EmbeddingService:
    def __init__(self, model_name="all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.model = SentenceTransformer(model_name)

    """
        This functions converts the text in to a vector
    """

    def embed(self, text: str) -> Embedding:
        embeddings = self.model.encode(text)
        dimension = embeddings.shape[0]
        vector = embeddings.tolist()
        created_at = datetime.now()

        return Embedding(
            vector=vector,
            dimension=dimension,
            created_at=created_at,
            model_name=self.model_name,
        )
