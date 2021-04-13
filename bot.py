import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print('You called?')

client.run('ODMxNTg4NDI2NjM2OTg0MzMx.YHXbEw.KP3qw-KCEXWC7330Wa6acergJgc')


