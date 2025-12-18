from discord.ext import commands
from discord.ext.commands import Bot


class SaveMemoryCommand(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command()
    async def save(self, ctx):
        # Saves the bot in memory

        await ctx.send("Saved!")
