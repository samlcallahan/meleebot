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

@bot.command(aliases=["meleelibrary","melee_library","themeleelibrary","the_melee_library"])
async def library(ctx):
    await ctx.send("https://www.meleelibrary.com/")

@bot.command(aliases=["relative_shields","relativeshields","shieldsizes","shield_size","shieldsize"])
async def shield_sizes(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/173202700710707200/547105310251155483/image0.png")

@bot.command(aliases=["fox_fox_cg","foxdittocg","fox_ditto_chaingrab","foxdittochaingrab"])
async def fox_ditto_cg(ctx):
    await ctx.send("https://smashboards.com/threads/fox-ditto-true-chaingrab-percents-data-2018.462429/")

@bot.command(aliases=["drilladvantage","drilladv","drill_advantage","fox_drill_adv","foxdrillladv","fox_drill_advantage","foxdrilladvantage","drill_on_hit","drillonhit"])
async def drill_adv(ctx):
    await ctx.send("https://docs.google.com/spreadsheets/d/1KZ5F8nEpNsY1NHDx91Aeq-3IeUAFFhgTOGf9h3kuP1I/edit?usp=sharing")

@bot.command(aliases=["20XX_shortcuts","20XX_codes","20XX_cheatsheet","20XX"])
async def hackpack_cheatsheet(ctx):
    await ctx.send("http://i.imgur.com/vLoGO9O.png")

@bot.command(aliases=["savestates","savestate_explained","savestates_explanation","savestate_explanation"])
async def savestates_explained(ctx):
    await ctx.send("https://www.reddit.com/r/SSBM/comments/6gkgol/406_20xx_save_states_explained_text_form/")

@bot.command(aliases=["beginnerneutral","beginner_neutral"])
async def neutral(ctx):
    await ctx.send("https://pastebin.com/MBWLNRwp")
bot.run(TOKEN)