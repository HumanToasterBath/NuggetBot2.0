from discord.ext import commands
import aiohttp
import discord


class GoogleDict(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def define(self, ctx, term: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://api.dictionaryapi.dev/api/v1/entries/en/{term}") as r:
                result = await r.json()
        try:
            data = result[0]['meaning']
            key = list(data.keys())[0]
        except KeyError:
            await ctx.send("> Unable to find word!")
            return

        embed = discord.Embed(title= f"definition of {term}", color=discord.Color.dark_gold())
        embed.add_field(name="Definition", value=data[key][0]['definition'])

        embed.add_field(name="Example", value=data[key][0]['example'])

        embed.add_field(name="Synonyms", value=data[key][0]['synonyms'])

        await ctx.send(embed=embed, content=None)


def setup(bot):
    bot.add_cog(GoogleDict(bot))