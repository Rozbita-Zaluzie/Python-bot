#import kni-hoven or what
import discord
import datetime
from discord.ext import commands, tasks
from discord import message, guild, Guild, channel
import random
import os
from os import system
from discord.utils import get
import time

intents = discord.Intents.all()
client = commands.Bot(command_prefix = '.', intents=intents)


@commands.has_permissions(view_channel = True)

#@client.event
#async def on_ready():


#on_ready
@client.event
async def on_ready():
    print("jsem připravenej ti ojet mámu debile")

#! .find
@client.command()
async def find(ctx):


    channel = client.get_channel(775322766814740512)

    print(channel.name)

    category = channel.category
    channels = category.channels
    for x in channels:
        await ctx.send(x)


#! .join
@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

   
#! .leave
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()


#! .members
@client.command()
async def members(ctx):
    await ctx.send(f"{ctx.guild.member_count} members.")
    for x in ctx.guild.members:
        await ctx.send(x)

#* .howareu
@client.command()
@commands.has_any_role("Majitel", "Admin")
async def howareu(ctx):
    await ctx.send("Mám se fajne", "Jde to", "Bylo líp", "mega fajn!", "ja neviem už :D")


tokenF = open("token.txt", "r")
token = tokenF.readline()
client.run(token)