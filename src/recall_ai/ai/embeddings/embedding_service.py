from pydantic import BaseModel
from sentence_transformers import SentenceTransformer


class EmbeddingModel(BaseModel):
    text: str


class EmbeddingService:
    pass
