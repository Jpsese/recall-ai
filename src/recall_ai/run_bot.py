import os
import asyncio

from dotenv import load_dotenv
from recall_ai.logging_config import setup_logging
from recall_ai.bot.client import create_bot

MODULES = ["recall_ai.bot.cogs.basic"]


async def main():
    load_dotenv()
    setup_logging()

    token = os.getenv("DISCORD_TOKEN")
    if not token:
        raise RuntimeError("DISCORD_TOKEN is not set")

    client = create_bot()

    for module in MODULES:
        await client.load_extension(module)

    await client.start(token)


if __name__ == "__main__":
    asyncio.run(main())
