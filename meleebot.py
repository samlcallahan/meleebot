# Work with Python 3.6
import discord
from discord.ext import commands

TOKEN_FILE = open("token.txt","r")
TOKEN = TOKEN_FILE.read()

description = " A bot to serve technical documentation and frame data about Super Smash Bros. Melee to Discord users."
bot = commands.Bot(command_prefix='!',description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def hello(ctx):
    msg = 'Hello {0.author.mention}'.format(ctx.message)
    await ctx.send(msg)

@bot.command(aliases=["fox_cc"])
async def foxcc(ctx):
    await ctx.send("https://drive.google.com/open?id=1VLO23ZVPmUcleKMuzJpSs71muvqoCUNiXIpxXZ5GXqk")

@bot.command(aliases=["author","creator"])
async def dev(ctx):
    await ctx.send("Brought to you by cagliostro9")

bot.run(TOKEN)