from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Embedding(BaseModel):
    vector: list[float]
    dimension: int
    model_name: str
    created_at: datetime = Field(default_factory=datetime.now)


class Memory(BaseModel):
    id: str
    content: str
    embedding: Embedding
    created_at: datetime = Field(default_factory=datetime.now)
    author: str
    source: Optional[str]
