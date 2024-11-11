import os
import discord
from discord.ext import commands
from discord.ext import tasks
from discord.ext.commands import Bot
from dotenv import load_dotenv

import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_ID')
CHANNEL = os.getenv('CHANNEL_ID')

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='g!', intents=intents)

@tasks.loop(minutes=15)
async def auto_send(channel : discord.TextChannel):
    await channel.send('george costanza')

@client.event
async def on_ready():

    if not auto_send.is_running():
        channel = await client.fetch_channel(CHANNEL)
        auto_send.start(channel)

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} has successfully connected to the following guild(s):\n'
        f'{guild.name}(id: {guild.id})'
    )

    await client.change_presence(
        activity=discord.Activity(name='baseball', type=discord.ActivityType.playing)
    )

@client.command()
async def quote(ctx):
    filename1=open('costanza.txt')
    wordList1=[line.rstrip('\n') for line in filename1]
    filename1.close()
    out1 = random.choice(wordList1)
    await ctx.send(f"{out1}")

client.run(TOKEN)
