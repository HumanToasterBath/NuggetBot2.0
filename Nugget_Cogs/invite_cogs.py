from discord.ext import commands
import aiohttp
import discord


class Invite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):
    	em = discord.Embed(title="https://discord.com/api/oauth2/authorize?client_id=668988124566781984&permissions=8&scope=bot")
    	await ctx.send(embed = em, content=None)



def setup(bot):
    bot.add_cog(Invite(bot))