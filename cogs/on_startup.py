import discord
from discord.ext import commands
import os
import asyncio

OWNER_ID = int(os.environ['DISCORD_OWNER_ID'])

class SyncCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged on as "{self.bot.user}"')
        await self.bot.tree.sync()
        await asyncio.sleep(2)
        await self.bot.change_presence(activity=None, status=discord.Status.dnd)

async def setup(bot):
    await bot.add_cog(SyncCog(bot))
