import discord
from bot_token import token
from discord.ext import commands

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '*', intents = intents)

@client.event
async def on_ready():
    print('Sebas is ready.')

@client.event
async def on_message(message):
    print('test')

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

client.run(token)


