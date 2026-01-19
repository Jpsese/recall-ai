import logging

from discord.ext import commands
from discord.ext.commands import Bot

from recall_ai.context import get_services


class SaveMemoryCommand(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command()
    async def save(self, ctx):
        # Saves the bot in memory
        services = get_services()
        content = ctx.message.content.replace("!save ", "", 1)
        author = str(ctx.author.id)
        source = ctx.guild.name

        embedding = services.embedding_service.embed(content)
        services.memory_store.store(content, author, source, embedding)
        await ctx.send("Memory saved!")

    @commands.command()
    async def search(self, ctx):
        services = get_services()
        content = ctx.message.content.replace("!search ", "", 1)
        embedding = services.embedding_service.embed(content)

        memory_list = services.memory_store.search(embedding)
        if not memory_list:
            await ctx.send("🔍 No similar memories found.")
            return

        response = f"🧠 Found {len(memory_list)} similar memories:\n\n"
        for i, result in enumerate(memory_list, 1):
            response += f"{i}. **Score: {result.score:.2f}**\n"
            response += f"   {result.memory.content[:100]}...\n\n"

        await ctx.send(response)


async def setup(bot: Bot):
    await bot.add_cog(SaveMemoryCommand(bot))
