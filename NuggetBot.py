import discord
from discord.ext import commands
from discord.ext.commands import CommandOnCooldown
import datetime
import pypokedex
import cog_serverinfo
import json
import os
import random
import time
import asyncio
from time import time
from gtts import gTTS
import requests
import praw

reddit = praw.Reddit(client_id = "Iv-8LqyF2ybpSw",
					client_secret = "icebXQlMkVPy6T6Lkt70mmgxxRWs6w",
					username = "zachpef",
					password = "1905358",
					user_agent = "nuggetbot")	



owner_id = 373970357498937385
zach_id = 561358345097969684
james_id = 343219159598891021

os.chdir("C:\\Users\\zpfla\\Documents\\OLD DELL PC\\code stuffs\\Nugget2")

TOKEN = ''

client = commands.Bot(command_prefix = "n-")

client.remove_command("help")



api_key = "93184e557fa03bd35d72e64e25004625"
base_url = "http://api.openweathermap.org/data/2.5/weather?"

cogs = ["dictionary_cogs", "permissions_cogs", "channels_cogs"]

for x in cogs:
    client.load_extension(f"Nugget_Cogs.{x}")

@client.event
async def on_ready():
    time = datetime.datetime.now()
    print("Online at {}".format(time))

    acts = client.guilds
    mem = 0

    print("\nServers:")
    for s in acts:
        print(str(s.name))
        
    if str(s.name) == "Discord Bot List":
        return

    for a in acts:
        mem += len(a.members)

    print("\nMembers:", mem)

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="-help || Version 2.4"))

    channel = client.get_channel(804756831071240192)

    embed = discord.Embed(title="**OI** I'm alive!", description="{}".format(time), color=discord.Colour.dark_gold())

    await channel.send(embed=embed, content=None)

@client.event
async def on_command_error(ctx, error):

	if isinstance(error, commands.CommandOnCooldown):
		m, s = divmod(error.retry_after, 60)
		h, m = divmod(m, 60)
		if int(h) is 0 and int(m) is 0:

			em = discord.Embed(description=f":watch: You must wait {int(s)} seconds before using this command again.", color=ctx.author.color)
			em.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
			await ctx.send(embed=em, content=None)


		elif int(h) is 0 and int(m) is not 0:
			em = discord.Embed(description=f":watch: You must wait {int(m)} minutes before using this command again.", color=ctx.author.color)
			em.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
			await ctx.send(embed=em, content=None)
		else:
			em = discord.Embed(description=f":watch: You must wait {int(h) * 2} hours and {int(m)} before using this command again.", color=ctx.author.color)
			em.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
			await ctx.send(embed=em, content=None)

@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, id="<790355292894134292>")
    await member.add_roles(role)


@client.command()
@commands.has_permissions(administrator=True, manage_roles=True)
async def reactrole(ctx, emoji, role: discord.Role, *, message):

    emb = discord.Embed(description=message)
    msg = await ctx.channel.send(embed=emb)
    await msg.add_reaction(emoji)

    with open('reactrole.json') as json_file:
        data = json.load(json_file)

        new_react_role = {'role_name': role.name, 
        'role_id': role.id,
        'emoji': emoji,
        'message_id': msg.id}

        data.append(new_react_role)

    with open('reactrole.json', 'w') as f:
        json.dump(data, f, indent=4)


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def restart(ctx):
	if ctx.author.id == owner_id or ctx.author.id == zach_id or ctx.author.id == james_id:
		embed = discord.Embed(title=":wave: Restarting....", value="", color=ctx.author.color)

		await ctx.send(embed=embed, content=None)

		channel = client.get_channel(804756831071240192)

		embed = discord.Embed(title="Restart at {}".format(datetime.datetime.now()), description="triggered by {}".format(ctx.author), color=discord.Colour.dark_gold())

		await channel.send(embed=embed)

		await client.logout()
	else:
		#pass
		embed = discord.Embed(title="You do not have permission to use this command.", value="", color=ctx.author.color)	

		await ctx.send(embed=embed, content=None)		


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def help(ctx):
	help = discord.Embed(title=':computer: All commands :computer:', description=None, colour=ctx.author.color)

	help.add_field(name=':gear: `General` :gear: ', value="** **", inline=False)

	help.add_field(name='Help', value='Shows this message', inline=True)

	help.add_field(name='Ping', value='responds with client latency', inline=True)

	help.add_field(name='Invite', value='Generates an invite link to add Nugget2.0 to your server', inline=True)

	help.add_field(name='Serverinfo', value='Shows information on the current server as an embedded message', inline=True)

	help.add_field(name='Whois', value='Shows information on specified user as an embedded message', inline=True)

	help.add_field(name='Define', value='Searches wikipedia and provides a breif summary of the article', inline=True)

	help.add_field(name=':coin: `Economy` :coin: ', value="** **", inline=False)

	help.add_field(name='Work', value='You work in a shitty retail chain for $16/hour', inline=True)

	help.add_field(name='Beg', value="On the streets again are ya?", inline=True)

	help.add_field(name='Balance', value='Check how much money you got. Dont wanna be going broke now do we?', inline=True)

	help.add_field(name='Deposit', value='Deposit some money in your wallet to your bank account', inline=True)

	help.add_field(name='Withdraw', value='Take some cash out of your bank account for spending', inline=True)

	help.add_field(name='Slots', value='Its only illegal if you get caught :smirk:', inline=True)

	help.add_field(name='Shop', value='Spend your money on stupid shit you dont need', inline=True)

	help.add_field(name='Buy', value='Confirm your purchase in the shop', inline=True)

	help.add_field(name='Bag', value='Your inventory or list of things you have bought', inline=True)

	help.add_field(name=':lock_with_ink_pen: `Moderation(admin)` :lock_with_ink_pen: ', value="** **", inline=False)

	help.add_field(name='Clear', value='Cleans up unwanted messages', inline=True)

	help.add_field(name='Kick', value='Temporarily kick a member out of the server', inline=True)

	help.add_field(name='Ban', value='Temporarily ban a member from the server', inline=True)

	help.add_field(name='checkperms', value='Check what permission level you have with the bot', inline=True)

	help.add_field(name='Restart', value='Restart the bot client (owners only)', inline=True)

	help.add_field(name=':mag: `Server` :mag: ', value="** **", inline=False)

	help.add_field(name='Ticket', value='Creates a text channel called Ticket. Use this channel to ask for help in from admin in your server.', inline=True)

	help.add_field(name='Ticketclose', value='Closes the open ticket and deletes the channel', inline=True)

	help.set_author(name = ctx.author.name, icon_url = ctx.author.avatar_url)



	help2 = discord.Embed(title=':musical_note: `Music` :musical_note:', description=None, colour=ctx.author.color)

	help2.add_field(name='Play', value='Searches all major streaming services and plays the specified song in vc', inline=True)

	help2.add_field(name='Pause', value='Pause the current song', inline=True)

	help2.add_field(name='Resume', value='Resume playback of the current song', inline=True)

	help2.add_field(name='Skip', value='Skip to the next song in the queue', inline=True)

	help2.add_field(name='Queue', value='List of songs to be played next', inline=True)

	help2.add_field(name='Summon', value="Joins the channel you're currently connected to", inline=True)

	help2.add_field(name='Disconnect', value="Leaves the channel the bot is connected to", inline=True)

	help2.add_field(name='clear', value='Clears all cache and resets the queue', inline=True)

	await ctx.author.send(embed=help, content=None)

	await ctx.author.send(embed=help2, content=None)

	await ctx.send(f"{ctx.author.mention} Check your dm's")


##GENERAL COMMANDS###

@client.command()
async def meme(ctx):
	subreddit = reddit.subreddit("dankmemes")
	all_subs = []

	top = subreddit.top(limit = 50)

	for submission in top:
		all_subs.append(submission)

	random_sub = random.choice(all_subs)

	name = random_sub.title
	url = random_sub.url

	em = discord.Embed(title = name, color=ctx.author.color)

	em.set_image(url = url)

	await ctx.send(embed=em)




@client.command()
async def porno(ctx):
	#subreddit = reddit.subreddit("nsfw")
	#all_subs = []

	#top = subreddit.top(limit = 100)

	#for submission in top:
		#all_subs.append(submission)

	#random_sub = random.choice(all_subs)

	#name = random_sub.title
	#url = random_sub.url

	#em = discord.Embed(title = name, color=ctx.author.color)

	#em.set_image(url = url)

	#await ctx.send(embed=em)	

	embed = discord.Embed(title="Lawl get a girl you sick fuck XD", color=discord.Colour.red())
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/790593036069371935/805807788861030410/ezgif-1-24d86df81078.gif")
	await ctx.send(embed=embed)

@client.command()
async def scree(ctx):
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")
	await ctx.send("sCrEeE")
	await ctx.send("ScReE")

@client.command()
async def kill(ctx):
	if ctx.author.id == owner_id or ctx.author.id == zach_id or ctx.author.id == james_id:
		await ctx.send(":pensive: :wave:")

		channel = client.get_channel(804756831071240192)

		embed = discord.Embed(title="Bot killed at {}".format(datetime.datetime.now()), description="triggered by {}".format(ctx.author), color=discord.Colour.dark_gold())

		await channel.send(embed=embed)

		await client.logout()

	else:
		#pass
		embed = discord.Embed(title="You do not have permission to use this command.", value="", color=ctx.author.color)	

		await ctx.send(embed=embed, content=None)	

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def weather(ctx, *, city: str):
    city_name = city
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    channel = ctx.message.channel

    if x["cod"] != "404":
        async with channel.typing():    	
            y = x["main"]
            current_temperature = y["temp"]
            current_temperature_fahrenheit = str(round(current_temperature - 273.15))
            current_pressure = y["pressure"]
            current_humidity = y["humidity"]
            z = x["weather"]

            weather_description = z[0]["description"]
            embed = discord.Embed(title=f"Weather in {city_name}",
                              color=ctx.author.color,
                              timestamp=ctx.message.created_at,)
            embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
            embed.add_field(name="Temperature(C)", value=f"**{current_temperature_fahrenheit}°C**", inline=False)
            embed.add_field(name="Humidity(%)", value=f"**{current_humidity}%**", inline=False)
            embed.add_field(name="Atmospheric Pressure(hPa)", value=f"**{current_pressure}hPa**", inline=False)
            embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
            embed.set_footer(text=f"Command Executed by {ctx.author}", icon_url=ctx.author.avatar_url)


            await channel.send(embed=embed)
    else:
        await channel.send("City not found.")
	

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def ping(ctx):
	start = time()
	em = discord.Embed(title=f'Pong! Client latency: {round(client.latency * 1000)}ms', color=ctx.author.color)
	
	await ctx.send(embed = em, content=None)
	end = time()

	await ctx.channel.purge(limit = 1)

	em = discord.Embed(title=f'Pong! Client latency: {round(client.latency * 1000)}ms | Response time: {(end-start)*1000:,.0f} ms', color=ctx.author.color)

	await ctx.send(embed = em, content=None)

@client.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def serverinfo(ctx):
    mbed = discord.Embed(
        colour=discord.Colour.dark_gold(),
        title=f"{ctx.guild.name}"
    )
    mbed.set_image(url=f"{ctx.guild.icon_url}")
    mbed.add_field(name='Owner', value=f"{ctx.guild.owner}")
    mbed.add_field(name='Region', value=f"{ctx.guild.region}")
    mbed.add_field(name='Member Count', value=f"{ctx.guild.member_count}")
    mbed.add_field(name='Server created At', value=f"{ctx.guild.created_at}")
    mbed.add_field(name='Booster Count', value=f"{ctx.guild.premium_subscription_count}")
    mbed.add_field(name='Description', value=f"{ctx.guild.description}")
    mbed.add_field(name='Max emoji', value=f"{ctx.guild.emoji_limit}")
    mbed.set_footer(text=f"Command Executed by {ctx.author}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=mbed)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def whois(ctx, member: discord.Member):
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

        await ctx.send(embed=embed, content=None)


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def credits(ctx):
    embed = discord.Embed(title="Credits", color=ctx.author.color)

    embed.set_author(name="Nugget2.0", icon_url="https://cdn.discordapp.com/avatars/668988124566781984/5a0927708295e1190e2c1b7df70ebeea.webp?size=1024")

    embed.add_field(name="Created on:", value="Tue, 21 January 2020, 01:19 AM UTC", inline=True)

    embed.add_field(name="Author", value="@SON. YOU DROPPED THE NUGGIES", inline=True)

    embed.add_field(name="Co-Author", value="@JamesBoi.exe")

    embed.set_footer(text="https://github.com/ZachFlatt/NuggetBOT", icon_url="https://cdn.discordapp.com/avatars/668988124566781984/5a0927708295e1190e2c1b7df70ebeea.webp?size=1024")

    await ctx.send(embed=embed, content=None)


###MODERATION / ADMIN COMMANDS###

@client.command(aliases=['c'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def clear(ctx, amount=5):

	if ctx.author.guild_permissions.administrator:
		await ctx.channel.purge(limit = amount)

		em = discord.Embed(title=f"Sucessfully purged {amount} messages", color = ctx.author.color)

		await ctx.send(embed = em, content=None)
	else:
		em = discord.Embed(title="You are missing Manage Messages permission(s) to run this command.", color = ctx.author.color)

		await ctx.send(embed = em, content=None)

@client.command(aliases=['k'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def kick(ctx, member : discord.Member,*,reason):

	if ctx.author.guild_permissions.kick_members:
		await member.send(f"You have been kicked. Reason: {reason}")
		await member.kick(reason=reason)

		em = discord.Embed(title=f"Sucessfully kicked {member}", color = ctx.author.color)

		await ctx.send(embed = em, content=None)
	else:
		em = discord.Embed(title="You are missing `Kick Members` permission(s) to run this command.", color = ctx.author.color)

		await ctx.send(embed = em, content=None)


@client.command(aliases=['b'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def ban(ctx, member : discord.Member,*,reason):

	if ctx.author.guild_permissions.ban_members:
		await member.send(f"You have been banned. Reason: {reason}")
		await member.ban(reason=reason)

		em = discord.Embed(title=f"Sucessfully banned {member}", color = ctx.author.color)

		await ctx.send(embed = em, content=None)
	else:
		em = discord.Embed(title="You are missing `Ban Members` permission(s) to run this command.", color = ctx.author.color)

		await ctx.send(embed = em, content=None)



### ECONOMY COMMANDS ###

mainshop = [{"name":"Experience boost - 100","price":100},
	    {"name":"Experience boost - 1,000","price":1000},
	    {"name":"Experience boost - 10,000","price":10000}]

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def add(ctx):
	em = discord.Embed(title="**Shit! Thats an error!**", description="Event logged to C:/Users/zpfla/Documents/OLD DELL PC/code stuffs/Nugget2/logs/{}.txt".format(time), color=discord.Colour.red())

	await ctx.send(embed=em)


@client.command()
@commands.cooldown(1, 5, commands.BucketType.user) 
async def shop(ctx):
	em = discord.Embed(title="Availible Boosters", color=ctx.author.color)

	for item in mainshop:
		name = item["name"]
		price = item["price"]
		description = None
		em.add_field(name = name, value = f"${price} | {description}")

	em.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)

	await ctx.send(embed = em, content=None)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def buy(ctx,item,amount = 1):
	await open_account(ctx.author)

	res = await buy_this(ctx.author,item,amount)

	if not res[0]:
		if res[1]==1:
			embed = discord.Embed(title="There is no such item by that name")
			await ctx.send(embed = embed, content=None)
		if res[1]==2:
			embed = discord.Embed(title=f"You don't have enough money in your wallet to buy {amount}")
			await ctx.send(embed = embed, content=None)
			return

	embed = discord.Embed(title=f"You just bought {amount} {item}", color = ctx.author.color)

	await ctx.send(embed = embed, content=None)

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def sell(ctx,item,amount = 1):
	if ctx.author.id == zach_id or ctx.author.id == owner_id or ctx.author.id == james_id:
		await open_account(ctx.author)
		res = await sell_this(ctx.author,item,amount)
		if not res[0]:
			if res[1]==1:
				embed = discord.Embed(title="There is no such item by that name")
				await ctx.send(embed = embed, content=None)

		embed = discord.Embed(title=f"You just sold {amount} {item}", color = ctx.author.color)
		await ctx.send(embed = embed, content=None)

@client.command(aliases=['bal'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def balance(ctx):
	await open_account(ctx.author)

	user = ctx.author

	users = await get_bank_data()

	wallet_amt = users[str(user.id)]["wallet"]

	bank_amt = users[str(user.id)]["bank"]

	em = discord.Embed(color = ctx.author.color)
	em.add_field(name = "Wallet balance", value = wallet_amt)
	em.add_field(name = "Bank balance", value = bank_amt)
	em.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)

	await ctx.send(embed = em, content=None)


@client.command()
@commands.cooldown(1, 7200, commands.BucketType.user)
async def beg(ctx):
	await open_account(ctx.author)

	users = await get_bank_data() 

	user = ctx.author

	earnings =  random.randrange(101)

	em = discord.Embed(title=f"Someone gave you {earnings} coins!!", color=ctx.author.color)

	await ctx.send(embed=em, content=None)



	users[str(user.id)]["wallet"] += earnings

	with open("mainbank.json", "w") as f:
		json.dump(users,f)




@client.command(aliases=['dep'])
@commands.cooldown(1, 5, commands.BucketType.user)
async def deposit(ctx, amount = None):
	await open_account(ctx.author)

	if amount == None:
		embed = discord.Embed(title="Please enter the amount", color = ctx.author.color)
		
		await ctx.send(embed = embed, content=None)
		return

	bal = await update_bank(ctx.author)


	amount = int(amount)
	if amount > bal[0]:
		embed = discord.Embed(title="You don't have enough money!", color = ctx.author.color)
		await ctx.send(embed = embed, content=None)
		return
	if amount < 0:
		embed = discord.Embed(title="Amount must be positive!", color = ctx.author.color)
		await ctx.send(embed = embed, content=None)
		return

	await update_bank(ctx.author, -1*amount)
	await update_bank(ctx.author, amount, "bank")

	embed = discord.Embed(title=f"You deposited {amount} coins!", color = ctx.author.color)
	await ctx.send(embed = embed, content=None)	

@client.command()
@commands.cooldown(1, 5, commands.BucketType.user)
async def withdraw(ctx, amount = None):
	await open_account(ctx.author)

	if amount == None:
		embed = discord.Embed(title="Please enter the amount", color = ctx.author.color)
		
		await ctx.send(embed = embed, content=None)
		return

	bal = await update_bank(ctx.author)


	amount = int(amount)
	if amount > bal[1]:
		embed = discord.Embed(title="You don't have enough money!", color = ctx.author.color)
		await ctx.send(embed = embed, content=None)
		return
	if amount < 0:
		embed = discord.Embed(title="Amount must be positive!", color = ctx.author.color)
		await ctx.send(embed = embed, content=None)
		return

	await update_bank(ctx.author, amount)
	await update_bank(ctx.author, -1*amount, "bank")

	embed = discord.Embed(title=f"You withdrew {amount} coins!", color = ctx.author.color)
	await ctx.send(embed = embed, content=None)	



@client.command()
@commands.cooldown(1, 7200, commands.BucketType.user)
async def slots(ctx, amount = None):
	await open_account(ctx.author)

	if amount == None:
		embed = discord.Embed(title="Please enter the amount", color = ctx.author.color)
		
		await ctx.send(embed = embed, content=None)
		return

	bal = await update_bank(ctx.author)


	amount = int(amount)
	if amount > bal[0]:
		embed = discord.Embed(title="You don't have enough money!", color = ctx.author.color)
		await ctx.send(embed = embed, content=None)
		return
	if amount < 0:
		embed = discord.Embed(title="Amount must be positive!", color = ctx.author.color)
		await ctx.send(embed = embed, content=None)
		return		

	final = []
	for i in range(3):
		a = random.choice([":kiwi:", ":strawberry:", ":grapes:"])

		final.append(a)

	await ctx.send(str(final))

	if final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
		await update_bank(ctx.author, + amount)

		embed = discord.Embed(title="Spinning....", color=ctx.author.color)

		a = random.choice([":kiwi:", ":strawberry:", ":grapes:"])

		final.append(a)

		embed.add_field(name=(str(final)), value="** **")

		await ctx.send(embed = embed, content=None)
		

	else:
		await update_bank(ctx.author,-1*amount)

		embed = discord.Embed(title="You Lost!", color=ctx.author.color)

		await ctx.send(embed = embed, content=None)

@client.command()
async def quote(ctx, message):
	await ctx.send(message)

@client.command()
@commands.cooldown(1, 7200, commands.BucketType.user)
async def work(ctx):
	range = random.randrange(300)
	if range >= 70 and range < 120:
		await open_account(ctx.author)

		users = await get_bank_data()

		em = discord.Embed(title=None, description=random.choice([f"God damnit carl! He comes home wasted and steals your wallet shouting you owe him. You never see him again.", 
																	"**You are working at noodle when you notice your boss left her phone at the front desk. Naturally you want to return it to her but you forgot that the floor was wet so you slip and fall on a nearby customer. You land on top of her on the floor like one of those weird sexy movie moments. But sadly she wasnt feeling it. She kicked you so hard you lost your wallet**",
																	"**You cought corona, you have to empty your wallet to pay the hospital bills**"]), color=ctx.author.color)
		
		em.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
		await ctx.send(embed=em, content=None)

		user = ctx.author

		users[str(user.id)]["wallet"] = 0

		with open("mainbank.json", "w") as f:
			json.dump(users,f)	

	else:
		await open_account(ctx.author)

		users = await get_bank_data()

		user = ctx.author

		range = random.randrange(401)
			
		em = discord.Embed(description=random.choice([f"You work as a Bingo Manager and earn :coin: {range}", 
												f"Your ex pays you :coin: {range} to ghost write her online dating profile", 
												f"You work as a high school student with no life. Have :cookie: {range} because we pity you.",
												f"You work as lead camera at PornHub and earn :coin: {range}",
												f"You're broke and desperate. You decide to sell your ass for money. You gain :coin: {range}",
												f"You work as a flatulence smell reduction underwear maker and earn :coin: {range}"]), color=ctx.author.color)
		em.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
		await ctx.send(embed = em, content=None)

		users[str(user.id)]["wallet"] += range

		with open("mainbank.json", "w") as f:
			json.dump(users,f)

@client.command()
async def pay(ctx, user: discord.User, amount):

	em = discord.Embed(description=f"{ctx.author} payed {user} {amount}", color=ctx.author.color)
	em.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)

	await ctx.send(embed=em, content=None)

	await open_account(ctx.author)

	ctx.author[str(user.id)]["wallet"] -1* amount

	await open_account(user)

	user[str(user.id)]["wallet"] += amount






@client.command()
async def source(ctx):
	if ctx.author.id == owner_id or ctx.author.id == zach_id:
		em = discord.Embed(description="Check your dm's", color=ctx.author.color)
		em.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)

		await ctx.send(embed=em, content=None)

		with open("NuggetBot.py", "rb") as file:
			await ctx.author.send("**PLEASE DO NOT SHARE THIS FILE WITH ANYONE**")
			await ctx.author.send(file=discord.File(file, "NuggetBot.py"))

	else:
		em = discord.Embed(description="**You do not have permission to use this command**", color=ctx.author.color)
		em.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)

		await ctx.send(embed = em, content=None)



async def open_account(user):
	
	users = await get_bank_data()

	if str(user.id) in users:
		return False
	else:
		users[str(user.id)] = {}
		users[str(user.id)]["wallet"] = 0
		users[str(user.id)]["bank"] = 0

	with open("mainbank.json", "w") as f:
		json.dump(users,f)
	return True

async def get_bank_data():
	with open("mainbank.json", "r") as f:
		users = json.load(f)
	
	return users

async def update_bank(user,change = 0,mode = "wallet"):
	users = await get_bank_data()

	users[str(user.id)][mode] += change

	with open("mainbank.json", "w") as f:
		json.dump(users,f)

	bal = [users[str(user.id)]["wallet"], users[str(user.id)]["bank"]]
	return bal




@client.command()
async def bag(ctx):
	await open_account(ctx.author)
	user = ctx.author
	users = await get_bank_data()

	try:
		bag = users[str(user.id)]["bag"]
	except:
		bag = []

	em = discord.Embed(title = "Bag", color=ctx.author.color)
	for item in bag:
		name = item["item"]
		amount = item["amount"]

		em.add_field(name = name, value = amount)
		
	await ctx.send(embed = em, content=None)

async def sell_this(user,item_name,amount):
	item_name = item_name.lower()
	name_ = None
	for item in users[str(user.id)]["bag"]:
		name = item["name"].lower()
		if name == item_name:
			name_ = name
			price = item["price"]
			break
	if name_ == None:
		return [False,1]

	cost = price*amount

	users = await get_bank_data()

	bal = await update_bank(user)

	if bal[0]<cost:
		return[False,2]

	try:
		index = 0
		t = None
		for thing in users[str(user.id)]["bag"]:
			n = thing["item"]
			if n == item_name:
				old_amt = thing["amount"]
				new_amt = old_amt - amount
				users[str(user.id)]["bag"][index]["amount"] = new_amt
				t = 1
				break
			index+=1
		if t == None:
			obj = {"item":item_name , "amount" : amount}
			users[str(user.id)]["bag"].append(obj)
	except:
		obj = {"item":item_name, "amount" : amount}
		users[str(user.id)]["bag"] = [obj]

	with open("mainbank.json","w") as f:
		json.dump(users,f)

	await update_bank(user,cost*+1, "wallet")

	return [True, "Worked"]


async def buy_this(user,item_name,amount):
	item_name = item_name.lower()
	name_ = None
	for item in mainshop:
		name = item["name"].lower()
		if name == item_name:
			name_ = name
			price = item["price"]
			break
	if name_ == None:
		return [False,1]

	cost = price*amount

	users = await get_bank_data()

	bal = await update_bank(user)

	if bal[0]<cost:
		return[False,2]

	try:
		index = 0
		t = None
		for thing in users[str(user.id)]["bag"]:
			n = thing["item"]
			if n == item_name:
				old_amt = thing["amount"]
				new_amt = old_amt + amount
				users[str(user.id)]["bag"][index]["amount"] = new_amt
				t = 1
				break
			index+=1
		if t == None:
			obj = {"item":item_name , "amount" : amount}
			users[str(user.id)]["bag"].append(obj)
	except:
		obj = {"item":item_name, "amount" : amount}
		users[str(user.id)]["bag"] = [obj]

	with open("mainbank.json","w") as f:
		json.dump(users,f)

	await update_bank(user,cost*-1, "wallet")

	return [True, "Worked"]

@client.event
async def on_message(message):
    if not message.author.bot:
        #print('function load')
        with open('level.json','r') as f:
            users = json.load(f)
            #print('file load')
        await update_data(users, message.author,message.guild)
        await add_experience(users, message.author, 4, message.guild)
        await level_up(users, message.author,message.channel, message.guild)

        with open('level.json','w') as f:
            json.dump(users, f)
    await client.process_commands(message)


async def update_data(users, user,server):
    if not str(server.id) in users:
        users[str(server.id)] = {}
        if not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1
    elif not str(user.id) in users[str(server.id)]:
            users[str(server.id)][str(user.id)] = {}
            users[str(server.id)][str(user.id)]['experience'] = 0
            users[str(server.id)][str(user.id)]['level'] = 1

async def add_experience(users, user, exp, server):
  users[str(user.guild.id)][str(user.id)]['experience'] += exp

async def level_up(users, user, channel, server):
  experience = users[str(user.guild.id)][str(user.id)]['experience']
  lvl_start = users[str(user.guild.id)][str(user.id)]['level']
  lvl_end = int(experience ** (1/4))
  if str(user.guild.id) != '757383943116030074':
    if lvl_start < lvl_end:
      await channel.send('{} has leveled up to Level {}'.format(user.mention, lvl_end))
      users[str(user.guild.id)][str(user.id)]['level'] = lvl_end


@client.command(aliases = ['rank','lvl', 'Level'])
async def level(ctx,user=None, member: discord.Member = None):

    if not member:
        user = ctx.message.author
        with open('level.json','r') as f:
            users = json.load(f)
        lvl = users[str(ctx.guild.id)][str(user.id)]['level']
        exp = users[str(ctx.guild.id)][str(user.id)]['experience']

        embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP " ,color = ctx.author.color)
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)
    else:
      with open('level.json','r') as f:
          users = json.load(f)
      lvl = users[str(ctx.guild.id)][str(member.id)]['level']
      exp = users[str(ctx.guild.id)][str(member.id)]['experience']
      embed = discord.Embed(title = 'Level {}'.format(lvl), description = f"{exp} XP" ,color = ctx.author.color)
      embed.set_author(name = member, icon_url = member.avatar_url)

      await ctx.send(embed = embed)




client.run(TOKEN)
