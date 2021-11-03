import discord
from discord.ext import commands
from discord_slash import cog_ext

class SetupCommands(commands.cog):
    @cog_ext.cog_slash(name='set_channel', description='Set the channel that the chatbot will talk in! (When not in training mode)')
    async def set_channel(self, channel:discord.TextChannel):
        pass

def setup(bot):
    bot.add_cog(SetupCommands(bot))