from discord.ext import commands
import aiohttp
import discord


class search(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
##############################
#########DICTIONARY###########
##############################
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

        embed = discord.Embed()
        embed.title = f"Definition of {term}"
        embed.add_field(name="Definition", value=data[key][0]['definition'])
        try:
            embed.add_field(name="Example", value=data[key][0]['example'])
        except KeyError:
            pass
        try:
            embed.add_field(name="Synonyms", value=data[key][0]['synonyms'])
        except KeyError:
            pass
        await ctx.send(embed=embed)

##############################
#########WIKIPEDIA###########
##############################

    @commands.Cog.listener()
    async def on_ready():
        time = datetime.datetime.now()
        print("Wiki Search online at {}".format(time))

    def wiki_summary(arg):
        definition = wikipedia.summary(arg, sentences=3, chars=1000,
                                      auto_suggest=True, redirect=True)
        return definition

    @commands.Cog.listener()
    async def on_message(message):
        words = message.content.split()
        important_words = words[1:]

        if message.content.startswith('-wiki'):
            words = message.content.split()
            important_words = words[1:]
            search = discord.Embed(title="Searching...", description=wiki_summary(important_words), color=discord.Colour.purple())
            await message.channel.send(content=None, embed=search)

def setup(bot):
    bot.add_cog(search(bot))