import discord, os, random
from discord.ext import commands

class Services(commands.Cog):
    def __init__(self, client):
        self.client = client


    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for your requests"))
        print('Sebas is Ready.')    
    # Commands

def setup(client):
    client.add_cog(Services(client))