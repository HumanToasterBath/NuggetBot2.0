from discord.ext import commands
import aiohttp
import discord
from discord.ext.commands import CommandOnCooldown

class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def help(self, ctx):
        embed = discord.Embed(title="", value="", color=discord.Color.dark_gold())
        embed.add_field(name=':gear: General :gear: ', value="** **", inline=False)
        embed.add_field(name='Help', value='Shows this message', inline=True)
        embed.add_field(name='Ping', value='responds with client latency', inline=True)
        embed.add_field(name='Invite', value='Generates an invite link to add Nugget2.0 to your server', inline=True)
        embed.add_field(name='Serverinfo', value='Shows information on the current server as an embedded message', inline=True)
        embed.add_field(name='Whois', value='Shows information on specified user as an embedded message', inline=True)
        embed.add_field(name='Define', value='Searches wikipedia and provides a breif summary of the article', inline=True)
        embed.set_footer(text="⚙️ = General |  = Economy |  =  Moderation", icon_url="https://cdn.discordapp.com/avatars/668988124566781984/5a776620e9be5ebbfdf1a100f28c4162.webp?size=1024")
        message = await ctx.send(embed = embed, content=None)

        await message.add_reaction("⚙️")
        await message.add_reaction("💰")
        await message.add_reaction("🔏")
        await message.add_reaction("")

        @client.event
        async def on_reaction_add(reaction, user):
            if user != client.user:
                if reaction.emoji == ":moneybag:":
                    helpe = discord.Embed(title=":coin: Economy :coin:", value="** **", color=discord.Color.dark_gold())

                    helpe.add_field(name='Work', value='You work in a shitty retail chain for $16/hour', inline=True)
                    helpe.add_field(name='Beg', value="On the streets again are ya?", inline=True)
                    helpe.add_field(name='Balance', value='Check how much money you got. Dont wanna be going broke now do we?', inline=True)
                    helpe.add_field(name='Deposit', value='Deposit some money in your wallet to your bank account', inline=True)
                    helpe.add_field(name='Withdraw', value='Take some cash out of your bank account for spending', inline=True)
                    helpe.add_field(name='Slots', value='Its only illegal if you get caught :smirk:', inline=True)
                    helpe.add_field(name='Shop', value='Spend your money on stupid shit you dont need', inline=True)
                    helpe.add_field(name='Buy', value='Confirm your purchase in the shop', inline=True)
                    helpe.add_field(name='Bag', value='Your inventory or list of things you have bought', inline=True)
                    helpe.set_footer(text="⚙️ = General | = Economy |  =  Moderation", icon_url="https://cdn.discordapp.com/avatars/668988124566781984/5a776620e9be5ebbfdf1a100f28c4162.webp?size=1024")
                    await ctx.channel.purge(limit = 1)
                    message = await ctx.send(embed=helpe, content=None)

                    await message.add_reaction("⚙️")
                    await message.add_reaction("💰")
                    await message.add_reaction("🔏")
                    await message.add_reaction("")

                    if reaction.emoji == ":lock_with_ink_pen:":
                        #if user != client.user:
                            em = discord.Embed(title=":lock_with_ink_pen: Moderation :lock_with_ink_pen:", description="** **", color=discord.Color.dark_gold())
                            em.add_field(name='Clear', value='Cleans up unwanted messages', inline=True)
                            em.add_field(name='Kick', value='Temporarily kick a member out of the server', inline=True)
                            em.add_field(name='Ban', value='Temporarily ban a member from the server', inline=True)
                            em.add_field(name='checkperms', value='Check what permission level you have with the bot', inline=True)
                            em.add_field(name='Restart', value='Restart the bot client (owners only)', inline=True)
                            em.set_footer(text="⚙️ = General | = Economy |  =  Moderation ", icon_url="https://cdn.discordapp.com/avatars/668988124566781984/5a776620e9be5ebbfdf1a100f28c4162.webp?size=1024")

                            await ctx.channel.purge(limit = 1)

                            message = await ctx.send(embed = em, content=None)


                            await message.add_reaction("⚙️")
                            await message.add_reaction("💰")
                            await message.add_reaction("🔏")
                            await message.add_reaction("")


                            if reaction.emoji == "⚙️":
                                if user != client.user:
                                    embed = discord.Embed(title="", value="", color=discord.Color.dark_gold())

                                    embed.add_field(name=':gear: General :gear: ', value="** **", inline=False)

                                    embed.add_field(name='Help', value='Shows this message', inline=True)

                                    embed.add_field(name='Ping', value='responds with client latency', inline=True)

                                    embed.add_field(name='Invite', value='Generates an invite link to add Nugget2.0 to your server', inline=True)

                                    embed.add_field(name='Serverinfo', value='Shows information on the current server as an embedded message', inline=True)

                                    embed.add_field(name='Whois', value='Shows information on specified user as an embedded message', inline=True)

                                    embed.add_field(name='Define', value='Searches wikipedia and provides a breif summary of the article', inline=True)
                                        
                                    embed.set_footer(text="⚙️ = General |  = Economy |  =  Moderation", icon_url="https://cdn.discordapp.com/avatars/668988124566781984/5a776620e9be5ebbfdf1a100f28c4162.webp?size=1024")

                                    await ctx.channel.purge(limit = 1)

                                    message = await ctx.send(embed = embed, content=None)

                                    await message.add_reaction("⚙️")
                                    await message.add_reaction("💰")
                                    await message.add_reaction("🔏")
                                    await message.add_reaction("")

                                    if reaction.emoji == "":
                                        if user != client.user:
                                            embed = discord.Embed(title=" Server ", value="", color=discord.Color.dark_gold())
                                            embed.add_field(name='Ticket', value='Useful command that lets users create a ticket(text channel) to get help from admin in any server', inline=True)
                                            embed.add_field(name='Createchannel', value="Creates a new channel(text channel) ", inline=True)
                                            embed.add_field(name='Close', value="Deletes a channel(text channel) ", inline=True)
                                            embed.set_footer(text="⚙️ = General |  = Economy |  =  Moderation", icon_url="https://cdn.discordapp.com/avatars/668988124566781984/5a776620e9be5ebbfdf1a100f28c4162.webp?size=1024")
                                            await ctx.channel.purge(limit = 1)
                                            message = await ctx.send(embed = embed, content=None)

                                            await message.add_reaction("⚙️")
                                            await message.add_reaction("💰")
                                            await message.add_reaction("🔏")
                                            await message.add_reaction("")
def setup(bot):
    bot.add_cog(help(bot))
