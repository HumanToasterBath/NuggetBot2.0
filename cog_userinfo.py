import discord
from discord.ext import commands
import datetime

client = commands.Bot(command_prefix = '-')

@client.event
async def on_ready():
    time = datetime.datetime.now()
    print("User info online at {}".format(time))

client.remove_command("help")

@client.command()
async def user(ctx, member: discord.Member):
        roles = [role for role in member.roles]

        embed = discord.Embed(color=member.color, timestamp=datetime.datetime.utcnow())

        embed.set_author(name=f"{member}", icon_url=member.avatar_url)

        embed.set_image(url=member.avatar_url)

        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))

        embed.add_field(name="ID:", value=member.id)

        embed.add_field(name="Guild Name:", value=member.display_name)

        embed.add_field(name="Top role:", value=member.top_role.mention)

        embed.add_field(name="Bot?", value=member.bot)
        embed.set_footer(text=f"Requested By: {ctx.author.name}")

        await ctx.send(embed=embed)

client.run("NjY4OTg4MTI0NTY2NzgxOTg0.XiZRvg.CKej4DECCsw92EHN9pKsDHZwjgk")

        

 
