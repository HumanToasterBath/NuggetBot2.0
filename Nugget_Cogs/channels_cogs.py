from discord.ext import commands
import aiohttp
import discord
from discord.ext.commands import CommandOnCooldown

class ticket(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ticket(self, ctx):
        try:
            await ctx.guild.create_text_channel('ticket')
            em = discord.Embed(title="Ticket created in #ticket", color=discord.Color.dark_gold())
            await ctx.send(embed=em, content=None)
        except Exception as e:
            await ctx.send(f"Error: {str(e)}")

    @commands.command()
    @commands.has_permissions(manage_channels = True)
    async def createchannel(self, ctx, args):
        try:
            await ctx.guild.create_text_channel(args)
            em = discord.Embed(title=f"Created channel #{args}", color=discord.Color.dark_gold())
            await ctx.send(embed=em, content=None)
        except Exception as e:
            await ctx.send(f"Error: {str(e)}")

    @commands.command()
    async def close(self, ctx, channel: discord.TextChannel):
        try:
            await channel.delete()

        except Exception as e:
            await ctx.send(f"Error: {str(e)}")

def setup(bot):
    bot.add_cog(ticket(bot))
