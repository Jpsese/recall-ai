from discord.ext import commands
from discord.ext.commands import Bot
import time

START_TIME = time.time()


class Basic(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Recall-AI is working!")

    @commands.command()
    async def status(self, ctx):
        uptime = int(time.time() - START_TIME)
        await ctx.send(f"Uptime: {uptime}s")


async def setup(bot: Bot):
    await bot.add_cog(Basic(bot))
