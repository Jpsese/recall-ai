"""
Global application context.
Follows the Application Context pattern used in frameworks like Flask, FastAPI.
"""

from typing import Optional

from recall_ai.services import AppServices


class ApplicationContext:
    """
    Global application context.
    Initialized once at startup, accessible throughout the app.
    """

    _instance: Optional["ApplicationContext"] = None

    def __init__(self):
        if ApplicationContext._instance is not None:
            raise RuntimeError("ApplicationContext already exists. Use get_context()")
        self.services: Optional[AppServices] = None
        ApplicationContext._instance = self

    @classmethod
    def get_context(cls) -> "ApplicationContext":
        """Get the global application context."""
        if cls._instance is None:
            raise RuntimeError("Application not initialized")
        return cls._instance

    def initialize(self, config: dict | None = None):
        """Initialize the application context."""
        self.services = AppServices()
        self.services.initialize(config)


# Convenience function
def get_services() -> AppServices:
    """Get the application services."""
    ctx = ApplicationContext.get_context()
    if ctx.services is None:
        raise RuntimeError("Services not initialized")
    return ctx.services
