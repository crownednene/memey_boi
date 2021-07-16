# memey_boi.py

import os
import discord
import edit_picture

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
path = os.getcwd()

#define the command prefix
bot = commands.Bot(command_prefix='$')



#check for event
@client.event
#makes the bot online on discord
async def on_ready():
	print('We have logged in as {0.user}.'.format(client))


#check for event
@client.event
#check for message sent on discord
async def on_message(message):
	#print in console => name of the channel that had the message: author of message (username#id):author of message (nickname): content of message
	print(f"{message.channel.name}: {message.author}: {message.author.name}: {message.content}")
	
	#if the bot sent a message, ignore it
	if message.author == client.user:
		return

	#if someone types $hello, reply with "fuck off"
	if message.content.startswith('$hi'):
		await message.channel.send('fuck off')
		await client.change_presence(status=discord.Status.idle, activity="you knoooww...")

	if "anata wa botto desu ka?" == message.content.lower():
		await message.channel.send('はい')

	if "send nudes" == message.content.lower():
		await client.change_presence(status=discord.Status.online, activity=discord.Game("with nudes"))
		channel = client.get_channel(message.channel.id)
		edit_picture.write_blank()
		await channel.send(file=discord.File('text.png'))

	#if someone types $byebitch, reply with "wtvr loser" and disconnect
	if "bitch bye" == message.content.lower():
		await message.channel.send('wtvr loser')
		await client.close()

	if "what" == message.content.lower():
		channel = client.get_channel(message.channel.id)
		edit_picture.find_image()
		await message.channel.send('found dog')
		#await channel.send()

	if "happy birthday" in message.content.lower() or "hap birth" in message.content.lower():
		await client.change_presence(status=discord.Status.online, activity=discord.Game("birthday wishes"))
		channel = client.get_channel(message.channel.id)
		edit_picture.quinns_birthday()
		await channel.send(file=discord.File(path + '/imageDownload/buttigieg/generatedButt.jpg'))

client.run(TOKEN)


@bot.command()
async def test(ctx, *args):
	await ctx.send(format(len(args), ' '.join(args)))

async def hello(ctx, arg):
	await ctx.send("sup dude")

async def bye(ctx, arg):
	bot.close()

bot.run(TOKEN)