import discord, os, random
from discord.ext import commands

class Services(commands.Cog):
    def __init__(self, client):
        self.client = client


    # Events

    # Commands

def setup(client):
    client.add_cog(Services(client))