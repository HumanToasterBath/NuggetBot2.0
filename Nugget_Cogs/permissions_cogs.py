from discord.ext import commands
import aiohttp
import discord

owner_id = 373970357498937385
zach_id = 561358345097969684
james_id = 343219159598891021

class Permissions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    

    @commands.command()
    async def upgradeperms(self, ctx, user: discord.User):
        try:
            if user.id == owner_id or user.id == zach_id or user.id == james_id:
                em = discord.Embed(description = f"{user} already has super user permissions", color=ctx.author.color)
                em.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)

                await ctx.send(embed=em, content=None)

            else:

                
                super_user = user.id

                em = discord.Embed(description = f"{ctx.author} has given {user} super user permissions", color=ctx.author.color)
                em.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)

                await ctx.send(embed=em, content=None)

        except Exception as e:
            await ctx.send(f"Error: {str(e)}")




    @commands.command()
    async def checkperms(self, ctx, user: discord.User):
        try:
            if user.id == owner_id or user.id == zach_id or user.id:
                em = discord.Embed(title=f"{user} has `owner` permissions", color=ctx.author.color)

                em.set_footer(text="if you believe this is a mistake, please contact SON. YOU DROPPED THE NUGGIES#0141 via pm.", icon_url="https://cdn.discordapp.com/avatars/668988124566781984/5a0927708295e1190e2c1b7df70ebeea.webp?size=128")

                await ctx.send(embed = em, content=None)

            else:
                em1 = discord.Embed(title=f"{user} has `standard user` permissions", color=ctx.author.color)

                em1.set_footer(text="if you believe this is a mistake, please contact SON. YOU DROPPED THE NUGGIES#0141 via pm.", icon_url="https://cdn.discordapp.com/avatars/668988124566781984/5a0927708295e1190e2c1b7df70ebeea.webp?size=128")

                await ctx.send(embed = em1, content=None)

        except Exception as e:
            await ctx.send(f"Error: {str(e)}")




def setup(bot):
    bot.add_cog(Permissions(bot))
