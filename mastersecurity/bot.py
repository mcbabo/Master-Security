import os
import discord
from discord.ext import commands
from discord.commands import slash_command
import random

client = discord.Bot()

@client.event
async def on_ready():
  print("Bot is Online")

#ping (working)
@client.slash_command(guild_ids = [878339997034504252])
async def ping(ctx):
  await ctx.respond(f"**Pong** { round (client.latency * 1000)}ms")

#purge(working)
@client.slash_command(guild_ids = [878339997034504252])
@commands.has_permissions(manage_messages = True)
async def purge(ctx,*,amount:int):
  channel = ctx.channel
  number = len(await channel.purge(limit = amount + 1)) # deletes desired amt of msgs + cmd
  embed = discord.Embed(title="Purge Successful", color= discord.color.random())

  if number == 1:
    embed.add_field(name="", value=f"{ctx.author.mention} has deleted {number} messages")
    await ctx.respond(f"{number} messages was purged by {ctx.author.mention}",delete_after = 3)
  else:
    embed.add_field(name="Clean-Up:", value=f"{ctx.author.mention} has deleted {amount} messages")
    await ctx.respond(f"{number} messages were purged by {ctx.author.mention}")

client.run(os.getenv('token'))
