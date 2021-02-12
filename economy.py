import discord
from discord.ext import commands
import datetime
import pypokedex
import cog_serverinfo

import random
import json
import os

TOKEN = 'NjY4OTg4MTI0NTY2NzgxOTg0.XiZRvg.CKej4DECCsw92EHN9pKsDHZwjgk'

client = commands.Bot(command_prefix = '-')

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
    
    #await client.change_presence(activity=discord.Game(name='-help || Version 2.4'.format(mem)))

    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="-help || Version 2.4"))

client.remove_command("help")


@client.command()
async def balance(ctx):
	await open_account(ctx.author)

	user = ctx.author

	users = await get_bank_data()

	wallet_amt = users[str(user.id)]["wallet"]
	bank_amt = usesr[str(user.id)]["bank"]

	em = discord.Embed(title = f"{ctx.author.name}'s balance", color = discord.Color.purple)

	em.add_field(name = "Wallet balance", value = wallet_amt)

	em.add_field(name = "Bank balance", value = bank_amt)

	await ctx.send(embed=em, content=None)

@client.command()
async def beg(ctx):
	await open_account(ctx.author)

	users = await get_bank_data()

	user = ctx.author

	earnings = random.randrange(101)

	await ctx.send(f"Someone gave you {earnings} coins!!")

	users[str(user.id)]["wallet"] += earnings

	with open("mainbank.json", "w") as f:
		json.dump(sers,f)





async def open_account(user):

	users = await get_bank_data()

	if str(user.id) in users:
		return False
	else:
		user[str(user.id)] = {}
		user[str(user.id)]["wallet"] = 0
		user[str(user.id)]["bank"] = 0

	with open("mainbank.json", "w") as f:
		json.dump(users,f)
	return True

async def get_bank_data():
	with open("mainbank.json", "r") as f:
		users = json.load(f)

	return users

client.run(TOKEN)