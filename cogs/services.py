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
    @commands.command()
    async def on_member_join(self, member):
        print(f'{member} has joined a server')

    @commands.command()
    async def on_member_remove(self, member):
        print(f'{member} has left a server')

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount)

    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason = reason)
        await ctx.send(f'Kicked {member.mention}')

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason = reason)
        await ctx.send(f'Banned {member.mention}')

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'{user.mention} will be allowed back on the premises')
                return
def setup(client):
    client.add_cog(Services(client))