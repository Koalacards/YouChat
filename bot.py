import discord
from discord.ext import commands
from discord_slash import SlashCommand
from confidential import RUN_ID
from vars import guild_ids

client = commands.Bot(".")
slash = SlashCommand(client, sync_commands=True, override_type=True, sync_on_cog_reload=True)

client.load_extension('cogs.setupcommands')

@client.event
async def on_ready():
    print("ready")

@slash.slash(name='reloadCog', guild_ids=guild_ids)
async def reloadCog(ctx, cog):
    if ctx.author.display_name == 'Koalacards':
        client.reload_extension(cog)
        await ctx.send("Cog has been reloaded")
    else:
        await ctx.send("You are not my creator")

client.run(RUN_ID)