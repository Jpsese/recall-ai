from recall_ai.ai.embeddings.embedding_service import EmbeddingService
from recall_ai.ai.memory.memory_store import MemoryStore


class AppServices:
    """
    Centralized service container for the application.

    All services are initialized once and shared across the app.
    This follows the Singleton pattern for service management.
    """

    def __init__(self):
        self.embedding_service: EmbeddingService | None = None
        self.memory_store: MemoryStore | None = None
        self._initialized = False

    def initialize(self, config: dict | None = None):
        """
        Iniatialize all services

        Args:
            config: Optional configuration
        """
        if self._initialized:
            raise RuntimeError("Services already initialized")

        config = config or {}

        model_name = config.get("embedding_model", "all-mpnet-base-v2")
        self.embedding_service = EmbeddingService(model_name=model_name)

        min_score = config.get("min_similarity_score", 0.7)
        limit = config.get("search_limit", 5)
        self.memory_store = MemoryStore(min_score=min_score, limit=limit)

        self._initialized = True

    def is_ready(self) -> bool:
        """Check if services are initialized and ready."""
        return self._initialized

    def assert_ready(self):
        """Raise error if services not initialized."""
        if not self._initialized:
            raise RuntimeError("Services not initialized. Call initialize() first.")
