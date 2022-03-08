from config import token
from discord.ext import commands
from myserver import server

TOKEN = token()

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Bot {} telah online'.format(bot.user))

@bot.command()
async def hello(ctx):
    await ctx.send('Hello, {}! Jangan lupa subscribenya ya :)'.format(ctx.author.name.title()))

bot.run(TOKEN)