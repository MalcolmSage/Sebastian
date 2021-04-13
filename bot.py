import discord
from bot_token import token
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('You called?')

client.run(token)


