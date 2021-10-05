import discord
import datetime
from discord.ext import commands, tasks
from discord import message, guild, Guild
import random
import os
from os import system
import htmlParser as parser
from discord.utils import get
import time


intents = discord.Intents(messages = True, guilds = True, members = True)
client = commands.Bot(command_prefix = '.', intents=intents)

#! on ready
@client.event
async def on_ready():
    activity = discord.Activity(name='SERVER', type=discord.ActivityType.watching)
    await client.change_presence(activity=activity)
    os.system("cls")
    for x in client.guilds:
        print(f"\033[1;32;40m[loged] \033[1;37;40m- {x.name}")
    ms = round(client.latency * 1000)
    print(f"\033[1;32;40m[loged] \033[1;37;40m- {ms}ms")
    print()
    parser.on_ready(client.guilds, ms)

#! on_command_error
@client.event
async def on_command_error(ctx, error):
    print(f"\033[1;31;40m[error] \033[1;34;40m- command \033[1;37;40m- {ctx.message.content}")
    print(f"\033[1;31;40m[error] \033[1;34;40m- channel \033[1;37;40m- {ctx.channel}")
    print(f"\033[1;31;40m[error] \033[1;34;40m- error \033[1;37;40m- {error}\n")
    parser.on_command_error(ctx.guild.id, ctx.message.content, ctx.channel.name, error)

#! on member join
@client.event
async def on_member_join(member):
    print(f"\033[1;32;40m[join] \033[1;34;40m- member \033[1;37;40m- {member.name}\n")
    parser.on_member_join(member.guild.id, member.name)

#! on member remove 
@client.event
async def on_member_remove(member):
    print(f"\033[1;31;40m[leave] \033[1;34;40m- member \033[1;37;40m- {member.name}\n")
    parser.on_member_join(member.guild.id, member.name)

#! .delete
@client.command()
@commands.has_any_role("Majitel", "Admin")
async def delete(ctx, x=2):
    channel = ctx.channel
    if x == 0:
        messages = await channel.history().flatten()
    else:
        messages = await channel.history(limit=x).flatten()

    for message in messages:
        await message.delete()

    if x == 0:
        print(f"\033[1;31;40m[delete] \033[1;34;40m- channel \033[1;37;40m- {channel.name}")
        print(f"\033[1;31;40m[delete] \033[1;34;40m- messages \033[1;37;40m- all\n")
        parser.delete(ctx.guild.id, channel.name, "all")
    else:
        print(f"\033[1;31;40m[delete] \033[1;34;40m- channel \033[1;37;40m- {channel.name}")
        print(f"\033[1;31;40m[delete] \033[1;34;40m- messages \033[1;37;40m- {x}\n")
        parser.delete(ctx.guild.id, channel.name, x)

#! .delete_member
@client.command()
@commands.has_any_role("Majitel", "Admin")
async def delete_member(ctx, member : discord.Member):
    channel = ctx.channel
    number = 0

    messages2 = await channel.history(limit=1).flatten()
    for message in messages2:
        await message.delete()

    messages = await channel.history().flatten()
    for message in messages:
        if message.author == member:
            await message.delete()
            number += 1

    print(f"\033[1;31;40m[delete] \033[1;34;40m- channel \033[1;37;40m- {channel.name}")
    print(f"\033[1;31;40m[delete] \033[1;34;40m- member \033[1;37;40m- {member.name}")
    print(f"\033[1;31;40m[delete] \033[1;34;40m- messages \033[1;37;40m- {number}\n")
    parser.delete_member(ctx.guild.id, channel.name, member.name, number)

#! .credits
@client.command()
async def credits(ctx):
    await ctx.send("``` Made by - Rozbita_Zaluzie ```")
    await ctx.send("https://www.instagram.com/rozbita_zaluzie/")
    write(ctx.guild.id, "credits")


#* .pilot
@client.command()
async def pilot(ctx):
    responses = ["I will be Pilot and destroy India!!!"]
    await ctx.send(f'{random.choice(responses)}')
    write(ctx.guild.id, "pilot")

#* .pele
@client.command()
async def pele(ctx):
    leng = ['mm','cm','m']
    x = random.randint(0,100)
    xx = random.choice(leng)
    if x % 11 == 0:
        await ctx.send('404 - Tvoje pelko not found')
    elif x % 15 == 0:
        await ctx.send('you mother small')
    else:
        await ctx.send(f'Tvoje pelko má {x} {xx}')
    write(ctx.guild.id, "pele")

#* .anone
@client.command()
async def anone(ctx, *, question):
    responses = ["Samozřejmě", "Ano", "Možná", "Ne", "Ani náhodou :|"]
    await ctx.send(f'Otázka: {question}\nOdpověd: {random.choice(responses)}')
    write(ctx.guild.id, "anone")
    
#* .jakoty
@client.command()
async def jakoty(ctx):
    responses = ["Maximálně ty", "Maska jaska", "Jaska fiska", "Míla íla","you mother small" , "knedl :|", "Minimálně ty", "Průměrně ty", "Jako já"]
    await ctx.send(f'{random.choice(responses)}')
    write(ctx.guild.id, "jakoty")

#* .kralik
@client.command()
async def kralik(ctx):
    responses = ["Měl by si ho nakrmit", "Ty prasa zoofilské", "Ferda :D", "Celkem fešný bobek"]
    await ctx.send(f'{random.choice(responses)}')
    write(ctx.guild.id, "kralik")

#* .didorici
@client.command()
@commands.has_any_role("Majitel", "Admin")
async def didorici(ctx):
    await ctx.send("Omlouvám se mistře, tato chyba se už nebude opakovat")
    write(ctx.guild.id, "didorici")

#! .trello
@client.command()
async def trello(ctx):
    await ctx.send("Tello - ")
    write(ctx.guild.id, "trello")

#! .join
@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    write(ctx.guild.id, "join")
   
#! .leave
@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    write(ctx.guild.id, "leave")

#! .members
@client.command()
async def members(ctx):
    await ctx.send(f"{ctx.guild.member_count} members.")
    for x in ctx.guild.members:
        print(x)
    majit = "👑"
    adm = "⚙️"
    mmr = "😂"
    bot = "🤖"
    dj = "🎵"
    hrc = "🎮"
    gay = "🏳️‍🌈"
    tstr = "🧪"
    evr = "⚪️"
    i = 1
    roleW = ""
    for x in ctx.guild.members:
        role = x.top_role.name
        if role == "Majitel":
            roleW = majit
            await ctx.send(f"`{i}. - {roleW} {x.name}`")
            i += 1
    for x in ctx.guild.members:
        role = x.top_role.name
        if role == "Admin":
            roleW = adm
            await ctx.send(f"`{i}. - {roleW} {x.name}`")
            i += 1
    for x in ctx.guild.members:
        role = x.top_role.name
        if role == "Memer":
            roleW = mmr
            await ctx.send(f"`{i}. - {roleW} {x.name}`")
            i += 1
    for x in ctx.guild.members:
        role = x.top_role.name
        if role == "DJ":
            roleW = dj
            await ctx.send(f"`{i}. - {roleW} {x.name}`")
            i += 1
    for x in ctx.guild.members:
        role = x.top_role.name
        if role == "BOT":
            roleW = bot
            await ctx.send(f"`{i}. - {roleW} {x.name}`")
            i += 1
    for x in ctx.guild.members:
        role = x.top_role.name
        if role == "Hráč":
            roleW = hrc
            await ctx.send(f"`{i}. - {roleW} {x.name}`")
            i += 1
    for x in ctx.guild.members:
        role = x.top_role.name
        if role == "GEJ":
            roleW = gay
            await ctx.send(f"`{i}. - {roleW} {x.name}`")
            i += 1
    for x in ctx.guild.members:
        role = x.top_role.name
        if role == "Tester":
            roleW = tstr
            await ctx.send(f"`{i}. - {roleW} {x.name}`")
            i += 1
    for x in ctx.guild.members:
        role = x.top_role.name
        if role == "@everyone":
            roleW = evr
            await ctx.send(f"`{i}. - {roleW} {x.name}`")
            i += 1

    write(ctx.guild.id, "members")

#* .facka
@client.command()
async def facka(ctx):
    lis = []
    
    for x in ctx.guild.members:
        lis.append(x)
        if x.top_role.name != "BOT" and x.name != ctx.author.name:
            lis.append(x)
    
    r = random.choice(lis)
    if r == ctx.author:
        await ctx.send(f"{r.mention} si dal facku... (proč se mlátíš ty buzno ??)")
    else: 
        odpovedi = [" dostal facku od "," dostal granáta od "," byl proplesknut "]
        slovo = random.choice(odpovedi)

        await ctx.send(f"{r.mention}{slovo}{ctx.author.mention}")
    write(ctx.guild.id, "facka")

#* .lock
@client.command()
@commands.has_any_role("Majitel", "Admin")
async def lock(ctx, member : discord.Member, channel : discord.VoiceChannel, channel2 : discord.VoiceChannel, x=14):
    print(f"\033[1;31;40m[locker] \033[1;34;40m- member \033[1;37;40m- {member.name}")
    print(f"\033[1;31;40m[locker] \033[1;34;40m- channel 1 \033[1;37;40m- {channel.name}")
    print(f"\033[1;31;40m[locker] \033[1;34;40m- channel 2 \033[1;37;40m- {channel2.name}")
    print(f"\033[1;31;40m[locker] \033[1;34;40m- time \033[1;37;40m- {x}")
    if x < 14:
        x = 14
    x = (x / float(14)) * 10
    i = 1
    while i <= x:
        try:
            await member.move_to(channel)
        except:
            pass
        try:
            await member.move_to(channel2)
        except:
            pass
        i+=1
        time.sleep(0.1)
    print(f"\033[1;32;40m[locker] \033[1;34;40m- unlocked \033[1;37;40m- {member.name}\n")
    parser.locker(ctx.guild.id, member.name, channel.name, channel2.name, x)

#* .meme
@client.command()
async def meme(ctx):
    imgs = []
    with os.scandir('memes/') as memes:
        for image in memes:
            imgs.append(image) 
    meme = random.choice(imgs)
    memeC = "memes\\" + str(meme.name) 
    await ctx.channel.send(file=discord.File(memeC))
    write(ctx.guild.id, "meme")

#// write stats
def write(guild, commandN):
    print(f"\033[1;33;40m[added] \033[1;37;40m- {commandN}\n")
    fileR = open("stats.txt", "r")
    stats = []
    for x in fileR:
        if x.startswith(commandN):
            st = x.split(" - ")
            i = int(st[1])
            i+=1
            x = st[0] + " - " + str(i) + "\n"
        stats.append(x)
    with open('stats.txt', 'w') as file2:
        file2.writelines( stats )    
    parser.added(guild, commandN)
    
tokenF = open("token.txt", "r")
token = tokenF.readline()
client.run(token)
