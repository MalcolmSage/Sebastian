import discord, os, dotenv, random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('token')

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '*', intents = intents)

@client.event
async def on_ready():
    print('Sebas is ready.')

# Cog setup
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    await ctx.send(f'I will be providing my {extension} skills.')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'I shall refrain from using my {extension} skills.')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(token)


