# memey_boi.py
import os
import edit_picture

import discord

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

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
	if message.content.startswith('$hello'):
		await message.channel.send('fuck off')
		await client.change_presence(status=discord.Status.idle, activity=game)

	if "anata wa botto desu ka?" == message.content.lower():
		await message.channel.send('はい')

	if "send nudes" == message.content.lower():
		await client.change_presence(status=discord.Status.online, activity=discord.Game("with nudes"))
		channel = client.get_channel(message.channel.id)
		print(f"{channel}")
		await channel.send(file=discord.File('text.png'))

	#if someone types $byebitch, reply with "wtvr loser" and disconnect
	if "$byebitch" == message.content.lower():
		await message.channel.send('wtvr loser')
		await client.close()

	if "what" == message.content.lower():
		edit_picture.find_image()
		await channel.send()

client.run(TOKEN)