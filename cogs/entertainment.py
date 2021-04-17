import discord, os, random
from discord.ext import commands
class Entertainment(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Sebas Entertainment is Ready.')        

    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = [   "As I see it, yes",
                        "It is certain",
                        "It is decidedly so",
                        "Most likely",
                        "Outlook good",
                        "Signs point to yes",
                        "Without a doubt",
                        "Yes",
                        "Yes - definitely",
                        "You may rely on it",
                        "Reply hazy, try again",
                        "Ask again later",
                        "Better not tell you now",
                        "Cannot predict now",
                        "Concentrate and ask again",
                        "Don't count on it",
                        "My reply is no",
                        "My sources say no",
                        "Outlook not so good",
                        "Very doubtful"]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')    

def setup(client):
    client.add_cog(Entertainment(client))