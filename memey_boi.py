# memey_boi.py

import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('CLIENT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
	print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('$hello'):
		await message.channel.send('fuck off')

client.run('NzIyOTk0Nzk4NjcxMTY3NTkx.XurWvg.toVmJMtJjmZ0E5biu37f7LL9kak')