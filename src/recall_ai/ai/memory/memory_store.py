import uuid
from typing import Optional

from pydantic import BaseModel
from sentence_transformers import util

from recall_ai.ai.memory.models import Embedding, Memory


class MemoryLookup(BaseModel):
    score: float
    memory: Memory


class MemoryStore:
    def __init__(self, min_score=0.5, limit=5):
        self.memory_list: list[Memory] = []
        self.min_score = min_score
        self.limit = limit

    def store(
        self, content: str, author: str, source: Optional[str], embedding: Embedding
    ) -> Memory:
        id = str(uuid.uuid4())

        memory = Memory(
            id=id,
            author=author,
            content=content,
            source=source,
            embedding=embedding,
        )

        self.memory_list.append(memory)
        return memory

    def search(self, query_embedding: Embedding) -> list[MemoryLookup]:
        memory_lookups: list[MemoryLookup] = []
        query_vector = query_embedding.vector
        for memory in self.memory_list:
            memory_vector = memory.embedding.vector
            score = util.cos_sim([query_vector], [memory_vector])
            print(f"whats the score {score}")
            if score >= self.min_score:
                memory_lookups.append(MemoryLookup(score=score, memory=memory))

        memory_lookups.sort(key=lambda memory: memory.score, reverse=True)
        return memory_lookups[: self.limit]
