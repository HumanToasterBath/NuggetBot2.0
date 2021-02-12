import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot


async def info1(ctx):
    mbed = discord.Embed(
        colour=discord.Colour.purple(),
        title=f"{ctx.guild.name}"
    )
    mbed.set_image(url=f"{ctx.guild.icon_url}")
    mbed.add_field(name='Region', value=f"{ctx.guild.region}")
    mbed.add_field(name='Member Count', value=f"{ctx.guild.member_count}")
    mbed.add_field(name='Server created At', value=f"{ctx.guild.created_at}")
    mbed.add_field(name='Booster Count', value=f"{ctx.guild.premium_subscription_count}")
    mbed.add_field(name='Description', value=f"{ctx.guild.description}")
    mbed.add_field(name='Max emoji', value=f"{ctx.guild.emoji_limit}")
    mbed.set_footer(text=f"Command Executed by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=mbed)

