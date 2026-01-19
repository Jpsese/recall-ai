import asyncio
import os

from dotenv import load_dotenv

from recall_ai.bot.client import create_bot
from recall_ai.context import ApplicationContext
from recall_ai.logging_config import setup_logging

MODULES = ["recall_ai.bot.commands.basic", "recall_ai.bot.commands.save_memory"]


async def main():
    load_dotenv()
    setup_logging()

    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_TOKEN is not set")

    client = create_bot()

    app_context = ApplicationContext()
    app_context.initialize(
        config={
            "embedding_model": "all-mpnet-base-v2",
            "min_similarity_score": 0.7,
            "search_limit": 5,
        }
    )

    for module in MODULES:
        await client.load_extension(module)

    await client.start(token)


if __name__ == "__main__":
    asyncio.run(main())
