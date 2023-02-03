import discord
from discord.ext import commands
from myserver import server_on

TOKEN = "MTA2NDA5MTQyMDQ2NzY3NTIxNg.GxIj0H.YnxpN3Taidjini5xZb6qyEWNbjlx3qiIOILxj8" # ganti dengan token bot anda

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot {} telah online'.format(bot.user))

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, {}! Jangan lupa subscribenya ya :)'.format(ctx.author.name.title()))

server_on()
bot.run(MTA2NDA5MTQyMDQ2NzY3NTIxNg.GxIj0H.YnxpN3Taidjini5xZb6qyEWNbjlx3qiIOILxj8)
