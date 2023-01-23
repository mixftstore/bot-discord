import discord
from discord.ext import commands
from myserver import server_on

TOKEN = "MTA2NzA4MTU0NjgyNzMxMzIwMg.G93vcs.rmfkJHEjxWFvxVwRYKOgeWxjQJ6xeHnsBYc_EQ" # ganti dengan token bot anda

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

@bot.event
async def on_ready():
    print('Bot {} telah online'.format(bot.user))

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, {}! Jangan lupa subscribenya ya :)'.format(ctx.author.name.title()))

server_on()
bot.run(MTA2NzA4MTU0NjgyNzMxMzIwMg.G93vcs.rmfkJHEjxWFvxVwRYKOgeWxjQJ6xeHnsBYc_EQ)
