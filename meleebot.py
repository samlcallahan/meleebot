# Work with Python 3.6
import discord
from discord.ext import commands

TOKEN_FILE = open("token.txt","r")
TOKEN = TOKEN_FILE.read()
client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)
    if message.content.startswith('!dev'):
        await message.channel.send("brought to you by cagliostro9")
    if message.content.startswith('!foxcc'):
        await message.channel.send('https://drive.google.com/open?id=1VLO23ZVPmUcleKMuzJpSs71muvqoCUNiXIpxXZ5GXqk')
    if message.content.startswith('!help'):
        await message.author.send('help goes here eventually')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)