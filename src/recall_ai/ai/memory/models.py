from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Embedding(BaseModel):
    vector: list[float]
    dimention: int
    model_name: str
    created_at: datetime


class Memory(BaseModel):
    id: str
    content: str
    embedding: Embedding
    timestamp: datetime
    author: str
    source: Optional[str]
